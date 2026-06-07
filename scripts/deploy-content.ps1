# Script PowerShell de déploiement CONTENU UNIQUEMENT
# Ne touche PAS à nginx, SSL, ou configuration serveur
# Usage: .\deploy-content.ps1

param(
    # Ne mets pas de valeurs perso en dur ici.
    # Exemple:
    #   .\scripts\deploy-content.ps1 -ServerUser "deploy" -ServerHost "server.local" -ServerPath "/var/www/example.com"
    # Les valeurs par défaut sont injectées depuis .env/.env.local (variables DEPLOY_*).
    # Les paramètres CLI gardent la priorité.
    [string]$ServerUser = "",
    [string]$ServerHost = "",
    [string]$ServerPath = "",
    # Base URL utilisee pendant le build (canoniques, OG, sitemaps).
    # Exemple: -SiteBase "https://ton-domaine.com"
    [string]$SiteBase = "",
    # Nom utilise pour les fichiers de logs nginx (ex: example.com -> /var/log/nginx/example.com-error.log)
    [string]$NginxLogName = "",
    # Optionnel : chemin explicite vers rsync (par ex. C:\cygwin64\bin\rsync.exe)
    [string]$RsyncPath = ""
)

# Configuration
$ErrorActionPreference = "Stop"

# Couleurs pour les messages
function Write-ColorOutput {
    param([string]$Message, [string]$Color = "White")
    Write-Host $Message -ForegroundColor $Color
}

function Import-DotEnvFile {
    param([string]$Path)

    if (-not (Test-Path $Path)) { return }

    Get-Content $Path | ForEach-Object {
        $line = $_.Trim()
        if (-not $line) { return }
        if ($line.StartsWith("#")) { return }

        $idx = $line.IndexOf("=")
        if ($idx -lt 1) { return }

        $key = $line.Substring(0, $idx).Trim()
        $val = $line.Substring($idx + 1).Trim()

        if (-not $key) { return }

        # Strip simple surrounding quotes.
        if (($val.StartsWith('"') -and $val.EndsWith('"')) -or ($val.StartsWith("'") -and $val.EndsWith("'"))) {
            $val = $val.Substring(1, $val.Length - 2)
        }

        # Inject as process env var (non persistant).
        Set-Item -Path ("Env:" + $key) -Value $val
    }
}

function Load-DeployDefaultsFromEnv {
    # Charge .env.local puis .env (priorité au plus local).
    Import-DotEnvFile ".env.local"
    Import-DotEnvFile ".env"

    if (-not $PSBoundParameters.ContainsKey('ServerUser') -or [string]::IsNullOrWhiteSpace($ServerUser)) {
        if ($env:DEPLOY_SERVER_USER) { $script:ServerUser = $env:DEPLOY_SERVER_USER }
    }
    if (-not $PSBoundParameters.ContainsKey('ServerHost') -or [string]::IsNullOrWhiteSpace($ServerHost)) {
        if ($env:DEPLOY_SERVER_HOST) { $script:ServerHost = $env:DEPLOY_SERVER_HOST }
    }
    if (-not $PSBoundParameters.ContainsKey('ServerPath') -or [string]::IsNullOrWhiteSpace($ServerPath)) {
        if ($env:DEPLOY_SERVER_PATH) { $script:ServerPath = $env:DEPLOY_SERVER_PATH }
    }
    if (-not $PSBoundParameters.ContainsKey('SiteBase') -or [string]::IsNullOrWhiteSpace($SiteBase)) {
        if ($env:DEPLOY_SITE_BASE) { $script:SiteBase = $env:DEPLOY_SITE_BASE }
        elseif ($env:SITE_BASE) { $script:SiteBase = $env:SITE_BASE }
    }
    if (-not $PSBoundParameters.ContainsKey('NginxLogName') -or [string]::IsNullOrWhiteSpace($NginxLogName)) {
        if ($env:DEPLOY_NGINX_LOG_NAME) { $script:NginxLogName = $env:DEPLOY_NGINX_LOG_NAME }
    }
    if (-not $PSBoundParameters.ContainsKey('RsyncPath') -or [string]::IsNullOrWhiteSpace($RsyncPath)) {
        if ($env:DEPLOY_RSYNC_PATH) { $script:RsyncPath = $env:DEPLOY_RSYNC_PATH }
    }
}

