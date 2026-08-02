#!/usr/bin/env python3
"""
Compile le contenu Markdown du blog vers HTML.

Usage:
    python build_blog.py [--output dist/blog]
    python build_blog.py --output ../dist/blog

Lit les fichiers .md dans content/articles/ et content/tutorials/,
convertit en HTML et genere les pages dans le dossier de sortie.
"""

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional
from urllib.parse import quote

try:
    import markdown
    import yaml
except ImportError as e:
    print(f"[ERREUR] Dependances manquantes : {e}")
    print("Installe avec : pip install markdown PyYAML")
    sys.exit(1)

# Configuration
def _is_local_site_base(url: str) -> bool:
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
    site_base = (os.environ.get('SITE_BASE') or default_base or '').strip()
    deploy_base = (os.environ.get('DEPLOY_SITE_BASE') or '').strip()
    if deploy_base and _is_local_site_base(site_base):
        return deploy_base.rstrip('/')
    return site_base.rstrip('/')


SITE_BASE = _resolve_public_site_base(os.environ.get('SITE_BASE', 'https://example.com'))
OG_IMAGE_BLOG = f'{SITE_BASE}/assets/images/og/blog-1200x630.jpg'
OG_IMAGE_HOME = f'{SITE_BASE}/assets/images/og/home-1200x630.jpg'
BLOG_DIR = Path(__file__).parent
PROJECT_ROOT = BLOG_DIR.parent
SCRIPTS_DIR = PROJECT_ROOT / 'scripts'
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))
from blog_seo import block_breadcrumbs, crumbs_article, crumbs_blog_index, crumbs_collection
SRC_DIR = PROJECT_ROOT / 'src'
CONTENT_DIR = BLOG_DIR / 'content'
ARTICLES_SRC = CONTENT_DIR / 'articles'
TUTORIALS_SRC = CONTENT_DIR / 'tutorials'
COLLECTIONS_SRC = CONTENT_DIR / 'collections'
TEMPLATES_DIR = BLOG_DIR / 'templates'
_SITE_LAYOUT_CACHE: Optional[dict] = None


def _render_site_include(include_path: str, vars_dict: dict) -> str:
    """
    Rend un fragment HTML partagé depuis src/includes/ (même moteur que build.py).

    @param include_path Chemin relatif sous src/ (ex. includes/nav.html)
    @param vars_dict Variables du template (current_page, blog_enabled, etc.)
    @returns HTML rendu
    """
    sys.path.insert(0, str(PROJECT_ROOT))
    try:
        from build import TemplateEngine
    except ImportError as exc:
        print(f'[WARN] TemplateEngine indisponible : {exc}')
        return ''

    engine = TemplateEngine(SRC_DIR)
    raw = engine.load_include(include_path)
    raw = engine.process_includes(raw, vars_dict)
    return engine.replace_variables(raw, vars_dict)


def _get_site_layout_html() -> dict:
    """
    Nav, footer et modales identiques au site principal (mis en cache par build).

    @returns Dict avec les clés nav, footer, modals
    """
    global _SITE_LAYOUT_CACHE
    if _SITE_LAYOUT_CACHE is not None:
        return _SITE_LAYOUT_CACHE

    sys.path.insert(0, str(PROJECT_ROOT))
    try:
        from build import _apply_analytics_vars
    except ImportError as exc:
        print(f'[WARN] Config analytics indisponible : {exc}')

        def _apply_analytics_vars(_vars_dict: dict) -> None:
            return None

    vars_dict = {
        'current_page': 'blog',
        'blog_enabled': True,
        'page_scripts_content': '<script src="/assets/js/main.js" defer></script>',
    }
    _apply_analytics_vars(vars_dict)
    _SITE_LAYOUT_CACHE = {
        'nav': _render_site_include('includes/nav.html', vars_dict),
        'footer': _render_site_include('includes/footer.html', vars_dict),
        'analytics': _render_site_include('includes/analytics.html', vars_dict),
        'modals': (
            _render_site_include('includes/modal-prestation-devis.html', vars_dict)
            + _render_site_include('includes/modal-projet.html', vars_dict)
        ),
    }
    return _SITE_LAYOUT_CACHE


def _get_assets_query() -> str:
    """Cache-bust CSS/JS, aligné sur le build site principal."""
    try:
        sys.path.insert(0, str(PROJECT_ROOT))
        from build import compute_assets_version

        return f'?v={compute_assets_version(PROJECT_ROOT / "assets")}'
    except Exception:
        return ''


def _apply_asset_paths(html: str, assets_query: Optional[str] = None) -> str:
    """Chemins absolus /assets + cache-bust (même skin que le site)."""
    q = _get_assets_query() if assets_query is None else assets_query
    html = html.replace('{{ASSETS}}', '/assets')
    html = html.replace('{{ASSETS_QUERY}}', q)
    # Favicons / racines en absolu (indépendant de la profondeur /blog/…)
    html = html.replace('href="{{ROOT}}/favicon.ico"', 'href="/favicon.ico"')
    html = html.replace('href="{{ROOT}}favicon.ico"', 'href="/favicon.ico"')
    html = html.replace('href="{{ROOT}}/assets/', 'href="/assets/')
    html = html.replace('href="{{ROOT}}assets/', 'href="/assets/')
    html = html.replace('{{ROOT}}', '/')
    return html


def _inject_site_layout(html: str) -> str:
    """Injecte nav, footer et modales partagés dans un template blog."""
    layout = _get_site_layout_html()
    html = html.replace('{{NAV_HTML}}', layout.get('nav', ''))
    html = html.replace('{{FOOTER_HTML}}', layout.get('footer', ''))
    html = html.replace('{{ANALYTICS_HTML}}', layout.get('analytics', ''))
    html = html.replace('{{MODALS_HTML}}', layout.get('modals', ''))
    return html


