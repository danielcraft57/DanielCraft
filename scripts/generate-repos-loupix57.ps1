# Genere assets/data/repos-loupix57.json a partir de l'API GitHub (compte loupix57).
# Usage: .\scripts\generate-repos-loupix57.ps1
# Execute depuis la racine du projet DanielCraftFr.

$ErrorActionPreference = "Stop"
$apiUrl = "https://api.github.com/users/loupix57/repos?per_page=100&sort=updated"
$outDir = "assets\data"
$outFile = "assets\data\repos-loupix57.json"

if (-not (Test-Path $outDir)) {
    New-Item -ItemType Directory -Path $outDir -Force
}

Write-Host "Recuperation des depots GitHub loupix57..."
try {
    $repos = Invoke-RestMethod -Uri $apiUrl -Method Get -Headers @{
        "Accept" = "application/vnd.github.v3+json"
        "User-Agent" = "DanielCraftFr-Build"
    }
} catch {
    Write-Host "Erreur API GitHub: $_" -ForegroundColor Red
    exit 1
}

$simplified = $repos | ForEach-Object {
    [PSCustomObject]@{
        name         = $_.name
        full_name    = $_.full_name
        description  = $_.description
        language     = $_.language
        html_url     = $_.html_url
        clone_url    = $_.clone_url
        updated_at   = $_.updated_at
        created_at   = $_.created_at
        pushed_at    = $_.pushed_at
        stargazers_count = $_.stargazers_count
        forks_count  = $_.forks_count
        size         = $_.size
        default_branch = $_.default_branch
        topics       = @($_.topics)
        archived     = $_.archived
        fork         = $_.fork
        homepage     = $_.homepage
        open_issues_count = $_.open_issues_count
        license      = if ($_.license) { $_.license.spdx_id } else { $null }
    }
}

$json = $simplified | ConvertTo-Json -Depth 4 -Compress
$json | Set-Content -Path $outFile -Encoding UTF8
Write-Host "OK: $outFile ($($repos.Count) depots)" -ForegroundColor Green
