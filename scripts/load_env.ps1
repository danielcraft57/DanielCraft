# Charge un fichier .env (au root du repo) et l'injecte dans $env: pour les scripts.
# - Ignore lignes vides et commentaires (# ...)
# - Gère KEY=VALUE avec valeurs entre guillemets simples/doubles.

function Load-EnvFile {
  param(
    [string]$EnvPath
  )

  if (-not (Test-Path $EnvPath)) {
    return
  }

  $lines = Get-Content -Path $EnvPath -ErrorAction SilentlyContinue
  foreach ($raw in $lines) {
    if ($null -eq $raw) { continue }
    $line = $raw.Trim()
    if ($line.Length -eq 0) { continue }
    if ($line.StartsWith('#')) { continue }
    if ($line -notmatch '^(?<k>[^=]+)=(?<v>.*)$') { continue }

    $key = $Matches['k'].Trim()
    $val = $Matches['v'].Trim()

    # Clé attendue pour $env:<KEY> : lettres/chiffres/underscore (sinon Set-Item peut échouer)
    if ($key -notmatch '^[A-Za-z_][A-Za-z0-9_]*$') {
      continue
    }

    # Dé-quotage basique
    if (($val.StartsWith('"') -and $val.EndsWith('"')) -or ($val.StartsWith(''') -and $val.EndsWith('''))) {
      $val = $val.Substring(1, $val.Length - 2)
    }

    # Affectation dynamique d'une variable d'environnement
    Set-Item -Path ("Env:{0}" -f $key) -Value $val
  }
}