def slugify(text: str) -> str:
    """Convertit un texte en slug pour l'URL."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def parse_front_matter(content: str) -> tuple[dict, str]:
    """
    Parse le front matter YAML et retourne (metadatas, body).
    """
    if not content.strip().startswith('---'):
        return {}, content

    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content

    try:
        meta = yaml.safe_load(parts[1])
        return meta or {}, parts[2].strip()
    except yaml.YAMLError:
        return {}, parts[2].strip()


def md_to_html(md_content: str) -> str:
    """Convertit le Markdown en HTML."""
    extensions = [
        'extra',       # tables, fenced code, etc.
        'codehilite',  # syntax highlighting (optionnel)
        'toc',         # table des matieres (optionnel)
    ]
    try:
        return markdown.markdown(md_content, extensions=['extra'])
    except Exception:
        return markdown.markdown(md_content, extensions=[])


def load_article(md_path: Path) -> Optional[dict]:
    """
    Charge un article/tutoriel depuis un fichier Markdown.
    Retourne un dict avec title, slug, date, excerpt, content_html, type, etc.
    """
    if not md_path.suffix == '.md':
        return None

    raw = md_path.read_text(encoding='utf-8')
    meta, body = parse_front_matter(raw)

    # Slug : depuis le front matter ou le nom du fichier
    slug = meta.get('slug') or slugify(md_path.stem)
    title = meta.get('title', md_path.stem)
    date_val = meta.get('date', datetime.now())
    date = date_val.strftime('%Y-%m-%d') if hasattr(date_val, 'strftime') else str(date_val)
    excerpt = meta.get('excerpt', '')
    content_type = meta.get('type', 'article')
    tags = meta.get('tags', [])
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(',')]
    series = meta.get('series')
    series_order = meta.get('series_order')
    og_image = meta.get('og_image')

    content_html = md_to_html(body)

    return {
        'title': title,
        'slug': slug,
        'date': date,
        'excerpt': excerpt,
        'content_html': content_html,
        'type': content_type,
        'tags': tags,
        'series': series,
        'series_order': series_order,
        'og_image': og_image,
        'source_file': str(md_path.relative_to(BLOG_DIR)),
    }


def collect_content() -> list[dict]:
    """Collecte tous les articles et tutoriels depuis content/."""
    articles = []
    src_dirs = [ARTICLES_SRC, TUTORIALS_SRC]

    for src_dir in src_dirs:
        if not src_dir.exists():
            continue
        for md_path in src_dir.rglob('*.md'):
            article = load_article(md_path)
            if article:
                articles.append(article)

    # Trie par date (plus recent en premier)
    articles.sort(key=lambda a: a.get('date', ''), reverse=True)
    return articles


def load_collections() -> list[dict]:
    """Charge les collections (series) depuis content/collections/."""
    collections = []
    if not COLLECTIONS_SRC.exists():
        return collections

    for json_path in COLLECTIONS_SRC.glob('*.json'):
        try:
            data = json.loads(json_path.read_text(encoding='utf-8'))
            collections.append(data)
        except Exception as e:
            print(f"[WARN] Collection invalide {json_path}: {e}")
    return collections


def _escape_html(s: str) -> str:
    """Echappe les caracteres HTML pour injection securisee."""
    return (s or '').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def _article_href(slug: str, prefix: str = '') -> str:
    """Lien fichier article (.html) pour hebergement statique et preview locale."""
    return f"{prefix}{slug}.html"


def _series_href(slug: str, prefix: str = '') -> str:
    return f"{prefix}{slug}.html"


def _abs_blog_url(path: str) -> str:
    """URL absolue stable pour hébergement statique (avec .html quand pertinent)."""
    base = SITE_BASE.rstrip('/')
    p = (path or '').lstrip('/')
    return f"{base}/{p}"


def _article_thumb_src(article: dict, assets_root: str = '/assets') -> str:
    """Image de couverture d'un article (chemin absolu site, valide depuis series/types/index)."""
    og = article.get('og_image')
    if og and str(og).startswith('http'):
        return str(og)
    root = (assets_root or '/assets').rstrip('/')
    if og:
        return f"{root}/images/og/{og}"
    return f"{root}/images/og/blog-1200x630.jpg"


def _collection_cover_src(collection: dict, articles: list[dict]) -> str:
    """Image de couverture d'une serie (chemin absolu /assets/...)."""
    cover = collection.get('cover_image')
    if cover:
        if str(cover).startswith('http'):
            return str(cover)
        if str(cover).startswith('blog/'):
            return f"/assets/images/{cover}"
        if str(cover).startswith('/'):
            return str(cover)
        return f"/assets/images/og/{cover}"
    for slug in collection.get('articles', []):
        for article in articles:
            if article.get('slug') == slug and article.get('og_image'):
                return f"/assets/images/og/{article['og_image']}"
    return '/assets/images/og/blog-1200x630.jpg'


def _series_featured_html(collections: list[dict], articles: list[dict]) -> str:
    """Bloc series mises en avant sur l'index du blog (cartes avec image)."""
    if not collections:
        return ''

    def sort_key(coll: dict) -> tuple:
        cid = coll.get('id') or coll.get('slug') or ''
        if 'design-patterns' in cid:
            return (0, coll.get('title', ''))
        return (1, coll.get('title', ''))

    lines = [
        '<section class="blog-series-featured blog-reveal" aria-label="Séries du blog">',
        '<h2 class="blog-section-title">Séries à suivre</h2>',
        '<p class="blog-series-intro">Parcours thématiques : images, schémas et articles à lire dans l’ordre.</p>',
        '<div class="blog-series-grid">',
    ]
    for i, coll in enumerate(sorted(collections, key=sort_key)):
        slug = coll.get('slug') or coll.get('id') or ''
        if not slug:
            continue
        title = _escape_html(coll.get('title', slug))
        desc_raw = coll.get('description') or ''
        desc = _escape_html(desc_raw[:180] + ('…' if len(desc_raw) > 180 else ''))
        n = len(coll.get('articles') or [])
        img = _escape_html(_collection_cover_src(coll, articles))
        article_word = 'articles' if n != 1 else 'article'
        lines.append(
            f'<a href="{_series_href(slug, "series/")}" class="series-card blog-card-animated blog-reveal-item blog-reveal-delay-{(i % 6) + 1}">'
            f'<div class="series-card-media">'
            f'<img src="{img}" alt="" width="600" height="315" loading="lazy" decoding="async" />'
            f'</div>'
            f'<div class="series-card-body">'
            f'<span class="series-card-badge">Série · {n} {article_word}</span>'
            f'<h3>{title}</h3>'
            f'<p>{desc}</p>'
            f'</div>'
            f'</a>'
        )
    lines.append('</div></section>')
    return '\n'.join(lines)


