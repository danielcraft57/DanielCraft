# API formulaire de contact

Le dossier `api/` contient le script PHP d'envoi du formulaire de contact.

- **Endpoint :** `POST /api/send-contact.php`
- **Données :** `name`, `email`, `phone`, `service`, `budget`, `message` (form-data)
- **Réponse :** JSON `{ "success": true }` ou `{ "success": false, "error": "..." }`

Le script envoie un email à `contact@danielcraft.fr` via `mail()`. Sur le serveur, Nginx exécute les `.php` avec PHP 8.2-FPM (voir `scripts/nginx.conf`, socket `php8.2-fpm.sock`).
