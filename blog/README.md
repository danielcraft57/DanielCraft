# Blog Automatique DanielCraft

Système de blog qui génère automatiquement des articles pour danielcraft.fr.

## Installation

### 1. Installer les dépendances Python

```bash
cd blog
pip3 install -r requirements.txt
```

### 2. Configuration de l'API (optionnel)

Pour générer des articles avec l'IA, tu peux utiliser OpenAI ou une autre API :

```bash
export OPENAI_API_KEY='ta-clé-api'
```

Si tu n'as pas de clé API, le script génère des articles exemple.

## Utilisation

### Générer un article manuellement

```bash
python3 generate_article.py "Le sujet de ton article"
```

Exemple :
```bash
python3 generate_article.py "Les meilleures pratiques en développement web"
```

### Générer un article quotidien automatiquement

```bash
python3 generate_daily.py
```

### Mettre à jour l'index du blog

```bash
python3 update_blog_index.py
```

## Automatisation avec Cron

Pour générer un article chaque jour automatiquement, ajoute cette ligne dans ton crontab :

```bash
crontab -e
```

Ajoute :
```
0 9 * * * cd /var/www/danielcraft.fr/blog && /usr/bin/python3 generate_daily.py >> /var/log/blog-generation.log 2>&1
```

Cela génère un article chaque jour à 9h.

## Structure des fichiers

```
blog/
├── articles/          # Articles générés (HTML + JSON)
│   ├── article-1.html
│   ├── article-1.json
│   └── list.json      # Liste de tous les articles (généré automatiquement)
├── generate_article.py    # Script principal de génération
├── generate_daily.py      # Script pour génération quotidienne
├── update_blog_index.py   # Met à jour l'index
├── article_template.html  # Template HTML pour les articles
├── blog.html             # Page qui liste tous les articles
└── requirements.txt      # Dépendances Python
```

## Intégration au site

1. Les articles sont générés dans `blog/articles/`
2. La page `blog.html` liste automatiquement tous les articles
3. Ajoute un lien vers le blog dans la navigation principale

## Personnalisation

### Modifier les sujets d'articles

Édite le fichier `generate_daily.py` et modifie la liste `TOPICS`.

### Changer le template

Modifie `article_template.html` pour personnaliser l'apparence des articles.

### Utiliser une autre API

Modifie la fonction `generate_article_content()` dans `generate_article.py` pour utiliser une autre API (Anthropic, etc.).

## Performance sur Raspberry Pi 3B+

Cette solution est optimisée pour un Raspberry Pi 3B+ :
- Génération d'articles en Python (léger)
- Fichiers statiques servis par nginx (pas de serveur à faire tourner)
- Pas de base de données (fichiers JSON simples)
- Consommation mémoire minimale

## Notes

- Les articles sont générés en HTML statique
- Pas besoin de serveur backend pour afficher les articles
- Le script peut tourner en arrière-plan via cron
- Compatible avec nginx existant















































