def _article_card_html(
    article: dict,
    *,
    href_prefix: str = 'articles/',
    heading_tag: str = 'h2',
    extra_classes: str = '',
) -> str:
    """Carte article avec vignette pour les grilles du blog."""
    date_str = str(article.get('date', ''))[:10]
    try:
        dt = datetime.fromisoformat(str(article.get('date', '')))
        date_fr = dt.strftime('%d %B %Y')
    except ValueError:
        date_fr = date_str
    excerpt_raw = article.get('excerpt') or ''
    excerpt = _escape_html(excerpt_raw[:160] + ('…' if len(excerpt_raw) > 160 else ''))
    type_label = _escape_html(_type_label(article))
    title = _escape_html(article['title'])
    img = _escape_html(_article_thumb_src(article))
    alt = _escape_html((article.get('title') or '')[:120])
    classes = f'article-card blog-card-animated {extra_classes}'.strip()
    article_url = _abs_blog_url(f'blog/articles/{article["slug"]}.html')
    href = _article_href(article['slug'], href_prefix)
    return (
        f'<a href="{href}" class="{classes}" itemscope itemtype="https://schema.org/BlogPosting" '
        f'itemprop="blogPost" itemid="{article_url}">'
        f'<link itemprop="url" href="{article_url}">'
        f'<div class="article-card-media">'
        f'<img src="{img}" alt="{alt}" width="600" height="315" loading="lazy" decoding="async" itemprop="image" />'
        f'</div>'
        f'<div class="article-card-body">'
        f'<span class="article-type">{type_label}</span>'
        f'<{heading_tag} itemprop="headline">{title}</{heading_tag}>'
        f'<div class="article-meta"><time datetime="{date_str}" itemprop="datePublished">{date_fr}</time></div>'
        f'<div class="article-excerpt" itemprop="description">{excerpt}</div>'
        f'<span class="article-card-cta">Lire l’article →</span>'
        f'</div>'
        f'</a>'
    )


def _og_image_file_meta(url: str) -> tuple[str, str, str]:
    """Largeur, hauteur et MIME réels du fichier OG local."""
    raw = (url or '').split('?')[0].split('#')[0]
    idx = raw.find('/assets/images/og/')
    if idx < 0:
        return '1200', '630', 'image/jpeg'
    rel = raw[idx + len('/assets/'):]
    local = PROJECT_ROOT / 'assets' / rel.replace('/', os.sep)
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


def _inject_og_image_meta(html: str, og_url: str) -> str:
    """Remplace {{OG_IMAGE*}} avec URL cache-bust et dimensions réelles du fichier."""
    busted = _og_image_cache_bust(og_url)
    w, h, mime = _og_image_file_meta(busted)
    return (
        html.replace('{{OG_IMAGE}}', busted)
        .replace('{{OG_IMAGE_WIDTH}}', w)
        .replace('{{OG_IMAGE_HEIGHT}}', h)
        .replace('{{OG_IMAGE_TYPE}}', mime)
    )


def _og_image_cache_bust(url: str) -> str:
    """?v=mtime sur les JPEG OG locaux (cache Facebook / LinkedIn / X)."""
    raw = (url or '').strip()
    if not raw or '/assets/images/og/' not in raw:
        return raw
    path_only = raw.split('?')[0].split('#')[0]
    idx = path_only.find('/assets/images/og/')
    if idx < 0:
        return raw
    rel = path_only[idx + len('/assets/'):]
    local = PROJECT_ROOT / 'assets' / rel.replace('/', os.sep)
    if not local.is_file():
        return raw
    try:
        mtime = datetime.fromtimestamp(local.stat().st_mtime).strftime('%Y%m%d%H%M')
    except OSError:
        return raw
    return f"{path_only}?v={mtime}"


def _get_article_og_image(article: dict) -> str:
    """Retourne l'URL absolue de l'image OG pour les metas et le schema.org."""
    og_img = article.get('og_image')
    if og_img and og_img.startswith('http'):
        url = og_img
    elif og_img:
        url = f"{SITE_BASE}/assets/images/og/{og_img}"
    else:
        url = OG_IMAGE_BLOG
    return _og_image_cache_bust(url)


def _get_article_hero_image(article: dict, assets_prefix: str) -> str:
    """Image hero de la page article (absolu /assets pour eviter les 404 selon la profondeur d'URL)."""
    og_img = article.get('og_image')
    if og_img and str(og_img).startswith('http'):
        return str(og_img)
    # assets_prefix conserve pour compat appelants ; chemins absolus preferes
    _ = assets_prefix
    if og_img:
        return f"/assets/images/og/{og_img}"
    return '/assets/images/og/blog-1200x630.jpg'


