# Configuration Nginx

Ce dossier contient les fichiers de configuration Nginx pour le site.

## Fichiers

- **nginx.conf** - Configuration complète avec SSL (production)
- **nginx.conf.no-ssl** - Configuration sans SSL (développement/test)

## Installation

### Sur le serveur

1. Copier la configuration dans le dossier nginx :
```bash
sudo cp scripts/nginx.conf /etc/nginx/sites-available/danielcraft.fr
```

2. Créer le lien symbolique :
```bash
sudo ln -s /etc/nginx/sites-available/danielcraft.fr /etc/nginx/sites-enabled/
```

3. Tester la configuration :
```bash
sudo nginx -t
```

4. Recharger nginx :
```bash
sudo systemctl reload nginx
```

## Configuration SSL

La configuration utilise Let's Encrypt avec Certbot. Pour installer les certificats :

```bash
sudo certbot --nginx -d danielcraft.fr -d www.danielcraft.fr
```

## Fonctionnalités

- ✅ Redirection HTTP → HTTPS
- ✅ URLs propres (sans .html)
- ✅ Compression Gzip optimisée
- ✅ Cache pour les assets statiques (1 an)
- ✅ Cache pour les fichiers HTML (1 heure)
- ✅ Headers de sécurité
- ✅ Support HTTP/2

## Optimisations

- Compression Gzip niveau 6
- Cache immutable pour les assets statiques
- Cache must-revalidate pour les HTML
- Headers de sécurité (X-Frame-Options, etc.)
- Logs séparés (access et error)

## Notes

- Les fichiers HTML sont servis sans extension (URLs propres)
- Les anciennes URLs avec .html sont redirigées en 301
- Le dossier racine est `/var/www/danielcraft.fr`

