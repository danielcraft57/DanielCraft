<?php
/**
 * Client ProspectLab partagé (token, rate limit, HTTP).
 */

declare(strict_types=1);

require_once __DIR__ . '/env.php';

function pl_bootstrap(): void
{
    api_bootstrap_env();
}

function pl_token(): string
{
    $token = getenv('PROSPECTLAB_TOKEN') ?: '';
    return trim((string) $token);
}

function pl_base_url(): string
{
    return rtrim(getenv('PROSPECTLAB_BASE_URL') ?: 'https://prospectlab.danielcraft.fr', '/');
}

function pl_api_base(): string
{
    $custom = trim((string) (getenv('PROSPECTLAB_API_BASE') ?: ''));
    if ($custom !== '') {
        return rtrim($custom, '/');
    }
    return pl_base_url() . '/api/public';
}

function pl_website_analysis_endpoint(): string
{
    $endpoint = trim((string) (getenv('PROSPECTLAB_ENDPOINT') ?: ''));
    if ($endpoint !== '') {
        return rtrim($endpoint, '/');
    }
    return pl_api_base() . '/website-analysis';
}

/**
 * Clé alternative documentée : header X-Website-Audit-Key (PUBLIC_WEBSITE_AUDIT_LEAD_KEY).
 */
function pl_website_audit_lead_key(): string
{
    $key = getenv('PUBLIC_WEBSITE_AUDIT_LEAD_KEY') ?: getenv('PROSPECTLAB_WEBSITE_AUDIT_KEY') ?: '';
    return trim((string) $key);
}

/** URL POST audit PDF + email (gratuit) ou mode complet (premium). */
function pl_website_audit_report_url(bool $complete = false): string
{
    $custom = trim((string) (getenv('PROSPECTLAB_WEBSITE_AUDIT_REPORT_URL') ?: ''));
    if ($custom !== '') {
        return rtrim($custom, '/');
    }
    $base = pl_api_base() . '/website-audit-report';
    return $complete ? $base . '/complete' : $base;
}

/**
 * @return array<string, mixed>
 */
function pl_website_audit_report_payload(string $website, string $email): array
{
    $payload = [
        'website' => $website,
        'email' => $email,
    ];

    foreach (['max_depth', 'max_workers', 'max_time', 'max_pages'] as $key) {
        $envKey = 'PROSPECTLAB_AUDIT_' . strtoupper($key);
        $raw = getenv($envKey);
        if ($raw !== false && trim((string) $raw) !== '' && ctype_digit(trim((string) $raw))) {
            $payload[$key] = (int) trim((string) $raw);
        }
    }

    $nmap = getenv('PROSPECTLAB_AUDIT_ENABLE_NMAP');
    if ($nmap !== false && trim((string) $nmap) !== '') {
        $payload['enable_nmap'] = in_array(strtolower(trim((string) $nmap)), ['1', 'true', 'yes', 'on'], true);
    }

    $lh = getenv('PROSPECTLAB_AUDIT_USE_LIGHTHOUSE');
    if ($lh !== false && trim((string) $lh) !== '') {
        $payload['use_lighthouse'] = in_array(strtolower(trim((string) $lh)), ['1', 'true', 'yes', 'on'], true);
    }

    return $payload;
}

function pl_has_audit_auth(): bool
{
    $token = pl_token();
    if ($token !== '' && $token !== 'REPLACE_ME') {
        return true;
    }
    return pl_website_audit_lead_key() !== '';
}

function pl_env_int(string $key, int $default): int
{
    $raw = getenv($key);
    if ($raw === false || trim((string) $raw) === '') {
        return $default;
    }
    $n = (int) $raw;
    return $n > 0 ? $n : $default;
}

function pl_json_error(int $status, string $message, array $extra = []): void
{
    http_response_code($status);
    echo json_encode(array_merge(['success' => false, 'error' => $message], $extra), JSON_UNESCAPED_UNICODE);
    exit;
}

