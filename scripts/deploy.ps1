# Script PowerShell de déploiement pour DanielCraft V6
# Usage: .\deploy.ps1
#        .\deploy.ps1 -Domain "danielcraft.fr"
#        .\deploy.ps1 -ContentOnly  (déploiement contenu uniquement)

param(
    [string]$Domain = "danielcraft.fr",
    [switch]$ContentOnly
)

# Configuration
$ErrorActionPreference = "Stop"
$SERVER_USER = "pi"
$SERVER_HOST = "node12.lan"
$SERVER_PATH = "/var/www/danielcraft.fr"
$NGINX_SITES_AVAILABLE = "/etc/nginx/sites-available"
$NGINX_SITES_ENABLED = "/etc/nginx/sites-enabled"
$CONFIG_NAME = "danielcraft.fr"

# Couleurs pour les messages
function Write-ColorOutput {
    param([string]$Message, [string]$Color = "White")
    Write-Host $Message -ForegroundColor $Color
}

Write-ColorOutput "=== Deploiement DanielCraft V6 ===" "Green"
Write-ColorOutput "Domaine: $Domain" "Yellow"
Write-ColorOutput "Serveur: ${SERVER_USER}@${SERVER_HOST}" "Yellow"
Write-Host ""

# 1. Vérifier que nous sommes dans le bon répertoire
if (-not (Test-Path "build.py")) {
    Write-ColorOutput "Erreur: build.py non trouve. Execute ce script depuis le dossier V6." "Red"
    exit 1
}

# 1.5. Lancer le build Python
Write-ColorOutput "[0/6] Lancement du build Python..." "Yellow"

# On essaie d'utiliser 'python' en priorité (là où Pillow est installé),
# et on tombe sur 'python3' si besoin.
$pythonCmd = "python"
try {
    Get-Command $pythonCmd -ErrorAction Stop | Out-Null
} catch {
    $pythonCmd = "python3"
}

$buildOutput = & $pythonCmd build.py 2>&1 | Out-String
if ($LASTEXITCODE -ne 0) {
    Write-ColorOutput "Erreur lors du build Python (commande: $pythonCmd build.py):" "Red"
    Write-Host $buildOutput
    exit 1
}
Write-Host $buildOutput

# Info UX/perf: compter les WebP generees dans dist/assets
$DIST_DIR = "dist"
if (Test-Path "$DIST_DIR/assets") {
    $webpFiles = Get-ChildItem -Path "$DIST_DIR/assets" -Recurse -Filter *.webp -ErrorAction SilentlyContinue
    $webpCount = ($webpFiles | Measure-Object).Count
    Write-ColorOutput "Images WebP detectees dans dist/assets: $webpCount" "Yellow"
}

Write-ColorOutput "Build Python termine avec succes" "Green"
Write-Host ""

# Vérifier que le dossier dist/ existe et contient index.html
if (-not (Test-Path "$DIST_DIR/index.html")) {
    Write-ColorOutput "Erreur: index.html non trouve dans $DIST_DIR/. Le build a peut-etre echoue." "Red"
    exit 1
}
Write-ColorOutput "Dossier $DIST_DIR/ verifie, pret pour le deploiement" "Green"
Write-Host ""

# 2. Créer le répertoire sur le serveur si nécessaire
Write-ColorOutput "[1/6] Creation du repertoire sur le serveur..." "Yellow"
$createDirCmd = "sudo mkdir -p $SERVER_PATH && sudo chown -R ${SERVER_USER}:www-data $SERVER_PATH && sudo chmod -R 755 $SERVER_PATH"
ssh "${SERVER_USER}@${SERVER_HOST}" $createDirCmd

# 3. Transférer les fichiers depuis dist/ avec rsync
Write-ColorOutput "[2/6] Transfert des fichiers depuis $DIST_DIR/..." "Yellow"

