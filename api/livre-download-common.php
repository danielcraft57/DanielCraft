<?php
/**
 * Tokens + codes uniques de telechargement PDF livres.
 * Code affiche : DC-XXXX-XXXX (saisie facile)
 * Token technique : hex 64 (lien securise)
 */

declare(strict_types=1);

require_once __DIR__ . '/stripe-common.php';

/** Duree de validite du lien (secondes). */
function livre_download_token_ttl_seconds(): int
{
    $raw = getenv('LIVRE_DOWNLOAD_TTL_DAYS') ?: '30';
    $days = is_numeric($raw) ? (int) $raw : 30;
    if ($days < 1) {
        $days = 30;
    }
    if ($days > 365) {
        $days = 365;
    }

    return $days * 86400;
}

function livre_download_storage_dir(): string
{
    $custom = trim((string) (getenv('LIVRE_DOWNLOAD_DIR') ?: ''));
    if ($custom !== '') {
        if (!is_dir($custom)) {
            @mkdir($custom, 0700, true);
        }

        return rtrim($custom, DIRECTORY_SEPARATOR);
    }

    $dir = rtrim(sys_get_temp_dir(), DIRECTORY_SEPARATOR) . DIRECTORY_SEPARATOR . 'dc_livre_dl';
    if (!is_dir($dir)) {
        @mkdir($dir, 0700, true);
    }

    return $dir;
}

function livre_pdf_base_dir(): string
{
    $custom = trim((string) (getenv('LIVRE_PDF_DIR') ?: ''));
    if ($custom !== '' && is_dir($custom)) {
        return rtrim($custom, DIRECTORY_SEPARATOR);
    }

    $candidates = [
        __DIR__ . '/../livres-formation/pdf',
        __DIR__ . '/../../livres-formation/pdf',
    ];
    foreach ($candidates as $path) {
        if (is_dir($path)) {
            return rtrim($path, DIRECTORY_SEPARATOR);
        }
    }

    return rtrim(__DIR__ . '/../livres-formation/pdf', DIRECTORY_SEPARATOR);
}

/**
 * @return list<array{filename: string, label: string, cover?: string}>
 */
function livre_resolve_pdf_files(array $item): array
{
    $isPack = (($item['kind'] ?? '') === 'pack') || str_starts_with((string) ($item['slug'] ?? ''), 'pack-');
    $files = [];

    if ($isPack && is_array($item['book_slugs'] ?? null)) {
        foreach ($item['book_slugs'] as $bookSlug) {
            $bookSlug = trim((string) $bookSlug);
            if ($bookSlug === '') {
                continue;
            }
            $book = stripe_find_livre_item($bookSlug);
            if (!is_array($book)) {
                continue;
            }
            $pdf = trim((string) ($book['pdf'] ?? ''));
            if ($pdf === '' || !preg_match('/^[a-z0-9._-]+\.pdf$/i', $pdf)) {
                continue;
            }
            $entry = [
                'filename' => $pdf,
                'label' => trim((string) ($book['title'] ?? $bookSlug)),
            ];
            $cover = trim((string) ($book['cover'] ?? ''));
            if ($cover !== '') {
                $entry['cover'] = $cover;
            }
            $files[] = $entry;
        }

        return $files;
    }

    $pdf = trim((string) ($item['pdf'] ?? ''));
    if ($pdf !== '' && preg_match('/^[a-z0-9._-]+\.pdf$/i', $pdf)) {
        $entry = [
            'filename' => $pdf,
            'label' => trim((string) ($item['title'] ?? $pdf)),
        ];
        $cover = trim((string) ($item['cover'] ?? ''));
        if ($cover !== '') {
            $entry['cover'] = $cover;
        }
        $files[] = $entry;
    }

    return $files;
}

