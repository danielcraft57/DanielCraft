#!/usr/bin/env python3
"""
Système de build pour générer les pages HTML à partir de templates et includes.

Ce script :
1. Lit les fichiers source dans src/
2. Remplace les includes et variables
3. Génère les pages finales dans le dossier racine

Usage:
    python3 build.py              # Build toutes les pages
    python3 build.py --watch      # Mode watch (rebuild automatique)
    python3 build.py index        # Build une page spécifique
"""

import html
import os
import re
import sys
import json
import shutil
from pathlib import Path
from typing import Dict, Optional, List
from datetime import datetime

# Configuration
BASE_DIR = Path(__file__).parent
SRC_DIR = BASE_DIR / 'src'
INCLUDES_DIR = SRC_DIR / 'includes'
TEMPLATES_DIR = SRC_DIR / 'templates'
PAGES_DIR = SRC_DIR / 'pages'
DATA_DIR = SRC_DIR / 'data'
PROJECTS_JSON = DATA_DIR / 'projects.json'
READMES_DIR = DATA_DIR / 'readmes'
# Dossier de sortie par défaut : dist/ (peut être modifié via --output)
OUTPUT_DIR = BASE_DIR / 'dist'
# Base URL du site (utilisée pour canoniques/OG/sitemaps).
# Pour éviter toute donnée perso en dur, configure via variable d'environnement :
#   SITE_BASE="https://ton-domaine.com"
SITE_BASE = os.environ.get('SITE_BASE', 'https://example.com')

# Libelles categories et statuts (pages projet)
CATEGORY_LABELS = {'web': 'Web', 'tools': 'Outils', 'mobile': 'Mobile', 'iot': 'IoT', 'specialized': 'Specialise', 'learning': 'Apprentissage', 'desktop': 'Desktop'}
STATUS_LABELS = {'active': 'Actif', 'archived': 'Archive'}

# Pages statiques pour le sitemap (path, changefreq, priority)
SITEMAP_PAGES = [
    ('/', 'weekly', '1.0'),
    ('/autres-prestations', 'monthly', '0.8'),
    ('/processus', 'monthly', '0.8'),
    ('/metz', 'monthly', '0.8'),
    ('/portfolio', 'monthly', '0.7'),
    ('/projets', 'monthly', '0.6'),
    ('/statistiques', 'monthly', '0.5'),
    ('/mentions-legales', 'yearly', '0.3'),
    ('/cgv', 'yearly', '0.3'),
    ('/cgu', 'yearly', '0.3'),
    ('/politique-confidentialite', 'yearly', '0.3'),
]

# Variables par défaut
DEFAULT_VARS = {
    'page_title': 'Loïc DANIEL - Développeur Full-Stack TypeScript Freelance',
    'page_description': 'Développeur Full-Stack TypeScript freelance avec plus de 7 ans d\'expérience.',
    'page_keywords': 'développeur freelance, full-stack, TypeScript, React, Node.js',
    'site_base': SITE_BASE,
    'page_url': f'{SITE_BASE}/',
    # Image OG par défaut (home) - architecture dediee dans assets/images/og/
    'og_image': f'{SITE_BASE}/assets/images/og/home-1200x630.jpg',
    'og_type': 'website',
    'current_page': '',
    'page_scripts': [],
    'extra_css': None,
    'blog_enabled': True
}


