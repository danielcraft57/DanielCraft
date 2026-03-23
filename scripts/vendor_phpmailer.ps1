# Télécharge PHPMailer (legacy v5.2.26) dans api/vendor/phpmailer/
# Utilisable sans composer, utile pour dev local/projets sans build PHP complexe.

param(
  [string]$Version = "v5.2.26",
  [switch]$Force
)

$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

$destDir = Join-Path $root "api\\vendor\\phpmailer"
$classMailer = Join-Path $destDir "class.phpmailer.php"
$classSmtp = Join-Path $destDir "class.smtp.php"

New-Item -ItemType Directory -Path $destDir -Force | Out-Null

$base = "https://raw.githubusercontent.com/PHPMailer/PHPMailer/$Version"
$files = @(
  @{ name = "class.phpmailer.php"; url = "$base/class.phpmailer.php"; target = $classMailer },
  @{ name = "class.smtp.php"; url = "$base/class.smtp.php"; target = $classSmtp }
)

foreach ($f in $files) {
  $shouldDownload = $Force -or (-not (Test-Path $f.target))
  if (-not $shouldDownload) { continue }
  Write-Host ("[PHPMailer] Téléchargement " + $f.name + " ...") -ForegroundColor Cyan
  try {
    Invoke-WebRequest -Uri $f.url -OutFile $f.target -UseBasicParsing
  } catch {
    Write-Error ("Impossible de télécharger " + $f.name + ": " + $_.Exception.Message)
    exit 1
  }
}

Write-Host "[PHPMailer] Vendor prêt dans $destDir" -ForegroundColor Green

