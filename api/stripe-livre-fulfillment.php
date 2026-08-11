<?php
/**
 * Apres paiement Stripe (livre PDF) : facture Prestafacture + lien unique de telechargement par e-mail.
 */

declare(strict_types=1);

require_once __DIR__ . '/stripe-common.php';
require_once __DIR__ . '/prestafacture-common.php';
require_once __DIR__ . '/devis-notification.php';
require_once __DIR__ . '/livre-download-common.php';

/**
 * @return array{invoice: bool, delivery: bool}
 */
function stripe_livre_fulfillment_state(string $sessionId): array
{
    $file = stripe_livre_fulfillment_state_file($sessionId);
    if (!is_file($file)) {
        return ['invoice' => false, 'delivery' => false];
    }
    $raw = @file_get_contents($file);
    $data = is_string($raw) ? json_decode($raw, true) : null;
    if (!is_array($data)) {
        return ['invoice' => false, 'delivery' => false];
    }

    return [
        'invoice' => !empty($data['invoice']),
        'delivery' => !empty($data['delivery']),
    ];
}

function stripe_livre_fulfillment_state_file(string $sessionId): string
{
    $dir = rtrim(sys_get_temp_dir(), DIRECTORY_SEPARATOR) . DIRECTORY_SEPARATOR . 'dc_livre_fulfill';
    if (!is_dir($dir)) {
        @mkdir($dir, 0700, true);
    }

    return $dir . DIRECTORY_SEPARATOR . 'sess_' . sha1($sessionId) . '.json';
}

/**
 * @param array{invoice?: bool, delivery?: bool} $patch
 */
function stripe_livre_fulfillment_mark(string $sessionId, array $patch): void
{
    $state = stripe_livre_fulfillment_state($sessionId);
    foreach (['invoice', 'delivery'] as $key) {
        if (array_key_exists($key, $patch) && $patch[$key]) {
            $state[$key] = true;
        }
    }
    @file_put_contents(
        stripe_livre_fulfillment_state_file($sessionId),
        json_encode($state, JSON_UNESCAPED_UNICODE),
        LOCK_EX
    );
}

/**
 * @param array<string, mixed> $session
 */
function stripe_session_is_paid_livre(array $session): bool
{
    $status = isset($session['payment_status']) ? (string) $session['payment_status'] : '';
    if ($status !== 'paid') {
        return false;
    }
    $meta = is_array($session['metadata'] ?? null) ? $session['metadata'] : [];
    $productType = isset($meta['product_type']) ? (string) $meta['product_type'] : '';
    if ($productType === 'livre_pdf') {
        return true;
    }

    return isset($meta['livre_slug']) && (string) $meta['livre_slug'] !== '';
}

/**
 * @param array<string, mixed> $session
 * @return array{email: string, name: string, slug: string, title: string}
 */
function stripe_livre_session_context(array $session): array
{
    $meta = is_array($session['metadata'] ?? null) ? $session['metadata'] : [];
    $email = '';
    if (!empty($session['customer_email']) && is_string($session['customer_email'])) {
        $email = trim($session['customer_email']);
    }
    if ($email === '' && is_array($session['customer_details'] ?? null)) {
        $details = $session['customer_details'];
        if (!empty($details['email']) && is_string($details['email'])) {
            $email = trim($details['email']);
        }
    }

    $slug = isset($meta['livre_slug']) ? trim((string) $meta['livre_slug']) : '';
    $title = isset($meta['livre_title']) ? trim((string) $meta['livre_title']) : $slug;
    $name = $email !== '' && str_contains($email, '@') ? (strstr($email, '@', true) ?: '') : '';

    return [
        'email' => $email,
        'name' => $name,
        'slug' => $slug,
        'title' => $title,
    ];
}

/**
 * @return array{ok: bool, error: string, invoice_id: string, email_sent: bool}
 */
