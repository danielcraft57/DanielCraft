<?php
/**
 * Demande d'audit gratuit — déclenche l'analyse ProspectLab + envoi email du rapport.
 *
 * POST JSON ou form-data :
 *   website  (URL http(s))
 *   email    (destinataire du rapport)
 *
 * ProspectLab (configurable) :
 *   POST {PROSPECTLAB_API_BASE}/free-audit
 *   Corps : { "website": "...", "email": "...", "source": "danielcraft_audit_gratuit" }
 */

header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');

$origin = isset($_SERVER['HTTP_ORIGIN']) ? $_SERVER['HTTP_ORIGIN'] : '';
if (preg_match('#^https?://(www\.)?danielcraft\.fr$#', $origin)) {
    header('Access-Control-Allow-Origin: ' . $origin);
} elseif ($origin !== '' && preg_match('#^https?://(127\.0\.0\.1|localhost)(:\d+)?$#i', $origin)) {
    header('Access-Control-Allow-Origin: ' . $origin);
}
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'error' => 'Méthode non autorisée'], JSON_UNESCAPED_UNICODE);
    exit;
}

function load_dotenv_if_present(array $paths): void
{
    foreach ($paths as $envPath) {
        if (!is_string($envPath) || $envPath === '' || !is_file($envPath) || !is_readable($envPath)) {
            continue;
        }
        $lines = @file($envPath, FILE_IGNORE_NEW_LINES);
        if (!is_array($lines)) {
            continue;
        }
        foreach ($lines as $rawLine) {
            $line = trim((string) $rawLine);
            if ($line === '' || str_starts_with($line, '#')) {
                continue;
            }
            if (!preg_match('/^([A-Za-z_][A-Za-z0-9_]*)=(.*)$/', $line, $m)) {
                continue;
            }
            $key = $m[1];
            $val = trim($m[2]);
            if (($val !== '') && (
                (str_starts_with($val, '"') && str_ends_with($val, '"')) ||
                (str_starts_with($val, "'") && str_ends_with($val, "'"))
            )) {
                $val = substr($val, 1, -1);
            }
            if (getenv($key) !== false && getenv($key) !== '') {
                continue;
            }
            putenv($key . '=' . $val);
            $_ENV[$key] = $val;
            $_SERVER[$key] = $val;
        }
        break;
    }
}

load_dotenv_if_present([
    __DIR__ . '/../.env',
    __DIR__ . '/../../.env',
    getcwd() . '/.env',
]);

const LIMIT_PER_SECOND = 1;
const LIMIT_PER_MINUTE = 10;

function json_error(int $status, string $message): void
{
    http_response_code($status);
    echo json_encode(['success' => false, 'error' => $message], JSON_UNESCAPED_UNICODE);
    exit;
}

function client_ip(): string
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

