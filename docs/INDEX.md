# Documentation - DanielCraft V6

Index de toute la documentation du projet.

## 📖 Documentation Générale

- **[CHANGELOG.md](./CHANGELOG.md)** - Historique des versions et changements
- **[README.md](../README.md)** - Documentation principale du projet

## 🏗️ Architecture et Build

- **[ARCHITECTURE.md](./ARCHITECTURE.md)** - Architecture du système de blocs réutilisables
- **[README_BUILD.md](./README_BUILD.md)** - Guide d'utilisation du système de build

## 🚀 Déploiement

- **[DEPLOYMENT.md](./DEPLOYMENT.md)** - Guide de déploiement (Bash/Linux)
- **[DEPLOYMENT-PS.md](./DEPLOYMENT-PS.md)** - Guide de déploiement (PowerShell/Windows)
- **[PERMISSIONS.md](./PERMISSIONS.md)** - Configuration des permissions
- **[troubleshooting.md](./troubleshooting.md)** - Dépannage des problèmes courants
- **[fix-ssl.md](./fix-ssl.md)** - Réparation des certificats SSL
- **[LOGS_ANALYSIS.md](./LOGS_ANALYSIS.md)** - Analyse des logs Nginx et solutions

## 🔍 SEO et Performance

- **[SEO_README.md](./SEO_README.md)** - Optimisation SEO et référencement
- **[GOOGLE_SETUP.md](./GOOGLE_SETUP.md)** - Configuration Google Analytics et Search Console
- **[PERFORMANCE.md](./PERFORMANCE.md)** - Optimisations de performance

## 🔧 Configuration Serveur

- **[../scripts/README_NGINX.md](../scripts/README_NGINX.md)** - Configuration Nginx

## 📝 Autres

- **[prompt_og_image.md](./prompt_og_image.md)** - Génération d'images Open Graph

## 📁 Structure du Projet

```
V6/
├── src/              # Sources (templates, includes, pages)
│   ├── includes/     # Composants réutilisables
│   ├── templates/   # Templates de base
│   └── pages/       # Contenu des pages
├── assets/           # Assets statiques (CSS, JS, images)
├── dist/             # Fichiers générés (ne pas éditer)
├── docs/             # Documentation (ce dossier)
├── scripts/          # Scripts de déploiement et config nginx
├── build.py          # Script de build Python
└── README.md
```

## 🎯 Quick Start

1. **Développement** : Éditer les fichiers dans `src/`
2. **Build** : `python3 build.py`
3. **Déploiement** : `.\scripts\deploy-content.ps1` (Windows) ou `./scripts/deploy-content.sh` (Linux)

## 📌 Version Actuelle

**Version 1.0.0** - Release majeure avec architecture modulaire complète, SEO optimisé, et système de build fonctionnel.

Voir [CHANGELOG.md](./CHANGELOG.md) pour les détails complets.

