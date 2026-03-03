# DanielCraft V6 - Site Portfolio Freelance

Site web professionnel pour Loïc DANIEL, développeur Full-Stack TypeScript freelance avec plus de 7 ans d'expérience.

Site statique moderne avec système de build Python, optimisé pour le SEO, les performances et l'expérience utilisateur.

## Fonctionnalités

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
- **Meta tags** : Open Graph, Twitter Cards, Schema.org (Person, LocalBusiness, WebSite, BlogPosting)
- **Sitemaps** : Génération à chaque build (sitemap.xml index, sitemap-pages.xml, blog/sitemap-blog.xml)
- **URLs propres** : Sans extension .html (blog, projets, pages) avec redirections 301
- **Optimisations** : Preload, defer, DNS prefetch, compression

### Blog
- **Blog** (`/blog/`) : articles et tutoriels (GEO, SEO, Marketing digital, Communication)
- Contenu en Markdown (`blog/content/articles/`), build via `blog/build_blog.py`
- URLs sans .html : `/blog/articles/<slug>`, `/blog/series/<slug>`
- Séries : GEO, SEO, Marketing digital, Communication (classique et digitale)
- Page index avec bloc "À découvrir" et grille de tous les articles
- Pages article avec lien précédent/suivant et articles recommandés
- Google Analytics (GA4) sur toutes les pages blog
- Sitemap blog et JSON-LD optimisés (BlogPosting, BreadcrumbList, CollectionPage)

### Projets
- **Projets** (`/projets`, `/projets/<slug>`) : pages dédiées par projet, URLs sans .html et sans suffixe -l57
- Données depuis `src/data/projects.json` (généré par `scripts/build_projects_data.py`)
- README GitHub téléchargés et affichés en HTML sur chaque page projet
- Liens projet précédent/suivant et bloc "Projets suggérés" (même catégorie en priorité)

### Pages Disponibles
- Accueil avec sections complètes (Hero, Services, Portfolio, À Propos, Contact)
- Blog et articles
- Processus de travail
- Présentation Metz
- Portfolio de projets
- Statistiques
- Pages légales (Mentions légales, CGV, CGU, Politique de confidentialité)

## Structure du Projet

```
DanielCraftFr/
├── src/                    # Sources (templates, includes, pages)
├── assets/                 # CSS, JS, images (dont blog/, og/)
├── blog/                   # Blog (Markdown -> HTML)
│   ├── content/articles/   # Articles .md
│   ├── content/collections/# Séries (GEO, SEO, Marketing, Communication)
│   ├── templates/         # article.html, blog_index.html, collection.html
│   └── build_blog.py       # Compilation du blog
├── dist/                   # Fichiers générés (build + blog)
├── docs/                   # Documentation
├── scripts/                # Déploiement, nginx, optimize_images
├── build.py                # Build principal (pages + blog + sitemaps)
└── README.md
```

## Installation et Utilisation

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
python build.py
```

Génère les pages dans `dist/`, le blog dans `dist/blog/`, et les sitemaps (sitemap.xml, sitemap-pages.xml, blog/sitemap-blog.xml).

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

## Documentation

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

## Quick Start

1. **Modifier une page** : Éditer `src/pages/index.html` ou créer une nouvelle page
2. **Ajouter une variable** : Créer/modifier `src/pages/index.json`
3. **Build** : `python3 build.py`
4. **Déployer** : `.\scripts\deploy-content.ps1` (Windows) ou `./scripts/deploy-content.sh` (Linux)

## Configuration

### Variables d'Environnement
Les scripts de déploiement utilisent des variables d'exemple par défaut :
- **Domaine** : `votre-domaine.fr`
- **Utilisateur SSH** : `deploy`
- **Serveur** : `serveur.local`
- **Chemin serveur** : `/var/www/votre-domaine.fr`

Adapte ces valeurs à ton propre environnement (domaine, serveur, chemin) ou surcharge-les via les variables d'environnement documentées dans les scripts.

### Nginx
La configuration Nginx est dans `scripts/nginx.conf`. Elle inclut :
- Compression Gzip
- Cache des assets
- URLs propres (sans .html)
- Redirections 301
- Blocage des requêtes suspectes
- SSL/TLS

## Technologies

- **Frontend** : HTML5, CSS3, JavaScript (ES6+)
- **Build** : Python 3
- **Fonts** : Inter, JetBrains Mono (Google Fonts)
- **Icons** : Font Awesome 6.5.0
- **Analytics** : Google Analytics 4
- **Server** : Nginx
- **Déploiement** : rsync (avec timeout/keepalive), fallback scp si rsync échoue ; blog inclus dans `dist/blog/`

## License

© 2025 Loïc DANIEL - Tous droits réservés

## Auteur

**Loïc DANIEL**
- Email : loic5488@gmail.com
- Téléphone : 03 87 78 09 16
- Localisation : 57000 Metz, France
- LinkedIn : [linkedin.com/in/loicdaniel](https://linkedin.com/in/loicdaniel)
- GitHub : [github.com/likedevGit](https://github.com/likedevGit)

## Version

Voir [CHANGELOG.md](docs/CHANGELOG.md) pour l'historique. Version 1.0.0 : première release stable avec
- Architecture modulaire complète
- Système de build fonctionnel
- SEO et performance optimisés
- Navigation et footer améliorés
- Documentation complète