function livre_pdf_absolute_path(string $filename): string
{
    $filename = basename($filename);
    if (!preg_match('/^[a-z0-9._-]+\.pdf$/i', $filename)) {
        return '';
    }

    $base = livre_pdf_base_dir();
    $path = $base . DIRECTORY_SEPARATOR . $filename;
    if (!is_file($path) || !is_readable($path)) {
        return '';
    }

    $realBase = realpath($base);
    $realPath = realpath($path);
    if ($realBase === false || $realPath === false) {
        return '';
    }
    if (!str_starts_with($realPath, $realBase . DIRECTORY_SEPARATOR) && $realPath !== $realBase) {
        return '';
    }

    return $realPath;
}

/** Alphabet Crockford-like (pas de 0/O/1/I/L). */
function livre_download_code_alphabet(): string
{
    return '23456789ABCDEFGHJKMNPQRSTUVWXYZ';
}

/**
 * Genere un code affiche DC-XXXX-XXXX.
 */
function livre_download_generate_code(): string
{
    $alphabet = livre_download_code_alphabet();
    $len = strlen($alphabet);
    $parts = ['', ''];
    for ($p = 0; $p < 2; $p++) {
        for ($i = 0; $i < 4; $i++) {
            $parts[$p] .= $alphabet[random_int(0, $len - 1)];
        }
    }

    return 'DC-' . $parts[0] . '-' . $parts[1];
}

/**
 * Normalise saisie utilisateur → DC-XXXX-XXXX ou ''.
 */
function livre_download_normalize_code(string $raw): string
{
    $raw = strtoupper(trim($raw));
    $raw = preg_replace('/[^A-Z0-9]/', '', $raw) ?? '';
    if (str_starts_with($raw, 'DC')) {
        $raw = substr($raw, 2);
    }
    if (strlen($raw) !== 8) {
        return '';
    }
    if (!preg_match('/^[23456789ABCDEFGHJKMNPQRSTUVWXYZ]{8}$/', $raw)) {
        return '';
    }

    return 'DC-' . substr($raw, 0, 4) . '-' . substr($raw, 4, 4);
}

function livre_download_code_key(string $code): string
{
    $norm = livre_download_normalize_code($code);
    if ($norm === '') {
        return '';
    }

    return str_replace('-', '', $norm);
}

function livre_download_token_file(string $token): string
{
    $token = strtolower(trim($token));
    if (!preg_match('/^[a-f0-9]{48,128}$/', $token)) {
        return '';
    }

    return livre_download_storage_dir() . DIRECTORY_SEPARATOR . 'tok_' . hash('sha256', $token) . '.json';
}

function livre_download_code_index_file(string $code): string
{
    $key = livre_download_code_key($code);
    if ($key === '') {
        return '';
    }

    return livre_download_storage_dir() . DIRECTORY_SEPARATOR . 'code_' . $key . '.json';
}

function livre_download_session_index_file(string $sessionId): string
{
    if (!preg_match('/^cs_[a-zA-Z0-9_]+$/', $sessionId)) {
        return '';
    }

    return livre_download_storage_dir() . DIRECTORY_SEPARATOR . 'sess_' . sha1($sessionId) . '.json';
}

/**
 * @return array<string, mixed>|null
 */
function livre_download_load_record_from_file(string $file): ?array
{
    if ($file === '' || !is_file($file)) {
        return null;
    }
    $raw = @file_get_contents($file);
    $data = is_string($raw) ? json_decode($raw, true) : null;
    if (!is_array($data)) {
        return null;
    }
    $expires = (int) ($data['expires_at'] ?? 0);
    if ($expires > 0 && time() > $expires) {
        return null;
    }

    return $data;
}

/**
 * @return array<string, mixed>|null
 */
function livre_download_load_token(string $token): ?array
{
    $file = livre_download_token_file($token);
    $data = livre_download_load_record_from_file($file);
    if ($data === null) {
        return null;
    }
    if (($data['token'] ?? '') !== strtolower(trim($token))) {
        return null;
    }

    return $data;
}

/**
 * @return array<string, mixed>|null
 */
