<?php
/**
 * Endpoint d'envoi du formulaire de contact (AJAX).
 * Recoit POST, valide les champs, envoie un email et repond en JSON.
 */

require_once __DIR__ . '/contact-common.php';

header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');

// Autoriser les requetes depuis le meme domaine (CORS)
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
    echo json_encode(['success' => false, 'error' => 'Méthode non autorisée']);
    exit;
}

$validated = contact_validate_payload($_POST);
$errors = $validated['errors'];
if ($errors !== []) {
    api_log('send-contact', 'validation 400', [
        'errors' => $errors,
        'project_type' => $validated['data']['project_type'] ?? '',
        'service' => $validated['data']['service'] ?? '',
    ]);
    http_response_code(400);
    echo json_encode([
        'success' => false,
        'error' => implode(' ', $errors),
        'errors' => $errors,
    ]);
    exit;
}

$data = $validated['data'];
$name = $data['name'];
$email = $data['email'];
$phone = $data['phone'];
$service = $data['service'];
$project_type = $data['project_type'];
$budget = $data['budget'];
$message = $data['message'];
$preferred_date = $data['preferred_date'];
$preferred_time = $data['preferred_time'];
$vitrine_slug = $data['vitrine_slug'];
$vitrine_title = $data['vitrine_title'];
$site_url = $data['site_url'];
$billing_address = $data['billing_address'];

api_bootstrap_env();

// --- Configuration SMTP DEV via variables d'environnement (optionnel) ---
// Supporte deux formats :
// 1) MAIL_SMTP_HOST / MAIL_SMTP_PORT (compat avec nos réglages précédents)
// 2) MAIL_SERVER / MAIL_PORT / MAIL_USE_TLS / MAIL_USERNAME / MAIL_PASSWORD (format user)
$envSmtpHost = getenv('MAIL_SMTP_HOST') ?: getenv('MAIL_SERVER') ?: '';
$envSmtpPort = getenv('MAIL_SMTP_PORT') ?: getenv('MAIL_PORT') ?: '';
$envUseTls = getenv('MAIL_USE_TLS') ?: '';
$envSmtpUser = getenv('MAIL_USERNAME') ?: '';
$envSmtpPass = getenv('MAIL_PASSWORD') ?: '';
$envSendmailPath = getenv('MAIL_SENDMAIL_PATH') ?: '';

if ($envSmtpHost !== '') {
    @ini_set('SMTP', $envSmtpHost);
}
if ($envSmtpPort !== '' && ctype_digit((string)$envSmtpPort)) {
    @ini_set('smtp_port', (int)$envSmtpPort);
}

// Note : PHP natif supporte mal certains réglages STARTTLS/auth.
// On essaie quand même (au cas où la lib mail du serveur le permette).
$useTlsNorm = strtolower(trim((string)$envUseTls));
if (in_array($useTlsNorm, ['1', 'true', 'yes', 'on'], true)) {
    @ini_set('smtp_crypto', 'tls');
}

if ($envSmtpUser !== '' && $envSmtpPass !== '') {
    @ini_set('smtp_auth', '1');
    @ini_set('smtp_user', $envSmtpUser);
    @ini_set('smtp_pass', $envSmtpPass);
    // Certaines builds PHP utilisent ces clés alternatives.
    @ini_set('auth_username', $envSmtpUser);
    @ini_set('auth_password', $envSmtpPass);
}

if ($envSendmailPath !== '') {
    @ini_set('sendmail_path', $envSendmailPath);
}

// Limite de longueur pour eviter abus
if (strlen($name) > 200 || strlen($message) > 5000 || strlen($phone) > 30) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'Données trop longues.']);
    exit;
}

$contactTo = getenv('CONTACT_TO') ?: getenv('MAIL_DEFAULT_RECIPIENT') ?: 'contact@danielcraft.fr';

$fromName = getenv('CONTACT_FROM_NAME') ?: '';
$fromAddress = getenv('CONTACT_FROM_ADDRESS') ?: '';
$defaultSender = getenv('MAIL_DEFAULT_SENDER') ?: '';

