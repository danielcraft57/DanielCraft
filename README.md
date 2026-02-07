# DanielCraft V6 - Site Portfolio Freelance

Site web professionnel pour Loïc DANIEL, développeur Full-Stack TypeScript freelance avec plus de 7 ans d'expérience.

## 🚀 Version 1.0.0

Site statique moderne avec système de build Python, optimisé pour le SEO, les performances et l'expérience utilisateur.

## ✨ Fonctionnalités

### Architecture Modulaire
- **Système de build** : Génération statique avec Python
- **Templates réutilisables** : Architecture modulaire avec includes
- **Variables et conditions** : Support complet dans les templates
- **Build optimisé** : Génération dans `dist/` pour production

### Navigation Intelligente
- **Navbar responsive** : Menu hamburger pour mobile
- **Menu déroulant "Plus"** : Regroupe les pages secondaires
- **Navigation active** : Highlight automatique de la page courante
- **CTA visible** : Bouton "Devis gratuit" toujours accessible

### SEO et Performance
- **Google Analytics** : Intégration GA4 complète
- **Google Search Console** : Vérification DNS configurée
- **Meta tags** : Open Graph, Twitter Cards, Schema.org
- **URLs propres** : Sans extension .html avec redirections 301
- **Optimisations** : Preload, defer, DNS prefetch, compression

### Pages Disponibles
- Accueil avec sections complètes (Hero, Services, Portfolio, À Propos, Contact)
- Processus de travail
- Présentation Metz
- Portfolio de projets
- Statistiques
- Pages légales (Mentions légales, CGV, CGU, Politique de confidentialité)

## 📁 Structure du Projet

```
V6/
├── src/                    # Sources
│   ├── includes/           # Composants réutilisables
│   ├── templates/          # Templates de base
│   └── pages/             # Contenu des pages
├── assets/                # Assets statiques (CSS, JS, images)
├── dist/                   # Fichiers générés (ne pas éditer)
├── docs/                   # Documentation complète
├── scripts/                # Scripts de déploiement et config Nginx
├── build.py               # Script de build Python
└── README.md
```

## 🛠️ Installation et Utilisation

### Prérequis
- Python 3.7+
- Accès SSH au serveur de production (pour déploiement)

### Développement Local

1. **Cloner le projet** (si applicable)
```bash
git clone <repository-url>
cd V6
```

2. **Éditer les sources**
   - Modifier les fichiers dans `src/` (templates, includes, pages)
   - Modifier les assets dans `assets/` (CSS, JS, images)

3. **Build le projet**
```bash
python3 build.py
```

Les fichiers générés sont dans `dist/`.

4. **Tester localement**
```bash
# Ouvrir dist/index.html dans un navigateur
# Ou utiliser un serveur local :
python3 -m http.server 8000 -d dist
```

### Déploiement

#### Windows (PowerShell)
```powershell
# Déploiement complet (build + déploiement)
.\scripts\deploy.ps1

# Déploiement du contenu uniquement (si build déjà fait)
.\scripts\deploy-content.ps1
```

#### Linux/Mac (Bash)
```bash
# Déploiement complet
./scripts/deploy.sh

# Déploiement du contenu uniquement
./scripts/deploy-content.sh
```

## 📚 Documentation

Toute la documentation est disponible dans le dossier `docs/` :

- **[INDEX.md](docs/INDEX.md)** - Index de toute la documentation
- **[ARCHITECTURE.md](docs/ARCHITECTURE.md)** - Architecture du système de build
- **[README_BUILD.md](docs/README_BUILD.md)** - Guide d'utilisation du build
- **[DEPLOYMENT-PS.md](docs/DEPLOYMENT-PS.md)** - Guide de déploiement Windows
- **[DEPLOYMENT.md](docs/DEPLOYMENT.md)** - Guide de déploiement Linux
- **[SEO_README.md](docs/SEO_README.md)** - Optimisation SEO
- **[GOOGLE_SETUP.md](docs/GOOGLE_SETUP.md)** - Configuration Google Analytics
- **[PERFORMANCE.md](docs/PERFORMANCE.md)** - Optimisations de performance
- **[CHANGELOG.md](docs/CHANGELOG.md)** - Historique des versions

## 🎯 Quick Start

1. **Modifier une page** : Éditer `src/pages/index.html` ou créer une nouvelle page
2. **Ajouter une variable** : Créer/modifier `src/pages/index.json`
3. **Build** : `python3 build.py`
4. **Déployer** : `.\scripts\deploy-content.ps1` (Windows) ou `./scripts/deploy-content.sh` (Linux)

## 🔧 Configuration

### Variables d'Environnement
Les scripts de déploiement utilisent des variables par défaut :
- **Domaine** : `danielcraft.fr`
- **Utilisateur SSH** : `pi`
- **Serveur** : `node12.lan`
- **Chemin serveur** : `/var/www/danielcraft.fr`

Modifier les scripts si nécessaire.

### Nginx
La configuration Nginx est dans `scripts/nginx.conf`. Elle inclut :
- Compression Gzip
- Cache des assets
- URLs propres (sans .html)
- Redirections 301
- Blocage des requêtes suspectes
- SSL/TLS

## 🚀 Technologies

- **Frontend** : HTML5, CSS3, JavaScript (ES6+)
- **Build** : Python 3
- **Fonts** : Inter, JetBrains Mono (Google Fonts)
- **Icons** : Font Awesome 6.5.0
- **Analytics** : Google Analytics 4
- **Server** : Nginx
- **Déploiement** : rsync, scp

## 📝 License

© 2025 Loïc DANIEL - Tous droits réservés

## 👤 Auteur

**Loïc DANIEL**
- Email : loic5488@gmail.com
- Téléphone : 03 87 78 09 16
- Localisation : 57000 Metz, France
- LinkedIn : [linkedin.com/in/loicdaniel](https://linkedin.com/in/loicdaniel)
- GitHub : [github.com/likedevGit](https://github.com/likedevGit)

## 🎉 Version 1.0.0

Cette version marque la première release stable du site avec :
- Architecture modulaire complète
- Système de build fonctionnel
- SEO et performance optimisés
- Navigation et footer améliorés
- Documentation complète

Voir [CHANGELOG.md](docs/CHANGELOG.md) pour plus de détails.