class TemplateEngine:
    """Moteur de template simple avec support includes et variables."""
    
    def __init__(self, base_dir: Path):
        self.base_dir = base_dir
        self.includes_cache = {}
    
    def load_include(self, include_path: str) -> str:
        """Charge un fichier include avec cache."""
        if include_path in self.includes_cache:
            return self.includes_cache[include_path]
        
        full_path = self.base_dir / include_path
        if not full_path.exists():
            print(f"[WARN] Include non trouve : {include_path}")
            return f'<!-- Include manquant : {include_path} -->'
        
        content = full_path.read_text(encoding='utf-8')
        self.includes_cache[include_path] = content
        return content

    def process_includes(self, content: str, vars_dict: Dict) -> str:
        """Traite les directives {% include %}."""
        pattern = r'\{%\s*include\s+["\']([^"\']+)["\']\s*%\}'

        def replace_include(match):
            include_path = match.group(1)
            include_content = self.load_include(include_path)
            # Traite récursivement les includes dans le fichier inclus
            include_content = self.process_includes(include_content, vars_dict)
            # Remplace les variables dans l'include
            include_content = self.replace_variables(include_content, vars_dict)
            return include_content

        max_iterations = 20
        for _ in range(max_iterations):
            new_content = re.sub(pattern, replace_include, content)
            if new_content == content:
                break
            content = new_content

        return content

    def replace_variables(self, content: str, vars_dict: Dict) -> str:
        """Remplace les variables {{variable}}."""

        def replace_var(match):
            var_name = match.group(1)
            value = vars_dict.get(var_name, '')

            return str(value) if value is not None else ''

        # Remplace {{variable}}
        content = re.sub(r'\{\{(\w+)\}\}', replace_var, content)

        # Traite les conditions {% if %}
        content = self.process_conditions(content, vars_dict)

        return content

    def process_conditions(self, content: str, vars_dict: Dict) -> str:
        """Traite les conditions {% if %} {% else %} {% endif %}."""
        # Pattern pour {% if var == "value" %} ... {% else %} ... {% endif %}
        pattern1 = r'\{%\s*if\s+(\w+)\s*==\s*["\']([^"\']+)["\']\s*%\}(.*?)(?:\{%\s*else\s*%\}(.*?))?\{%\s*endif\s*%\}'

        # Pattern pour {% if var %} ... {% else %} ... {% endif %}
        pattern2 = r'\{%\s*if\s+(\w+)\s*%\}(.*?)(?:\{%\s*else\s*%\}(.*?))?\{%\s*endif\s*%\}'

        def replace_condition1(match):
            var_name = match.group(1)
            expected_value = match.group(2)
            if_content = match.group(3) or ''
            else_content = match.group(4) or ''
            actual_value = vars_dict.get(var_name, '')

            if str(actual_value) == expected_value:
                return if_content
            return else_content

        def replace_condition2(match):
            var_name = match.group(1)
            if_content = match.group(2) or ''
            else_content = match.group(3) or ''
            actual_value = vars_dict.get(var_name, '')

            # Vérifie si la variable existe et est "truthy"
            if actual_value and actual_value != 'False' and actual_value != 'false':
                if isinstance(actual_value, list) and len(actual_value) > 0:
                    return if_content
                elif not isinstance(actual_value, list):
                    return if_content
            return else_content

        max_iterations = 10
        for _ in range(max_iterations):
            new_content = re.sub(pattern1, replace_condition1, content, flags=re.DOTALL)
            new_content = re.sub(pattern2, replace_condition2, new_content, flags=re.DOTALL)
            if new_content == content:
                break
            content = new_content

        return content

    def render(self, template_path: Path, vars_dict: Dict) -> str:
        """Rend un template avec les variables données."""
        if not template_path.exists():
            raise FileNotFoundError(f"Template non trouvé : {template_path}")

        content = template_path.read_text(encoding='utf-8')

        # Traite les includes
        content = self.process_includes(content, vars_dict)

        # Remplace les variables
        content = self.replace_variables(content, vars_dict)

        return content


def generate_robots_txt(output_dir: Path) -> None:
    """
    Genere robots.txt dans dist/ avec des URLs basees sur SITE_BASE.

    Ca evite de versionner un domaine "reel" dans le repo, tout en ayant des
    sitemaps absolus corrects au moment du build/deploiement.
    """
    base = SITE_BASE.rstrip('/')
    content = (
        "User-agent: *\n"
        "Allow: /\n"
        "\n"
        "# Sitemap\n"
        f"Sitemap: {base}/sitemap.xml\n"
        f"Sitemap: {base}/blog/sitemap-blog.xml\n"
        "\n"
        "# Autoriser le blog\n"
        "Allow: /blog/\n"
        "\n"
        "# Autoriser les assets\n"
        "Allow: /assets/\n"
    )
    (output_dir / 'robots.txt').write_text(content, encoding='utf-8')


