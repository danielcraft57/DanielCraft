<?php
/**
 * Client API Facturio (routes publiques).
 * Base : https://facturio.danielcraft.fr/api/public
 * Auth : Authorization: Bearer fact_… (Paramètres → API — Jetons)
 */

declare(strict_types=1);

require_once __DIR__ . '/env.php';

function facturio_bootstrap(): void
{
    api_bootstrap_env();
}

function facturio_api_token(): string
{
    $token = getenv('FACTURIO_API_TOKEN') ?: getenv('FACTURIO_TOKEN') ?: '';
    return trim((string) $token);
}

function facturio_api_base(): string
{
    $base = trim((string) (getenv('FACTURIO_API_BASE') ?: getenv('FACTURIO_BASE_URL') ?: ''));
    if ($base === '') {
        return 'https://facturio.danielcraft.fr/api/public';
    }
    $base = rtrim($base, '/');
    if (str_ends_with($base, '/api/v1')) {
        $base = substr($base, 0, -3) . '/public';
    } elseif (str_ends_with($base, '/api') && !str_ends_with($base, '/public')) {
        $base .= '/public';
    } elseif (!str_contains($base, '/public')) {
        $base .= '/public';
    }

    return $base;
}

function facturio_configured(): bool
{
    $token = facturio_api_token();
    return $token !== '' && $token !== 'REPLACE_ME';
}

/**
 * @param array<string, mixed>|null $data
 */
function facturio_extract_id(?array $data, string ...$keys): string
{
    if ($data === null) {
        return '';
    }
    foreach ($keys as $key) {
        if (!isset($data[$key])) {
            continue;
        }
        $val = $data[$key];
        if (is_string($val) && $val !== '') {
            return $val;
        }
        if (is_int($val) || is_float($val)) {
            return (string) $val;
        }
    }
    if (isset($data['data']) && is_array($data['data'])) {
        return facturio_extract_id($data['data'], ...$keys);
    }
    return '';
}

/**
 * @param array<string, mixed>|null $jsonBody
 * @return array{ok: bool, status: int, data: array<string, mixed>|null, error: string}
 */
function facturio_http(string $method, string $path, ?array $jsonBody = null): array
{
    $token = facturio_api_token();
    if ($token === '' || $token === 'REPLACE_ME') {
        return ['ok' => false, 'status' => 500, 'data' => null, 'error' => 'FACTURIO_API_TOKEN non configuré.'];
    }

    $path = '/' . ltrim($path, '/');
    $url = facturio_api_base() . $path;
    $headers = [
        'Accept: application/json; charset=utf-8',
        'Authorization: Bearer ' . $token,
    ];
    if ($jsonBody !== null) {
        $headers[] = 'Content-Type: application/json; charset=utf-8';
    }

    if (!function_exists('curl_init')) {
        return ['ok' => false, 'status' => 502, 'data' => null, 'error' => 'cURL requis pour Facturio.'];
    }

    $ch = curl_init($url);
    $opts = [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_CONNECTTIMEOUT => 8,
        CURLOPT_TIMEOUT => 25,
        CURLOPT_HTTPHEADER => $headers,
        CURLOPT_CUSTOMREQUEST => strtoupper($method),
    ];
    if ($jsonBody !== null) {
        $opts[CURLOPT_POSTFIELDS] = json_encode($jsonBody, JSON_UNESCAPED_UNICODE);
    }
    curl_setopt_array($ch, $opts);
    $body = curl_exec($ch);
    $status = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
    $err = curl_error($ch);
    curl_close($ch);

    if ($body === false) {
        return ['ok' => false, 'status' => 502, 'data' => null, 'error' => 'Facturio : ' . ($err ?: 'réseau')];
    }

    $decoded = json_decode((string) $body, true);
    $data = is_array($decoded) ? $decoded : null;

    if ($status >= 200 && $status < 300) {
        return ['ok' => true, 'status' => $status, 'data' => $data, 'error' => ''];
    }

    $msg = 'Erreur Facturio HTTP ' . $status;
    if (is_array($data)) {
        if (isset($data['message']) && is_string($data['message'])) {
            $msg = $data['message'];
        } elseif (isset($data['error']) && is_string($data['error'])) {
            $msg = $data['error'];
        }
    }

    return ['ok' => false, 'status' => $status, 'data' => $data, 'error' => $msg];
}

/** Taux TVA décimal pour l’API (20 → 0.2). */
function facturio_tax_rate_decimal(float $taxRate): float
{
    if ($taxRate <= 0) {
        return 0.0;
    }
    if ($taxRate > 1) {
        return round($taxRate / 100.0, 4);
    }
    return round($taxRate, 4);
}

/** Prix HT à partir du TTC (ex. 0,94 € TTC, 20 % → 0,7833). */
function facturio_unit_price_ht(float $priceTtc, float $taxRatePercent): float
{
    $rate = $taxRatePercent > 1 ? $taxRatePercent : $taxRatePercent * 100;
    if ($rate <= 0) {
        return round($priceTtc, 4);
    }
    $divisor = 1.0 + ($rate / 100.0);
    return round($priceTtc / $divisor, 4);
}