Load-DeployDefaultsFromEnv

if ([string]::IsNullOrWhiteSpace($ServerUser) -or [string]::IsNullOrWhiteSpace($ServerHost) -or [string]::IsNullOrWhiteSpace($ServerPath)) {
    Write-ColorOutput "Erreur: parametres de deploiement incomplets." "Red"
    Write-ColorOutput "Renseigne DEPLOY_SERVER_USER / DEPLOY_SERVER_HOST / DEPLOY_SERVER_PATH dans .env(.local) ou passe-les en parametres." "Yellow"
    exit 1
}
if ([string]::IsNullOrWhiteSpace($SiteBase)) {
    Write-ColorOutput "Erreur: DEPLOY_SITE_BASE (ou SITE_BASE) manquant." "Red"
    Write-ColorOutput "Ce champ sert au build (canoniques, OG, sitemaps)." "Yellow"
    exit 1
}
if ([string]::IsNullOrWhiteSpace($NginxLogName)) {
    Write-ColorOutput "Erreur: DEPLOY_NGINX_LOG_NAME manquant (nom des logs nginx)." "Red"
    exit 1
}

Write-ColorOutput "=== Deploiement CONTENU - DanielCraft V6 ===" "Green"
Write-ColorOutput "Serveur: ${ServerUser}@${ServerHost}" "Yellow"
Write-ColorOutput "Chemin: ${ServerPath}" "Yellow"
Write-ColorOutput "Base URL (build): ${SiteBase}" "Yellow"
Write-Host ""

# 1. Vérifier que nous sommes dans le bon répertoire
if (-not (Test-Path "build.py")) {
    Write-ColorOutput "Erreur: build.py non trouve. Execute ce script depuis le dossier V6." "Red"
    exit 1
}

# 1.5. Lancer le build Python (toujours avant le transfert, comme dans deploy.ps1)
$DIST_DIR = "dist"
Write-ColorOutput "[0/4] Lancement du build Python..." "Yellow"
$env:SITE_BASE = $SiteBase
$buildLines = & python3 build.py 2>&1
$buildOutput = [string]::Join("`n", $buildLines)
if ($LASTEXITCODE -ne 0) {
    Write-ColorOutput "Erreur lors du build Python:" "Red"
    Write-Host $buildOutput
    exit 1
}
Write-Host $buildOutput
Write-ColorOutput "Build Python termine avec succes" "Green"
Write-Host ""

# 2. Verifier que dist/ existe et contient index.html + placeholder projets
if (-not (Test-Path "$DIST_DIR/index.html")) {
    Write-ColorOutput "Erreur: index.html non trouve dans $DIST_DIR/. Le build a peut-etre echoue." "Red"
    exit 1
}
$placeholderPath = "$DIST_DIR/assets/images/projets/placeholder.svg"
if (-not (Test-Path $placeholderPath)) {
    Write-ColorOutput "Attention: placeholder.svg absent dans $DIST_DIR/assets/images/projets/" "Yellow"
    Write-ColorOutput "Les vignettes projet afficheront un fond rouge. Copie du source si possible..." "Yellow"
    $srcPlaceholder = "assets/images/projets/placeholder.svg"
    if (Test-Path $srcPlaceholder) {
        $projetsDir = "$DIST_DIR/assets/images/projets"
        if (-not (Test-Path $projetsDir)) { New-Item -ItemType Directory -Path $projetsDir -Force | Out-Null }
        Copy-Item $srcPlaceholder -Destination $placeholderPath -Force
        Write-ColorOutput "  -> placeholder.svg copie dans dist" "Green"
    }
}