function livre_download_load_by_code(string $code): ?array
{
    $norm = livre_download_normalize_code($code);
    if ($norm === '') {
        return null;
    }
    $indexFile = livre_download_code_index_file($norm);
    $index = livre_download_load_record_from_file($indexFile);
    if ($index === null) {
        return null;
    }
    $token = isset($index['token']) ? strtolower(trim((string) $index['token'])) : '';
    if ($token === '') {
        return null;
    }
    $record = livre_download_load_token($token);
    if ($record === null) {
        return null;
    }
    if (livre_download_normalize_code((string) ($record['code'] ?? '')) !== $norm) {
        return null;
    }

    return $record;
}

/**
 * @return array<string, mixed>|null
 */
function livre_download_load_by_session(string $sessionId): ?array
{
    $indexFile = livre_download_session_index_file($sessionId);
    $index = livre_download_load_record_from_file($indexFile);
    if ($index === null) {
        return null;
    }
    $token = isset($index['token']) ? strtolower(trim((string) $index['token'])) : '';
    if ($token === '') {
        return null;
    }

    return livre_download_load_token($token);
}

/**
 * @param list<array{filename: string, label: string, cover?: string}> $files
 * @return array{ok: bool, token: string, code: string, error: string}
 */
function livre_download_create_token(
    string $sessionId,
    string $email,
    string $livreSlug,
    string $title,
    array $files,
    string $cover = '',
    string $kind = 'livre'
): array {
    $empty = ['ok' => false, 'token' => '', 'code' => '', 'error' => ''];
    if ($files === []) {
        $empty['error'] = 'Aucun PDF associe a cette commande.';
        return $empty;
    }
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $empty['error'] = 'Email client invalide.';
        return $empty;
    }

    $existing = livre_download_load_by_session($sessionId);
    if ($existing !== null) {
        return [
            'ok' => true,
            'token' => (string) ($existing['token'] ?? ''),
            'code' => (string) ($existing['code'] ?? ''),
            'error' => '',
        ];
    }

    $token = bin2hex(random_bytes(32));
    $code = '';
    for ($attempt = 0; $attempt < 12; $attempt++) {
        $candidate = livre_download_generate_code();
        $indexPath = livre_download_code_index_file($candidate);
        if ($indexPath !== '' && !is_file($indexPath)) {
            $code = $candidate;
            break;
        }
    }
    if ($code === '') {
        $empty['error'] = 'Impossible de generer un code unique.';
        return $empty;
    }

    $now = time();
    $record = [
        'token' => $token,
        'code' => $code,
        'session_id' => $sessionId,
        'email' => strtolower(trim($email)),
        'livre_slug' => $livreSlug,
        'title' => $title,
        'kind' => $kind === 'pack' ? 'pack' : 'livre',
        'cover' => $cover,
        'files' => $files,
        'created_at' => $now,
        'expires_at' => $now + livre_download_token_ttl_seconds(),
    ];

    $file = livre_download_token_file($token);
    if ($file === '') {
        $empty['error'] = 'Token invalide.';
        return $empty;
    }
    $written = @file_put_contents($file, json_encode($record, JSON_UNESCAPED_UNICODE), LOCK_EX);
    if ($written === false) {
        $empty['error'] = 'Stockage token impossible.';
        return $empty;
    }

    $codeIndex = livre_download_code_index_file($code);
    @file_put_contents($codeIndex, json_encode([
        'token' => $token,
        'code' => $code,
        'expires_at' => $record['expires_at'],
    ], JSON_UNESCAPED_UNICODE), LOCK_EX);

    $sessIndex = livre_download_session_index_file($sessionId);
    if ($sessIndex !== '') {
        @file_put_contents($sessIndex, json_encode([
            'token' => $token,
            'code' => $code,
            'expires_at' => $record['expires_at'],
        ], JSON_UNESCAPED_UNICODE), LOCK_EX);
    }

    return ['ok' => true, 'token' => $token, 'code' => $code, 'error' => ''];
}

