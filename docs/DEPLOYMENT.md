# Guide de Déploiement - DanielCraft V6

## Prérequis

- Serveur nginx sur `pi@node12.lan`
- Nom de domaine configuré (DNS pointant vers le serveur)
- Accès SSH au serveur
- rsync installé (généralement déjà présent)

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

## Déploiement Manuel

### 1. Préparer les fichiers sur le serveur

```bash
# Se connecter au serveur
ssh pi@node12.lan

# Créer le répertoire pour le site
sudo mkdir -p /var/www/danielcraft-v6

# Donner les permissions appropriées
sudo chown -R pi:www-data /var/www/danielcraft-v6
sudo chmod -R 755 /var/www/danielcraft-v6
```

### 2. Transférer les fichiers

Depuis ta machine locale :

```bash
# Depuis le dossier V6
rsync -avz --exclude 'node_modules' --exclude '.git' --exclude '*.md' --exclude 'deploy.sh' --exclude 'nginx.conf' ./ pi@node12.lan:/var/www/danielcraft-v6/
```

### 3. Configurer Nginx

```bash
# Se connecter au serveur
ssh pi@node12.lan

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
Valeur: IP de node12.lan
TTL: 3600
```

Pour www :
```
Type: A
Nom: www
Valeur: IP de node12.lan
TTL: 3600
```

### 6. Obtenir le certificat SSL

```bash
ssh pi@node12.lan
sudo certbot --nginx -d ton-domaine.com -d www.ton-domaine.com
```

### 7. Vérifier le déploiement

- Visiter `https://ton-domaine.com`
- Vérifier que toutes les pages fonctionnent
- Vérifier que les assets (CSS, JS, images) se chargent correctement

## Mise à Jour

Pour mettre à jour le site après des modifications :

```bash
# Depuis ta machine locale, dans le dossier V6
rsync -avz --exclude 'node_modules' --exclude '.git' ./ pi@node12.lan:/var/www/danielcraft-v6/

# Sur le serveur, recharger nginx si nécessaire
ssh pi@node12.lan "sudo systemctl reload nginx"
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

