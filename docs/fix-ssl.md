# Fix SSL - Certificats manquants

## Problème

Certbot ne peut pas créer les certificats car nginx.conf référence des certificats qui n'existent pas encore.

## Solution

1. **Utiliser la version sans SSL temporairement**

Sur le serveur, remplace la config nginx par la version sans SSL :

```bash
ssh pi@node12.lan
sudo cp /var/www/danielcraft.fr/nginx.conf.no-ssl /etc/nginx/sites-available/danielcraft.fr
sudo nginx -t
sudo systemctl reload nginx
```

2. **Créer les certificats avec Certbot**

```bash
sudo certbot --nginx -d danielcraft.fr -d www.danielcraft.fr --non-interactive --agree-tos --email loic5488@gmail.com --redirect
```

Certbot va :
- Créer les certificats SSL
- Modifier automatiquement nginx.conf pour ajouter le bloc SSL
- Configurer la redirection HTTP → HTTPS

3. **Après création des certificats**

Si tu veux utiliser la version complète de nginx.conf (avec toutes les optimisations SSL), tu peux la restaurer :

```bash
sudo cp /var/www/danielcraft.fr/nginx.conf /etc/nginx/sites-available/danielcraft.fr
sudo nginx -t
sudo systemctl reload nginx
```

Mais normalement, Certbot a déjà tout configuré correctement, donc c'est optionnel.

## Alternative : Script mis à jour

Le script `deploy.sh` a été mis à jour pour détecter automatiquement si les certificats existent et utiliser la bonne version de la config.

