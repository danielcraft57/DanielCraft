# Dév local : active conda, lance PHP server sur dist, puis build watch.
# Sert à tester l'endpoint PHP (/api/send-contact.php) en local.

param(
  [string]$CondaEnv = "danielcraft",
  [string]$ServerHost = "127.0.0.1",
  [int]$ServerPort = 8000,
  # Par défaut, on tue tout ce qui écoute sur le port pour éviter les conflits.
  [switch]$NoKillPort
)

$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

# Charger .env (si présent)
$envFile = Join-Path $root ".env"
if (Test-Path $envFile) {
  . (Join-Path $root "scripts\\load_env.ps1")
  Load-EnvFile -EnvPath $envFile
}

# Assurer le vendor PHPMailer (sans composer)
$vendorScript = Join-Path $root "scripts\\vendor_phpmailer.ps1"
if (Test-Path $vendorScript) {
  & $vendorScript
}

# Laisser la config .env piloter par défaut
if ($env:CONDA_ENV -and $CondaEnv -eq "danielcraft") {
  $CondaEnv = $env:CONDA_ENV
}

Write-Host "Activation conda: $CondaEnv" -ForegroundColor Cyan
try {
  conda activate $CondaEnv 2>$null
} catch {
  Write-Error "Impossible d'activer conda. Vérifie que 'conda' est bien initialisé dans ta session PowerShell."
  exit 1
}

Write-Host "Build initial (sans WebP)..." -ForegroundColor Cyan
python build.py --no-webp
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

$phpExe = $null
try {
  $phpCmd = Get-Command php -ErrorAction SilentlyContinue
  if ($phpCmd) { $phpExe = $phpCmd.Source }
} catch {
  $phpExe = $null
}

# Fallback WinGet (installation type php via winget)
if (-not $phpExe) {
  $pkgRoot = Join-Path $env:LOCALAPPDATA "Microsoft\\WinGet\\Packages"
  if (Test-Path $pkgRoot) {
    $pkg = Get-ChildItem $pkgRoot -Directory -ErrorAction SilentlyContinue |
      Where-Object { $_.Name -like "PHP.PHP.*" } |
      Sort-Object Name -Descending |
      Select-Object -First 1

    if ($pkg) {
      $candidate = Join-Path $pkg.FullName "php.exe"
      if (Test-Path $candidate) {
        $phpExe = $candidate
      }
    }
  }
}

# Fallback Laragon (si présent)
if (-not $phpExe) {
  $laragonCandidate = "C:\laragon\bin\php\php.exe"
  if (Test-Path $laragonCandidate) {
    $phpExe = $laragonCandidate
  }
}

if (-not $phpExe) {
  Write-Error "PHP introuvable. Installe PHP et assure-toi que 'php' est dans le PATH, ou vérifie l'installation WinGet (php.exe sous %LOCALAPPDATA%\\Microsoft\\WinGet\\Packages\\PHP.PHP.*\\php.exe)."
  exit 1
}

$phpExeNorm = $phpExe
Write-Host ("PHP détecté : " + $phpExeNorm) -ForegroundColor Green

$phpDir = Split-Path -Parent $phpExeNorm
$phpIni = Join-Path $phpDir "php.ini"
$phpIniDev = Join-Path $phpDir "php.ini-development"

