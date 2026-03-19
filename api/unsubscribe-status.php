<?php
/**
 * Vérifie si une entreprise est déjà désabonnée (par website).
 *
 * Usage:
 *   GET /api/unsubscribe-status.php?website=https://exemple.com
 */

header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');
header('Cache-Control: no-store, no-cache, must-revalidate, max-age=0');
header('Pragma: no-cache');

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

load_dotenv(__DIR__ . '/../.env');

$apiToken = getenv('PROSPECTLAB_TOKEN') ?: '';
// Simplification: on derive depuis PROSPECTLAB_BASE_URL (fallback: ancienne var PROSPECTLAB_API_BASE)
$baseUrl = rtrim(getenv('PROSPECTLAB_BASE_URL') ?: 'https://prospectlab.danielcraft.fr', '/');
$apiBase = rtrim(getenv('PROSPECTLAB_API_BASE') ?: ($baseUrl . '/api/public'), '/');

const LIMIT_PER_SECOND = 4;  // check status is cheap
const LIMIT_PER_MINUTE = 60;

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

    if (preg_match('#^https?://#i', $website)) {
        if (!filter_var($website, FILTER_VALIDATE_URL)) return '';
        return $website;
    }

    if (str_contains($website, '/')) return '';
    if (!filter_var($website, FILTER_VALIDATE_DOMAIN, FILTER_FLAG_HOSTNAME)) return '';
    return $website;
}

function is_list_array(array $a): bool {
    $keys = array_keys($a);
    $max = count($a) - 1;
    for ($i = 0; $i <= $max; $i++) {
        if (!isset($keys[$i]) || $keys[$i] !== $i) return false;
    }
    return true;
}

function extract_entreprise_id(mixed $decoded): ?string {
    if (!is_array($decoded)) return null;
    $try = [];
    $try[] = $decoded['id'] ?? null;
    $try[] = is_array($decoded['entreprise'] ?? null) ? ($decoded['entreprise']['id'] ?? null) : null;
    $try[] = is_array($decoded['data'] ?? null) ? ($decoded['data']['id'] ?? null) : null;
    foreach ($try as $v) {
        if (is_int($v) || is_string($v)) {
            $s = trim((string) $v);
            if ($s !== '') return $s;
        }
    }
    if (is_list_array($decoded)) {
        foreach ($decoded as $item) {
            $id = extract_entreprise_id($item);
            if ($id !== null) return $id;
        }
    }
    return null;
}

function get_entreprise_statut(mixed $decoded): string {
    if (!is_array($decoded)) return '';
    $v = $decoded['statut'] ?? null;
    if (!is_string($v)) {
        $v = is_array($decoded['entreprise'] ?? null) ? ($decoded['entreprise']['statut'] ?? null) : null;
    }
    if (!is_string($v)) {
        $v = is_array($decoded['data'] ?? null) ? ($decoded['data']['statut'] ?? null) : null;
    }
    return is_string($v) ? trim($v) : '';
}

function is_unsubscribed(string $statut): bool {
    $s = $statut ?: '';
    if (function_exists('mb_strtolower')) {
        $s = mb_strtolower($s, 'UTF-8');
    } else {
        $s = strtolower($s);
    }
    if ($s === '') return false;
    return str_contains($s, 'désabonn') || str_contains($s, 'desabonn') || str_contains($s, 'unsubscribe');
}

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'GET') {
    json_error(405, 'Méthode non autorisée');
}

$ip = client_ip();
rate_limit_or_die('unsubstat:' . $ip . ':sec', LIMIT_PER_SECOND, 1);
rate_limit_or_die('unsubstat:' . $ip . ':min', LIMIT_PER_MINUTE, 60);

$website = isset($_GET['website']) ? (string) $_GET['website'] : '';
$website = sanitize_website($website);
if ($website === '') {
    json_error(400, 'Paramètre "website" invalide.');
}

if ($apiToken === '' || $apiToken === 'REPLACE_ME') {
    json_error(500, 'Token API non configuré côté serveur.');
}

$headers = [
    'Authorization: Bearer ' . $apiToken,
    'Accept: application/json',
];

// 1) by-website -> id
$byWebsiteUrl = $apiBase . '/entreprises/by-website?website=' . rawurlencode($website);
$ch = curl_init();
curl_setopt_array($ch, [
    CURLOPT_URL => $byWebsiteUrl,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_FOLLOWLOCATION => true,
    CURLOPT_CONNECTTIMEOUT => 8,
    CURLOPT_TIMEOUT => 20,
    CURLOPT_HTTPHEADER => $headers,
    CURLOPT_CUSTOMREQUEST => 'GET',
]);
$bodyBy = curl_exec($ch);
$errBy = curl_error($ch);
$statusBy = (int) curl_getinfo($ch, CURLINFO_RESPONSE_CODE);
curl_close($ch);

if ($bodyBy === false) {
    json_error(502, 'Erreur proxy (cURL by-website): ' . ($errBy ?: 'inconnue'));
}
$decodedBy = json_decode($bodyBy, true);
if ($statusBy >= 400) {
    http_response_code($statusBy);
    echo is_array($decodedBy)
        ? json_encode($decodedBy, JSON_UNESCAPED_UNICODE)
        : json_encode(['success' => false, 'error' => 'Erreur API (by-website)', 'status' => $statusBy], JSON_UNESCAPED_UNICODE);
    exit;
}

$entrepriseId = extract_entreprise_id($decodedBy);
if ($entrepriseId === null || $entrepriseId === '') {
    json_error(404, 'Entreprise introuvable pour ce site.');
}

// 2) entreprise/<id> -> statut
$detailsUrl = $apiBase . '/entreprises/' . rawurlencode((string) $entrepriseId);
$ch = curl_init();
curl_setopt_array($ch, [
    CURLOPT_URL => $detailsUrl,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_FOLLOWLOCATION => true,
    CURLOPT_CONNECTTIMEOUT => 8,
    CURLOPT_TIMEOUT => 20,
    CURLOPT_HTTPHEADER => $headers,
    CURLOPT_CUSTOMREQUEST => 'GET',
]);
$body = curl_exec($ch);
$err = curl_error($ch);
$status = (int) curl_getinfo($ch, CURLINFO_RESPONSE_CODE);
curl_close($ch);

if ($body === false) {
    json_error(502, 'Erreur proxy (cURL entreprise): ' . ($err ?: 'inconnue'));
}
$decoded = json_decode($body, true);
if ($status >= 400) {
    http_response_code($status);
    echo is_array($decoded)
        ? json_encode($decoded, JSON_UNESCAPED_UNICODE)
        : json_encode(['success' => false, 'error' => 'Erreur API (entreprise)', 'status' => $status], JSON_UNESCAPED_UNICODE);
    exit;
}

$statut = get_entreprise_statut($decoded);
echo json_encode([
    'success' => true,
    'entreprise_id' => $entrepriseId,
    'statut' => $statut,
    'already_unsubscribed' => is_unsubscribed($statut),
], JSON_UNESCAPED_UNICODE);

