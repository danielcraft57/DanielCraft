# Script PowerShell de déploiement CONTENU UNIQUEMENT
# Ne touche PAS à nginx, SSL, ou configuration serveur
# Usage: .\deploy-content.ps1

param(
    [string]$ServerUser = "pi",
    [string]$ServerHost = "node12.lan",
    [string]$ServerPath = "/var/www/danielcraft.fr"
)

# Configuration
$ErrorActionPreference = "Stop"

# Couleurs pour les messages
function Write-ColorOutput {
    param([string]$Message, [string]$Color = "White")
    Write-Host $Message -ForegroundColor $Color
}

Write-ColorOutput "=== Deploiement CONTENU - DanielCraft V6 ===" "Green"
Write-ColorOutput "Serveur: ${ServerUser}@${ServerHost}" "Yellow"
Write-ColorOutput "Chemin: ${ServerPath}" "Yellow"
Write-Host ""

# 1. Vérifier que nous sommes dans le bon répertoire
if (-not (Test-Path "build.py")) {
    Write-ColorOutput "Erreur: build.py non trouve. Execute ce script depuis le dossier V6." "Red"
    exit 1
}

# 1.5. Lancer le build Python (toujours avant le transfert, comme dans deploy.ps1)
$DIST_DIR = "dist"
Write-ColorOutput "[0/4] Lancement du build Python..." "Yellow"
$buildOutput = python3 build.py 2>&1 | Out-String
if ($LASTEXITCODE -ne 0) {
    Write-ColorOutput "Erreur lors du build Python:" "Red"
    Write-Host $buildOutput
    exit 1
}
Write-Host $buildOutput
Write-ColorOutput "Build Python termine avec succes" "Green"
Write-Host ""

# 2. Vérifier que dist/ existe et contient index.html
if (-not (Test-Path "$DIST_DIR/index.html")) {
    Write-ColorOutput "Erreur: index.html non trouve dans $DIST_DIR/. Le build a peut-etre echoue." "Red"
    exit 1
}

# 2. Lister les fichiers à déployer depuis dist/
Write-ColorOutput "[1/4] Verification des fichiers dans $DIST_DIR/..." "Yellow"
$filesToDeploy = @(
    "$DIST_DIR/index.html",
    "$DIST_DIR/processus.html",
    "$DIST_DIR/metz.html",
    "$DIST_DIR/portfolio.html",
    "$DIST_DIR/projets.html",
    "$DIST_DIR/statistiques.html",
    "$DIST_DIR/mentions-legales.html",
    "$DIST_DIR/cgv.html",
    "$DIST_DIR/cgu.html",
    "$DIST_DIR/politique-confidentialite.html",
    "$DIST_DIR/robots.txt",
    "$DIST_DIR/sitemap.xml",
    "$DIST_DIR/assets",
    "$DIST_DIR/api"
)

$missingFiles = @()
foreach ($file in $filesToDeploy) {
    if (-not (Test-Path $file)) {
        $missingFiles += $file
    }
}

if ($missingFiles.Count -gt 0) {
    Write-ColorOutput "Attention: Fichiers manquants:" "Yellow"
    $missingFiles | ForEach-Object { Write-Host "  - $_" }
    $response = Read-Host "Continuer quand meme ? (o/N)"
    if ($response -notmatch "^[Oo]$") {
        exit 1
    }
}

# 3. Créer le répertoire sur le serveur si nécessaire
Write-ColorOutput "[2/4] Creation du repertoire sur le serveur (si necessaire)..." "Yellow"
$createDirCmd = "mkdir -p $ServerPath && mkdir -p $ServerPath/assets && mkdir -p $ServerPath/api"
try {
    ssh "${ServerUser}@${ServerHost}" $createDirCmd
    Write-ColorOutput "Repertoire cree/verifie" "Green"
} catch {
    Write-ColorOutput "Erreur lors de la creation du repertoire: $_" "Red"
    exit 1
}

# 4. Transférer les fichiers avec rsync (ou scp en fallback)
Write-ColorOutput "[3/4] Transfert des fichiers..." "Yellow"

# Exclusions
$excludes = @(
    "--exclude=node_modules",
    "--exclude=.git",
    "--exclude=docs",
    "--exclude=scripts",
    "--exclude=src",
    "--exclude=build.py",
    "--exclude=.gitignore",
    "--exclude=README.md",
    "--exclude=blog"
)

$excludeArgs = $excludes -join " "