def _type_label(article: dict) -> str:
    """
    Retourne un libelle humain a partir du champ type du front matter.

    Exemples (type normalise en minuscules):
    - article / vide                    -> "Article"
    - tutorial / tutoriel               -> "Tutoriel"
    - guide                             -> "Guide"
    - comparatif                        -> "Comparatif"
    - case-study / etude_cas            -> "Étude de cas"
    - checklist                         -> "Checklist"
    - framework / methode / method      -> "Framework / Méthode"
    - glossary / glossaire / reference  -> "Référence"
    - toolbox / outils                  -> "Boîte à outils"
    - template                          -> "Template"
    - rex / retour-experience           -> "Retour d’expérience"
    """
    t = (article.get("type") or "article").strip().lower()
    if t in {"tutorial", "tutoriel"}:
        return "Tutoriel"
    if t in {"guide"}:
        return "Guide"
    if t in {"comparatif", "comparison"}:
        return "Comparatif"
    if t in {"case-study", "case_study", "etude_cas", "etude-de-cas", "etude de cas"}:
        return "Étude de cas"
    if t in {"checklist"}:
        return "Checklist"
    if t in {"framework", "methode", "method"}:
        return "Framework / Méthode"
    if t in {"reference", "glossaire", "glossary"}:
        return "Référence"
    if t in {"toolbox", "boite_outils", "outils"}:
        return "Boîte à outils"
    if t in {"template"}:
        return "Template"
    if t in {"rex", "retour-experience", "retour_experience"}:
        return "Retour d’expérience"
    return "Article"


def load_template(name: str) -> str:
    """Charge un template HTML."""
    path = TEMPLATES_DIR / name
    if path.exists():
        return path.read_text(encoding='utf-8')
    return ''


_BLOG_CLIENT_PRIORITY = (
    'seo-local', 'geo', 'seo', 'local', 'artisan', 'metz', 'google', 'vitrine', 'visibilité',
)


def _article_client_priority_score(article: dict) -> int:
    """Score pour mettre en avant les articles utiles aux artisans / SEO local."""
    parts = [
        article.get('title', ''),
        article.get('excerpt', ''),
        ' '.join(article.get('tags') or []),
        article.get('series') or '',
        article.get('slug', ''),
    ]
    text = ' '.join(str(p) for p in parts).lower()
    return sum(2 for kw in _BLOG_CLIENT_PRIORITY if kw in text)


