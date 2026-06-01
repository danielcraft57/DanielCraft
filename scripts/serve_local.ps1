<#
.SYNOPSIS
  Build le site dans dist/ et sert ce dossier en HTTP (prévisualisation locale).

.DESCRIPTION
  La racine du site servie est dist/. Ouvrez http://localhost:<Port>/ (sans /dist/).
  Ne pas ouvrir src/pages/*.html dans le navigateur : les {% include %} ne sont pas résolus hors build.

.PARAMETER Port
  Port d'écoute (défaut 8000).

.PARAMETER SkipBuild
  Ne pas exécuter build.py (réutilise le contenu actuel de dist/).
#>
[CmdletBinding()]
param(
  [ValidateRange(1, 65535)]
  [int]$Port = 8000,
  [switch]$SkipBuild
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

$dist = Join-Path $root "dist"
$indexHtml = Join-Path $dist "index.html"

# Charger .env (si présent) pour SITE_BASE, etc.
$envFile = Join-Path $root ".env"
if (Test-Path $envFile) {
  . (Join-Path $root "scripts\load_env.ps1")
  Load-EnvFile -EnvPath $envFile
}

if (-not $SkipBuild) {
  Write-Host "Build rapide (sans WebP)..." -ForegroundColor Cyan
  python build.py --no-webp
  if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}
else {
  Write-Host "[SkipBuild] build.py ignore — utilisation de dist/ tel quel." -ForegroundColor Yellow
}

if (-not (Test-Path $indexHtml)) {
  Write-Error "Fichier manquant : $indexHtml — lancez sans -SkipBuild pour générer dist/."
  exit 1
}

$indexRaw = Get-Content -LiteralPath $indexHtml -Raw -Encoding UTF8
if ($indexRaw -match '\{%\s*include') {
  Write-Warning "dist/index.html contient encore des directives {% include %}. Relancez un build complet ou vérifiez build.py."
}

# http.server --directory nécessite Python 3.7+
$pyOk = $true
python -c "import sys; raise SystemExit(0 if sys.version_info >= (3, 7) else 1)" 2>$null
if ($LASTEXITCODE -ne 0) {
  $pyOk = $false
}

$baseUrl = "http://localhost:$Port/"
Write-Host ""
Write-Host "Prévisualisation locale" -ForegroundColor Green
Write-Host "  URL       : $baseUrl"
Write-Host "  Racine HTTP : $dist (chemins /assets/..., /vitrines/...)"
Write-Host "  Ctrl+C pour arrêter le serveur."
Write-Host ""

if ($pyOk) {
  # URLs blog /blog/articles/slug sans .html (comme en prod avec réécriture)
  python (Join-Path $root "scripts\blog_dev_server.py") $Port --directory dist
}
else {
  Write-Warning "Python < 3.7 : serveur lancé depuis le dossier dist/ (sans --directory)."
  Push-Location $dist
  try {
    python -m http.server $Port
  }
  finally {
    Pop-Location
  }
}
