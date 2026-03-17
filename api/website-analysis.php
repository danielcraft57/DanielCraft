<?php
/**
 * Proxy sécurisé d'analyse (token côté serveur).
 *
 * Usage:
 *   GET /api/website-analysis.php?website=https://exemple.com&full=1
 *
 * Sécurité:
 * - Token en dur (NE PAS versionner en public).
 * - Rate limiting par IP (req/sec + req/min) via fichiers temporaires.
 */

header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');
header('Cache-Control: no-store, no-cache, must-revalidate, max-age=0');
header('Pragma: no-cache');

/**
 * Charge un fichier .env très simple (KEY=VALUE) si présent.
 * - Ignore les lignes vides et commentaires (# ...)
 * - Ne gère pas les quotes complexes (suffisant ici)
 */
function load_dotenv(string $path): void {
    if (!is_readable($path)) return;
    $lines = @file($path, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    if (!is_array($lines)) return;
    foreach ($lines as $line) {
        $line = trim((string) $line);
        if ($line === '' || str_starts_with($line, '#')) continue;
        $parts = explode('=', $line, 2);
        if (count($parts) !== 2) continue;
        $k = trim($parts[0]);
        $v = trim($parts[1]);
        if ($k === '') continue;
        putenv($k . '=' . $v);
        $_ENV[$k] = $v;
        $_SERVER[$k] = $v;
    }
}

// --- Config ---
// Charge .env à la racine du projet (un niveau au-dessus de /api)
load_dotenv(__DIR__ . '/../.env');

// Variables attendues dans .env
$apiToken = getenv('PROSPECTLAB_TOKEN') ?: '';
$apiEndpoint = getenv('PROSPECTLAB_ENDPOINT') ?: 'https://prospectlab.danielcraft.fr/api/public/website-analysis';

// Rate limit (par IP)
const LIMIT_PER_SECOND = 2;  // max 2 req/s
const LIMIT_PER_MINUTE = 30; // max 30 req/min

function json_error(int $status, string $message): void {
    http_response_code($status);
    echo json_encode(['success' => false, 'error' => $message], JSON_UNESCAPED_UNICODE);
    exit;
}

function client_ip(): string {
    if (!empty($_SERVER['HTTP_CF_CONNECTING_IP'])) return (string) $_SERVER['HTTP_CF_CONNECTING_IP'];
    if (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
        $parts = explode(',', (string) $_SERVER['HTTP_X_FORWARDED_FOR']);
        if (!empty($parts[0])) return trim($parts[0]);
    }
    return !empty($_SERVER['REMOTE_ADDR']) ? (string) $_SERVER['REMOTE_ADDR'] : 'unknown';
}

function rate_limit_or_die(string $key, int $limit, int $windowSeconds): void {
    $dir = rtrim(sys_get_temp_dir(), DIRECTORY_SEPARATOR) . DIRECTORY_SEPARATOR . 'dc_rl';
    if (!is_dir($dir)) {
        @mkdir($dir, 0700, true);
    }

    $file = $dir . DIRECTORY_SEPARATOR . 'rl_' . sha1($key) . '.json';
    $now = time();
    $data = ['ts' => []];

    $fp = @fopen($file, 'c+');
    if ($fp === false) return;
    if (!flock($fp, LOCK_EX)) {
        fclose($fp);
        return;
    }

    $raw = stream_get_contents($fp);
    if ($raw !== false && trim($raw) !== '') {
        $decoded = json_decode($raw, true);
        if (is_array($decoded) && isset($decoded['ts']) && is_array($decoded['ts'])) {
            $data = $decoded;
        }
    }

    $cutoff = $now - $windowSeconds;
    $ts = [];
    foreach ($data['ts'] as $t) {
        $ti = (int) $t;
        if ($ti >= $cutoff) $ts[] = $ti;
    }

    if (count($ts) >= $limit) {
        flock($fp, LOCK_UN);
        fclose($fp);
        json_error(429, 'Trop de requêtes. Réessayez dans quelques instants.');
    }

    $ts[] = $now;
    $data['ts'] = $ts;

    ftruncate($fp, 0);
    rewind($fp);
    fwrite($fp, json_encode($data));
    fflush($fp);
    flock($fp, LOCK_UN);
    fclose($fp);
}

function sanitize_website(string $website): string {
    $website = trim($website);
    if ($website === '') return '';
    if (!preg_match('#^https?://#i', $website)) return '';
    if (!filter_var($website, FILTER_VALIDATE_URL)) return '';
    return $website;
}

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'GET') {
    json_error(405, 'Méthode non autorisée');
}

$ip = client_ip();
rate_limit_or_die('wa:' . $ip . ':sec', LIMIT_PER_SECOND, 1);
rate_limit_or_die('wa:' . $ip . ':min', LIMIT_PER_MINUTE, 60);

$website = isset($_GET['website']) ? (string) $_GET['website'] : '';
$full = isset($_GET['full']) ? (string) $_GET['full'] : '1';

$website = sanitize_website($website);
if ($website === '') {
    json_error(400, 'Paramètre "website" invalide. Utilisez une URL http(s).');
}

$full = ($full === '0' || $full === '1') ? $full : '1';

if ($apiToken === '' || $apiToken === 'REPLACE_ME') {
    json_error(500, 'Token API non configuré côté serveur.');
}

$url = rtrim($apiEndpoint, '/') . '?website=' . rawurlencode($website) . '&full=' . rawurlencode($full);

$ch = curl_init();
curl_setopt_array($ch, [
    CURLOPT_URL => $url,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_FOLLOWLOCATION => true,
    CURLOPT_CONNECTTIMEOUT => 8,
    CURLOPT_TIMEOUT => 45,
    CURLOPT_HTTPHEADER => [
        'Authorization: Bearer ' . $apiToken,
        'Accept: application/json',
    ],
]);

$body = curl_exec($ch);
$err = curl_error($ch);
$status = (int) curl_getinfo($ch, CURLINFO_RESPONSE_CODE);
curl_close($ch);

if ($body === false) {
    json_error(502, 'Erreur proxy (cURL): ' . ($err ?: 'inconnue'));
}

if ($status >= 400) {
    http_response_code($status);
    $decoded = json_decode($body, true);
    if (is_array($decoded)) {
        echo json_encode($decoded, JSON_UNESCAPED_UNICODE);
        exit;
    }
    echo json_encode(['success' => false, 'error' => 'Erreur API', 'status' => $status], JSON_UNESCAPED_UNICODE);
    exit;
}

echo $body;