# Vérifier si rsync est disponible (sinon utiliser scp)
try {
    $rsyncCheck = Get-Command rsync -ErrorAction Stop
    Write-ColorOutput "Utilisation de rsync (transfert optimise)..." "Yellow"
    $rsyncCmd = "rsync -avz --delete $DIST_DIR/ ${SERVER_USER}@${SERVER_HOST}:${SERVER_PATH}/"
    Invoke-Expression $rsyncCmd
    
    if ($LASTEXITCODE -eq 0) {
        Write-ColorOutput "Transfert rsync reussi" "Green"
    } else {
        Write-ColorOutput "Erreur lors du transfert rsync" "Red"
        exit 1
    }
} catch {
    Write-ColorOutput "rsync non trouve, utilisation de scp..." "Yellow"
    # Alternative avec scp (moins efficace mais fonctionne)
    # Transfère tous les fichiers HTML et le dossier assets
    Get-ChildItem -Path $DIST_DIR -Filter *.html | ForEach-Object {
        Write-Host "  Transfert: $($_.Name)"
        scp $_.FullName "${SERVER_USER}@${SERVER_HOST}:${SERVER_PATH}/"
    }
    
    # Transfère robots.txt et sitemap.xml
    foreach ($file in @("robots.txt", "sitemap.xml")) {
        $filePath = Join-Path $DIST_DIR $file
        if (Test-Path $filePath) {
            Write-Host "  Transfert: $file"
            scp $filePath "${SERVER_USER}@${SERVER_HOST}:${SERVER_PATH}/"
        }
    }
    
    # Transfère le dossier assets
    if (Test-Path "$DIST_DIR/assets") {
        Write-Host "  Transfert: assets/ (peut prendre du temps...)"
        scp -r "$DIST_DIR/assets" "${SERVER_USER}@${SERVER_HOST}:${SERVER_PATH}/"
    }

    # Transfère le dossier api (formulaire contact PHP)
    if (Test-Path "$DIST_DIR/api") {
        Write-Host "  Transfert: api/"
        scp -r "$DIST_DIR/api" "${SERVER_USER}@${SERVER_HOST}:${SERVER_PATH}/"
    }
    
    Write-ColorOutput "Transfert scp termine" "Green"
}

# 3.5 Vérification rapide des images hero sur le serveur
Write-ColorOutput "[Check] Verification des images du hero (assets/images/hero)..." "Yellow"
$checkHeroCmd = 'if test -d ' + $SERVER_PATH + '/assets/images/hero; then n=$(ls -1 ' + $SERVER_PATH + '/assets/images/hero/*.{png,jpg,jpeg,webp} 2>/dev/null | wc -l); echo "OK: assets/images/hero present ($n images)"; else echo "ATTENTION: assets/images/hero manquant (mockups hero)"; fi'
$checkHeroResult = ssh "${SERVER_USER}@${SERVER_HOST}" $checkHeroCmd
Write-Host $checkHeroResult

# Mode contenu uniquement : on s'arrête ici
if ($ContentOnly) {
    Write-ColorOutput "[Mode contenu] Pas de config nginx/SSL, seulement les fichiers." "Yellow"
    Write-ColorOutput "Transfert termine. Tu peux recharger nginx si besoin :" "Yellow"
    Write-Host "ssh ${SERVER_USER}@${SERVER_HOST} 'sudo systemctl reload nginx'"
    Write-ColorOutput "=== Deploiement contenu termine ===" "Green"
    exit 0
}

# 4. Configurer les permissions (CRITIQUE pour nginx/www-data)
Write-ColorOutput "[3/6] Configuration des permissions (chown/chmod pour www-data)..." "Yellow"
$permissionsCmd = "sudo chown -R ${SERVER_USER}:www-data $SERVER_PATH; sudo find $SERVER_PATH -type d -exec chmod 755 {} ';'; sudo find $SERVER_PATH -type f -exec chmod 644 {} ';'; sudo -u www-data test -r $SERVER_PATH/index.html && echo 'Permissions OK' || echo 'ERREUR: nginx ne peut pas lire les fichiers'"
ssh "${SERVER_USER}@${SERVER_HOST}" $permissionsCmd

# 5. Préparer la config nginx
Write-ColorOutput "[4/6] Preparation de la configuration nginx..." "Yellow"

# Vérifier si les certificats SSL existent déjà
$certCheckCmd = "test -f /etc/letsencrypt/live/$Domain/fullchain.pem && echo 'yes' || echo 'no'"
$certExists = (ssh "${SERVER_USER}@${SERVER_HOST}" $certCheckCmd).Trim()

$tmpFile = [System.IO.Path]::GetTempFileName() + ".conf"

# Utiliser la config nginx depuis scripts/ (SSL déjà installé)
$nginxConfigPath = Join-Path $PSScriptRoot "nginx.conf"

if (-not (Test-Path $nginxConfigPath)) {
    Write-ColorOutput "Erreur: nginx.conf non trouve dans scripts/" "Red"
    exit 1
}

Write-ColorOutput "Utilisation de la configuration nginx avec SSL" "Green"
Copy-Item $nginxConfigPath $tmpFile

# Transférer la config sur le serveur
scp $tmpFile "${SERVER_USER}@${SERVER_HOST}:/tmp/nginx-${CONFIG_NAME}.conf"

