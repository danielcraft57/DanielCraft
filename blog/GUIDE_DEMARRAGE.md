# Guide de Démarrage Rapide - Blog Automatique

## Pourquoi cette solution ?

Pour un Raspberry Pi 3B+, j'ai choisi une approche **ultra-légère** :
- **Python** : léger, déjà installé sur la plupart des Pi
- **Fichiers statiques** : pas de base de données, pas de serveur backend
- **Génération à la demande** : les articles sont créés puis servis par nginx
- **Consommation minimale** : ~50-100 MB de RAM

## Installation en 5 minutes

### 1. Sur ton Raspberry Pi

```bash
# Se connecter au Pi
ssh pi@node12.lan

# Aller dans le dossier du blog
cd /var/www/danielcraft.fr/blog

# Installer les dépendances Python
pip3 install -r requirements.txt
```

### 2. Tester la génération d'un article

```bash
# Sans API (génère un article exemple)
python3 generate_article.py "Mon premier article de blog"

# Avec API OpenAI (si tu as une clé)
export OPENAI_API_KEY='ta-clé'
python3 generate_article.py "Les meilleures pratiques en développement web"
```

### 3. Mettre à jour l'index

```bash
python3 update_blog_index.py
```

### 4. Vérifier que ça marche

Ouvre `https://danielcraft.fr/blog/blog.html` dans ton navigateur.

## Automatisation quotidienne

Pour générer un article chaque jour automatiquement :

```bash
# Éditer le crontab
crontab -e

# Ajouter cette ligne (génère un article chaque jour à 9h)
0 9 * * * cd /var/www/danielcraft.fr/blog && /usr/bin/python3 generate_daily.py >> /var/log/blog-generation.log 2>&1
```

## Configuration de l'API (optionnel)

### Option 1 : OpenAI

1. Crée un compte sur [OpenAI](https://platform.openai.com)
2. Génère une clé API
3. Configure-la :

```bash
export OPENAI_API_KEY='sk-...'
# Ou ajoute dans ~/.bashrc pour que ça persiste
echo 'export OPENAI_API_KEY="sk-..."' >> ~/.bashrc
```

### Option 2 : Sans API

Le script fonctionne aussi sans API, mais génère des articles plus basiques (exemples).

## Personnalisation

### Changer les sujets d'articles

Édite `generate_daily.py` et modifie la liste `TOPICS` :

```python
TOPICS = [
    "Ton sujet 1",
    "Ton sujet 2",
    # ...
]
```

### Modifier le design

- **Page blog** : édite `blog.html`
- **Articles** : édite `article_template.html`

## Dépannage

### Les articles ne s'affichent pas

1. Vérifie que `update_blog_index.py` a été exécuté
2. Vérifie que le fichier `articles/list.json` existe
3. Vérifie les permissions : `chmod 644 articles/*.json`

### Erreur "Module not found"

```bash
pip3 install -r requirements.txt
```

### L'article ne se génère pas

Vérifie les logs :
```bash
tail -f /var/log/blog-generation.log
```

## Structure finale

```
/var/www/danielcraft.fr/
├── blog/
│   ├── articles/
│   │   ├── article-1.html
│   │   ├── article-1.json
│   │   └── list.json
│   ├── generate_article.py
│   ├── generate_daily.py
│   ├── update_blog_index.py
│   ├── blog.html
│   └── article_template.html
└── index.html (avec lien vers blog)
```

## Avantages de cette solution

✅ **Léger** : parfait pour Raspberry Pi 3B+  
✅ **Simple** : pas de base de données complexe  
✅ **Rapide** : fichiers statiques servis par nginx  
✅ **Automatique** : génération quotidienne possible  
✅ **Flexible** : facile à personnaliser  

## Prochaines étapes

1. Génère quelques articles de test
2. Configure le cron job pour l'automatisation
3. Personnalise les sujets selon tes besoins
4. Ajuste le design si besoin

Bon blogging !















































