def load_page_config(page_name: str) -> Dict:
    """Charge la configuration d'une page depuis src/pages/."""
    config_file = PAGES_DIR / f"{page_name}.json"
    
    if config_file.exists():
        with open(config_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    return {}


def _to_absolute_url(url_or_path: str) -> str:
    """
    Convertit un chemin ou une URL en URL absolue basee sur SITE_BASE.

    Règles :
    - si c'est deja une URL http(s), on la retourne telle quelle (mais on remplace
      l'eventuel domaine historique par SITE_BASE si on detecte '/assets/' ou un path local)
    - si ca commence par '/', on prefixe avec SITE_BASE
    - sinon, on prefixe avec SITE_BASE + '/'
    """
    if not url_or_path:
        return url_or_path

    base = SITE_BASE.rstrip('/')
    s = url_or_path.strip()

    if s.startswith('http://') or s.startswith('https://'):
        # Si l'URL contient un path local du site, on peut rebaser sur SITE_BASE
        try:
            from urllib.parse import urlparse

            p = urlparse(s)
            if p.path.startswith('/'):
                return base + p.path + (('?' + p.query) if p.query else '') + (('#' + p.fragment) if p.fragment else '')
        except Exception:
            return s
        return s

    if s.startswith('/'):
        return base + s
    return base + '/' + s


def _normalize_page_meta(vars_dict: Dict, page_name: str) -> None:
    """
    Normalise `page_url` et `og_image` pour eviter les domaines en dur.
    """
    # Canonical: si absent, on derive d'apres la page
    page_url = vars_dict.get('page_url')
    if not page_url:
        if page_name == 'index':
            page_url = '/'
        else:
            page_url = '/' + page_name
        vars_dict['page_url'] = page_url

    vars_dict['page_url'] = _to_absolute_url(str(vars_dict.get('page_url', '')))

    og_image = vars_dict.get('og_image')
    if og_image:
        vars_dict['og_image'] = _to_absolute_url(str(og_image))


def load_projects() -> List[Dict]:
    """Charge la liste des projets depuis src/data/projects.json. Lance le script de gen si absent."""
    if not PROJECTS_JSON.exists():
        script = BASE_DIR / 'scripts' / 'build_projects_data.py'
        if script.exists():
            try:
                import subprocess
                subprocess.run(
                    [sys.executable, str(script)],
                    cwd=str(BASE_DIR),
                    capture_output=True,
                    timeout=30,
                    check=True
                )
            except Exception as e:
                print(f"[WARN] Gen projects.json : {e}")
        if not PROJECTS_JSON.exists():
            return []
    with open(PROJECTS_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)


def _markdown_to_html_fallback(raw: str) -> str:
    """Conversion Markdown -> HTML sans dependance externe (fallback si 'markdown' absent)."""
    out = raw
    # Fenced code blocks (```...``` ou ```lang...```)
    def _code_block(m):
        lang = (m.group(1) or '').strip()
        code = html.escape(m.group(2))
        cls = f' class="language-{lang}"' if lang else ''
        return f'<pre><code{cls}>{code}</code></pre>'
    out = re.sub(r'```(\w*)\n(.*?)```', _code_block, out, flags=re.DOTALL)
    # Inline code (echappe le HTML dans le code)
    out = re.sub(r'`([^`]+)`', lambda m: '<code>' + html.escape(m.group(1)) + '</code>', out)
    # Liens [text](url)
    out = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>', out)
    # Gras **...**
    out = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', out)
    out = re.sub(r'__([^_]+)__', r'<strong>\1</strong>', out)
    # Italique *...*
    out = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', out)
    out = re.sub(r'_([^_]+)_', r'<em>\1</em>', out)
    # Titres (h6 -> h1 pour garder l'ordre)
    for i in range(6, 0, -1):
        prefix = '#' * i
        out = re.sub(r'^' + prefix + r'\s+(.+)$', f'<h{i}>\\1</h{i}>', out, flags=re.MULTILINE)
    # Ligne horizontale
    out = re.sub(r'^---+$', '<hr>', out, flags=re.MULTILINE)
    out = re.sub(r'^\*\*\*+$', '<hr>', out, flags=re.MULTILINE)
    # Blockquote > ...
    lines = out.split('\n')
    result = []
    in_blockquote = False
    for line in lines:
        if line.strip().startswith('>'):
            content = line.lstrip('> ').strip()
            if not in_blockquote:
                result.append('<blockquote>')
                in_blockquote = True
            result.append(content + ' ')
        else:
            if in_blockquote:
                result.append('</blockquote>')
                in_blockquote = False
            result.append(line)
    if in_blockquote:
        result.append('</blockquote>')
    out = '\n'.join(result)
    # Listes non ordonnees (- ou *)
    out = re.sub(r'^[\*\-]\s+(.+)$', r'<li>\1</li>', out, flags=re.MULTILINE)
    out = re.sub(r'(<li>.*?</li>\n?)+', lambda m: '<ul>' + m.group(0) + '</ul>', out, flags=re.DOTALL)
    # Listes ordonnees 1. ...
    out = re.sub(r'^\d+\.\s+(.+)$', r'<li>\1</li>', out, flags=re.MULTILINE)
    # Paragraphes: blocs de lignes non vides entoures de <p> si pas deja une balise block
    parts = re.split(r'\n\s*\n', out)
    final = []
    for p in parts:
        p = p.strip()
        if not p:
            final.append(p)
            continue
        if p.startswith('<') and re.match(r'^<(?:h[1-6]|ul|ol|pre|blockquote|hr|table|p)', p):
            final.append(p)
        else:
            if not p.startswith('<'):
                p = '<p>' + p + '</p>'
            final.append(p)
    out = '\n'.join(final)
    return out


def _readme_to_html(slug: str) -> str:
    """Convertit le README Markdown en HTML si le fichier existe. Retourne une chaine vide sinon."""
    path = READMES_DIR / f'{slug}.md'
    if not path.exists():
        path_legacy = READMES_DIR / f'{slug}-l57.md'
        path = path_legacy if path_legacy.exists() else path
    if not path.exists():
        return ''
    try:
        raw = path.read_text(encoding='utf-8')
    except Exception:
        return ''
    try:
        import markdown
        html_out = markdown.markdown(
            raw,
            extensions=['fenced_code', 'tables', 'nl2br', 'sane_lists'],
            extension_configs={'fenced_code': {}}
        )
        return html_out or ''
    except ImportError:
        return _markdown_to_html_fallback(raw)
    except Exception:
        return _markdown_to_html_fallback(raw)


def _project_prev_next_html(projects: List[dict], current_slug: str) -> str:
    """Genere le bloc HTML projet precedent / suivant (ordre de la liste)."""
    idx = next((i for i, pr in enumerate(projects) if (pr.get('slug') or pr.get('id', '')) == current_slug), -1)
    if idx < 0:
        return ''
    prev_p = projects[idx - 1] if idx > 0 else None
    next_p = projects[idx + 1] if idx < len(projects) - 1 else None
    parts = ['<div class="prev-next-links">']
    if prev_p:
        s = prev_p.get('slug') or prev_p.get('id', '')
        t = prev_p.get('title', s)
        parts.append(f'<a href="/projets/{s}" class="prev-next-link prev-link"><i class="fas fa-arrow-left" aria-hidden="true"></i> {t}</a>')
    else:
        parts.append('<span class="prev-next-link prev-link empty"></span>')
    if next_p:
        s = next_p.get('slug') or next_p.get('id', '')
        t = next_p.get('title', s)
        parts.append(f'<a href="/projets/{s}" class="prev-next-link next-link">{t} <i class="fas fa-arrow-right" aria-hidden="true"></i></a>')
    else:
        parts.append('<span class="prev-next-link next-link empty"></span>')
    parts.append('</div>')
    return '\n'.join(parts)


def _project_recommendations_html(projects: List[dict], current_project: dict, max_n: int = 4) -> str:
    """Genere le bloc HTML des projets recommandes (meme categorie en priorite, puis autres)."""
    current_slug = current_project.get('slug') or current_project.get('id', '')
    category = current_project.get('category', '')
    same_cat = [pr for pr in projects if (pr.get('slug') or pr.get('id', '')) != current_slug and (pr.get('category') or '') == category]
    others = [pr for pr in projects if (pr.get('slug') or pr.get('id', '')) != current_slug and pr not in same_cat]
    recommended = same_cat[:max_n] + [pr for pr in others if pr not in same_cat][:max_n - len(same_cat)]
    recommended = recommended[:max_n]
    if not recommended:
        return ''
    lines = ['<h2 class="projet-recommendations-title">Projets suggeres</h2>', '<div class="projet-recommendations-grid">']
    for pr in recommended:
        s = pr.get('slug') or pr.get('id', '')
        title = pr.get('title', s)
        desc = (pr.get('description') or '')[:120] + ('...' if len(pr.get('description') or '') > 120 else '')
        cat_label = CATEGORY_LABELS.get(pr.get('category', ''), pr.get('category', 'Projet'))
        lines.append(f'''<a href="/projets/{s}" class="projet-card">
            <span class="projet-card-type">{cat_label}</span>
            <h3 class="projet-card-title">{title}</h3>
            <p class="projet-card-excerpt">{desc}</p>
        </a>''')
    lines.append('</div>')
    return '\n'.join(lines)


def build_project_pages(template_engine: TemplateEngine, output_dir: Path) -> List[str]:
    """Genere les pages HTML pour chaque projet dans output_dir/projets/. Retourne la liste des slugs."""
    projects = load_projects()
    if not projects:
        print("[WARN] Aucun projet dans projects.json - pages projet non generees")
        return []
    out_projets = output_dir / 'projets'
    out_projets.mkdir(parents=True, exist_ok=True)
    template_path = TEMPLATES_DIR / 'base.html'
    content_path = PAGES_DIR / 'projet.html'
    if not content_path.exists():
        print("[WARN] src/pages/projet.html manquant")
        return []
    content_tpl = content_path.read_text(encoding='utf-8')
    slugs = []
    for p in projects:
        slug = p.get('slug') or p.get('id', '')
        if not slug:
            continue
        techs = p.get('technologies') or []
        tech_html = ''.join(f'<span class="tech-tag">{t}</span>' for t in techs)
        img_url = p.get('imageUrl') or ''
        if img_url and not img_url.startswith('http'):
            img_url = SITE_BASE + '/' + img_url
        readme_html = _readme_to_html(slug)
        prev_next_html = _project_prev_next_html(projects, slug)
        recommendations_html = _project_recommendations_html(projects, p)
        vars_dict = DEFAULT_VARS.copy()
        vars_dict.update({
            'current_page': 'projet',
            'page_title': f"{p.get('title', slug)} - Projets | DanielCraft",
            'page_description': (p.get('description') or '')[:160],
            'page_keywords': ', '.join(techs[:5]) if techs else 'projet, open source',
            'page_url': f"{SITE_BASE}/projets/{slug}",
            'og_image': img_url or DEFAULT_VARS['og_image'],
            'og_type': 'website',
            'schema_type': 'project',
            'page_content': '',  # sera remplace par le rendu du fragment
            'project_title': p.get('title', slug),
            'project_description': p.get('description') or '',
            'project_category_label': CATEGORY_LABELS.get(p.get('category', ''), p.get('category', 'Projet')),
            'project_technologies_html': tech_html,
            'project_year': p.get('year', ''),
            'project_account': p.get('account', ''),
            'project_licence': p.get('licence') or '',
            'project_status': p.get('status', ''),
            'project_status_label': STATUS_LABELS.get(p.get('status', ''), p.get('status', '')),
            'project_image_url': '/' + p.get('imageUrl', '') if p.get('imageUrl') and not p.get('imageUrl', '').startswith('http') else (p.get('imageUrl') or ''),
            'project_github_url': p.get('github_url') or '',
            'project_stars': p.get('stars', 0),
            'project_forks': p.get('forks', 0),
            'project_language': p.get('language') or '',
            'project_readme_html': readme_html,
            'project_prev_next_html': prev_next_html,
            'project_recommendations_html': recommendations_html,
        })
        content_rendered = template_engine.replace_variables(content_tpl, vars_dict)
        content_rendered = template_engine.process_includes(content_rendered, vars_dict)
        vars_dict['page_content'] = content_rendered
        vars_dict['page_scripts_content'] = '<script src="/assets/js/main.js" defer></script>\n<link rel="preload" href="/assets/js/main.js" as="script">'
        html_output = template_engine.render(template_path, vars_dict)
        (out_projets / f'{slug}.html').write_text(html_output, encoding='utf-8')
        slugs.append(slug)
    print(f"[OK] {len(slugs)} page(s) projet genere(s) dans {out_projets}")
    return slugs


def build_page(page_name: str, template_engine: TemplateEngine):
    """Build une page HTML."""
    # Charge la config de la page
    page_config = load_page_config(page_name)
    
    # Fusionne avec les valeurs par défaut
    vars_dict = DEFAULT_VARS.copy()
    vars_dict.update(page_config)
    vars_dict['current_page'] = page_name

    # Normalise canonical/OG a partir de SITE_BASE
    _normalize_page_meta(vars_dict, page_name)
    
    # Génère le contenu des scripts
    scripts = vars_dict.get('page_scripts', [])
    if scripts:
        scripts_content = '\n'.join([
            f'<script src="assets/js/{script}" defer></script>\n<link rel="preload" href="assets/js/{script}" as="script">'
            for script in scripts
        ])
    else:
        scripts_content = '<script src="assets/js/main.js" defer></script>\n<link rel="preload" href="assets/js/main.js" as="script">'
    vars_dict['page_scripts_content'] = scripts_content
    
    # Détermine le template à utiliser
    template_name = page_config.get('template', 'base.html')
    template_path = TEMPLATES_DIR / template_name
    
    if not template_path.exists():
        print(f"[ERREUR] Template non trouve : {template_name}")
        return False
    
    # Charge le contenu de la page
    page_content_file = PAGES_DIR / f"{page_name}.html"
    if page_content_file.exists():
        page_content = page_content_file.read_text(encoding='utf-8')
        vars_dict['page_content'] = page_content
    else:
        print(f"[WARN] Contenu de page non trouve : {page_content_file}")
        vars_dict['page_content'] = f'<!-- Contenu de {page_name} -->'
    
    # Génère le HTML final
    try:
        html_output = template_engine.render(template_path, vars_dict)
        
        # Écrit le fichier de sortie
        output_file = OUTPUT_DIR / f"{page_name}.html"
        output_file.write_text(html_output, encoding='utf-8')
        
        print(f"[OK] {page_name}.html genere")
        return True
    except Exception as e:
        print(f"[ERREUR] Erreur lors du build de {page_name}: {e}")
        return False


def generate_webp_variants(assets_root: Path) -> None:
    """
    Génère des variantes WebP pour les images PNG/JPEG du dossier assets.
    Cette étape est optionnelle et nécessite Pillow (pip install pillow).
    """
    try:
        from PIL import Image  # type: ignore
    except ImportError:
        print("[WARN] Pillow non installe - generation des WebP ignoree. Installez-le avec: pip install pillow")
        return

    exts = {".png", ".jpg", ".jpeg"}
    generated = 0

    for img_path in assets_root.rglob("*"):
        if not img_path.is_file():
            continue
        if img_path.suffix.lower() not in exts:
            continue

        webp_path = img_path.with_suffix(".webp")
        if webp_path.exists():
            continue

        try:
            with Image.open(img_path) as img:
                # WebP supporte la transparence, on convertit en RGBA par securite
                converted = img.convert("RGBA")
                converted.save(
                    webp_path,
                    "WEBP",
                    quality=85,
                    method=6,
                )
            generated += 1
        except Exception as e:
            print(f"[WARN] Impossible de generer WebP pour {img_path}: {e}")

    if generated > 0:
        print(f"[OK] {generated} image(s) WebP generee(s) dans {assets_root}")


def generate_sitemap_pages(output_dir: Path, project_slugs: Optional[List[str]] = None) -> None:
    """Genere sitemap-pages.xml avec les pages statiques et les pages projet."""
    lastmod = datetime.now().strftime('%Y-%m-%d')
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"',
        '        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 '
        'http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">',
    ]
    for path, changefreq, priority in SITEMAP_PAGES:
        loc = SITE_BASE + path if path != '/' else SITE_BASE + '/'
        lines.append(f'  <url><loc>{loc}</loc><lastmod>{lastmod}</lastmod>'
                     f'<changefreq>{changefreq}</changefreq><priority>{priority}</priority></url>')
    for slug in (project_slugs or []):
        lines.append(f'  <url><loc>{SITE_BASE}/projets/{slug}</loc><lastmod>{lastmod}</lastmod>'
                     '<changefreq>monthly</changefreq><priority>0.5</priority></url>')
    lines.append('</urlset>')
    (output_dir / 'sitemap-pages.xml').write_text('\n'.join(lines), encoding='utf-8')


