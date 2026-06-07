<#
.SYNOPSIS
  Alias vers serve_dev.ps1 (conservé pour compatibilité).
#>
[CmdletBinding()]
param(
  [string]$CondaEnv = "danielcraft",
  [string]$ServerHost = "127.0.0.1",
  [int]$ServerPort = 8000,
  [switch]$NoKillPort
)

$devScript = Join-Path $PSScriptRoot "serve_dev.ps1"
$args = @("-Port", $ServerPort, "-ServerHost", $ServerHost, "-CondaEnv", $CondaEnv)
if ($NoKillPort) { $args += "-NoKillPort" }
& $devScript @args
exit $LASTEXITCODE
