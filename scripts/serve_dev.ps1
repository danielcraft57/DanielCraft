<#
.SYNOPSIS
  Dev local complet : build, URLs propres (blog, prestations…), PHP (/api) et rebuild auto.

.DESCRIPTION
  Remplace l'usage séparé de serve_local.ps1 + dev_php_watch.ps1 :
  - build.py (initial, --no-webp par défaut)
  - serveur PHP avec dist/router.php (pages + API)
  - sync api/ -> dist/api/
  - build.py --watch (optionnel)

.PARAMETER Port
  Port d'écoute (défaut 8000).

.PARAMETER SkipBuild
  Ne pas lancer le build initial.

.PARAMETER NoWatch
  Pas de rebuild automatique (serveur PHP seulement).

.PARAMETER NoKillPort
  Ne pas tuer les processus déjà sur le port.

.PARAMETER WebP
  Activer la génération WebP au build (sinon --no-webp, plus rapide).
  Alias CLI : --webp

.PARAMETER CondaEnv
  Environnement conda à activer avant le build (défaut : danielcraft ou CONDA_ENV).

.EXAMPLE
  .\scripts\serve_dev.ps1
.EXAMPLE
  .\scripts\serve_dev.ps1 -WebP
.EXAMPLE
  .\scripts\serve_dev.ps1 --webp
#>
[CmdletBinding(PositionalBinding = $false)]
param(
  [ValidateRange(1, 65535)]
  [int]$Port = 8000,
  [string]$ServerHost = "127.0.0.1",
  [switch]$SkipBuild,
  [switch]$NoWatch,
  [switch]$NoKillPort,
  [switch]$WebP,
  [string]$CondaEnv = "danielcraft",
  [Parameter(ValueFromRemainingArguments = $true)]
  [string[]]$RemainingArgs
)

foreach ($arg in @($RemainingArgs)) {
  switch -Regex ($arg) {
    '^(--webp|-webp|/webp)$' { $WebP = $true }
    '^(--no-webp|-no-webp|/no-webp)$' { $WebP = $false }
    default { Write-Warning "Argument ignore : $arg" }
  }
}

$buildWebpArgs = if ($WebP) { @() } else { @('--no-webp') }

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

$envFile = Join-Path $root ".env"
if (Test-Path $envFile) {
  . (Join-Path $root "scripts\load_env.ps1")
  Load-EnvFile -EnvPath $envFile
}

if ($env:CONDA_ENV -and $CondaEnv -eq "danielcraft") {
  $CondaEnv = $env:CONDA_ENV
}

try {
  conda activate $CondaEnv 2>$null
} catch {
  Write-Warning "Conda non activé ($CondaEnv) — build Python quand même."
}

$vendorScript = Join-Path $root "scripts\vendor_phpmailer.ps1"
if (Test-Path $vendorScript) {
  & $vendorScript
}

if (-not $SkipBuild) {
  if ($WebP) {
    Write-Host "Build initial (avec WebP)..." -ForegroundColor Cyan
    & python build.py
  } else {
    Write-Host "Build initial (sans WebP)..." -ForegroundColor Cyan
    # Guillemets + --% : evite que PowerShell mange --no-webp
    & python --% build.py --no-webp
  }
  if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}

$distDir = Join-Path $root "dist"
$indexHtml = Join-Path $distDir "index.html"
if (-not (Test-Path $indexHtml)) {
  Write-Error "dist/index.html manquant — relancez sans -SkipBuild."
  exit 1
}

$router = Join-Path $distDir "router.php"
if (-not (Test-Path $router)) {
  Write-Error "dist/router.php manquant — relancez un build (build.py copie scripts/router.php)."
  exit 1
}

$phpExe = $null
try {
  $phpCmd = Get-Command php -ErrorAction SilentlyContinue
  if ($phpCmd) { $phpExe = $phpCmd.Source }
} catch { }

if (-not $phpExe) {
  $pkgRoot = Join-Path $env:LOCALAPPDATA "Microsoft\WinGet\Packages"
  if (Test-Path $pkgRoot) {
    $pkg = Get-ChildItem $pkgRoot -Directory -ErrorAction SilentlyContinue |
      Where-Object { $_.Name -like "PHP.PHP.*" } |
      Sort-Object Name -Descending |
      Select-Object -First 1
    if ($pkg) {
      $candidate = Join-Path $pkg.FullName "php.exe"
      if (Test-Path $candidate) { $phpExe = $candidate }
    }
  }
}

