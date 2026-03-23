# API formulaire de contact

Le dossier `api/` contient le script PHP d'envoi du formulaire de contact.

- **Endpoint :** `POST /api/send-contact.php`
- **Données :** `name`, `email`, `phone`, `service`, `budget`, `message` (form-data)
- **Réponse :** JSON `{ "success": true }` ou `{ "success": false, "error": "..." }`

Le script envoie un email à `contact@danielcraft.fr` via `mail()`. Sur le serveur, Nginx exécute les `.php` avec PHP 8.2-FPM (voir `scripts/nginx.conf`, socket `php8.2-fpm.sock`).

## Test en local

- **`python -m http.server`** : ne traite pas le PHP ; un `POST` vers `/api/send-contact.php` peut renvoyer **501** ou **405**. Utilisez plutôt le serveur intégré PHP depuis la racine du site :
  - `php -S 127.0.0.1:8000`
- Puis ouvrez `http://127.0.0.1:8000/` (ou le dossier `dist/` selon votre flux de build).
