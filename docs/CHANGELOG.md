# Changelog - DanielCraft V6

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

## [1.0.0] - 2025-01-XX

### 🎉 Version Initiale - Release Majeure

#### ✨ Fonctionnalités Principales

**Système de Build et Architecture**
- Système de génération statique avec Python (`build.py`)
- Architecture modulaire avec templates réutilisables (`src/templates/base.html`)
- Système d'includes pour composants réutilisables (head, nav, footer, scripts, schema)
- Support des variables et conditions dans les templates (`{% if %}`, `{% else %}`, `{% endif %}`)
- Génération automatique de `favicon.ico` depuis `favicon.svg`
- Build dans le dossier `dist/` pour séparation claire source/production

**Navigation et Interface**
- Navbar responsive avec menu hamburger mobile
- Menu déroulant "Plus" pour regrouper les pages secondaires (Processus, Metz, Projets, Statistiques)
- Navigation intelligente avec liens principaux toujours visibles
- Système de navigation active avec highlight automatique
- Bouton CTA "Devis gratuit" dans la navbar

**Footer Amélioré**
- Structure en 4 colonnes (Brand, Navigation, Pages, Contact)
- Section brand avec logo, description et réseaux sociaux
- Liens de contact avec icônes (email, téléphone, adresse)
- Footer bottom avec copyright et liens légaux organisés
- Design responsive et ergonomique

**SEO et Référencement**
- Intégration Google Analytics (GA4) avec ID `G-4VN3CKFP14`
- Vérification Google Search Console via DNS TXT record
- Meta tags complets (Open Graph, Twitter Cards)
- Schema.org JSON-LD pour données structurées
- Sitemap.xml avec URLs propres (sans .html)
- Robots.txt optimisé
- URLs propres (sans extension .html) avec redirections 301

**Performance**
- Optimisation des polices (Inter, JetBrains Mono) avec subset et display=swap
- Preload des ressources critiques (CSS, fonts)
- Defer pour scripts non-critiques
- DNS prefetch pour Google Fonts et Font Awesome
- Configuration Nginx optimisée :
  - Compression Gzip niveau 6
  - Cache des assets statiques (1 an immutable)
  - Cache HTML (1 heure revalidate)
  - HTTP/2 activé

**Sécurité et Logs**
- Blocage des requêtes suspectes dans Nginx (bots malveillants)
- Redirection `/favicon.ico` vers `/assets/icons/favicon.svg`
- Gestion des erreurs SSL handshake (bots avec TLS obsolète)
- Configuration SSL/TLS sécurisée

**Déploiement**
- Scripts PowerShell (`deploy.ps1`, `deploy-content.ps1`) pour Windows
- Scripts Bash (`deploy.sh`, `deploy-content.sh`) pour Linux/Mac
- Intégration du build Python dans les scripts de déploiement
- Déploiement automatique depuis `dist/` vers le serveur
- Configuration Nginx centralisée dans `scripts/nginx.conf`
- Support rsync et scp avec gestion des permissions

**Pages Disponibles**
- Page d'accueil (`/`) avec sections : Hero, Services, Portfolio, À Propos, Contact
- Page Processus (`/processus`)
- Page Metz (`/metz`)
- Page Portfolio (`/portfolio`)
- Page Projets (`/projets`)
- Page Statistiques (`/statistiques`)
- Pages légales :
  - Mentions légales (`/mentions-legales`)
  - CGV (`/cgv`)
  - CGU (`/cgu`)
  - Politique de confidentialité (`/politique-confidentialite`)

**Documentation**
- Documentation complète dans `docs/`
- Guide d'architecture et de build
- Guides de déploiement (Windows et Linux)
- Documentation SEO et performance
- Guide de configuration Google Analytics
- Analyse des logs et troubleshooting
- Index de documentation (`docs/INDEX.md`)

#### 🐛 Corrections de Bugs

- Correction du système de conditions `{% else %}` dans le moteur de template
- Suppression des erreurs d'affichage liées aux conditions non traitées
- Correction des erreurs Unicode dans `build.py` (Windows)
- Gestion des erreurs de permissions Windows lors du build
- Correction des erreurs de favicon (404) dans les logs Nginx
- Blocage des requêtes suspectes pour éviter le spam dans les logs

#### 🔧 Améliorations Techniques

- Refactorisation du code JavaScript (suppression de duplication)
- Amélioration de l'accessibilité (ARIA labels, rôles)
- Optimisation du CSS avec variables personnalisées
- Responsive design amélioré pour mobile et tablette
- Amélioration de l'ergonomie du footer et de la navbar

#### 📝 Structure du Projet

```
V6/
├── src/                    # Sources
│   ├── includes/           # Composants réutilisables
│   │   ├── head.html
│   │   ├── nav.html
│   │   ├── footer.html
│   │   ├── scripts.html
│   │   └── schema.html
│   ├── templates/          # Templates de base
│   │   └── base.html
│   └── pages/             # Contenu des pages
│       ├── index.html
│       └── index.json
├── assets/                # Assets statiques
│   ├── css/
│   ├── js/
│   ├── images/
│   └── icons/
├── dist/                   # Fichiers générés (build)
├── docs/                   # Documentation
├── scripts/                # Scripts de déploiement
│   ├── deploy.ps1
│   ├── deploy.sh
│   └── nginx.conf
├── build.py               # Script de build
└── README.md
```

#### 🚀 Technologies Utilisées

- **Frontend** : HTML5, CSS3, JavaScript (ES6+)
- **Build** : Python 3 (système de génération statique)
- **Fonts** : Inter, JetBrains Mono (Google Fonts)
- **Icons** : Font Awesome 6.5.0
- **Analytics** : Google Analytics 4
- **Server** : Nginx avec SSL/TLS
- **Déploiement** : rsync, scp

---

## Format du Changelog

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

[1.0.0]: https://github.com/likedevGit/DanielCraft/releases/tag/v1.0.0