def _recommendations_index_html(articles: list[dict], collections: list[dict]) -> str:
    """Bloc « À la une » (1 grand) + grille de 3, style maquette Medium."""
    if not articles:
        return ''
    seen = set()
    picked = []
    for coll in collections:
        coll_id = coll.get('id', '') or coll.get('slug', '')
        if 'seo' not in str(coll_id).lower() and 'geo' not in str(coll_id).lower():
            continue
        for a in articles:
            if a.get('series') == coll_id and a['slug'] not in seen:
                picked.append(a)
                seen.add(a['slug'])
                break
        if len(picked) >= 4:
            break
    ranked = sorted(articles, key=_article_client_priority_score, reverse=True)
    for a in ranked:
        if len(picked) >= 4:
            break
        if a['slug'] not in seen:
            picked.append(a)
            seen.add(a['slug'])
    if not picked:
        return ''

    hero = picked[0]
    rest = picked[1:4]
    hero_href = _article_href(hero['slug'], 'articles/')
    hero_url = _abs_blog_url(f'blog/articles/{hero["slug"]}.html')
    hero_img = _escape_html(_article_thumb_src(hero))
    hero_title = _escape_html(hero['title'])
    hero_excerpt = _escape_html((hero.get('excerpt') or '')[:220] + ('…' if len(hero.get('excerpt') or '') > 220 else ''))
    hero_type = _escape_html(_type_label(hero))
    reading = max(4, min(14, len((hero.get('excerpt') or '') + hero.get('title', '')) // 45 or 8))

    lines = [
        '<section class="blog-spotlight blog-reveal" aria-label="À la une">',
        f'<a href="{hero_href}" class="blog-spotlight-card blog-reveal-item" itemscope itemtype="https://schema.org/BlogPosting" itemid="{hero_url}">',
        f'<link itemprop="url" href="{hero_url}">',
        f'<div class="blog-spotlight-media"><img src="{hero_img}" alt="" width="800" height="420" loading="eager" decoding="async" itemprop="image" /></div>',
        '<div class="blog-spotlight-body">',
        '<p class="blog-spotlight-kicker">À la une</p>',
        f'<h2 class="blog-spotlight-title" itemprop="headline">{hero_title}</h2>',
        f'<p class="blog-spotlight-excerpt" itemprop="description">{hero_excerpt}</p>',
        '<div class="blog-spotlight-meta">',
        f'<span><i class="fas fa-clock" aria-hidden="true"></i> {reading} min de lecture</span>',
        f'<span class="blog-spotlight-tag">{hero_type}</span>',
        '<span class="blog-spotlight-cta">Lire l’article →</span>',
        '</div></div></a>',
    ]
    if rest:
        lines.append('<div class="blog-spotlight-grid">')
        for i, a in enumerate(rest):
            lines.append(
                _article_card_html(
                    a,
                    href_prefix='articles/',
                    heading_tag='h3',
                    extra_classes=f'recommendation-featured blog-reveal-item blog-reveal-delay-{i + 2}',
                )
            )
        lines.append('</div>')
    lines.append('</section>')
    return '\n'.join(lines)


def _prev_next_html(articles: list[dict], current_slug: str) -> str:
    """Genere le bloc HTML article precedent / suivant (meme serie ou ordre global)."""
    idx = next((i for i, a in enumerate(articles) if a['slug'] == current_slug), -1)
    if idx < 0:
        return ''
    prev_a = articles[idx - 1] if idx > 0 else None
    next_a = articles[idx + 1] if idx < len(articles) - 1 else None
    parts = ['<div class="prev-next-links">']
    if prev_a:
        parts.append(f'<a href="{_article_href(prev_a["slug"])}" class="prev-next-link prev-link"><i class="fas fa-arrow-left"></i> {prev_a["title"]}</a>')
    else:
        parts.append('<span class="prev-next-link prev-link empty"></span>')
    if next_a:
        parts.append(f'<a href="{_article_href(next_a["slug"])}" class="prev-next-link next-link">{next_a["title"]} <i class="fas fa-arrow-right"></i></a>')
    else:
        parts.append('<span class="prev-next-link next-link empty"></span>')
    parts.append('</div>')
    return '\n'.join(parts)


def _recommendations_html(articles: list[dict], current_article: dict, max_n: int = 4) -> str:
    """Genere le bloc HTML des articles recommandes (meme serie, puis autres)."""
    current_slug = current_article['slug']
    series_id = current_article.get('series')
    same_series = [a for a in articles if a.get('series') == series_id and a['slug'] != current_slug]
    others = [a for a in articles if a['slug'] != current_slug and a not in same_series]
    recommended = (same_series[:max_n] if same_series else []) + [a for a in others if a not in same_series][:max_n - len(same_series)]
    recommended = recommended[:max_n]
    if not recommended:
        return ''
    lines = ['<h2 class="recommendations-title">Articles recommandés</h2>', '<div class="recommendations-grid">']
    for a in recommended:
        date_str = str(a.get('date', ''))[:10]
        try:
            dt = datetime.fromisoformat(str(a.get('date', '')))
            date_fr = dt.strftime('%d %B %Y')
        except Exception:
            date_fr = date_str
        excerpt = (a.get('excerpt') or '')[:120] + ('...' if len(a.get('excerpt') or '') > 120 else '')
        type_label = _type_label(a)
        lines.append(f'''<a href="{_article_href(a["slug"])}" class="article-card recommendation-card">
            <span class="article-type">{type_label}</span>
            <h3>{a["title"]}</h3>
            <div class="article-meta">{date_fr}</div>
            <div class="article-excerpt">{excerpt}</div>
        </a>''')
    lines.append('</div>')
    return '\n'.join(lines)


def render_article_page(article: dict, articles: list[dict], collections: list[dict], output_dir: Path, assets_prefix: str, assets_prefix_article: str) -> None:
    """Genere la page HTML d'un article (avec prev/next et recommandations)."""
    template = load_template('article.html')
    if not template:
        template = _default_article_template()

    date_str = str(article.get('date', ''))[:10]
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        date_obj = datetime.now()
    date_fr = date_obj.strftime('%d %B %Y')

    page_url = _abs_blog_url(f"blog/articles/{article['slug']}.html")
    share_twitter_url = 'https://twitter.com/intent/tweet?url=' + quote(page_url, safe='') + '&text=' + quote(article['title'], safe='')
    share_linkedin_url = 'https://www.linkedin.com/sharing/share-offsite/?url=' + quote(page_url, safe='')
    keywords = ', '.join(article.get('tags', [])) or 'développement web, TypeScript, blog'
    excerpt = _escape_html(article.get('excerpt', ''))
    title = _escape_html(article['title'])
    og_img_url = _get_article_og_image(article)
    og_w, og_h, og_mime = _og_image_file_meta(og_img_url)
    hero_img_url = _get_article_hero_image(article, assets_prefix_article)

    prev_next = _prev_next_html(articles, article['slug'])
    recommendations = _recommendations_html(articles, article)

    # Serie (collection) pour la sidebar
    series_id = article.get('series')
    series_title = ''
    series_url = ''
    series_html = ''
    if series_id and collections:
        for coll in collections:
            if coll.get('id') == series_id or coll.get('slug') == series_id:
                series_title = coll.get('title', series_id)
                slug = coll.get('slug', coll.get('id', series_id))
                series_url = _abs_blog_url(f"blog/series/{slug}.html")
                series_html = f'<span class="sidebar-label">Série</span><a href="{series_url}" class="sidebar-series-link">' + _escape_html(series_title) + '</a>'
                break

    html = template.replace('{{TITLE}}', title)
    html = html.replace('{{EXCERPT}}', excerpt)
    html = html.replace('{{CONTENT}}', article['content_html'])
    html = html.replace('{{DATE_ISO}}', date_str)
    html = html.replace('{{DATE_MODIFIED_ISO}}', date_str)
    html = html.replace('{{DATE_FR}}', date_fr)
    html = html.replace('{{PAGE_URL}}', page_url)
    # JSON-LD (valeurs JSON encodees)
    _site = SITE_BASE.rstrip('/')
    html = html.replace('{{JSON_HEADLINE}}', json.dumps(title, ensure_ascii=False))
    html = html.replace('{{JSON_DESCRIPTION}}', json.dumps(excerpt, ensure_ascii=False))
    html = html.replace('{{JSON_IMAGE}}', json.dumps(og_img_url, ensure_ascii=False))
    html = html.replace('{{JSON_DATE_PUBLISHED}}', json.dumps(date_str))
    html = html.replace('{{JSON_DATE_MODIFIED}}', json.dumps(date_str))
    html = html.replace('{{JSON_PAGE_URL}}', json.dumps(page_url, ensure_ascii=False))
    html = html.replace('{{JSON_SITE_BASE}}', json.dumps(_site + '/', ensure_ascii=False))
    html = html.replace('{{JSON_LOGO}}', json.dumps(_site + '/assets/images/og/home-1200x630.jpg', ensure_ascii=False))
    html = html.replace('{{SHARE_TWITTER_URL}}', share_twitter_url)
    html = html.replace('{{SHARE_LINKEDIN_URL}}', share_linkedin_url)
    html = html.replace('{{OG_IMAGE}}', og_img_url)
    html = html.replace('{{OG_IMAGE_WIDTH}}', og_w)
    html = html.replace('{{OG_IMAGE_HEIGHT}}', og_h)
    html = html.replace('{{OG_IMAGE_TYPE}}', og_mime)
    html = html.replace('{{HERO_IMAGE}}', hero_img_url)
    html = html.replace('{{META_KEYWORDS}}', _escape_html(keywords))
    html = html.replace('{{ARTICLE_SECTION}}', _escape_html(_type_label(article)))
    html = html.replace('{{SITE_BASE}}', SITE_BASE)
    html = html.replace('{{PREV_NEXT}}', prev_next)
    html = html.replace('{{RECOMMENDATIONS}}', recommendations)
    html = html.replace('{{SERIES_HTML}}', series_html)
    html = html.replace(
        '{{BREADCRUMBS}}',
        block_breadcrumbs(
            crumbs_article(
                SITE_BASE,
                article['title'],
                series_title=series_title,
                series_url=series_url,
            )
        ),
    )

    html = _apply_asset_paths(html)
    html = _inject_site_layout(html)

    out_file = output_dir / 'articles' / f"{article['slug']}.html"
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(html, encoding='utf-8')


def _default_article_template() -> str:
    """Template HTML par defaut pour un article."""
    return '''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}} | Blog DanielCraft</title>
    <meta name="description" content="{{EXCERPT}}">
    <link rel="stylesheet" href="{{ASSETS}}/css/main.css">
    <link rel="stylesheet" href="{{ASSETS}}/css/responsive.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
</head>
<body>
    <main class="blog-article">
        <article>
            <header>
                <h1>{{TITLE}}</h1>
                <div class="article-meta"><time datetime="{{DATE_ISO}}">{{DATE_FR}}</time></div>
            </header>
            <div class="article-content">{{CONTENT}}</div>
        </article>
    </main>
</body>
</html>'''


def render_blog_index(articles: list[dict], collections: list[dict], output_dir: Path, assets_prefix: str) -> None:
    """Genere la page index du blog (liste des articles)."""
    template = load_template('blog_index.html')
    if not template:
        template = _default_blog_index_template()

    # Liste des articles en JSON pour le JS (convertit dates en str)
    articles_serializable = []
    for a in articles:
        ac = {k: v for k, v in a.items() if k not in ('content_html', 'source_file')}
        d = ac.get('date')
        if d is not None and hasattr(d, 'isoformat'):
            ac['date'] = d.isoformat()
        articles_serializable.append(ac)
    articles_json = json.dumps(articles_serializable, ensure_ascii=False, indent=2)
    collections_json = json.dumps(collections, ensure_ascii=False, indent=2)

    # Pre-render des cartes HTML pour le SEO (pas de chargement async)
    cards_html = []
    for i, a in enumerate(articles):
        cards_html.append(
            _article_card_html(
                a,
                href_prefix='articles/',
                heading_tag='h2',
                extra_classes=f'blog-reveal-item blog-reveal-delay-{(i % 8) + 1}',
            )
        )

    meta_desc = 'Guides SEO local, visibilité Google, IA pratique (ChatGPT, Claude, Gemini, agents) et site vitrine — plus articles techniques sur l’espace pro.'
    page_url = _abs_blog_url('blog/index.html')

    # Bloc "A découvrir" : 4 articles (un par serie ou derniers)
    series_html = _series_featured_html(collections, articles)
    rec_index_html = _recommendations_index_html(articles, collections)
    html = template.replace('{{SERIES_FEATURED}}', series_html)
    html = html.replace('{{RECOMMENDATIONS_INDEX}}', rec_index_html)
    html = html.replace('{{ARTICLES_GRID}}', '\n'.join(cards_html))
    html = html.replace('{{ARTICLES_JSON}}', articles_json)
    html = html.replace('{{COLLECTIONS_JSON}}', collections_json)
    html = html.replace('{{META_DESCRIPTION}}', _escape_html(meta_desc))
    html = html.replace('{{META_KEYWORDS}}', 'IA, ChatGPT, Claude, Gemini, prompts, agents, SEO, GEO, tutoriels, formations')
    html = html.replace('{{PAGE_URL}}', page_url)
    html = html.replace('{{SITE_BASE}}', SITE_BASE.rstrip('/'))
    html = _inject_og_image_meta(html, OG_IMAGE_BLOG)
    html = _apply_asset_paths(html)
    html = _inject_site_layout(html)

    out_file = output_dir / 'index.html'
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(html, encoding='utf-8')


def _default_blog_index_template() -> str:
    """Template par defaut pour l'index du blog."""
    return '''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog | DanielCraft - Articles et tutoriels</title>
    <meta name="description" content="Blog DanielCraft : articles sur le developpement web, TypeScript, et bonnes pratiques.">
    <link rel="stylesheet" href="{{ASSETS}}/css/main.css">
    <link rel="stylesheet" href="{{ASSETS}}/css/responsive.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        .blog-page { max-width: 1200px; margin: 0 auto; padding: 2rem; }
        .blog-header { text-align: center; margin-bottom: 3rem; }
        .blog-header h1 { font-size: 2.5rem; color: #333; }
        .articles-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 1.5rem; }
        .article-card { background: white; border-radius: 8px; padding: 1.5rem; box-shadow: 0 2px 10px rgba(0,0,0,0.08); text-decoration: none; color: inherit; display: block; transition: transform 0.2s, box-shadow 0.2s; }
        .article-card:hover { transform: translateY(-3px); box-shadow: 0 4px 20px rgba(0,0,0,0.12); }
        .article-type { font-size: 0.75rem; text-transform: uppercase; color: #dc2626; font-weight: 600; }
        .article-card h2 { font-size: 1.25rem; margin: 0.5rem 0; color: #333; }
        .article-meta { color: #6b7280; font-size: 0.875rem; }
        .article-excerpt { color: #555; font-size: 0.9rem; line-height: 1.5; margin-top: 0.5rem; }
    </style>
</head>
<body>
    <main class="blog-page">
        <div class="blog-header">
            <h1>Blog DanielCraft</h1>
            <p>Articles et tutoriels sur le developpement web</p>
        </div>
        <div class="articles-grid">{{ARTICLES_GRID}}</div>
    </main>
</body>
</html>'''


def render_collection_page(collection: dict, all_articles: list[dict], output_dir: Path, assets_prefix: str, assets_prefix_series: str) -> None:
    """Genere une page pour une collection (serie)."""
    slugs = collection.get('articles', [])
    items = []
    for slug in slugs:
        for a in all_articles:
            if a['slug'] == slug:
                items.append(a)
                break

    if not items:
        return

    template = load_template('collection.html')
    if not template:
        return

    cards = []
    for a in items:
        date_str = a.get('date', '')[:10]
        try:
            dt = datetime.fromisoformat(a.get('date', ''))
            date_fr = dt.strftime('%d %B %Y')
        except Exception:
            date_fr = date_str
        type_label = _type_label(a)
        excerpt = a.get("excerpt", "")
        cards.append(
            _article_card_html(a, href_prefix='../articles/', heading_tag='h2')
        )

    slug = collection.get('slug', collection.get('id', 'serie'))
    page_url = _abs_blog_url(f'blog/series/{slug}.html')
    title = collection.get('title', 'Serie')
    desc = collection.get('description', '')
    keywords = ', '.join({tag for a in items for tag in a.get('tags', [])}) or 'blog, série'

    html = template.replace('{{TITLE}}', _escape_html(title))
    html = html.replace('{{DESCRIPTION}}', _escape_html(desc))
    html = html.replace('{{ARTICLES_GRID}}', '\n'.join(cards))
    html = html.replace('{{PAGE_URL}}', page_url)
    html = _inject_og_image_meta(html, OG_IMAGE_BLOG)
    html = html.replace('{{META_KEYWORDS}}', _escape_html(keywords))
    html = html.replace(
        '{{BREADCRUMBS}}',
        block_breadcrumbs(crumbs_collection(SITE_BASE, title)),
    )

    html = _apply_asset_paths(html)
    html = _inject_site_layout(html)

    out_file = output_dir / 'series' / f'{slug}.html'
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(html, encoding='utf-8')


def _type_slug(article_type: str) -> str:
    """Slug propre pour une page de type (tutoriels, guides, etudes-de-cas...)."""
    t = (article_type or '').strip().lower()
    if not t:
        return ''
    return t.replace('_', '-').replace(' ', '-')


def render_type_pages(articles: list[dict], output_dir: Path, assets_prefix: str, assets_prefix_types: str) -> None:
    """Genere des pages /blog/types/<type> pour chaque type d'article non vide."""
    template = load_template('collection.html')
    if not template:
        return

    # Regrouper les articles par type (hors 'article' vide)
    by_type: Dict[str, List[dict]] = {}
    for a in articles:
        t = (a.get('type') or '').strip().lower()
        if not t or t == 'article':
            continue
        by_type.setdefault(t, []).append(a)

    if not by_type:
        return

    type_title_map = {
        'tutorial': 'Tutoriels',
        'tutoriel': 'Tutoriels',
        'guide': 'Guides',
        'comparatif': 'Comparatifs',
        'case-study': 'Études de cas',
        'case_study': 'Études de cas',
        'etude_cas': 'Études de cas',
        'etude-de-cas': 'Études de cas',
        'etude de cas': 'Études de cas',
        'checklist': 'Checklists',
        'framework': 'Frameworks & méthodes',
        'methode': 'Frameworks & méthodes',
        'method': 'Frameworks & méthodes',
        'glossaire': 'Glossaires & références',
        'glossary': 'Glossaires & références',
        'reference': 'Glossaires & références',
        'toolbox': 'Boîtes à outils',
        'outils': 'Boîtes à outils',
        'boite_outils': 'Boîtes à outils',
        'template': 'Templates',
        'rex': 'Retours d’expérience',
        'retour-experience': 'Retours d’expérience',
        'retour_experience': 'Retours d’expérience',
    }

    for t, items in by_type.items():
        if not items:
            continue
        slug = _type_slug(t)
        title = type_title_map.get(t, _type_label({'type': t}))
        desc = f"{title} DanielCraft : tous les contenus de type {title.lower()}."

        cards: List[str] = []
        for a in sorted(items, key=lambda x: x.get('date', ''), reverse=True):
            cards.append(
                _article_card_html(a, href_prefix='../articles/', heading_tag='h2')
            )

        page_url = _abs_blog_url(f'blog/types/{slug}.html')
        html = template.replace('{{TITLE}}', _escape_html(title))
        html = html.replace('{{DESCRIPTION}}', _escape_html(desc))
        html = html.replace('{{ARTICLES_GRID}}', '\n'.join(cards))
        html = html.replace('{{PAGE_URL}}', page_url)
        html = _inject_og_image_meta(html, OG_IMAGE_BLOG)
        html = html.replace('{{META_KEYWORDS}}', _escape_html(f"{title}, blog, DanielCraft"))
        html = html.replace(
            '{{BREADCRUMBS}}',
            block_breadcrumbs(crumbs_collection(SITE_BASE, title)),
        )
        html = _apply_asset_paths(html)
        html = _inject_site_layout(html)

        out_file = output_dir / 'types' / f'{slug}.html'
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(html, encoding='utf-8')


def generate_sitemap_blog(articles: list[dict], collections: list[dict], output_dir: Path) -> None:
    """Genere sitemap-blog.xml pour le referencement (namespace et lastmod optimises)."""
    from urllib.parse import quote

    lastmod_blog = max((str(a.get('date', ''))[:10] for a in articles), default=datetime.now().strftime('%Y-%m-%d'))
    # Recherches populaires (chips) — deep-links indexables via SearchAction
    blog_search_queries = (
        'seo local',
        'google',
        'visibilité',
        'chatgpt',
        'claude',
        'gemini',
        'agents ia',
        'prompts',
        'n8n',
        'formation',
        'geo',
        'docker',
    )
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"',
        '        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 '
        'http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">',
        f'  <url><loc>{SITE_BASE}/blog</loc><lastmod>{lastmod_blog}</lastmod>'
        f'<changefreq>weekly</changefreq><priority>0.8</priority></url>',
    ]
    for q in blog_search_queries:
        url = f'{SITE_BASE}/blog/?q={quote(q, safe="")}'
        lines.append(
            f'  <url><loc>{url}</loc><lastmod>{lastmod_blog}</lastmod>'
            f'<changefreq>weekly</changefreq><priority>0.55</priority></url>'
        )
    for a in articles:
        url = f'{SITE_BASE}/blog/articles/{a["slug"]}'
        date = str(a.get('date', ''))[:10]
        lines.append(f'  <url><loc>{url}</loc><lastmod>{date}</lastmod><changefreq>monthly</changefreq><priority>0.6</priority></url>')
    for c in collections:
        slug = c.get('slug', c.get('id', ''))
        if slug:
            url = f'{SITE_BASE}/blog/series/{slug}'
            # lastmod serie = dernier article de la serie si possible
            coll_articles = [a for a in articles if a.get('series') == c.get('id')]
            lastmod_c = max((str(a.get('date', ''))[:10] for a in coll_articles), default=lastmod_blog)
            lines.append(f'  <url><loc>{url}</loc><lastmod>{lastmod_c}</lastmod><changefreq>monthly</changefreq><priority>0.5</priority></url>')
    # Pages par type (dossiers tutoriels, guides, études de cas, etc.)
    type_slugs: Dict[str, str] = {}
    for a in articles:
        t = (a.get('type') or 'article').strip().lower()
        if not t or t == 'article':
            continue
        if t not in type_slugs:
            slug = t.replace('_', '-').replace(' ', '-')
            type_slugs[t] = slug
    for t, slug in type_slugs.items():
        url = f'{SITE_BASE}/blog/types/{slug}'
        lastmod_t = lastmod_blog
        lines.append(f'  <url><loc>{url}</loc><lastmod>{lastmod_t}</lastmod><changefreq>monthly</changefreq><priority>0.5</priority></url>')
    lines.append('</urlset>')
    (output_dir / 'sitemap-blog.xml').write_text('\n'.join(lines), encoding='utf-8')


def save_list_json(articles: list[dict], output_dir: Path) -> None:
    """Sauvegarde list.json pour compatibilite avec l'ancien systeme."""
    # Enleve le HTML du contenu pour l'index
    list_data = []
    for a in articles:
        list_data.append({
            'title': a['title'],
            'slug': a['slug'],
            'date': a['date'],
            'excerpt': a.get('excerpt', ''),
            'type': a.get('type', 'article'),
            'tags': a.get('tags', []),
            'series': a.get('series'),
            'series_order': a.get('series_order'),
        })
    out_file = output_dir / 'articles' / 'list.json'
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(json.dumps(list_data, ensure_ascii=False, indent=2), encoding='utf-8')


def main():
    """Point d'entree."""
    global _SITE_LAYOUT_CACHE
    _SITE_LAYOUT_CACHE = None

    # Parse --output
    output_arg = 'dist/blog'
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == '--output' and i + 1 < len(sys.argv):
            output_arg = sys.argv[i + 1]
            i += 2
        else:
            i += 1

    # Chemin de sortie : relatif a la racine du projet (parent de blog/)
    project_root = BLOG_DIR.parent
    output_dir = (project_root / output_arg).resolve()
    assets_prefix = '../assets'   # depuis dist/blog/

    print(f"[BLOG] Compilation vers {output_dir}")

    articles = collect_content()
    collections = load_collections()

    if not articles:
        print("[WARN] Aucun article trouve dans content/articles/ et content/tutorials/")
        # Cree quand meme la structure
        output_dir.mkdir(parents=True, exist_ok=True)

    # Genere les templates s'ils n'existent pas
    TEMPLATES_DIR.mkdir(exist_ok=True)
    if not (TEMPLATES_DIR / 'article.html').exists():
        _write_default_templates()

    assets_prefix_article = '../' + assets_prefix  # depuis blog/articles/ -> ../../assets
    for article in articles:
        render_article_page(article, articles, collections, output_dir, assets_prefix, assets_prefix_article)
        print(f"  [OK] {article['slug']}.html")

    # Index principal du blog
    render_blog_index(articles, collections, output_dir, assets_prefix)
    print("  [OK] index.html")

    # JSON list.json + sitemap (incl. series + types)
    save_list_json(articles, output_dir)
    generate_sitemap_blog(articles, collections, output_dir)
    print("  [OK] sitemap-blog.xml")

    # Pages de series
    assets_prefix_series = '../../assets'  # depuis dist/blog/series/
    for coll in collections:
        render_collection_page(coll, articles, output_dir, assets_prefix, assets_prefix_series)
        print(f"  [OK] series/{coll.get('slug', coll.get('id'))}.html")

    # Pages par type (tutoriels, guides, études de cas, etc.)
    assets_prefix_types = '../../assets'  # depuis dist/blog/types/
    render_type_pages(articles, output_dir, assets_prefix, assets_prefix_types)

    print(f"\n[BLOG] Termine : {len(articles)} article(s), {len(collections)} collection(s)")


def _write_default_templates() -> None:
    """Ecrit les templates par defaut dans templates/."""
    article_tpl = '''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}} | Blog DanielCraft</title>
    <meta name="description" content="{{EXCERPT}}">
    <link rel="stylesheet" href="{{ASSETS}}/css/main.css">
    <link rel="stylesheet" href="{{ASSETS}}/css/responsive.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
</head>
<body>
    <main class="blog-article">
        <article>
            <header>
                <h1>{{TITLE}}</h1>
                <div class="article-meta"><time datetime="{{DATE_ISO}}">{{DATE_FR}}</time></div>
            </header>
            <div class="article-content">{{CONTENT}}</div>
        </article>
    </main>
</body>
</html>'''
    (TEMPLATES_DIR / 'article.html').write_text(article_tpl, encoding='utf-8')
    print("[BLOG] Templates par defaut crees dans blog/templates/")


if __name__ == '__main__':
    main()