function pl_client_ip(): string
{
    if (!empty($_SERVER['HTTP_CF_CONNECTING_IP'])) {
        return (string) $_SERVER['HTTP_CF_CONNECTING_IP'];
    }
    if (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
        $parts = explode(',', (string) $_SERVER['HTTP_X_FORWARDED_FOR']);
        if (!empty($parts[0])) {
            return trim($parts[0]);
        }
    }
    return !empty($_SERVER['REMOTE_ADDR']) ? (string) $_SERVER['REMOTE_ADDR'] : 'unknown';
}

/**
 * Fenêtre glissante (fichiers temp) — même logique que website-analysis.php.
 */
function pl_rate_limit_or_die(string $key, int $limit, int $windowSeconds, string $userMessage = ''): void
{
    if ($limit < 1 || $windowSeconds < 1) {
        return;
    }

    $dir = rtrim(sys_get_temp_dir(), DIRECTORY_SEPARATOR) . DIRECTORY_SEPARATOR . 'dc_rl';
    if (!is_dir($dir)) {
        @mkdir($dir, 0700, true);
    }

    $file = $dir . DIRECTORY_SEPARATOR . 'rl_' . sha1($key) . '.json';
    $now = time();
    $data = ['ts' => []];

    $fp = @fopen($file, 'c+');
    if ($fp === false) {
        return;
    }
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
        if ($ti >= $cutoff) {
            $ts[] = $ti;
        }
    }

    if (count($ts) >= $limit) {
        flock($fp, LOCK_UN);
        fclose($fp);
        $msg = $userMessage !== ''
            ? $userMessage
            : 'Trop de demandes. Réessayez plus tard.';
        pl_json_error(429, $msg);
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

function pl_apply_free_audit_rate_limits(string $ip, string $email, string $websiteHost): void
{
    $perSec = pl_env_int('PROSPECTLAB_FREE_AUDIT_LIMIT_PER_SECOND', 1);
    $perMin = pl_env_int('PROSPECTLAB_FREE_AUDIT_LIMIT_PER_MINUTE', 8);
    $emailLimit = pl_env_int('PROSPECTLAB_FREE_AUDIT_EMAIL_LIMIT', 1);
    $emailWindow = pl_env_int('PROSPECTLAB_FREE_AUDIT_EMAIL_WINDOW_SEC', 86400);
    $siteLimit = pl_env_int('PROSPECTLAB_FREE_AUDIT_WEBSITE_LIMIT', 2);
    $siteWindow = pl_env_int('PROSPECTLAB_FREE_AUDIT_WEBSITE_WINDOW_SEC', 86400);

    pl_rate_limit_or_die('free_audit:ip:sec:' . $ip, $perSec, 1);
    pl_rate_limit_or_die('free_audit:ip:min:' . $ip, $perMin, 60);
    pl_rate_limit_or_die(
        'free_audit:email:' . sha1(strtolower($email)),
        $emailLimit,
        $emailWindow,
        'Un audit gratuit a déjà été demandé récemment pour cette adresse email. Réessayez demain.'
    );
    if ($websiteHost !== '') {
        pl_rate_limit_or_die(
            'free_audit:host:' . sha1(strtolower($websiteHost)),
            $siteLimit,
            $siteWindow,
            'Un audit pour ce site a déjà été demandé récemment. Réessayez plus tard.'
        );
    }
}

function pl_normalize_website(string $url): string
{
    $url = trim(preg_replace('/[\r\n]+/', '', $url));
    if ($url === '') {
        return '';
    }
    if (!preg_match('#^https?://#i', $url)) {
        $url = 'https://' . ltrim($url, '/');
    }
    if (!filter_var($url, FILTER_VALIDATE_URL)) {
        return '';
    }
    return $url;
}

function pl_website_host(string $website): string
{
    $host = parse_url($website, PHP_URL_HOST);
    if (!is_string($host) || $host === '') {
        return '';
    }
    return strtolower(preg_replace('/^www\./i', '', $host));
}

/**
 * Accepte une URL http(s) ou un nom de domaine (parametre GET website).
 */
function pl_sanitize_website_query(string $website): string
{
    $website = trim(preg_replace('/[\r\n]+/', '', $website));
    if ($website === '') {
        return '';
    }
    if (preg_match('#^https?://#i', $website)) {
        return pl_normalize_website($website);
    }
    if (str_contains($website, '/')) {
        return '';
    }
    $domain = strtolower($website);
    if (!filter_var($domain, FILTER_VALIDATE_DOMAIN, FILTER_FLAG_HOSTNAME)) {
        return '';
    }
    return pl_normalize_website($domain);
}

/**
 * @return list<string>
 */
function pl_website_lookup_candidates(string $website): array
{
    $raw = trim(preg_replace('/[\r\n]+/', '', $website));
    if ($raw === '') {
        return [];
    }

    $normalized = pl_sanitize_website_query($raw);
    if ($normalized === '') {
        return [];
    }

    $host = pl_website_host($normalized);
    $candidates = [];
    $add = static function (string $value) use (&$candidates): void {
        $value = trim($value);
        if ($value !== '' && !in_array($value, $candidates, true)) {
            $candidates[] = $value;
        }
    };

    $add($normalized);
    if ($raw !== $normalized) {
        $add($raw);
    }
    if ($host === '') {
        return $candidates;
    }

    $add($host);
    foreach (['https', 'http'] as $scheme) {
        foreach (['', 'www.'] as $prefix) {
            $add($scheme . '://' . $prefix . $host);
            $add($scheme . '://' . $prefix . $host . '/');
        }
    }

    return $candidates;
}

/**
 * @param array<string, mixed> $data
 */
function pl_extract_entreprise_website(array $data): string
{
    $paths = [
        ['data', 'website'],
        ['data', 'entreprise', 'website'],
        ['entreprise', 'website'],
        ['website'],
    ];
    foreach ($paths as $path) {
        $cur = $data;
        $ok = true;
        foreach ($path as $segment) {
            if (!is_array($cur) || !array_key_exists($segment, $cur)) {
                $ok = false;
                break;
            }
            $cur = $cur[$segment];
        }
        if ($ok && is_string($cur) && trim($cur) !== '') {
            $stored = pl_sanitize_website_query($cur);
            if ($stored !== '') {
                return $stored;
            }
        }
    }
    return '';
}

/**
 * Recherche un rapport ProspectLab en essayant plusieurs formes d'URL
 * puis un fallback entreprises/by-website.
 *
 * @return array{ok: bool, status: int, body: string, matched_website: string, error: string}
 */
function pl_fetch_website_analysis(string $website, string $full = '1'): array
{
    $fail = [
        'ok' => false,
        'status' => 404,
        'body' => '',
        'matched_website' => '',
        'error' => 'Aucun rapport trouvé pour ce site.',
    ];

    $token = pl_token();
    if ($token === '' || $token === 'REPLACE_ME') {
        return array_merge($fail, ['status' => 500, 'error' => 'Token API non configuré côté serveur.']);
    }

    $full = ($full === '0' || $full === '1') ? $full : '1';
    $endpoint = pl_website_analysis_endpoint();
    $tried = [];

    $tryOne = function (string $candidate) use ($endpoint, $full, &$tried): ?array {
        if ($candidate === '' || in_array($candidate, $tried, true)) {
            return null;
        }
        $tried[] = $candidate;
        $url = $endpoint . '?website=' . rawurlencode($candidate) . '&full=' . rawurlencode($full);
        $res = pl_http('GET', $url, null, 45);
        if ($res['ok'] && is_string($res['body']) && trim($res['body']) !== '') {
            return [
                'ok' => true,
                'status' => $res['status'],
                'body' => $res['body'],
                'matched_website' => $candidate,
                'error' => '',
            ];
        }
        if (!in_array((int) $res['status'], [400, 404], true)) {
            return [
                'ok' => false,
                'status' => (int) ($res['status'] ?: 502),
                'body' => is_string($res['body']) ? $res['body'] : '',
                'matched_website' => '',
                'error' => $res['error'] !== '' ? $res['error'] : 'Erreur API ProspectLab',
            ];
        }
        return null;
    };

    foreach (pl_website_lookup_candidates($website) as $candidate) {
        $hit = $tryOne($candidate);
        if ($hit !== null) {
            return $hit;
        }
    }

    $host = pl_website_host(pl_sanitize_website_query($website));
    $hostCandidates = array_values(array_unique(array_filter([
        $host,
        $host !== '' ? 'www.' . $host : '',
    ])));

    foreach ($hostCandidates as $hostTry) {
        $byUrl = pl_api_base() . '/entreprises/by-website?website=' . rawurlencode($hostTry);
        $byRes = pl_http('GET', $byUrl, null, 20);
        if (!$byRes['ok'] || !is_array($byRes['data'])) {
            continue;
        }
        $stored = pl_extract_entreprise_website($byRes['data']);
        if ($stored === '') {
            continue;
        }
        $hit = $tryOne($stored);
        if ($hit !== null) {
            return $hit;
        }
    }

    return $fail;
}

function pl_auth_headers(): array
{
    $headers = ['Accept: application/json'];
    $auditKey = pl_website_audit_lead_key();
    if ($auditKey !== '') {
        $headers[] = 'X-Website-Audit-Key: ' . $auditKey;
    }
    $token = pl_token();
    if ($token !== '' && $token !== 'REPLACE_ME') {
        $headers[] = 'Authorization: Bearer ' . $token;
    }
    return $headers;
}

/**
 * @param array<string, mixed>|null $jsonBody
 * @return array{ok: bool, status: int, data: array<string, mixed>|null, body: string, error: string}
 */
function pl_http(string $method, string $url, ?array $jsonBody = null, int $timeout = 45): array
{
    $headers = pl_auth_headers();
    if ($jsonBody !== null) {
        $headers[] = 'Content-Type: application/json; charset=utf-8';
    }

    if (function_exists('curl_init')) {
        $ch = curl_init();
        $opts = [
            CURLOPT_URL => $url,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_FOLLOWLOCATION => true,
            CURLOPT_CONNECTTIMEOUT => 8,
            CURLOPT_TIMEOUT => $timeout,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_CUSTOMREQUEST => strtoupper($method),
        ];
        if ($jsonBody !== null) {
            $opts[CURLOPT_POSTFIELDS] = json_encode($jsonBody, JSON_UNESCAPED_UNICODE);
        }
        curl_setopt_array($ch, $opts);
        $body = curl_exec($ch);
        $err = curl_error($ch);
        $status = (int) curl_getinfo($ch, CURLINFO_RESPONSE_CODE);
        curl_close($ch);
        if ($body === false) {
            return ['ok' => false, 'status' => 502, 'data' => null, 'body' => '', 'error' => 'cURL: ' . ($err ?: 'inconnue')];
        }
    } else {
        $headerLines = implode("\r\n", $headers);
        $content = null;
        if ($jsonBody !== null) {
            $content = json_encode($jsonBody, JSON_UNESCAPED_UNICODE);
            $headerLines .= "\r\nContent-Length: " . strlen((string) $content);
        }
        $context = stream_context_create([
            'http' => [
                'method' => strtoupper($method),
                'header' => $headerLines . "\r\n",
                'content' => $content,
                'ignore_errors' => true,
                'timeout' => $timeout,
            ],
            'ssl' => [
                'verify_peer' => true,
                'verify_peer_name' => true,
            ],
        ]);
        $body = @file_get_contents($url, false, $context);
        if ($body === false) {
            return ['ok' => false, 'status' => 502, 'data' => null, 'body' => '', 'error' => 'Erreur HTTP (file_get_contents).'];
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

    $decoded = json_decode((string) $body, true);
    $data = is_array($decoded) ? $decoded : null;

    if ($status >= 200 && $status < 300) {
        return ['ok' => true, 'status' => $status, 'data' => $data, 'body' => (string) $body, 'error' => ''];
    }

    $msg = 'Erreur API ProspectLab';
    if (is_array($data)) {
        if (isset($data['message']) && is_string($data['message']) && $data['message'] !== '') {
            $msg = $data['message'];
        } elseif (isset($data['error']) && is_string($data['error']) && $data['error'] !== '') {
            $msg = $data['error'];
        }
    }
    if ($status === 429) {
        $msg = 'Limite atteinte côté analyse. ' . $msg;
    }

    return ['ok' => false, 'status' => $status, 'data' => $data, 'body' => (string) $body, 'error' => $msg];
}

/**
 * Détermine si la réponse ProspectLab indique une analyse planifiée / en cours.
 *
 * @param array<string, mixed>|null $data
 */
function pl_response_queued(?array $data, int $httpStatus = 200): bool
{
    if ($httpStatus === 202) {
        return true;
    }
    if ($data === null) {
        return false;
    }
    if (!empty($data['skipped_analysis'])) {
        return true;
    }
    if (isset($data['task_id']) && is_string($data['task_id']) && $data['task_id'] !== '') {
        return true;
    }
    foreach (['queued', 'accepted', 'scheduled', 'success'] as $flag) {
        if (array_key_exists($flag, $data) && $data[$flag] === true) {
            return true;
        }
    }
    if (isset($data['status']) && is_string($data['status'])) {
        $st = strtolower($data['status']);
        if (in_array($st, ['queued', 'pending', 'processing', 'started', 'accepted', 'ok', 'success'], true)) {
            return true;
        }
    }
    if (isset($data['email_sent']) && $data['email_sent'] === true) {
        return true;
    }
    return false;
}

/**
 * POST /api/public/website-audit-report — PDF + email (audit gratuit).
 * POST /api/public/website-audit-report/complete — mode complet, réponse 202 (audit premium).
 *
 * @return array{ok: bool, queued: bool, source: string, error: string, status: int, task_id: string, skipped_analysis: bool}
 */
function pl_request_website_audit_report(string $website, string $email, bool $completeMode = false): array
{
    $empty = [
        'ok' => false,
        'queued' => false,
        'source' => $completeMode ? 'website-audit-report/complete' : 'website-audit-report',
        'error' => '',
        'status' => 0,
        'task_id' => '',
        'skipped_analysis' => false,
    ];

    if (!pl_has_audit_auth()) {
        $empty['error'] = 'Authentification API audit non configurée.';
        return $empty;
    }

    $payload = pl_website_audit_report_payload($website, $email);
    if ($completeMode) {
        $extra = trim((string) (getenv('PROSPECTLAB_AUDIT_EXTRA_INSTRUCTIONS') ?: ''));
        if ($extra !== '') {
            $payload['extra_instructions'] = $extra;
        }
    }

    $url = pl_website_audit_report_url($completeMode);
    $timeout = $completeMode ? 45 : 120;
    $res = pl_http('POST', $url, $payload, $timeout);

    if (!$res['ok']) {
        $empty['error'] = $res['error'];
        $empty['status'] = $res['status'];
        return $empty;
    }

    $data = $res['data'];
    $taskId = is_array($data) && isset($data['task_id']) ? trim((string) $data['task_id']) : '';
    $skipped = is_array($data) && !empty($data['skipped_analysis']);

    return [
        'ok' => true,
        'queued' => pl_response_queued($data, $res['status']),
        'source' => $completeMode ? 'website-audit-report/complete' : 'website-audit-report',
        'error' => '',
        'status' => $res['status'],
        'task_id' => $taskId,
        'skipped_analysis' => $skipped,
    ];
}

/**
 * GET /api/public/website-audit-report/<task_id> — suivi Celery (PENDING, STARTED, SUCCESS, FAILURE).
 *
 * @return array{ok: bool, status: int, data: array<string, mixed>|null, error: string}
 */
function pl_get_website_audit_task(string $taskId): array
{
    $taskId = trim($taskId);
    if ($taskId === '' || !preg_match('/^[a-zA-Z0-9_-]{8,128}$/', $taskId)) {
        return ['ok' => false, 'status' => 400, 'data' => null, 'error' => 'task_id invalide.'];
    }
    if (!pl_has_audit_auth()) {
        return ['ok' => false, 'status' => 500, 'data' => null, 'error' => 'Authentification API audit non configurée.'];
    }

    $url = pl_website_audit_report_url(false) . '/' . rawurlencode($taskId);
    $res = pl_http('GET', $url, null, 30);
    if (!$res['ok']) {
        return ['ok' => false, 'status' => $res['status'], 'data' => $res['data'], 'error' => $res['error']];
    }
    return ['ok' => true, 'status' => $res['status'], 'data' => $res['data'], 'error' => ''];
}

/** Lance l’audit gratuit (PDF + email via website-audit-report). */
function pl_request_free_audit(string $website, string $email, string $source = 'danielcraft_audit_gratuit'): array
{
    unset($source);
    return pl_request_website_audit_report($website, $email, false);
}
