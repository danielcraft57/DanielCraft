# Architecture du Site - Système de Blocs Réutilisables

Ce document explique la nouvelle architecture modulaire du site avec système de templates et blocs réutilisables.

## Structure des Dossiers

```
V6/
├── src/                      # Sources (templates, includes, pages)
│   ├── includes/            # Blocs réutilisables
│   │   ├── head.html        # En-tête HTML (meta, fonts, CSS, GA)
│   │   ├── nav.html         # Navigation
│   │   ├── footer.html      # Pied de page
│   │   ├── scripts.html     # Scripts JavaScript
│   │   └── schema.html       # Schema.org JSON-LD
│   ├── templates/           # Templates de base
│   │   └── base.html        # Template principal
│   └── pages/               # Contenu des pages
│       ├── index.html       # Contenu de la page d'accueil
│       ├── index.json       # Config de la page d'accueil
│       ├── processus.html
│       ├── processus.json
│       └── ...
├── assets/                   # Assets statiques (CSS, JS, images)
├── build.py                  # Script de build Python
├── index.html                # Pages générées (à ne pas éditer manuellement)
├── processus.html
└── ...
```

## Principe de Fonctionnement

1. **Sources** : Les fichiers sources sont dans `src/`
   - `src/includes/` : Blocs réutilisables (head, nav, footer, etc.)
   - `src/templates/` : Templates de base
   - `src/pages/` : Contenu spécifique de chaque page

2. **Build** : Le script `build.py` génère les pages finales
   - Lit les templates et includes
   - Remplace les variables
   - Génère les fichiers HTML finaux dans le dossier racine

3. **Déploiement** : Les fichiers générés sont déployés sur le serveur

## Syntaxe des Templates

### Variables

```html
{{page_title}}          <!-- Remplace par la valeur de page_title -->
{{page_description}}    <!-- Remplace par la valeur de page_description -->
```

### Includes

```html
{% include "includes/head.html" %}
{% include "includes/nav.html" %}
```

### Conditions

```html
{% if current_page == 'index' %}
    <!-- Contenu si current_page vaut 'index' -->
{% endif %}
```

## Configuration d'une Page

Chaque page a un fichier JSON de configuration dans `src/pages/` :

```json
{
  "page_title": "Titre de la page",
  "page_description": "Description de la page",
  "page_keywords": "mot-clé1, mot-clé2",
  "page_url": "https://danielcraft.fr/ma-page",
  "current_page": "ma-page",
  "page_scripts": ["main.js", "autre-script.js"],
  "extra_css": "stats.css",
  "schema_type": "home"
}
```

## Utilisation

### Build Toutes les Pages

```bash
python3 build.py
```

### Build une Page Spécifique

```bash
python3 build.py index
```

### Mode Watch (rebuild automatique)

```bash
python3 build.py --watch
```

## Avantages

✅ **DRY (Don't Repeat Yourself)** : Plus de duplication de code  
✅ **Maintenance facile** : Modifier une fois, appliqué partout  
✅ **Cohérence** : Toutes les pages ont la même structure  
✅ **Flexibilité** : Variables pour personnaliser chaque page  
✅ **Prêt pour le blog** : Structure extensible pour ajouter un blog facilement  
✅ **Performance** : Pages statiques générées, pas de traitement serveur  

## Migration des Pages Existantes

Pour migrer une page existante :

1. Créer `src/pages/nom-page.html` avec uniquement le contenu (sans head, nav, footer)
2. Créer `src/pages/nom-page.json` avec la configuration
3. Lancer `python3 build.py nom-page`
4. Vérifier le résultat

## Préparation pour le Blog

La structure est prête pour intégrer un blog :

- Le système de templates permet de créer facilement des pages de blog
- Les includes peuvent être réutilisés pour les articles
- Le build peut être étendu pour générer automatiquement les pages d'articles

## Workflow Recommandé

1. **Développement** : Éditer les fichiers dans `src/`
2. **Build** : Lancer `python3 build.py` pour générer les pages
3. **Test** : Vérifier les pages générées localement
4. **Déploiement** : Utiliser `deploy-content.ps1` ou `deploy-content.sh`

## Notes Importantes

⚠️ **Ne pas éditer directement** les fichiers HTML dans le dossier racine (index.html, processus.html, etc.)  
✅ **Toujours éditer** les fichiers dans `src/` puis rebuilder  
✅ **Versionner** le dossier `src/` dans Git  
✅ **Ignorer** les fichiers générés dans `.gitignore` si nécessaire

