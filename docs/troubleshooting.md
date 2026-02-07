# Troubleshooting - Erreurs Courantes

## Erreur : Ports 80/443 déjà utilisés

### Symptôme
```
nginx: [emerg] bind() to 0.0.0.0:443 failed (98: Address already in use)
nginx: [emerg] bind() to 0.0.0.0:80 failed (98: Address already in use)
```

### Cause
Un autre processus (souvent une autre instance de nginx) écoute déjà sur les ports 80 et/ou 443.

### Solution

#### 1. Vérifier ce qui utilise les ports

```bash
# Sur le serveur
ssh pi@node12.lan

# Vérifier le port 80
sudo lsof -i:80

# Vérifier le port 443
sudo lsof -i:443

# Ou avec netstat
sudo netstat -tulpn | grep :80
sudo netstat -tulpn | grep :443
```

#### 2. Si c'est nginx qui utilise les ports

C'est normal si nginx est déjà en cours d'exécution. Vérifie simplement que la config est correcte :

```bash
# Tester la config nginx
sudo nginx -t

# Si la config est OK, recharger (pas redémarrer)
sudo systemctl reload nginx
```

#### 3. Si c'est un autre processus

Si ce n'est pas nginx, il faut soit l'arrêter, soit le déplacer sur d'autres ports.

#### 4. Vérifier les sites activés

Parfois, plusieurs sites nginx essaient d'écouter sur les mêmes ports :

```bash
# Lister les sites activés
ls -la /etc/nginx/sites-enabled/

# Vérifier qu'il n'y a pas de conflit
sudo nginx -T | grep "listen"
```

#### 5. Redémarrer nginx proprement

Si nginx est dans un état incohérent :

```bash
# Arrêter nginx
sudo systemctl stop nginx

# Vérifier qu'aucun processus nginx ne tourne
ps aux | grep nginx

# Tuer les processus orphelins si nécessaire
sudo pkill -9 nginx

# Vérifier que les ports sont libres
sudo lsof -i:80
sudo lsof -i:443

# Redémarrer nginx
sudo systemctl start nginx
sudo systemctl status nginx
```

## Erreur : Certificats SSL manquants

### Symptôme
```
cannot load certificate "/etc/letsencrypt/live/danielcraft.fr/fullchain.pem": No such file or directory
```

### Solution
Utiliser `nginx.conf.no-ssl` avant de créer les certificats (voir `fix-ssl.md`)

## Erreur : Permissions 403/404

### Symptôme
- Erreur 403 (Forbidden)
- Erreur 404 (Not Found)

### Solution
Voir `PERMISSIONS.md` pour les détails complets.

Rapide :
```bash
sudo chown -R pi:www-data /var/www/danielcraft.fr
sudo find /var/www/danielcraft.fr -type d -exec chmod 755 {} \;
sudo find /var/www/danielcraft.fr -type f -exec chmod 644 {} \;
```

## Vérification Rapide

```bash
# État de nginx
sudo systemctl status nginx

# Test de configuration
sudo nginx -t

# Logs d'erreur
sudo tail -f /var/log/nginx/danielcraft.fr-error.log

# Logs d'accès
sudo tail -f /var/log/nginx/danielcraft.fr-access.log
```

