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
from datetime import datetime, timedelta
from urllib.parse import quote

# Configuration
BASE_DIR = Path(__file__).parent
SRC_DIR = BASE_DIR / 'src'
INCLUDES_DIR = SRC_DIR / 'includes'
# Includes réécrits à chaque build_page — ne pas les surveiller (sinon boucle watch).
GENERATED_INCLUDE_NAMES = frozenset({
    'home-vitrines-teaser.html',
    'vitrines-page-collection.html',
    'vitrines-catalog-embed.html',
    'prestations-catalog-embed.html',
    'livres-catalog-embed.html',
    'livres-deal-week.html',
})
TEMPLATES_DIR = SRC_DIR / 'templates'
PAGES_DIR = SRC_DIR / 'pages'
DATA_DIR = SRC_DIR / 'data'
PROJECTS_JSON = DATA_DIR / 'projects.json'
PROJECT_SLUG_ALIASES_JSON = DATA_DIR / 'project-slug-aliases.json'
VITRINES_JSON = DATA_DIR / 'vitrines.json'
PRESTATIONS_JSON = DATA_DIR / 'prestations.json'
LIVRES_JSON = DATA_DIR / 'livres.json'
AUDITS_JSON = DATA_DIR / 'audits.json'
READMES_DIR = DATA_DIR / 'readmes'
# Sources vitrines (anciennement showcase/) — publiées sous /vitrines/ au build
VITRINES_DEMOS_SRC = BASE_DIR / 'assets' / 'vitrines' / 'demos'
VITRINES_SCREENSHOTS_SRC = BASE_DIR / 'assets' / 'vitrines' / 'screenshots'

# Filtres vitrines phares (mobile + raccourcis desktop)
VITRINE_FEATURED_FILTER_KEYS = ['hcr', 'retail', 'beaute', 'sante', 'artisanat']
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
    'immobilier': 'Immobilier',
    'juridique': 'Juridique',
    'architecture': 'Architecture',
    'sport': 'Sport & fitness',
    'creatif': 'Créatif & médias',
}
# Dossier de sortie par défaut : dist/ (peut être modifié via --output)
OUTPUT_DIR = BASE_DIR / 'dist'
# Base URL du site (utilisée pour canoniques/OG/sitemaps).
# Pour éviter toute donnée perso en dur, configure via variable d'environnement :
#   SITE_BASE="https://ton-domaine.com"
SITE_BASE = os.environ.get('SITE_BASE', 'https://example.com')


def _is_local_site_base(url: str) -> bool:
    """Détecte une base locale/dev qui ne doit pas fuiter en prod."""
    raw = (url or '').strip().lower()
    if not raw:
        return True
    return (
        'localhost' in raw
        or '127.0.0.1' in raw
        or '0.0.0.0' in raw
        or 'example.com' in raw
    )


def _resolve_public_site_base(default_base: str) -> str:
    """
    Résout la base publique finale.
    - En dev local: SITE_BASE peut rester localhost.
    - En contexte de déploiement: si SITE_BASE est local et DEPLOY_SITE_BASE est défini,
      on utilise DEPLOY_SITE_BASE pour éviter des URLs localhost dans canoniques/sitemaps.
    """
    site_base = (os.environ.get('SITE_BASE') or default_base or '').strip()
    deploy_base = (os.environ.get('DEPLOY_SITE_BASE') or '').strip()
    if deploy_base and _is_local_site_base(site_base):
        return deploy_base.rstrip('/')
    return site_base.rstrip('/')


def _load_build_dotenv() -> None:
    """Charge .env à la racine du repo pour SITE_BASE, Stripe, etc."""
    env_path = BASE_DIR / '.env'
    if not env_path.is_file():
        return
    for raw in env_path.read_text(encoding='utf-8').splitlines():
        line = raw.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        key, val = line.split('=', 1)
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if key and os.environ.get(key) in (None, ''):
            os.environ[key] = val


def _stripe_publishable_key() -> str:
    _load_build_dotenv()
    return (os.environ.get('STRIPE_PUBLISHABLE_KEY') or '').strip()


def _webful_analytics_config() -> Dict[str, Any]:
    """Config Webful Analytics (script head, sans cookies, RGPD)."""
    _load_build_dotenv()
    site_id = (os.environ.get('WEBFUL_SITE_ID') or '').strip()
    api_key = (os.environ.get('WEBFUL_API_KEY') or '').strip()
    base_url = (os.environ.get('WEBFUL_BASE_URL') or 'https://webful.fr').strip().rstrip('/')
    enabled = bool(site_id and api_key)
    return {
        'webful_enabled': enabled,
        'webful_site_id': site_id,
        'webful_api_key': api_key,
        'webful_base_url': base_url,
    }


def _apply_analytics_vars(vars_dict: Dict) -> None:
    vars_dict.update(_webful_analytics_config())


# Libelles categories et statuts (pages projet)
CATEGORY_LABELS = {'web': 'Web', 'tools': 'Outils', 'mobile': 'Mobile', 'iot': 'IoT', 'specialized': 'Specialise', 'learning': 'Apprentissage', 'desktop': 'Desktop'}
STATUS_LABELS = {'active': 'Actif', 'archived': 'Archive'}

# Pages statiques pour le sitemap (path, changefreq, priority)
SITEMAP_PAGES = [
    ('/', 'weekly', '1.0'),
    ('/nos-offres', 'weekly', '0.95'),
    ('/livres/', 'weekly', '0.9'),
    ('/contact', 'weekly', '0.95'),
    ('/pro', 'monthly', '0.55'),
    ('/audit', 'weekly', '0.95'),
    ('/vitrines/', 'weekly', '0.85'),
    ('/processus', 'monthly', '0.75'),
    ('/metz', 'monthly', '0.80'),
    ('/portfolio', 'monthly', '0.55'),
    ('/projets', 'monthly', '0.50'),
    ('/statistiques', 'monthly', '0.40'),
    ('/analyse', 'monthly', '0.45'),
    ('/mentions-legales', 'yearly', '0.25'),
    ('/cgv', 'yearly', '0.25'),
    ('/cgu', 'yearly', '0.25'),
    ('/politique-confidentialite', 'yearly', '0.25'),
    ('/desabonnement', 'yearly', '0.20'),
]

# Coordonnées & SEO structuré (schema.org)
SEO_ORG_EMAIL = 'contact@danielcraft.fr'
SEO_LOCALITY = 'Metz'
SEO_POSTAL_CODE = '57000'
SEO_REGION = 'Grand Est'
SEO_GEO_LAT = 49.1193
SEO_GEO_LNG = 6.1757

# Correspondance page statique → fichier OG (scripts/generate_site_og_images.py)
OG_PAGE_FILE_SLUGS = {
    'index': 'home',
    'nos-offres': 'prestations',
    'prestations': 'prestations',
    'livres': 'home',
}

# Variables par défaut
DEFAULT_VARS = {
    'page_title': 'DanielCraft — Sites vitrines & visibilité web | Metz',
    'page_description': 'Sites clairs, visibilité Google et assistants intelligents pour artisans et commerces. Devis par e-mail, Metz & Lorraine.',
    'page_keywords': 'site vitrine Metz, visibilité Google, création site internet, assistant IA site web, DanielCraft Lorraine',
    'page_robots': 'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1',
    'site_base': SITE_BASE,
    'page_url': f'{SITE_BASE}/',
    # Image OG par défaut (home) - architecture dediee dans assets/images/og/
    'og_image': f'{SITE_BASE}/assets/images/og/home-1200x630.jpg',
    'og_type': 'website',
    'current_page': '',
    'page_scripts': [],
    'extra_css': None,
    'blog_enabled': True,
    'og_meta_profile': 'default',
    'og_image_width': '1200',
    'og_image_height': '630',
    'og_image_type': 'image/jpeg',
    'assets_version': '',
    'assets_query': '',
}


def compute_assets_version(assets_root: Path) -> str:
    """Version cache-bust pour CSS/JS locaux (mtime max → YYYYMMDDHHMM)."""
    mtimes: List[float] = []
    for sub in ('css', 'js'):
        folder = assets_root / sub
        if not folder.is_dir():
            continue
        for path in folder.rglob('*'):
            if path.is_file() and path.suffix.lower() in ('.css', '.js'):
                try:
                    mtimes.append(path.stat().st_mtime)
                except OSError:
                    pass
    if not mtimes:
        return datetime.now().strftime('%Y%m%d%H%M')
    return datetime.fromtimestamp(max(mtimes)).strftime('%Y%m%d%H%M')


def apply_assets_version_to_defaults(assets_root: Path) -> str:
    """Injecte assets_version / assets_query dans DEFAULT_VARS."""
    version = compute_assets_version(assets_root)
    DEFAULT_VARS['assets_version'] = version
    DEFAULT_VARS['assets_query'] = f'?v={version}'
    return version


def build_page_scripts_content(scripts: Optional[List[str]], assets_q: str = '') -> str:
    """Balises script defer avec cache-bust."""
    q = assets_q or DEFAULT_VARS.get('assets_query') or ''
    names = scripts if scripts else ['main.js']
    return '\n'.join(f'<script src="/assets/js/{name}{q}" defer></script>' for name in names)


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

    def _eval_template_condition(self, condition: str, vars_dict: Dict) -> bool:
        """Évalue une condition {% if ... %} simple (égalité ou variable truthy)."""
        condition = condition.strip()
        eq_match = re.match(r'^(\w+)\s*==\s*["\']([^"\']+)["\']$', condition)
        if eq_match:
            var_name, expected_value = eq_match.group(1), eq_match.group(2)
            return str(vars_dict.get(var_name, '')) == expected_value

        var_match = re.match(r'^(\w+)$', condition)
        if var_match:
            actual_value = vars_dict.get(var_match.group(1), '')
            if actual_value in (False, 'False', 'false', '', None, 0, '0'):
                return False
            if isinstance(actual_value, list):
                return len(actual_value) > 0
            return True

        return False

    def _render_if_block(self, condition: str, body: str, vars_dict: Dict) -> str:
        """Rend un bloc {% if %}...{% else %}?...{% endif %} sans if imbriqué."""
        parts = re.split(r'\{%\s*else\s*%\}', body, maxsplit=1)
        if_content = parts[0]
        else_content = parts[1] if len(parts) > 1 else ''
        return if_content if self._eval_template_condition(condition, vars_dict) else else_content

    def _find_if_blocks(self, content: str) -> List[Dict[str, Any]]:
        """Repère les blocs {% if %}…{% endif %} avec pile (endif appariés correctement)."""
        tag_re = re.compile(r'\{%\s*(if\s+(.+?)|else|endif)\s*%\}', re.DOTALL)
        stack: List[Dict[str, Any]] = []
        blocks: List[Dict[str, Any]] = []

        for m in tag_re.finditer(content):
            tag = (m.group(1) or '').strip()
            if tag.startswith('if'):
                stack.append({
                    'start': m.start(),
                    'condition': m.group(2).strip(),
                    'if_content_start': m.end(),
                    'else_pos': None,
                    'else_content_start': None,
                })
            elif tag == 'else':
                if stack:
                    stack[-1]['else_pos'] = m.start()
                    stack[-1]['else_content_start'] = m.end()
            elif tag == 'endif':
                if not stack:
                    continue
                item = stack.pop()
                end_pos = m.end()
                if item['else_pos'] is not None:
                    if_content = content[item['if_content_start']:item['else_pos']]
                    else_content = content[item['else_content_start']:m.start()]
                else:
                    if_content = content[item['if_content_start']:m.start()]
                    else_content = ''
                blocks.append({
                    'start': item['start'],
                    'end': end_pos,
                    'condition': item['condition'],
                    'if_content': if_content,
                    'else_content': else_content,
                })

        return blocks

    def process_conditions(self, content: str, vars_dict: Dict) -> str:
        """Traite les conditions {% if %} {% else %} {% endif %} (imbriquées, de l'intérieur vers l'extérieur)."""
        inner_if_pattern = re.compile(r'\{%\s*if\s+')
        max_iterations = 100

        for _ in range(max_iterations):
            blocks = self._find_if_blocks(content)
            target = None
            for block in blocks:
                combined = block['if_content'] + block['else_content']
                if not inner_if_pattern.search(combined):
                    target = block
                    break
            if target is None:
                break

            body = target['if_content']
            if target['else_content']:
                body = target['if_content'] + '{% else %}' + target['else_content']
            rendered = self._render_if_block(target['condition'], body, vars_dict)
            content = content[:target['start']] + rendered + content[target['end']:]

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
    html = re.sub(
        r'\s*<meta\s+name=["\']robots["\'][^>]*>\s*',
        '\n',
        html,
        flags=re.IGNORECASE,
    )
    html = re.sub(
        r'\s*<link\s+rel=["\']canonical["\'][^>]*>\s*',
        '\n',
        html,
        flags=re.IGNORECASE,
    )
    block = (
        f'\n  <!-- {_DEMO_PROTECTION_MARKER} -->\n'
        '  <meta name="robots" content="noindex, noarchive, nosnippet, noimageindex">\n'
        f'  <meta name="{_DEMO_PROTECTION_MARKER}" content="1">\n'
        '  <link rel="stylesheet" href="../../shared/demo-protection.css">\n'
        '  <script src="../../shared/demo-protection.js" defer></script>\n'
    )
    new_html, n = re.subn(r'</head>', block + r'</head>', html, count=1, flags=re.IGNORECASE)
    return new_html if n else html


def sync_assets_to_dist(assets_src: Path, assets_dst: Path) -> None:
    """
    Copie assets/ vers dist/assets/ sans supprimer tout le dossier.
    Evite les 404 sur /assets/js/*.js pendant un rebuild (serveur PHP encore actif).
    """
    if not assets_src.is_dir():
        return
    assets_dst.mkdir(parents=True, exist_ok=True)
    copied = 0
    for path in assets_src.rglob('*'):
        if not path.is_file():
            continue
        rel = path.relative_to(assets_src)
        dest = assets_dst / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        try:
            src_stat = path.stat()
            if dest.exists():
                dst_stat = dest.stat()
                if (
                    int(dst_stat.st_mtime) >= int(src_stat.st_mtime)
                    and dst_stat.st_size == src_stat.st_size
                ):
                    continue
            shutil.copy2(path, dest)
            copied += 1
        except (PermissionError, OSError):
            pass
    if copied:
        print(f"[OK] Assets synchronises vers {assets_dst} ({copied} fichier(s) mis a jour)")
    else:
        print(f"[OK] Assets deja a jour dans {assets_dst}")


def sync_api_to_dist(api_src: Path, api_dst: Path) -> None:
    """
    Copie api/ vers dist/api/ sans rmtree (fichiers PHP parfois verrouillés par php -S).
    """
    if not api_src.is_dir():
        return
    api_dst.mkdir(parents=True, exist_ok=True)
    copied = 0
    locked = 0
    src_files = {p.relative_to(api_src) for p in api_src.rglob('*') if p.is_file()}
    for rel in sorted(src_files):
        src_path = api_src / rel
        dest = api_dst / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        try:
            src_stat = src_path.stat()
            if dest.exists():
                dst_stat = dest.stat()
                if (
                    int(dst_stat.st_mtime) >= int(src_stat.st_mtime)
                    and dst_stat.st_size == src_stat.st_size
                ):
                    continue
            shutil.copy2(src_path, dest)
            copied += 1
        except (PermissionError, OSError):
            locked += 1
    for dest_path in api_dst.rglob('*'):
        if not dest_path.is_file():
            continue
        rel = dest_path.relative_to(api_dst)
        if rel in src_files:
            continue
        try:
            dest_path.unlink()
        except (PermissionError, OSError):
            locked += 1
    if copied:
        print(f"[OK] api/ synchronise vers {api_dst} ({copied} fichier(s) mis a jour)")
    elif locked:
        print(f"[WARN] api/ deja a jour dans {api_dst} ({locked} fichier(s) verrouille(s), ignore)")
    else:
        print(f"[OK] api/ deja a jour dans {api_dst}")


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
        f"Sitemap: {base}/sitemap-pages.xml\n"
        f"Sitemap: {base}/sitemap-vitrines.xml\n"
        f"Sitemap: {base}/sitemap-prestations.xml\n"
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