/**
 * POST /public/factures — clientEmail + paidExternally.
 *
 * @return array{ok: bool, invoice_id: string, error: string}
 */
function facturio_create_paid_facture(
    string $customerEmail,
    string $customerName,
    string $lineDescription,
    float $unitPriceHt,
    float $taxRateDecimal
): array {
    $empty = ['ok' => false, 'invoice_id' => '', 'error' => ''];
    $email = trim($customerEmail);
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $empty['error'] = 'Email client invalide.';
        return $empty;
    }

    $name = trim(preg_replace('/[\r\n]+/', ' ', $customerName));
    if ($name === '') {
        $name = strstr($email, '@', true) ?: 'Client';
    }

    $res = facturio_http('POST', '/factures', [
        'clientEmail' => $email,
        'clientName' => mb_substr($name, 0, 200),
        'paidExternally' => true,
        'lines' => [
            [
                'description' => mb_substr($lineDescription, 0, 500),
                'quantity' => 1,
                'unitPrice' => $unitPriceHt,
                'taxRate' => $taxRateDecimal,
            ],
        ],
    ]);
    if (!$res['ok'] || !is_array($res['data'])) {
        $empty['error'] = $res['error'];
        return $empty;
    }

    $id = facturio_extract_id($res['data'], 'id', 'factureId', 'invoice_id');
    if ($id === '') {
        $empty['error'] = 'Réponse Facturio sans id facture.';
        return $empty;
    }

    return ['ok' => true, 'invoice_id' => $id, 'error' => ''];
}

/**
 * POST /public/factures/:id/send
 *
 * @return array{ok: bool, error: string, email_sent: bool}
 */
function facturio_send_facture_email(string $factureId, string $customerEmail): array
{
    $fail = ['ok' => false, 'error' => '', 'email_sent' => false];
    $factureId = trim($factureId);
    if ($factureId === '') {
        $fail['error'] = 'id facture invalide.';
        return $fail;
    }
    $email = trim($customerEmail);
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $fail['error'] = 'Email invalide.';
        return $fail;
    }

    $res = facturio_http('POST', '/factures/' . $factureId . '/send', [
        'email' => $email,
        'updateClientEmail' => true,
    ]);
    if (!$res['ok']) {
        $fail['error'] = $res['error'];
        return $fail;
    }

    $sent = false;
    if (is_array($res['data'])) {
        if (!empty($res['data']['emailSent'])) {
            $sent = true;
        } elseif (isset($res['data']['sentTo']) && is_string($res['data']['sentTo']) && $res['data']['sentTo'] !== '') {
            $sent = true;
        }
    }
    if (!$sent && $res['ok']) {
        $sent = true;
    }

    return ['ok' => true, 'error' => '', 'email_sent' => $sent];
}

/**
 * Crée la facture payée (paiement Stripe) puis envoie l’email.
 *
 * @return array{ok: bool, invoice_id: string, error: string}
 */
function facturio_issue_audit_invoice(
    string $customerEmail,
    string $customerName,
    string $serviceTitle,
    float $priceTtc,
    float $taxRatePercent = 20.0,
    string $siteUrl = ''
): array {
    $empty = ['ok' => false, 'invoice_id' => '', 'email_sent' => false, 'error' => '', 'warning' => ''];
    if (!facturio_configured()) {
        $empty['error'] = 'Facturio non configuré.';
        return $empty;
    }

    $description = trim($serviceTitle);
    if ($siteUrl !== '') {
        $description .= ' — ' . mb_substr($siteUrl, 0, 120);
    }

    $unitHt = facturio_unit_price_ht($priceTtc, $taxRatePercent);
    $taxDecimal = facturio_tax_rate_decimal($taxRatePercent);

    $invoice = facturio_create_paid_facture(
        $customerEmail,
        $customerName,
        $description,
        $unitHt,
        $taxDecimal
    );
    if (!$invoice['ok']) {
        $empty['error'] = $invoice['error'];
        return $empty;
    }

    $send = facturio_send_facture_email($invoice['invoice_id'], $customerEmail);
    if (!$send['ok']) {
        error_log('[facturio] send facture ' . $invoice['invoice_id'] . ': ' . $send['error']);
        // Facture créée (PAID) même si l’email Facturio échoue (ex. SMTP non configuré côté Facturio).
        return [
            'ok' => true,
            'invoice_id' => $invoice['invoice_id'],
            'email_sent' => false,
            'error' => '',
            'warning' => $send['error'],
        ];
    }

    return [
        'ok' => true,
        'invoice_id' => $invoice['invoice_id'],
        'email_sent' => !empty($send['email_sent']),
        'error' => '',
        'warning' => '',
    ];
}
