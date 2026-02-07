# Guide d'Utilisation du Système de Build

## Vue d'ensemble

Le site utilise maintenant un système de templates et blocs réutilisables pour éviter la duplication de code et faciliter la maintenance.

## Structure

```
V6/
├── src/                      # Sources (à éditer)
│   ├── includes/            # Blocs réutilisables
│   ├── templates/           # Templates de base
│   └── pages/               # Contenu des pages
├── assets/                   # Assets statiques
├── build.py                  # Script de build
└── *.html                    # Pages générées (ne pas éditer)
```

## Commandes

### Build toutes les pages

```bash
python3 build.py
```

### Build une page spécifique

```bash
python3 build.py index
python3 build.py processus
```

### Mode watch (rebuild automatique)

```bash
python3 build.py --watch
```

## Workflow

1. **Éditer les sources** dans `src/`
2. **Builder** avec `python3 build.py`
3. **Tester** les pages générées
4. **Déployer** avec `deploy-content.ps1`

## Syntaxe des Templates

### Variables

```html
{{page_title}}
{{page_description}}
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

{% if blog_enabled %}
    <!-- Contenu si blog_enabled est true -->
{% endif %}
```

## Configuration d'une Page

Chaque page a un fichier JSON dans `src/pages/` :

```json
{
  "page_title": "Titre",
  "page_description": "Description",
  "page_url": "https://danielcraft.fr/page",
  "current_page": "page",
  "page_scripts": ["main.js", "autre.js"]
}
```

## Important

⚠️ **Ne jamais éditer directement** les fichiers HTML dans le dossier racine  
✅ **Toujours éditer** les fichiers dans `src/` puis rebuilder