def generate_nginx_project_alias_redirects(output_dir: Path) -> None:
    """Genere un snippet nginx (301) pour les alias /projets/<slug> -> slug canonique."""
    aliases = load_project_slug_aliases()
    if not aliases:
        return
    lines = [
        '# Redirections 301 alias projets (genere par build.py — ne pas editer a la main)',
    ]
    for alias_slug, canonical_slug in sorted(aliases.items()):
        if alias_slug == canonical_slug:
            continue
        lines.append(f'location = /projets/{alias_slug} {{')
        lines.append(f'    return 301 /projets/{canonical_slug};')
        lines.append('}')
    (output_dir / 'nginx-project-aliases.conf').write_text('\n'.join(lines) + '\n', encoding='utf-8')


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


def _apply_seo_meta_limits(vars_dict: Dict) -> None:
    """Tronque titre, description et mots-clés pour les SERP et les réseaux sociaux."""
    title = str(vars_dict.get('page_title') or '').strip()
    if title:
        vars_dict['page_title'] = _truncate_meta_text(title, 60)
    desc = str(vars_dict.get('page_description') or '').strip()
    if desc:
        vars_dict['page_description'] = _truncate_meta_text(desc, 160)
    kw = str(vars_dict.get('page_keywords') or '').strip()
    if kw:
        vars_dict['page_keywords'] = _truncate_meta_text(kw, 280)


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

    _apply_seo_meta_limits(vars_dict)

    og_slug = _static_page_og_slug(page_name)
    resolved = _resolve_generated_og(
        og_slug,
        str(vars_dict.get('og_image') or DEFAULT_VARS['og_image']),
    )
    og_abs = _to_absolute_url(resolved)
    vars_dict['og_image'] = _og_image_url_with_cache_bust(og_abs)
    _apply_og_image_file_meta(vars_dict)
    title = str(vars_dict.get('page_title') or 'DanielCraft').strip()
    vars_dict['og_image_alt'] = _truncate_meta_text(
        f"Visuel de partage DanielCraft — {title}", 200
    )


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


def load_project_slug_aliases() -> Dict[str, str]:
    """Alias slug -> slug canonique (ex. ticket-caisse -> ticketcaisse)."""
    if not PROJECT_SLUG_ALIASES_JSON.is_file():
        return {}
    try:
        data = json.loads(PROJECT_SLUG_ALIASES_JSON.read_text(encoding='utf-8'))
    except (json.JSONDecodeError, OSError):
        return {}
    if not isinstance(data, dict):
        return {}
    out: Dict[str, str] = {}
    for alias, canonical in data.items():
        a = str(alias or '').strip()
        c = str(canonical or '').strip()
        if a and c and a != c:
            out[a] = c
    return out


def _render_project_alias_redirect_page(alias_slug: str, canonical_slug: str) -> str:
    """Page HTML legere : canonical + noindex + redirection client vers le slug canonique."""
    base = SITE_BASE.rstrip('/')
    target = f'{base}/projets/{canonical_slug}'
    title = f'Redirection vers {canonical_slug} — DanielCraft'
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <meta name="robots" content="noindex, follow">
  <link rel="canonical" href="{target}">
  <meta http-equiv="refresh" content="0;url={target}">
  <script>window.location.replace({json.dumps(target)});</script>
</head>
<body>
  <p>Cette URL a ete deplacee. <a href="{target}">Continuer vers le projet</a>.</p>
</body>
</html>
'''


def _render_catalog_redirect_page() -> str:
    """Ancien index /prestations/ → catalogue /nos-offres."""
    base = SITE_BASE.rstrip('/')
    target = f'{base}/nos-offres'
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Redirection vers Nos offres — DanielCraft</title>
  <meta name="robots" content="noindex, follow">
  <link rel="canonical" href="{target}">
  <meta http-equiv="refresh" content="0;url={target}">
  <script>window.location.replace({json.dumps(target)});</script>
</head>
<body>
  <p>Le catalogue est sur <a href="{target}">Nos offres</a>.</p>
</body>
</html>
'''


def write_prestations_catalog_redirect(output_dir: Path) -> None:
    """Ecrit prestations/index.html (redirect client) vers /nos-offres."""
    out = output_dir / 'prestations'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'index.html').write_text(_render_catalog_redirect_page(), encoding='utf-8')
    print('[OK] Redirection /prestations/ -> /nos-offres')


def load_vitrines() -> Optional[Dict[str, Any]]:
    """Charge le catalogue vitrines (YAML/JSON unique : src/data/vitrines.json)."""
    if not VITRINES_JSON.exists():
        return None
    with open(VITRINES_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)


def vitrine_slugs_for_sitemap() -> List[str]:
    """Slugs des fiches /vitrines/<slug>/ depuis le catalogue (ordre vitrines.json)."""
    data = load_vitrines()
    if not data or not isinstance(data.get('items'), list):
        return []
    out: List[str] = []
    for it in data['items']:
        slug = (it.get('slug') or '').strip()
        if slug:
            out.append(slug)
    return out


def _sitemap_url_line(base: str, path: str, lastmod: str, changefreq: str, priority: str) -> str:
    """Une entree <url> pour les sitemaps XML."""
    p = path if path.startswith('/') else f'/{path}'
    loc = f'{base.rstrip("/")}{p}'
    return (
        f'  <url><loc>{loc}</loc><lastmod>{lastmod}</lastmod>'
        f'<changefreq>{changefreq}</changefreq><priority>{priority}</priority></url>'
    )


def _truncate_meta_text(s: str, max_len: int) -> str:
    s = ' '.join((s or '').split())
    if len(s) <= max_len:
        return s
    return s[: max_len - 1].rstrip(' ,.;:') + '…'


def _assets_file_from_rel(rel_url: str) -> Path:
    """Convertit /assets/... en chemin local sous assets/."""
    rel = (rel_url or '').strip()
    if rel.startswith('/assets/'):
        rel = rel[len('/assets/'):]
    elif rel.startswith('assets/'):
        rel = rel[len('assets/'):]
    return BASE_DIR / 'assets' / rel.replace('/', os.sep)


def _og_image_file_meta(url: str) -> tuple[str, str, str]:
    """Largeur, hauteur et MIME réels du fichier OG local (pour Meta / Messenger)."""
    raw = (url or '').split('?')[0].split('#')[0]
    idx = raw.find('/assets/')
    if idx < 0:
        return '1200', '630', 'image/jpeg'
    local = _assets_file_from_rel(raw[idx:])
    if not local.is_file():
        return '1200', '630', 'image/jpeg'
    try:
        from PIL import Image

        with Image.open(local) as im:
            w, h = im.size
            fmt = (im.format or 'JPEG').upper()
            mime = {
                'JPEG': 'image/jpeg',
                'PNG': 'image/png',
                'WEBP': 'image/webp',
                'GIF': 'image/gif',
            }.get(fmt, 'image/jpeg')
            return str(w), str(h), mime
    except OSError:
        return '1200', '630', 'image/jpeg'


def _apply_og_image_file_meta(vars_dict: Dict) -> None:
    """Injecte og:image:width/height/type depuis le fichier réel."""
    og_url = str(vars_dict.get('og_image') or '')
    w, h, mime = _og_image_file_meta(og_url)
    vars_dict['og_image_width'] = w
    vars_dict['og_image_height'] = h
    vars_dict['og_image_type'] = mime
    # Alias vitrine (head.html historique)
    vars_dict['vitrine_og_image_width'] = w
    vars_dict['vitrine_og_image_height'] = h
    vars_dict['vitrine_og_image_type'] = mime


def _og_image_url_with_cache_bust(url: str) -> str:
    """
    Ajoute ?v=mtime sur les images OG locales pour invalider le cache Facebook/LinkedIn/X.
    Recommande apres regeneration des visuels (referencement social).
    """
    raw = (url or '').strip()
    if not raw:
        return raw
    path_only = raw.split('?')[0].split('#')[0]
    idx = path_only.find('/assets/')
    if idx < 0:
        return raw
    rel = path_only[idx:]
    local = _assets_file_from_rel(rel)
    if not local.is_file():
        return raw
    try:
        mtime = datetime.fromtimestamp(local.stat().st_mtime).strftime('%Y%m%d%H%M')
    except OSError:
        return raw
    return f"{path_only}?v={mtime}"


def _generated_og_rel(page_or_slug: str, *, subdir: str = '') -> str:
    """Chemin relatif web vers une image OG 1200x630 generee."""
    if subdir:
        return f'/assets/images/og/{subdir}/{page_or_slug}-1200x630.jpg'
    return f'/assets/images/og/{page_or_slug}-1200x630.jpg'


def _resolve_generated_og(page_or_slug: str, fallback: str, *, subdir: str = '') -> str:
    """Utilise l'image OG generee si le fichier existe, sinon le fallback."""
    rel = _generated_og_rel(page_or_slug, subdir=subdir)
    if _assets_file_from_rel(rel).is_file():
        return rel
    return fallback


def _static_page_og_slug(page_name: str) -> str:
    return OG_PAGE_FILE_SLUGS.get(page_name, page_name)


def _vitrine_og_mime_from_url(url: str) -> str:
    u = (url or '').lower()
    if u.endswith('.webp'):
        return 'image/webp'
    if u.endswith('.png'):
        return 'image/png'
    return 'image/jpeg'


def _vitrine_og_dims_from_url(url: str) -> tuple[str, str]:
    """Extrait largeur × hauteur depuis un nom du type desktop_1920x2400.webp (sinon 1600×900)."""
    m = re.search(r'_(\d+)x(\d+)\.(webp|jpe?g|png)', url or '', re.I)
    if m:
        return m.group(1), m.group(2)
    return '1600', '900'


