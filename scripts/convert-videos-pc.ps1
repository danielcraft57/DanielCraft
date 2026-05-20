<#
.SYNOPSIS
    Convertit en lot des vidéos 1080p (ou plus) au format PC : 720p H.264 + AAC dans un MP4.

.DESCRIPTION
    Parcourt un dossier (récursif par défaut), trouve les .mkv/.mp4 même dans les
    sous-dossiers type release (un épisode = un dossier), et écrit les MP4 dans « pc ».

    Par défaut, sortie à plat dans pc\ (pas de copie de l'arborescence des releases).
    Utilisez -MirrorFolders pour reproduire les sous-dossiers source.

    Prérequis : ffmpeg dans le PATH (https://ffmpeg.org)

.EXAMPLE
    .\scripts\convert-videos-pc.ps1 -InputPath "C:\Users\...\Videos\Series\Ma.Saison.1080p-FCK"

.EXAMPLE
    .\scripts\convert-videos-pc.ps1 -InputPath "D:\Series\MaSerie" -Fast

.EXAMPLE
    .\scripts\convert-videos-pc.ps1 -InputPath "D:\Series\MaSerie" -Encoder NVENC -CopyAudio

.EXAMPLE
    .\scripts\convert-videos-pc.ps1 -InputPath "D:\Series\MaSerie" -Fast -Force
#>
param(
    [Parameter(Mandatory = $true)]
    [string]$InputPath,

    [string]$OutputDir = "",

    [int]$Height = 720,

    [int]$Crf = 23,

    [ValidateSet("ultrafast", "superfast", "veryfast", "faster", "fast", "medium", "slow", "slower", "veryslow")]
    [string]$Preset = "veryfast",

    [int]$AudioBitrateK = 192,

    [ValidateSet("Auto", "CPU", "NVENC", "QSV", "AMF")]
    [string]$Encoder = "Auto",

  # Recopie la piste audio sans ré-encodage (ac3, eac3, aac…) — beaucoup plus rapide
    [switch]$CopyAudio,

  # GPU si dispo + preset rapide + copie audio quand possible
    [switch]$Fast,

  # Désactive la recherche dans les sous-dossiers (un épisode par dossier, etc.)
    [switch]$NoRecurse,

  # Recrée l'arborescence source sous pc\ (défaut : tous les MP4 directement dans pc\)
    [switch]$MirrorFolders,

    [switch]$SkipExisting,

  # Reconvertit tout (ignore -SkipExisting, écrase les MP4 valides déjà présents)
    [switch]$Force,

    [switch]$WhatIf
)

$ErrorActionPreference = "Stop"

$videoExtensions = @(".mkv", ".mp4", ".avi", ".m4v", ".mov", ".ts", ".wmv", ".webm", ".flv")

function Test-CommandAvailable {
    param([string]$Name)
    $null -ne (Get-Command $Name -ErrorAction SilentlyContinue)
}

$script:FfmpegEncoderList = $null

function Get-FfmpegEncoderList {
    if ($null -eq $script:FfmpegEncoderList) {
        $script:FfmpegEncoderList = & ffmpeg -hide_banner -encoders 2>&1 | Out-String
    }
    $script:FfmpegEncoderList
}

function Test-FfmpegEncoder {
    param([string]$Name)
    (Get-FfmpegEncoderList) -match [regex]::Escape($Name)
}

function Resolve-VideoEncoder {
    param([string]$Choice)
    $map = @{
        NVENC = "h264_nvenc"
        QSV   = "h264_qsv"
        AMF   = "h264_amf"
    }
    if ($Choice -eq "CPU") { return "cpu" }
    if ($Choice -ne "Auto") {
        if (-not (Test-FfmpegEncoder $map[$Choice])) {
            throw "Encodeur $Choice indisponible dans cette build ffmpeg. Essayez -Encoder Auto ou installez ffmpeg avec support GPU."
        }
        return $Choice.ToLowerInvariant()
    }
    foreach ($key in @("NVENC", "QSV", "AMF")) {
        if (Test-FfmpegEncoder $map[$key]) { return $key.ToLowerInvariant() }
    }
    "cpu"
}

function Get-FirstAudioCodec {
    param([string]$Path)
    if (-not (Test-CommandAvailable "ffprobe")) { return $null }
    $raw = & ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 -- "$Path" 2>$null
    if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($raw)) { return $null }
    return $raw.Trim().ToLowerInvariant()
}

function Test-AudioCopyOk {
    param([string]$Codec)
    $copyable = @("aac", "ac3", "eac3", "mp3", "opus", "flac")
    $copyable -contains $Codec
}

function Get-VideoEncoderArgs {
    param(
        [string]$EncoderKind,
        [int]$Crf,
        [string]$CpuPreset
    )
    switch ($EncoderKind) {
        "nvenc" {
            $cq = [Math]::Min(51, $Crf + 2)
            return @(
                "-c:v", "h264_nvenc",
                "-preset", "p2",
                "-tune", "hq",
                "-rc", "vbr",
                "-cq", "$cq",
                "-b:v", "0",
                "-pix_fmt", "yuv420p"
            )
        }
        "qsv" {
            return @(
                "-c:v", "h264_qsv",
                "-global_quality", "$Crf",
                "-preset", "veryfast",
                "-pix_fmt", "nv12"
            )
        }
        "amf" {
            return @(
                "-c:v", "h264_amf",
                "-quality", "speed",
                "-rc", "cqp",
                "-qp_i", "$Crf",
                "-qp_p", "$Crf",
                "-pix_fmt", "yuv420p"
            )
        }
        default {
            return @(
                "-c:v", "libx264",
                "-crf", "$Crf",
                "-preset", $CpuPreset,
                "-pix_fmt", "yuv420p",
                "-threads", "0"
            )
        }
    }
}

function Get-FullPathNormalized {
    param([string]$Path)
    [System.IO.Path]::GetFullPath($Path)
}

function Test-PathUnderDirectory {
    param(
        [string]$FilePath,
        [string]$DirectoryPath
    )
    $dir = (Get-FullPathNormalized $DirectoryPath).TrimEnd('\', '/') + [System.IO.Path]::DirectorySeparatorChar
    $file = Get-FullPathNormalized $FilePath
    return $file.StartsWith($dir, [StringComparison]::OrdinalIgnoreCase)
}

function Test-MediaFileValid {
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) { return $false }
    if (-not (Test-CommandAvailable "ffprobe")) {
        return (Get-Item -LiteralPath $Path).Length -gt 1MB
    }
    & ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 -- "$Path" 2>$null | Out-Null
    return $LASTEXITCODE -eq 0
}

function Get-OutputFilePath {
    param(
        [System.IO.FileInfo]$Source,
        [string]$RootIn,
        [string]$RootOut,
        [bool]$Flat
    )
    if ($Flat) {
        $baseName = [System.IO.Path]::GetFileNameWithoutExtension($Source.Name)
        return Join-Path $RootOut ($baseName + ".mp4")
    }
    $relative = $Source.FullName.Substring($RootIn.Length).TrimStart("\", "/")
    $baseName = [System.IO.Path]::GetFileNameWithoutExtension($relative)
    $parent = [System.IO.Path]::GetDirectoryName($relative)
    $destDir = if ([string]::IsNullOrEmpty($parent)) { $RootOut } else { Join-Path $RootOut $parent }
    Join-Path $destDir ($baseName + ".mp4")
}

if (-not (Test-CommandAvailable "ffmpeg")) {
    throw "ffmpeg introuvable dans le PATH. Installez-le puis relancez (ex. winget install Gyan.FFmpeg)."
}

if (-not (Test-Path -LiteralPath $InputPath)) {
    throw "Chemin introuvable : $InputPath"
}

$item = Get-Item -LiteralPath $InputPath
$inputResolved = $item.FullName
$isFile = -not $item.PSIsContainer

if ($isFile) {
  if ($videoExtensions -notcontains $item.Extension.ToLowerInvariant()) {
    throw "Extension non gérée : $($item.Extension). Extensions : $($videoExtensions -join ', ')"
  }
  $files = @($item)
  $rootIn = Split-Path -Parent $inputResolved
  if ([string]::IsNullOrWhiteSpace($OutputDir)) {
    $rootOut = Join-Path $rootIn "pc"
  } elseif (Test-Path -LiteralPath $OutputDir) {
    $rootOut = (Resolve-Path -LiteralPath $OutputDir).Path
  } else {
    $rootOut = $OutputDir
  }
} else {
  $rootIn = $inputResolved
  if ([string]::IsNullOrWhiteSpace($OutputDir)) {
    $rootOut = Join-Path $rootIn "pc"
  } else {
    if ([System.IO.Path]::IsPathRooted($OutputDir)) {
      $rootOut = $OutputDir
    } else {
      $rootOut = Join-Path $rootIn $OutputDir
    }
  }
  $searchParams = @{
    LiteralPath = $rootIn
    File        = $true
  }
  if (-not $NoRecurse) { $searchParams["Recurse"] = $true }
  $rootOutFullForExclude = Get-FullPathNormalized $rootOut
  $files = @(Get-ChildItem @searchParams | Where-Object {
    $videoExtensions -contains $_.Extension.ToLowerInvariant() -and
    -not (Test-PathUnderDirectory -FilePath $_.FullName -DirectoryPath $rootOutFullForExclude) -and
    -not $_.Name.EndsWith(".part", [StringComparison]::OrdinalIgnoreCase)
  } | Sort-Object FullName)
}

$rootOutFull = Get-FullPathNormalized $rootOut
$rootInFull = Get-FullPathNormalized $rootIn

$flatOutput = -not $MirrorFolders
if ($isFile) { $flatOutput = $true }

if ($files.Count -eq 0) {
  Write-Host "Aucun fichier vidéo trouvé dans : $inputResolved"
  if (-not $isFile -and -not $NoRecurse) {
    $subdirs = @(Get-ChildItem -LiteralPath $inputResolved -Directory -ErrorAction SilentlyContinue)
    if ($subdirs.Count -gt 0) {
      Write-Host "Des sous-dossiers existent ; vérifiez qu'ils contiennent bien un .mkv / .mp4."
    }
  }
  exit 0
}

New-Item -ItemType Directory -Force -Path $rootOut | Out-Null

if (Test-Path -LiteralPath $rootOutFull) {
    $broken = @(Get-ChildItem -LiteralPath $rootOutFull -Recurse -File -ErrorAction SilentlyContinue |
        Where-Object { $_.Extension -eq ".mp4" -and -not (Test-MediaFileValid -Path $_.FullName) })
    foreach ($bad in $broken) {
        Write-Host "Nettoyage : $($bad.FullName.Substring($rootOutFull.Length).TrimStart('\')) (fichier incomplet)"
        Remove-Item -LiteralPath $bad.FullName -Force -ErrorAction SilentlyContinue
    }
    Get-ChildItem -LiteralPath $rootOutFull -Recurse -Filter "*.part" -File -ErrorAction SilentlyContinue |
        Remove-Item -Force -ErrorAction SilentlyContinue
}

if ($Fast) {
    $Preset = "veryfast"
    $CopyAudio = $true
}

$videoEncoder = Resolve-VideoEncoder -Choice $Encoder
$encoderLabel = switch ($videoEncoder) {
    "nvenc" { "H.264 NVENC (GPU NVIDIA)" }
    "qsv"   { "H.264 QSV (GPU Intel)" }
    "amf"   { "H.264 AMF (GPU AMD)" }
    default { "H.264 libx264 (CPU, preset $Preset)" }
}

Write-Host "Entrée  : $rootIn"
Write-Host "Dossier : $rootOut ($(if ($flatOutput) { 'fichiers à plat' } else { 'miroir arborescence' }))"
Write-Host "Vidéo   : ${Height}p — $encoderLabel — qualité ~CRF $Crf"
Write-Host "Audio   : $(if ($CopyAudio) { 'copie si compatible (ac3/eac3/aac…), sinon AAC' } else { "ré-encodage AAC ${AudioBitrateK}k" })"
Write-Host "Scan    : $(if ($NoRecurse) { 'racine uniquement' } else { 'récursif (hors dossier de sortie)' })"
if ($Fast) { Write-Host "Mode    : -Fast (GPU + copie audio)" }
if ($Force) { Write-Host "Mode    : -Force (reconversion, écrase les sorties existantes)" }
Write-Host "Fichiers: $($files.Count) source(s)"
Write-Host ""

$index = 0
$failed = @()

foreach ($file in $files) {
  $index++
  $outFile = Get-OutputFilePath -Source $file -RootIn $rootIn -RootOut $rootOut -Flat:$flatOutput
  $outParent = Split-Path -Parent $outFile
  if (-not (Test-Path -LiteralPath $outParent)) {
    New-Item -ItemType Directory -Force -Path $outParent | Out-Null
  }

  if (Test-Path -LiteralPath $outFile) {
    if (-not (Test-MediaFileValid -Path $outFile)) {
      Write-Host "[$index/$($files.Count)] Sortie invalide supprimée : $([System.IO.Path]::GetFileName($outFile))"
      Remove-Item -LiteralPath $outFile -Force -ErrorAction SilentlyContinue
    } elseif ($SkipExisting -and -not $Force) {
      $srcTime = $file.LastWriteTimeUtc
      $outTime = (Get-Item -LiteralPath $outFile).LastWriteTimeUtc
      if ($outTime -ge $srcTime) {
        Write-Host "[$index/$($files.Count)] SKIP (déjà à jour) : $($file.Name)"
        continue
      }
    } elseif ($Force) {
      Write-Host "  (écrasement forcé)"
    }
  }

  $tmpOut = "$outFile.part"
  if (Test-Path -LiteralPath $tmpOut) {
    Remove-Item -LiteralPath $tmpOut -Force -ErrorAction SilentlyContinue
  }

  $relSrc = $file.FullName.Substring($rootIn.Length).TrimStart("\", "/")
  Write-Host "[$index/$($files.Count)] $relSrc"
  Write-Host "  -> $([System.IO.Path]::GetFileName($outFile))"

  if ($WhatIf) { continue }

  $vf = "scale=-2:${Height}:force_original_aspect_ratio=decrease"
  $videoArgs = Get-VideoEncoderArgs -EncoderKind $videoEncoder -Crf $Crf -CpuPreset $Preset

  $audioCodec = Get-FirstAudioCodec -Path $file.FullName
  $useAudioCopy = $CopyAudio -and (Test-AudioCopyOk -Codec $audioCodec)

  $inputArgs = @("-hide_banner", "-loglevel", "error", "-stats", "-nostdin")
  if ($videoEncoder -ne "cpu") {
    $inputArgs += @("-hwaccel", "auto")
  }
  $ffmpegArgs = $inputArgs + @(
    "-i", $file.FullName,
    "-map", "0:v:0?", "-map", "0:a:0?",
    "-vf", $vf
  ) + $videoArgs

  if ($useAudioCopy) {
    $ffmpegArgs += @("-c:a", "copy")
  } else {
    $ffmpegArgs += @("-c:a", "aac", "-b:a", "${AudioBitrateK}k", "-ac", "2")
  }

  $ffmpegArgs += @("-movflags", "+faststart", "-y", $tmpOut)

  if ($useAudioCopy) {
    Write-Host "  audio: copie ($audioCodec)"
  } elseif ($audioCodec) {
    Write-Host "  audio: transcode $audioCodec -> aac"
  }

  & ffmpeg @ffmpegArgs
  if ($LASTEXITCODE -ne 0) {
    Remove-Item -LiteralPath $tmpOut -Force -ErrorAction SilentlyContinue
    $failed += $file.FullName
    Write-Warning "Échec ffmpeg pour : $($file.FullName)"
  } else {
    Move-Item -LiteralPath $tmpOut -Destination $outFile -Force
  }
}

Write-Host ""
if ($WhatIf) {
  Write-Host "Mode -WhatIf : aucune conversion effectuée."
} elseif ($failed.Count -gt 0) {
  Write-Host "Terminé avec $($failed.Count) erreur(s)."
  exit 1
} else {
  Write-Host "Terminé. Fichiers dans : $rootOut"
}