# Vérifier si rsync est disponible
try {
    $rsyncCheck = Get-Command rsync -ErrorAction Stop
    Write-ColorOutput "Utilisation de rsync (transfert optimise)..." "Yellow"
    
    $rsyncCmd = "rsync -avz --delete $excludeArgs $DIST_DIR/ ${ServerUser}@${ServerHost}:${ServerPath}/"
    Invoke-Expression $rsyncCmd
    
    if ($LASTEXITCODE -eq 0) {
        Write-ColorOutput "Transfert rsync reussi" "Green"
    } else {
        Write-ColorOutput "Erreur lors du transfert rsync" "Red"
        exit 1
    }
} catch {
    Write-ColorOutput "rsync non trouve, utilisation de scp (plus lent)..." "Yellow"
    
    # Transfert fichier par fichier avec scp depuis dist/
    $htmlFiles = @(
        "index.html", 
        "processus.html", 
        "metz.html", 
        "portfolio.html", 
        "projets.html", 
        "statistiques.html",
        "mentions-legales.html",
        "cgv.html",
        "cgu.html",
        "politique-confidentialite.html"
    )
    $otherFiles = @("robots.txt", "sitemap.xml")
    
    foreach ($file in $htmlFiles) {
        $filePath = Join-Path $DIST_DIR $file
        if (Test-Path $filePath) {
            Write-Host "  Transfert: $file"
            scp $filePath "${ServerUser}@${ServerHost}:${ServerPath}/"
        }
    }
    
    foreach ($file in $otherFiles) {
        $filePath = Join-Path $DIST_DIR $file
        if (Test-Path $filePath) {
            Write-Host "  Transfert: $file"
            scp $filePath "${ServerUser}@${ServerHost}:${ServerPath}/"
        }
    }
    
    # Transfert du dossier assets
    $assetsPath = Join-Path $DIST_DIR "assets"
    if (Test-Path $assetsPath) {
        Write-Host "  Transfert: assets/ (peut prendre du temps...)"
        scp -r $assetsPath "${ServerUser}@${ServerHost}:${ServerPath}/"
    }

    # Transfert du dossier api (formulaire contact PHP)
    $apiPath = Join-Path $DIST_DIR "api"
    if (Test-Path $apiPath) {
        Write-Host "  Transfert: api/"
        scp -r $apiPath "${ServerUser}@${ServerHost}:${ServerPath}/"
    }
    
    Write-ColorOutput "Transfert scp termine" "Green"
}

# 5. Configurer les permissions (sans sudo, juste les permissions de base)
Write-ColorOutput "[4/4] Configuration des permissions..." "Yellow"
$permissionsCmd = "chmod -R 755 $ServerPath && find $ServerPath -type f -exec chmod 644 {} ';' && find $ServerPath -type d -exec chmod 755 {} ';'"
try {
    ssh "${ServerUser}@${ServerHost}" $permissionsCmd
    Write-ColorOutput "Permissions configurees" "Green"
} catch {
    Write-ColorOutput "Attention: Erreur lors de la configuration des permissions" "Yellow"
    Write-ColorOutput "Si nginx ne peut pas lire les fichiers, execute manuellement:" "Yellow"
    Write-Host "ssh ${ServerUser}@${ServerHost} 'sudo chown -R ${ServerUser}:www-data $ServerPath && sudo chmod -R 755 $ServerPath'"
}

# 6. Vérification finale
Write-Host ""
Write-ColorOutput "=== Verification finale ===" "Yellow"

# Vérifier que index.html est accessible
$checkCmd = "test -f $ServerPath/index.html && echo 'OK: index.html present' || echo 'ERREUR: index.html manquant'"
$checkResult = ssh "${ServerUser}@${ServerHost}" $checkCmd
Write-Host $checkResult

# Vérifier que api/send-contact.php est présent (formulaire contact)
$apiCheckCmd = "test -f $ServerPath/api/send-contact.php && echo 'OK: api/send-contact.php present' || echo 'ATTENTION: api/send-contact.php manquant (formulaire contact)'"
$apiCheckResult = ssh "${ServerUser}@${ServerHost}" $apiCheckCmd
Write-Host $apiCheckResult

# Lister les fichiers déployés
$listCmd = "ls -lh $ServerPath/*.html 2>/dev/null | wc -l"
$fileCount = (ssh "${ServerUser}@${ServerHost}" $listCmd).Trim()
Write-Host "Fichiers HTML deployes: $fileCount"

Write-Host ""
Write-ColorOutput "=== Deploiement contenu termine ! ===" "Green"
Write-ColorOutput "Les fichiers ont ete transferes sur le serveur." "Green"
Write-Host ""
Write-ColorOutput "Note: Ce script ne touche PAS a nginx." "Yellow"
Write-ColorOutput "Si tu veux recharger nginx (sans modifier la config):" "Yellow"
Write-Host "ssh ${ServerUser}@${ServerHost} 'sudo systemctl reload nginx'"
Write-Host ""
Write-ColorOutput "Pour verifier les logs d'erreur nginx:" "Yellow"
Write-Host "ssh ${ServerUser}@${ServerHost} 'sudo tail -f /var/log/nginx/danielcraft.fr-error.log'"