# Textes marketing page fiche vitrine : variantes par catégorie (personnalisation secteur).
# Placeholders : __TITLE__ (nom vitrine échappé), __TAG__ (sous-titre échappé), __DEMO__ (lien HTML démo).
_VITRINE_SECTOR_COPY: Dict[str, Dict[str, str]] = {
    'retail': {
        'shots_title': 'Visuels commerce & drive prêts pour Google et les réseaux sociaux',
        'shots_lead': (
            'Pour <strong>__TITLE__</strong> — <strong>__TAG__</strong> — chaque cadre montre une '
            '<strong>capture pleine page</strong> (scrollable) comme vos clients la parcourent sur '
            '<strong>ordinateur</strong>, <strong>tablette</strong> et <strong>smartphone</strong>. '
            'Idéal pour rassurer sur le rendu en magasin virtuel et alimenter vos partages Meta ou LinkedIn. '
            'Ouvrez la capture en grand ou explorez la __DEMO__ pour un parcours réaliste.'
        ),
        'marketing_h2': 'Conversion commerce, rayons et prise de contact',
        'included': (
            'Une <strong>maquette de site</strong> déjà structurée pour <strong>vendre en ligne</strong> : '
            'offres, preuves, appels à l’action et parcours contact — vous remplacez les textes d’exemple par '
            'les vôtres pour <strong>__TITLE__</strong> et vos visuels produits. Parfait pour <strong>tester '
            'votre discours retail</strong> (drive, horaires, fidélité) avant d’industrialiser avec moi le '
            'tunnel d’acquisition, le paiement ou le back-office.'
        ),
    },
    'tech': {
        'shots_title': 'Visuels produit & SaaS prêts pour Google, LinkedIn et pitch deck',
        'shots_lead': (
            'Pour <strong>__TITLE__</strong> — <strong>__TAG__</strong> — chaque cadre reproduit une '
            '<strong>capture pleine page</strong> scrollable sur <strong>ordinateur</strong>, '
            '<strong>tablette</strong> et <strong>smartphone</strong>. Utile pour un post LinkedIn, une annonce '
            'Google ou une slide investisseur. Ouvrez la capture en plein écran ou parcourez la __DEMO__ '
            'comme un décideur technique.'
        ),
        'marketing_h2': 'Parcours produit, preuves et conversion côté tech',
        'included': (
            'Une <strong>maquette de site</strong> pensée comme un <strong>site produit</strong> : '
            'navigation claire, blocs preuve, FAQ et appels à l’action vers <strong>démo ou contact</strong>. '
            'Pour <strong>__TITLE__</strong>, vous substituez textes et captures puis présentez le rendu à vos '
            'prospects avant d’investir dans l’<strong>API</strong>, l’<strong>auth</strong> ou la '
            '<strong>tarification</strong> sur mesure.'
        ),
    },
    'services': {
        'shots_title': 'Captures prêtes pour vendre vos prestations (Meta, LinkedIn, Google)',
        'shots_lead': (
            '<strong>__TITLE__</strong> — <strong>__TAG__</strong> : les captures déroulent le parcours comme '
            'chez un <strong>client B2B</strong> — offres, galerie, FAQ et prise de contact. Idéal pour rassurer '
            'sur le ton pro et alimenter vos campagnes. Ouvrez une capture en grand ou testez la __DEMO__ '
            'bout en bout.'
        ),
        'marketing_h2': 'Crédibilité terrain, devis et prise de contact B2B',
        'included': (
            'Une <strong>maquette de site</strong> qui met en scène vos <strong>prestations</strong>, '
            'vos <strong>références</strong> et un <strong>parcours devis</strong> lisible. Pour '
            '<strong>__TITLE__</strong>, vous adaptez les formulations à votre métier (facility, conciergerie, '
            'multi-sites…) puis vous validez le discours commercial avant de brancher vos outils métiers ou '
            'votre CRM.'
        ),
    },
    'hcr': {
        'shots_title': 'Visuels restauration prêts pour réseaux sociaux et réservation',
        'shots_lead': (
            'Pour <strong>__TITLE__</strong> — <strong>__TAG__</strong> — les cadres montrent le rendu '
            '<strong>pleine page</strong> sur <strong>ordinateur</strong>, <strong>tablette</strong> et '
            '<strong>mobile</strong> : carte, ambiance, réservation. Parfait pour donner envie sur Instagram '
            'ou Meta et rassurer sur le site. Ouvrez la capture ou la __DEMO__ comme un convive.'
        ),
        'marketing_h2': 'Carte, ambiance et conversion réservation',
        'included': (
            'Une <strong>maquette de site</strong> orientée <strong>HCR</strong> : photos, menus, horaires '
            'et <strong>appel à la réservation</strong>. Pour <strong>__TITLE__</strong>, vous remplacez textes '
            'et visuels puis testez votre promesse (brasserie, traiteur, bar…) avant de connecter votre '
            'moteur de réservation ou votre téléphonie.'
        ),
    },
    'formation': {
        'shots_title': 'Captures formation prêtes pour Google Ads et réseaux pros',
        'shots_lead': (
            '<strong>__TITLE__</strong> — <strong>__TAG__</strong> : chaque cadre présente une '
            '<strong>capture scrollable</strong> desktop / tablette / mobile pour montrer parcours, modules '
            'et confiance pédagogique. Ouvrez la capture en grand ou la __DEMO__ pour simuler l’inscription.'
        ),
        'marketing_h2': 'Parcours apprenant, modules et inscription',
        'included': (
            'Une <strong>maquette de site</strong> pensée <strong>formation</strong> : parcours clair, '
            'niveaux, preuves et <strong>prise de contact</strong>. Pour <strong>__TITLE__</strong>, vous '
            'personnalisez les intitulés et visuels campus avant de brancher votre LMS, votre paiement ou votre '
            'outil de gestion des sessions.'
        ),
    },
    'hotel': {
        'shots_title': 'Visuels hôtellerie prêts pour réservation et réseaux sociaux',
        'shots_lead': (
            'Pour <strong>__TITLE__</strong> — <strong>__TAG__</strong> — les captures pleine page montrent '
            'chambres, offres et <strong>parcours réservation</strong> sur tous les écrans. Idéal pour '
            'campagnes Google Hôtels ou posts Instagram. Ouvrez la capture ou la __DEMO__ comme un voyageur.'
        ),
        'marketing_h2': 'Chambres, expérience et conversion réservation',
        'included': (
            'Une <strong>maquette de site</strong> type <strong>grand hôtel</strong> : gammes de chambres, '
            'spa, séminaires et CTA réservation. Pour <strong>__TITLE__</strong>, vous adaptez textes et '
            'visuels puis validez le discours avant de connecter votre moteur de réservation ou votre PMS.'
        ),
    },
    'beaute': {
        'shots_title': 'Captures institut & spa prêtes pour Meta, Google et prise de RDV',
        'shots_lead': (
            '<strong>__TITLE__</strong> — <strong>__TAG__</strong> : les cadres scrollables montrent '
            'soins, ambiance et <strong>demande de rendez-vous</strong> sur desktop, tablette et mobile. '
            'Ouvrez la capture ou la __DEMO__ pour un parcours client réaliste.'
        ),
        'marketing_h2': 'Soins, confiance et conversion rendez-vous',
        'included': (
            'Une <strong>maquette de site</strong> pour <strong>beauté & bien-être</strong> : fiches soins, '
            'engagements et formulaire RDV. Pour <strong>__TITLE__</strong>, vous remplacez textes et photos '
            'puis testez votre promesse avant de brancher votre agenda ou votre logiciel métier.'
        ),
    },
    'mobilite': {
        'shots_title': 'Visuels garage & mobilité prêts pour Google Business et réseaux',
        'shots_lead': (
            'Pour <strong>__TITLE__</strong> — <strong>__TAG__</strong> — chaque cadre montre une '
            '<strong>capture pleine page</strong> : services, atelier et <strong>prise de RDV</strong>. '
            'Ouvrez la capture en grand ou la __DEMO__ comme un automobiliste.'
        ),
        'marketing_h2': 'Prestations atelier et prise de rendez-vous',
        'included': (
            'Une <strong>maquette de site</strong> orientée <strong>atelier</strong> : expertises, visuels '
            'véhicules et <strong>formulaire RDV</strong>. Pour <strong>__TITLE__</strong>, vous adaptez '
            'offres (pneus, carrosserie, révision…) puis validez le message avant de connecter votre planning '
            'ou votre téléphonie.'
        ),
    },
    'artisanat': {
        'shots_title': 'Captures boutique artisanale prêtes pour réseaux sociaux et SEO local',
        'shots_lead': (
            '<strong>__TITLE__</strong> — <strong>__TAG__</strong> : les cadres pleine page valorisent '
            'produits, origines et <strong>parcours commande</strong> sur tous les écrans. Ouvrez la capture '
            'ou la __DEMO__ pour simuler l’achat.'
        ),
        'marketing_h2': 'Histoire de maison, coffrets et conversion',
        'included': (
            'Une <strong>maquette de site</strong> pour <strong>commerce artisanal</strong> : galerie, '
            'storytelling et FAQ coffrets. Pour <strong>__TITLE__</strong>, vous remplacez textes et visuels '
            'produits avant de brancher votre caisse en ligne ou votre logistique.'
        ),
    },
    'sante': {
        'shots_title': 'Visuels cabinet & santé prêts pour rassurer (web et réseaux)',
        'shots_lead': (
            'Pour <strong>__TITLE__</strong> — <strong>__TAG__</strong> — les captures scrollables montrent '
            'un parcours <strong>clair et rassurant</strong> sur ordinateur, tablette et mobile (tarifs, '
            'parcours patient, contact). Ouvrez la capture ou la __DEMO__ comme un patient.'
        ),
        'marketing_h2': 'Lisibilité, confiance et prise de contact soignée',
        'included': (
            'Une <strong>maquette de site</strong> adaptée <strong>santé</strong> : repères tarifaires, '
            'prévention et <strong>demande de rappel</strong>. Pour <strong>__TITLE__</strong>, vous '
            'personnalisez les contenus médicaux avec votre équipe puis branchez votre secrétariat ou votre '
            'outil de prise de rendez-vous conforme au cadre légal.'
        ),
    },
    'finance': {
        'shots_title': 'Captures institutionnelles prêtes pour confiance et campagnes',
        'shots_lead': (
            '<strong>__TITLE__</strong> — <strong>__TAG__</strong> : les cadres pleine page montrent un '
            'parcours <strong>sobre et structuré</strong> sur tous les écrans. Ouvrez la capture ou la '
            '__DEMO__ pour valider le ton institutionnel.'
        ),
        'marketing_h2': 'Offres, transparence et prise de contact mesurée',
        'included': (
            'Une <strong>maquette de site</strong> pour <strong>finance & banque</strong> : offres comparables, '
            'repères agences et CTA contact. Pour <strong>__TITLE__</strong>, vous adaptez formulations et '
            'mentions réglementaires avec votre conformité avant toute mise en production.'
        ),
    },
    'industrie': {
        'shots_title': 'Visuels industriels prêts pour B2B, Google et salons',
        'shots_lead': (
            'Pour <strong>__TITLE__</strong> — <strong>__TAG__</strong> — chaque cadre montre une '
            '<strong>capture pleine page</strong> : capacités, qualité et <strong>demande de devis</strong>. '
            'Ouvrez la capture ou la __DEMO__ comme un donneur d’ordre.'
        ),
        'marketing_h2': 'Savoir-faire machine et conversion devis',
        'included': (
            'Une <strong>maquette de site</strong> orientée <strong>industrie</strong> : process, équipements '
            'et FAQ techniques. Pour <strong>__TITLE__</strong>, vous remplacez textes et preuves puis '
            'validez le discours commercial avant de connecter votre ERP ou votre pipeline commercial.'
        ),
    },
    'conseil': {
        'shots_title': 'Captures cabinet conseil prêtes pour LinkedIn et prospection',
        'shots_lead': (
            '<strong>__TITLE__</strong> — <strong>__TAG__</strong> : les captures scrollables présentent '
            'méthode, offres et <strong>prise de contact</strong> sur desktop, tablette et mobile. Ouvrez la '
            'capture ou la __DEMO__ pour un parcours dirigeant.'
        ),
        'marketing_h2': 'Expertise, packs et prise de rendez-vous',
        'included': (
            'Une <strong>maquette de site</strong> pour <strong>cabinets & conseil</strong> : méthode, '
            'forfaits et CTA bilan flash ou RDV. Pour <strong>__TITLE__</strong>, vous adaptez les messages à '
            'votre cible (TPE, associations, filiales…) avant de brancher votre agenda ou votre CRM.'
        ),
    },
    'ess': {
        'shots_title': 'Visuels association prêts pour mobilisation et campagnes',
        'shots_lead': (
            'Pour <strong>__TITLE__</strong> — <strong>__TAG__</strong> — les cadres montrent mission, '
            'actions et <strong>engagement</strong> (dons, bénévolat) sur tous les écrans. Ouvrez la capture '
            'ou la __DEMO__ comme un sympathisant.'
        ),
        'marketing_h2': 'Mobilisation, dons et bénévolat',
        'included': (
            'Une <strong>maquette de site</strong> pour <strong>ESS & associations</strong> : campagnes, '
            'preuves d’impact et formulaires engagement. Pour <strong>__TITLE__</strong>, vous remplacez textes '
            'et visuels terrain avant de connecter votre outil de dons ou votre mailing.'
        ),
    },
    'immobilier': {
        'shots_title': 'Visuels immobilier prêts pour mandats et réseaux sociaux',
        'shots_lead': (
            'Pour <strong>__TITLE__</strong> — <strong>__TAG__</strong> — chaque capture pleine page montre '
            'biens, services et <strong>estimation</strong> sur desktop, tablette et mobile. Ouvrez la capture '
            'ou la __DEMO__ comme un vendeur ou un acquéreur.'
        ),
        'marketing_h2': 'Biens, crédibilité locale et conversion estimation',
        'included': (
            'Une <strong>maquette de site</strong> type <strong>agence immobilière</strong> : sélection de biens, '
            'équipe et formulaire d’estimation. Pour <strong>__TITLE__</strong>, vous remplacez annonces et visuels '
            'avant de brancher votre CRM ou vos portails partenaires.'
        ),
    },
    'juridique': {
        'shots_title': 'Captures cabinet prêtes pour LinkedIn et prospection B2B',
        'shots_lead': (
            '<strong>__TITLE__</strong> — <strong>__TAG__</strong> : parcours sobre expertises, méthode et '
            '<strong>contact</strong> sur tous les écrans. Ouvrez la capture ou la __DEMO__ comme un dirigeant.'
        ),
        'marketing_h2': 'Expertises, méthode et prise de rendez-vous',
        'included': (
            'Une <strong>maquette de site</strong> pour <strong>cabinet d’avocats</strong> : domaines, équipe et '
            'FAQ. Pour <strong>__TITLE__</strong>, vous adaptez les contenus avec votre conformité avant toute '
            'mise en ligne.'
        ),
    },
    'architecture': {
        'shots_title': 'Visuels atelier prêts pour concours et portfolios',
        'shots_lead': (
            'Pour <strong>__TITLE__</strong> — <strong>__TAG__</strong> — les cadres scrollables valorisent '
            'projets et <strong>approche</strong> sur tous les écrans. Ouvrez la capture ou la __DEMO__ '
            'comme un maître d’ouvrage.'
        ),
        'marketing_h2': 'Projets, méthode et brief contact',
        'included': (
            'Une <strong>maquette de site</strong> type <strong>atelier d’architecture</strong> : réalisations, '
            'process et formulaire brief. Pour <strong>__TITLE__</strong>, vous intégrez vos visuels chantier '
            'et livrables avant de connecter votre outil de gestion de projet.'
        ),
    },
    'sport': {
        'shots_title': 'Captures salle de sport prêtes pour inscription et réseaux',
        'shots_lead': (
            '<strong>__TITLE__</strong> — <strong>__TAG__</strong> : les cadres montrent cours, tarifs et '
            '<strong>essai gratuit</strong> sur desktop, tablette et mobile. Ouvrez la capture ou la __DEMO__ '
            'comme un futur adhérent.'
        ),
        'marketing_h2': 'Cours, formules et conversion essai',
        'included': (
            'Une <strong>maquette de site</strong> pour <strong>fitness & sport</strong> : planning, offres et '
            'inscription. Pour <strong>__TITLE__</strong>, vous remplacez textes et visuels avant de brancher '
            'votre logiciel d’abonnement ou votre agenda cours.'
        ),
    },
    'creatif': {
        'shots_title': 'Visuels portfolio prêts pour réseaux et book client',
        'shots_lead': (
            'Pour <strong>__TITLE__</strong> — <strong>__TAG__</strong> — chaque capture pleine page met en '
            'scène votre <strong>portfolio</strong> et vos prestations sur tous les écrans. Ouvrez la capture '
            'ou la __DEMO__ comme un client en recherche de photographe.'
        ),
        'marketing_h2': 'Portfolio, prestations et prise de contact',
        'included': (
            'Une <strong>maquette de site</strong> type <strong>créatif / photographe</strong> : galerie masonry, '
            'offres et contact. Pour <strong>__TITLE__</strong>, vous remplacez séries et tarifs avant de '
            'connecter votre galerie privée ou votre CRM.'
        ),
    },
}


def _vitrine_body_copy(it: Dict[str, Any], price: int, demo_rel_url: str) -> Dict[str, str]:
    """
    Paragraphes visibles fiche vitrine : variantes par catégorie + overrides optionnels dans vitrines.json.
    Overrides (HTML de confiance, catalogue statique) : copy_shots_html, copy_included_html, copy_delivery_html.
    Titres optionnels échappés : copy_shots_section_title, copy_marketing_h2.
    """
    cat = (it.get('category') or 'retail').strip() or 'retail'
    if cat not in VITRINE_CATEGORY_LABELS:
        cat = 'retail'
    title_plain = (it.get('title') or '').strip()
    tag_plain = (it.get('tagline') or '').strip()
    title_e = html.escape(title_plain) or 'ce modèle'
    tag_e = html.escape(tag_plain) or 'votre positionnement'
    demo_a = (
        f'<a href="{html.escape(demo_rel_url, quote=True)}" class="vitrine-prose-link vitrine-prose-link--demo" '
        'target="_blank" rel="noopener noreferrer">démo live</a>'
    )
    contact_a = '<a href="/#contact" class="vitrine-prose-link">formulaire sur l’accueil</a>'
    sector = _VITRINE_SECTOR_COPY.get(cat, _VITRINE_SECTOR_COPY['retail'])

    shots_title = (it.get('copy_shots_section_title') or '').strip() or sector['shots_title']
    shots_title = html.escape(shots_title)

    if (it.get('copy_shots_html') or '').strip():
        shots_html = str(it['copy_shots_html']).strip()
    else:
        lead = (
            sector['shots_lead']
            .replace('__TITLE__', title_e)
            .replace('__TAG__', tag_e)
            .replace('__DEMO__', demo_a)
        )
        shots_html = f'<p class="section-description vitrine-prose">{lead}</p>'

    marketing_h2 = (it.get('copy_marketing_h2') or '').strip() or sector['marketing_h2']
    marketing_h2 = html.escape(marketing_h2)

    if (it.get('copy_included_html') or '').strip():
        included_html = str(it['copy_included_html']).strip()
    else:
        inc = sector['included'].replace('__TITLE__', title_e)
        included_html = f'<p class="vitrine-included-lead vitrine-prose">{inc}</p>'

    if (it.get('copy_delivery_html') or '').strip():
        delivery_html = str(it['copy_delivery_html']).strip()
    else:
        delivery_html = (
            '<div class="vitrine-detail-note box-soft vitrine-prose">'
            '<p><strong>Livraison & visibilité</strong> : <strong>fichiers sources</strong> prêts à '
            'héberger — <strong>aucune base de données</strong> requise. Les formulaires sont des '
            '<strong>maquettes</strong> (branchement e-mail, CRM ou paiement sur devis). Les captures de cette '
            f'fiche illustrent le rendu pour <strong>{title_e}</strong> ; elles peuvent être régénérées après '
            'vos contenus définitifs. Pour installation, domaine ou hébergement, utilisez le bloc à droite ou '
            f'{contact_a}.</p>'
            '</div>'
        )

    seo_line = (
        f'Démo live, pack visuels multi-écrans et sources prêtes au déploiement · à partir de {price} € HT'
    )

    return {
        'vitrine_seo_line': seo_line,
        'vitrine_shots_section_title': shots_title,
        'vitrine_copy_shots_html': shots_html,
        'vitrine_copy_marketing_h2': marketing_h2,
        'vitrine_copy_included_html': included_html,
        'vitrine_copy_delivery_html': delivery_html,
    }


