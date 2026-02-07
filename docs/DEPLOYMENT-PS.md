# Guide de Déploiement PowerShell - DanielCraft V6

## Script PowerShell de Déploiement

Un script PowerShell (`deploy.ps1`) a été créé pour faciliter le déploiement depuis Windows.

## Utilisation

### Déploiement complet (contenu + nginx + PHP)

```powershell
cd V6
.\scripts\deploy.ps1 -Domain "danielcraft.fr"
```

Transfère tout depuis `dist/` (HTML, assets, **api/**), applique les permissions, copie la config nginx (avec le bloc PHP pour le formulaire de contact) et recharge nginx. À faire au moins une fois, puis après chaque modification de `scripts/nginx.conf`.

### Déploiement contenu uniquement (rapide)

```powershell
cd V6
.\scripts\deploy-content.ps1
```

Lance le build Python puis transfère uniquement le contenu de `dist/` (HTML, assets, **api/**). Ne modifie pas nginx. Idéal pour les mises à jour fréquentes (textes, CSS, JS, formulaire PHP).

### Formulaire de contact (PHP)

Le dossier `dist/api/` contient `send-contact.php`. Pour que le formulaire fonctionne sur le serveur :

1. **PHP-FPM** doit être installé et actif : `sudo systemctl status php*-fpm`
2. La config nginx doit inclure le bloc pour `/api/*.php` (déjà présent dans `scripts/nginx.conf`). Si le socket PHP diffère (ex. `php8.1-fpm.sock`), adapter la ligne `fastcgi_pass` dans `nginx.conf`.
3. Après un déploiement complet, recharger nginx : `ssh pi@node12.lan 'sudo systemctl reload nginx'`

### Prérequis

- **SSH** : Doit être installé et configuré (généralement inclus dans Windows 10/11)
- **rsync** (optionnel) : Pour un transfert plus efficace. Si absent, le script utilise `scp`
- **Accès SSH** : Certificat SSH configuré pour `pi@node12.lan`

### Vérifier les Prérequis

```powershell
# Vérifier SSH
ssh -V

# Vérifier rsync (optionnel)
rsync --version

# Tester la connexion
ssh pi@node12.lan "echo 'Connexion OK'"
```

## Fonctionnalités du Script

Le script `deploy.ps1` fait automatiquement :

1. ✅ Vérification du répertoire (présence de index.html)
2. ✅ Création du répertoire sur le serveur
3. ✅ Transfert des fichiers (rsync ou scp)
4. ✅ Configuration des permissions (chown/chmod pour www-data)
5. ✅ Préparation de la config nginx (avec ou sans SSL selon certificats)
6. ✅ Activation de la configuration nginx
7. ✅ Test de la configuration
8. ✅ Création des certificats SSL (si nécessaire)
9. ✅ Rechargement de nginx
10. ✅ Vérification finale

## Différences avec deploy.sh

- **Syntaxe PowerShell** : Adapté pour Windows
- **Gestion des erreurs** : `$ErrorActionPreference = "Stop"`
- **Fichiers temporaires** : Utilise `[System.IO.Path]::GetTempFileName()`
- **Fallback rsync** : Si rsync n'est pas disponible, utilise scp

## Exemple de Sortie

```
=== Deploiement DanielCraft V6 ===
Domaine: danielcraft.fr
Serveur: pi@node12.lan

[1/6] Creation du repertoire sur le serveur...
[2/6] Transfert des fichiers...
[3/6] Configuration des permissions (chown/chmod pour www-data)...
Permissions OK
[4/6] Preparation de la configuration nginx...
Certificats SSL trouves, utilisation de la config complete
[5/6] Activation de la configuration nginx...
Lien symbolique cree
Test de la configuration nginx...
[6/6] Configuration du certificat SSL...
Certificats SSL deja presents, configuration OK.
[Finalisation] Verification finale des permissions et rechargement de nginx...
OK: Nginx est actif et fonctionne correctement

=== Deploiement termine avec succes ! ===
Site disponible sur: https://danielcraft.fr
```

## Dépannage

### Erreur "ssh : commande introuvable"
- Installer OpenSSH : `Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0`

### Erreur "rsync : commande introuvable"
- Le script utilise automatiquement `scp` en fallback
- Pour installer rsync : utiliser WSL ou installer via Chocolatey

### Erreur de permissions
- Vérifier que le certificat SSH est bien configuré
- Tester manuellement : `ssh pi@node12.lan`

### Erreur nginx
- Voir `troubleshooting.md` pour les solutions détaillées

## Comparaison Scripts

| Fonctionnalité | deploy.sh (Bash) | deploy.ps1 (PowerShell) |
|----------------|------------------|-------------------------|
| Système | Linux/Mac/Git Bash | Windows PowerShell |
| Transfert | rsync | rsync (fallback scp) |
| SSL | Certbot automatique | Certbot automatique |
| Permissions | chown/chmod | chown/chmod |
| Test config | nginx -t | nginx -t |

**Les deux scripts font la même chose, seul l'environnement d'exécution change.**

## Notes

- Le script PowerShell est équivalent au script bash
- Même logique, même fonctionnalités
- Adapté pour Windows avec gestion d'erreurs PowerShell
- Compatible avec PowerShell 5.1+ et PowerShell Core 7+

---

*Pour Linux/Mac, utiliser `deploy.sh`. Pour Windows, utiliser `deploy.ps1`.*

