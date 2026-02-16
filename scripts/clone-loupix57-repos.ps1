# Clone tous les depots GitHub de l'utilisateur loupix57
# Usage : executer dans PowerShell depuis V6 ou DanielCraft

$ErrorActionPreference = "Stop"
$baseDir = if ($PSScriptRoot) { Split-Path $PSScriptRoot } else { "c:\Users\loicDaniel\Documents\DanielCraft" }
$targetDir = Join-Path $baseDir "repos-loupix57"

if (-not (Test-Path $targetDir)) {
    New-Item -ItemType Directory -Path $targetDir | Out-Null
    Write-Host "Dossier cree : $targetDir"
}

$repos = Invoke-RestMethod -Uri "https://api.github.com/users/loupix57/repos?per_page=100"
Write-Host "Nombre de depots a cloner : $($repos.Count)"

foreach ($repo in $repos) {
    $name = $repo.name
    $path = Join-Path $targetDir $name
    if (Test-Path $path) {
        Write-Host "[SKIP] $name (deja present)"
        continue
    }
    $url = $repo.clone_url
    Write-Host "[CLONE] $name ..."
    try {
        git clone --depth 1 $url $path 2>&1 | Out-Null
        Write-Host "  OK : $name"
    } catch {
        Write-Host "  ERREUR : $name - $_"
    }
}

Write-Host "Termine. Depots dans : $targetDir"