def _build_vitrine_seo_bundle(
    it: Dict[str, Any],
    slug: str,
    price: int,
    page_url_abs: str,
    og_image_abs: str,
    shot_desk_abs: str,
    shot_tab_abs: str,
    shot_mob_abs: str,
    stack: List[str],
) -> Dict[str, Any]:
    """Titres, meta, alts images et JSON-LD (Product + WebPage + fil d'Ariane) orientés SEO / partage social."""
    cat = (it.get('category') or 'all').strip() or 'all'
    cat_label = VITRINE_CATEGORY_LABELS.get(cat, cat.replace('_', ' ').title())
    title = (it.get('title') or slug).strip()
    tagline = (it.get('tagline') or '').strip()
    excerpt = (it.get('excerpt') or tagline or '').strip()
    stack_bits = ', '.join(str(s) for s in stack[:8]) if stack else 'HTML5, CSS3, JavaScript'

    custom_title = (it.get('seo_title') or '').strip()
    suffix = ' | DanielCraft'
    if custom_title:
        page_title = _truncate_meta_text(custom_title + suffix, 70)
    else:
        # Titre complet (nom du modèle lisible dans l’onglet) — pas de troncature au milieu du nom.
        compact = f'{title} — {cat_label}{suffix}'
        if len(compact) <= 70:
            page_title = compact
        else:
            page_title = f'{title}{suffix}'
            if len(page_title) > 70:
                page_title = _truncate_meta_text(page_title, 70)

    custom_desc = (it.get('seo_description') or '').strip()
    desc = custom_desc or (
        f'{excerpt} '
        f'Démo interactive + captures desktop, tablette et mobile. '
        f'Maquette {stack_bits} livrable. Dès {price} € HT — DanielCraft Lorraine.'
    )
    page_description = _truncate_meta_text(desc, 158)

    kw_parts = [
        'modèle site web professionnel',
        'maquette web responsive',
        'landing page secteur',
        cat_label.lower(),
        title.lower(),
        slug.replace('-', ' '),
        'démo site web',
        'capture site desktop mobile',
        'achat maquette site',
        'DanielCraft Metz',
    ] + [str(s).lower() for s in stack[:6]]
    seen: set[str] = set()
    kw_unique = []
    for k in kw_parts:
        k = k.strip()
        if k and k not in seen:
            seen.add(k)
            kw_unique.append(k)
    page_keywords = _truncate_meta_text(', '.join(kw_unique), 280)

    vitrine_og_image_alt = _truncate_meta_text(
        f'{title} — secteur {cat_label} : capture pleine page desktop (partage LinkedIn, Facebook, Google).',
        190,
    )
    ow, oh, _om = _og_image_file_meta(og_image_abs)
    vitrine_img_alt_desktop = _truncate_meta_text(
        f'Maquette « {title} » — capture desktop scrollable, secteur {cat_label}, blocs conversion.',
        130,
    )
    vitrine_img_alt_tablet = _truncate_meta_text(
        f'« {title} » — rendu tablette, navigation et offres mises en avant.',
        130,
    )
    vitrine_img_alt_mobile = _truncate_meta_text(
        f'« {title} » — version mobile, lisibilité et prise de contact rapide.',
        130,
    )

    hero_badge = f'Modèle de site pro · {cat_label}'

    return {
        'page_title': page_title,
        'page_description': page_description,
        'page_keywords': page_keywords,
        'schema_type': 'vitrine',
        'og_meta_profile': 'vitrine',
        'vitrine_hero_badge': hero_badge,
        'vitrine_category_label': cat_label,
        'vitrine_og_image_alt': vitrine_og_image_alt,
        'vitrine_og_image_width': ow,
        'vitrine_og_image_height': oh,
        'vitrine_og_image_type': _vitrine_og_mime_from_url(og_image_abs),
        'vitrine_img_alt_desktop': vitrine_img_alt_desktop,
        'vitrine_img_alt_tablet': vitrine_img_alt_tablet,
        'vitrine_img_alt_mobile': vitrine_img_alt_mobile,
    }


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


def publish_catalog_json_for_api(output_dir: Path) -> None:
    """Copie src/data/vitrines.json vers dist/data/ et api/data/ (PHP Stripe + checkout)."""
    if not VITRINES_JSON.is_file():
        return
    for dest_root in (output_dir / 'data', BASE_DIR / 'api' / 'data'):
        dest_root.mkdir(parents=True, exist_ok=True)
        shutil.copy2(VITRINES_JSON, dest_root / 'vitrines.json')
    print('[OK] Catalogue vitrines copie vers data/ et api/data/')


def format_audit_price_eur_display(value) -> str:
    """Affichage FR du prix audit TTC (ex. 199)."""
    try:
        n = float(value) if value is not None else 199
    except (TypeError, ValueError):
        n = 199
    if n <= 0:
        n = 199
    if abs(n - round(n)) < 0.001:
        return str(int(round(n)))
    return f'{n:.2f}'.replace('.', ',')


def load_audits_config() -> Dict:
    """Charge src/data/audits.json (offres audit payant)."""
    if not AUDITS_JSON.is_file():
        return {}
    try:
        data = json.loads(AUDITS_JSON.read_text(encoding='utf-8'))
        return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, OSError):
        return {}


def publish_audits_json_for_api(output_dir: Path) -> None:
    """Copie src/data/audits.json vers dist/data/ et api/data/ (Stripe audit)."""
    if not AUDITS_JSON.is_file():
        return
    for dest_root in (output_dir / 'data', BASE_DIR / 'api' / 'data'):
        dest_root.mkdir(parents=True, exist_ok=True)
        shutil.copy2(AUDITS_JSON, dest_root / 'audits.json')
    print('[OK] Catalogue audits copie vers data/ et api/data/')


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
        # Index racine réservé à la page catalogue DanielCraft (générée après copie).
        (out / 'hub-bulma.html').write_text(hub_text, encoding='utf-8')
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


def _vitrines_distinct_category_keys(items: List[Dict[str, Any]]) -> List[str]:
    seen: set = set()
    cats: List[str] = []
    for it in items:
        c = (it.get('category') or '').strip()
        if c and c not in seen:
            seen.add(c)
            cats.append(c)
    return sorted(cats)


def _vitrines_catalog_inner_lines(items: List[Dict[str, Any]], cats: List[str]) -> List[str]:
    """Filtres + grille cartes + note de pied (même indentation que dans .container)."""
    lines: List[str] = []
    lines.append('        <div class="vitrines-toolbar scroll-reveal">')
    lines.append('            <label class="vitrines-filter-select-wrap" for="vitrineFilterSelect">')
    lines.append('                <span class="vitrines-filter-select-label">Choisir mon secteur</span>')
    lines.append('                <select class="vitrines-filter-select" id="vitrineFilterSelect" aria-label="Filtrer par secteur">')
    lines.append('                    <option value="all">Tous les secteurs</option>')
    for c in cats:
        label = VITRINE_CATEGORY_LABELS.get(c, c.replace('_', ' ').title())
        lines.append(
            f'                    <option value="{html.escape(c)}">{html.escape(label)}</option>'
        )
    lines.append('                </select>')
    lines.append('            </label>')
    lines.append('            <div class="vitrines-filter vitrines-filter--featured" role="group" aria-label="Secteurs phares">')
    lines.append('                <button type="button" class="vitrines-filter-btn active" data-vitrine-filter="all">Tous</button>')
    for c in VITRINE_FEATURED_FILTER_KEYS:
        if c not in cats:
            continue
        label = VITRINE_CATEGORY_LABELS.get(c, c.replace('_', ' ').title())
        lines.append(
            f'                <button type="button" class="vitrines-filter-btn" '
            f'data-vitrine-filter="{html.escape(c)}">{html.escape(label)}</button>'
        )
    lines.append('            </div>')
    lines.append('            <div class="vitrines-filter vitrines-filter--extended" role="group" aria-label="Tous les secteurs" hidden>')
    for c in cats:
        if c in VITRINE_FEATURED_FILTER_KEYS:
            continue
        label = VITRINE_CATEGORY_LABELS.get(c, c.replace('_', ' ').title())
        lines.append(
            f'                <button type="button" class="vitrines-filter-btn" '
            f'data-vitrine-filter="{html.escape(c)}">{html.escape(label)}</button>'
        )
    lines.append('            </div>')
    lines.append('            <button type="button" class="vitrines-filter-more" id="vitrineFilterMore" aria-expanded="false">Voir plus de secteurs</button>')
    lines.append('        </div>')
    lines.append('        <div class="vitrines-grid" id="vitrinesGrid">')
    idx = 0
    for it in items:
        slug = (it.get('slug') or '').strip()
        if not slug:
            continue
        cat = (it.get('category') or 'all').strip() or 'all'
        title_raw = (it.get('title') or slug).strip()
        title = html.escape(title_raw)
        card_cta = html.escape(f'Voir {title_raw}')
        tagline = html.escape(it.get('tagline') or '')
        excerpt = html.escape(it.get('excerpt') or '')
        _a_thumb = _vitrine_screenshot_paths(slug, 'desktop')[2]
        thumb = _a_thumb or '/assets/images/og/home-1200x630.jpg'
        cat_label = html.escape(VITRINE_CATEGORY_LABELS.get(cat, cat))
        delay = min(idx * 40, 400)
        idx += 1
        lines.append(
            f'        <article class="vitrine-card scroll-reveal" data-vitrine-cat="{html.escape(cat)}" '
            f'style="--reveal-delay:{delay}ms">'
        )
        lines.append(
            f'            <a class="vitrine-card-media" href="/vitrines/{html.escape(slug)}/" '
            f'aria-label="{card_cta}">'
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
            f'{card_cta}</a>'
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
        'Modèle catalogue à partir de 42&nbsp;€ HT — ou <a href="/prestations/site-vitrine/">site sur mesure à 490&nbsp;€ HT</a>.</p>'
    )
    return lines


def build_home_vitrines_teaser_embed() -> None:
    """Fragment léger accueil : 3 exemples vitrine (+ 1 tablette paysage uniquement)."""
    data = load_vitrines()
    path_out = INCLUDES_DIR / 'home-vitrines-teaser.html'
    if not data or not data.get('items'):
        path_out.write_text('', encoding='utf-8')
        print('[WARN] home-vitrines-teaser.html : pas de donnees vitrines')
        return

    by_slug = {
        (it.get('slug') or '').strip(): it
        for it in data.get('items', [])
        if (it.get('slug') or '').strip()
    }

    def _teaser_card(slug: str, extra_class: str = '') -> str:
        it = by_slug.get(slug)
        if not it:
            return ''
        title = html.escape((it.get('title') or slug).strip())
        tagline = html.escape((it.get('tagline') or '').strip())
        cat = (it.get('category') or '').strip()
        cat_label = html.escape(VITRINE_CATEGORY_LABELS.get(cat, cat.replace('_', ' ').title()))
        thumb = _vitrine_screenshot_paths(slug, 'desktop')[2] or '/assets/images/og/home-1200x630.jpg'
        demo_url = f'/vitrines/{html.escape(slug)}/demo/index.html'
        fiche_url = f'/vitrines/{html.escape(slug)}/'
        cls = f'home-vitrine-teaser scroll-reveal{extra_class}'
        return (
            f'<article class="{cls}">'
            f'<a class="home-vitrine-teaser-media" href="{demo_url}" target="_blank" rel="noopener noreferrer">'
            f'<img src="{html.escape(thumb)}" alt="" width="640" height="400" loading="lazy" decoding="async">'
            f'<span class="home-vitrine-teaser-cat">{cat_label}</span>'
            f'</a>'
            f'<div class="home-vitrine-teaser-body">'
            f'<h3 class="home-vitrine-teaser-title">{title}</h3>'
            f'<p class="home-vitrine-teaser-tagline">{tagline}</p>'
            f'<div class="home-vitrine-teaser-actions">'
            f'<a class="btn btn-primary btn-sm" href="{demo_url}" target="_blank" rel="noopener noreferrer">'
            f'<span>Aperçu live</span><i class="fas fa-external-link-alt" aria-hidden="true"></i></a>'
            f'<a class="btn btn-outline btn-sm" href="{fiche_url}"><span>En savoir plus</span></a>'
            f'</div></div></article>'
        )

    cards: List[str] = []
    for slug in HOME_VITRINE_TEASER_SLUGS:
        card = _teaser_card(slug)
        if card:
            cards.append(card)
    tablet_card = _teaser_card(HOME_VITRINE_TEASER_TABLET_SLUG, ' home-vitrine-teaser--mid-grid-only')
    if tablet_card:
        cards.append(tablet_card)

    content = (
        '<!-- Genere par build.py : 3 exemples vitrine pour l\'accueil -->\n'
        f'<div class="home-vitrines-teaser-grid">{"".join(cards)}</div>\n'
        '<p class="home-vitrines-teaser-more">'
        '<a href="/vitrines/">Voir tous les modèles par métier</a>'
        '</p>\n'
    )
    path_out.write_text(content, encoding='utf-8')
    print(f'[OK] home-vitrines-teaser.html genere ({len(cards)} exemple(s))')


def build_vitrines_page_collection_embed() -> None:
    """Fragment catalogue (filtre + grille) pour la page /vitrines/ — theme DanielCraft."""
    data = load_vitrines()
    path_out = INCLUDES_DIR / 'vitrines-page-collection.html'
    if not data or not data.get('items'):
        path_out.write_text(
            '<!-- Genere par build.py -->\n'
            '<section class="vitrines-page-collection" data-vitrines-root aria-label="Catalogue modèles">\n'
            '    <div class="container">\n'
            '        <p class="vitrines-empty">Catalogue indisponible '
            '(ajoutez <code>src/data/vitrines.json</code>).</p>\n'
            '    </div>\n'
            '</section>\n',
            encoding='utf-8',
        )
        return
    items = data['items']
    cats = _vitrines_distinct_category_keys(items)
    inner = _vitrines_catalog_inner_lines(items, cats)
    lines: List[str] = []
    lines.append('<!-- Genere automatiquement par build.py depuis src/data/vitrines.json -->')
    lines.append(
        '<section class="vitrines-page-collection vitrines-showcase vitrines-showcase--page" '
        'data-vitrines-root aria-labelledby="vitrines-catalogue-heading">'
    )
    lines.append('    <div class="container">')
    lines.append('        <div class="section-header scroll-reveal">')
    lines.append('            <span class="section-badge">Thèmes sectoriels</span>')
    lines.append(
        '            <h2 id="vitrines-catalogue-heading" class="section-title">'
        'Catalogue des thèmes vitrine</h2>'
    )
    lines.append('            <p class="section-description">')
    lines.append(
        '                Filtrez par univers métier, ouvrez une fiche commerciale (textes, tarif indicatif, visuels) '
        'ou lancez la démo pleine page. Chaque carte montre une capture « fenêtrée » : aperçu long, '
        'défilant doucement dans le cadre pour simuler le scroll sans alourdir la grille.'
    )
    lines.append('            </p>')
    lines.append('        </div>')
    lines.extend(inner)
    lines.append('    </div>')
    lines.append('</section>')
    new_content = '\n'.join(lines) + '\n'
    if path_out.exists() and path_out.read_text(encoding='utf-8') == new_content:
        return
    path_out.write_text(new_content, encoding='utf-8')
    print(f'[OK] vitrines-page-collection.html genere ({len(items)} vitrine(s))')