function rate_limit_or_die(string $key, int $limit, int $windowSeconds): void
{
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
        json_error(429, 'Trop de demandes. Réessayez dans quelques minutes.');
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

function normalize_website(string $url): string
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

function esc(string $s): string
{
    return htmlspecialchars($s, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}

function send_simple_mail(string $to, string $subject, string $textBody, string $htmlBody, string $replyTo = ''): bool
{
    $fromName = getenv('CONTACT_FROM_NAME') ?: 'DanielCraft';
    $fromAddress = getenv('CONTACT_FROM_ADDRESS') ?: '';
    $defaultSender = getenv('MAIL_DEFAULT_SENDER') ?: '';

    if ($fromAddress === '' && $defaultSender !== '') {
        if (preg_match('/^(.*)<([^>]+)>$/', $defaultSender, $m)) {
            $fromName = trim($m[1], " \t\n\r\0\x0B\"'");
            $fromAddress = trim($m[2]);
        } elseif (filter_var(trim($defaultSender), FILTER_VALIDATE_EMAIL)) {
            $fromAddress = trim($defaultSender);
        }
    }
    if ($fromAddress === '') {
        $fromAddress = getenv('MAIL_DEFAULT_RECIPIENT') ?: 'contact@danielcraft.fr';
    }

    $boundary = 'bnd_' . bin2hex(random_bytes(8));
    $headers = [
        'From: ' . $fromName . ' <' . $fromAddress . '>',
        'MIME-Version: 1.0',
        'Content-Type: multipart/alternative; boundary="' . $boundary . '"',
    ];
    if ($replyTo !== '' && filter_var($replyTo, FILTER_VALIDATE_EMAIL)) {
        $headers[] = 'Reply-To: ' . $replyTo;
    }

    $subjectEncoded = '=?UTF-8?B?' . base64_encode($subject) . '?=';
    $mimeHeaders = implode("\r\n", $headers) . "\r\n" . 'To: ' . $to . "\r\n" . 'Subject: ' . $subjectEncoded;

    $mailBody =
        '--' . $boundary . "\r\n" .
        'Content-Type: text/plain; charset=UTF-8' . "\r\n\r\n" .
        $textBody . "\r\n\r\n" .
        '--' . $boundary . "\r\n" .
        'Content-Type: text/html; charset=UTF-8' . "\r\n\r\n" .
        $htmlBody . "\r\n\r\n" .
        '--' . $boundary . '--';

    $phpMailerBase = __DIR__ . '/vendor/phpmailer';
    if (file_exists($phpMailerBase . '/class.phpmailer.php')) {
        try {
            require_once $phpMailerBase . '/class.phpmailer.php';
            require_once $phpMailerBase . '/class.smtp.php';

            $mail = new PHPMailer(true);
            $mail->CharSet = 'UTF-8';
            $mail->setFrom($fromAddress, $fromName);
            $mail->addAddress($to);
            if ($replyTo !== '') {
                $mail->addReplyTo($replyTo);
            }
            $mail->Subject = $subject;
            $mail->Body = $htmlBody;
            $mail->AltBody = $textBody;
            $mail->isHTML(true);

            $smtpHost = getenv('MAIL_SERVER') ?: '';
            if ($smtpHost !== '') {
                $mail->isSMTP();
                $mail->Host = $smtpHost;
                $mail->Port = (int) (getenv('MAIL_PORT') ?: 587);
                $useTls = strtolower(trim((string) (getenv('MAIL_USE_TLS') ?: '')));
                $mail->SMTPAuth = true;
                $mail->Username = getenv('MAIL_USERNAME') ?: '';
                $mail->Password = getenv('MAIL_PASSWORD') ?: '';
                $mail->SMTPSecure = in_array($useTls, ['1', 'true', 'yes', 'on'], true) ? 'tls' : '';
            }

            return $mail->send();
        } catch (Throwable $e) {
            error_log('[request-free-audit] PHPMailer: ' . $e->getMessage());
        }
    }

    return @mail($to, $subjectEncoded, $mailBody, $mimeHeaders);
}

$ip = client_ip();
rate_limit_or_die('free_audit:' . $ip . ':sec', LIMIT_PER_SECOND, 1);
rate_limit_or_die('free_audit:' . $ip . ':min', LIMIT_PER_MINUTE, 60);

$contentType = isset($_SERVER['CONTENT_TYPE']) ? strtolower((string) $_SERVER['CONTENT_TYPE']) : '';
$website = '';
$email = '';
$honeypot = '';

if (str_contains($contentType, 'application/json')) {
    $raw = file_get_contents('php://input');
    $decoded = json_decode($raw ?: '', true);
    if (is_array($decoded)) {
        $website = isset($decoded['website']) ? (string) $decoded['website'] : '';
        $email = isset($decoded['email']) ? (string) $decoded['email'] : '';
        $honeypot = isset($decoded['company']) ? (string) $decoded['company'] : '';
    }
} else {
    $website = isset($_POST['website']) ? (string) $_POST['website'] : '';
    $email = isset($_POST['email']) ? (string) $_POST['email'] : '';
    $honeypot = isset($_POST['company']) ? (string) $_POST['company'] : '';
}

$website = normalize_website(trim(strip_tags($website)));
$email = trim((string) $email);
$honeypot = trim(strip_tags($honeypot));

if ($honeypot !== '') {
    echo json_encode([
        'success' => true,
        'message' => 'Merci ! Votre demande est enregistrée. Le rapport vous sera envoyé sous 48 h ouvrées.',
    ], JSON_UNESCAPED_UNICODE);
    exit;
}

$errors = [];
if ($website === '') {
    $errors[] = 'URL du site invalide. Utilisez une adresse http(s).';
}
if ($email === '') {
    $errors[] = 'L’email est obligatoire.';
} elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    $errors[] = 'L’email n’est pas valide.';
}
if (preg_match("/[\r\n]/", $email)) {
    $errors[] = 'Données invalides.';
}

if (!empty($errors)) {
    json_error(400, implode(' ', $errors));
}

$apiToken = getenv('PROSPECTLAB_TOKEN') ?: '';
$baseUrl = rtrim(getenv('PROSPECTLAB_BASE_URL') ?: 'https://prospectlab.danielcraft.fr', '/');
$apiBase = rtrim(getenv('PROSPECTLAB_API_BASE') ?: ($baseUrl . '/api/public'), '/');
$auditPath = trim((string) (getenv('PROSPECTLAB_FREE_AUDIT_PATH') ?: 'free-audit'), '/');
$auditUrl = $apiBase . '/' . $auditPath;

$plQueued = false;
$plError = '';

if ($apiToken !== '' && $apiToken !== 'REPLACE_ME') {
    $payload = json_encode([
        'website' => $website,
        'email' => $email,
        'source' => 'danielcraft_audit_gratuit',
        'send_report_by_email' => true,
    ], JSON_UNESCAPED_UNICODE);

    $ch = curl_init();
    curl_setopt_array($ch, [
        CURLOPT_URL => $auditUrl,
        CURLOPT_CUSTOMREQUEST => 'POST',
        CURLOPT_POSTFIELDS => $payload,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_CONNECTTIMEOUT => 8,
        CURLOPT_TIMEOUT => 30,
        CURLOPT_HTTPHEADER => [
            'Authorization: Bearer ' . $apiToken,
            'Accept: application/json',
            'Content-Type: application/json; charset=utf-8',
        ],
    ]);

    $body = curl_exec($ch);
    $err = curl_error($ch);
    $status = (int) curl_getinfo($ch, CURLINFO_RESPONSE_CODE);
    curl_close($ch);

    if ($body === false) {
        $plError = 'cURL: ' . ($err ?: 'inconnue');
    } elseif ($status >= 200 && $status < 300) {
        $plQueued = true;
    } else {
        $decoded = json_decode((string) $body, true);
        $plError = is_array($decoded)
            ? (string) ($decoded['error'] ?? $decoded['message'] ?? 'HTTP ' . $status)
            : 'HTTP ' . $status;
        error_log('[request-free-audit] ProspectLab ' . $status . ': ' . substr((string) $body, 0, 400));
    }
} else {
    $plError = 'Token ProspectLab non configuré';
}

$dryRunRaw = getenv('CONTACT_MAIL_DRY_RUN');
$dryRun = $dryRunRaw !== false && in_array(strtolower(trim((string) $dryRunRaw)), ['1', 'true', 'yes', 'on'], true);

$adminTo = getenv('CONTACT_TO') ?: getenv('MAIL_DEFAULT_RECIPIENT') ?: 'contact@danielcraft.fr';
$safeSite = esc($website);
$safeEmail = esc($email);

if (!$dryRun) {
    $adminSubject = 'Demande audit gratuit — ' . preg_replace('#^https?://#i', '', $website);
    $adminText = "Nouvelle demande d'audit gratuit\n\nSite : {$website}\nEmail : {$email}\nProspectLab : " . ($plQueued ? 'OK' : 'échec — ' . $plError) . "\n";
    $adminHtml = '<p><strong>Site :</strong> <a href="' . $safeSite . '">' . $safeSite . '</a></p>'
        . '<p><strong>Email :</strong> ' . $safeEmail . '</p>'
        . '<p><strong>ProspectLab :</strong> ' . esc($plQueued ? 'analyse planifiée' : $plError) . '</p>';
    send_simple_mail($adminTo, $adminSubject, $adminText, $adminHtml, $email);

    $userSubject = 'Votre audit gratuit est en cours — DanielCraft';
    $userText = "Bonjour,\n\nNous avons bien reçu votre demande d'audit gratuit pour :\n{$website}\n\n"
        . "Notre outil ProspectLab réalise l'analyse complète. Vous recevrez le rapport détaillé à cette adresse sous 48 h ouvrées.\n\n"
        . "En attendant, vous pouvez consulter un aperçu interactif :\nhttps://danielcraft.fr/analyse?website=" . rawurlencode($website) . "&full=1\n\n"
        . "DanielCraft\nhttps://danielcraft.fr\n";
    $userHtml = '<p>Bonjour,</p><p>Nous avons bien reçu votre demande d’audit gratuit pour :</p>'
        . '<p><a href="' . $safeSite . '"><strong>' . $safeSite . '</strong></a></p>'
        . '<p>L’analyse complète est en cours via <strong>ProspectLab</strong>. '
        . 'Vous recevrez le rapport détaillé à <strong>' . $safeEmail . '</strong> sous <strong>48 h ouvrées</strong>.</p>'
        . '<p><a href="https://danielcraft.fr/analyse?website=' . rawurlencode($website) . '&amp;full=1">Voir un aperçu interactif</a></p>'
        . '<p>À bientôt,<br>DanielCraft</p>';
    send_simple_mail($email, $userSubject, $userText, $userHtml);
}

$response = [
    'success' => true,
    'queued' => $plQueued,
    'message' => 'Merci ! Votre demande est enregistrée. Le rapport complet vous sera envoyé par email sous 48 h ouvrées.',
];

if ($dryRun) {
    $response['dry_run'] = true;
}

echo json_encode($response, JSON_UNESCAPED_UNICODE);