function stripe_fulfill_livre_invoice(string $sessionId, array $ctx, array $item): array
{
    $empty = ['ok' => false, 'error' => '', 'invoice_id' => '', 'email_sent' => false];
    $state = stripe_livre_fulfillment_state($sessionId);
    if ($state['invoice']) {
        return ['ok' => true, 'error' => '', 'invoice_id' => '', 'email_sent' => true];
    }

    if (!prestafacture_configured()) {
        $empty['error'] = 'Prestafacture non configure.';
        return $empty;
    }

    $title = trim((string) ($item['title'] ?? $ctx['title']));
    $isPack = (($item['kind'] ?? '') === 'pack') || str_starts_with((string) ($item['slug'] ?? ''), 'pack-');
    $lineTitle = $isPack ? ($title . ' — pack PDF DanielCraft') : ($title . ' — livre PDF DanielCraft');
    $catalog = stripe_load_livres_catalog() ?? [];
    $defaultPrice = (float) ($catalog['default_price_eur'] ?? 0.5);
    $priceTtc = is_numeric($item['price_eur'] ?? null) ? (float) $item['price_eur'] : $defaultPrice;
    $taxRate = 20.0;

    $inv = prestafacture_issue_audit_invoice(
        $ctx['email'],
        $ctx['name'],
        $lineTitle,
        $priceTtc,
        $taxRate,
        ''
    );
    if (!$inv['ok'] || ($inv['invoice_id'] ?? '') === '') {
        error_log('[stripe-livre-fulfill] Prestafacture session ' . $sessionId . ': ' . ($inv['error'] ?? ''));
        $empty['error'] = $inv['error'] !== '' ? $inv['error'] : 'Creation facture impossible.';
        return $empty;
    }

    if (empty($inv['email_sent'])) {
        error_log('[stripe-livre-fulfill] Facture ' . $inv['invoice_id'] . ' creee, envoi email Prestafacture en echec : ' . ($inv['warning'] ?? ''));
    }

    stripe_livre_fulfillment_mark($sessionId, ['invoice' => true]);

    return [
        'ok' => true,
        'error' => '',
        'invoice_id' => (string) $inv['invoice_id'],
        'email_sent' => !empty($inv['email_sent']),
    ];
}

/**
 * @return array{ok: bool, error: string, download_url: string, code: string, email_sent: bool}
 */
function stripe_fulfill_livre_delivery(string $sessionId, array $ctx, array $item): array
{
    $empty = ['ok' => false, 'error' => '', 'download_url' => '', 'code' => '', 'email_sent' => false];
    $state = stripe_livre_fulfillment_state($sessionId);
    if ($state['delivery']) {
        $existing = livre_download_load_by_session($sessionId);
        $code = is_array($existing) ? (string) ($existing['code'] ?? '') : '';
        $token = is_array($existing) ? (string) ($existing['token'] ?? '') : '';
        return [
            'ok' => true,
            'error' => '',
            'download_url' => livre_download_page_url($code, $token),
            'code' => $code,
            'email_sent' => true,
        ];
    }

    $files = livre_resolve_pdf_files($item);
    if ($files === []) {
        $empty['error'] = 'PDF introuvable pour cette reference.';
        return $empty;
    }
    foreach ($files as $file) {
        if (livre_pdf_absolute_path((string) $file['filename']) === '') {
            $empty['error'] = 'Fichier PDF manquant sur le serveur : ' . $file['filename'];
            return $empty;
        }
    }

    $title = trim((string) ($item['title'] ?? $ctx['title']));
    $isPack = (($item['kind'] ?? '') === 'pack') || str_starts_with((string) ($item['slug'] ?? ''), 'pack-');
    $cover = trim((string) ($item['cover'] ?? ''));
    $tokenRes = livre_download_create_token(
        $sessionId,
        $ctx['email'],
        $ctx['slug'],
        $title,
        $files,
        $cover,
        $isPack ? 'pack' : 'livre'
    );
    if (!$tokenRes['ok']) {
        $empty['error'] = $tokenRes['error'];
        return $empty;
    }

    $code = (string) $tokenRes['code'];
    $downloadUrl = livre_download_page_url($code, (string) $tokenRes['token']);
    $mail = livre_delivery_build_email($ctx['email'], $title, $downloadUrl, $code, $isPack);
    $sent = devis_send_simple_mail($ctx['email'], $mail['subject'], $mail['text'], $mail['html']);

    if (!$sent) {
        error_log('[stripe-livre-fulfill] email livraison session ' . $sessionId . ' vers ' . $ctx['email']);
        $empty['error'] = 'Lien cree mais e-mail de livraison non envoye.';
        $empty['download_url'] = $downloadUrl;
        $empty['code'] = $code;
        return $empty;
    }

    stripe_livre_fulfillment_mark($sessionId, ['delivery' => true]);

    return [
        'ok' => true,
        'error' => '',
        'download_url' => $downloadUrl,
        'code' => $code,
        'email_sent' => true,
    ];
}

