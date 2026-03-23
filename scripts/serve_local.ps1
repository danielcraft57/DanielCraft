# Prévisualisation locale : sert la RACINE du site = dossier dist/
# (obligatoire : les URLs commencent par /assets/...)

$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

# Charger .env (si présent) pour SITE_BASE, etc.
$envFile = Join-Path $root ".env"
if (Test-Path $envFile) {
  . (Join-Path $root "scripts\\load_env.ps1")
  Load-EnvFile -EnvPath $envFile
}

Write-Host "Build rapide (sans WebP)..." -ForegroundColor Cyan
python build.py --no-webp
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host ""
Write-Host "Serveur : http://localhost:8000/" -ForegroundColor Green
Write-Host "Ne pas utiliser http://localhost:8000/dist/ si le serveur est lance depuis la racine du repo." -ForegroundColor Yellow
Write-Host ""

python -m http.server 8000 --directory dist
