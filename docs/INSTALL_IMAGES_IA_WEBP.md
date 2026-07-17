# Installer les images OG WebP (serie IA pratique)

## Prerequis

- Les JPG `*-1200x630.jpg` generes via `docs/prompt_og_images_articles_ia_pratique.md`
- Python 3 + Pillow : `pip install pillow`

## Etapes

1. Genere les images avec les prompts du fichier ci-dessus (Flux, ChatGPT Images, Recraft, Midjourney...).
2. Copie tous les JPG dans `assets/images/og/` (noms exacts : `slug-1200x630.jpg`).
3. Execute :

```bash
python scripts/install_ia_og_webp.py
```

Le script :
- trouve les JPG listes dans le fichier prompts (ou tous les `ia-*-1200x630.jpg`)
- cree le `.webp` a cote (qualite 82)
- recentre au ratio 1200/630 et redimensionne en 1200x630

4. Verifie qu'un article pointe bien `og_image: slug-1200x630.jpg` dans le frontmatter.
5. Rebuild : `python build.py` (ou `python blog/build_blog.py`)

## Depannage

- Si le WebP manque, le site peut retomber sur le JPG selon le loader.
- Les fichiers sous `assets/images/og/` sont souvent gitignores : regenerer avant deploy.
- Pour regenerer les articles depuis les transcripts :

```bash
python scripts/generate_ia_articles_from_transcripts.py
```
