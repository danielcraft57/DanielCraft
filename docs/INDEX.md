# Documentation - DanielCraft V6

Index de toute la documentation du projet.

## Documentation generale

- **[CHANGELOG.md](./CHANGELOG.md)** - Historique des versions et changements
- **[README.md](../README.md)** - Documentation principale du projet

## Architecture et build

- **[ARCHITECTURE.md](./ARCHITECTURE.md)** - Architecture du système de blocs réutilisables
- **[README_BUILD.md](./README_BUILD.md)** - Guide d'utilisation du système de build
- **[VITRINES.md](./VITRINES.md)** - Catalogue vitrines HTML (ancre `#vitrines`, build, captures, déploiement)

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
- **[ECO_CONCEPTION_PRESTATIONS.md](./ECO_CONCEPTION_PRESTATIONS.md)** - Positionnement éco-conception et nouvelles prestations proposées

## Configuration serveur

- **[../scripts/README_NGINX.md](../scripts/README_NGINX.md)** - Configuration Nginx

## Blog

- **[../blog/README.md](../blog/README.md)** - Blog : structure, build, series
- **[../blog/GUIDE_DEMARRAGE.md](../blog/GUIDE_DEMARRAGE.md)** - Guide de demarrage blog

## UX et parcours utilisateur

- **[ux-user-flow.md](./ux-user-flow.md)** - Parcours devis → appel → livraison
- **[ux-screenshots/README.md](./ux-screenshots/README.md)** - Matrice QA visuelle (captures locales)
- **[charte-visuelle-bd.md](./charte-visuelle-bd.md)** - Charte BD cartoon (OG, réseaux)

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

**Version 1.3.0** - Vitrines : hub, démos sous `assets/vitrines/demos/`, captures, déploiement `dist/vitrines/`, doc VITRINES et ignore captures. Voir le CHANGELOG pour le détail.

Voir [CHANGELOG.md](./CHANGELOG.md) pour les details complets.

