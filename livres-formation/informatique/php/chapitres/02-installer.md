# Installer PHP

## Ce qu'il te faut

Pour coder en PHP tu as besoin de PHP (l'interpreteur) et d'un serveur web local. La solution la plus simple : XAMPP (Windows/Mac) ou le serveur integre de PHP.

## Option 1 : serveur integre (recommande pour debuter)

1. Installe PHP depuis php.net (ou via XAMPP/Laragon).
2. Ouvre un terminal et tape `php -v`.
3. Cree un dossier `mon-projet` avec un fichier `index.php`.
4. Lance : `php -S localhost:8000`.
5. Ouvre `http://localhost:8000` dans ton navigateur.

> **Astuce DanielCraft** - Le serveur integre est parfait pour apprendre. Pas besoin d'Apache ni Nginx au debut.

## Option 2 : XAMPP

XAMPP installe PHP, Apache, MySQL et phpMyAdmin d'un coup. Pratique pour les projets avec base de donnees.

## Installer VS Code

Telecharge VS Code. Installe l'extension "PHP Intelephense" pour l'auto-completion et la detection d'erreurs.

## Petite histoire

Max installe PHP avec Laragon en 3 clics. Il cree `test.php`, ecrit `<?php phpinfo(); ?>`, ouvre le navigateur et voit toute la configuration PHP.

## A retenir

- `php -v` pour verifier l'installation.
- `php -S localhost:8000` pour le serveur integre.
- XAMPP pour un environnement complet.
