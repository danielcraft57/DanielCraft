<?php
/**
 * Telechargement PDF livre via token unique (GET ?token=… [&file=…]).
 * Le parametre code= n'est plus accepte ici (anti brute-force) — passer par la page telechargement.
 */

declare(strict_types=1);

require_once __DIR__ . '/livre-download-common.php';

api_bootstrap_env();

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'GET') {
    http_response_code(405);
    header('Content-Type: text/plain; charset=utf-8');
    echo 'Methode non autorisee';
    exit;
}

$page = api_site_base() . '/livres/telechargement/';
$ip = livre_download_client_ip();

$lock = livre_download_lock_status($ip);
if ($lock['locked']) {
    header('Location: ' . $page . '?error=locked', true, 302);
    exit;
}

if (!livre_download_rate_allow('dl:' . $ip, 60, 900)) {
    http_response_code(429);
    header('Content-Type: text/plain; charset=utf-8');
    echo 'Trop de telechargements. Reessaie plus tard.';
    exit;
}

$token = isset($_GET['token']) ? trim((string) $_GET['token']) : '';
$fileParam = isset($_GET['file']) ? trim((string) $_GET['file']) : '';

// Ancien parametre code= : redirige vers la page (ne sert plus le PDF directement)
if ($token === '' && isset($_GET['code'])) {
    $code = trim((string) $_GET['code']);
    $norm = livre_download_normalize_code($code);
    $dest = $norm !== '' ? ($page . '?code=' . rawurlencode($norm)) : ($page . '?error=expired');
    header('Location: ' . $dest, true, 302);
    exit;
}

if ($token === '' || !preg_match('/^[a-f0-9]{48,128}$/i', $token)) {
    header('Location: ' . $page . '?error=expired', true, 302);
    exit;
}

$record = livre_download_load_token(strtolower($token));
if ($record === null) {
    // Ne compte pas comme fort que le formulaire, mais limite le scanning
    if (!livre_download_rate_allow('dlfail:' . $ip, 10, 900)) {
        livre_download_record_failure($ip);
    }
    header('Location: ' . $page . '?error=expired', true, 302);
    exit;
}

$files = is_array($record['files'] ?? null) ? $record['files'] : [];
if ($files === []) {
    http_response_code(404);
    header('Content-Type: text/plain; charset=utf-8');
    echo 'Aucun fichier pour cette commande.';
    exit;
}

$token = (string) ($record['token'] ?? $token);

if ($fileParam !== '') {
    livre_download_serve_file($files, $fileParam);
    exit;
}

if (count($files) === 1) {
    livre_download_serve_file($files, (string) $files[0]['filename']);
    exit;
}

$codeNorm = livre_download_normalize_code((string) ($record['code'] ?? ''));
$dest = livre_download_page_url($codeNorm, $token);
header('Location: ' . $dest, true, 302);
exit;

/**
 * @param list<array{filename: string, label: string}> $files
 */
function livre_download_serve_file(array $files, string $requested): void
{
    $requested = basename($requested);
    $match = null;
    foreach ($files as $file) {
        if (!is_array($file)) {
            continue;
        }
        if (basename((string) ($file['filename'] ?? '')) === $requested) {
            $match = $file;
            break;
        }
    }
    if ($match === null) {
        http_response_code(404);
        header('Content-Type: text/plain; charset=utf-8');
        echo 'Fichier introuvable.';
        exit;
    }

    $path = livre_pdf_absolute_path((string) $match['filename']);
    if ($path === '') {
        http_response_code(404);
        header('Content-Type: text/plain; charset=utf-8');
        echo 'PDF indisponible sur le serveur.';
        exit;
    }

    $filename = basename($path);
    header('Content-Type: application/pdf');
    header('Content-Disposition: attachment; filename="' . str_replace('"', '', $filename) . '"');
    header('Content-Length: ' . (string) filesize($path));
    header('Cache-Control: private, no-store');
    header('X-Content-Type-Options: nosniff');
    header('X-Frame-Options: DENY');
    readfile($path);
    exit;
}
