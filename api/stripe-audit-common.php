<?php
/**
 * Catalogue audits payants + session Stripe Checkout.
 */

declare(strict_types=1);

require_once __DIR__ . '/stripe-common.php';

/**
 * @return array<string, mixed>|null
 */
function stripe_load_audits_catalog(): ?array
{
    $paths = [
        __DIR__ . '/data/audits.json',
        __DIR__ . '/../data/audits.json',
        __DIR__ . '/../src/data/audits.json',
    ];
    foreach ($paths as $path) {
        if (!is_file($path) || !is_readable($path)) {
            continue;
        }
        $raw = file_get_contents($path);
        if ($raw === false) {
            continue;
        }
        $data = json_decode($raw, true);
        if (is_array($data)) {
            return $data;
        }
    }
    return null;
}

/**
 * @return array<string, mixed>|null
 */
function stripe_find_audit_item(string $slug): ?array
{
    if (!preg_match('/^[a-z0-9-]{1,80}$/', $slug)) {
        return null;
    }
    $catalog = stripe_load_audits_catalog();
    $paid = is_array($catalog['paid_audit'] ?? null) ? $catalog['paid_audit'] : null;
    if ($paid === null) {
        return null;
    }
    if (($paid['slug'] ?? '') === $slug) {
        return $paid;
    }
    return null;
}

/**
 * @return array{ok: bool, url: string, session_id: string, error: string}
 */
function stripe_create_audit_checkout_session(
    string $slug,
    string $customerEmail = '',
    string $siteUrl = '',
    string $customerName = ''
): array {
    $item = stripe_find_audit_item($slug);
    if ($item === null) {
        return ['ok' => false, 'url' => '', 'session_id' => '', 'error' => 'Offre audit introuvable.'];
    }

    $staticLink = trim((string) ($item['stripe_payment_link_url'] ?? ''));
    if ($staticLink !== '' && filter_var($staticLink, FILTER_VALIDATE_URL)) {
        return ['ok' => true, 'url' => $staticLink, 'session_id' => '', 'error' => ''];
    }

    $priceEur = (int) ($item['price_eur'] ?? 19);
    if ($priceEur < 1 || $priceEur > 99999) {
        return ['ok' => false, 'url' => '', 'session_id' => '', 'error' => 'Prix audit invalide.'];
    }

    $title = trim((string) ($item['title'] ?? 'Audit complet IA'));
    $base = api_site_base();
    $successUrl = $base . '/audit?stripe=success&session_id={CHECKOUT_SESSION_ID}';
    $cancelUrl = $base . '/audit?stripe=cancel';

    $siteUrl = preg_replace('/[\r\n]+/', '', trim($siteUrl));
    $customerName = preg_replace('/[\r\n]+/', '', trim($customerName));

    $params = [
        'mode' => 'payment',
        'success_url' => $successUrl,
        'cancel_url' => $cancelUrl,
        'line_items[0][quantity]' => 1,
        'line_items[0][price_data][currency]' => 'eur',
        'line_items[0][price_data][unit_amount]' => $priceEur * 100,
        'line_items[0][price_data][product_data][name]' => $title . ' — DanielCraft',
        'metadata[audit_slug]' => $slug,
        'metadata[product_type]' => 'audit_ia',
        'payment_intent_data[metadata][audit_slug]' => $slug,
    ];

    if ($siteUrl !== '') {
        $params['metadata[site_url]'] = mb_substr($siteUrl, 0, 450);
        $params['payment_intent_data[metadata][site_url]'] = mb_substr($siteUrl, 0, 450);
    }
    if ($customerName !== '') {
        $params['metadata[customer_name]'] = mb_substr($customerName, 0, 120);
    }

    if ($customerEmail !== '' && filter_var($customerEmail, FILTER_VALIDATE_EMAIL)) {
        $params['customer_email'] = $customerEmail;
    }

    $res = stripe_api('POST', '/checkout/sessions', $params);
    if (!$res['ok'] || !is_array($res['data'])) {
        return ['ok' => false, 'url' => '', 'session_id' => '', 'error' => $res['error']];
    }

    $url = isset($res['data']['url']) ? (string) $res['data']['url'] : '';
    $sessionId = isset($res['data']['id']) ? (string) $res['data']['id'] : '';
    if ($url === '') {
        return ['ok' => false, 'url' => '', 'session_id' => '', 'error' => 'Session Checkout sans URL.'];
    }

    return ['ok' => true, 'url' => $url, 'session_id' => $sessionId, 'error' => ''];
}
