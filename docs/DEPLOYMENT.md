# Guide de Déploiement - DanielCraft V6

## Prérequis

- Serveur nginx sur `deploy@server.local` (exemple)
- Nom de domaine configuré (DNS pointant vers le serveur)
- Accès SSH au serveur
- rsync installé (généralement déjà présent)
- Sous Windows : `ssh`/`scp` disponibles (OpenSSH) et idéalement `rsync` (sinon fallback `scp` dans `deploy-content.ps1`)

## Déploiement Automatique (Recommandé)

### Utiliser le script de déploiement

```bash
# Depuis le dossier V6
./deploy.sh ton-domaine.com
```

Le script va automatiquement :
1. Créer le répertoire sur le serveur
2. Transférer les fichiers
3. Configurer les permissions
4. Installer la configuration nginx
5. Activer la configuration
6. Configurer le certificat SSL avec Certbot
7. Recharger nginx

**Exemple :**
```bash
./deploy.sh portfolio-likedev.fr
```

## Déploiement contenu uniquement (Windows / PowerShell)

Si nginx + SSL sont déjà en place et que tu veux uniquement publier le contenu généré dans `dist/`, utilise `scripts/deploy-content.ps1`.

- Ce script lance `python3 build.py`, puis transfère `dist/` sur le serveur.
- Il **ne modifie pas** nginx, Certbot, ni la configuration serveur.
- Il utilise **rsync** si dispo, sinon bascule en **scp**.
- Il lit sa config depuis `.env.local` puis `.env` (variables `DEPLOY_*`). Les paramètres CLI gardent la priorité.

### Exemple pour `node12.lan`

Depuis la racine du repo :

```powershell
.\scripts\deploy-content.ps1 `
  -ServerUser "pi" `
  -ServerHost "node12.lan" `
  -ServerPath "/var/www/danielcraft.fr" `
  -SiteBase "https://danielcraft.fr" `
  -NginxLogName "danielcraft.fr"
```

### Notes utiles

- Si `rsync` n’est pas trouvé, le script te le dira et passera en fallback `scp`.
- `SiteBase` sert au build (canoniques, OG, sitemaps) : mets l’URL publique finale.
- Variante “sans paramètres” (recommandé) : mets ces valeurs dans `.env.local` :
  - `DEPLOY_SERVER_USER`, `DEPLOY_SERVER_HOST`, `DEPLOY_SERVER_PATH`
  - `DEPLOY_SITE_BASE`, `DEPLOY_NGINX_LOG_NAME`
- Pour consulter les logs nginx (si tu as les droits) :

```bash
ssh deploy@node12.lan "sudo tail -f /var/log/nginx/danielcraft.fr-error.log"
```

## Déploiement Manuel

### 1. Préparer les fichiers sur le serveur

```bash
# Se connecter au serveur
ssh deploy@server.local

# Créer le répertoire pour le site
sudo mkdir -p /var/www/example.com

# Donner les permissions appropriées
sudo chown -R deploy:www-data /var/www/example.com
sudo chmod -R 755 /var/www/example.com
```

### 2. Transférer les fichiers

Depuis ta machine locale :

```bash
# Depuis le dossier V6
rsync -avz --exclude 'node_modules' --exclude '.git' --exclude '*.md' --exclude 'deploy.sh' --exclude 'nginx.conf' ./ deploy@server.local:/var/www/example.com/
```

### 3. Configurer Nginx

```bash
# Se connecter au serveur
ssh deploy@server.local

# Copier et adapter la config nginx (remplacer 'ton-domaine.com' par ton domaine)
sed "s/ton-domaine.com/TON-DOMAINE/g" nginx.conf | sudo tee /etc/nginx/sites-available/danielcraft-v6

# Ou éditer manuellement
sudo nano /etc/nginx/sites-available/danielcraft-v6
```

**Points à vérifier/modifier dans la config :**
- `server_name` : remplacer `ton-domaine.com` par ton nom de domaine réel
- `root` : chemin vers les fichiers (par défaut `/var/www/danielcraft-v6`)
- Les chemins SSL seront configurés automatiquement par Certbot

### 4. Activer la configuration

```bash
# Créer le lien symbolique
sudo ln -s /etc/nginx/sites-available/danielcraft-v6 /etc/nginx/sites-enabled/

# Tester la configuration
sudo nginx -t