def generate_sitemap_index(output_dir: Path) -> None:
    """Genere sitemap.xml (index) pointant vers sitemap-pages et blog."""
    lastmod = datetime.now().strftime('%Y-%m-%d')
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"',
        '              xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 '
        'http://www.sitemaps.org/schemas/sitemap/0.9/siteindex.xsd">',
        f'  <sitemap><loc>{SITE_BASE}/sitemap-pages.xml</loc><lastmod>{lastmod}</lastmod></sitemap>',
        f'  <sitemap><loc>{SITE_BASE}/blog/sitemap-blog.xml</loc><lastmod>{lastmod}</lastmod></sitemap>',
        '</sitemapindex>',
    ]
    (output_dir / 'sitemap.xml').write_text('\n'.join(lines), encoding='utf-8')


def main():
    """Fonction principale."""
    global OUTPUT_DIR
    
    # Parse les arguments
    output_dir_arg = None
    watch_mode = False
    page_name = None
    
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == '--output' and i + 1 < len(sys.argv):
            output_dir_arg = sys.argv[i + 1]
            i += 2
        elif arg == '--watch':
            watch_mode = True
            i += 1
        elif not arg.startswith('--'):
            page_name = arg
            i += 1
        else:
            i += 1
    
    # Définit le dossier de sortie
    if output_dir_arg:
        OUTPUT_DIR = BASE_DIR / output_dir_arg
    else:
        OUTPUT_DIR = BASE_DIR / 'dist'
    
    # Crée les dossiers nécessaires
    SRC_DIR.mkdir(exist_ok=True)
    INCLUDES_DIR.mkdir(exist_ok=True)
    TEMPLATES_DIR.mkdir(exist_ok=True)
    PAGES_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    # Copie les assets dans le dossier de sortie
    assets_src = BASE_DIR / 'assets'
    assets_dst = OUTPUT_DIR / 'assets'
    if assets_src.exists():
        do_full_copytree = True
        if assets_dst.exists():
            try:
                shutil.rmtree(assets_dst)
            except (PermissionError, OSError):
                import stat
                def handle_remove_readonly(func, path, exc):
                    os.chmod(path, stat.S_IWRITE)
                    func(path)
                try:
                    shutil.rmtree(assets_dst, onerror=handle_remove_readonly)
                except (PermissionError, OSError):
                    # Fichier verrouillé : copie par ecrasement sans supprimer
                    for path in assets_src.rglob('*'):
                        if path.is_file():
                            rel = path.relative_to(assets_src)
                            dest = assets_dst / rel
                            dest.parent.mkdir(parents=True, exist_ok=True)
                            try:
                                shutil.copy2(path, dest)
                            except (PermissionError, OSError):
                                pass
                    placeholder_dst = assets_dst / 'images' / 'projets' / 'placeholder.svg'
                    if not placeholder_dst.exists():
                        placeholder_src = assets_src / 'images' / 'projets' / 'placeholder.svg'
                        if placeholder_src.exists():
                            placeholder_dst.parent.mkdir(parents=True, exist_ok=True)
                            shutil.copy2(placeholder_src, placeholder_dst)
                    print(f"[OK] Assets mis a jour (fichiers verrouilles, copie par ecrasement)")
                    do_full_copytree = False
        if do_full_copytree:
            shutil.copytree(assets_src, assets_dst)
            print(f"[OK] Assets copies dans {assets_dst}")
        # Génère les variantes WebP pour les images (optimisation UX / perf)
        generate_webp_variants(assets_dst)

    # Genere robots.txt (base sur SITE_BASE)
    generate_robots_txt(OUTPUT_DIR)
    print("[OK] robots.txt genere")

    # Sitemaps : generes apres le build du blog (voir plus bas)
    
    # Copie manifest.json et browserconfig.xml à la racine
    # manifest.json peut être référencé depuis n'importe où, mais on le met à la racine pour simplicité
    manifest_src = BASE_DIR / 'assets' / 'icons' / 'favicons' / 'manifest.json'
    manifest_dst = OUTPUT_DIR / 'manifest.json'
    if manifest_src.exists():
        shutil.copy2(manifest_src, manifest_dst)
        print(f"[OK] manifest.json copie a la racine")
    
    # browserconfig.xml doit être à la racine (convention Microsoft)
    # On crée une version avec les chemins relatifs depuis la racine
    browserconfig_src = BASE_DIR / 'assets' / 'icons' / 'favicons' / 'browserconfig.xml'
    browserconfig_dst = OUTPUT_DIR / 'browserconfig.xml'
    if browserconfig_src.exists():
        # Lit le contenu et ajuste les chemins pour qu'ils soient relatifs depuis la racine
        browserconfig_content = browserconfig_src.read_text(encoding='utf-8')
        # Les chemins dans browserconfig.xml pointent déjà vers assets/icons/favicons/, c'est bon
        browserconfig_dst.write_text(browserconfig_content, encoding='utf-8')
        print(f"[OK] browserconfig.xml copie a la racine")

    # Copie du dossier api/ (PHP formulaire contact) vers dist/
    api_src = BASE_DIR / 'api'
    api_dst = OUTPUT_DIR / 'api'
    if api_src.exists():
        api_dst.mkdir(exist_ok=True)
        for f in api_src.iterdir():
            if f.is_file():
                shutil.copy2(f, api_dst / f.name)
        print(f"[OK] api/ copie dans {api_dst}")

    # Copie le favicon.svg vers favicon.ico à la racine
    # Note: nginx redirigera /favicon.ico vers /assets/icons/favicon.svg
    favicon_svg_src = BASE_DIR / 'assets' / 'icons' / 'favicon.svg'
    favicon_ico = OUTPUT_DIR / 'favicon.ico'
    if favicon_svg_src.exists():
        # Copie le contenu du SVG vers favicon.ico (pour compatibilité)
        favicon_svg_content = favicon_svg_src.read_text(encoding='utf-8')
        favicon_ico.write_text(favicon_svg_content, encoding='utf-8')
        print(f"[OK] favicon.ico cree depuis favicon.svg")
    
    # Initialise le moteur de template
    template_engine = TemplateEngine(SRC_DIR)
    
    # Si une page spécifique est demandée
    if page_name and not watch_mode:
        if build_page(page_name, template_engine):
            print(f"\n[OK] Build de {page_name} termine dans {OUTPUT_DIR} !")
        else:
            sys.exit(1)
        return
    
    # Build toutes les pages
    print(f"[BUILD] Build de toutes les pages dans {OUTPUT_DIR}...\n")
    
    # Liste des pages à builder
    pages = [
        'index',
        'autres-prestations',
        'processus',
        'metz',
        'portfolio',
        'projets',
        'statistiques',
        'mentions-legales',
        'cgv',
        'cgu',
        'politique-confidentialite'
    ]
    
    success_count = 0
    for page in pages:
        if build_page(page, template_engine):
            success_count += 1

    # Build du blog (articles Markdown -> HTML)
    blog_dir = BASE_DIR / 'blog'
    if blog_dir.exists():
        import subprocess
        try:
            blog_output = str((OUTPUT_DIR / 'blog').relative_to(BASE_DIR))
        except ValueError:
            blog_output = str(OUTPUT_DIR / 'blog')
        try:
            result = subprocess.run(
                [sys.executable, str(blog_dir / 'build_blog.py'), '--output', blog_output],
                cwd=str(BASE_DIR),
                capture_output=True,
                text=True,
                timeout=60
            )
            if result.returncode == 0:
                print(result.stdout or '')
            else:
                print(f"[WARN] Build blog echoue : {result.stderr or result.stdout}")
        except Exception as e:
            print(f"[WARN] Build blog non execute : {e}")

    # Pages projet (projets/<slug>.html)
    project_slugs = build_project_pages(template_engine, OUTPUT_DIR)

    # Generation des sitemaps (pages statiques + projets)
    generate_sitemap_pages(OUTPUT_DIR, project_slugs=project_slugs)
    generate_sitemap_index(OUTPUT_DIR)
    print("[OK] sitemap.xml et sitemap-pages.xml generes")

    print(f"\n[OK] Build termine ! {success_count}/{len(pages)} page(s) generee(s) dans {OUTPUT_DIR}.")
    
    # Mode watch
    if len(sys.argv) > 1 and sys.argv[1] == '--watch':
        print("\n[WATCH] Mode watch active. Appuyez sur Ctrl+C pour arreter.")
        try:
            import time
            from watchdog.observers import Observer
            from watchdog.events import FileSystemEventHandler
            
            class BuildHandler(FileSystemEventHandler):
                def on_modified(self, event):
                    if event.src_path.endswith(('.html', '.json')):
                        print(f"\n📝 Fichier modifié : {event.src_path}")
                        # Détermine quelle page rebuilder
                        for page in pages:
                            if page in event.src_path:
                                build_page(page, template_engine)
                                break
            
            event_handler = BuildHandler()
            observer = Observer()
            observer.schedule(event_handler, str(SRC_DIR), recursive=True)
            observer.start()
            
            while True:
                time.sleep(1)
        except ImportError:
            print("[WARN] Mode watch necessite 'watchdog'. Installez avec: pip install watchdog")
        except KeyboardInterrupt:
            print("\n\n[WATCH] Arret du mode watch.")


if __name__ == '__main__':
    main()