def build_vitrines_catalog_embed() -> None:
    """Genere includes/vitrines-catalog-embed.html (accueil) + vitrines-page-collection.html (page /vitrines/)."""
    data = load_vitrines()
    path_out = INCLUDES_DIR / 'vitrines-catalog-embed.html'
    if not data or not data.get('items'):
        path_out.write_text(
            '<section id="vitrines" class="vitrines-showcase" data-vitrines-root><div class="container">'
            '<p class="vitrines-empty">Catalogue indisponible (ajoutez <code>src/data/vitrines.json</code>).</p>'
            '</div></section>\n',
            encoding='utf-8',
        )
        build_vitrines_page_collection_embed()
        print('[WARN] vitrines-catalog-embed.html : pas de donnees vitrines')
        return

    hub = (data.get('vitrines_hub_path') or data.get('showcase_hub_path') or '/vitrines/hub-bulma.html').strip()
    if not hub.startswith('/'):
        hub = '/' + hub

    items = data['items']
    cats = _vitrines_distinct_category_keys(items)
    inner = _vitrines_catalog_inner_lines(items, cats)

    lines: List[str] = []
    lines.append('<!-- Genere automatiquement par build.py depuis src/data/vitrines.json -->')
    lines.append('<section id="vitrines" class="vitrines-showcase" data-vitrines-root>')
    lines.append('    <div class="container">')
    lines.append('        <div class="section-header scroll-reveal">')
    lines.append('            <span class="section-badge">Thèmes vitrine</span>')
    lines.append(
        '            <h2 class="section-title">Dix-neuf thèmes sectoriels, prêts à accueillir votre marque</h2>'
    )
    lines.append('            <p class="section-description">')
    lines.append(
        '                Chaque thème est un parcours complet (navigation, contenus, médias, prise de contact) '
        '— pas une simple maquette figée. Les aperçus sont pensés pour les pages longues : vignette fenêtrée '
        'avec défilement léger au survol. Comparez les univers ici, puis ouvrez la '
        f'<a href="/vitrines/">page catalogue</a> pour les fiches détaillées.'
    )
    lines.append('            </p>')
    lines.append('        </div>')
    lines.extend(inner)
    lines.append('    </div>')
    lines.append('</section>')
    new_content = '\n'.join(lines) + '\n'
    if not (path_out.exists() and path_out.read_text(encoding='utf-8') == new_content):
        path_out.write_text(new_content, encoding='utf-8')
        print(f'[OK] vitrines-catalog-embed.html genere ({len(items)} vitrine(s))')
    build_vitrines_page_collection_embed()


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
        stripe_pk = _stripe_publishable_key()
        stripe_checkout = bool(stripe_pk) and not stripe_url
        page_scripts = [
            'main.js',
            'vitrines-screenshots.js',
            'vitrine-detail-modals.js',
            'vitrine-detail-effects.js',
        ]
        if stripe_url or stripe_pk:
            page_scripts.append('vitrine-stripe-checkout.js')
        _, d_desk, a_desk = _vitrine_screenshot_paths(slug, 'desktop')
        _, d_tab, _a_tab = _vitrine_screenshot_paths(slug, 'tablet')
        _, d_mob, _a_mob = _vitrine_screenshot_paths(slug, 'mobile')
        fallback = '/assets/images/og/home-1200x630.jpg'
        desk = d_desk or fallback
        tab = d_tab or d_desk or fallback
        mob = d_mob or d_desk or fallback
        og_desk = _resolve_generated_og(slug, a_desk or fallback, subdir='vitrines')
        title = (it.get('title') or slug).strip()
        mail_subj = quote(f'Installation vitrine — {title}')
        page_url_abs = _to_absolute_url(f'/vitrines/{slug}/')
        shot_desk_abs = _to_absolute_url(a_desk or fallback)
        shot_tab_abs = _to_absolute_url(_a_tab or a_desk or fallback)
        shot_mob_abs = _to_absolute_url(_a_mob or a_desk or fallback)
        og_image_abs = _to_absolute_url(og_desk)
        seo_bundle = _build_vitrine_seo_bundle(
            it, slug, price, page_url_abs, og_image_abs, shot_desk_abs, shot_tab_abs, shot_mob_abs, stack
        )
        vars_dict = DEFAULT_VARS.copy()
        vars_dict.update({
            'current_page': 'vitrine',
            'page_url': f'{SITE_BASE.rstrip("/")}/vitrines/{slug}/',
            'og_image': og_desk,
            'og_type': 'website',
            'extra_css': 'vitrines-portfolio.css',
            'page_scripts': page_scripts,
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
            'stripe_publishable_key': stripe_pk,
            'vitrine_has_stripe_checkout': stripe_checkout,
            'vitrine_mailto_subject': mail_subj,
        })
        vars_dict.update(seo_bundle)
        demo_rel = f'/vitrines/{slug}/demo/index.html'
        vars_dict.update(_vitrine_body_copy(it, price, demo_rel))
        _normalize_page_meta(vars_dict, slug)
        vars_dict['page_url'] = _to_absolute_url(f'/vitrines/{slug}/')
        vars_dict['og_image'] = _og_image_url_with_cache_bust(_to_absolute_url(og_desk))
        _apply_og_image_file_meta(vars_dict)
        scripts = vars_dict.get('page_scripts') or []
        vars_dict['page_scripts_content'] = build_page_scripts_content(scripts)
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


def load_prestations() -> Dict[str, Any]:
    """Charge src/data/prestations.json (catalogue prestations)."""
    if not PRESTATIONS_JSON.is_file():
        return {'categories': [], 'items': []}
    try:
        data = json.loads(PRESTATIONS_JSON.read_text(encoding='utf-8'))
        if not isinstance(data, dict):
            return {'categories': [], 'items': []}
        data.setdefault('categories', [])
        data.setdefault('items', [])
        return data
    except (json.JSONDecodeError, OSError):
        return {'categories': [], 'items': []}


def publish_prestations_json_for_api(output_dir: Path) -> None:
    """Copie prestations.json vers dist/data/ et api/data/ (devis PHP)."""
    if not PRESTATIONS_JSON.is_file():
        return
    for dest_root in (output_dir / 'data', BASE_DIR / 'api' / 'data'):
        dest_root.mkdir(parents=True, exist_ok=True)
        shutil.copy2(PRESTATIONS_JSON, dest_root / 'prestations.json')
    print('[OK] Catalogue prestations copie vers data/ et api/data/')


def _prestation_items_by_category(data: Dict[str, Any]) -> Dict[str, List[Dict[str, Any]]]:
    cats = {c['id']: c for c in data.get('categories', []) if c.get('id')}
    grouped: Dict[str, List[Dict[str, Any]]] = {cid: [] for cid in cats}
    for it in data.get('items', []):
        cid = (it.get('category') or '').strip()
        if cid in grouped:
            grouped[cid].append(it)
    return grouped


def _prestation_price_display(item: Dict[str, Any]) -> str:
    try:
        price = int(item.get('price_eur', 0))
    except (TypeError, ValueError):
        price = 0
    label = (item.get('price_label') or 'Forfait').strip()
    if price <= 0:
        return label
    return f'{label} · {price} €'


PRESTATION_FEATURED_ORDER = (
    'site-vitrine',
    'visibilite-complete',
    'repondeur-intelligent',
)

HOME_VITRINE_TEASER_SLUGS = (
    'restauration',
    'architecture',
    'beaute',
)

# 4e exemple vitrine : visible uniquement tablette / mobile paysage (grille 2×2)
HOME_VITRINE_TEASER_TABLET_SLUG = 'commerce'


def _prestation_duration_label(item: Dict[str, Any]) -> str:
    """Libellé durée sous le prix (heures estimées, alignées Facturio)."""
    try:
        hours = float(item.get('estimated_hours', 0) or 0)
    except (TypeError, ValueError):
        hours = 0.0
    if hours <= 0:
        return ''
    period = (item.get('estimated_hours_period') or '').strip().lower()
    if hours < 1:
        mins = max(1, int(round(hours * 60)))
        core = f'≈ {mins} min'
    elif abs(hours - round(hours)) < 0.05:
        core = f'≈ {int(round(hours))} h'
    else:
        core = f'≈ {hours:.1f} h'.replace('.0 h', ' h')
    if period == 'month':
        return f'{core} / mois'
    if period == 'year':
        return f'{core} / an'
    return f'{core} d\'intervention'


def _prestation_card_visual_html(item: Dict[str, Any], *, featured_hero: bool = False) -> str:
    """Visuel carte : icône + dégradé (évite les SVG génériques peu parlants)."""
    icon = html.escape((item.get('icon') or 'fa-star').strip())
    cat = html.escape((item.get('category') or 'identite').strip())
    hero_class = ' prestation-card-visual--hero' if featured_hero else ''
    return (
        f'<div class="prestation-card-visual prestation-card-visual--icon{hero_class}"'
        f' data-prestation-cat="{cat}" aria-hidden="true">'
        f'<i class="fas {icon}"></i></div>'
    )


def _prestation_card_html(
    item: Dict[str, Any],
    *,
    show_featured_badge: bool = False,
    featured_hero: bool = False,
) -> str:
    slug = (item.get('slug') or '').strip()
    title_raw = (item.get('title') or slug).strip()
    title = html.escape(title_raw)
    desc = html.escape((item.get('short_description') or item.get('description') or '').strip())
    icon = html.escape((item.get('icon') or 'fa-star').strip())
    tagline = html.escape((item.get('tagline') or '').strip())
    service_slug = html.escape((item.get('service_slug') or slug).strip())
    try:
        price_eur = int(item.get('price_eur', 0))
    except (TypeError, ValueError):
        price_eur = 0
    price_label = html.escape((item.get('price_label') or 'Forfait').strip())
    if item.get('has_page'):
        cta_href = f'/prestations/{slug}/'
        short_title = title_raw.split('—')[0].strip() if '—' in title_raw else title_raw
        if len(short_title) > 36:
            short_title = short_title[:33].rstrip() + '…'
        cta_label = f'{short_title} — {price_eur} € HT'
        devis_short = short_title.lower()
        devis_label = f'Devis {devis_short} par e-mail'
        actions = (
            f'<div class="prestation-card-actions">'
            f'<a href="{cta_href}" class="service-cta"><span>{html.escape(cta_label)}</span>'
            f'<i class="fas fa-arrow-right" aria-hidden="true"></i></a>'
            f'<button type="button" class="service-cta service-cta--devis" data-prestation-devis-open'
            f' data-prestation-slug="{html.escape(slug, quote=True)}"'
            f' data-service-slug="{service_slug}"'
            f' data-prestation-title="{title}"'
            f' data-prestation-price="{price_eur}"'
            f' data-prestation-price-label="{price_label}">'
            f'<span>{html.escape(devis_label)}</span><i class="fas fa-envelope" aria-hidden="true"></i></button>'
            f'</div>'
        )
    else:
        actions = (
            f'<button type="button" class="service-cta service-cta--devis" data-prestation-devis-open'
            f' data-prestation-slug="{html.escape(slug, quote=True)}"'
            f' data-service-slug="{service_slug}"'
            f' data-prestation-title="{title}"'
            f' data-prestation-price="{price_eur}"'
            f' data-prestation-price-label="{price_label}">'
            f'<span>Devis par e-mail</span><i class="fas fa-envelope" aria-hidden="true"></i></button>'
        )
    badge = ''
    if show_featured_badge and item.get('featured'):
        badge = '<span class="prestation-card-badge">Coup de cœur</span>'
    card_class = 'service-card prestation-card'
    if item.get('featured') or featured_hero:
        card_class += ' prestation-card--featured'
    tagline_html = (
        f'<p class="prestation-card-tagline">{tagline}</p>' if tagline and featured_hero else ''
    )
    duration = _prestation_duration_label(item)
    duration_html = (
        f'<span class="price-duration">{html.escape(duration)}</span>' if duration else ''
    )
    tier = (item.get('price_tier') or '').strip()
    tier_html = (
        '<span class="price-tier">Petit budget</span>' if tier == 'entry' else ''
    )
    return (
        f'<article class="{card_class}" data-prestation-slug="{html.escape(slug, quote=True)}">'
        f'{badge}'
        f'{_prestation_card_visual_html(item, featured_hero=featured_hero)}'
        f'<h3 class="service-title">{title}</h3>'
        f'{tagline_html}'
        f'<p class="service-description">{desc}</p>'
        f'<div class="service-price">{tier_html}'
        f'<span class="price-label">{price_label}</span>'
        f'<span class="price-amount">{price_eur} € <span class="price-ht">HT</span></span>'
        f'{duration_html}</div>'
        f'{actions}'
        '</article>'
    )


def build_prestations_catalog_embed() -> None:
    """Génère includes/prestations-catalog-embed.html depuis prestations.json."""
    data = load_prestations()
    cats = {c['id']: c for c in data.get('categories', []) if c.get('id')}
    grouped = _prestation_items_by_category(data)
    featured_raw = [
        it for it in data.get('items', [])
        if it.get('featured') and it.get('has_page')
    ]
    order_index = {slug: i for i, slug in enumerate(PRESTATION_FEATURED_ORDER)}
    featured_pages = sorted(
        featured_raw,
        key=lambda it: order_index.get((it.get('slug') or '').strip(), 999),
    )[:3]
    parts: List[str] = []
    if featured_pages:
        cards = ''.join(
            _prestation_card_html(it, show_featured_badge=True, featured_hero=True)
            for it in featured_pages
        )
        parts.append(
            '<section class="prestations-featured" aria-labelledby="prestations-featured-title">'
            '<div class="prestations-featured-head">'
            '<h2 id="prestations-featured-title" class="prestations-section-title">'
            '<i class="fas fa-star" aria-hidden="true"></i> Services en vedette</h2>'
            '<a class="prestations-featured-all" href="#catalogue-categories">Voir tous les services →</a>'
            '</div>'
            '<p class="prestations-featured-lead">Site clair, visibilité Google <em>et</em> IA, ou assistant sur votre site.</p>'
            f'<div class="services-grid prestations-grid prestations-grid--featured">{cards}</div>'
            '</section>'
        )
    parts.append('<div id="catalogue-categories" class="prestations-categories-anchor"></div>')
    for cid, cat in cats.items():
        items = grouped.get(cid) or []
        if not items:
            continue
        title = html.escape((cat.get('title') or cid).strip())
        icon = html.escape((cat.get('icon') or 'fa-folder').strip())
        cards = ''.join(_prestation_card_html(it) for it in items)
        parts.append(
            f'<section class="prestations-category" aria-labelledby="{html.escape(cid)}">'
            f'<h2 id="{html.escape(cid)}" class="prestations-section-title">'
            f'<i class="fas {icon}" aria-hidden="true"></i> {title}</h2>'
            f'<div class="services-grid prestations-grid">{cards}</div>'
            f'</section>'
        )
    out_path = INCLUDES_DIR / 'prestations-catalog-embed.html'
    out_path.write_text('\n'.join(parts), encoding='utf-8')
    print(f'[OK] prestations-catalog-embed.html genere ({len(data.get("items", []))} prestation(s))')

    # Sidebar catégories (ancres + compteurs)
    total = sum(1 for it in data.get('items', []) if it.get('has_page'))
    side: List[str] = [
        f'<li><a class="prestations-sidebar-link is-active" href="#prestations-featured-title">'
        f'<i class="fas fa-th-large" aria-hidden="true"></i> '
        f'<span>Tous les services</span> <em>{total}</em></a></li>'
    ]
    for cid, cat in cats.items():
        items = grouped.get(cid) or []
        if not items:
            continue
        title = html.escape((cat.get('nav_label') or cat.get('title') or cid).strip())
        icon = html.escape((cat.get('icon') or 'fa-folder').strip())
        n = len(items)
        side.append(
            f'<li><a class="prestations-sidebar-link" href="#{html.escape(cid)}">'
            f'<i class="fas {icon}" aria-hidden="true"></i> '
            f'<span>{title}</span> <em>{n}</em></a></li>'
        )
    side.append(
        '<li><a class="prestations-sidebar-link" href="#prestations-featured-title">'
        '<i class="fas fa-star" aria-hidden="true"></i> <span>Services populaires</span></a></li>'
    )
    side_path = INCLUDES_DIR / 'prestations-sidebar-nav.html'
    side_path.write_text('\n'.join(side) + '\n', encoding='utf-8')
    print('[OK] prestations-sidebar-nav.html genere')


