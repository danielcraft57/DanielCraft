<?php
/**
 * Lookup commande livre (code ou token) — JSON pour /livres/telechargement/.
 *
 * POST JSON (formulaire code) :
 *   code, form_ts, company (honeypot), website (honeypot), source?=form|link
 *
 * GET (lien e-mail / auto) :
 *   ?token=…  (prioritaire)  |  ?code=… (compte aussi comme essai)
 *
 * Securite : max essais / IP → lock 24 h, honeypot, delai mini formulaire, rate soft.
 */

declare(strict_types=1);

require_once __DIR__ . '/livre-download-common.php';

api_bootstrap_env();
api_json_headers();

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204);
    exit;
}

$method = strtoupper((string) ($_SERVER['REQUEST_METHOD'] ?? 'GET'));
if ($method !== 'GET' && $method !== 'POST') {
    http_response_code(405);
    echo json_encode(['ok' => false, 'error' => 'Methode non autorisee'], JSON_UNESCAPED_UNICODE);
    exit;
}

$ip = livre_download_client_ip();

/**
 * @param array<string, mixed> $extra
 */
function livre_download_lookup_json(int $status, array $payload): void
{
    http_response_code($status);
    echo json_encode($payload, JSON_UNESCAPED_UNICODE);
    exit;
}

$lock = livre_download_lock_status($ip);
if ($lock['locked']) {
    livre_download_lookup_json(429, [
        'ok' => false,
        'locked' => true,
        'retry_after' => $lock['retry_after'],
        'locked_until' => $lock['locked_until'],
        'attempts_left' => 0,
        'error' => 'Trop d\'essais incorrects. Acces bloque pendant '
            . livre_download_format_retry_human($lock['retry_after'])
            . '. Ecris a contact@danielcraft.fr si besoin.',
    ]);
}

if (!livre_download_rate_allow('lookup:' . $ip, 30, 900)) {
    livre_download_lookup_json(429, [
        'ok' => false,
        'locked' => false,
        'error' => 'Trop de requetes. Reessaie dans quelques minutes.',
        'attempts_left' => $lock['attempts_left'],
    ]);
}

$code = '';
$token = '';
$honeypotCompany = '';
$honeypotWebsite = '';
$formTs = 0;
$source = 'form';
$strictTiming = true;

if ($method === 'POST') {
    $contentType = isset($_SERVER['CONTENT_TYPE']) ? strtolower((string) $_SERVER['CONTENT_TYPE']) : '';
    $decoded = null;
    if (str_contains($contentType, 'application/json')) {
        $raw = file_get_contents('php://input');
        $decoded = json_decode($raw ?: '', true);
    }
    if (is_array($decoded)) {
        $code = isset($decoded['code']) ? trim((string) $decoded['code']) : '';
        $token = isset($decoded['token']) ? trim((string) $decoded['token']) : '';
        $honeypotCompany = isset($decoded['company']) ? (string) $decoded['company'] : '';
        $honeypotWebsite = isset($decoded['website']) ? (string) $decoded['website'] : '';
        $formTs = isset($decoded['form_ts']) ? (int) $decoded['form_ts'] : 0;
        $source = isset($decoded['source']) ? trim((string) $decoded['source']) : 'form';
    } else {
        $code = isset($_POST['code']) ? trim((string) $_POST['code']) : '';
        $token = isset($_POST['token']) ? trim((string) $_POST['token']) : '';
        $honeypotCompany = isset($_POST['company']) ? (string) $_POST['company'] : '';
        $honeypotWebsite = isset($_POST['website']) ? (string) $_POST['website'] : '';
        $formTs = isset($_POST['form_ts']) ? (int) $_POST['form_ts'] : 0;
        $source = isset($_POST['source']) ? trim((string) $_POST['source']) : 'form';
    }
    // Lien auto (token e-mail / retour Stripe) : timing assoupli
    if ($source === 'link' || $source === 'auto') {
        $strictTiming = false;
    }
    $guards = livre_download_verify_form_guards($honeypotCompany, $honeypotWebsite, $formTs, $strictTiming);
    if (!$guards['ok']) {
        if ($guards['error'] === 'honeypot') {
            // Faux succes pour bots
            livre_download_lookup_json(200, [
                'ok' => true,
                'code' => 'DC-XXXX-XXXX',
                'title' => 'Livre PDF',
                'kind' => 'livre',
                'cover' => '',
                'files' => [],
                'days_left' => 30,
            ]);
        }
        livre_download_lookup_json(400, [
            'ok' => false,
            'error' => $guards['error'],
            'attempts_left' => $lock['attempts_left'],
        ]);
    }
} else {
    // GET : reserve aux liens (token prioritaire). Compte comme essai si echec.
    $code = isset($_GET['code']) ? trim((string) $_GET['code']) : '';
    $token = isset($_GET['token']) ? trim((string) $_GET['token']) : '';
    $source = 'link';
}