// Parser MAIL_DEFAULT_SENDER au format : "Nom <email@domaine>"
if (($fromName === '' || $fromAddress === '') && $defaultSender !== '') {
    if (preg_match('/^(.*)<([^>]+)>$/', $defaultSender, $m)) {
        $fromName = trim($m[1], " \t\n\r\0\x0B\"'");
        $fromAddress = trim($m[2]);
    } else {
        // Si pas de "<...>", tenter au moins de prendre une adresse brute.
        $candidate = trim($defaultSender);
        if (filter_var($candidate, FILTER_VALIDATE_EMAIL)) {
            $fromAddress = $candidate;
            if ($fromName === '') $fromName = 'DanielCraft';
        }
    }
}

if ($fromName === '') $fromName = 'DanielCraft';
if ($fromAddress === '') $fromAddress = $contactTo ?: 'contact@danielcraft.fr';

$to = $contactTo;
$serviceLabel = contact_service_label($service);
$projectTypeLabel = contact_project_type_label($project_type);
if ($service === 'vitrine_catalog_order') {
    $tail = $vitrine_title !== '' ? $vitrine_title : $vitrine_slug;
    $subject = 'Pré-commande catalogue — ' . (function_exists('mb_substr') ? mb_substr($tail, 0, 70, 'UTF-8') : substr($tail, 0, 70));
} elseif ($service === 'vitrine_catalog_devis') {
    $tail = $vitrine_title !== '' ? $vitrine_title : $vitrine_slug;
    $subject = 'Devis catalogue — ' . (function_exists('mb_substr') ? mb_substr($tail, 0, 72, 'UTF-8') : substr($tail, 0, 72));
} else {
    $subjectShort = function_exists('mb_substr')
        ? mb_substr($serviceLabel, 0, 55, 'UTF-8')
        : substr($serviceLabel, 0, 55);
    $subject = 'Nouveau contact — ' . $subjectShort;
}

$body = "Nom : " . $name . "\n";
$body .= "Email : " . $email . "\n";
$body .= "Téléphone : " . ($phone ?: 'Non renseigné') . "\n";
$body .= "Besoin : " . $projectTypeLabel . " (" . $project_type . ")\n";
$body .= "Prestation : " . $serviceLabel . " (slug: " . $service . ")\n";
$body .= "Réf. forfait / budget (si indiqué) : " . ($budget."€" ?: 'Non renseigné') . "\n";
$body .= "Date proposée (échange) : " . ($preferred_date ?: 'Non renseignée') . "\n";
$body .= "Créneau horaire : " . ($preferred_time ?: 'Non renseigné') . "\n\n";
if ($vitrine_slug !== '') {
    $body .= "--- Fiche catalogue ---\n";
    $body .= 'Slug : ' . $vitrine_slug . "\n";
    $body .= 'Titre : ' . $vitrine_title . "\n";
    if ($site_url !== '') {
        $body .= 'URL du site visée : ' . $site_url . "\n";
    }
    if ($billing_address !== '') {
        $body .= "Adresse de facturation :\n" . $billing_address . "\n\n";
    } else {
        $body .= "\n";
    }
} elseif (in_array($service, $audit_flow_services, true) && $site_url !== '') {
    $body .= "--- Site à auditer ---\n";
    $body .= 'URL : ' . $site_url . "\n\n";
}
$body .= "Message :\n" . $message . "\n";

