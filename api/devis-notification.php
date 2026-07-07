<?php
/**
 * Notification e-mail de secours quand Prestafacture est indisponible.
 */
declare(strict_types=1);

require_once __DIR__ . '/env.php';

function devis_send_simple_mail(string $to, string $subject, string $textBody, string $htmlBody, string $replyTo = ''): bool
{
    api_bootstrap_env();

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
                $mail->Timeout = 20;
                $mail->SMTPAutoTLS = true;
                $useTls = strtolower(trim((string) (getenv('MAIL_USE_TLS') ?: '')));
                $smtpUser = getenv('MAIL_USERNAME') ?: '';
                $smtpPass = getenv('MAIL_PASSWORD') ?: '';
                $mail->SMTPAuth = ($smtpUser !== '' && $smtpPass !== '');
                if ($mail->SMTPAuth) {
                    $mail->Username = $smtpUser;
                    $mail->Password = $smtpPass;
                }
                if (in_array($useTls, ['1', 'true', 'yes', 'on'], true)) {
                    $mail->SMTPSecure = 'tls';
                    $allowSelfSigned = strtolower(trim((string) (getenv('MAIL_TLS_ALLOW_SELF_SIGNED') ?: '')));
                    if (in_array($allowSelfSigned, ['1', 'true', 'yes', 'on'], true)) {
                        $mail->SMTPOptions = [
                            'ssl' => [
                                'verify_peer' => false,
                                'verify_peer_name' => false,
                                'allow_self_signed' => true,
                            ],
                        ];
                    }
                }
            }

            return $mail->send();
        } catch (Throwable $e) {
            error_log('[devis-notification] PHPMailer: ' . $e->getMessage());
        }
    }

    return @mail($to, $subjectEncoded, $mailBody, $mimeHeaders);
}

/**
 * @param list<array{description: string, quantity: float, unitPrice: float}> $lines
 * @return array{ok: bool, admin_sent: bool, client_sent: bool}
 */
function devis_notify_fallback(
    string $customerEmail,
    string $customerName,
    string $prestationTitle,
    int $totalHt,
    array $lines,
    string $internalNote = ''
): array {
    $adminTo = trim((string) (getenv('MAIL_DEFAULT_RECIPIENT') ?: 'contact@danielcraft.fr'));
    if (!filter_var($adminTo, FILTER_VALIDATE_EMAIL)) {
        $adminTo = 'contact@danielcraft.fr';
    }

    $lineText = [];
    foreach ($lines as $line) {
        if (!is_array($line)) {
            continue;
        }
        $desc = (string) ($line['description'] ?? '');
        $unit = (float) ($line['unitPrice'] ?? 0);
        if ($desc === '') {
            continue;
        }
        $lineText[] = '- ' . $desc . ' : ' . number_format($unit, 2, ',', ' ') . ' € HT';
    }

    $ttc = round($totalHt * 1.2);
    $adminSubject = '[DanielCraft] Demande de devis — ' . $prestationTitle;
    $adminText = implode("\n", [
        'Nouvelle demande de devis (Prestafacture indisponible — à traiter manuellement).',
        '',
        'Client : ' . $customerName,
        'E-mail : ' . $customerEmail,
        'Prestation : ' . $prestationTitle,
        'Total HT : ' . $totalHt . ' € HT (' . $ttc . ' € TTC)',
        '',
        'Lignes :',
        ...$lineText,
        '',
        $internalNote !== '' ? 'Notes :' . "\n" . $internalNote : '',
    ]);

    $adminHtml = '<p><strong>Demande de devis</strong> (Prestafacture indisponible — à traiter manuellement).</p>'
        . '<ul><li><strong>Client :</strong> ' . htmlspecialchars($customerName, ENT_QUOTES, 'UTF-8') . '</li>'
        . '<li><strong>E-mail :</strong> ' . htmlspecialchars($customerEmail, ENT_QUOTES, 'UTF-8') . '</li>'
        . '<li><strong>Prestation :</strong> ' . htmlspecialchars($prestationTitle, ENT_QUOTES, 'UTF-8') . '</li>'
        . '<li><strong>Total HT :</strong> ' . $totalHt . ' € HT (' . $ttc . ' € TTC)</li></ul>'
        . '<pre style="font-family:sans-serif;white-space:pre-wrap">' . htmlspecialchars(implode("\n", $lineText), ENT_QUOTES, 'UTF-8') . '</pre>';

    if ($internalNote !== '') {
        $adminHtml .= '<p><strong>Notes</strong></p><pre style="white-space:pre-wrap">'
            . htmlspecialchars($internalNote, ENT_QUOTES, 'UTF-8') . '</pre>';
    }

    $clientSubject = 'Votre demande de devis — DanielCraft';
    $clientText = implode("\n", [
        'Bonjour ' . $customerName . ',',
        '',
        'Merci pour votre demande concernant : ' . $prestationTitle . '.',
        'Montant HT : ' . $totalHt . ' € HT (' . $ttc . ' € TTC).',
        '',
        'Voici ce qui se passe dans les 24 h ouvrées :',
        '1. Je relis votre demande et les options choisies',
        '2. Vous recevez votre devis PDF à cette adresse',
        '3. Une question ? Répondez à cet e-mail',
        '',
        '— Loïc, DanielCraft',
    ]);

    $clientHtml = '<p>Bonjour ' . htmlspecialchars($customerName, ENT_QUOTES, 'UTF-8') . ',</p>'
        . '<p>Merci pour votre demande concernant <strong>'
        . htmlspecialchars($prestationTitle, ENT_QUOTES, 'UTF-8')
        . '</strong>.</p><p>Montant HT : <strong>'
        . $totalHt . ' € HT</strong> (' . $ttc . ' € TTC).</p>'
        . '<p><strong>Voici ce qui se passe dans les 24 h ouvrées :</strong></p>'
        . '<ol><li>Je relis votre demande et les options choisies</li>'
        . '<li>Vous recevez votre devis PDF à cette adresse</li>'
        . '<li>Une question ? Répondez à cet e-mail</li></ol>'
        . '<p>— Loïc, DanielCraft</p>';

    $adminSent = devis_send_simple_mail($adminTo, $adminSubject, $adminText, $adminHtml, $customerEmail);
    $clientSent = devis_send_simple_mail($customerEmail, $clientSubject, $clientText, $clientHtml, $adminTo);

    return [
        'ok' => $adminSent || $clientSent,
        'admin_sent' => $adminSent,
        'client_sent' => $clientSent,
    ];
}
