param(
  [string]$ListenHost = "127.0.0.1",
  [int]$Port = 8765,
  [switch]$NoBrowser
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$script = Join-Path $root "scripts\serve_vitrines_demos.py"

if (-not (Test-Path $script)) {
  throw "Introuvable: $script"
}

$pyArgs = @("--host", $ListenHost, "--port", "$Port")
if ($NoBrowser) {
  $pyArgs += "--no-browser"
}

Set-Location $root
python $script @pyArgs