if (-not $phpExe) {
  $laragon = "C:\laragon\bin\php\php.exe"
  if (Test-Path $laragon) { $phpExe = $laragon }
}

if (-not $phpExe) {
  Write-Error "PHP introuvable. Installez PHP (PATH, WinGet ou Laragon) ou utilisez .\scripts\serve_local.ps1 (aperçu statique sans API)."
  exit 1
}

Write-Host ("PHP : " + $phpExe) -ForegroundColor Green

$apiSrcDir = Join-Path $root "api"
$apiDistDir = Join-Path $distDir "api"

function Sync-ApiToDist {
  param([string]$SourceDir, [string]$TargetDir)
  if (-not (Test-Path $SourceDir)) { return }
  if (-not (Test-Path $TargetDir)) {
    New-Item -ItemType Directory -Path $TargetDir -Force | Out-Null
  }
  $null = robocopy $SourceDir $TargetDir *.php /MIR /R:1 /W:1 /NFL /NDL /NJH /NJS /NP
}

if (-not $NoKillPort) {
  $listeners = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue
  if ($listeners) {
    $pids = $listeners | Select-Object -ExpandProperty OwningProcess | Where-Object { $_ } | Sort-Object -Unique
    foreach ($procId in $pids) {
      Write-Host "Libération du port $Port (PID $procId)..." -ForegroundColor Yellow
      Stop-Process -Id $procId -Force -ErrorAction SilentlyContinue | Out-Null
    }
    Start-Sleep -Seconds 1
  }
}

$watchLogPath = Join-Path $root "logs\watch_dev.log"
$watchLogDir = Split-Path -Parent $watchLogPath
if (-not (Test-Path $watchLogDir)) {
  New-Item -ItemType Directory -Path $watchLogDir -Force | Out-Null
}

$baseUrl = "http://${ServerHost}:$Port/"
Write-Host ""
Write-Host "Dev local (PHP + URLs propres + API)" -ForegroundColor Green
Write-Host "  URL         : $baseUrl"
Write-Host "  Nos offres : ${baseUrl}nos-offres"
Write-Host "  Fiches    : ${baseUrl}prestations/<slug>/"
Write-Host "  API         : ${baseUrl}api/ (contact, devis Prestafacture…)"
Write-Host "  Watch build : $(if ($NoWatch) { 'non' } else { 'oui' })"
Write-Host "  Watch log   : $(if ($NoWatch) { 'n/a' } else { $watchLogPath })"
Write-Host "  WebP        : $(if ($WebP) { 'oui' } else { 'non (--no-webp)' })"
Write-Host "  Ctrl+C pour arrêter."
Write-Host ""

Sync-ApiToDist -SourceDir $apiSrcDir -TargetDir $apiDistDir

$routerArg = Join-Path $distDir "router.php"
$server = Start-Process -FilePath $phpExe -ArgumentList @(
  "-S", "${ServerHost}:$Port",
  "-t", $distDir,
  $routerArg
) -NoNewWindow -PassThru

$buildWatch = $null
function Start-BuildWatch {
  $watchArgs = if ($WebP) {
    @("build.py", "--watch")
  } else {
    @("build.py", "--watch", "--no-webp")
  }
  $env:DANIELCRAFT_WATCH_SUPERVISOR = "1"
  return Start-Process -FilePath "python" -ArgumentList $watchArgs -NoNewWindow -PassThru
}

try {
  if (-not $NoWatch) {
    $buildWatch = Start-BuildWatch
  }

  while ($true) {
    # Watch qui quitte (restart build.py code 75, crash) : relancer au lieu de tuer tout le dev
    if ($buildWatch -and $buildWatch.HasExited) {
      $code = $buildWatch.ExitCode
      if ($null -eq $code) { $code = -1 }
      Write-Host "Watch build terminé (code $code) — relance dans 1s..." -ForegroundColor Yellow
      Start-Sleep -Seconds 1
      $buildWatch = Start-BuildWatch
      continue
    }
    Sync-ApiToDist -SourceDir $apiSrcDir -TargetDir $apiDistDir
    Start-Sleep -Seconds 1
  }
} finally {
  if ($buildWatch -and -not $buildWatch.HasExited) {
    Stop-Process -Id $buildWatch.Id -Force -ErrorAction SilentlyContinue | Out-Null
  }
  if ($server -and -not $server.HasExited) {
    Write-Host "Arrêt serveur PHP..." -ForegroundColor Yellow
    Stop-Process -Id $server.Id -Force -ErrorAction SilentlyContinue | Out-Null
  }
}