// --- HTML mail (inline + compat email clients) ---
function esc(string $s): string
{
    return htmlspecialchars($s, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}

$safeName = esc($name);
$safeEmail = esc($email);
$safePhone = esc($phone ?: 'Non renseigné');
$safeProjectTypeLabel = esc($projectTypeLabel);
$safeProjectTypeSlug = esc($project_type);
$safeServiceLabel = esc($serviceLabel);
$safeServiceSlug = esc($service);
$safeBudget = esc($budget !== '' ? ($budget . ' €') : 'Non renseigné');
$safePreferredDate = esc($preferred_date ?: 'Non renseignée');
$safePreferredTime = esc($preferred_time ?: 'Non renseigné');
$safeMessage = nl2br(esc($message));
$serviceLabelUser = trim((string)preg_replace('/\s*\([^)]*€[^)]*\)\s*/u', ' ', $serviceLabel));
if ($serviceLabelUser === '') {
    $serviceLabelUser = $serviceLabel;
}
$safeServiceLabelUser = esc($serviceLabelUser);
$budgetMarketingLine = $budget !== ''
    ? 'Budget envisagé : ' . $budget . ' € (repère indicatif, ajustable selon vos priorités).'
    : 'Budget : à définir ensemble selon vos objectifs et vos priorités.';
$safeBudgetMarketingLine = esc($budgetMarketingLine);

$extraVitrineRows = '';
if ($vitrine_slug !== '') {
    $safeVSlug = esc($vitrine_slug);
    $safeVTitle = esc($vitrine_title);
    $extraVitrineRows .= '<tr><td style="padding:10px 0;border-bottom:1px solid #eef1f7;"><div style="font-size:12px;color:#6b7280;font-weight:700;">Référence (slug)</div><div style="font-size:14px;color:#0f172a;font-weight:800;">' . $safeVSlug . '</div></td></tr>';
    $extraVitrineRows .= '<tr><td style="padding:10px 0;border-bottom:1px solid #eef1f7;"><div style="font-size:12px;color:#6b7280;font-weight:700;">Modèle (titre)</div><div style="font-size:14px;color:#0f172a;font-weight:800;">' . $safeVTitle . '</div></td></tr>';
    if ($site_url !== '') {
        $safeSiteUrl = esc($site_url);
        $extraVitrineRows .= '<tr><td style="padding:10px 0;border-bottom:1px solid #eef1f7;"><div style="font-size:12px;color:#6b7280;font-weight:700;">URL du site visée</div><div style="font-size:14px;color:#0f172a;font-weight:800;"><a href="' . $safeSiteUrl . '" style="color:#2f56b3;">' . $safeSiteUrl . '</a></div></td></tr>';
    }
    if ($billing_address !== '') {
        $safeBill = nl2br(esc($billing_address));
        $extraVitrineRows .= '<tr><td style="padding:10px 0;border-bottom:1px solid #eef1f7;"><div style="font-size:12px;color:#6b7280;font-weight:700;">Adresse de facturation</div><div style="font-size:14px;color:#0f172a;line-height:1.45;">' . $safeBill . '</div></td></tr>';
    }
}

$htmlBody = '
<!doctype html>
<html lang="fr">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nouveau contact</title>
  </head>
  <body style="margin:0;padding:0;background:#f4f7ff;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif;">
    <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="background:#f4f7ff;">
      <tr>
        <td align="center" style="padding:28px 14px;">
          <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="640" style="width:640px;max-width:640px;background:#ffffff;border-radius:16px;overflow:hidden;box-shadow:0 10px 30px rgba(25,40,88,0.08);">
            <tr>
              <td style="padding:22px 24px;background:linear-gradient(135deg,#5b7fd1 0%, #2f56b3 100%);">
                <div style="font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:rgba(255,255,255,0.85);font-weight:700;">
                  DanielCraft
                </div>
                <div style="font-size:20px;line-height:1.3;color:#ffffff;font-weight:800;margin-top:6px;">
                  Nouveau formulaire de contact
                </div>
                <div style="font-size:13px;color:rgba(255,255,255,0.85);margin-top:4px;">
                  Un client a complété le parcours.
                </div>
              </td>
            </tr>

            <tr>
              <td style="padding:18px 24px 6px 24px;">
                <div style="font-size:13px;color:#5b6472;font-weight:700;margin-bottom:10px;">
                  Informations
                </div>
                <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="border-collapse:collapse;">
                  <tr>
                    <td style="padding:10px 0;border-bottom:1px solid #eef1f7;">
                      <div style="font-size:12px;color:#6b7280;font-weight:700;">Nom</div>
                      <div style="font-size:14px;color:#0f172a;font-weight:800;">'.$safeName.'</div>
                    </td>
                  </tr>
                  <tr>
                    <td style="padding:10px 0;border-bottom:1px solid #eef1f7;">
                      <div style="font-size:12px;color:#6b7280;font-weight:700;">Email</div>
                      <div style="font-size:14px;color:#0f172a;font-weight:800;">'.$safeEmail.'</div>
                    </td>
                  </tr>
                  <tr>
                    <td style="padding:10px 0;border-bottom:1px solid #eef1f7;">
                      <div style="font-size:12px;color:#6b7280;font-weight:700;">Téléphone</div>
                      <div style="font-size:14px;color:#0f172a;font-weight:800;">'.$safePhone.'</div>
                    </td>
                  </tr>
                  <tr>
                    <td style="padding:10px 0;border-bottom:1px solid #eef1f7;">
                      <div style="font-size:12px;color:#6b7280;font-weight:700;">Besoin</div>
                      <div style="font-size:14px;color:#0f172a;font-weight:800;">'.$safeProjectTypeLabel.' <span style="font-weight:700;color:#6b7280;">('.$safeProjectTypeSlug.')</span></div>
                    </td>
                  </tr>
                  <tr>
                    <td style="padding:10px 0;border-bottom:1px solid #eef1f7;">
                      <div style="font-size:12px;color:#6b7280;font-weight:700;">Prestation</div>
                      <div style="font-size:14px;color:#0f172a;font-weight:800;">'.$safeServiceLabel.' <span style="font-weight:700;color:#6b7280;">(slug: '.$safeServiceSlug.')</span></div>
                    </td>
                  </tr>
                  <tr>
                    <td style="padding:10px 0;border-bottom:1px solid #eef1f7;">
                      <div style="font-size:12px;color:#6b7280;font-weight:700;">Budget / forfait</div>
                      <div style="font-size:14px;color:#0f172a;font-weight:800;">'.$safeBudget.'</div>
                    </td>
                  </tr>
                  <tr>
                    <td style="padding:10px 0;">
                      <div style="font-size:12px;color:#6b7280;font-weight:700;">Date proposée</div>
                      <div style="font-size:14px;color:#0f172a;font-weight:800;">'.$safePreferredDate.'</div>
                    </td>
                  </tr>
                  <tr>
                    <td style="padding:10px 0 14px 0;">
                      <div style="font-size:12px;color:#6b7280;font-weight:700;">Créneau horaire</div>
                      <div style="font-size:14px;color:#0f172a;font-weight:800;">'.$safePreferredTime.'</div>
                    </td>
                  </tr>
                  '.$extraVitrineRows.'
                </table>
              </td>
            </tr>

            <tr>
              <td style="padding:6px 24px 22px 24px;">
                <div style="font-size:13px;color:#5b6472;font-weight:700;margin:2px 0 10px 0;">
                  Message
                </div>
                <div style="background:#f8fafc;border:1px solid #eef1f7;border-radius:12px;padding:14px 14px;color:#0f172a;line-height:1.5;font-size:13px;">
                  '.$safeMessage.'
                </div>
              </td>
            </tr>

            <tr>
              <td style="padding:14px 24px;background:#f8fafc;border-top:1px solid #eef1f7;">
                <div style="font-size:12px;color:#64748b;">
                  Réponse recommandée par email : <span style="font-weight:800;color:#2f56b3;">'.$safeEmail.'</span>
                </div>
              </td>
            </tr>

          </table>
          <div style="font-size:11px;color:#9aa3b2;margin-top:10px;">
            Ceci est un email généré automatiquement.
          </div>
        </td>
      </tr>
    </table>
  </body>
</html>
';

// Variante HTML pour l'expéditeur (confirmation)
$htmlBodyUser = '
<!doctype html>
<html lang="fr">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Confirmation de votre demande</title>
  </head>
  <body style="margin:0;padding:0;background:#f4f7ff;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif;">
    <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="background:#f4f7ff;">
      <tr>
        <td align="center" style="padding:28px 14px;">
          <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="640" style="width:640px;max-width:640px;background:#ffffff;border-radius:16px;overflow:hidden;box-shadow:0 10px 30px rgba(25,40,88,0.08);">
            <tr>
              <td style="padding:22px 24px;background:linear-gradient(135deg,#5b7fd1 0%, #2f56b3 100%);">
                <div style="font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:rgba(255,255,255,0.85);font-weight:700;">
                  DanielCraft
                </div>
                <div style="font-size:20px;line-height:1.3;color:#ffffff;font-weight:800;margin-top:6px;">
                  Merci pour votre demande
                </div>
                <div style="font-size:13px;color:rgba(255,255,255,0.85);margin-top:4px;">
                  Ce message confirme la bonne réception de votre formulaire.
                </div>
              </td>
            </tr>

            <tr>
              <td style="padding:18px 24px 6px 24px;">
                <div style="font-size:14px;color:#0f172a;margin:0 0 10px 0;">
                  Bonjour '. $safeName .',
                </div>
                <div style="font-size:13px;color:#5b6472;line-height:1.6;margin:0 0 16px 0;">
                  Merci pour votre confiance. Voici un récapitulatif rapide de votre demande&nbsp;:
                </div>
                <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="border-collapse:collapse;">
                  <tr>
                    <td style="padding:8px 0;border-bottom:1px solid #eef1f7;">
                      <div style="font-size:12px;color:#6b7280;font-weight:700;">Besoin</div>
                      <div style="font-size:14px;color:#0f172a;font-weight:800;">'.$safeProjectTypeLabel.'</div>
                    </td>
                  </tr>
                  <tr>
                    <td style="padding:8px 0;border-bottom:1px solid #eef1f7;">
                      <div style="font-size:12px;color:#6b7280;font-weight:700;">Prestation</div>
                      <div style="font-size:14px;color:#0f172a;font-weight:800;">'.$safeServiceLabelUser.'</div>
                    </td>
                  </tr>
                  <tr>
                    <td style="padding:8px 0;border-bottom:1px solid #eef1f7;">
                      <div style="font-size:12px;color:#6b7280;font-weight:700;">Budget</div>
                      <div style="font-size:14px;color:#0f172a;font-weight:700;">'.$safeBudgetMarketingLine.'</div>
                    </td>
                  </tr>
                  <tr>
                    <td style="padding:8px 0;border-bottom:1px solid #eef1f7;">
                      <div style="font-size:12px;color:#6b7280;font-weight:700;">Date proposée</div>
                      <div style="font-size:14px;color:#0f172a;font-weight:800;">'.$safePreferredDate.'</div>
                    </td>
                  </tr>
                  <tr>
                    <td style="padding:8px 0 12px 0;">
                      <div style="font-size:12px;color:#6b7280;font-weight:700;">Créneau horaire</div>
                      <div style="font-size:14px;color:#0f172a;font-weight:800;">'.$safePreferredTime.'</div>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>

            <tr>
              <td style="padding:6px 24px 22px 24px;">
                <div style="font-size:13px;color:#5b6472;line-height:1.6;">
                  Je reviens vers vous par email pour confirmer le créneau ou vous proposer une alternative.
                </div>
              </td>
            </tr>

            <tr>
              <td style="padding:14px 24px;background:#f8fafc;border-top:1px solid #eef1f7;">
                <div style="font-size:12px;color:#64748b;">
                  Si ce message ne vous était pas destiné, vous pouvez simplement l’ignorer.
                </div>
              </td>
            </tr>

          </table>
          <div style="font-size:11px;color:#9aa3b2;margin-top:10px;">
            Email envoyé automatiquement depuis danielcraft.fr.
          </div>
        </td>
      </tr>
    </table>
  </body>
</html>
';

$bodyUser = "Bonjour " . $name . ",\n\n";
$bodyUser .= "Merci pour votre demande, elle a bien été reçue.\n\n";
$bodyUser .= "Récapitulatif :\n";
$bodyUser .= "- Besoin : " . $projectTypeLabel . "\n";
$bodyUser .= "- Prestation : " . $serviceLabelUser . "\n";
$bodyUser .= "- " . $budgetMarketingLine . "\n";
$bodyUser .= "- Date proposée : " . ($preferred_date ?: 'Non renseignée') . "\n";
$bodyUser .= "- Créneau horaire : " . ($preferred_time ?: 'Non renseigné') . "\n\n";
$bodyUser .= "Je reviens vers vous rapidement pour confirmer le créneau ou vous proposer une meilleure option.\n";
$bodyUser .= "DanielCraft\n";

$boundary = 'bnd_' . bin2hex(random_bytes(8));

$headers = [
    // Le "From" doit idéalement appartenir au domaine pour éviter les rejets DMARC/SPF.
    'From: ' . esc($fromName) . ' <' . esc($fromAddress) . '>',
    'Reply-To: ' . $email,
    'X-Mailer: PHP/' . phpversion(),
    'MIME-Version: 1.0',
    'Content-Type: multipart/alternative; boundary="' . $boundary . '"',
];

$mailBody =
    '--' . $boundary . "\r\n" .
    'Content-Type: text/plain; charset=UTF-8' . "\r\n\r\n" .
    $body . "\r\n\r\n" .
    '--' . $boundary . "\r\n" .
    'Content-Type: text/html; charset=UTF-8' . "\r\n\r\n" .
    $htmlBody . "\r\n\r\n" .
    '--' . $boundary . '--';

function smtpReadLine($socket): string
{
    $line = '';
    while (!str_ends_with($line, "\n")) {
        $chunk = fread($socket, 1);
        if ($chunk === '' || $chunk === false) break;
        $line .= $chunk;
        if ($line === "\n") break;
    }
    return $line;
}

function smtpExpect($socket, array &$lines, ?int $code = null): bool
{
    // Lit potentiellement un bloc multi-lignes (code- puis code space).
    while (true) {
        $line = fgets($socket);
        if ($line === false) return false;
        $lines[] = rtrim($line, "\r\n");
        if (strlen($line) < 4) continue;
        $c = (int)substr($line, 0, 3);
        $sep = $line[3] ?? ' ';
        if ($code === null) {
            if ($sep === ' ') return true;
            continue;
        }
        if ($c !== $code) return false;
        if ($sep === ' ') return true;
    }
}

function smtpCmd($socket, string $cmd): bool
{
    $raw = $cmd . "\r\n";
    return fwrite($socket, $raw) !== false;
}

function smtpSend(
    string $host,
    int $port,
    bool $useTls,
    bool $allowSelfSignedTls,
    string $username,
    string $password,
    string $fromName,
    string $fromEmail,
    string $toEmail,
    string $subject,
    string $mimeHeaders,
    string $mimeBody
): bool {
    $timeoutSec = 20;
    $context = stream_context_create([
        'ssl' => [
            'verify_peer' => !$allowSelfSignedTls,
            'verify_peer_name' => !$allowSelfSignedTls,
            'allow_self_signed' => $allowSelfSignedTls
        ]
    ]);
    $socket = @stream_socket_client(
        'tcp://' . $host . ':' . $port,
        $errno,
        $errstr,
        $timeoutSec,
        STREAM_CLIENT_CONNECT,
        $context
    );
    if (!$socket) {
        error_log('[send-contact][smtp] connect failed errno=' . $errno . ' err=' . $errstr);
        return false;
    }
    stream_set_timeout($socket, $timeoutSec);

    $lines = [];
    if (!smtpExpect($socket, $lines, 220)) {
        error_log('[send-contact][smtp] greeting invalid. last=' . end($lines));
        fclose($socket);
        return false;
    }

    // EHLO
    $lines = [];
    smtpCmd($socket, 'EHLO danielcraft.local');
    // EHLO: 250 avec multi-lignes.
    if (!smtpExpect($socket, $lines, 250)) {
        // Certains serveurs acceptent HELO fallback
        $lines = [];
        smtpCmd($socket, 'HELO danielcraft.local');
        if (!smtpExpect($socket, $lines, 250)) {
            fclose($socket);
            return false;
        }
    }

    if ($useTls) {
        // STARTTLS
        $lines = [];
        smtpCmd($socket, 'STARTTLS');
        if (!smtpExpect($socket, $lines, 220)) {
            error_log('[send-contact][smtp] STARTTLS refused last=' . end($lines));
            fclose($socket);
            return false;
        }
        $cryptoOk = @stream_socket_enable_crypto($socket, true, STREAM_CRYPTO_METHOD_TLS_CLIENT);
        if (!$cryptoOk) {
            error_log('[send-contact][smtp] enable_crypto failed');
            fclose($socket);
            return false;
        }

        // EHLO après STARTTLS
        $lines = [];
        smtpCmd($socket, 'EHLO danielcraft.local');
        if (!smtpExpect($socket, $lines, 250)) {
            fclose($socket);
            return false;
        }
    }

    if ($username !== '' && $password !== '') {
        // AUTH LOGIN
        $lines = [];
        smtpCmd($socket, 'AUTH LOGIN');
        if (!smtpExpect($socket, $lines, 334)) {
            $last = (string)end($lines);
            // Certains serveurs exigent STARTTLS avant AUTH (ex: "530 Must issue a STARTTLS command first")
            if (stripos($last, 'STARTTLS') !== false) {
                $lines = [];
                smtpCmd($socket, 'STARTTLS');
                if (!smtpExpect($socket, $lines, 220)) {
                    error_log('[send-contact][smtp] STARTTLS required but refused last=' . end($lines));
                    fclose($socket);
                    return false;
                }
                $cryptoOk = @stream_socket_enable_crypto($socket, true, STREAM_CRYPTO_METHOD_TLS_CLIENT);
                if (!$cryptoOk) {
                    error_log('[send-contact][smtp] enable_crypto failed after AUTH-STARTTLS');
                    fclose($socket);
                    return false;
                }
                // Re-EHLO puis AUTH LOGIN
                $lines = [];
                smtpCmd($socket, 'EHLO danielcraft.local');
                if (!smtpExpect($socket, $lines, 250)) {
                    fclose($socket);
                    return false;
                }
                $lines = [];
                smtpCmd($socket, 'AUTH LOGIN');
                if (!smtpExpect($socket, $lines, 334)) {
                    error_log('[send-contact][smtp] AUTH LOGIN step1 failed after STARTTLS last=' . end($lines));
                    fclose($socket);
                    return false;
                }
            } else {
                error_log('[send-contact][smtp] AUTH LOGIN step1 failed last=' . $last);
                fclose($socket);
                return false;
            }
        }
        smtpCmd($socket, base64_encode($username));
        $lines = [];
        if (!smtpExpect($socket, $lines, 334)) {
            error_log('[send-contact][smtp] AUTH LOGIN step2 failed last=' . end($lines));
            fclose($socket);
            return false;
        }
        smtpCmd($socket, base64_encode($password));
        $lines = [];
        if (!smtpExpect($socket, $lines, 235)) {
            error_log('[send-contact][smtp] AUTH LOGIN step3 failed last=' . end($lines));
            fclose($socket);
            return false;
        }
    }

    // MAIL FROM / RCPT TO / DATA
    $lines = [];
    smtpCmd($socket, 'MAIL FROM:<' . $fromEmail . '>');
    if (!smtpExpect($socket, $lines, 250)) {
        error_log('[send-contact][smtp] MAIL FROM failed last=' . end($lines));
        fclose($socket);
        return false;
    }

    $lines = [];
    smtpCmd($socket, 'RCPT TO:<' . $toEmail . '>');
    if (!smtpExpect($socket, $lines, 250) && !smtpExpect($socket, $lines, 251)) {
        error_log('[send-contact][smtp] RCPT TO failed last=' . end($lines));
        fclose($socket);
        return false;
    }

    $lines = [];
    smtpCmd($socket, 'DATA');
    if (!smtpExpect($socket, $lines, 354)) {
        error_log('[send-contact][smtp] DATA refused last=' . end($lines));
        fclose($socket);
        return false;
    }

    $full = $mimeHeaders . "\r\n\r\n" . $mimeBody . "\r\n";
    // SMTP: on termine par ligne composée uniquement d'un "."
    // On échappe les lignes commençant par "." (dot-stuffing).
    $full = preg_replace('/^\./m', '..', $full);
    if (@fwrite($socket, $full . "\r\n.\r\n") === false) {
        fclose($socket);
        return false;
    }
    $lines = [];
    if (!smtpExpect($socket, $lines, 250)) {
        error_log('[send-contact][smtp] DATA end failed last=' . end($lines));
        fclose($socket);
        return false;
    }

    smtpCmd($socket, 'QUIT');
    fclose($socket);
    return true;
}

$smtpHost = getenv('MAIL_SERVER') ?: '';
$smtpPort = getenv('MAIL_PORT') ?: '';
$smtpUseTls = getenv('MAIL_USE_TLS') ?: '';
$smtpAllowSelfSigned = getenv('MAIL_TLS_ALLOW_SELF_SIGNED') ?: '';
$smtpUser = getenv('MAIL_USERNAME') ?: '';
$smtpPass = getenv('MAIL_PASSWORD') ?: '';

$subjectEncoded = '=?UTF-8?B?' . base64_encode($subject) . '?=';
$mimeHeaders = implode("\r\n", $headers) . "\r\n" . 'To: ' . esc($to) . "\r\n" . 'Subject: ' . $subjectEncoded;

// Dev / CI : accepter la demande sans envoyer d’email (SMTP ou mail() souvent absents en local).
$dryRunRaw = getenv('CONTACT_MAIL_DRY_RUN');
$dryRun = $dryRunRaw !== false && in_array(strtolower(trim((string) $dryRunRaw)), ['1', 'true', 'yes', 'on'], true);
if ($dryRun) {
    error_log('[send-contact] CONTACT_MAIL_DRY_RUN=1 : email non envoyé (service=' . $service . ').');
    echo json_encode(['success' => true, 'dry_run' => true]);
    exit;
}

$sent = false;
// Envoi SMTP via PHPMailer (vendor sans composer)
$phpMailerBase = __DIR__ . '/vendor/phpmailer';
if (
    !$sent &&
    file_exists($phpMailerBase . '/class.phpmailer.php') &&
    file_exists($phpMailerBase . '/class.smtp.php')
) {
    try {
        require_once $phpMailerBase . '/class.phpmailer.php';
        require_once $phpMailerBase . '/class.smtp.php';

        $useTlsBool = in_array(strtolower(trim((string)$smtpUseTls)), ['1', 'true', 'yes', 'on'], true);
        $smtpPortInt = (int)$smtpPort;

        $mail = new PHPMailer(true);
        $mail->CharSet = 'UTF-8';
        $mail->isSMTP();
        $mail->Host = (string)$smtpHost;
        $mail->Port = $smtpPortInt;
        $mail->Timeout = 20;
        $mail->SMTPAutoTLS = true;
        $mail->SMTPAuth = ($smtpUser !== '' && $smtpPass !== '');
        if ($mail->SMTPAuth) {
            $mail->Username = (string)$smtpUser;
            $mail->Password = (string)$smtpPass;
        }
        if ($useTlsBool) {
            $mail->SMTPSecure = 'tls';
            $allowSelfSigned = in_array(strtolower(trim((string)$smtpAllowSelfSigned)), ['1', 'true', 'yes', 'on'], true);
            if ($allowSelfSigned) {
                $mail->SMTPOptions = [
                    'ssl' => [
                        'verify_peer' => false,
                        'verify_peer_name' => false,
                        'allow_self_signed' => true
                    ]
                ];
            }
        }

        // 1) Mail vers toi (admin)
        $mail->setFrom($fromAddress, $fromName);
        $mail->addReplyTo($email, $email);
        $mail->addAddress($to);
        $mail->Subject = $subject;
        $mail->msgHTML($htmlBody);
        $mail->AltBody = $body;
        $sent = $mail->send();

        // 2) Mail de confirmation vers le demandeur
        if ($sent && filter_var($email, FILTER_VALIDATE_EMAIL)) {
            $mail->clearAllRecipients();
            $mail->clearReplyTos();
            $mail->clearAttachments();
            $mail->setFrom($fromAddress, $fromName);
            $mail->addAddress($email);
            $mail->Subject = 'Confirmation de votre demande - DanielCraft';
            $mail->msgHTML($htmlBodyUser);
            $mail->AltBody = $bodyUser;
            $sent = $mail->send();
        }
    } catch (Throwable $e) {
        error_log('[send-contact] PHPMailer send failed: ' . $e->getMessage());
        $sent = false;
    }
}

// Fallback : envoi SMTP maison
if (
    !$sent &&
    $smtpHost !== '' &&
    $smtpPort !== '' &&
    ctype_digit((string)$smtpPort)
) {
    $sent = smtpSend(
        $smtpHost,
        (int)$smtpPort,
        in_array(strtolower(trim((string)$smtpUseTls)), ['1', 'true', 'yes', 'on'], true),
        in_array(strtolower(trim((string)$smtpAllowSelfSigned)), ['1', 'true', 'yes', 'on'], true),
        $smtpUser,
        $smtpPass,
        $fromName,
        $fromAddress,
        $to,
        $subject,
        $mimeHeaders,
        $mailBody
    );
}

// Fallback (si SMTP pas configuré) : PHP mail()
if (!$sent) {
    $sent = @mail($to, $subject, $mailBody, $mimeHeaders);
}

if (!$sent) {
    // Si l'envoi échoue, on renvoie une erreur pour que l'UI puisse le montrer.
    error_log(
        '[send-contact] mail() failed. sendmail_path=' . (string)ini_get('sendmail_path') .
        ' SMTP=' . (string)ini_get('SMTP') .
        ' smtp_port=' . (string)ini_get('smtp_port') .
        ' smtp_crypto=' . (string)ini_get('smtp_crypto') .
        ' smtp_auth=' . (string)ini_get('smtp_auth') .
        ' smtp_user=' . (string)ini_get('smtp_user') .
        ' to=' . $to .
        ' email=' . $email .
        ' service=' . $service .
        ' project_type=' . $project_type .
        ' err_context=php_mail'
    );
    error_log(
        '[send-contact] mail() failed. to=' . $to .
        ' email=' . $email .
        ' service=' . $service .
        ' project_type=' . $project_type .
        ' err_context=php_mail SMTP=' . (string)ini_get('SMTP') .
        ' smtp_port=' . (string)ini_get('smtp_port') .
        ' smtp_crypto=' . (string)ini_get('smtp_crypto') .
        ' smtp_auth=' . (string)ini_get('smtp_auth') .
        ' smtp_user=' . (string)ini_get('smtp_user')
    );
    http_response_code(500);
    echo json_encode(['success' => false, 'error' => "Envoi email impossible (mail() a échoué)."]);
    exit;
}

echo json_encode(['success' => true]);