# Assurer une config PHP locale avec OpenSSL activé (requis pour SMTP TLS/587).
if (-not (Test-Path $phpIni) -and (Test-Path $phpIniDev)) {
  Copy-Item -Path $phpIniDev -Destination $phpIni -Force
}
if (Test-Path $phpIni) {
  $iniText = Get-Content -Path $phpIni -Raw -ErrorAction SilentlyContinue
  if ($null -eq $iniText) { $iniText = "" }
  # extension_dir
  $iniText = [regex]::Replace($iniText, '^[;#\s]*extension_dir\s*=.*$', 'extension_dir = "ext"', [System.Text.RegularExpressions.RegexOptions]::Multiline)
  if ($iniText -notmatch '(?m)^\s*extension_dir\s*=') {
    $iniText += "`r`nextension_dir = `"ext`"`r`n"
  }
  # openssl extension (uncomment / add)
  $iniText = [regex]::Replace($iniText, '^[;#\s]*extension\s*=\s*openssl\s*$', 'extension=openssl', [System.Text.RegularExpressions.RegexOptions]::Multiline)
  if ($iniText -notmatch '(?m)^\s*extension\s*=\s*openssl\s*$') {
    $iniText += "`r`nextension=openssl`r`n"
  }
  Set-Content -Path $phpIni -Value $iniText -Encoding UTF8
}

# Vérifier que l'extension openssl est bien chargée
$opensslLoaded = $false
try {
  $opensslCheck = & $phpExeNorm -c $phpDir -m 2>$null
  if ($opensslCheck -match '(?im)^openssl$') {
    $opensslLoaded = $true
  }
} catch {
  $opensslLoaded = $false
}
if ($opensslLoaded) {
  Write-Host "PHP OpenSSL: OK" -ForegroundColor Green
} else {
  Write-Host "PHP OpenSSL: non chargé (les emails TLS risquent d'échouer)." -ForegroundColor Yellow
}

$distDir = Join-Path $root "dist"
if (-not (Test-Path $distDir)) {
  Write-Error "Le dossier dist/ est introuvable ($distDir). Lance d'abord un build."
  exit 1
}

$apiSrcDir = Join-Path $root "api"
$apiDistDir = Join-Path $distDir "api"
if (-not (Test-Path $apiDistDir)) {
  New-Item -ItemType Directory -Path $apiDistDir -Force | Out-Null
}

function Sync-ApiToDist {
  param(
    [string]$SourceDir,
    [string]$TargetDir
  )
  if (-not (Test-Path $SourceDir)) { return }
  # /MIR = inclut créations, modifs et suppressions.
  # /NFL /NDL /NJH /NJS /NP réduisent fortement le bruit terminal.
  $null = robocopy $SourceDir $TargetDir *.php /MIR /R:1 /W:1 /NFL /NDL /NJH /NJS /NP
}

if (-not $NoKillPort) {
  $listeners = Get-NetTCPConnection -LocalPort $ServerPort -State Listen -ErrorAction SilentlyContinue
  if ($listeners) {
    $pids = $listeners | Select-Object -ExpandProperty OwningProcess | Where-Object { $_ -ne $null } | Sort-Object -Unique
    if ($pids) {
      Write-Host ("KillPort: arrêt des processus sur port " + $ServerPort + " : " + ($pids -join ", ")) -ForegroundColor Yellow
      foreach ($procId in $pids) {
        Stop-Process -Id $procId -Force -ErrorAction SilentlyContinue | Out-Null
      }
      # Petite boucle pour laisser le temps au système de libérer le port.
      for ($i = 0; $i -lt 10; $i++) {
        Start-Sleep -Milliseconds 250
        if (-not (Test-NetConnection -ComputerName $ServerHost -Port $ServerPort -InformationLevel Quiet)) {
          break
        }
      }
    }
  }
}

if (Test-NetConnection -ComputerName $ServerHost -Port $ServerPort -InformationLevel Quiet) {
  Write-Error "Le port $ServerPort est encore utilisé sur $ServerHost après KillPort. Arrête manuellement et relance."
  exit 1
}

Write-Host "Lancement serveur PHP: http://$ServerHost`:$ServerPort" -ForegroundColor Green
$server = Start-Process -FilePath $phpExe -ArgumentList @("-c", $phpDir, "-S", "$ServerHost`:$ServerPort", "-t", $distDir) -NoNewWindow -PassThru

try {
  Write-Host "Sync API initiale -> dist/api..." -ForegroundColor Cyan
  Sync-ApiToDist -SourceDir $apiSrcDir -TargetDir $apiDistDir

  Write-Host "Build watch + sync API (Ctrl+C pour stopper)..." -ForegroundColor Cyan
  $buildWatch = Start-Process -FilePath "python" -ArgumentList @("build.py", "--watch") -NoNewWindow -PassThru

  while (-not $buildWatch.HasExited) {
    Sync-ApiToDist -SourceDir $apiSrcDir -TargetDir $apiDistDir
    Start-Sleep -Seconds 1
  }

  if ($buildWatch.ExitCode -ne 0) {
    exit $buildWatch.ExitCode
  }
} finally {
  if ($buildWatch -and -not $buildWatch.HasExited) {
    Stop-Process -Id $buildWatch.Id -Force -ErrorAction SilentlyContinue | Out-Null
  }
  if ($server -and -not $server.HasExited) {
    Write-Host "Arrêt serveur PHP..." -ForegroundColor Yellow
    Stop-Process -Id $server.Id -Force | Out-Null
  }
}