def _build_prestation_seo_bundle(
    item: Dict[str, Any],
    slug: str,
    page_url_abs: str,
    og_image_abs: str,
) -> Dict[str, Any]:
    title = (item.get('title') or slug).strip()
    tagline = (item.get('tagline') or '').strip()
    short = (item.get('short_description') or item.get('description') or '').strip()
    try:
        price = int(item.get('price_eur', 0))
    except (TypeError, ValueError):
        price = 0

    custom_title = (item.get('seo_title') or '').strip()
    title_seo = custom_title or f'{title} — prestation DanielCraft'
    page_title = _truncate_meta_text(title_seo + ' | DanielCraft', 118)

    custom_desc = (item.get('seo_description') or '').strip()
    desc = custom_desc or f'{short} Devis par e-mail, sans engagement. DanielCraft, Metz & Lorraine.'
    page_description = _truncate_meta_text(desc, 158)

    kw = [
        title.lower(),
        slug.replace('-', ' '),
        'prestation web',
        'devis site internet',
        'DanielCraft Metz',
        tagline.lower() if tagline else '',
    ]
    page_keywords = _truncate_meta_text(', '.join(dict.fromkeys(k for k in kw if k)), 280)

    og_alt = _truncate_meta_text(f'{title} — {tagline or short}', 190)

    benefits = item.get('benefits') or []
    includes = item.get('includes') or []
    faq = item.get('faq') or []
    benefits_html = (
        '<ul class="prestation-benefits">'
        + ''.join(f'<li>{html.escape(str(x))}</li>' for x in benefits)
        + '</ul>'
    ) if benefits else ''
    includes_html = (
        '<ul class="prestation-includes">'
        + ''.join(f'<li>{html.escape(str(x))}</li>' for x in includes)
        + '</ul>'
    ) if includes else ''
    faq_html = ''
    if faq:
        faq_bits = []
        for entry in faq:
            if not isinstance(entry, dict):
                continue
            q = html.escape(str(entry.get('q') or '').strip())
            a = html.escape(str(entry.get('a') or '').strip())
            if q and a:
                faq_bits.append(
                    f'<details class="prestation-faq-item"><summary>{q}</summary><p>{a}</p></details>'
                )
        if faq_bits:
            faq_html = '<div class="prestation-faq">' + ''.join(faq_bits) + '</div>'

    examples = item.get('examples') or []
    examples_html = (
        '<ul class="prestation-examples">'
        + ''.join(f'<li>{html.escape(str(x))}</li>' for x in examples if str(x).strip())
        + '</ul>'
    ) if examples else ''

    promo_raw = (item.get('promo') or '').strip()
    promo_html = (
        f'<aside class="prestation-promo" role="note">'
        f'<i class="fas fa-lightbulb" aria-hidden="true"></i>'
        f'<p>{html.escape(promo_raw)}</p></aside>'
    ) if promo_raw else ''

    addons = item.get('addons') or []
    addons_json = json.dumps(addons, ensure_ascii=False)

    return {
        'page_title': page_title,
        'page_description': page_description,
        'page_keywords': page_keywords,
        'prestation_og_image_alt': og_alt,
        'prestation_benefits_html': benefits_html,
        'prestation_includes_html': includes_html,
        'prestation_examples_html': examples_html,
        'prestation_promo_html': promo_html,
        'prestation_faq_html': faq_html,
        'prestation_addons_json': addons_json,
        'prestation_price_eur': str(price),
        'prestation_price_label': html.escape((item.get('price_label') or 'Forfait').strip()),
        'prestation_price_note': html.escape((item.get('price_note') or '').strip()),
        'prestation_duration': html.escape(_prestation_duration_label(item)),
    }


def build_prestation_pages(template_engine: TemplateEngine, output_dir: Path) -> List[str]:
    """Génère prestations/<slug>/index.html pour les fiches détaillées."""
    data = load_prestations()
    content_path = PAGES_DIR / 'prestation-detail.html'
    if not content_path.exists():
        print('[WARN] src/pages/prestation-detail.html manquant')
        return []
    content_tpl = content_path.read_text(encoding='utf-8')
    template_path = TEMPLATES_DIR / 'base.html'
    out_root = output_dir / 'prestations'
    slugs_out: List[str] = []
    for it in data.get('items', []):
        if not it.get('has_page'):
            continue
        slug = (it.get('slug') or '').strip()
        if not slug:
            continue
        title = (it.get('title') or slug).strip()
        img_rel = (it.get('image') or '/assets/images/prestations/google.svg').strip()
        og_rel = _resolve_generated_og(slug, img_rel, subdir='prestations')
        og_image_abs = _to_absolute_url(og_rel)
        page_url_abs = _to_absolute_url(f'/prestations/{slug}/')
        seo_bundle = _build_prestation_seo_bundle(it, slug, page_url_abs, og_image_abs)
        vars_dict = DEFAULT_VARS.copy()
        vars_dict.update({
            'schema_type': 'prestation',
            'og_meta_profile': 'prestation',
            'current_page': 'prestation',
            'page_url': page_url_abs,
            'og_image': og_image_abs,
            'og_type': 'website',
            'extra_css': 'prestations.css',
            'page_scripts': ['main.js', 'prestation-devis-modal.js', 'prestation-devis.js'],
            'prestation_slug': slug,
            'prestation_service_slug': (it.get('service_slug') or slug).strip(),
            'prestation_title': title,
            'prestation_tagline': (it.get('tagline') or '').strip(),
            'prestation_description': (it.get('description') or it.get('short_description') or '').strip(),
            'prestation_image': img_rel,
            'prestation_icon': (it.get('icon') or 'fa-star').strip(),
            'prestation_category': (it.get('category') or 'identite').strip(),
        })
        vars_dict.update(seo_bundle)
        _normalize_page_meta(vars_dict, slug)
        vars_dict['page_url'] = page_url_abs
        vars_dict['og_image'] = _og_image_url_with_cache_bust(og_image_abs)
        _apply_og_image_file_meta(vars_dict)
        scripts = vars_dict.get('page_scripts') or []
        vars_dict['page_scripts_content'] = build_page_scripts_content(scripts)
        content_rendered = template_engine.replace_variables(content_tpl, vars_dict)
        content_rendered = template_engine.process_includes(content_rendered, vars_dict)
        vars_dict['page_content'] = content_rendered
        html_output = template_engine.render(template_path, vars_dict)
        dest_dir = out_root / slug
        dest_dir.mkdir(parents=True, exist_ok=True)
        (dest_dir / 'index.html').write_text(html_output, encoding='utf-8')
        slugs_out.append(slug)
    print(f'[OK] {len(slugs_out)} page(s) prestation dans {out_root}')
    return slugs_out


def prestation_slugs_for_sitemap() -> List[str]:
    return [
        (it.get('slug') or '').strip()
        for it in load_prestations().get('items', [])
        if it.get('has_page') and (it.get('slug') or '').strip()
    ]


# --- Livres de formation (catalogue + fiches produit) ---

def load_livres() -> Dict[str, Any]:
    """Charge src/data/livres.json (catalogue livres PDF)."""
    if not LIVRES_JSON.exists():
        return {'categories': [], 'items': [], 'levels': [], 'featured_order': []}
    try:
        data = json.loads(LIVRES_JSON.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError) as exc:
        print(f'[WARN] livres.json illisible : {exc}')
        return {'categories': [], 'items': [], 'levels': [], 'featured_order': []}
    return data if isinstance(data, dict) else {'categories': [], 'items': []}


def publish_livres_json_for_api(output_dir: Path) -> None:
    """Copie livres.json vers dist/data/ et api/data/ (Stripe Checkout)."""
    if not LIVRES_JSON.exists():
        return
    for dest_root in (output_dir / 'data', BASE_DIR / 'api' / 'data'):
        dest_root.mkdir(parents=True, exist_ok=True)
        shutil.copy2(LIVRES_JSON, dest_root / 'livres.json')
    print('[OK] Catalogue livres copie vers data/ et api/data/')


def _livre_price_display(item: Dict[str, Any], catalog: Optional[Dict[str, Any]] = None) -> str:
    raw = item.get('price_eur')
    if raw is None and catalog:
        raw = catalog.get('default_price_eur', 0.5)
    try:
        val = float(raw)
    except (TypeError, ValueError):
        val = 0.5
    return f'{val:.2f}'.replace('.', ',')


def _livre_level_label(item: Dict[str, Any], catalog: Dict[str, Any]) -> str:
    level_id = (item.get('level') or 'base').strip()
    for lv in catalog.get('levels', []):
        if lv.get('id') == level_id:
            return str(lv.get('label') or level_id)
    return level_id.capitalize()


def _livre_category_label(item: Dict[str, Any], catalog: Dict[str, Any]) -> str:
    cat_id = (item.get('category') or '').strip()
    for cat in catalog.get('categories', []):
        if cat.get('id') == cat_id:
            return str(cat.get('title') or cat_id)
    return cat_id


def _livre_items_by_category(data: Dict[str, Any]) -> Dict[str, List[Dict[str, Any]]]:
    grouped: Dict[str, List[Dict[str, Any]]] = {}
    for it in data.get('items', []):
        if not isinstance(it, dict):
            continue
        cid = (it.get('category') or 'informatique').strip()
        grouped.setdefault(cid, []).append(it)
    return grouped


def _livre_cover_url(item: Dict[str, Any]) -> str:
    cover = (item.get('cover') or '').strip()
    if cover.startswith('/'):
        local = BASE_DIR / cover.lstrip('/').replace('/', os.sep)
        if local.is_file():
            return cover
    stack = item.get('cover_stack') or []
    if stack and isinstance(stack[0], str) and stack[0].startswith('/'):
        local = BASE_DIR / stack[0].lstrip('/').replace('/', os.sep)
        if local.is_file():
            return stack[0]
    return ''


def _livre_card_visual_html(item: Dict[str, Any], catalog: Dict[str, Any]) -> str:
    cat = html.escape((item.get('category') or 'informatique').strip())
    icon = html.escape((item.get('icon') or 'fa-book').strip())
    title = html.escape((item.get('title') or '').strip())
    cover = _livre_cover_url(item)
    stack = item.get('cover_stack') or []
    if (item.get('kind') or '') == 'pack' and isinstance(stack, list) and len(stack) >= 2:
        imgs = []
        for i, url in enumerate(stack[:4]):
            if not isinstance(url, str) or not url.startswith('/'):
                continue
            imgs.append(
                f'<img class="livre-card-cover-stack-img" src="{html.escape(url, quote=True)}" '
                f'alt="" loading="lazy" decoding="async" style="--stack-i:{i}">'
            )
        if imgs:
            return (
                f'<div class="prestation-card-visual livre-card-visual livre-card-visual--stack" '
                f'data-livre-cat="{cat}" aria-hidden="true">'
                f'<div class="livre-card-cover-stack">{"".join(imgs)}</div>'
                f'</div>'
            )
    if cover:
        return (
            f'<div class="prestation-card-visual livre-card-visual livre-card-visual--cover" '
            f'data-livre-cat="{cat}">'
            f'<img class="livre-card-cover" src="{html.escape(cover, quote=True)}" '
            f'alt="Couverture — {title}" loading="lazy" decoding="async" width="210" height="280">'
            f'</div>'
        )
    return (
        f'<div class="prestation-card-visual prestation-card-visual--icon" '
        f'data-livre-cat="{cat}" aria-hidden="true">'
        f'<i class="fas {icon}"></i></div>'
    )


def _livre_card_html(
    item: Dict[str, Any],
    catalog: Dict[str, Any],
    *,
    show_featured_badge: bool = False,
) -> str:
    slug = (item.get('slug') or '').strip()
    title = html.escape((item.get('title') or slug).strip())
    desc = html.escape((item.get('short_description') or item.get('description') or '').strip())
    level = (item.get('level') or 'base').strip()
    level_label = html.escape(_livre_level_label(item, catalog))
    keywords = html.escape(','.join(item.get('keywords') or []))
    price = html.escape(_livre_price_display(item, catalog))
    price_label = html.escape((item.get('price_label') or "Prix d'appel").strip())
    cta_href = f'/livres/{slug}/'
    badge = ''
    kind = (item.get('kind') or '').strip()
    if show_featured_badge and item.get('featured') and kind != 'pack':
        badge = '<span class="prestation-card-badge">Coup de cœur</span>'
    if kind == 'pack':
        badge = '<span class="prestation-card-badge">Pack</span>'
    elif not badge:
        badge = '<span class="prestation-card-badge livre-card-badge--pdf">PDF</span>'
    card_class = 'service-card prestation-card livre-card'
    if item.get('featured'):
        card_class += ' prestation-card--featured livre-card--featured'
    if (item.get('kind') or '') == 'pack':
        card_class += ' livre-card--pack'
    if _livre_cover_url(item) or item.get('cover_stack'):
        card_class += ' livre-card--has-cover'
    n_books = len(item.get('book_slugs') or [])
    compare = item.get('compare_at_eur')
    compare_html = ''
    if compare is not None:
        try:
            cmp_disp = f'{float(compare):.2f}'.replace('.', ',')
            compare_html = (
                f'<span class="price-compare">{cmp_disp} € à l\'unité</span>'
            )
        except (TypeError, ValueError):
            compare_html = ''
    meta_extra = (
        f'<p class="livre-card-pack-meta">{n_books} PDF inclus</p>'
        if n_books
        else ''
    )
    return (
        f'<article class="{card_class}" data-livre-slug="{html.escape(slug, quote=True)}" '
        f'data-livre-level="{html.escape(level, quote=True)}" '
        f'data-livre-keywords="{keywords}">'
        f'{badge}'
        f'{_livre_card_visual_html(item, catalog)}'
        f'<span class="livre-card-level">{level_label}</span>'
        f'<h3 class="service-title">{title}</h3>'
        f'{meta_extra}'
        f'<p class="service-description">{desc}</p>'
        f'<div class="service-price">'
        f'<span class="price-label">{price_label}</span>'
        f'<span class="price-amount">{price} € <span class="price-ht">TTC</span></span>'
        f'{compare_html}'
        f'</div>'
        f'<div class="prestation-card-actions">'
        f'<a href="{cta_href}" class="service-cta"><span>Acheter — {price} €</span>'
        f'<i class="fas fa-arrow-right" aria-hidden="true"></i></a>'
        f'</div>'
        '</article>'
    )


