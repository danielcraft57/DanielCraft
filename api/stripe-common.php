<?php
/**
 * Catalogue vitrines + appels API Stripe (cURL, sans SDK).
 */

declare(strict_types=1);

require_once __DIR__ . '/env.php';

api_bootstrap_env();

function stripe_secret_key(): string
{
    $key = getenv('STRIPE_SECRET_KEY') ?: '';
    return trim((string) $key);
}

function stripe_publishable_key(): string
{
    $key = getenv('STRIPE_PUBLISHABLE_KEY') ?: '';
    return trim((string) $key);
}

/**
 * @return array<string, mixed>|null
 */
function stripe_load_catalog(): ?array
{
    $paths = [
        __DIR__ . '/data/vitrines.json',
        __DIR__ . '/../data/vitrines.json',
        __DIR__ . '/../src/data/vitrines.json',
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
function stripe_find_vitrine_item(string $slug): ?array
{
    if (!preg_match('/^[a-z0-9-]{1,80}$/', $slug)) {
        return null;
    }
    $catalog = stripe_load_catalog();
    if (!$catalog || !is_array($catalog['items'] ?? null)) {
        return null;
    }
    foreach ($catalog['items'] as $item) {
        if (!is_array($item)) {
            continue;
        }
        if (($item['slug'] ?? '') === $slug) {
            return $item;
        }
    }
    return null;
}

/**
 * @param array<string, string|int|bool> $params
 * @return array{ok: bool, http: int, data: array<string, mixed>|null, error: string}
 */
function stripe_api(string $method, string $path, array $params = []): array
{
    $secret = stripe_secret_key();
    if ($secret === '' || !str_starts_with($secret, 'sk_')) {
        return ['ok' => false, 'http' => 0, 'data' => null, 'error' => 'STRIPE_SECRET_KEY manquante ou invalide.'];
    }

    $url = 'https://api.stripe.com/v1' . $path;
    $ch = curl_init($url);
    if ($ch === false) {
        return ['ok' => false, 'http' => 0, 'data' => null, 'error' => 'cURL indisponible.'];
    }

    $headers = ['Content-Type: application/x-www-form-urlencoded'];
    curl_setopt_array($ch, [
        CURLOPT_USERPWD => $secret . ':',
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT => 30,
        CURLOPT_HTTPHEADER => $headers,
    ]);

    $method = strtoupper($method);
    if ($method === 'GET' && $params !== []) {
        $url .= '?' . http_build_query($params);
        curl_setopt($ch, CURLOPT_URL, $url);
    } elseif ($method === 'POST') {
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($params));
    } else {
        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, $method);
        if ($params !== []) {
            curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($params));
        }
    }

    $body = curl_exec($ch);
    $http = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
    $curlErr = curl_error($ch);
    curl_close($ch);

    if ($body === false) {
        return ['ok' => false, 'http' => $http, 'data' => null, 'error' => $curlErr ?: 'Erreur réseau Stripe.'];
    }

    $decoded = json_decode((string) $body, true);
    if (!is_array($decoded)) {
        return ['ok' => false, 'http' => $http, 'data' => null, 'error' => 'Réponse Stripe illisible.'];
    }

    if ($http < 200 || $http >= 300) {
        $msg = isset($decoded['error']['message']) ? (string) $decoded['error']['message'] : 'Erreur Stripe HTTP ' . $http;
        return ['ok' => false, 'http' => $http, 'data' => $decoded, 'error' => $msg];
    }

    return ['ok' => true, 'http' => $http, 'data' => $decoded, 'error' => ''];
}

/**
 * @return array{ok: bool, url: string, session_id: string, error: string}
 */
function stripe_create_checkout_session(string $slug, string $customerEmail = ''): array
{
    $item = stripe_find_vitrine_item($slug);
    if ($item === null) {
        return ['ok' => false, 'url' => '', 'session_id' => '', 'error' => 'Modèle catalogue introuvable.'];
    }

    $catalog = stripe_load_catalog();
    $defaultPrice = (int) ($catalog['default_price_eur'] ?? 42);
    $rawPrice = $item['price_eur'] ?? $defaultPrice;
    try {
        $priceEur = (int) $rawPrice;
    } catch (Throwable) {
        $priceEur = $defaultPrice;
    }
    if ($priceEur < 1 || $priceEur > 99999) {
        return ['ok' => false, 'url' => '', 'session_id' => '', 'error' => 'Prix catalogue invalide.'];
    }

    $title = trim((string) ($item['title'] ?? $slug));
    $base = api_site_base();
    $successUrl = $base . '/vitrines/' . rawurlencode($slug) . '/?stripe=success&session_id={CHECKOUT_SESSION_ID}';
    $cancelUrl = $base . '/vitrines/' . rawurlencode($slug) . '/?stripe=cancel';

    $params = [
        'mode' => 'payment',
        'success_url' => $successUrl,
        'cancel_url' => $cancelUrl,
        'line_items[0][quantity]' => 1,
        'line_items[0][price_data][currency]' => 'eur',
        'line_items[0][price_data][unit_amount]' => $priceEur * 100,
        'line_items[0][price_data][product_data][name]' => $title . ' — maquette DanielCraft',
        'metadata[vitrine_slug]' => $slug,
        'metadata[vitrine_title]' => $title,
        'payment_intent_data[metadata][vitrine_slug]' => $slug,
    ];

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
