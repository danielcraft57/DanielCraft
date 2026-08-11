<?php
/**
 * Après paiement Stripe (audit premium) : facture Prestafacture + lancement audit ProspectLab.
 */

declare(strict_types=1);

require_once __DIR__ . '/stripe-audit-common.php';
require_once __DIR__ . '/prestafacture-common.php';
require_once __DIR__ . '/prospectlab-common.php';

/**
 * @return array{invoice: bool, audit: bool, skipped: bool}
 */
function stripe_audit_fulfillment_state(string $sessionId): array
{
    $file = stripe_audit_fulfillment_state_file($sessionId);
    if (!is_file($file)) {
        return ['invoice' => false, 'audit' => false, 'skipped' => false];
    }
    $raw = @file_get_contents($file);
    $data = is_string($raw) ? json_decode($raw, true) : null;
    if (!is_array($data)) {
        return ['invoice' => false, 'audit' => false, 'skipped' => false];
    }
    return [
        'invoice' => !empty($data['invoice']),
        'audit' => !empty($data['audit']),
        'skipped' => !empty($data['skipped']),
    ];
}

function stripe_audit_fulfillment_state_file(string $sessionId): string
{
    $dir = rtrim(sys_get_temp_dir(), DIRECTORY_SEPARATOR) . DIRECTORY_SEPARATOR . 'dc_audit_fulfill';
    if (!is_dir($dir)) {
        @mkdir($dir, 0700, true);
    }
    return $dir . DIRECTORY_SEPARATOR . 'sess_' . sha1($sessionId) . '.json';
}

/**
 * @param array{invoice?: bool, audit?: bool, skipped?: bool} $patch
 */
function stripe_audit_fulfillment_mark(string $sessionId, array $patch): void
{
    $file = stripe_audit_fulfillment_state_file($sessionId);
    $state = stripe_audit_fulfillment_state($sessionId);
    foreach (['invoice', 'audit', 'skipped'] as $key) {
        if (array_key_exists($key, $patch) && $patch[$key]) {
            $state[$key] = true;
        }
    }
    @file_put_contents($file, json_encode($state, JSON_UNESCAPED_UNICODE), LOCK_EX);
}

/**
 * @param array<string, mixed> $session
 */
function stripe_session_is_paid_audit(array $session): bool
{
    $status = isset($session['payment_status']) ? (string) $session['payment_status'] : '';
    if ($status !== 'paid') {
        return false;
    }
    $meta = is_array($session['metadata'] ?? null) ? $session['metadata'] : [];
    $productType = isset($meta['product_type']) ? (string) $meta['product_type'] : '';
    if ($productType === 'audit_ia') {
        return true;
    }
    return isset($meta['audit_slug']) && (string) $meta['audit_slug'] !== '';
}

/**
 * @param array<string, mixed> $session
 * @return array{email: string, name: string, site_url: string, slug: string}
 */
function stripe_audit_session_context(array $session): array
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

    $name = isset($meta['customer_name']) ? trim((string) $meta['customer_name']) : '';
    $siteUrl = isset($meta['site_url']) ? trim((string) $meta['site_url']) : '';
    $slug = isset($meta['audit_slug']) ? trim((string) $meta['audit_slug']) : 'audit-complet-ia';

    return [
        'email' => $email,
        'name' => $name,
        'site_url' => $siteUrl,
        'slug' => $slug,
    ];
}

/**
 * Étape 1 — facture Prestafacture (email) uniquement.
 *
 * @return array{ok: bool, error: string, invoice_id: string, email_sent: bool}
 */
function stripe_fulfill_audit_invoice(string $sessionId, array $ctx, array $item): array
{
    $empty = ['ok' => false, 'error' => '', 'invoice_id' => '', 'email_sent' => false];
    $state = stripe_audit_fulfillment_state($sessionId);
    if ($state['invoice']) {
        return ['ok' => true, 'error' => '', 'invoice_id' => '', 'email_sent' => true];
    }

    if (!prestafacture_configured()) {
        $empty['error'] = 'Prestafacture non configuré.';
        return $empty;
    }

    $title = trim((string) ($item['title'] ?? 'Audit premium site web'));
    $priceTtc = (float) ($item['price_eur'] ?? 199);
    $taxRate = (float) ($item['tax_rate'] ?? 20);

    $inv = prestafacture_issue_audit_invoice(
        $ctx['email'],
        $ctx['name'],
        $title,
        $priceTtc,
        $taxRate,
        $ctx['site_url']
    );
    if (!$inv['ok'] || ($inv['invoice_id'] ?? '') === '') {
        error_log('[stripe-audit-fulfill] Prestafacture session ' . $sessionId . ': ' . ($inv['error'] ?? ''));
        $empty['error'] = $inv['error'] !== '' ? $inv['error'] : 'Création facture impossible.';
        return $empty;
    }

    if (empty($inv['email_sent'])) {
        error_log('[stripe-audit-fulfill] Facture ' . $inv['invoice_id'] . ' créée, envoi email Prestafacture en échec : ' . ($inv['warning'] ?? ''));
    }

    stripe_audit_fulfillment_mark($sessionId, ['invoice' => true]);
    return [
        'ok' => true,
        'error' => '',
        'invoice_id' => (string) $inv['invoice_id'],
        'email_sent' => !empty($inv['email_sent']),
    ];
}