def build_livres_deal_week_embed(data: Optional[Dict[str, Any]] = None) -> None:
    """Bandeau commercial « Pack de la semaine » (sous la recherche)."""
    catalog = data if data is not None else load_livres()
    deal = catalog.get('deal_of_the_week') or {}
    slug = (deal.get('slug') or '').strip()
    item = None
    for it in catalog.get('items', []):
        if (it.get('slug') or '').strip() == slug:
            item = it
            break
    if not item:
        packs = [it for it in catalog.get('items', []) if it.get('kind') == 'pack']
        item = packs[0] if packs else None
    out_path = INCLUDES_DIR / 'livres-deal-week.html'
    if not item:
        out_path.write_text('<!-- Pas de pack de la semaine -->\n', encoding='utf-8')
        print('[WARN] livres-deal-week : aucun pack')
        return

    slug = (item.get('slug') or '').strip()
    title = html.escape((item.get('title') or slug).strip())
    tagline = html.escape((item.get('tagline') or '').strip())
    desc = html.escape((item.get('short_description') or '').strip())
    icon = html.escape((item.get('icon') or 'fa-box-open').strip())
    price = html.escape(_livre_price_display(item, catalog))
    n_books = len(item.get('book_slugs') or [])
    badge = html.escape((deal.get('badge') or 'Pack de la semaine').strip())
    urgency = html.escape((deal.get('urgency') or 'Offre mise en avant cette semaine').strip())
    cta = html.escape((deal.get('cta_label') or "Voir l'offre").strip())
    compare_html = ''
    save_html = ''
    try:
        compare = float(item.get('compare_at_eur')) if item.get('compare_at_eur') is not None else None
        price_f = float(item.get('price_eur'))
    except (TypeError, ValueError):
        compare = None
        price_f = 0.0
    if compare and compare > price_f:
        cmp_disp = f'{compare:.2f}'.replace('.', ',')
        save = compare - price_f
        save_disp = f'{save:.2f}'.replace('.', ',')
        pct = int(round(100 * save / compare))
        compare_html = f'<span class="livres-deal-compare">{html.escape(cmp_disp)}&nbsp;€</span>'
        save_html = (
            f'<span class="livres-deal-save">−{html.escape(save_disp)}&nbsp;€ '
            f'<em>(−{pct}&nbsp;%)</em></span>'
        )
    titles = []
    by_slug = {(it.get('slug') or ''): it for it in catalog.get('items', [])}
    cover_urls: List[str] = []
    for bs in item.get('book_slugs') or []:
        bit = by_slug.get(bs) or {}
        titles.append(html.escape((bit.get('title') or bs).strip()))
        cov = _livre_cover_url(bit)
        if cov:
            cover_urls.append(cov)
    if not cover_urls:
        cov = _livre_cover_url(item)
        if cov:
            cover_urls.append(cov)
    pills = ''.join(f'<li>{t}</li>' for t in titles[:6])
    more = ''
    if len(titles) > 6:
        more = f'<li class="livres-deal-more">+{len(titles) - 6} autre(s)</li>'

    if cover_urls:
        stack_imgs = []
        for i, url in enumerate(cover_urls[:4]):
            stack_imgs.append(
                f'<img class="livres-deal-cover" src="{html.escape(url, quote=True)}" '
                f'alt="" loading="lazy" decoding="async" style="--stack-i:{i}">'
            )
        visual = (
            f'<div class="livres-deal-visual livres-deal-visual--covers" aria-hidden="true">'
            f'<div class="livres-deal-visual-glow"></div>'
            f'<div class="livres-deal-cover-stack">{"".join(stack_imgs)}</div>'
            f'<span class="livres-deal-ribbon">{badge}</span>'
            f'</div>'
        )
    else:
        visual = (
            f'<div class="livres-deal-visual" aria-hidden="true">'
            f'<div class="livres-deal-visual-glow"></div>'
            f'<div class="livres-deal-icon"><i class="fas {icon}"></i></div>'
            f'<span class="livres-deal-ribbon">{badge}</span>'
            f'</div>'
        )

    html_out = f'''<aside class="livres-deal-week" aria-labelledby="livres-deal-title">
  <div class="container livres-deal-week-inner">
    {visual}
    <div class="livres-deal-copy">
      <p class="livres-deal-kicker"><i class="fas fa-fire" aria-hidden="true"></i> {urgency}</p>
      <h2 id="livres-deal-title" class="livres-deal-title">{title}</h2>
      <p class="livres-deal-tagline">{tagline}</p>
      <p class="livres-deal-desc">{desc}</p>
      <ul class="livres-deal-pills" aria-label="Contenu du pack">{pills}{more}</ul>
    </div>
    <div class="livres-deal-buy">
      <p class="livres-deal-price-block">
        {compare_html}
        <span class="livres-deal-price">{price}&nbsp;€ <small>TTC</small></span>
        {save_html}
      </p>
      <p class="livres-deal-meta">{n_books} PDF · envoi e-mail apres paiement</p>
      <a class="btn btn-primary btn-large livres-deal-cta" href="/livres/{html.escape(slug)}/">
        <span>{cta}</span>
        <i class="fas fa-arrow-right" aria-hidden="true"></i>
      </a>
      <a class="livres-deal-secondary" href="/livres/?q=pack">Voir tous les packs</a>
    </div>
  </div>
</aside>
'''
    out_path.write_text(html_out, encoding='utf-8')
    print(f'[OK] livres-deal-week.html ({slug} @ {price} EUR)')


def build_livres_catalog_embed() -> None:
    """Genere includes/livres-catalog-embed.html depuis livres.json."""
    data = load_livres()
    build_livres_deal_week_embed(data)
    cats = {c['id']: c for c in data.get('categories', []) if c.get('id')}
    grouped = _livre_items_by_category(data)
    featured_order = data.get('featured_order') or []
    order_index = {slug: i for i, slug in enumerate(featured_order)}
    featured_raw = [it for it in data.get('items', []) if it.get('featured') and it.get('has_page')]
    featured_pages = sorted(
        featured_raw,
        key=lambda it: order_index.get((it.get('slug') or '').strip(), 999),
    )
    parts: List[str] = []
    shelf_links: List[str] = []
    if featured_pages:
        shelf_links.append(
            '<li><a href="#livres-featured-title">'
            '<i class="fas fa-star" aria-hidden="true"></i> Pour commencer</a></li>'
        )
    for cat in data.get('categories', []):
        cid = cat.get('id')
        if not cid or cid not in grouped:
            continue
        meta = cats.get(cid, cat)
        icon = html.escape((meta.get('icon') or 'fa-book').strip())
        label = html.escape((meta.get('nav_label') or meta.get('title') or cid).strip())
        shelf_links.append(
            f'<li><a href="#livres-cat-{html.escape(cid)}">'
            f'<i class="fas {icon}" aria-hidden="true"></i> {label}</a></li>'
        )
    if shelf_links:
        parts.append(
            '<nav class="livres-shelf-nav" aria-label="Rayons du catalogue">'
            f'<ul>{"".join(shelf_links)}</ul>'
            '</nav>'
        )
    if featured_pages:
        cards = ''.join(
            _livre_card_html(it, data, show_featured_badge=True) for it in featured_pages[:8]
        )
        parts.append(
            '<section class="prestations-featured" aria-labelledby="livres-featured-title">'
            '<h2 id="livres-featured-title" class="prestations-section-title">'
            '<i class="fas fa-star" aria-hidden="true"></i> Pour commencer</h2>'
            '<p class="prestations-featured-lead">'
            "Livre a 0,50&nbsp;€ — packs moins cher qu'a l'unite (remise volume)."
            '</p>'
            f'<div class="services-grid prestations-grid prestations-grid--featured">{cards}</div>'
            '</section>'
        )
    for cat in data.get('categories', []):
        cid = cat.get('id')
        if not cid or cid not in grouped:
            continue
        items = grouped[cid]
        meta = cats.get(cid, cat)
        icon = html.escape((meta.get('icon') or 'fa-book').strip())
        title = html.escape((meta.get('title') or cid).strip())
        lead = html.escape((meta.get('description') or '').strip())
        cards = ''.join(_livre_card_html(it, data) for it in items)
        parts.append(
            f'<section class="prestations-category" aria-labelledby="livres-cat-{html.escape(cid)}">'
            f'<h2 id="livres-cat-{html.escape(cid)}" class="prestations-section-title">'
            f'<i class="fas {icon}" aria-hidden="true"></i> {title}</h2>'
            f'<p class="prestations-category-lead">{lead}</p>'
            f'<div class="services-grid prestations-grid">{cards}</div>'
            '</section>'
        )
    out_path = INCLUDES_DIR / 'livres-catalog-embed.html'
    out_path.write_text('\n'.join(parts) + '\n', encoding='utf-8')
    print(f'[OK] livres-catalog-embed.html genere ({len(data.get("items", []))} livre(s))')


def _build_livre_seo_bundle(
    item: Dict[str, Any],
    catalog: Dict[str, Any],
    slug: str,
    page_url_abs: str,
) -> Dict[str, str]:
    title = (item.get('title') or slug).strip()
    tagline = (item.get('tagline') or '').strip()
    desc = (item.get('description') or item.get('short_description') or tagline).strip()
    price_disp = _livre_price_display(item, catalog)
    benefits = item.get('benefits') or []
    includes = item.get('includes') or []
    keywords = item.get('keywords') or []
    benefits_html = (
        '<ul class="prestation-benefits">'
        + ''.join(f'<li>{html.escape(str(b))}</li>' for b in benefits)
        + '</ul>'
    )
    includes_html = (
        '<ul class="prestation-includes">'
        + ''.join(f'<li>{html.escape(str(x))}</li>' for x in includes)
        + '</ul>'
    )
    keywords_html = html.escape(', '.join(str(k) for k in keywords))
    promo_html = (
        '<aside class="prestation-promo" role="note">'
        f"<strong>Prix d'appel</strong> — {html.escape(price_disp)}&nbsp;€ TTC. "
        'PDF envoye par e-mail apres paiement securise.'
        '</aside>'
    )
    return {
        'page_title': f'{title} — livre PDF DanielCraft',
        'page_description': desc[:160],
        'page_keywords': ', '.join(
            [title] + [str(k) for k in keywords] + ['livre formation PDF', 'DanielCraft']
        ),
        'livre_benefits_html': benefits_html,
        'livre_includes_html': includes_html,
        'livre_promo_html': promo_html,
        'livre_keywords_html': keywords_html,
        'livre_price_display': price_disp,
        'livre_price_eur': str(
            item.get('price_eur')
            if item.get('price_eur') is not None
            else catalog.get('default_price_eur', 0.5)
        ),
        'livre_price_label': html.escape((item.get('price_label') or "Prix d'appel").strip()),
        'livre_price_note': html.escape(
            (item.get('price_note') or 'TTC — PDF envoye par e-mail apres paiement').strip()
        ),
        'livre_level_label': html.escape(_livre_level_label(item, catalog)),
        'livre_category_label': html.escape(_livre_category_label(item, catalog)),
    }


def build_livre_pages(template_engine: TemplateEngine, output_dir: Path) -> List[str]:
    """Genere livres/<slug>/index.html pour les fiches produit."""
    data = load_livres()
    content_path = PAGES_DIR / 'livre-detail.html'
    if not content_path.exists():
        print('[WARN] src/pages/livre-detail.html manquant')
        return []
    content_raw = content_path.read_text(encoding='utf-8')
    out_root = output_dir / 'livres'
    out_root.mkdir(parents=True, exist_ok=True)
    stripe_pk = _stripe_publishable_key()
    slugs_out: List[str] = []
    for it in data.get('items', []):
        if not it.get('has_page'):
            continue
        slug = (it.get('slug') or '').strip()
        if not slug:
            continue
        title = (it.get('title') or slug).strip()
        page_url_abs = _to_absolute_url(f'/livres/{slug}/')
        seo = _build_livre_seo_bundle(it, data, slug, page_url_abs)
        stripe_url = (it.get('stripe_payment_link_url') or '').strip()
        stripe_checkout = bool(stripe_pk) and not stripe_url
        page_scripts = ['main.js']
        if stripe_url or stripe_pk:
            page_scripts.append('livre-stripe-checkout.js')
        vars_dict = DEFAULT_VARS.copy()
        extra_css = 'vitrines-portfolio.css,livres.css'
        aq = str(DEFAULT_VARS.get('assets_query') or '')
        extra_links = '\n'.join(
            f'<link rel="stylesheet" href="/assets/css/{html.escape(n.strip())}{aq}">'
            for n in extra_css.split(',')
            if n.strip()
        )
        vars_dict.update({
            'schema_type': 'livre',
            'og_meta_profile': 'default',
            'current_page': 'livre',
            'page_url': page_url_abs,
            'extra_css': extra_css,
            'extra_css_links': extra_links,
            'page_scripts': page_scripts,
            'livre_slug': slug,
            'livre_title': title,
            'livre_tagline': (it.get('tagline') or '').strip(),
            'livre_description': (
                it.get('description') or it.get('short_description') or ''
            ).strip(),
            'livre_icon': (it.get('icon') or 'fa-book').strip(),
            'livre_category': (it.get('category') or 'informatique').strip(),
            'livre_cover': _livre_cover_url(it),
            'livre_stripe_url': stripe_url,
            'livre_pay_link': bool(stripe_url),
            'livre_pay_checkout': stripe_checkout,
            'stripe_publishable_key': stripe_pk,
            'livre_mailto_subject': quote(f'Commande livre : {title}'),
        })
        vars_dict.update(seo)
        _normalize_page_meta(vars_dict, 'livre')
        vars_dict['page_scripts_content'] = build_page_scripts_content(
            page_scripts,
            str(vars_dict.get('assets_query') or ''),
        )
        content_rendered = template_engine.process_includes(content_raw, vars_dict)
        content_rendered = template_engine.replace_variables(content_rendered, vars_dict)
        vars_dict['page_content'] = content_rendered
        template_path = TEMPLATES_DIR / 'base.html'
        html_output = template_engine.render(template_path, vars_dict)
        dest_dir = out_root / slug
        dest_dir.mkdir(parents=True, exist_ok=True)
        (dest_dir / 'index.html').write_text(html_output, encoding='utf-8')
        slugs_out.append(slug)
    print(f'[OK] {len(slugs_out)} page(s) livre dans {out_root}')
    return slugs_out


def livre_slugs_for_sitemap() -> List[str]:
    return [
        (it.get('slug') or '').strip()
        for it in load_livres().get('items', [])
        if it.get('has_page') and (it.get('slug') or '').strip()
    ]


def generate_sitemap_livres(output_dir: Path) -> None:
    """Genere sitemap-livres.xml : catalogue + fiches."""
    base = SITE_BASE.rstrip('/')
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"',
        '        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 '
        'http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">',
    ]
    today = datetime.now().date()
    lastmod = today.isoformat()
    lines.append(_sitemap_url_line(base, '/livres/', lastmod, 'weekly', '0.9'))
    for q in ('python', 'javascript', 'sql', 'ia', 'securite', 'finance'):
        lines.append(
            _sitemap_url_line(base, f'/livres/?q={quote(q, safe="")}', lastmod, 'weekly', '0.5')
        )
    for slug in livre_slugs_for_sitemap():
        seed = sum(ord(ch) for ch in slug)
        days_ago = 3 + (seed % 180)
        organic_lastmod = (today - timedelta(days=days_ago)).isoformat()
        lines.append(
            _sitemap_url_line(base, f'/livres/{slug}/', organic_lastmod, 'monthly', '0.7')
        )
    lines.append('</urlset>')
    (output_dir / 'sitemap-livres.xml').write_text('\n'.join(lines), encoding='utf-8')


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
    """Genere les pages HTML pour chaque projet dans output_dir/projets/. Retourne les slugs canoniques (sitemap)."""
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
    slugs: List[str] = []
    canonical_set: set = set()
    for p in projects:
        slug = p.get('slug') or p.get('id', '')
        if not slug:
            continue
        canonical_set.add(slug)
        techs = p.get('technologies') or []
        tech_html = ''.join(f'<span class="tech-tag">{t}</span>' for t in techs)
        img_url = p.get('imageUrl') or ''
        if img_url and not img_url.startswith('http'):
            img_url = SITE_BASE + '/' + img_url.lstrip('/')
        og_fallback = img_url or DEFAULT_VARS['og_image']
        og_rel = _resolve_generated_og(slug, og_fallback, subdir='projets')
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
            'og_image': _og_image_url_with_cache_bust(_to_absolute_url(og_rel)),
            'og_type': 'website',
            'schema_type': 'project',
            'page_content': '',
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
        vars_dict['page_scripts_content'] = build_page_scripts_content(None)
        html_output = template_engine.render(template_path, vars_dict)
        (out_projets / f'{slug}.html').write_text(html_output, encoding='utf-8')
        slugs.append(slug)

    aliases = load_project_slug_aliases()
    alias_count = 0
    for alias_slug, canonical_slug in sorted(aliases.items()):
        if canonical_slug not in canonical_set:
            print(f"[WARN] Alias projet ignore (canonique absent) : {alias_slug} -> {canonical_slug}")
            continue
        redirect_html = _render_project_alias_redirect_page(alias_slug, canonical_slug)
        (out_projets / f'{alias_slug}.html').write_text(redirect_html, encoding='utf-8')
        alias_count += 1

    print(f"[OK] {len(slugs)} page(s) projet genere(s) dans {out_projets}"
          + (f" (+ {alias_count} alias redirect)" if alias_count else ''))
    return slugs


