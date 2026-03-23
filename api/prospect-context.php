<?php
/**
 * Construit un contexte de personnalisation depuis ProspectLab.
 *
 * Usage:
 *   GET /api/prospect-context.php?email=contact@exemple.com
 *   GET /api/prospect-context.php?website=exemple.com
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
$baseUrl = rtrim(getenv('PROSPECTLAB_BASE_URL') ?: 'https://prospectlab.danielcraft.fr', '/');
$apiBase = rtrim(getenv('PROSPECTLAB_API_BASE') ?: ($baseUrl . '/api/public'), '/');

const LIMIT_PER_SECOND = 6;
const LIMIT_PER_MINUTE = 80;
const CACHE_TTL_SECONDS = 900;
const CACHE_VERSION = 'v2';

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
    if (!is_dir($dir)) @mkdir($dir, 0700, true);

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

function sanitize_email(string $email): string {
    $email = trim($email);
    if ($email === '') return '';
    return filter_var($email, FILTER_VALIDATE_EMAIL) ? $email : '';
}

function sanitize_website(string $website): string {
    $website = trim($website);
    if ($website === '') return '';
    if (preg_match('#^https?://#i', $website)) {
        return filter_var($website, FILTER_VALIDATE_URL) ? $website : '';
    }
    if (str_contains($website, '/')) return '';
    return filter_var($website, FILTER_VALIDATE_DOMAIN, FILTER_FLAG_HOSTNAME) ? $website : '';
}

function normalize_text(mixed $v): string {
    if (!is_string($v)) return '';
    return trim($v);
}

function read_nested(array $a, array $paths): string {
    foreach ($paths as $path) {
        $cur = $a;
        $ok = true;
        foreach ($path as $segment) {
            if (!is_array($cur) || !array_key_exists($segment, $cur)) {
                $ok = false;
                break;
            }
            $cur = $cur[$segment];
        }
        if ($ok && is_string($cur)) {
            $s = normalize_text($cur);
            if ($s !== '') return $s;
        }
    }
    return '';
}

function build_segments_from_data(array $data): array {
    $segments = [];
    $industry = read_nested($data, [
        ['industry'], ['secteur'], ['entreprise', 'secteur'], ['data', 'secteur'], ['data', 'entreprise', 'secteur']
    ]);
    $size = read_nested($data, [
        ['company_size'], ['taille'], ['entreprise', 'taille'], ['data', 'taille'], ['data', 'entreprise', 'taille_estimee']
    ]);
    $status = read_nested($data, [
        ['statut'], ['entreprise', 'statut'], ['data', 'statut'], ['data', 'entreprise', 'statut']
    ]);
    $website = read_nested($data, [
        ['website'], ['site_web'], ['entreprise', 'website'], ['data', 'website'], ['data', 'entreprise', 'website']
    ]);
    $resume = read_nested($data, [
        ['resume'], ['data', 'resume'], ['data', 'entreprise', 'resume']
    ]);
    $nom = read_nested($data, [
        ['nom'], ['entreprise', 'nom'], ['data', 'entreprise', 'nom']
    ]);
    $tagsTxt = '';
    if (
        isset($data['data']) &&
        is_array($data['data']) &&
        isset($data['data']['entreprise']) &&
        is_array($data['data']['entreprise']) &&
        isset($data['data']['entreprise']['tags']) &&
        is_array($data['data']['entreprise']['tags'])
    ) {
        $tagsTxt = implode(' ', array_map(
            static fn($x) => is_string($x) ? $x : '',
            $data['data']['entreprise']['tags']
        ));
    }

    $haystack = strtolower(implode(' | ', array_filter([$industry, $size, $status, $website, $resume, $nom, $tagsTxt])));
    if ($haystack !== '') {
        if (str_contains($haystack, 'saas')) $segments[] = 'saas';
        if (str_contains($haystack, 'agence')) $segments[] = 'agence';
        if (str_contains($haystack, 'e-commerce') || str_contains($haystack, 'ecommerce')) $segments[] = 'ecommerce';
        if (str_contains($haystack, 'magento') || str_contains($haystack, 'shopify') || str_contains($haystack, 'checkout')) $segments[] = 'ecommerce';
        if (str_contains($haystack, 'b2b')) $segments[] = 'b2b';
        if (str_contains($haystack, 'pm') || str_contains($haystack, 'pme')) $segments[] = 'pme';
        if (str_contains($haystack, 'artisan') || str_contains($haystack, 'commerce')) $segments[] = 'local-business';
        if (str_contains($haystack, 'restaurant') || str_contains($haystack, 'restauration')) $segments[] = 'local-business';
    }

    return array_values(array_unique($segments));
}

function build_priorities_from_data(array $data): array {
    $priorities = [];
    $industry = read_nested($data, [
        ['industry'], ['secteur'], ['entreprise', 'secteur'], ['data', 'secteur'], ['data', 'entreprise', 'secteur']
    ]);
    $description = read_nested($data, [
        ['description'], ['resume'], ['entreprise', 'description'], ['data', 'description'], ['data', 'entreprise', 'resume']
    ]);
    $website = read_nested($data, [
        ['website'], ['site_web'], ['entreprise', 'website'], ['data', 'website'], ['data', 'entreprise', 'website']
    ]);
    $stack = read_nested($data, [
        ['stack'], ['tech_stack'], ['entreprise', 'stack'], ['data', 'stack'], ['data', 'entreprise', 'framework'], ['data', 'entreprise', 'cms']
    ]);
    $tagsTxt = '';
    if (
        isset($data['data']) &&
        is_array($data['data']) &&
        isset($data['data']['entreprise']) &&
        is_array($data['data']['entreprise']) &&
        isset($data['data']['entreprise']['tags']) &&
        is_array($data['data']['entreprise']['tags'])
    ) {
        $tagsTxt = implode(' ', array_map(
            static fn($x) => is_string($x) ? $x : '',
            $data['data']['entreprise']['tags']
        ));
    }

    $haystack = strtolower(implode(' | ', array_filter([$industry, $description, $website, $stack, $tagsTxt])));
    if ($haystack !== '') {
        if (
            str_contains($haystack, 'seo') ||
            str_contains($haystack, 'google') ||
            str_contains($haystack, 'trafic') ||
            str_contains($haystack, 'acquisition')
        ) {
            $priorities[] = 'seo';
        }
        if (
            str_contains($haystack, 'chatgpt') ||
            str_contains($haystack, 'ia') ||
            str_contains($haystack, 'ai')
        ) {
            $priorities[] = 'ai';
        }
        if (
            str_contains($haystack, 'crm') ||
            str_contains($haystack, 'lead') ||
            str_contains($haystack, 'prospect')
        ) {
            $priorities[] = 'crm';
        }
        if (
            str_contains($haystack, 'site_sans_https') ||
            str_contains($haystack, 'fort_potentiel_refonte') ||
            str_contains($haystack, 'contact_form') ||
            str_contains($haystack, 'blog')
        ) {
            $priorities[] = 'seo';
            $priorities[] = 'web';
        }
        if (
            str_contains($haystack, 'api') ||
            str_contains($haystack, 'backend') ||
            str_contains($haystack, 'intégration') ||
            str_contains($haystack, 'integration')
        ) {
            $priorities[] = 'api';
        }
        if (
            str_contains($haystack, 'magento') ||
            str_contains($haystack, 'shopify') ||
            str_contains($haystack, 'e-commerce') ||
            str_contains($haystack, 'ecommerce')
        ) {
            $priorities[] = 'web';
            $priorities[] = 'seo';
            $priorities[] = 'automation';
        }
        if (
            str_contains($haystack, 'automatisation') ||
            str_contains($haystack, 'automation') ||
            str_contains($haystack, 'workflow')
        ) {
            $priorities[] = 'automation';
        }
    }

    if (!$priorities) $priorities[] = 'web';
    return array_values(array_unique($priorities));
}

function extract_prefill(array $data, string $requestedEmail): array {
    $name = '';
    $phone = '';
    $email = $requestedEmail;

    if (
        isset($data['data']) &&
        is_array($data['data']) &&
        isset($data['data']['match']) &&
        is_array($data['data']['match']) &&
        isset($data['data']['match']['person']) &&
        is_array($data['data']['match']['person'])
    ) {
        $fullName = $data['data']['match']['person']['full_name'] ?? null;
        if (is_string($fullName)) $name = trim($fullName);
    }
    // Si le "nom perso" est trop générique, on le vide pour permettre le fallback entreprise.
    if ($name !== '' && preg_match('/^(contact|votre)$/i', $name)) {
        $name = '';
    }
    if (
        isset($data['data']) &&
        is_array($data['data']) &&
        isset($data['data']['entreprise']) &&
        is_array($data['data']['entreprise'])
    ) {
        $tel = $data['data']['entreprise']['telephone'] ?? null;
        if (is_string($tel) || is_int($tel)) $phone = trim((string) $tel);
        if ($email === '') {
            $ep = $data['data']['entreprise']['email_principal'] ?? null;
            if (is_string($ep) && filter_var($ep, FILTER_VALIDATE_EMAIL)) $email = $ep;
        }
        if ($name === '') {
            $nom = $data['data']['entreprise']['nom'] ?? null;
            if (is_string($nom)) $name = trim($nom);
        }
    }
    return ['name' => $name, 'email' => $email, 'phone' => normalize_phone_fr_international($phone)];
}

function normalize_phone_fr_international(string $raw): string {
    $s = trim($raw);
    if ($s === '') return '';

    // Garde uniquement + et chiffres.
    $s = preg_replace('/[^\d+]/', '', $s);
    if (!is_string($s) || $s === '') return '';

    // Cas "0033..."
    if (str_starts_with($s, '00')) {
        $s = '+' . substr($s, 2);
    }
    // Cas "33..." (sans +)
    if (!str_starts_with($s, '+') && str_starts_with($s, '33')) {
        $s = '+' . $s;
    }
    // Cas national "0X..."
    if (!str_starts_with($s, '+') && str_starts_with($s, '0')) {
        $s = '+33' . substr($s, 1);
    }

    // Format conventionnel FR: +33 X XX XX XX XX
    if (preg_match('/^\+33(\d{9})$/', $s, $m)) {
        $d = $m[1];
        return sprintf(
            '+33 %s %s %s %s %s',
            substr($d, 0, 1),
            substr($d, 1, 2),
            substr($d, 3, 2),
            substr($d, 5, 2),
            substr($d, 7, 2)
        );
    }

    return $raw;
}

function get_cache_file(string $key): string {
    $dir = rtrim(sys_get_temp_dir(), DIRECTORY_SEPARATOR) . DIRECTORY_SEPARATOR . 'dc_pl_cache';
    if (!is_dir($dir)) @mkdir($dir, 0700, true);
    return $dir . DIRECTORY_SEPARATOR . 'ctx_' . sha1($key) . '.json';
}

function read_cache(string $key): ?array {
    $file = get_cache_file($key);
    if (!is_file($file) || !is_readable($file)) return null;
    $raw = @file_get_contents($file);
    if (!is_string($raw) || trim($raw) === '') return null;
    $decoded = json_decode($raw, true);
    if (!is_array($decoded)) return null;
    $ts = isset($decoded['cached_at']) ? (int) $decoded['cached_at'] : 0;
    if ($ts <= 0 || (time() - $ts) > CACHE_TTL_SECONDS) return null;
    return $decoded;
}

function write_cache(string $key, array $payload): void {
    $file = get_cache_file($key);
    $payload['cached_at'] = time();
    @file_put_contents($file, json_encode($payload, JSON_UNESCAPED_UNICODE));
}

function to_bool_query(mixed $v): bool {
    if (!is_string($v) && !is_int($v) && !is_bool($v)) return false;
    $s = strtolower(trim((string) $v));
    return in_array($s, ['1', 'true', 'yes', 'on'], true);
}

function as_debug_payload(array $payload, bool $includeRaw = false): array {
    $out = [
        'success' => (bool)($payload['success'] ?? false),
        'source' => (string)($payload['source'] ?? ''),
        'query' => is_array($payload['query'] ?? null) ? $payload['query'] : [],
        'segments' => is_array($payload['segments'] ?? null) ? $payload['segments'] : [],
        'priorities' => is_array($payload['priorities'] ?? null) ? $payload['priorities'] : [],
        'confidence' => $payload['confidence'] ?? null,
        'prefill' => is_array($payload['prefill'] ?? null) ? $payload['prefill'] : [],
        'cache_key' => (string)($payload['_cache_key'] ?? ''),
        'cached_at' => $payload['cached_at'] ?? null,
    ];
    if ($includeRaw) {
        $out['entreprise'] = $payload['entreprise'] ?? null;
    }
    return $out;
}

function as_public_payload(array $payload, bool $includeRaw = false): array {
    // Format public volontairement identique au format debug
    // pour simplifier le traitement côté front.
    return as_debug_payload($payload, $includeRaw);
}

function call_pl_get(string $url, array $headers): array {
    if (function_exists('curl_init')) {
        $ch = curl_init();
        curl_setopt_array($ch, [
            CURLOPT_URL => $url,
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
            return ['ok' => false, 'status' => 502, 'error' => 'Erreur proxy cURL: ' . ($err ?: 'inconnue')];
        }
    } else {
        $headersRaw = implode("\r\n", $headers);
        $context = stream_context_create([
            'http' => [
                'method' => 'GET',
                'header' => $headersRaw . "\r\n",
                'ignore_errors' => true,
                'timeout' => 20,
            ],
            'ssl' => [
                'verify_peer' => true,
                'verify_peer_name' => true,
            ],
        ]);
        $body = @file_get_contents($url, false, $context);
        if ($body === false) {
            return ['ok' => false, 'status' => 502, 'error' => 'Erreur proxy HTTP (file_get_contents).'];
        }
        $status = 200;
        if (isset($http_response_header) && is_array($http_response_header)) {
            foreach ($http_response_header as $line) {
                if (preg_match('#^HTTP/\S+\s+(\d{3})#', (string) $line, $m)) {
                    $status = (int) $m[1];
                    break;
                }
            }
        }
    }
    $decoded = json_decode($body, true);
    if ($status >= 400) {
        return ['ok' => false, 'status' => $status, 'error' => is_array($decoded) ? ($decoded['error'] ?? 'Erreur API') : 'Erreur API'];
    }
    return ['ok' => true, 'status' => $status, 'data' => is_array($decoded) ? $decoded : []];
}

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204);
    exit;
}
if ($_SERVER['REQUEST_METHOD'] !== 'GET') {
    json_error(405, 'Méthode non autorisée');
}

$ip = client_ip();
rate_limit_or_die('plctx:' . $ip . ':sec', LIMIT_PER_SECOND, 1);
rate_limit_or_die('plctx:' . $ip . ':min', LIMIT_PER_MINUTE, 60);

if ($apiToken === '' || $apiToken === 'REPLACE_ME') {
    json_error(500, 'Token API non configuré côté serveur.');
}

$email = sanitize_email((string) ($_GET['email'] ?? ''));
$website = sanitize_website((string) ($_GET['website'] ?? ''));
if ($email === '' && $website === '') {
    json_error(400, 'Paramètre "email" ou "website" requis.');
}

$source = $email !== '' ? 'email' : 'website';
$cacheKey = CACHE_VERSION . ':' . $source . ':' . ($source === 'email' ? strtolower($email) : strtolower($website));
$refresh = isset($_GET['refresh']) && (string)$_GET['refresh'] === '1';
$debug = to_bool_query($_GET['debug'] ?? null);
$debugFull = to_bool_query($_GET['debug_full'] ?? null);
$includeRaw = to_bool_query($_GET['include_raw'] ?? null) || $debugFull;
$cached = $refresh ? null : read_cache($cacheKey);
if (is_array($cached)) {
    if ($debug) {
        echo json_encode(as_debug_payload($cached, $debugFull), JSON_UNESCAPED_UNICODE);
        exit;
    }
    echo json_encode(as_public_payload($cached, $includeRaw), JSON_UNESCAPED_UNICODE);
    exit;
}

$headers = [
    'Authorization: Bearer ' . $apiToken,
    'Accept: application/json',
];

$url = $source === 'email'
    ? ($apiBase . '/entreprises/by-email?email=' . rawurlencode($email) . '&include_emails=1')
    : ($apiBase . '/entreprises/by-website?website=' . rawurlencode($website));

$res = call_pl_get($url, $headers);
if (!$res['ok']) {
    json_error((int) ($res['status'] ?? 502), (string) ($res['error'] ?? 'Erreur API ProspectLab'));
}

$data = is_array($res['data']) ? $res['data'] : [];
$segments = build_segments_from_data($data);
$priorities = build_priorities_from_data($data);
$prefill = extract_prefill($data, $email);

$payload = [
    'success' => true,
    'source' => $source,
    'query' => [
        'email' => $source === 'email' ? $email : null,
        'website' => $source === 'website' ? $website : null,
    ],
    'segments' => $segments,
    'priorities' => $priorities,
    'confidence' => count($segments) > 0 ? 0.75 : 0.55,
    'entreprise' => $data,
    'offer_hints' => [
        'priorities' => $priorities,
        'segments' => $segments,
    ],
    'prefill' => $prefill,
    '_cache_key' => $cacheKey,
];

write_cache($cacheKey, $payload);
if ($debug) {
    echo json_encode(as_debug_payload($payload, $debugFull), JSON_UNESCAPED_UNICODE);
    exit;
}
echo json_encode(as_public_payload($payload, $includeRaw), JSON_UNESCAPED_UNICODE);

