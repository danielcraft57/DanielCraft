<#
.SYNOPSIS
  Prévisualisation locale du site (dist/).

.DESCRIPTION
  Par défaut, délègue à serve_dev.ps1 (PHP + URLs propres + API + watch).
  Avec -StaticOnly : serveur Python uniquement (sans PHP / sans formulaires).

.PARAMETER Port
  Port d'écoute (défaut 8000).

.PARAMETER SkipBuild
  Ne pas exécuter build.py au démarrage.

.PARAMETER StaticOnly
  Aperçu statique Python (blog sans .html) — pas d'API PHP.

.PARAMETER NoWatch
  Pas de rebuild automatique (transmis à serve_dev.ps1).
#>
[CmdletBinding()]
param(
  [ValidateRange(1, 65535)]
  [int]$Port = 8000,
  [switch]$SkipBuild,
  [switch]$StaticOnly,
  [switch]$NoWatch
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

if (-not $StaticOnly) {
  $devScript = Join-Path $PSScriptRoot "serve_dev.ps1"
  $devArgs = @("-Port", $Port)
  if ($SkipBuild) { $devArgs += "-SkipBuild" }
  if ($NoWatch) { $devArgs += "-NoWatch" }
  & $devScript @devArgs
  exit $LASTEXITCODE
}

# --- Mode statique Python (legacy) ---
$dist = Join-Path $root "dist"
$indexHtml = Join-Path $dist "index.html"

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

if (-not (Test-Path $indexHtml)) {
  Write-Error "Fichier manquant : $indexHtml — lancez sans -SkipBuild."
  exit 1
}

Write-Host ""
Write-Host "Prévisualisation statique (Python — sans API PHP)" -ForegroundColor Yellow
Write-Host "  URL : http://localhost:$Port/"
Write-Host "  Pour contact/devis : .\scripts\serve_dev.ps1"
Write-Host ""

python (Join-Path $root "scripts\blog_dev_server.py") $Port --directory dist