function livre_download_page_url(string $code = '', string $token = ''): string
{
    $base = api_site_base() . '/livres/telechargement/';
    $norm = $code !== '' ? livre_download_normalize_code($code) : '';
    if ($norm !== '') {
        return $base . '?code=' . rawurlencode($norm);
    }
    $token = strtolower(trim($token));
    if ($token !== '' && preg_match('/^[a-f0-9]{48,128}$/', $token)) {
        return $base . '?token=' . rawurlencode($token);
    }

    return $base;
}

/** @deprecated Prefer livre_download_page_url — conserve pour compat e-mails anciens. */
function livre_download_public_url(string $token): string
{
    return livre_download_page_url('', $token);
}

function livre_download_file_url(string $token, string $filename = ''): string
{
    $url = api_site_base() . '/api/download-livre.php?token=' . rawurlencode($token);
    if ($filename !== '') {
        $url .= '&file=' . rawurlencode(basename($filename));
    }

    return $url;
}

/**
 * Payload public pour la page telechargement (pas de token en clair hors besoin download).
 *
 * @param array<string, mixed> $record
 * @return array<string, mixed>
 */
function livre_download_public_payload(array $record): array
{
    $token = (string) ($record['token'] ?? '');
    $code = (string) ($record['code'] ?? '');
    $filesOut = [];
    $files = is_array($record['files'] ?? null) ? $record['files'] : [];
    foreach ($files as $file) {
        if (!is_array($file)) {
            continue;
        }
        $filename = basename((string) ($file['filename'] ?? ''));
        if ($filename === '') {
            continue;
        }
        $filesOut[] = [
            'filename' => $filename,
            'label' => (string) ($file['label'] ?? $filename),
            'cover' => (string) ($file['cover'] ?? ''),
            'download_url' => livre_download_file_url($token, $filename),
        ];
    }

    $expiresAt = (int) ($record['expires_at'] ?? 0);
    $daysLeft = 0;
    if ($expiresAt > time()) {
        $daysLeft = (int) max(1, (int) ceil(($expiresAt - time()) / 86400));
    }

    return [
        'ok' => true,
        'code' => $code,
        'title' => (string) ($record['title'] ?? ''),
        'kind' => (string) ($record['kind'] ?? 'livre'),
        'cover' => (string) ($record['cover'] ?? ''),
        'livre_slug' => (string) ($record['livre_slug'] ?? ''),
        'expires_at' => $expiresAt,
        'days_left' => $daysLeft,
        'page_url' => livre_download_page_url($code, $token),
        'files' => $filesOut,
    ];
}

/* ===== Securite page telechargement (essais / lock / formulaire) ===== */

function livre_download_max_attempts(): int
{
    $raw = getenv('LIVRE_DOWNLOAD_MAX_ATTEMPTS') ?: '5';
    $n = is_numeric($raw) ? (int) $raw : 5;
    return max(3, min(20, $n));
}

function livre_download_lock_seconds(): int
{
    $raw = getenv('LIVRE_DOWNLOAD_LOCK_HOURS') ?: '24';
    $hours = is_numeric($raw) ? (int) $raw : 24;
    $hours = max(1, min(168, $hours));

    return $hours * 3600;
}

function livre_download_min_form_seconds(): int
{
    return 2;
}

function livre_download_client_ip(): string
{
    if (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
        $parts = explode(',', (string) $_SERVER['HTTP_X_FORWARDED_FOR']);
        if (!empty($parts[0])) {
            $ip = trim($parts[0]);
            if (filter_var($ip, FILTER_VALIDATE_IP)) {
                return $ip;
            }
        }
    }
    $remote = !empty($_SERVER['REMOTE_ADDR']) ? (string) $_SERVER['REMOTE_ADDR'] : 'unknown';
    if ($remote !== 'unknown' && filter_var($remote, FILTER_VALIDATE_IP)) {
        return $remote;
    }

    return 'unknown';
}