# 2. Lister les fichiers à déployer depuis dist/
Write-ColorOutput "[1/4] Verification des fichiers dans $DIST_DIR/..." "Yellow"
$filesToDeploy = @(
    "$DIST_DIR/index.html",
    "$DIST_DIR/autres-prestations.html",
    "$DIST_DIR/processus.html",
    "$DIST_DIR/metz.html",
    "$DIST_DIR/portfolio.html",
    "$DIST_DIR/projets.html",
    "$DIST_DIR/statistiques.html",
    "$DIST_DIR/analyse.html",
    "$DIST_DIR/audit.html",
    "$DIST_DIR/desabonnement.html",
    "$DIST_DIR/mentions-legales.html",
    "$DIST_DIR/cgv.html",
    "$DIST_DIR/cgu.html",
    "$DIST_DIR/politique-confidentialite.html",
    "$DIST_DIR/robots.txt",
    "$DIST_DIR/sitemap.xml",
    "$DIST_DIR/sitemap-pages.xml",
    "$DIST_DIR/sitemap-vitrines.xml",
    "$DIST_DIR/blog/sitemap-blog.xml",
    "$DIST_DIR/assets",
    "$DIST_DIR/api",
    "$DIST_DIR/blog",
    "$DIST_DIR/projets",
    "$DIST_DIR/vitrines"
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
$createDirCmd = "mkdir -p $ServerPath && mkdir -p $ServerPath/assets && mkdir -p $ServerPath/assets/images/projets && mkdir -p $ServerPath/assets/images/hero && mkdir -p $ServerPath/api && mkdir -p $ServerPath/blog && mkdir -p $ServerPath/projets && mkdir -p $ServerPath/vitrines"
try {
    ssh "${ServerUser}@${ServerHost}" $createDirCmd
    Write-ColorOutput "Repertoire cree/verifie (dont assets/images/projets et assets/images/hero pour les images)" "Green"
} catch {
    Write-ColorOutput "Erreur lors de la creation du repertoire: $_" "Red"
    exit 1
}

# Fonction utilitaire pour comparer la taille locale et distante d'un fichier
function Should-TransferFile {
    param(
        [string]$LocalPath,
        [string]$RemotePath
    )

    if (-not (Test-Path $LocalPath)) {
        return $false
    }

    $localSize = (Get-Item $LocalPath).Length

    # Récupère la taille distante (en octets) sans pipe
    $remoteCmd = "if [ -f '$RemotePath' ]; then stat -c %s '$RemotePath'; else echo 0; fi"
    $remoteSizeRaw = ssh "${ServerUser}@${ServerHost}" $remoteCmd

    # Si ssh échoue, on renvoie true pour forcer le transfert
    if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($remoteSizeRaw)) {
        return $true
    }

    $remoteSizeRaw = $remoteSizeRaw.Trim()
    [long]$remoteSize = 0
    [void][long]::TryParse($remoteSizeRaw, [ref]$remoteSize)

    return ($localSize -ne $remoteSize)
}

# 4. Transférer les fichiers avec rsync (ou scp en fallback)
Write-ColorOutput "[3/4] Transfert des fichiers..." "Yellow"

# Exclusions (le blog est dans dist/blog/ et est deploye)
$excludes = @(
    "--exclude=node_modules",
    "--exclude=.git",
    "--exclude=docs",
    "--exclude=scripts",
    "--exclude=src",
    "--exclude=build.py",
    "--exclude=.gitignore",
    "--exclude=README.md"
)

$excludeArgs = $excludes -join " "

