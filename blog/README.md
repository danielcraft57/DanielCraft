# Blog DanielCraft

Blog integre au site : articles en Markdown, compilation en HTML, series (GEO, SEO, Marketing digital, Communication).

## Structure

- **content/articles/** : fichiers `.md` (front matter YAML + contenu)
- **content/collections/** : fichiers `.json` (series : geo-serie, seo-serie, marketing-digital-serie, communication-serie)
- **templates/** : article.html, blog_index.html, collection.html
- **build_blog.py** : compile le blog vers le dossier de sortie (ex. dist/blog)

## Utilisation

### Compilation seule

```bash
# Depuis la racine du projet
python blog/build_blog.py --output dist/blog
```

Le build principal (`python build.py`) appelle automatiquement le build du blog et genere ensuite les sitemaps.

### Contenu

- **Articles** : titre, date, excerpt, tags, series, og_image. Les schemas SVG sont dans `assets/images/blog/`.
- **Page index** : bloc "A decouvrir" (4 articles mis en avant) + grille "Tous les articles".
- **Page article** : lien precedent/suivant, bloc "Articles recommandes" (meme serie puis autres).
- **Menu "Plus"** : fonctionnel sur le blog grace au chargement de `main.js` dans les templates.

### Images OG

Les images de partage social (1200x630) sont dans `assets/images/og/`. Prompts dans `docs/prompt_og_images_articles_*.md`. Optimisation et generation WebP : `python scripts/optimize_images.py`.

## URLs generees

- Index : `/blog/` (fichier `blog/index.html`)
- Article : `/blog/articles/<slug>.html`
- Serie : `/blog/series/<slug>.html`
- Sitemap blog : `/blog/sitemap-blog.xml`

## Documentation

- **blog/GUIDE_DEMARRAGE.md** : guide de demarrage
- **docs/SEO_README.md** : SEO et sitemaps
- **assets/images/og/README.md** : liste des images OG attendues
