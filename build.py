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
    python3 build.py --no-webp    # Omet la conversion WebP (build plus rapide en local)
    python3 build.py index        # Build une page spécifique
"""

import html
import os
import re
import sys
import json
import shutil
from pathlib import Path
from typing import Dict, Optional, List, Any
from datetime import datetime
from urllib.parse import quote

# Configuration
BASE_DIR = Path(__file__).parent
SRC_DIR = BASE_DIR / 'src'
INCLUDES_DIR = SRC_DIR / 'includes'
TEMPLATES_DIR = SRC_DIR / 'templates'
PAGES_DIR = SRC_DIR / 'pages'
DATA_DIR = SRC_DIR / 'data'
PROJECTS_JSON = DATA_DIR / 'projects.json'
VITRINES_JSON = DATA_DIR / 'vitrines.json'
READMES_DIR = DATA_DIR / 'readmes'
# Sources vitrines (anciennement showcase/) — publiées sous /vitrines/ au build
VITRINES_DEMOS_SRC = BASE_DIR / 'assets' / 'vitrines' / 'demos'
VITRINES_SCREENSHOTS_SRC = BASE_DIR / 'assets' / 'vitrines' / 'screenshots'

# Libelles categories vitrines (filtre home + cartes)
VITRINE_CATEGORY_LABELS = {
    'tech': 'Tech & SaaS',
    'services': 'Services',
    'hcr': 'HCR & restauration',
    'retail': 'Commerce',
    'formation': 'Formation',
    'hotel': 'Hôtellerie',
    'beaute': 'Beauté & spa',
    'mobilite': 'Automobile',
    'artisanat': 'Artisanat',
    'sante': 'Santé',
    'finance': 'Finance',
    'industrie': 'Industrie',
    'conseil': 'Conseil',
    'ess': 'ESS',
}
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
    ('/analyse', 'monthly', '0.6'),
    ('/vitrines/', 'monthly', '0.65'),
    ('/vitrines/parcours.html', 'monthly', '0.6'),
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


# Marqueur d'injection (evite doublons si rebuild)
_DEMO_PROTECTION_MARKER = 'danielcraft-demo-protection'


def _inject_demo_protection(html: str) -> str:
    """
    Injecte meta robots + bandeau demo (shared/demo-protection.*) dans chaque HTML
    publie sous vitrines/<slug>/demo/. Dissuasion legere — pas une barriere technique absolue.
    Chemins en ../../shared/ (profondeur demo/ depuis dist/vitrines/<slug>/demo/).
    """
    if _DEMO_PROTECTION_MARKER in html:
        return html
    block = (
        f'\n  <!-- {_DEMO_PROTECTION_MARKER} -->\n'
        '  <meta name="robots" content="noindex, noarchive, nosnippet, noimageindex">\n'
        f'  <meta name="{_DEMO_PROTECTION_MARKER}" content="1">\n'
        '  <link rel="stylesheet" href="../../shared/demo-protection.css">\n'
        '  <script src="../../shared/demo-protection.js" defer></script>\n'
    )
    new_html, n = re.subn(r'</head>', block + r'</head>', html, count=1, flags=re.IGNORECASE)
    return new_html if n else html


def generate_robots_txt(output_dir: Path) -> None:
    """
    Genere robots.txt dans dist/ avec des URLs basees sur SITE_BASE.

    Ca evite de versionner un domaine "reel" dans le repo, tout en ayant des
    sitemaps absolus corrects au moment du build/deploiement.
    """
    base = SITE_BASE.rstrip('/')
    demo_disallows: List[str] = []
    vdata = load_vitrines()
    if vdata and vdata.get('items'):
        demo_disallows.append('# Dossiers /vitrines/<slug>/demo/ (HTML de demonstration — pas d’indexation)')
        for it in vdata['items']:
            slug = (it.get('slug') or '').strip()
            if slug:
                demo_disallows.append(f'Disallow: /vitrines/{slug}/demo/')
        demo_disallows.append('')
    demo_block = '\n'.join(demo_disallows)

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
        "\n"
        + demo_block
        + "# Vitrines (hub, fiches, captures — hors dossiers demo ci-dessus)\n"
        "Allow: /vitrines/\n"
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


def load_vitrines() -> Optional[Dict[str, Any]]:
    """Charge le catalogue vitrines (YAML/JSON unique : src/data/vitrines.json)."""
    if not VITRINES_JSON.exists():
        return None
    with open(VITRINES_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)


def _vitrine_screenshot_basename(slug: str, prefix: str) -> str:
    """Nom du fichier capture ou '' (priorité WebP : plus léger). Sources : assets/vitrines/screenshots/<slug>/."""
    root = VITRINES_SCREENSHOTS_SRC / slug
    if not root.is_dir():
        return ''
    for ext in ('.webp', '.jpg', '.jpeg'):
        found = sorted(root.glob(f'{prefix}_*{ext}'))
        if found:
            return found[0].name
    return ''


def _vitrine_screenshot_paths(slug: str, prefix: str) -> tuple[str, str, str]:
    """
    Chemins pour une capture : (depuis la racine du site sans slash initial,
    depuis la fiche vitrine, absolu depuis la racine du site).
    Exemple : ('vitrines/hub/screenshots/desktop_....webp', 'screenshots/desktop_....webp', '/vitrines/hub/screenshots/...')
    """
    name = _vitrine_screenshot_basename(slug, prefix)
    if not name:
        return '', '', ''
    return (
        f'vitrines/{slug}/screenshots/{name}',
        f'screenshots/{name}',
        f'/vitrines/{slug}/screenshots/{name}',
    )


def _rewrite_vitrine_demo_shared_refs(text: str) -> str:
    """Les démos sont servies sous /vitrines/<slug>/demo/ : ../shared/ -> ../../shared/ (idempotent)."""
    return re.sub(r'(?:\.\./)+(?=shared/)', '../../', text)


def publish_vitrines_to_dist(output_dir: Path) -> None:
    """Publie assets/vitrines/* vers dist/vitrines/ (hub, shared, secteurs/demo/, captures par slug)."""
    demos_src = VITRINES_DEMOS_SRC
    shots_src = VITRINES_SCREENSHOTS_SRC
    if not demos_src.is_dir():
        print('[WARN] assets/vitrines/demos absent — vitrines statiques non publiees')
        return
    out = output_dir / 'vitrines'
    out.mkdir(parents=True, exist_ok=True)

    src_shared = demos_src / 'shared'
    if src_shared.is_dir():
        dst_s = out / 'shared'
        if dst_s.exists():
            shutil.rmtree(dst_s)
        shutil.copytree(src_shared, dst_s)

    hub_tpl = demos_src / 'index.html'
    if hub_tpl.is_file():
        hub_text = hub_tpl.read_text(encoding='utf-8')
        hub_text = re.sub(r'href="([a-z]+)/index.html"', r'href="\1/demo/index.html"', hub_text)
        hub_text = hub_text.replace('ÔÇö', '—')
        (out / 'index.html').write_text(hub_text, encoding='utf-8')
    for name in ('hub.css', 'hub-texture.png'):
        p = demos_src / name
        if p.is_file():
            shutil.copy2(p, out / name)

    skip_dirs = {'shared', '__pycache__'}
    for entry in demos_src.iterdir():
        if not entry.is_dir() or entry.name in skip_dirs:
            continue
        slug = entry.name
        dst_demo = out / slug / 'demo'
        if dst_demo.exists():
            shutil.rmtree(dst_demo)
        for path in entry.rglob('*'):
            rel = path.relative_to(entry)
            dest = dst_demo / rel
            if path.is_dir():
                dest.mkdir(parents=True, exist_ok=True)
                continue
            dest.parent.mkdir(parents=True, exist_ok=True)
            ext = path.suffix.lower()
            if ext in {'.html', '.css', '.js', '.svg'}:
                try:
                    txt = path.read_text(encoding='utf-8')
                except UnicodeDecodeError:
                    shutil.copy2(path, dest)
                    continue
                txt = _rewrite_vitrine_demo_shared_refs(txt)
                if ext == '.html':
                    txt = _inject_demo_protection(txt)
                dest.write_text(txt, encoding='utf-8')
            else:
                shutil.copy2(path, dest)

    if shots_src.is_dir():
        for sub in shots_src.iterdir():
            if not sub.is_dir():
                continue
            dst_sh = out / sub.name / 'screenshots'
            if dst_sh.exists():
                shutil.rmtree(dst_sh)
            shutil.copytree(sub, dst_sh)
    print(f'[OK] vitrines/ publie dans {out}')


def build_vitrines_catalog_embed() -> None:
    """Genere includes/vitrines-catalog-embed.html pour la section #vitrines de l'accueil."""
    data = load_vitrines()
    path_out = INCLUDES_DIR / 'vitrines-catalog-embed.html'
    if not data or not data.get('items'):
        path_out.write_text(
            '<section id="vitrines" class="vitrines-showcase"><div class="container">'
            '<p class="vitrines-empty">Catalogue vitrines indisponible (ajoutez <code>src/data/vitrines.json</code>).</p>'
            '</div></section>\n',
            encoding='utf-8',
        )
        print('[WARN] vitrines-catalog-embed.html : pas de donnees vitrines')
        return

    hub = (data.get('vitrines_hub_path') or data.get('showcase_hub_path') or '/vitrines/').strip()
    if not hub.startswith('/'):
        hub = '/' + hub
    if hub in ('/vitrines', '/vitrines/'):
        hub = '/vitrines/'

    items = data['items']
    cats: List[str] = []
    seen: set = set()
    for it in items:
        c = (it.get('category') or '').strip()
        if c and c not in seen:
            seen.add(c)
            cats.append(c)

    lines: List[str] = []
    lines.append('<!-- Genere automatiquement par build.py depuis src/data/vitrines.json -->')
    lines.append('<section id="vitrines" class="vitrines-showcase">')
    lines.append('    <div class="container">')
    lines.append('        <div class="section-header scroll-reveal">')
    lines.append('            <span class="section-badge">Vitrines HTML</span>')
    lines.append('            <h2 class="section-title">Démos par secteur, prêtes à personnaliser</h2>')
    lines.append('            <p class="section-description">')
    lines.append(
        '                Parcours statiques Bulma : captures harmonisées avec la charte DanielCraft. '
        f'<a href="{html.escape(hub)}">Ouvrir le hub des vitrines</a> ou choisissez une fiche pour la démo, le résumé et l’achat.'
    )
    lines.append('            </p>')
    lines.append('        </div>')
    lines.append('        <div class="vitrines-toolbar scroll-reveal">')
    lines.append('            <div class="vitrines-filter" role="group" aria-label="Filtrer par secteur">')
    lines.append('                <button type="button" class="vitrines-filter-btn active" data-vitrine-filter="all">Tous</button>')
    for c in sorted(cats):
        label = VITRINE_CATEGORY_LABELS.get(c, c.replace('_', ' ').title())
        lines.append(
            f'                <button type="button" class="vitrines-filter-btn" '
            f'data-vitrine-filter="{html.escape(c)}">{html.escape(label)}</button>'
        )
    lines.append('            </div>')
    lines.append('        </div>')
    lines.append('        <div class="vitrines-grid" id="vitrinesGrid">')
    for idx, it in enumerate(items):
        slug = (it.get('slug') or '').strip()
        if not slug:
            continue
        cat = (it.get('category') or 'all').strip() or 'all'
        title = html.escape(it.get('title') or slug)
        tagline = html.escape(it.get('tagline') or '')
        excerpt = html.escape(it.get('excerpt') or '')
        _c_thumb, _d_thumb, _a_thumb = _vitrine_screenshot_paths(slug, 'desktop')
        thumb = _c_thumb or '/assets/images/og/home-1200x630.jpg'
        cat_label = html.escape(VITRINE_CATEGORY_LABELS.get(cat, cat))
        delay = min(idx * 40, 400)
        lines.append(
            f'        <article class="vitrine-card scroll-reveal" data-vitrine-cat="{html.escape(cat)}" '
            f'style="--reveal-delay:{delay}ms">'
        )
        lines.append(
            f'            <a class="vitrine-card-media" href="/vitrines/{html.escape(slug)}/" '
            f'aria-label="Voir la fiche détail — {title}">'
        )
        lines.append(
            '                <div class="vitrine-card-img-scroll vitrine-scroll-hide-scrollbar" '
            'data-vitrine-card-hover-scroll>'
        )
        lines.append(
            f'                    <img src="{html.escape(thumb)}" alt="" width="640" height="400" '
            'loading="lazy" decoding="async" class="vitrine-card-img">'
        )
        lines.append('                </div>')
        lines.append('                <span class="vitrine-card-tint" aria-hidden="true"></span>')
        lines.append(f'                <span class="vitrine-card-badge">{cat_label}</span>')
        lines.append('            </a>')
        lines.append('            <div class="vitrine-card-body">')
        lines.append(f'                <h3 class="vitrine-card-title">{title}</h3>')
        lines.append(f'                <p class="vitrine-card-tagline">{tagline}</p>')
        lines.append(f'                <p class="vitrine-card-excerpt">{excerpt}</p>')
        lines.append('                <div class="vitrine-card-actions">')
        lines.append(
            f'                    <a class="btn btn-primary vitrine-card-btn" href="/vitrines/{html.escape(slug)}/">'
            'Voir la fiche détail</a>'
        )
        lines.append(
            f'                    <a class="btn btn-outline vitrine-card-btn" href="/vitrines/{html.escape(slug)}/demo/index.html" '
            'target="_blank" rel="noopener noreferrer">Démo live</a>'
        )
        lines.append('                </div>')
        lines.append('            </div>')
        lines.append('        </article>')
    lines.append('        </div>')
    lines.append(
        '        <p class="vitrines-footnote scroll-reveal">'
        'Pour les dépôts open source, voir aussi <a href="/projets">la page Projets</a>.</p>'
    )
    lines.append('    </div>')
    lines.append('</section>')
    new_content = '\n'.join(lines) + '\n'
    if path_out.exists() and path_out.read_text(encoding='utf-8') == new_content:
        return
    path_out.write_text(new_content, encoding='utf-8')
    print(f'[OK] vitrines-catalog-embed.html genere ({len(items)} vitrine(s))')


def build_vitrine_pages(template_engine: TemplateEngine, output_dir: Path) -> List[str]:
    """Genere vitrines/<slug>/index.html pour chaque entree du catalogue."""
    data = load_vitrines()
    if not data or not data.get('items'):
        return []
    content_path = PAGES_DIR / 'vitrine-detail.html'
    if not content_path.exists():
        print('[WARN] src/pages/vitrine-detail.html manquant')
        return []
    content_tpl = content_path.read_text(encoding='utf-8')
    template_path = TEMPLATES_DIR / 'base.html'
    out_root = output_dir / 'vitrines'
    default_price = int(data.get('default_price_eur') or 42)
    slugs_out: List[str] = []
    for it in data['items']:
        slug = (it.get('slug') or '').strip()
        if not slug:
            continue
        raw_price = it.get('price_eur', default_price)
        try:
            price = int(raw_price)
        except (TypeError, ValueError):
            price = default_price
        features = it.get('features') or []
        features_html = (
            '<ul class="vitrine-feature-list">'
            + ''.join(f'<li>{html.escape(str(x))}</li>' for x in features)
            + '</ul>'
        )
        stack = it.get('stack') or []
        stack_html = ''.join(f'<li>{html.escape(str(x))}</li>' for x in stack)
        stripe_url = (it.get('stripe_payment_link_url') or '').strip()
        _, d_desk, a_desk = _vitrine_screenshot_paths(slug, 'desktop')
        _, d_tab, _a_tab = _vitrine_screenshot_paths(slug, 'tablet')
        _, d_mob, _a_mob = _vitrine_screenshot_paths(slug, 'mobile')
        fallback = '/assets/images/og/home-1200x630.jpg'
        desk = d_desk or fallback
        tab = d_tab or d_desk or fallback
        mob = d_mob or d_desk or fallback
        og_desk = a_desk or fallback
        title = it.get('title') or slug
        excerpt = (it.get('excerpt') or it.get('tagline') or '')[:170]
        mail_subj = quote(f'Installation vitrine — {title}')
        vars_dict = DEFAULT_VARS.copy()
        vars_dict.update({
            'current_page': 'vitrine',
            'page_title': f'{title} – Vitrine HTML | DanielCraft',
            'page_description': excerpt,
            'page_keywords': 'vitrine html, vitrines, bulma, ' + ', '.join(str(s) for s in (it.get('stack') or [])[:6]),
            'page_url': f'{SITE_BASE.rstrip("/")}/vitrines/{slug}/',
            'og_image': og_desk,
            'og_type': 'website',
            'schema_type': '',
            'extra_css': 'vitrines-portfolio.css',
            'page_scripts': ['main.js', 'vitrines-screenshots.js'],
            'vitrine_title': title,
            'vitrine_tagline': it.get('tagline') or '',
            'vitrine_excerpt': it.get('excerpt') or '',
            'vitrine_slug': slug,
            'vitrine_demo_url': f'/vitrines/{slug}/demo/index.html',
            'vitrine_shot_desktop': desk,
            'vitrine_shot_tablet': tab,
            'vitrine_shot_mobile': mob,
            'vitrine_features_html': features_html,
            'vitrine_stack_html': stack_html,
            'vitrine_price_eur': str(price),
            'vitrine_stripe_url': stripe_url,
            'vitrine_has_stripe': stripe_url,
            'vitrine_mailto_subject': mail_subj,
        })
        _normalize_page_meta(vars_dict, slug)
        vars_dict['page_url'] = _to_absolute_url(f'/vitrines/{slug}/')
        vars_dict['og_image'] = _to_absolute_url(og_desk)
        scripts = vars_dict.get('page_scripts') or []
        scripts_content = '\n'.join(f'<script src="/assets/js/{s}" defer></script>' for s in scripts)
        vars_dict['page_scripts_content'] = scripts_content
        content_rendered = template_engine.replace_variables(content_tpl, vars_dict)
        content_rendered = template_engine.process_includes(content_rendered, vars_dict)
        vars_dict['page_content'] = content_rendered
        html_output = template_engine.render(template_path, vars_dict)
        dest_dir = out_root / slug
        dest_dir.mkdir(parents=True, exist_ok=True)
        (dest_dir / 'index.html').write_text(html_output, encoding='utf-8')
        slugs_out.append(slug)
    print(f'[OK] {len(slugs_out)} page(s) vitrine dans {out_root}')
    return slugs_out


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
        vars_dict['page_scripts_content'] = '<script src="/assets/js/main.js" defer></script>'
        html_output = template_engine.render(template_path, vars_dict)
        (out_projets / f'{slug}.html').write_text(html_output, encoding='utf-8')
        slugs.append(slug)
    print(f"[OK] {len(slugs)} page(s) projet genere(s) dans {out_projets}")
    return slugs


def build_page(page_name: str, template_engine: TemplateEngine):
    """Build une page HTML."""
    if page_name == 'index':
        build_vitrines_catalog_embed()

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
            f'<script src="/assets/js/{script}" defer></script>'
            for script in scripts
        ])
    else:
        scripts_content = '<script src="/assets/js/main.js" defer></script>'
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
        # Comme {{page_content}} est injecté après le rendu du gabarit, les
        # {% include %} du fragment ne seraient pas traités sans ce passage.
        page_content = template_engine.process_includes(page_content, vars_dict)
        page_content = template_engine.replace_variables(page_content, vars_dict)
        vars_dict['page_content'] = page_content
    else:
        print(f"[WARN] Contenu de page non trouve : {page_content_file}")
        vars_dict['page_content'] = f'<!-- Contenu de {page_name} -->'
    
    # Génère le HTML final
    try:
        html_output = template_engine.render(template_path, vars_dict)
        
        # Écrit le fichier de sortie (option : output_subpath dans la config JSON)
        out_sub = (page_config.get('output_subpath') or '').strip()
        if out_sub:
            output_file = OUTPUT_DIR / out_sub.replace('/', os.sep)
        else:
            output_file = OUTPUT_DIR / f"{page_name}.html"
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(html_output, encoding='utf-8')
        
        rel_out = output_file.relative_to(OUTPUT_DIR)
        print(f'[OK] {rel_out.as_posix()} genere')
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
        from PIL import ImageFile  # type: ignore
    except ImportError:
        print("[WARN] Pillow non installe - generation des WebP ignoree. Installez-le avec: pip install pillow")
        return

    # PNG/JPEG incomplets (copie interrompue, etc.) : tenter de charger le maximum de données
    ImageFile.LOAD_TRUNCATED_IMAGES = True

    exts = {".png", ".jpg", ".jpeg"}
    generated = 0
    skipped = 0

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
                img.load()
                converted = img.convert("RGBA")
                # method=4 : bien plus rapide que 6 (qualité encore correcte à quality=85)
                converted.save(
                    webp_path,
                    "WEBP",
                    quality=85,
                    method=4,
                )
            generated += 1
        except Exception as e:
            skipped += 1
            print(f"[WARN] Impossible de generer WebP pour {img_path}: {e}")

    if generated > 0:
        print(f"[OK] {generated} image(s) WebP generee(s) dans {assets_root}")
    if skipped > 0:
        print(f"[INFO] {skipped} fichier(s) ignore(s) pour WebP (image corrompue ou illisible). Reparer ou remplacer le PNG source si besoin.")


def generate_sitemap_pages(
    output_dir: Path,
    project_slugs: Optional[List[str]] = None,
    vitrine_slugs: Optional[List[str]] = None,
) -> None:
    """Genere sitemap-pages.xml avec les pages statiques, projets et vitrines."""
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
    for slug in (vitrine_slugs or []):
        lines.append(f'  <url><loc>{SITE_BASE}/vitrines/{slug}/</loc><lastmod>{lastmod}</lastmod>'
                     '<changefreq>monthly</changefreq><priority>0.55</priority></url>')
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
    skip_webp = False
    
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == '--output' and i + 1 < len(sys.argv):
            output_dir_arg = sys.argv[i + 1]
            i += 2
        elif arg == '--watch':
            watch_mode = True
            i += 1
        elif arg == '--no-webp':
            skip_webp = True
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
        if not skip_webp:
            generate_webp_variants(assets_dst)
        else:
            print("[INFO] Generation WebP ignoree (--no-webp)")

    publish_vitrines_to_dist(OUTPUT_DIR)

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
        # Copie récursive (fichiers + sous-dossiers), utile pour vendor/ (PHPMailer)
        if api_dst.exists():
            try:
                shutil.rmtree(api_dst)
            except Exception:
                pass
        shutil.copytree(api_src, api_dst, dirs_exist_ok=True)
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
        'vitrines',
        'autres-prestations',
        'processus',
        'metz',
        'portfolio',
        'projets',
        'statistiques',
        'analyse',
        'desabonnement',
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
    vitrine_slugs = build_vitrine_pages(template_engine, OUTPUT_DIR)

    # Generation des sitemaps (pages statiques + projets + vitrines)
    generate_sitemap_pages(OUTPUT_DIR, project_slugs=project_slugs, vitrine_slugs=vitrine_slugs)
    generate_sitemap_index(OUTPUT_DIR)
    print("[OK] sitemap.xml et sitemap-pages.xml generes")

    print(f"\n[OK] Build termine ! {success_count}/{len(pages)} page(s) generee(s) dans {OUTPUT_DIR}.")
    
    # Mode watch
    if watch_mode:
        print("\n[WATCH] Mode watch active. Appuyez sur Ctrl+C pour arreter.")
        try:
            import time
            from watchdog.observers import Observer
            from watchdog.events import FileSystemEventHandler
            
            class BuildHandler(FileSystemEventHandler):
                def __init__(self):
                    self._last_event = {}

                def _is_debounced(self, key: str, delay_s: float = 0.25) -> bool:
                    now = time.time()
                    prev = self._last_event.get(key, 0.0)
                    if (now - prev) < delay_s:
                        return True
                    self._last_event[key] = now
                    return False

                def _copy_asset_file(self, src_path: Path):
                    if not src_path.exists() or not src_path.is_file():
                        return
                    try:
                        rel = src_path.relative_to(assets_src)
                    except ValueError:
                        return
                    dst_path = assets_dst / rel
                    dst_path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src_path, dst_path)
                    print(f"[ASSET] Copie: {rel}")

                def _rebuild_all_pages(self):
                    ok = 0
                    for p in pages:
                        if build_page(p, template_engine):
                            ok += 1
                    ps = build_project_pages(template_engine, OUTPUT_DIR)
                    vs = build_vitrine_pages(template_engine, OUTPUT_DIR)
                    generate_sitemap_pages(OUTPUT_DIR, project_slugs=ps, vitrine_slugs=vs)
                    print(f"[WATCH] Rebuild complet: {ok}/{len(pages)} page(s) + projets/vitrines/sitemap")

                def on_modified(self, event):
                    if event.is_directory:
                        return

                    src = Path(event.src_path)
                    src_str = str(src)
                    ext = src.suffix.lower()

                    if self._is_debounced(src_str):
                        return

                    # Changement dans assets (css/js/images/...) => copie live vers dist/assets
                    if assets_src in src.parents:
                        if ext in {'.css', '.js', '.png', '.jpg', '.jpeg', '.webp', '.svg', '.ico', '.gif', '.json', '.woff', '.woff2', '.ttf'}:
                            self._copy_asset_file(src)
                            return

                    # Changement de page source => rebuild ciblé si possible
                    if ext in {'.html', '.json'} and PAGES_DIR in src.parents:
                        page = src.stem
                        print(f"\n📝 Page modifiee : {src.name}")
                        if page in pages:
                            build_page(page, template_engine)
                        else:
                            self._rebuild_all_pages()
                        return

                    # Donnees partagees (vitrines, etc.) => rebuild global
                    if ext in {'.html', '.json'} and DATA_DIR in src.parents:
                        print(f"\n📦 Data modifiee : {src.name}")
                        self._rebuild_all_pages()
                        return

                    # Changement template/include => rebuild global
                    if ext in {'.html', '.json'} and (TEMPLATES_DIR in src.parents or INCLUDES_DIR in src.parents):
                        print(f"\n🧩 Template/include modifie : {src.name}")
                        self._rebuild_all_pages()
                        return
            
            event_handler = BuildHandler()
            observer = Observer()
            observer.schedule(event_handler, str(SRC_DIR), recursive=True)
            if assets_src.exists():
                observer.schedule(event_handler, str(assets_src), recursive=True)
            observer.start()
            
            while True:
                time.sleep(1)
        except ImportError:
            print("[WARN] Mode watch necessite 'watchdog'. Installez avec: pip install watchdog")
        except KeyboardInterrupt:
            print("\n\n[WATCH] Arret du mode watch.")


if __name__ == '__main__':
    main()

