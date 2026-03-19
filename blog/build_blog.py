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
from urllib.parse import quote

try:
    import markdown
    import yaml
except ImportError as e:
    print(f"[ERREUR] Dependances manquantes : {e}")
    print("Installe avec : pip install markdown PyYAML")
    sys.exit(1)

# Configuration
SITE_BASE = os.environ.get('SITE_BASE', 'https://example.com')
OG_IMAGE_BLOG = f'{SITE_BASE}/assets/images/og/blog-1200x630.jpg'
OG_IMAGE_HOME = f'{SITE_BASE}/assets/images/og/home-1200x630.jpg'
BLOG_DIR = Path(__file__).parent
CONTENT_DIR = BLOG_DIR / 'content'
ARTICLES_SRC = CONTENT_DIR / 'articles'
TUTORIALS_SRC = CONTENT_DIR / 'tutorials'
COLLECTIONS_SRC = CONTENT_DIR / 'collections'
TEMPLATES_DIR = BLOG_DIR / 'templates'


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


def load_article(md_path: Path) -> dict | None:
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


def _get_article_og_image(article: dict) -> str:
    """Retourne l'URL de l'image OG pour un article."""
    og_img = article.get('og_image')
    if og_img and og_img.startswith('http'):
        return og_img
    if og_img:
        return f"{SITE_BASE}/assets/images/og/{og_img}"
    return OG_IMAGE_BLOG


def _schema_article(article: dict) -> str:
    """Genere le JSON-LD schema.org pour un article (optimise RDF/SEO).

    Le champ `type` du front matter ajuste:
    - le libelle articleSection/genre
    - parfois le @type schema.org (HowTo / TechArticle / Report)
    """
    url = f"{SITE_BASE}/blog/articles/{article['slug']}"
    raw_type = (article.get('type') or 'article').strip().lower()
    label = _type_label(article)

    schema_type = 'BlogPosting'
    if raw_type in {'tutorial', 'tutoriel', 'checklist', 'template'}:
        schema_type = 'HowTo'
    elif raw_type in {'guide', 'framework', 'methode', 'method'}:
        schema_type = 'TechArticle'
    elif raw_type in {'case-study', 'case_study', 'etude_cas', 'etude-de-cas', 'etude de cas', 'rex', 'retour-experience', 'retour_experience'}:
        schema_type = 'Report'

    schema = {
        '@context': 'https://schema.org',
        '@type': schema_type,
        'headline': article['title'],
        'description': article.get('excerpt', ''),
        'url': url,
        'image': _get_article_og_image(article),
        'datePublished': article.get('date', '')[:10],
        'dateModified': article.get('date', '')[:10],
        'inLanguage': 'fr-FR',
        'articleSection': label,
        'genre': label,
        'author': {
            '@type': 'Person',
            'name': 'Loïc DANIEL',
            'url': SITE_BASE,
            'sameAs': ['https://linkedin.com/in/loicdaniel', 'https://github.com/danielcraft57']
        },
        'publisher': {
            '@type': 'Organization',
            'name': 'DanielCraft',
            'url': SITE_BASE,
            'logo': {'@type': 'ImageObject', 'url': f'{SITE_BASE}/assets/icons/favicon.svg'}
        },
        'mainEntityOfPage': {'@type': 'WebPage', '@id': url}
    }
    if article.get('tags'):
        schema['keywords'] = ', '.join(article['tags'])
    breadcrumb = {
        '@context': 'https://schema.org',
        '@type': 'BreadcrumbList',
        'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Accueil', 'item': SITE_BASE + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Blog', 'item': SITE_BASE + '/blog'},
            {'@type': 'ListItem', 'position': 3, 'name': article['title'], 'item': url}
        ]
    }
    scripts = f'<script type="application/ld+json">\n{json.dumps(schema, ensure_ascii=False, indent=2)}\n</script>\n<script type="application/ld+json">\n{json.dumps(breadcrumb, ensure_ascii=False, indent=2)}\n</script>'
    return scripts


