#!/usr/bin/env python3
"""
Script pour générer automatiquement des articles de blog
Utilise l'API OpenAI (ou autre) pour créer du contenu
"""

import os
import json
import requests
from datetime import datetime
from pathlib import Path
import hashlib
import re

# Configuration
CONFIG = {
    'api_key': os.getenv('OPENAI_API_KEY', ''),
    'api_url': 'https://api.openai.com/v1/chat/completions',
    'model': 'gpt-4o-mini',  # Modèle léger et économique
    'blog_dir': Path(__file__).parent,
    'articles_dir': Path(__file__).parent / 'articles',
    'template_file': Path(__file__).parent / 'article_template.html'
}

def slugify(text):
    """Convertit un texte en slug pour l'URL"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def generate_article_content(topic, api_key=None):
    """
    Génère le contenu d'un article via l'API OpenAI
    Tu peux aussi utiliser d'autres APIs (Anthropic, etc.)
    """
    if not api_key:
        # Mode démo - génère un article exemple
        return {
            'title': topic,
            'content': f"""
<h2>Introduction</h2>
<p>Cet article traite de {topic}. C'est un sujet passionnant qui mérite d'être exploré en profondeur.</p>

<h2>Les points clés</h2>
<p>Voici les éléments essentiels à retenir sur {topic} :</p>
<ul>
    <li>Point important numéro 1</li>
    <li>Point important numéro 2</li>
    <li>Point important numéro 3</li>
</ul>

<h2>Conclusion</h2>
<p>En conclusion, {topic} est un domaine riche et varié qui offre de nombreuses opportunités.</p>
""",
            'excerpt': f"Un article complet sur {topic} pour approfondir vos connaissances."
        }
    
    # Appel à l'API OpenAI
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    prompt = f"""Écris un article de blog complet et professionnel en français sur le sujet : {topic}

L'article doit :
- Faire environ 800-1000 mots
- Être bien structuré avec des titres H2
- Être informatif et utile
- Avoir un ton professionnel mais accessible
- Inclure une introduction et une conclusion

Format de réponse en JSON :
{{
    "title": "Titre de l'article",
    "content": "Contenu HTML avec balises <h2>, <p>, <ul>, etc.",
    "excerpt": "Résumé court de 2-3 phrases"
}}"""

    data = {
        'model': CONFIG['model'],
        'messages': [
            {'role': 'system', 'content': 'Tu es un expert en rédaction de contenu web professionnel.'},
            {'role': 'user', 'content': prompt}
        ],
        'temperature': 0.7,
        'max_tokens': 2000
    }
    
    try:
        response = requests.post(CONFIG['api_url'], headers=headers, json=data, timeout=30)
        response.raise_for_status()
        
        result = response.json()
        content = result['choices'][0]['message']['content']
        
        # Parser le JSON de la réponse
        # Parfois l'API retourne du markdown avec ```json, on nettoie ça
        if '```json' in content:
            content = content.split('```json')[1].split('```')[0].strip()
        elif '```' in content:
            content = content.split('```')[1].split('```')[0].strip()
        
        article_data = json.loads(content)
        return article_data
        
    except Exception as e:
        print(f"Erreur lors de la génération : {e}")
        # Retourne un article exemple en cas d'erreur
        return generate_article_content(topic, api_key=None)

def load_template():
    """Charge le template HTML pour un article"""
    if CONFIG['template_file'].exists():
        return CONFIG['template_file'].read_text(encoding='utf-8')
    
    # Template par défaut
    return """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}} | Blog DanielCraft</title>
    <meta name="description" content="{{EXCERPT}}">
    <link rel="stylesheet" href="../assets/css/main.css">
    <link rel="stylesheet" href="../assets/css/responsive.css">
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <div class="nav-logo">
                <a href="../index.html" class="logo-link">
                    <span class="logo-name">DanielCraft</span>
                </a>
            </div>
            <div class="nav-menu">
                <a href="../index.html" class="nav-link">Accueil</a>
                <a href="blog.html" class="nav-link">Blog</a>
            </div>
        </div>
    </nav>
    
    <main class="blog-article">
        <article>
            <header>
                <h1>{{TITLE}}</h1>
                <div class="article-meta">
                    <time datetime="{{DATE_ISO}}">{{DATE_FR}}</time>
                </div>
            </header>
            <div class="article-content">
                {{CONTENT}}
            </div>
        </article>
    </main>
    
    <footer>
        <p><a href="blog.html">← Retour au blog</a></p>
    </footer>
</body>
</html>"""

def create_article(topic, api_key=None):
    """Crée un nouvel article de blog"""
    # Génère le contenu
    print(f"Génération de l'article sur : {topic}")
    article_data = generate_article_content(topic, api_key)
    
    # Crée le slug
    slug = slugify(article_data['title'])
    date = datetime.now()
    
    # Crée le dossier articles s'il n'existe pas
    CONFIG['articles_dir'].mkdir(parents=True, exist_ok=True)
    
    # Charge le template
    template = load_template()
    
    # Remplace les placeholders
    html = template.replace('{{TITLE}}', article_data['title'])
    html = html.replace('{{EXCERPT}}', article_data.get('excerpt', ''))
    html = html.replace('{{CONTENT}}', article_data['content'])
    html = html.replace('{{DATE_ISO}}', date.strftime('%Y-%m-%d'))
    html = html.replace('{{DATE_FR}}', date.strftime('%d %B %Y'))
    
    # Sauvegarde l'article
    article_file = CONFIG['articles_dir'] / f"{slug}.html"
    article_file.write_text(html, encoding='utf-8')
    
    # Crée le fichier JSON de métadonnées
    metadata = {
        'title': article_data['title'],
        'slug': slug,
        'date': date.isoformat(),
        'excerpt': article_data.get('excerpt', ''),
        'topic': topic
    }
    
    metadata_file = CONFIG['articles_dir'] / f"{slug}.json"
    metadata_file.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding='utf-8')
    
    print(f"Article créé : {article_file}")
    return metadata

def update_blog_index():
    """Met à jour la page blog.html avec tous les articles"""
    articles = []
    
    # Charge tous les fichiers JSON de métadonnées
    for json_file in CONFIG['articles_dir'].glob('*.json'):
        if json_file.name == 'list.json':
            continue  # Ignore le fichier list.json lui-même
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                articles.append(json.load(f))
        except Exception as e:
            print(f"Erreur lors du chargement de {json_file}: {e}")
    
    # Trie par date (plus récent en premier)
    articles.sort(key=lambda x: x.get('date', ''), reverse=True)
    
    # Sauvegarde la liste
    list_file = CONFIG['articles_dir'] / 'list.json'
    list_file.write_text(
        json.dumps(articles, ensure_ascii=False, indent=2),
        encoding='utf-8'
    )
    
    return articles

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python generate_article.py <sujet>")
        print("Exemple: python generate_article.py 'Les meilleures pratiques en développement web'")
        sys.exit(1)
    
    topic = ' '.join(sys.argv[1:])
    api_key = os.getenv('OPENAI_API_KEY')
    
    metadata = create_article(topic, api_key)
    print(f"Article généré avec succès : {metadata['title']}")
    
    # Met à jour l'index
    update_blog_index()
    print("Index du blog mis à jour")