/**
 * Étape 2 — audit ProspectLab (uniquement après facture envoyée).
 *
 * @return array{ok: bool, error: string, queued: bool, task_id: string}
 */
function stripe_fulfill_audit_run(string $sessionId, array $ctx): array
{
    $empty = ['ok' => false, 'error' => '', 'queued' => false, 'task_id' => ''];
    $state = stripe_audit_fulfillment_state($sessionId);
    if ($state['audit']) {
        return ['ok' => true, 'error' => '', 'queued' => true, 'task_id' => ''];
    }

    $website = pl_normalize_website($ctx['site_url']);
    if ($website === '') {
        $empty['error'] = 'URL du site manquante sur la commande.';
        return $empty;
    }
    if (!pl_has_audit_auth()) {
        $empty['error'] = 'Service d’audit indisponible.';
        return $empty;
    }

    $audit = pl_request_website_audit_report($website, $ctx['email'], true);
    if (!$audit['ok']) {
        error_log('[stripe-audit-fulfill] ProspectLab session ' . $sessionId . ': ' . $audit['error']);
        $empty['error'] = $audit['error'];
        return $empty;
    }

    stripe_audit_fulfillment_mark($sessionId, ['audit' => true]);
    return [
        'ok' => true,
        'error' => '',
        'queued' => $audit['queued'],
        'task_id' => $audit['task_id'],
    ];
}

/**
 * Après paiement : 1) facture par email, 2) audit complet (idempotent par session_id).
 *
 * @param array{site_url?: string, email?: string} $clientHints secours si metadata Stripe incomplète
 * @return array{ok: bool, error: string, invoice_ok: bool, audit_ok: bool}
 */
function stripe_fulfill_audit_checkout_session(string $sessionId, array $clientHints = []): array
{
    $fail = ['ok' => false, 'error' => '', 'invoice_ok' => false, 'audit_ok' => false];

    $fetch = stripe_fetch_checkout_session($sessionId);
    if (!$fetch['ok'] || $fetch['session'] === null) {
        $fail['error'] = $fetch['error'] !== '' ? $fetch['error'] : 'Session introuvable.';
        return $fail;
    }

    $session = $fetch['session'];
    if (!stripe_session_is_paid_audit($session)) {
        $fail['error'] = 'Paiement non confirmé pour cette commande audit.';
        return $fail;
    }

    $ctx = stripe_audit_session_context($session);
    if ($ctx['site_url'] === '' && !empty($clientHints['site_url']) && is_string($clientHints['site_url'])) {
        $hintSite = pl_normalize_website(trim(strip_tags($clientHints['site_url'])));
        if ($hintSite !== '') {
            $ctx['site_url'] = $hintSite;
        }
    }
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

    $state = stripe_audit_fulfillment_state($sessionId);
    if ($state['invoice'] && $state['audit']) {
        return ['ok' => true, 'error' => '', 'invoice_ok' => true, 'audit_ok' => true];
    }

    $item = stripe_find_audit_item($ctx['slug']);
    if (!is_array($item)) {
        $item = [
            'title' => 'Audit premium site web',
            'price_eur' => 199,
            'tax_rate' => 20,
        ];
    }

    $invoiceOk = $state['invoice'];
    $prestafactureRequired = prestafacture_configured();

    if (!$invoiceOk && $prestafactureRequired) {
        $inv = stripe_fulfill_audit_invoice($sessionId, $ctx, $item);
        $invoiceOk = $inv['ok'];
        if (!$invoiceOk) {
            $fail['error'] = $inv['error'] !== ''
                ? 'La facture n’a pas pu être envoyée : ' . $inv['error']
                : 'La facture n’a pas pu être envoyée. L’audit n’a pas été lancé.';
            return $fail;
        }
    } elseif (!$invoiceOk && !$prestafactureRequired) {
        error_log('[stripe-audit-fulfill] Prestafacture absent — audit seul (dev) session ' . $sessionId);
        $invoiceOk = false;
    } else {
        $invoiceOk = true;
    }

    // Audit uniquement après facture OK (ou si Prestafacture non configuré en local)
    $auditOk = $state['audit'];
    if (!$auditOk && ($invoiceOk || !$prestafactureRequired)) {
        $run = stripe_fulfill_audit_run($sessionId, $ctx);
        $auditOk = $run['ok'];
        if (!$auditOk) {
            $fail['error'] = $run['error'] !== ''
                ? 'Facture envoyée, mais l’audit n’a pas démarré : ' . $run['error']
                : 'Facture envoyée, mais l’audit n’a pas démarré. Contactez le support.';
            $fail['invoice_ok'] = $invoiceOk || $prestafactureRequired;
            return $fail;
        }
    }

    return [
        'ok' => true,
        'error' => '',
        'invoice_ok' => $invoiceOk || $prestafactureRequired,
        'audit_ok' => $auditOk,
    ];
}
