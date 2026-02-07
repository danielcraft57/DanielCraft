#!/usr/bin/env python3
"""
Script pour générer automatiquement un article chaque jour
À exécuter via cron job
"""

import os
import sys
import random
from pathlib import Path
from generate_article import create_article, update_blog_index

# Sujets prédéfinis pour générer des articles variés
TOPICS = [
    "Les meilleures pratiques en développement web moderne",
    "Comment optimiser les performances d'un site web",
    "Introduction à TypeScript pour les développeurs JavaScript",
    "Les frameworks frontend en 2025 : React, Vue, Angular",
    "Développement backend avec Node.js : bonnes pratiques",
    "Sécurité web : les vulnérabilités courantes et comment les éviter",
    "Déploiement continu : CI/CD pour les projets web",
    "Gestion d'état dans les applications React",
    "API REST vs GraphQL : lequel choisir ?",
    "Tests unitaires et d'intégration en JavaScript",
    "Optimisation SEO pour les sites web",
    "Accessibilité web : rendre son site utilisable par tous",
    "Microservices vs Monolithe : avantages et inconvénients",
    "Docker et conteneurisation pour le développement web",
    "Gestion de projet agile pour développeurs",
    "Les outils essentiels du développeur moderne",
    "Responsive design : créer des sites adaptatifs",
    "Performance web : techniques d'optimisation avancées",
    "Gestion de version avec Git : workflow efficace",
    "Architecture logicielle : principes SOLID appliqués"
]

def generate_daily_article():
    """Génère un article quotidien"""
    # Vérifie si un article a déjà été généré aujourd'hui
    from datetime import datetime
    today = datetime.now().strftime('%Y-%m-%d')
    
    articles_dir = Path(__file__).parent / 'articles'
    articles_dir.mkdir(parents=True, exist_ok=True)
    
    # Vérifie les articles d'aujourd'hui
    today_articles = list(articles_dir.glob(f'*{today}*.json'))
    if today_articles:
        print(f"Un article a déjà été généré aujourd'hui ({today})")
        return
    
    # Sélectionne un sujet aléatoire
    topic = random.choice(TOPICS)
    
    # Génère l'article
    api_key = os.getenv('OPENAI_API_KEY')
    try:
        metadata = create_article(topic, api_key)
        print(f"Article généré avec succès : {metadata['title']}")
        
        # Met à jour l'index
        update_blog_index()
        print("Index du blog mis à jour")
        
    except Exception as e:
        print(f"Erreur lors de la génération : {e}")
        sys.exit(1)

if __name__ == '__main__':
    generate_daily_article()















































