def build_page(page_name: str, template_engine: TemplateEngine):
    """Build une page HTML."""
    if page_name in ('index', 'vitrines'):
        build_vitrines_catalog_embed()
    if page_name == 'index':
        build_home_vitrines_teaser_embed()
    if page_name == 'nos-offres':
        build_prestations_catalog_embed()
    if page_name == 'livres':
        build_livres_catalog_embed()

    # Charge la config de la page
    page_config = load_page_config(page_name)
    
    # Fusionne avec les valeurs par défaut
    vars_dict = DEFAULT_VARS.copy()
    vars_dict.update(page_config)
    vars_dict['current_page'] = page_name

    if page_name == 'audit':
        audit_cfg = load_audits_config()
        paid = audit_cfg.get('paid_audit') if isinstance(audit_cfg.get('paid_audit'), dict) else {}
        vars_dict['stripe_publishable_key'] = _stripe_publishable_key()
        vars_dict['audit_paid_slug'] = str(paid.get('slug') or 'audit-complet-ia')
        vars_dict['audit_paid_price_eur'] = format_audit_price_eur_display(paid.get('price_eur', 199))
        if not vars_dict.get('schema_type'):
            vars_dict['schema_type'] = 'audit'

    # Profil meta OG (le moteur de template ne gère pas != )
    schema_type = str(vars_dict.get('schema_type') or '')
    if schema_type == 'vitrine':
        vars_dict['og_meta_profile'] = 'vitrine'
    elif schema_type == 'prestation':
        vars_dict['og_meta_profile'] = 'prestation'
    else:
        vars_dict['og_meta_profile'] = 'default'

    # CSS additionnels (un fichier ou liste separee par des virgules)
    extra_css_raw = vars_dict.get('extra_css')
    if extra_css_raw:
        aq = str(vars_dict.get('assets_query') or '')
        names = [n.strip() for n in str(extra_css_raw).split(',') if n.strip()]
        vars_dict['extra_css_links'] = '\n'.join(
            f'<link rel="stylesheet" href="/assets/css/{html.escape(n)}{aq}">' for n in names
        )
    else:
        vars_dict['extra_css_links'] = ''

    # Normalise canonical/OG a partir de SITE_BASE
    _normalize_page_meta(vars_dict, page_name)

    # Génère le contenu des scripts
    vars_dict['page_scripts_content'] = build_page_scripts_content(
        vars_dict.get('page_scripts') or None,
        str(vars_dict.get('assets_query') or ''),
    )
    
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


def generate_sitemap_vitrines(output_dir: Path) -> None:
    """Genere sitemap-vitrines.xml : catalogue /vitrines/ et fiches /vitrines/<slug>/."""
    lastmod = datetime.now().strftime('%Y-%m-%d')
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"',
        '        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 '
        'http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">',
    ]
    base = SITE_BASE.rstrip('/')
    lines.append(_sitemap_url_line(base, '/vitrines/', lastmod, 'weekly', '0.80'))
    for slug in vitrine_slugs_for_sitemap():
        lines.append(_sitemap_url_line(base, f'/vitrines/{slug}/', lastmod, 'monthly', '0.60'))
    lines.append('</urlset>')
    (output_dir / 'sitemap-vitrines.xml').write_text('\n'.join(lines), encoding='utf-8')


def generate_sitemap_pages(
    output_dir: Path,
    project_slugs: Optional[List[str]] = None,
) -> None:
    """Genere sitemap-pages.xml : pages statiques + projets (vitrines dans sitemap-vitrines.xml)."""
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


def generate_sitemap_prestations(output_dir: Path) -> None:
    """Genere sitemap-prestations.xml : fiches prestations + recherches catalogue."""
    from urllib.parse import quote

    base = SITE_BASE.rstrip('/')
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"',
        '        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 '
        'http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">',
    ]
    today = datetime.now().date()
    lastmod = today.isoformat()
    # Catalogue + deep-links recherche (chips) pour Google SearchAction
    lines.append(_sitemap_url_line(base, '/nos-offres', lastmod, 'weekly', '0.95'))
    for q in ('éco', 'site vitrine', 'google', 'assistant', 'entretien'):
        lines.append(
            _sitemap_url_line(base, f'/nos-offres?q={quote(q, safe="")}', lastmod, 'weekly', '0.55')
        )
    for slug in prestation_slugs_for_sitemap():
        # Donne des dates "naturelles" et stables (pas toutes identiques).
        seed = sum(ord(ch) for ch in slug)
        days_ago = 7 + (seed % 210)  # entre 1 semaine et ~7 mois
        organic_lastmod = (today - timedelta(days=days_ago)).isoformat()
        lines.append(
            _sitemap_url_line(base, f'/prestations/{slug}/', organic_lastmod, 'monthly', '0.75')
        )
    lines.append('</urlset>')
    (output_dir / 'sitemap-prestations.xml').write_text('\n'.join(lines), encoding='utf-8')


def generate_sitemap_index(output_dir: Path) -> None:
    """Genere sitemap.xml (index) : pages, vitrines, prestations, blog."""
    lastmod = datetime.now().strftime('%Y-%m-%d')
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"',
        '              xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 '
        'http://www.sitemaps.org/schemas/sitemap/0.9/siteindex.xsd">',
        f'  <sitemap><loc>{SITE_BASE}/sitemap-pages.xml</loc><lastmod>{lastmod}</lastmod></sitemap>',
        f'  <sitemap><loc>{SITE_BASE}/sitemap-vitrines.xml</loc><lastmod>{lastmod}</lastmod></sitemap>',
        f'  <sitemap><loc>{SITE_BASE}/sitemap-prestations.xml</loc><lastmod>{lastmod}</lastmod></sitemap>',
        f'  <sitemap><loc>{SITE_BASE}/sitemap-livres.xml</loc><lastmod>{lastmod}</lastmod></sitemap>',
        f'  <sitemap><loc>{SITE_BASE}/blog/sitemap-blog.xml</loc><lastmod>{lastmod}</lastmod></sitemap>',
        '</sitemapindex>',
    ]
    (output_dir / 'sitemap.xml').write_text('\n'.join(lines), encoding='utf-8')


def main():
    """Fonction principale."""
    global OUTPUT_DIR, SITE_BASE

    _load_build_dotenv()
    SITE_BASE = _resolve_public_site_base(SITE_BASE)
    DEFAULT_VARS['site_base'] = SITE_BASE
    DEFAULT_VARS['page_url'] = f'{SITE_BASE}/'
    DEFAULT_VARS['og_image'] = f'{SITE_BASE}/assets/images/og/home-1200x630.jpg'
    DEFAULT_VARS.update(_webful_analytics_config())

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
        elif arg in ('--no-webp', '-no-webp'):
            skip_webp = True
            i += 1
        elif arg.startswith('--'):
            # Flag inconnu : ignorer (ne pas le prendre pour un nom de page)
            print(f"[WARN] Argument ignore : {arg}")
            i += 1
        elif arg.startswith('-') and not arg.startswith('--'):
            # Ex. -no-webp mal passe par PowerShell — ne pas builder une page "-" / "p"
            if 'no-webp' in arg or arg in ('-n', '-w'):
                skip_webp = True
            else:
                print(f"[WARN] Argument ignore : {arg}")
            i += 1
        elif not arg.startswith('-'):
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
    # Normalise les JPEG OG (1200×630 réels) avant sync — requis Meta / Messenger
    _normalize_script = BASE_DIR / 'scripts' / 'normalize_og_images.py'
    if _normalize_script.is_file() and assets_src.is_dir():
        import subprocess
        subprocess.run([sys.executable, str(_normalize_script)], cwd=str(BASE_DIR), check=False)
    if assets_src.exists():
        if assets_dst.exists():
            sync_assets_to_dist(assets_src, assets_dst)
        else:
            shutil.copytree(assets_src, assets_dst)
            print(f"[OK] Assets copies dans {assets_dst}")
        assets_ver = apply_assets_version_to_defaults(assets_src)
        print(f"[OK] Assets version (cache-bust) : {assets_ver}")
        # Génère les variantes WebP pour les images (optimisation UX / perf)
        if not skip_webp:
            generate_webp_variants(assets_dst)
        else:
            print("[INFO] Generation WebP ignoree (--no-webp)")

    publish_vitrines_to_dist(OUTPUT_DIR)
    publish_catalog_json_for_api(OUTPUT_DIR)
    publish_audits_json_for_api(OUTPUT_DIR)
    publish_prestations_json_for_api(OUTPUT_DIR)
    publish_livres_json_for_api(OUTPUT_DIR)

    # Genere robots.txt (base sur SITE_BASE)
    generate_robots_txt(OUTPUT_DIR)
    generate_nginx_project_alias_redirects(OUTPUT_DIR)
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
        sync_api_to_dist(api_src, api_dst)

    router_src = BASE_DIR / 'scripts' / 'router.php'
    if router_src.is_file():
        shutil.copy2(router_src, OUTPUT_DIR / 'router.php')
        print('[OK] router.php copie dans dist/ (URLs sans .html pour php -S)')

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
            write_prestations_catalog_redirect(OUTPUT_DIR)
            if page_name in ('livres', 'nos-offres'):
                if page_name == 'livres':
                    build_livre_pages(template_engine, OUTPUT_DIR)
                    generate_sitemap_livres(OUTPUT_DIR)
                if page_name == 'nos-offres':
                    build_prestation_pages(template_engine, OUTPUT_DIR)
                    generate_sitemap_prestations(OUTPUT_DIR)
            print(f"\n[OK] Build de {page_name} termine dans {OUTPUT_DIR} !")
        else:
            sys.exit(1)
        return
    
    # Build toutes les pages
    print(f"[BUILD] Build de toutes les pages dans {OUTPUT_DIR}...\n")
    
    # Liste des pages à builder
    pages = [
        'index',
        'nos-offres',
        'livres',
        'contact',
        'vitrines',
        'processus',
        'metz',
        'portfolio',
        'projets',
        'statistiques',
        'analyse',
        'audit',
        'desabonnement',
        'mentions-legales',
        'cgv',
        'cgu',
        'politique-confidentialite',
        'not-found',
        'server-error',
        'pro',
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
            blog_env = os.environ.copy()
            blog_env['SITE_BASE'] = SITE_BASE
            # Donnée de secours pour build_blog.py si SITE_BASE local.
            if blog_env.get('DEPLOY_SITE_BASE') in (None, ''):
                blog_env['DEPLOY_SITE_BASE'] = SITE_BASE
            result = subprocess.run(
                [sys.executable, str(blog_dir / 'build_blog.py'), '--output', blog_output],
                cwd=str(BASE_DIR),
                env=blog_env,
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
    build_vitrine_pages(template_engine, OUTPUT_DIR)
    build_prestation_pages(template_engine, OUTPUT_DIR)
    write_prestations_catalog_redirect(OUTPUT_DIR)
    build_livre_pages(template_engine, OUTPUT_DIR)

    # Generation des sitemaps (pages + projets | vitrines | prestations | livres | index)
    generate_sitemap_vitrines(OUTPUT_DIR)
    generate_sitemap_prestations(OUTPUT_DIR)
    generate_sitemap_livres(OUTPUT_DIR)
    generate_sitemap_pages(OUTPUT_DIR, project_slugs=project_slugs)
    generate_sitemap_index(OUTPUT_DIR)
    print("[OK] sitemap.xml, sitemap-pages.xml, sitemap-vitrines.xml, sitemap-prestations.xml, sitemap-livres.xml generes")

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
                    self._rebuilding = False

                def _is_debounced(self, key: str, delay_s: float = 0.35) -> bool:
                    now = time.time()
                    prev = self._last_event.get(key, 0.0)
                    if (now - prev) < delay_s:
                        return True
                    self._last_event[key] = now
                    return False

                def _is_generated_include(self, src: Path) -> bool:
                    try:
                        return INCLUDES_DIR in src.parents and src.name in GENERATED_INCLUDE_NAMES
                    except (OSError, ValueError):
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
                    self._rebuilding = True
                    try:
                        ok = 0
                        for p in pages:
                            if build_page(p, template_engine):
                                ok += 1
                        ps = build_project_pages(template_engine, OUTPUT_DIR)
                        build_vitrine_pages(template_engine, OUTPUT_DIR)
                        build_prestation_pages(template_engine, OUTPUT_DIR)
                        write_prestations_catalog_redirect(OUTPUT_DIR)
                        build_livre_pages(template_engine, OUTPUT_DIR)
                        generate_sitemap_vitrines(OUTPUT_DIR)
                        generate_sitemap_prestations(OUTPUT_DIR)
                        generate_sitemap_livres(OUTPUT_DIR)
                        generate_sitemap_pages(OUTPUT_DIR, project_slugs=ps)
                        generate_sitemap_index(OUTPUT_DIR)
                        print(f"[WATCH] Rebuild complet: {ok}/{len(pages)} page(s) + projets/vitrines/prestations/livres/sitemap")
                    finally:
                        # Laisser le FS Windows digérer les write_text des includes générés
                        time.sleep(0.5)
                        self._rebuilding = False

                def _handle_src_change(self, event):
                    if event.is_directory or self._rebuilding:
                        return

                    src = Path(event.src_path)
                    # Ignore les includes générés par le build (évite la boucle watch)
                    if self._is_generated_include(src):
                        return

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
                            self._rebuilding = True
                            try:
                                build_page(page, template_engine)
                            finally:
                                time.sleep(0.35)
                                self._rebuilding = False
                        else:
                            self._rebuild_all_pages()
                        return

                    # Donnees partagees (vitrines, etc.) => rebuild global
                    if ext in {'.html', '.json'} and DATA_DIR in src.parents:
                        print(f"\n📦 Data modifiee : {src.name}")
                        self._rebuild_all_pages()
                        return

                    # Changement template/include (hors générés) => rebuild global
                    if ext in {'.html', '.json'} and (TEMPLATES_DIR in src.parents or INCLUDES_DIR in src.parents):
                        print(f"\n🧩 Template/include modifie : {src.name}")
                        self._rebuild_all_pages()
                        return

                def on_modified(self, event):
                    self._handle_src_change(event)

                def on_created(self, event):
                    self._handle_src_change(event)
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