def _schema_blog_index(articles: list[dict]) -> str:
    """Genere le JSON-LD schema.org Blog pour la page index (optimise RDF/SEO)."""
    schema = {
        '@context': 'https://schema.org',
        '@type': 'Blog',
        'name': 'Blog DanielCraft',
        'description': 'Articles et tutoriels sur le développement web, TypeScript, GEO, SEO et bonnes pratiques.',
        'url': f'{SITE_BASE}/blog',
        'inLanguage': 'fr-FR',
        'publisher': {
            '@type': 'Organization',
            'name': 'DanielCraft',
            'url': SITE_BASE,
            'logo': {'@type': 'ImageObject', 'url': f'{SITE_BASE}/assets/icons/favicon.svg'}
        },
    }
    if articles:
        schema['numberOfPosts'] = len(articles)
        schema['blogPost'] = [
            {'@type': 'BlogPosting', 'url': f'{SITE_BASE}/blog/articles/{a["slug"]}', 'headline': a['title']}
            for a in articles[:50]
        ]
    breadcrumb = {
        '@context': 'https://schema.org',
        '@type': 'BreadcrumbList',
        'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Accueil', 'item': SITE_BASE + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Blog', 'item': SITE_BASE + '/blog'}
        ]
    }
    return f'<script type="application/ld+json">\n{json.dumps(schema, ensure_ascii=False, indent=2)}\n</script>\n<script type="application/ld+json">\n{json.dumps(breadcrumb, ensure_ascii=False, indent=2)}\n</script>'


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


def _schema_collection(collection: dict, items: list) -> str:
    """Genere le JSON-LD schema.org CollectionPage pour une serie (optimise RDF/SEO)."""
    url = f"{SITE_BASE}/blog/series/{collection.get('slug', collection.get('id', ''))}"
    schema = {
        '@context': 'https://schema.org',
        '@type': 'CollectionPage',
        'name': collection.get('title', ''),
        'description': collection.get('description', ''),
        'url': url,
        'inLanguage': 'fr-FR',
    }
    if items:
        schema['mainEntity'] = {
            '@type': 'ItemList',
            'numberOfItems': len(items),
            'itemListElement': [
                {'@type': 'ListItem', 'position': i + 1, 'url': f'{SITE_BASE}/blog/articles/{a["slug"]}', 'name': a['title']}
                for i, a in enumerate(items[:100])
            ]
        }
    breadcrumb = {
        '@context': 'https://schema.org',
        '@type': 'BreadcrumbList',
        'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Accueil', 'item': SITE_BASE + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Blog', 'item': SITE_BASE + '/blog'},
            {'@type': 'ListItem', 'position': 3, 'name': collection.get('title', ''), 'item': url}
        ]
    }
    return f'<script type="application/ld+json">\n{json.dumps(schema, ensure_ascii=False, indent=2)}\n</script>\n<script type="application/ld+json">\n{json.dumps(breadcrumb, ensure_ascii=False, indent=2)}\n</script>'


def load_template(name: str) -> str:
    """Charge un template HTML."""
    path = TEMPLATES_DIR / name
    if path.exists():
        return path.read_text(encoding='utf-8')
    return ''


