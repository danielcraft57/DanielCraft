#!/bin/bash
# Script de déploiement du blog sur le Raspberry Pi

DOMAIN="danielcraft.fr"
REMOTE_USER="pi"
REMOTE_HOST="node12.lan"  # Ajuste selon ton setup
REMOTE_PATH="/var/www/${DOMAIN}/blog"

echo "Déploiement du blog sur ${REMOTE_HOST}..."

# Crée le dossier sur le serveur
ssh ${REMOTE_USER}@${REMOTE_HOST} "mkdir -p ${REMOTE_PATH}/articles"

# Copie les fichiers (sauf les articles générés)
rsync -avz --exclude 'articles/*.html' --exclude 'articles/*.json' \
    blog/ ${REMOTE_USER}@${REMOTE_HOST}:${REMOTE_PATH}/

# Rend les scripts exécutables
ssh ${REMOTE_USER}@${REMOTE_HOST} "chmod +x ${REMOTE_PATH}/*.py"

echo "Déploiement terminé !"
echo ""
echo "Pour générer un premier article :"
echo "ssh ${REMOTE_USER}@${REMOTE_HOST}"
echo "cd ${REMOTE_PATH}"
echo "python3 generate_article.py 'Mon premier article'"















































