# Installer la config
$installConfigCmd = "sudo mv /tmp/nginx-${CONFIG_NAME}.conf ${NGINX_SITES_AVAILABLE}/${CONFIG_NAME} && sudo chown root:root ${NGINX_SITES_AVAILABLE}/${CONFIG_NAME} && sudo chmod 644 ${NGINX_SITES_AVAILABLE}/${CONFIG_NAME}"
ssh "${SERVER_USER}@${SERVER_HOST}" $installConfigCmd

# Nettoyer le fichier temporaire local
Remove-Item $tmpFile -ErrorAction SilentlyContinue

# 6. Activer la configuration nginx
Write-ColorOutput "[5/6] Activation de la configuration nginx..." "Yellow"
$activateConfigCmd = "if [ ! -L ${NGINX_SITES_ENABLED}/${CONFIG_NAME} ]; then sudo ln -s ${NGINX_SITES_AVAILABLE}/${CONFIG_NAME} ${NGINX_SITES_ENABLED}/${CONFIG_NAME}; echo 'Lien symbolique cree'; else echo 'Lien symbolique existe deja'; fi"
ssh "${SERVER_USER}@${SERVER_HOST}" $activateConfigCmd

# Tester la configuration nginx
Write-Host "Test de la configuration nginx..."
$nginxTest = ssh "${SERVER_USER}@${SERVER_HOST}" "sudo nginx -t 2>&1"
$nginxTestResult = $LASTEXITCODE

if ($nginxTestResult -ne 0) {
    Write-ColorOutput "Erreur dans la configuration nginx." "Red"
    Write-ColorOutput "Diagnostic des ports 80/443..." "Yellow"
    ssh "${SERVER_USER}@${SERVER_HOST}" "echo '=== Port 80 ==='; sudo lsof -i:80 2>/dev/null || echo 'Libre'; echo ''; echo '=== Port 443 ==='; sudo lsof -i:443 2>/dev/null || echo 'Libre'; echo ''; echo '=== Sites actives ==='; ls -la ${NGINX_SITES_ENABLED}/"
    Write-ColorOutput "Note: Si les ports sont utilises par nginx lui-meme, c'est normal." "Yellow"
    Write-ColorOutput "Le probleme vient probablement d'une configuration invalide. Verifie les logs ci-dessus." "Yellow"
    exit 1
}

# 7. Vérifier les certificats SSL
Write-ColorOutput "[6/6] Verification des certificats SSL..." "Yellow"

if ($certExists -eq "yes") {
    Write-ColorOutput "Certificats SSL deja presents, configuration OK." "Green"
        } else {
    Write-ColorOutput "Attention: Certificats SSL non trouves sur le serveur." "Yellow"
    Write-ColorOutput "La configuration nginx est prete pour SSL, mais les certificats doivent etre installes." "Yellow"
    Write-ColorOutput "Si SSL est deja configure, c'est normal (le script verifie juste l'existence des fichiers)." "Yellow"
    Write-ColorOutput "Pour installer/renouveler SSL:" "Yellow"
        Write-Host "ssh ${SERVER_USER}@${SERVER_HOST} 'sudo certbot --nginx -d $Domain -d www.$Domain'"
}

# 8. Vérifier les permissions une dernière fois et recharger nginx
Write-ColorOutput "[Finalisation] Verification finale des permissions et rechargement de nginx..." "Yellow"
$finalPermissionsCmd = "sudo chown -R ${SERVER_USER}:www-data $SERVER_PATH; sudo find $SERVER_PATH -type d -exec chmod 755 {} ';'; sudo find $SERVER_PATH -type f -exec chmod 644 {} ';'"
ssh "${SERVER_USER}@${SERVER_HOST}" $finalPermissionsCmd
$reloadNginxCmd = "sudo systemctl reload nginx; sleep 1; if sudo systemctl is-active --quiet nginx; then echo 'OK: Nginx est actif et fonctionne correctement'; sudo systemctl status nginx --no-pager -l | head -10; else echo 'ERREUR: Nginx n est pas actif'; sudo journalctl -u nginx -n 20 --no-pager; exit 1; fi"
ssh "${SERVER_USER}@${SERVER_HOST}" $reloadNginxCmd

Write-Host ""
Write-ColorOutput "=== Deploiement termine avec succes ! ===" "Green"
Write-ColorOutput "Site disponible sur: https://$Domain" "Green"
Write-Host ""
Write-ColorOutput "Pour verifier les logs:" "Yellow"
Write-Host "ssh ${SERVER_USER}@${SERVER_HOST} 'sudo tail -f /var/log/nginx/${CONFIG_NAME}-error.log'"

