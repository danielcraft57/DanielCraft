#!/usr/bin/env bash
# Prévisualisation : racine du site = dist/ (URLs /assets/...)
set -e
cd "$(dirname "$0")/.."
echo "Build rapide (sans WebP)..."
python3 build.py --no-webp
echo ""
echo "Serveur : http://localhost:8000/"
echo "Ne pas ouvrir /dist/index.html avec le serveur à la racine du dépôt."
echo ""
python3 -m http.server 8000 --directory dist