def _recommendations_index_html(articles: list[dict], collections: list[dict]) -> str:
    """Genere le bloc "A découvrir" pour la page index du blog (4 articles mis en avant)."""
    if not articles:
        return ''
    seen = set()
    picked = []
    for coll in collections[:4]:
        coll_id = coll.get('id', '')
        for a in articles:
            if a.get('series') == coll_id and a['slug'] not in seen:
                picked.append(a)
                seen.add(a['slug'])
                break
    for a in articles:
        if len(picked) >= 4:
            break
        if a['slug'] not in seen:
            picked.append(a)
            seen.add(a['slug'])
    if not picked:
        return ''
    lines = ['<section class="blog-recommendations-index" aria-label="A découvrir">',
             '<h2 class="blog-section-title">À découvrir</h2>',
             '<div class="recommendations-index-grid">']
    for a in picked[:4]:
        date_str = str(a.get('date', ''))[:10]
        try:
            dt = datetime.fromisoformat(str(a.get('date', '')))
            date_fr = dt.strftime('%d %B %Y')
        except Exception:
            date_fr = date_str
        excerpt = (a.get('excerpt') or '')[:140] + ('...' if len(a.get('excerpt') or '') > 140 else '')
        type_label = _type_label(a)
        lines.append(f'''<a href="articles/{a["slug"]}" class="article-card recommendation-featured">
            <span class="article-type">{type_label}</span>
            <h2>{a["title"]}</h2>
            <div class="article-meta">{date_fr}</div>
            <div class="article-excerpt">{excerpt}</div>
        </a>''')
    lines.append('</div></section>')
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
        parts.append(f'<a href="{prev_a["slug"]}" class="prev-next-link prev-link"><i class="fas fa-arrow-left"></i> {prev_a["title"]}</a>')
    else:
        parts.append('<span class="prev-next-link prev-link empty"></span>')
    if next_a:
        parts.append(f'<a href="{next_a["slug"]}" class="prev-next-link next-link">{next_a["title"]} <i class="fas fa-arrow-right"></i></a>')
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
        lines.append(f'''<a href="{a["slug"]}" class="article-card recommendation-card">
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

    page_url = f"{SITE_BASE}/blog/articles/{article['slug']}"
    share_twitter_url = 'https://twitter.com/intent/tweet?url=' + quote(page_url, safe='') + '&text=' + quote(article['title'], safe='')
    share_linkedin_url = 'https://www.linkedin.com/sharing/share-offsite/?url=' + quote(page_url, safe='')
    keywords = ', '.join(article.get('tags', [])) or 'développement web, TypeScript, blog'
    excerpt = _escape_html(article.get('excerpt', ''))
    title = _escape_html(article['title'])
    og_img_url = _get_article_og_image(article)

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
                series_url = f"{SITE_BASE}/blog/series/{slug}"
                series_html = f'<span class="sidebar-label">Série</span><a href="{series_url}" class="sidebar-series-link">' + _escape_html(series_title) + '</a>'
                break

    html = template.replace('{{TITLE}}', title)
    html = html.replace('{{EXCERPT}}', excerpt)
    html = html.replace('{{CONTENT}}', article['content_html'])
    html = html.replace('{{DATE_ISO}}', date_str)
    html = html.replace('{{DATE_FR}}', date_fr)
    html = html.replace('{{ASSETS}}', assets_prefix_article)
    html = html.replace('{{ROOT}}', '../../')
    html = html.replace('{{PAGE_URL}}', page_url)
    html = html.replace('{{SHARE_TWITTER_URL}}', share_twitter_url)
    html = html.replace('{{SHARE_LINKEDIN_URL}}', share_linkedin_url)
    html = html.replace('{{OG_IMAGE}}', og_img_url)
    html = html.replace('{{META_KEYWORDS}}', _escape_html(keywords))
    html = html.replace('{{SCHEMA_JSON_LD}}', _schema_article(article))
    html = html.replace('{{PREV_NEXT}}', prev_next)
    html = html.replace('{{RECOMMENDATIONS}}', recommendations)
    html = html.replace('{{SERIES_HTML}}', series_html)

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
    for a in articles:
        date_str = a.get('date', '')[:10]
        try:
            dt = datetime.fromisoformat(a.get('date', ''))
            date_fr = dt.strftime('%d %B %Y')
        except Exception:
            date_fr = date_str
        excerpt = (a.get('excerpt') or '')[:160]
        type_label = _type_label(a)
        cards_html.append(f'''
        <a href="articles/{a['slug']}" class="article-card">
            <span class="article-type">{type_label}</span>
            <h2>{a['title']}</h2>
            <div class="article-meta">{date_fr}</div>
            <div class="article-excerpt">{excerpt}</div>
        </a>''')

    meta_desc = 'Blog DanielCraft : articles sur le développement web, TypeScript, GEO, SEO et bonnes pratiques.'
    page_url = f'{SITE_BASE}/blog'

    # Bloc "A découvrir" : 4 articles (un par serie ou derniers)
    rec_index_html = _recommendations_index_html(articles, collections)
    html = template.replace('{{RECOMMENDATIONS_INDEX}}', rec_index_html)
    html = html.replace('{{ARTICLES_GRID}}', '\n'.join(cards_html))
    html = html.replace('{{ARTICLES_JSON}}', articles_json)
    html = html.replace('{{COLLECTIONS_JSON}}', collections_json)
    html = html.replace('{{ASSETS}}', assets_prefix)
    html = html.replace('{{ROOT}}', '..')
    html = html.replace('{{META_DESCRIPTION}}', _escape_html(meta_desc))
    html = html.replace('{{META_KEYWORDS}}', 'développement web, TypeScript, GEO, SEO, tutoriels, bonnes pratiques')
    html = html.replace('{{PAGE_URL}}', page_url)
    html = html.replace('{{OG_IMAGE}}', OG_IMAGE_BLOG)
    html = html.replace('{{SCHEMA_JSON_LD}}', _schema_blog_index(articles))

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
            f'<a href="../articles/{a["slug"]}" class="article-card">'
            f'<span class="article-type">{type_label}</span>'
            f'<h2>{a["title"]}</h2>'
            f'<div class="article-meta">{date_fr}</div>'
            f'<div class="article-excerpt">{excerpt}</div>'
            f'</a>'
        )

    slug = collection.get('slug', collection.get('id', 'serie'))
    page_url = f'{SITE_BASE}/blog/series/{slug}'
    title = collection.get('title', 'Serie')
    desc = collection.get('description', '')
    keywords = ', '.join({tag for a in items for tag in a.get('tags', [])}) or 'blog, série'

    html = template.replace('{{TITLE}}', _escape_html(title))
    html = html.replace('{{DESCRIPTION}}', _escape_html(desc))
    html = html.replace('{{ARTICLES_GRID}}', '\n'.join(cards))
    html = html.replace('{{ASSETS}}', assets_prefix_series)
    html = html.replace('{{ROOT}}', '../..')
    html = html.replace('{{PAGE_URL}}', page_url)
    html = html.replace('{{OG_IMAGE}}', OG_IMAGE_BLOG)
    html = html.replace('{{META_KEYWORDS}}', _escape_html(keywords))
    html = html.replace('{{SCHEMA_JSON_LD}}', _schema_collection(collection, items))

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
            date_str = a.get('date', '')[:10]
            try:
                dt = datetime.fromisoformat(a.get('date', ''))
                date_fr = dt.strftime('%d %B %Y')
            except Exception:
                date_fr = date_str
            type_label = _type_label(a)
            excerpt = a.get('excerpt', '')
            cards.append(
                f'<a href="../articles/{a["slug"]}" class="article-card">'
                f'<span class="article-type">{type_label}</span>'
                f'<h2>{a["title"]}</h2>'
                f'<div class="article-meta">{date_fr}</div>'
                f'<div class="article-excerpt">{excerpt}</div>'
                f'</a>'
            )

        page_url = f'{SITE_BASE}/blog/types/{slug}'
        html = template.replace('{{TITLE}}', _escape_html(title))
        html = html.replace('{{DESCRIPTION}}', _escape_html(desc))
        html = html.replace('{{ARTICLES_GRID}}', '\n'.join(cards))
        html = html.replace('{{ASSETS}}', assets_prefix_types)
        html = html.replace('{{ROOT}}', '../..')
        html = html.replace('{{PAGE_URL}}', page_url)
        html = html.replace('{{OG_IMAGE}}', OG_IMAGE_BLOG)
        html = html.replace('{{META_KEYWORDS}}', _escape_html(f"{title}, blog, DanielCraft"))
        html = html.replace('{{SCHEMA_JSON_LD}}', '')  # optionnel: on pourrait generer un schema type

        out_file = output_dir / 'types' / f'{slug}.html'
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(html, encoding='utf-8')


def generate_sitemap_blog(articles: list[dict], collections: list[dict], output_dir: Path) -> None:
    """Genere sitemap-blog.xml pour le referencement (namespace et lastmod optimises)."""
    lastmod_blog = max((str(a.get('date', ''))[:10] for a in articles), default=datetime.now().strftime('%Y-%m-%d'))
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"',
        '        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 '
        'http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">',
        f'  <url><loc>{SITE_BASE}/blog</loc><lastmod>{lastmod_blog}</lastmod>'
        f'<changefreq>weekly</changefreq><priority>0.8</priority></url>',
    ]
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
