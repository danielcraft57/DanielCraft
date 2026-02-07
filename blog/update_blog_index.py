#!/usr/bin/env python3
"""
Met à jour la liste des articles (list.json) pour la page blog.html
"""

import json
from pathlib import Path
from datetime import datetime

BLOG_DIR = Path(__file__).parent
ARTICLES_DIR = BLOG_DIR / 'articles'

def update_index():
    """Met à jour le fichier list.json avec tous les articles"""
    articles = []
    
    # Charge tous les fichiers JSON de métadonnées
    for json_file in ARTICLES_DIR.glob('*.json'):
        # Ignore le fichier list.json lui-même
        if json_file.name == 'list.json':
            continue
            
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                article = json.load(f)
                # Vérifie que c'est bien un dictionnaire (pas une liste)
                if isinstance(article, dict):
                    articles.append(article)
                else:
                    print(f"Attention : {json_file} n'est pas un objet JSON valide")
        except Exception as e:
            print(f"Erreur lors du chargement de {json_file}: {e}")
    
    # Trie par date (plus récent en premier)
    articles.sort(key=lambda x: x.get('date', ''), reverse=True)
    
    # Sauvegarde la liste
    list_file = ARTICLES_DIR / 'list.json'
    list_file.write_text(
        json.dumps(articles, ensure_ascii=False, indent=2),
        encoding='utf-8'
    )
    
    print(f"Index mis à jour : {len(articles)} articles trouvés")
    return articles

if __name__ == '__main__':
    ARTICLES_DIR.mkdir(parents=True, exist_ok=True)
    update_index()

