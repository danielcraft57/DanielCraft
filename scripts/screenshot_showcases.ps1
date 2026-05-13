param(
  [int]$Port = 0,
  [switch]$Headed
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$script = Join-Path $root "showcase\screenshot_showcases.py"

if (-not (Test-Path $script)) {
  throw "Introuvable: $script"
}

$pyArgs = @()
if ($Port -gt 0) {
  $pyArgs += "--port", "$Port"
}
if ($Headed) {
  $pyArgs += "--headed"
}

Set-Location $root
python $script @pyArgs
