<?php
/**
 * Demande d'audit gratuit — lance l'analyse ProspectLab + envoi du rapport par email.
 *
 * POST JSON ou form-data :
 *   website  (URL http(s))
 *   email    (destinataire du rapport)
 *   company  (honeypot, doit rester vide)
 *
 * ProspectLab (doc API) :
 *   POST /api/public/website-audit-report
 *   Corps JSON : website, email (+ options scraping optionnelles via .env)
 *   Auth : Authorization: Bearer PROSPECTLAB_TOKEN et/ou X-Website-Audit-Key
 *
 * Limites (fichiers temp, comme les autres endpoints) :
 *   - par IP (seconde / minute)
 *   - par email (fenêtre configurable, défaut 24 h)
 *   - par site audité (hôte, fenêtre configurable)
 */

declare(strict_types=1);

require_once __DIR__ . '/prospectlab-common.php';

pl_bootstrap();
api_json_headers();

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    pl_json_error(405, 'Méthode non autorisée');
}

function audit_esc(string $s): string
{
    return htmlspecialchars($s, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}

function audit_send_simple_mail(string $to, string $subject, string $textBody, string $htmlBody, string $replyTo = ''): bool
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
    if ($website === '' && isset($_POST['site_url'])) {
        $website = (string) $_POST['site_url'];
    }
    $email = isset($_POST['email']) ? (string) $_POST['email'] : '';
    $honeypot = isset($_POST['company']) ? (string) $_POST['company'] : '';
}

$website = pl_normalize_website(trim(strip_tags($website)));
$email = trim((string) $email);
$honeypot = trim(strip_tags($honeypot));

if ($honeypot !== '') {
    echo json_encode([
        'success' => true,
        'message' => 'Merci ! Votre audit arrive dans votre boîte mail sous 24 h ouvrées.',
    ], JSON_UNESCAPED_UNICODE);
    exit;
}

if ($website === '') {
    pl_json_error(400, 'URL du site invalide. Utilisez une adresse http(s).');
}
if ($email === '') {
    pl_json_error(400, 'L’email est obligatoire.');
}
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    pl_json_error(400, 'L’email n’est pas valide.');
}
if (preg_match("/[\r\n]/", $email)) {
    pl_json_error(400, 'Données invalides.');
}

if (!pl_has_audit_auth()) {
    pl_json_error(500, 'Service d’audit temporairement indisponible.');
}

$ip = pl_client_ip();
$host = pl_website_host($website);
pl_apply_free_audit_rate_limits($ip, $email, $host);

$plResult = pl_request_free_audit($website, $email, 'danielcraft_audit_gratuit');

if (!$plResult['ok']) {
    $status = (int) $plResult['status'];
    if ($status === 429) {
        pl_json_error(429, $plResult['error'] !== '' ? $plResult['error'] : 'Trop de demandes. Réessayez plus tard.');
    }
    if ($status >= 400 && $status < 500) {
        pl_json_error($status, $plResult['error'] !== '' ? $plResult['error'] : 'Demande refusée.');
    }
    error_log('[request-free-audit] ProspectLab ' . $status . ': ' . $plResult['error']);
    pl_json_error(502, 'Impossible de lancer l’audit pour le moment. Réessayez dans quelques minutes.');
}

$dryRunRaw = getenv('CONTACT_MAIL_DRY_RUN');
$dryRun = $dryRunRaw !== false && in_array(strtolower(trim((string) $dryRunRaw)), ['1', 'true', 'yes', 'on'], true);

$adminTo = getenv('CONTACT_TO') ?: getenv('MAIL_DEFAULT_RECIPIENT') ?: 'contact@danielcraft.fr';
$safeSite = audit_esc($website);
$safeEmail = audit_esc($email);
$siteBase = rtrim(getenv('SITE_BASE') ?: 'https://danielcraft.fr', '/');

if (!$dryRun) {
    $adminSubject = 'Audit gratuit demandé — ' . preg_replace('#^https?://#i', '', $website);
    $taskNote = $plResult['task_id'] !== '' ? "\nTask ID : {$plResult['task_id']}" : '';
    $skipNote = $plResult['skipped_analysis'] ? "\n(Analyse déjà en base — PDF + email direct)" : '';
    $adminText = "Demande audit gratuit\n\nSite : {$website}\nEmail : {$email}\nAPI : {$plResult['source']}{$taskNote}{$skipNote}\n";
    $adminHtml = '<p><strong>Site :</strong> <a href="' . $safeSite . '">' . $safeSite . '</a></p>'
        . '<p><strong>Email :</strong> ' . $safeEmail . '</p>'
        . '<p><strong>Rapport PDF :</strong> demande envoyée à ProspectLab</p>';
    if ($plResult['task_id'] !== '') {
        $adminHtml .= '<p><strong>Task ID :</strong> ' . audit_esc($plResult['task_id']) . '</p>';
    }
    if ($plResult['skipped_analysis']) {
        $adminHtml .= '<p><em>Analyse déjà en base — envoi PDF direct.</em></p>';
    }
    audit_send_simple_mail($adminTo, $adminSubject, $adminText, $adminHtml, $email);

    $userSubject = 'Votre audit gratuit est en cours — DanielCraft';
    $userText = "Bonjour,\n\nNous avons bien reçu votre demande d'audit pour :\n{$website}\n\n"
        . "Rapport en route — vous recevrez 3 priorités concrètes pour votre site sous 48 h ouvrées.\n\n"
        . $siteBase . '/analyse?website=' . rawurlencode($website) . "&full=1\n\n"
        . "DanielCraft\n";
    $userHtml = '<p>Bonjour,</p><p>Nous avons bien reçu votre demande d’audit pour :</p>'
        . '<p><a href="' . $safeSite . '"><strong>' . $safeSite . '</strong></a></p>'
        . '<p><strong>Rapport en route</strong> — vous recevrez <strong>3 priorités</strong> pour votre site à <strong>'
        . $safeEmail . '</strong> sous <strong>48 h ouvrées</strong>.</p>'
        . '<p><a href="' . audit_esc($siteBase) . '/analyse?website=' . rawurlencode($website) . '&amp;full=1">Voir un aperçu en ligne</a></p>'
        . '<p>À bientôt,<br>DanielCraft</p>';
    audit_send_simple_mail($email, $userSubject, $userText, $userHtml);
}

$response = [
    'success' => true,
    'queued' => (bool) $plResult['queued'],
    'message' => $plResult['skipped_analysis']
        ? 'Merci ! Votre rapport PDF est en cours d’envoi par email.'
        : 'Rapport en route — 3 priorités pour votre site sous 48 h ouvrées.',
];
if ($plResult['task_id'] !== '') {
    $response['task_id'] = $plResult['task_id'];
}

if ($dryRun) {
    $response['dry_run'] = true;
}

echo json_encode($response, JSON_UNESCAPED_UNICODE);
