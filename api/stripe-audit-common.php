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

/** Montant Checkout en centimes (min. Stripe EUR : 50 = 0,50 €). */
function stripe_audit_unit_amount_cents(array $item): int
{
    if (isset($item['price_cents']) && is_numeric($item['price_cents'])) {
        return (int) $item['price_cents'];
    }
    $priceEur = $item['price_eur'] ?? 199;
    if (!is_numeric($priceEur)) {
        return 19900;
    }

    return (int) round((float) $priceEur * 100);
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
 * Paramètres Stripe Checkout enrichis (texte, image, carte + PayPal).
 *
 * @return array<string, string|int>
 */
function stripe_audit_checkout_session_params(array $item, string $slug, string $siteUrl, string $customerName): array
{
    $base = api_site_base();
    $productName = trim((string) ($item['checkout_product_name'] ?? $item['title'] ?? 'Audit premium site web'));
    $description = trim((string) ($item['checkout_description'] ?? ''));
    if ($description === '') {
        $description = 'Facture par email juste après le paiement, puis audit complet de votre site.';
    }
    if ($siteUrl !== '') {
        $description .= ' Site : ' . mb_substr($siteUrl, 0, 200);
    }

    $imageUrl = trim((string) ($item['checkout_image_url'] ?? ''));
    if ($imageUrl === '' || !filter_var($imageUrl, FILTER_VALIDATE_URL)) {
        $imageUrl = $base . '/assets/icons/favicons/android-icon-192x192.png';
    }

    $params = [
        'locale' => 'fr',
        'payment_method_types[0]' => 'card',
        'payment_method_types[1]' => 'paypal',
        'line_items[0][price_data][product_data][name]' => mb_substr($productName, 0, 120),
        'line_items[0][price_data][product_data][description]' => mb_substr($description, 0, 500),
        'line_items[0][price_data][product_data][images][0]' => $imageUrl,
        'custom_text[submit][message]' => 'Vous recevrez d’abord votre facture par email, puis l’audit complet sera lancé.',
        'custom_text[after_submit][message]' => 'Merci ! Consultez vos emails : facture, puis rapport d’audit sous 48 h.',
    ];

    if ($customerName !== '') {
        $params['metadata[customer_name]'] = mb_substr($customerName, 0, 120);
    }

    return $params;
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

    $unitAmount = stripe_audit_unit_amount_cents($item);
    if ($unitAmount < 50 || $unitAmount > 9_999_900) {
        return ['ok' => false, 'url' => '', 'session_id' => '', 'error' => 'Prix audit invalide (minimum Stripe : 0,50 €).'];
    }

    $base = api_site_base();
    $successUrl = $base . '/audit?stripe=success&session_id={CHECKOUT_SESSION_ID}';
    $cancelUrl = $base . '/audit?stripe=cancel';

    $siteUrl = preg_replace('/[\r\n]+/', '', trim($siteUrl));
    $customerName = preg_replace('/[\r\n]+/', '', trim($customerName));

    $params = array_merge([
        'mode' => 'payment',
        'success_url' => $successUrl,
        'cancel_url' => $cancelUrl,
        'line_items[0][quantity]' => 1,
        'line_items[0][price_data][currency]' => 'eur',
        'line_items[0][price_data][unit_amount]' => $unitAmount,
        'metadata[audit_slug]' => $slug,
        'metadata[product_type]' => 'audit_ia',
        'payment_intent_data[metadata][audit_slug]' => $slug,
        'payment_intent_data[description]' => mb_substr(
            trim((string) ($item['checkout_product_name'] ?? $item['title'] ?? 'Audit premium')),
            0,
            200
        ),
    ], stripe_audit_checkout_session_params($item, $slug, $siteUrl, $customerName));

    if ($siteUrl !== '') {
        $params['metadata[site_url]'] = mb_substr($siteUrl, 0, 450);
        $params['payment_intent_data[metadata][site_url]'] = mb_substr($siteUrl, 0, 450);
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
