# Gestion des Permissions pour Nginx

## Problème

Nginx fonctionne avec l'utilisateur `www-data`. Si les permissions ne sont pas correctement configurées, on obtient des erreurs 403 (Forbidden) ou 404 (Not Found).

## Solution

### Permissions Requises

- **Propriétaire** : `pi` (pour pouvoir modifier les fichiers)
- **Groupe** : `www-data` (pour que nginx puisse lire les fichiers)
- **Répertoires** : `755` (rwxr-xr-x) - propriétaire peut tout faire, groupe et autres peuvent lire/exécuter
- **Fichiers** : `644` (rw-r--r--) - propriétaire peut lire/écrire, groupe et autres peuvent seulement lire

### Commandes Manuelles

Si tu dois corriger les permissions manuellement :

```bash
# Sur le serveur
ssh pi@node12.lan

# Aller dans le répertoire du site
cd /var/www/danielcraft.fr

# Configurer le propriétaire et le groupe
sudo chown -R pi:www-data /var/www/danielcraft.fr

# Permissions pour les répertoires (755)
sudo find /var/www/danielcraft.fr -type d -exec chmod 755 {} \;

# Permissions pour les fichiers (644)
sudo find /var/www/danielcraft.fr -type f -exec chmod 644 {} \;

# Vérifier que nginx peut lire
sudo -u www-data test -r /var/www/danielcraft.fr/index.html && echo "OK" || echo "ERREUR"
```

### Vérification

Pour vérifier que tout fonctionne :

```bash
# Vérifier les permissions d'un fichier
ls -la /var/www/danielcraft.fr/index.html

# Devrait afficher quelque chose comme :
# -rw-r--r-- 1 pi www-data 12345 Dec 25 12:00 index.html

# Tester si nginx peut lire
sudo -u www-data cat /var/www/danielcraft.fr/index.html
```

### Erreurs Courantes

#### Erreur 403 (Forbidden)
- **Cause** : Nginx ne peut pas lire les fichiers (mauvaises permissions)
- **Solution** : `sudo chmod 644` sur les fichiers, `sudo chmod 755` sur les répertoires
- **Vérifier** : `sudo -u www-data test -r /var/www/danielcraft.fr/index.html`

#### Erreur 404 (Not Found)
- **Cause** : Fichier non trouvé ou chemin incorrect
- **Solution** : Vérifier que les fichiers sont bien dans `/var/www/danielcraft.fr/`
- **Vérifier** : `ls -la /var/www/danielcraft.fr/`

#### Erreur 500 (Internal Server Error)
- **Cause** : Problème de configuration nginx ou permissions sur les logs
- **Solution** : Vérifier les logs nginx : `sudo tail -f /var/log/nginx/danielcraft.fr-error.log`

## Le Script deploy.sh

Le script `deploy.sh` configure automatiquement les permissions :
1. Après création du répertoire
2. Après transfert des fichiers
3. Avant le rechargement de nginx

Si tu as des problèmes, relance le script ou corrige manuellement avec les commandes ci-dessus.