/**
 * @return array{subject: string, text: string, html: string}
 */
function livre_delivery_build_email(
    string $email,
    string $title,
    string $downloadUrl,
    string $code,
    bool $isPack
): array {
    $salut = 'Bonjour';
    if (str_contains($email, '@')) {
        $local = strstr($email, '@', true);
        if (is_string($local) && $local !== '') {
            $salut = ucfirst($local);
        }
    }

    $what = $isPack ? 'ton pack PDF' : 'ton livre PDF';
    $subject = 'DanielCraft — telechargement : ' . $title;

    $text = <<<TXT
{$salut},

Merci pour ton achat. Voici {$what} « {$title} ».

Page de telechargement (personnel, valable 30 jours) :
{$downloadUrl}

Ton code unique :
{$code}

Tu peux aussi le saisir plus tard sur danielcraft.fr/livres/telechargement/

Une facture t'a aussi ete envoyee par e-mail.

Question ? Reponds a cet e-mail ou ecris a contact@danielcraft.fr

— Loic Daniel, DanielCraft
TXT;

    $safeTitle = htmlspecialchars($title, ENT_QUOTES, 'UTF-8');
    $safeUrl = htmlspecialchars($downloadUrl, ENT_QUOTES, 'UTF-8');
    $safeCode = htmlspecialchars($code, ENT_QUOTES, 'UTF-8');
    $html = '<p>' . htmlspecialchars($salut, ENT_QUOTES, 'UTF-8') . ',</p>'
        . '<p>Merci pour ton achat. Voici ' . ($isPack ? 'ton <strong>pack PDF</strong>' : 'ton <strong>livre PDF</strong>')
        . ' « ' . $safeTitle . ' ».</p>'
        . '<p style="font-size:13px;color:#555;margin:0 0 6px;">Ton code unique</p>'
        . '<p style="font-family:ui-monospace,Consolas,monospace;font-size:22px;letter-spacing:0.08em;font-weight:700;color:#0f3550;margin:0 0 18px;">'
        . $safeCode . '</p>'
        . '<p><a href="' . $safeUrl . '" style="display:inline-block;padding:12px 20px;background:#1a5f85;color:#fff;text-decoration:none;border-radius:8px;">Ouvrir ma page de telechargement</a></p>'
        . '<p style="font-size:14px;color:#555;">Lien personnel, valable 30 jours :<br><a href="' . $safeUrl . '">' . $safeUrl . '</a></p>'
        . '<p>Une facture t\'a aussi ete envoyee par e-mail.</p>'
        . '<p>— Loic Daniel, DanielCraft<br>contact@danielcraft.fr</p>';

    return ['subject' => $subject, 'text' => $text, 'html' => $html];
}

/**
 * @param array{email?: string} $clientHints
 * @return array{ok: bool, error: string, invoice_ok: bool, delivery_ok: bool, download_url: string, code: string}
 */
