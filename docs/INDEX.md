# Documentation - DanielCraft V6

Index de toute la documentation du projet.

## Documentation generale

- **[CHANGELOG.md](./CHANGELOG.md)** - Historique des versions et changements
- **[README.md](../README.md)** - Documentation principale du projet

## Architecture et build

- **[ARCHITECTURE.md](./ARCHITECTURE.md)** - Architecture du système de blocs réutilisables
- **[README_BUILD.md](./README_BUILD.md)** - Guide d'utilisation du système de build

## Deploiement

- **[DEPLOYMENT.md](./DEPLOYMENT.md)** - Guide de déploiement (Bash/Linux)
- **[DEPLOYMENT-PS.md](./DEPLOYMENT-PS.md)** - Guide de déploiement (PowerShell/Windows)
- **[PERMISSIONS.md](./PERMISSIONS.md)** - Configuration des permissions
- **[troubleshooting.md](./troubleshooting.md)** - Dépannage des problèmes courants
- **[fix-ssl.md](./fix-ssl.md)** - Réparation des certificats SSL
- **[LOGS_ANALYSIS.md](./LOGS_ANALYSIS.md)** - Analyse des logs Nginx et solutions

## SEO et performance

- **[SEO_README.md](./SEO_README.md)** - Optimisation SEO et référencement
- **[GOOGLE_SETUP.md](./GOOGLE_SETUP.md)** - Configuration Google Analytics et Search Console
- **[PERFORMANCE.md](./PERFORMANCE.md)** - Optimisations de performance

## Configuration serveur

- **[../scripts/README_NGINX.md](../scripts/README_NGINX.md)** - Configuration Nginx

## Blog

- **[../blog/README.md](../blog/README.md)** - Blog : structure, build, series
- **[../blog/GUIDE_DEMARRAGE.md](../blog/GUIDE_DEMARRAGE.md)** - Guide de demarrage blog

## Images et visuels

- **[prompt_og_image.md](./prompt_og_image.md)** - Images Open Graph (pages principales)
- **[prompt_og_images_articles_geo.md](./prompt_og_images_articles_geo.md)** - Images OG articles GEO
- **[prompt_og_images_articles_seo.md](./prompt_og_images_articles_seo.md)** - Images OG articles SEO
- **[prompt_og_images_articles_marketing_digital.md](./prompt_og_images_articles_marketing_digital.md)** - Images OG articles Marketing

## Structure du projet

```
DanielCraftFr/
├── src/              # Sources (templates, includes, pages)
├── assets/           # CSS, JS, images (blog/, og/)
├── blog/             # Blog Markdown (content/, templates/, build_blog.py)
├── dist/             # Fichiers generes (build + blog)
├── docs/             # Documentation (ce dossier)
├── scripts/          # Deploiement, nginx, optimize_images
├── build.py          # Build principal (pages, blog, sitemaps)
└── README.md
```

## Quick Start

1. **Développement** : Éditer les fichiers dans `src/`
2. **Build** : `python3 build.py`
3. **Déploiement** : `.\scripts\deploy-content.ps1` (Windows) ou `./scripts/deploy-content.sh` (Linux)

## Version actuelle

**Version 1.2.0** - Projets sans -l57, prev/next et suggestions, README GitHub sur pages projet. Blog : liens sans .html, GA4 partout. Doc et menage.

Voir [CHANGELOG.md](./CHANGELOG.md) pour les details complets.

