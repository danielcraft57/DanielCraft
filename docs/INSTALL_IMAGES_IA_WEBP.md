# Installer les images OG WebP (blog complet)

## Prerequis

- Les JPG `*-1200x630.jpg` generes via `docs/prompt_og_images_articles_all.md`
- Python 3 + Pillow : `pip install pillow`

## Etapes

1. Genere les prompts pour tout le blog :

```bash
python scripts/generate_all_blog_og_prompts.py
```

2. Genere les images avec les prompts (Flux, ChatGPT Images, Recraft, Midjourney...).
3. Place les JPG dans le dossier assets Cursor ou dans `assets/images/og/`.
4. Installe OG + WebP + bannieres inline :

```bash
python scripts/install_ai_generated_blog_og.py
python scripts/install_blog_article_banners.py
```

5. Rebuild : `python build.py` et `python blog/build_blog.py`

## Suivi

- Manifest : `scripts/_blog_og_manifest.json`
- Restants a generer : `scripts/_blog_og_remaining.json`

## Depannage

- Si le WebP manque, le site peut retomber sur le JPG selon le loader.
- Les fichiers sous `assets/images/og/` sont souvent gitignores : regenerer avant deploy.