function livre_download_security_dir(): string
{
    $dir = rtrim(sys_get_temp_dir(), DIRECTORY_SEPARATOR) . DIRECTORY_SEPARATOR . 'dc_livre_sec';
    if (!is_dir($dir)) {
        @mkdir($dir, 0700, true);
    }

    return $dir;
}

function livre_download_security_file(string $kind, string $key): string
{
    return livre_download_security_dir() . DIRECTORY_SEPARATOR . $kind . '_' . sha1($key) . '.json';
}

/**
 * @return array{fails: list<int>, locked_until: int}
 */
function livre_download_security_read(string $kind, string $key): array
{
    $file = livre_download_security_file($kind, $key);
    $empty = ['fails' => [], 'locked_until' => 0];
    if (!is_file($file)) {
        return $empty;
    }
    $raw = @file_get_contents($file);
    $data = is_string($raw) ? json_decode($raw, true) : null;
    if (!is_array($data)) {
        return $empty;
    }
    $fails = [];
    if (isset($data['fails']) && is_array($data['fails'])) {
        foreach ($data['fails'] as $t) {
            $fails[] = (int) $t;
        }
    }

    return [
        'fails' => $fails,
        'locked_until' => (int) ($data['locked_until'] ?? 0),
    ];
}

/**
 * @param array{fails?: list<int>, locked_until?: int} $state
 */
function livre_download_security_write(string $kind, string $key, array $state): void
{
    $file = livre_download_security_file($kind, $key);
    @file_put_contents($file, json_encode([
        'fails' => array_values($state['fails'] ?? []),
        'locked_until' => (int) ($state['locked_until'] ?? 0),
        'updated_at' => time(),
    ], JSON_UNESCAPED_UNICODE), LOCK_EX);
}

/**
 * @return array{locked: bool, retry_after: int, attempts_left: int, locked_until: int}
 */
function livre_download_lock_status(?string $ip = null): array
{
    $ip = $ip ?? livre_download_client_ip();
    $state = livre_download_security_read('ip', $ip);
    $now = time();
    $lockedUntil = (int) ($state['locked_until'] ?? 0);
    if ($lockedUntil > $now) {
        return [
            'locked' => true,
            'retry_after' => $lockedUntil - $now,
            'attempts_left' => 0,
            'locked_until' => $lockedUntil,
        ];
    }

    $window = livre_download_lock_seconds();
    $cutoff = $now - $window;
    $fails = [];
    foreach ($state['fails'] as $t) {
        if ($t >= $cutoff) {
            $fails[] = $t;
        }
    }
    $max = livre_download_max_attempts();
    $left = max(0, $max - count($fails));

    return [
        'locked' => false,
        'retry_after' => 0,
        'attempts_left' => $left,
        'locked_until' => 0,
    ];
}

/**
 * Enregistre un echec ; verrouille 24 h apres le max d'essais.
 *
 * @return array{locked: bool, retry_after: int, attempts_left: int, locked_until: int}
 */
function livre_download_record_failure(?string $ip = null, string $codeHint = ''): array
{
    $ip = $ip ?? livre_download_client_ip();
    $now = time();
    $state = livre_download_security_read('ip', $ip);
    $window = livre_download_lock_seconds();
    $cutoff = $now - $window;
    $fails = [];
    foreach ($state['fails'] as $t) {
        if ($t >= $cutoff) {
            $fails[] = $t;
        }
    }
    $fails[] = $now;
    $max = livre_download_max_attempts();
    $lockedUntil = (int) ($state['locked_until'] ?? 0);
    if (count($fails) >= $max) {
        $lockedUntil = $now + $window;
        $fails = array_slice($fails, -$max);
    }
    livre_download_security_write('ip', $ip, [
        'fails' => $fails,
        'locked_until' => $lockedUntil,
    ]);

    if ($codeHint !== '') {
        $norm = livre_download_normalize_code($codeHint);
        if ($norm !== '') {
            $cState = livre_download_security_read('code', $norm);
            $cFails = [];
            foreach ($cState['fails'] as $t) {
                if ($t >= $cutoff) {
                    $cFails[] = $t;
                }
            }
            $cFails[] = $now;
            $cLocked = (int) ($cState['locked_until'] ?? 0);
            // Plus tolerant sur le code (partage / faute) : 12 essais / 24 h
            if (count($cFails) >= 12) {
                $cLocked = $now + $window;
                $cFails = array_slice($cFails, -12);
            }
            livre_download_security_write('code', $norm, [
                'fails' => $cFails,
                'locked_until' => $cLocked,
            ]);
        }
    }

    // Ralentit le brute-force (250–600 ms)
    usleep(random_int(250000, 600000));

    return livre_download_lock_status($ip);
}