# Vérifier si rsync est disponible (via RsyncPath explicite ou via PATH)
try {
    if ($RsyncPath -and (Test-Path $RsyncPath)) {
        $rsyncExe = $RsyncPath
    } else {
        $rsyncCmd = Get-Command rsync -ErrorAction Stop
        $rsyncExe = $rsyncCmd.Source
    }

    Write-ColorOutput "Utilisation de rsync (transfert optimise)..." "Yellow"
    
    $rsyncCommandLine = "`"$rsyncExe`" -avz --delete $excludeArgs $DIST_DIR/ ${ServerUser}@${ServerHost}:${ServerPath}/"
    Invoke-Expression $rsyncCommandLine
    
    if ($LASTEXITCODE -eq 0) {
        Write-ColorOutput "Transfert rsync reussi" "Green"
    } else {
        Write-ColorOutput "Erreur lors du transfert rsync" "Red"
        exit 1
    }
} catch {
    Write-ColorOutput "rsync non trouve, fallback scp (optimise par taille)..." "Yellow"
    
    # Transfert fichier par fichier avec scp depuis dist/
    $htmlFiles = @(
        "index.html",
        "autres-prestations.html",
        "processus.html",
        "metz.html",
        "portfolio.html",
        "projets.html",
        "statistiques.html",
        "analyse.html",
        "audit.html",
        "desabonnement.html",
        "mentions-legales.html",
        "cgv.html",
        "cgu.html",
        "politique-confidentialite.html"
    )
    $otherFiles = @("robots.txt", "sitemap.xml", "sitemap-pages.xml", "sitemap-vitrines.xml", "sitemap-prestations.xml")
    
    foreach ($file in $htmlFiles) {
        $filePath = Join-Path $DIST_DIR $file
        $remotePath = "$ServerPath/$file"
        if ((Test-Path $filePath) -and (Should-TransferFile -LocalPath $filePath -RemotePath $remotePath)) {
            Write-Host "  Transfert (modifie): $file"
            scp $filePath "${ServerUser}@${ServerHost}:${ServerPath}/"
        } else {
            Write-Host "  Skip (inchangé): $file"
        }
    }
    
    foreach ($file in $otherFiles) {
        $filePath = Join-Path $DIST_DIR $file
        $remotePath = "$ServerPath/$file"
        if ((Test-Path $filePath) -and (Should-TransferFile -LocalPath $filePath -RemotePath $remotePath)) {
            Write-Host "  Transfert (modifie): $file"
            scp $filePath "${ServerUser}@${ServerHost}:${ServerPath}/"
        } else {
            Write-Host "  Skip (inchangé): $file"
        }
    }
    
    # Transfert du dossier assets (toujours complet en fallback, plus simple que comparer fichier par fichier)
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

    # Transfert du blog (index, articles, series, sitemap-blog)
    $blogPath = Join-Path $DIST_DIR "blog"
    if (Test-Path $blogPath) {
        Write-Host "  Transfert: blog/"
        scp -r $blogPath "${ServerUser}@${ServerHost}:${ServerPath}/"
    }

    # Sitemap blog (référencé par sitemap.xml ; explicite pour le fallback SCP)
    $blogSitemapPath = Join-Path $DIST_DIR "blog/sitemap-blog.xml"
    if (Test-Path $blogSitemapPath) {
        $remoteBlogSitemap = "$ServerPath/blog/sitemap-blog.xml"
        if (Should-TransferFile -LocalPath $blogSitemapPath -RemotePath $remoteBlogSitemap) {
            Write-Host "  Transfert (modifie): blog/sitemap-blog.xml"
            scp $blogSitemapPath "${ServerUser}@${ServerHost}:${ServerPath}/blog/"
        } else {
            Write-Host "  Skip (inchangé): blog/sitemap-blog.xml"
        }
    }

    # Transfert des pages projet (projets/<slug>.html)
    $projetsPath = Join-Path $DIST_DIR "projets"
    if (Test-Path $projetsPath) {
        Write-Host "  Transfert: projets/"
        scp -r $projetsPath "${ServerUser}@${ServerHost}:${ServerPath}/"
    }

    # Transfert vitrines (hub, demos, captures, fiches)
    $vitrinesPath = Join-Path $DIST_DIR "vitrines"
    if (Test-Path $vitrinesPath) {
        Write-Host "  Transfert: vitrines/"
        scp -r $vitrinesPath "${ServerUser}@${ServerHost}:${ServerPath}/"
    }

    # Transfert fiches prestations (/prestations/<slug>/)
    $prestationsPath = Join-Path $DIST_DIR "prestations"
    if (Test-Path $prestationsPath) {
        Write-Host "  Transfert: prestations/"
        scp -r $prestationsPath "${ServerUser}@${ServerHost}:${ServerPath}/"
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

# Verifier que le blog est deploye
$blogCheckCmd = "test -f $ServerPath/blog/index.html && echo 'OK: blog/index.html present' || echo 'ATTENTION: blog manquant - relancer build.py puis deploy'"
$blogCheckResult = ssh "${ServerUser}@${ServerHost}" $blogCheckCmd
Write-Host $blogCheckResult

$blogSitemapCheckCmd = "test -f $ServerPath/blog/sitemap-blog.xml && echo 'OK: blog/sitemap-blog.xml present' || echo 'ATTENTION: blog/sitemap-blog.xml manquant (SEO / index sitemap)'"
$blogSitemapCheckResult = ssh "${ServerUser}@${ServerHost}" $blogSitemapCheckCmd
Write-Host $blogSitemapCheckResult

# Verifier que les pages projet sont deployees
$projetsCheckCmd = 'test -d ' + $ServerPath + '/projets && (n=$(ls -1 ' + $ServerPath + '/projets/*.html 2>/dev/null | wc -l); echo "OK: projets/ deploye ($n pages)") || echo ''ATTENTION: projets/ manquant - relancer build puis deploy'''
$projetsCheckResult = ssh "${ServerUser}@${ServerHost}" $projetsCheckCmd
Write-Host $projetsCheckResult

# Verifier dist/vitrines (hub + fiches + demos)
$vitrinesCheckCmd = 'test -f ' + $ServerPath + '/vitrines/index.html && echo "OK: vitrines/index.html present" || echo "ATTENTION: vitrines/ manquant - relancer build puis deploy"'
$vitrinesCheckResult = ssh "${ServerUser}@${ServerHost}" $vitrinesCheckCmd
Write-Host $vitrinesCheckResult

$prestationsCheckCmd = 'test -f ' + $ServerPath + '/prestations/site-vitrine/index.html && echo "OK: prestations/ deploye" || echo "ATTENTION: prestations/ manquant - relancer build puis deploy"'
$prestationsCheckResult = ssh "${ServerUser}@${ServerHost}" $prestationsCheckCmd
Write-Host $prestationsCheckResult

# Verifier assets/images/projets (placeholder.svg requis pour les vignettes)
$imagesProjetsCmd = 'if test -d ' + $ServerPath + '/assets/images/projets; then echo "Contenu:"; ls -la ' + $ServerPath + '/assets/images/projets/ 2>/dev/null; if test -f ' + $ServerPath + '/assets/images/projets/placeholder.svg; then echo "OK: placeholder.svg present (vignettes projet)"; else echo "ATTENTION: placeholder.svg manquant - ajoute-le pour eviter les blocs rouges"; fi; else echo "ATTENTION: assets/images/projets manquant"; fi'
$imagesProjetsResult = ssh "${ServerUser}@${ServerHost}" $imagesProjetsCmd
Write-Host $imagesProjetsResult

# Vérifier que les images du hero sont présentes (assets/images/hero)
$imagesHeroCmd = 'if test -d ' + $ServerPath + '/assets/images/hero; then n=$(ls -1 ' + $ServerPath + '/assets/images/hero/*.{png,jpg,jpeg} 2>/dev/null | wc -l); echo "OK: assets/images/hero present ($n images)"; else echo "ATTENTION: assets/images/hero manquant (mockups hero)"; fi'
$imagesHeroResult = ssh "${ServerUser}@${ServerHost}" $imagesHeroCmd
Write-Host $imagesHeroResult

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
Write-Host "ssh ${ServerUser}@${ServerHost} 'sudo tail -f /var/log/nginx/${NginxLogName}-error.log'"