if ($token === '' && $code === '') {
    livre_download_lookup_json(400, [
        'ok' => false,
        'error' => 'Indique un code de telechargement.',
        'attempts_left' => $lock['attempts_left'],
    ]);
}

$record = null;
if ($token !== '') {
    if (!preg_match('/^[a-f0-9]{48,128}$/i', $token)) {
        $status = livre_download_record_failure($ip);
        livre_download_lookup_json(404, [
            'ok' => false,
            'locked' => $status['locked'],
            'retry_after' => $status['retry_after'],
            'attempts_left' => $status['attempts_left'],
            'error' => $status['locked']
                ? ('Trop d\'essais incorrects. Acces bloque pendant '
                    . livre_download_format_retry_human($status['retry_after']) . '.')
                : 'Lien invalide ou expire.',
        ]);
    }
    $record = livre_download_load_token(strtolower($token));
} else {
    $norm = livre_download_normalize_code($code);
    if ($norm === '') {
        $status = livre_download_record_failure($ip, $code);
        livre_download_lookup_json(400, [
            'ok' => false,
            'locked' => $status['locked'],
            'retry_after' => $status['retry_after'],
            'attempts_left' => $status['attempts_left'],
            'error' => $status['locked']
                ? ('Trop d\'essais incorrects. Acces bloque pendant '
                    . livre_download_format_retry_human($status['retry_after']) . '.')
                : 'Code invalide. Format attendu : DC-XXXX-XXXX.',
        ]);
    }

    // Lock par code (si trop d'essais globaux sur ce code)
    $codeState = livre_download_security_read('code', $norm);
    if ((int) ($codeState['locked_until'] ?? 0) > time()) {
        $retry = (int) $codeState['locked_until'] - time();
        livre_download_lookup_json(429, [
            'ok' => false,
            'locked' => true,
            'retry_after' => $retry,
            'attempts_left' => 0,
            'error' => 'Ce code est temporairement verrouille apres trop d\'essais. Reessaie dans '
                . livre_download_format_retry_human($retry) . '.',
        ]);
    }

    $record = livre_download_load_by_code($norm);
}

if ($record === null) {
    $status = livre_download_record_failure($ip, $code);
    $msg = 'Code invalide ou expire. Verifie ta saisie, ou ecris a contact@danielcraft.fr.';
    if ($status['locked']) {
        $msg = 'Trop d\'essais incorrects. Acces bloque pendant '
            . livre_download_format_retry_human($status['retry_after'])
            . '. Ecris a contact@danielcraft.fr si besoin.';
    } elseif ($status['attempts_left'] <= 2 && $status['attempts_left'] > 0) {
        $msg .= ' Il te reste ' . $status['attempts_left'] . ' essai'
            . ($status['attempts_left'] > 1 ? 's' : '') . '.';
    }
    livre_download_lookup_json(404, [
        'ok' => false,
        'locked' => $status['locked'],
        'retry_after' => $status['retry_after'],
        'attempts_left' => $status['attempts_left'],
        'error' => $msg,
    ]);
}

livre_download_clear_failures($ip);
$payload = livre_download_public_payload($record);
$payload['attempts_left'] = livre_download_max_attempts();
livre_download_lookup_json(200, $payload);