function livre_download_clear_failures(?string $ip = null): void
{
    $ip = $ip ?? livre_download_client_ip();
    livre_download_security_write('ip', $ip, ['fails' => [], 'locked_until' => 0]);
}

/**
 * Soft rate-limit (fenetre glissante) — true si autorise.
 */
function livre_download_rate_allow(string $bucket, int $limit, int $windowSeconds): bool
{
    $file = livre_download_security_file('rl', $bucket);
    $now = time();
    $fp = @fopen($file, 'c+');
    if ($fp === false) {
        return true;
    }
    if (!flock($fp, LOCK_EX)) {
        fclose($fp);
        return true;
    }
    $raw = stream_get_contents($fp);
    $ts = [];
    if (is_string($raw) && trim($raw) !== '') {
        $decoded = json_decode($raw, true);
        if (is_array($decoded) && isset($decoded['ts']) && is_array($decoded['ts'])) {
            $cutoff = $now - $windowSeconds;
            foreach ($decoded['ts'] as $t) {
                $ti = (int) $t;
                if ($ti >= $cutoff) {
                    $ts[] = $ti;
                }
            }
        }
    }
    if (count($ts) >= $limit) {
        flock($fp, LOCK_UN);
        fclose($fp);

        return false;
    }
    $ts[] = $now;
    ftruncate($fp, 0);
    rewind($fp);
    fwrite($fp, json_encode(['ts' => $ts], JSON_UNESCAPED_UNICODE));
    fflush($fp);
    flock($fp, LOCK_UN);
    fclose($fp);

    return true;
}

/**
 * Verifie honeypot + delai mini formulaire.
 *
 * @return array{ok: bool, error: string}
 */
function livre_download_verify_form_guards(
    string $honeypotCompany,
    string $honeypotWebsite,
    int $formTs,
    bool $strictTiming = true
): array {
    $honeypotCompany = trim(strip_tags($honeypotCompany));
    $honeypotWebsite = trim(strip_tags($honeypotWebsite));
    if ($honeypotCompany !== '' || $honeypotWebsite !== '') {
        // Bot probable : faux succes silencieux cote caller (ne pas reveler)
        return ['ok' => false, 'error' => 'honeypot'];
    }

    if ($formTs <= 0) {
        return ['ok' => false, 'error' => 'Horodatage formulaire manquant. Recharge la page.'];
    }

    $now = time();
    $age = $now - $formTs;
    if ($age < 0 || $age > 7200) {
        return ['ok' => false, 'error' => 'Session formulaire expiree. Recharge la page.'];
    }
    if ($strictTiming && $age < livre_download_min_form_seconds()) {
        return ['ok' => false, 'error' => 'Un peu trop rapide — reessaie dans une seconde.'];
    }

    return ['ok' => true, 'error' => ''];
}

function livre_download_format_retry_human(int $seconds): string
{
    if ($seconds <= 60) {
        return 'une minute';
    }
    $hours = (int) ceil($seconds / 3600);
    if ($hours <= 1) {
        return 'environ 1 heure';
    }

    return 'environ ' . $hours . ' heures';
}