# Si OK, recharger nginx
sudo systemctl reload nginx
```

### 5. Configurer le DNS

Ajouter un enregistrement DNS A pour ton domaine :

```
Type: A
Nom: @ (ou ton-domaine.com)
Valeur: IP de ton serveur
TTL: 3600
```

Pour www :
```
Type: A
Nom: www
Valeur: IP de ton serveur
TTL: 3600
```

### 6. Obtenir le certificat SSL

```bash
ssh deploy@server.local
sudo certbot --nginx -d ton-domaine.com -d www.ton-domaine.com
```

### 7. Vérifier le déploiement

- Visiter `https://ton-domaine.com`
- Vérifier que toutes les pages fonctionnent
- Vérifier que les assets (CSS, JS, images) se chargent correctement
- Catalogue vitrines DanielCraft : `https://ton-domaine.com/vitrines/` (collection + fiches)
- Index technique des démos Bulma : `https://ton-domaine.com/vitrines/hub-bulma.html`
- Fiche vitrine (achat, textes) : `https://ton-domaine.com/vitrines/<slug>/` (ex. `/vitrines/technologie/`)
- Démo HTML d’un secteur : `https://ton-domaine.com/vitrines/<slug>/demo/index.html`
- Le build copie **`assets/vitrines/demos/`** et **`assets/vitrines/screenshots/`** vers **`dist/vitrines/`** ; le déploiement doit inclure tout le dossier **`dist/vitrines/`** (voir `scripts/deploy-content.ps1` et **[VITRINES.md](./VITRINES.md)**).

## Déploiement automatique sur le serveur (cron)

Le webroot (`/var/www/danielcraft.fr`) n’est **pas** un dépôt git. Le dépôt vit à part :

| Chemin | Rôle |
|--------|------|
| `/home/pi/danielcraft-src` | Clone git (pull, tests, build) |
| `/var/www/danielcraft.fr` | Site servi par nginx (rsync depuis `dist/`) |

Le script `scripts/prod-auto-deploy.sh` enchaîne : `git pull` → tests PHP/Python → `build.py` → `rsync` (`.env` prod préservé).

**Cron installé sur `pi@node12.lan`** — toutes les 15 minutes, déploie seulement si `master` a avancé sur GitHub :

```bash
*/15 * * * * REPO_DIR=/home/pi/danielcraft-src WEB_ROOT=/var/www/danielcraft.fr SITE_BASE=https://danielcraft.fr /home/pi/danielcraft-src/scripts/prod-auto-deploy.sh >> /home/pi/logs/danielcraft-deploy.log 2>&1
```

Commandes utiles :

```bash
# Forcer un déploiement immédiat (après push sur master)
ssh pi@node12.lan 'FORCE_DEPLOY=1 /home/pi/danielcraft-src/scripts/prod-auto-deploy.sh'

# Suivre les logs
ssh pi@node12.lan 'tail -f /home/pi/logs/danielcraft-deploy.log'
```

**Workflow** : merge sur `master` → GitHub Actions CI (optionnel) → cron Pi détecte le nouveau commit → tests + build + rsync.

## Mise à Jour

Pour mettre à jour le site manuellement depuis ta machine (sans attendre le cron) :

```bash
# Depuis ta machine locale, dans le dossier V6
rsync -avz --exclude 'node_modules' --exclude '.git' ./ deploy@server.local:/var/www/example.com/

# Sur le serveur, recharger nginx si nécessaire
ssh deploy@server.local "sudo systemctl reload nginx"
```

## Dépannage

### Vérifier les logs

```bash
# Logs d'accès
sudo tail -f /var/log/nginx/danielcraft-v6-access.log

# Logs d'erreur
sudo tail -f /var/log/nginx/danielcraft-v6-error.log
```

### Vérifier les permissions

```bash
sudo ls -la /var/www/danielcraft-v6
sudo chown -R pi:www-data /var/www/danielcraft-v6
sudo chmod -R 755 /var/www/danielcraft-v6
```

### Tester la configuration nginx

```bash
sudo nginx -t
```

## Notes

- Le fichier `nginx.conf` est configuré pour un nom de domaine complet (pas un sous-domaine)
- La config est optimisée pour les performances (cache, compression gzip)
- Les headers de sécurité sont inclus
- Les chemins relatifs sont gérés pour que le site fonctionne correctement
- Le script `deploy.sh` automatise tout le processus de déploiement