function stripe_fulfill_livre_checkout_session(string $sessionId, array $clientHints = []): array
{
    $fail = [
        'ok' => false,
        'error' => '',
        'invoice_ok' => false,
        'delivery_ok' => false,
        'download_url' => '',
        'code' => '',
    ];

    $fetch = stripe_fetch_checkout_session($sessionId);
    if (!$fetch['ok'] || $fetch['session'] === null) {
        $fail['error'] = $fetch['error'] !== '' ? $fetch['error'] : 'Session introuvable.';
        return $fail;
    }

    $session = $fetch['session'];
    if (!stripe_session_is_paid_livre($session)) {
        $fail['error'] = 'Paiement non confirme pour cette commande livre.';
        return $fail;
    }

    $ctx = stripe_livre_session_context($session);
    if ($ctx['email'] === '' && !empty($clientHints['email']) && is_string($clientHints['email'])) {
        $hintEmail = trim($clientHints['email']);
        if (filter_var($hintEmail, FILTER_VALIDATE_EMAIL)) {
            $ctx['email'] = $hintEmail;
        }
    }
    if ($ctx['email'] === '' || !filter_var($ctx['email'], FILTER_VALIDATE_EMAIL)) {
        $fail['error'] = 'Email client manquant sur la session Stripe.';
        return $fail;
    }
    if ($ctx['slug'] === '') {
        $fail['error'] = 'Reference livre manquante sur la commande.';
        return $fail;
    }

    $state = stripe_livre_fulfillment_state($sessionId);
    if ($state['invoice'] && $state['delivery']) {
        $existing = livre_download_load_by_session($sessionId);
        $code = is_array($existing) ? (string) ($existing['code'] ?? '') : '';
        $token = is_array($existing) ? (string) ($existing['token'] ?? '') : '';
        return [
            'ok' => true,
            'error' => '',
            'invoice_ok' => true,
            'delivery_ok' => true,
            'download_url' => livre_download_page_url($code, $token),
            'code' => $code,
        ];
    }

    $item = stripe_find_livre_item($ctx['slug']);
    if (!is_array($item)) {
        $fail['error'] = 'Livre catalogue introuvable.';
        return $fail;
    }

    $prestafactureRequired = prestafacture_configured();
    $invoiceOk = $state['invoice'];

    if (!$invoiceOk && $prestafactureRequired) {
        $inv = stripe_fulfill_livre_invoice($sessionId, $ctx, $item);
        $invoiceOk = $inv['ok'];
        if (!$invoiceOk) {
            $fail['error'] = $inv['error'] !== ''
                ? 'La facture n\'a pas pu etre envoyee : ' . $inv['error']
                : 'La facture n\'a pas pu etre envoyee. Le PDF n\'a pas ete envoye.';
            return $fail;
        }
    } elseif (!$invoiceOk && !$prestafactureRequired) {
        error_log('[stripe-livre-fulfill] Prestafacture absent — livraison seule (dev) session ' . $sessionId);
    } else {
        $invoiceOk = true;
    }

    $deliveryOk = $state['delivery'];
    $downloadUrl = '';
    $code = '';
    if (!$deliveryOk && ($invoiceOk || !$prestafactureRequired)) {
        $del = stripe_fulfill_livre_delivery($sessionId, $ctx, $item);
        $deliveryOk = $del['ok'];
        $downloadUrl = $del['download_url'];
        $code = $del['code'];
        if (!$deliveryOk) {
            $fail['error'] = $del['error'] !== ''
                ? 'Facture OK, mais livraison PDF en echec : ' . $del['error']
                : 'Facture OK, mais livraison PDF en echec. Contactez contact@danielcraft.fr.';
            $fail['invoice_ok'] = $invoiceOk || $prestafactureRequired;
            $fail['download_url'] = $downloadUrl;
            $fail['code'] = $code;
            return $fail;
        }
    } elseif ($deliveryOk) {
        $existing = livre_download_load_by_session($sessionId);
        $code = is_array($existing) ? (string) ($existing['code'] ?? '') : '';
        $token = is_array($existing) ? (string) ($existing['token'] ?? '') : '';
        $downloadUrl = livre_download_page_url($code, $token);
    }

    return [
        'ok' => true,
        'error' => '',
        'invoice_ok' => $invoiceOk || $prestafactureRequired,
        'delivery_ok' => $deliveryOk,
        'download_url' => $downloadUrl,
        'code' => $code,
    ];
}
