# Blog DanielCraft - Guide pour l'IA (Cursor)

Ce document explique comment creer des articles et tutoriels pour le blog. L'IA peut ecrire directement des fichiers Markdown.

## Structure des dossiers

```
blog/
├── content/                 # SOURCES - C'est ici que l'IA ecrit
│   ├── articles/           # Articles classiques (.md)
│   ├── tutorials/          # Tutoriels et series (.md)
│   └── collections/        # Listes/Series (.json)
├── templates/              # Templates HTML (a ne pas modifier sauf besoin)
├── build_blog.py           # Compile content/ -> dist/blog/
└── README_IA.md           # Ce fichier
```

## Creer un article

1. Cree un fichier `.md` dans `content/articles/`
2. Nom du fichier = slug de l'URL (ex: `mon-super-article.md` -> `/blog/articles/mon-super-article.html`)
3. Format avec front matter YAML :

```markdown
---
title: "Titre de l'article"
date: 2026-02-21
excerpt: "Resume court en 2-3 phrases pour les meta et les cartes."
type: article
tags: [tag1, tag2, tag3]
---

# Introduction

Le contenu ici. Markdown standard : **gras**, *italique*, listes, code, etc.

## Section

Du texte...

```javascript
const code = "exemple";
```
```

## Creer un tutoriel (serie)

1. Cree des fichiers dans `content/tutorials/`
2. Utilise `type: tutorial` et `series` + `series_order` pour les numeroter :

```markdown
---
title: "Mon tutoriel - Partie 2"
date: 2026-02-21
excerpt: "Deuxieme volet de la serie."
type: tutorial
series: mon-tutoriel
series_order: 2
tags: [tutoriel, sujet]
---

Contenu...
```

## Creer une collection / serie

Un fichier JSON dans `content/collections/` regroupe des articles par slug :

```json
{
  "id": "ma-serie",
  "title": "Titre de la serie",
  "description": "Description courte.",
  "slug": "ma-serie",
  "articles": [
    "slug-article-1",
    "slug-article-2",
    "slug-article-3"
  ]
}
```

L'ordre des slugs dans `articles` definit l'ordre d'affichage.

## Build

Apres avoir cree ou modifie du contenu :

```bash
# Depuis la racine DanielCraftFr
python blog/build_blog.py --output dist/blog

# Ou via le build complet
python build.py
```

Le build principal (`build.py`) appelle automatiquement le build du blog.

## Champs du front matter

| Champ | Obligatoire | Description |
|-------|-------------|-------------|
| title | Oui | Titre de l'article |
| date | Non (defaut: aujourd'hui) | Format YYYY-MM-DD |
| excerpt | Recommande | Resume pour SEO et cartes |
| type | Non (defaut: article) | `article` ou `tutorial` |
| tags | Non | Liste de mots-cles |
| series | Non | ID de la serie (pour tutoriels) |
| series_order | Non | Numero dans la serie |
| slug | Non | Override du slug (sinon = nom du fichier) |

## Exemples fournis

- `content/articles/exemple-article.md` - Modele d'article
- `content/tutorials/intro-typescript-01.md` - Modele de tutoriel
- `content/collections/geo-serie.json` - Exemple de collection

## SEO, GEO et RDF

Le build genere automatiquement :
- Meta tags complets (canonical, keywords, author, robots)
- Open Graph et Twitter Cards
- JSON-LD schema.org : BlogPosting (articles), Blog (index), BreadcrumbList, CollectionPage (series)
- Sitemap `sitemap-blog.xml` pour Google et moteurs generatifs

Pour le GEO : le contenu est dans le HTML initial (pas de chargement JS), structure semantique (h1, article, itemprop), auteur et publisher explicites.

Image OG recommandee : `assets/images/og/blog-1200x630.jpg` (1200x630px).

## Bonnes pratiques

1. **Excerpt** : 120-160 caracteres pour un bon affichage
2. **Slug** : lowercase, tirets, pas d'accents
3. **Tags** : 3-5 tags pertinents
4. **Structure** : H2 pour les sections principales, H3 pour les sous-sections
