<?php
/**
 * Client API Prestafacture (routes publiques).
 * Base : https://prestafacture.com/api/public
 * Auth : Authorization: Bearer fact_… (Paramètres → API — Jetons)
 */

declare(strict_types=1);

require_once __DIR__ . '/env.php';

function prestafacture_bootstrap(): void
{
    api_bootstrap_env();
}

function prestafacture_api_token(): string
{
    $token = getenv('PRESTAFACTURE_API_TOKEN')
        ?: getenv('FACTURIO_API_TOKEN')
        ?: getenv('PRESTAFACTURE_TOKEN')
        ?: getenv('FACTURIO_TOKEN')
        ?: '';
    return trim((string) $token);
}

function prestafacture_api_base(): string
{
    $base = trim((string) (
        getenv('PRESTAFACTURE_API_BASE')
        ?: getenv('FACTURIO_API_BASE')
        ?: getenv('PRESTAFACTURE_BASE_URL')
        ?: getenv('FACTURIO_BASE_URL')
        ?: ''
    ));
    if ($base === '') {
        return 'https://prestafacture.com/api/public';
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

function prestafacture_configured(): bool
{
    $token = prestafacture_api_token();
    return $token !== '' && $token !== 'REPLACE_ME';
}

/**
 * @param array<string, mixed>|null $data
 */
function prestafacture_extract_id(?array $data, string ...$keys): string
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
        return prestafacture_extract_id($data['data'], ...$keys);
    }
    return '';
}

function prestafacture_parse_api_error(int $status, ?array $data): string
{
    $msg = 'Erreur Prestafacture HTTP ' . $status;
    if (is_array($data)) {
        if (isset($data['message']) && is_string($data['message'])) {
            $msg = $data['message'];
        } elseif (isset($data['error']) && is_string($data['error'])) {
            $msg = $data['error'];
        }
    }
    if ($status === 403 && str_contains($msg, 'Permission API manquante')) {
        $msg .= ' — recréez le jeton Prestafacture avec les scopes requis (clients : clients.read, clients.write ; devis : devis.read, devis.write, devis.send ; audit : factures.read, factures.write, factures.send).';
    }

    return $msg;
}

/**
 * @param array<string, mixed>|null $jsonBody
 * @return array{ok: bool, status: int, data: array<string, mixed>|null, error: string}
 */
function prestafacture_http(string $method, string $path, ?array $jsonBody = null): array
{
    $token = prestafacture_api_token();
    if ($token === '' || $token === 'REPLACE_ME') {
        return ['ok' => false, 'status' => 500, 'data' => null, 'error' => 'prestafacture_API_TOKEN non configuré.'];
    }

    $path = '/' . ltrim($path, '/');
    $url = prestafacture_api_base() . $path;
    $headers = [
        'Accept: application/json; charset=utf-8',
        'Authorization: Bearer ' . $token,
    ];
    if ($jsonBody !== null) {
        $headers[] = 'Content-Type: application/json; charset=utf-8';
    }

    $method = strtoupper($method);
    $payload = $jsonBody !== null ? json_encode($jsonBody, JSON_UNESCAPED_UNICODE) : null;

    if (function_exists('curl_init')) {
        $ch = curl_init($url);
        $opts = [
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_CONNECTTIMEOUT => 8,
            CURLOPT_TIMEOUT => 25,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_CUSTOMREQUEST => $method,
        ];
        if ($payload !== null) {
            $opts[CURLOPT_POSTFIELDS] = $payload;
        }
        curl_setopt_array($ch, $opts);
        $body = curl_exec($ch);
        $status = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
        $err = curl_error($ch);
        curl_close($ch);

        if ($body === false) {
            return ['ok' => false, 'status' => 502, 'data' => null, 'error' => 'Prestafacture : ' . ($err ?: 'réseau')];
        }
    } else {
        $headerLines = implode("\r\n", $headers);
        if ($payload !== null) {
            $headerLines .= "\r\nContent-Length: " . strlen($payload);
        }
        $context = stream_context_create([
            'http' => [
                'method' => $method,
                'header' => $headerLines . "\r\n",
                'content' => $payload,
                'ignore_errors' => true,
                'timeout' => 25,
            ],
            'ssl' => [
                'verify_peer' => true,
                'verify_peer_name' => true,
            ],
        ]);
        $body = @file_get_contents($url, false, $context);
        if ($body === false) {
            return ['ok' => false, 'status' => 502, 'data' => null, 'error' => 'Prestafacture : échec HTTP (file_get_contents).'];
        }
        $status = 200;
        if (isset($http_response_header) && is_array($http_response_header)) {
            foreach ($http_response_header as $line) {
                if (preg_match('#^HTTP/\S+\s+(\d{3})#', (string) $line, $m)) {
                    $status = (int) $m[1];
                    break;
                }
            }
        }
    }

    $decoded = json_decode((string) $body, true);
    $data = is_array($decoded) ? $decoded : null;

    if ($status >= 200 && $status < 300) {
        return ['ok' => true, 'status' => $status, 'data' => $data, 'error' => ''];
    }

    return ['ok' => false, 'status' => $status, 'data' => $data, 'error' => prestafacture_parse_api_error($status, $data)];
}

/** Taux TVA décimal pour l’API (20 → 0.2). */
function prestafacture_tax_rate_decimal(float $taxRate): float
{
    if ($taxRate <= 0) {
        return 0.0;
    }
    if ($taxRate > 1) {
        return round($taxRate / 100.0, 4);
    }
    return round($taxRate, 4);
}

/**
 * Id produit Prestafacture depuis une entrée catalogue (prestations.json).
 */
function prestafacture_product_id_from_catalog(array $entry): ?int
{
    $raw = $entry['prestafacture_product_id'] ?? $entry['facturio_product_id'] ?? null;
    if ($raw === null) {
        return null;
    }
    $id = (int) $raw;
    return $id > 0 ? $id : null;
}

/**
 * Libellé court pour une ligne de devis Prestafacture (pas le long texte catalogue).
 */
function prestafacture_prestation_line_label(array $item, string $addonTitle = ''): string
{
    $title = trim(preg_replace('/[\r\n]+/', ' ', (string) ($item['title'] ?? 'Prestation')));
    if ($addonTitle !== '') {
        $line = $title . ' — ' . trim(preg_replace('/[\r\n]+/', ' ', $addonTitle));

        return mb_substr($line, 0, 160);
    }
    $short = trim(preg_replace('/[\r\n]+/', ' ', (string) ($item['short_description'] ?? '')));
    if ($short !== '') {
        return mb_substr($short, 0, 160);
    }

    return mb_substr($title, 0, 120);
}

/**
 * Ligne de devis/facture à partir d’un prix catalogue HT (prestations DanielCraft).
 *
 * @return array{description: string, quantity: float, unitPrice: float, taxRate: float, productId?: int}
 */
function prestafacture_line_from_price_ht(
    string $description,
    float $priceEurHt,
    float $taxRatePercent = 20.0,
    ?int $productId = null
): array {
    $line = [
        'description' => mb_substr(trim($description), 0, 200),
        'quantity' => 1,
        'unitPrice' => round(max(0.0, $priceEurHt), 2),
        'taxRate' => prestafacture_tax_rate_decimal($taxRatePercent),
    ];
    if ($productId !== null && $productId > 0) {
        $line['productId'] = $productId;
    }

    return $line;
}

/** Prix HT à partir du TTC (ex. 199 € TTC audit, 20 % → 165,83). */
function prestafacture_unit_price_ht(float $priceTtc, float $taxRatePercent): float
{
    $rate = $taxRatePercent > 1 ? $taxRatePercent : $taxRatePercent * 100;
    if ($rate <= 0) {
        return round($priceTtc, 4);
    }
    $divisor = 1.0 + ($rate / 100.0);
    return round($priceTtc / $divisor, 4);
}

/**
 * Champs client Prestafacture à partir du contact formulaire (personne + entreprise optionnelle).
 *
 * @return array{name: string, isCompany: bool}
 */
function prestafacture_client_fields_from_contact(string $personName, string $companyName = ''): array
{
    $companyName = trim(preg_replace('/[\r\n]+/', ' ', $companyName));
    $personName = trim(preg_replace('/[\r\n]+/', ' ', $personName));

    if ($companyName !== '') {
        return [
            'name' => mb_substr($companyName, 0, 200),
            'isCompany' => true,
        ];
    }

    $name = $personName !== '' ? $personName : 'Client';

    return [
        'name' => mb_substr($name, 0, 200),
        'isCompany' => false,
    ];
}

/**
 * Libellé affiché (e-mails de secours, logs).
 */
function prestafacture_client_display_name(string $personName, string $companyName = ''): string
{
    $companyName = trim(preg_replace('/[\r\n]+/', ' ', $companyName));
    $personName = trim(preg_replace('/[\r\n]+/', ' ', $personName));
    if ($companyName !== '' && $personName !== '') {
        return $companyName . ' — ' . $personName;
    }
    if ($companyName !== '') {
        return $companyName;
    }
    if ($personName !== '') {
        return $personName;
    }

    return 'Client';
}

/**
 * @param array<string, mixed> $data
 * @return list<array<string, mixed>>
 */
function prestafacture_client_list_items(?array $data): array
{
    if ($data === null) {
        return [];
    }
    $items = $data['items'] ?? $data['data'] ?? $data;
    if (!is_array($items)) {
        return [];
    }
    if ($items !== [] && !isset($items[0]) && isset($items['id'])) {
        return [$items];
    }

    $out = [];
    foreach ($items as $item) {
        if (is_array($item)) {
            $out[] = $item;
        }
    }

    return $out;
}

/**
 * Recherche un client Prestafacture par e-mail (GET /public/clients?search=).
 *
 * @return array<string, mixed>|null
 */
function prestafacture_find_client_by_email(string $email): ?array
{
    $email = strtolower(trim($email));
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        return null;
    }

    $query = http_build_query([
        'page' => 1,
        'pageSize' => 20,
        'search' => $email,
    ]);
    $res = prestafacture_http('GET', '/clients?' . $query);
    if (!$res['ok']) {
        return null;
    }

    foreach (prestafacture_client_list_items($res['data']) as $item) {
        $itemEmail = strtolower(trim((string) ($item['email'] ?? '')));
        if ($itemEmail === $email) {
            return $item;
        }
    }

    return null;
}

/**
 * Recherche un client Prestafacture par e-mail — retourne uniquement l’id.
 */
function prestafacture_find_client_id_by_email(string $email): string
{
    $client = prestafacture_find_client_by_email($email);
    if ($client === null) {
        return '';
    }

    return prestafacture_extract_id($client, 'id', 'clientId');
}

/**
 * POST /public/clients — crée une fiche client.
 *
 * @return array{ok: bool, client_id: string, error: string, status: int}
 */
function prestafacture_create_client(string $customerEmail, string $personName, string $companyName = ''): array
{
    $empty = ['ok' => false, 'client_id' => '', 'error' => '', 'status' => 0];
    $email = trim($customerEmail);
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $empty['error'] = 'Email client invalide.';
        return $empty;
    }

    $fields = prestafacture_client_fields_from_contact($personName, $companyName);
    if ($fields['name'] === 'Client' && str_contains($email, '@')) {
        $fields['name'] = strstr($email, '@', true) ?: 'Client';
    }

    $res = prestafacture_http('POST', '/clients', [
        'name' => $fields['name'],
        'email' => $email,
        'isCompany' => $fields['isCompany'],
        'countryCode' => 'FR',
    ]);
    if (!$res['ok'] || !is_array($res['data'])) {
        $empty['error'] = $res['error'] !== '' ? $res['error'] : 'Création client impossible.';
        $empty['status'] = (int) ($res['status'] ?? 0);
        return $empty;
    }

    $id = prestafacture_extract_id($res['data'], 'id', 'clientId');
    if ($id === '') {
        $empty['error'] = 'Réponse Prestafacture sans id client.';
        $empty['status'] = (int) ($res['status'] ?? 0);
        return $empty;
    }

    return ['ok' => true, 'client_id' => $id, 'error' => '', 'status' => (int) ($res['status'] ?? 201)];
}

/**
 * PATCH /public/clients/:id — met à jour une fiche client existante.
 *
 * @param array<string, mixed> $fields
 * @return array{ok: bool, error: string}
 */
function prestafacture_update_client(string $clientId, array $fields): array
{
    $fail = ['ok' => false, 'error' => ''];
    $clientId = trim($clientId);
    if ($clientId === '') {
        $fail['error'] = 'id client invalide.';
        return $fail;
    }
    if ($fields === []) {
        return ['ok' => true, 'error' => ''];
    }

    $res = prestafacture_http('PATCH', '/clients/' . rawurlencode($clientId), $fields);
    if (!$res['ok']) {
        $fail['error'] = $res['error'] !== '' ? $res['error'] : 'Mise à jour client impossible.';
        return $fail;
    }

    return ['ok' => true, 'error' => ''];
}

/**
 * Met à jour le nom / type société si le contact a changé depuis la dernière fiche.
 *
 * @param array<string, mixed> $existing
 */
function prestafacture_sync_client_record(array $existing, string $personName, string $companyName = ''): void
{
    $clientId = prestafacture_extract_id($existing, 'id', 'clientId');
    if ($clientId === '') {
        return;
    }

    $desired = prestafacture_client_fields_from_contact($personName, $companyName);
    $currentName = trim((string) ($existing['name'] ?? ''));
    $currentIsCompany = !empty($existing['isCompany']);

    $patch = [];
    if ($desired['name'] !== '' && $desired['name'] !== $currentName) {
        $patch['name'] = $desired['name'];
    }
    if ($desired['isCompany'] !== $currentIsCompany) {
        $patch['isCompany'] = $desired['isCompany'];
    }
    if ($patch === []) {
        return;
    }

    $updated = prestafacture_update_client($clientId, $patch);
    if (!$updated['ok']) {
        error_log('[Prestafacture] sync client ' . $clientId . ': ' . $updated['error']);
    }
}

/**
 * Résout clientId : recherche par e-mail, mise à jour si besoin, sinon création.
 * Requis pour POST /devis (clientId obligatoire).
 *
 * @return array{ok: bool, client_id: string, error: string, created: bool}
 */
function prestafacture_ensure_client_id(string $customerEmail, string $personName, string $companyName = ''): array
{
    $empty = ['ok' => false, 'client_id' => '', 'error' => '', 'created' => false];
    $email = trim($customerEmail);
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $empty['error'] = 'Email client invalide.';
        return $empty;
    }

    $existing = prestafacture_find_client_by_email($email);
    if ($existing !== null) {
        prestafacture_sync_client_record($existing, $personName, $companyName);
        $id = prestafacture_extract_id($existing, 'id', 'clientId');
        if ($id !== '') {
            return ['ok' => true, 'client_id' => $id, 'error' => '', 'created' => false];
        }
    }

    $created = prestafacture_create_client($email, $personName, $companyName);
    if ($created['ok']) {
        return [
            'ok' => true,
            'client_id' => $created['client_id'],
            'error' => '',
            'created' => true,
        ];
    }

    // Course : le client peut exister entre la recherche et la création.
    $retryId = prestafacture_find_client_id_by_email($email);
    if ($retryId !== '') {
        $retryClient = prestafacture_find_client_by_email($email);
        if ($retryClient !== null) {
            prestafacture_sync_client_record($retryClient, $personName, $companyName);
        }
        return ['ok' => true, 'client_id' => $retryId, 'error' => '', 'created' => false];
    }

    $empty['error'] = $created['error'] !== '' ? $created['error'] : 'Client Prestafacture introuvable.';
    return $empty;
}

/**
 * POST /public/factures — clientEmail + paidExternally.
 *
 * @return array{ok: bool, invoice_id: string, error: string}
 */
function prestafacture_create_paid_facture(
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

    $res = prestafacture_http('POST', '/factures', [
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

    $id = prestafacture_extract_id($res['data'], 'id', 'factureId', 'invoice_id');
    if ($id === '') {
        $empty['error'] = 'Réponse Prestafacture sans id facture.';
        return $empty;
    }

    return ['ok' => true, 'invoice_id' => $id, 'error' => ''];
}

/**
 * POST /public/factures/:id/send
 *
 * @return array{ok: bool, error: string, email_sent: bool}
 */
function prestafacture_send_facture_email(string $factureId, string $customerEmail): array
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

    $res = prestafacture_http('POST', '/factures/' . $factureId . '/send', [
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
function prestafacture_issue_audit_invoice(
    string $customerEmail,
    string $customerName,
    string $serviceTitle,
    float $priceTtc,
    float $taxRatePercent = 20.0,
    string $siteUrl = ''
): array {
    $empty = ['ok' => false, 'invoice_id' => '', 'email_sent' => false, 'error' => '', 'warning' => ''];
    if (!prestafacture_configured()) {
        $empty['error'] = 'Prestafacture non configuré.';
        return $empty;
    }

    $description = trim($serviceTitle);
    if ($siteUrl !== '') {
        $description .= ' — ' . mb_substr($siteUrl, 0, 120);
    }

    $unitHt = prestafacture_unit_price_ht($priceTtc, $taxRatePercent);
    $taxDecimal = prestafacture_tax_rate_decimal($taxRatePercent);

    $invoice = prestafacture_create_paid_facture(
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

    $send = prestafacture_send_facture_email($invoice['invoice_id'], $customerEmail);
    if (!$send['ok']) {
        error_log('[Prestafacture] send facture ' . $invoice['invoice_id'] . ': ' . $send['error']);
        // Facture créée (PAID) même si l’email Prestafacture échoue (ex. SMTP non configuré côté Prestafacture).
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

function prestafacture_lines_without_product_ids(array $lines): array
{
    $out = [];
    foreach ($lines as $line) {
        if (!is_array($line)) {
            continue;
        }
        unset($line['productId']);
        $out[] = $line;
    }

    return $out;
}

function prestafacture_is_missing_product_error(string $error): bool
{
    $error = mb_strtolower(trim($error));
    if ($error === '') {
        return false;
    }

    return str_contains($error, 'produit')
        && (str_contains($error, 'introuvable') || str_contains($error, 'not found') || str_contains($error, 'inexistant'));
}

/**
 *
 * @param list<array{description: string, quantity: int|float, unitPrice: float, taxRate?: float}> $lines
 * @return array{ok: bool, quote_id: string, error: string}
 */
function prestafacture_create_quote_devis(
    string $customerEmail,
    string $personName,
    array $lines,
    string $internalNote = '',
    string $companyName = ''
): array {
    $empty = ['ok' => false, 'quote_id' => '', 'error' => ''];
    $email = trim($customerEmail);
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $empty['error'] = 'Email client invalide.';
        return $empty;
    }

    $apiLines = [];
    foreach ($lines as $line) {
        if (!is_array($line)) {
            continue;
        }
        $desc = mb_substr(trim((string) ($line['description'] ?? '')), 0, 200);
        if ($desc === '') {
            continue;
        }
        $qty = $line['quantity'] ?? 1;
        $qty = is_numeric($qty) ? (float) $qty : 1.0;
        $unit = (float) ($line['unitPrice'] ?? 0);
        $tax = isset($line['taxRate']) ? (float) $line['taxRate'] : 0.2;
        if ($tax > 1) {
            $tax = prestafacture_tax_rate_decimal($tax);
        }
        $apiLine = [
            'description' => $desc,
            'quantity' => $qty,
            'unitPrice' => round($unit, 4),
            'taxRate' => $tax,
        ];
        if (isset($line['productId']) && is_numeric($line['productId']) && (int) $line['productId'] > 0) {
            $apiLine['productId'] = (int) $line['productId'];
        }
        $apiLines[] = $apiLine;
    }
    if ($apiLines === []) {
        $empty['error'] = 'Aucune ligne de devis.';
        return $empty;
    }

    $client = prestafacture_ensure_client_id($email, $personName, $companyName);
    if (!$client['ok']) {
        $empty['error'] = $client['error'];
        if (str_contains($client['error'], 'clients.read') || str_contains($client['error'], 'clients.write')) {
            error_log('[Prestafacture] Jeton API : ajouter clients.read et clients.write');
        }
        return $empty;
    }

    if (!empty($client['created'])) {
        error_log('[Prestafacture] client créé id=' . $client['client_id'] . ' email=' . $email);
    }

    // L’API /devis exige clientId (clientEmail seul renvoie « Client requis »).
    $body = [
        'clientId' => $client['client_id'],
        'lines' => $apiLines,
        'expiryDate' => gmdate('Y-m-d', strtotime('+30 days')),
    ];
    if ($internalNote !== '') {
        $body['notes'] = mb_substr($internalNote, 0, 2000);
    }

    $res = prestafacture_http('POST', '/devis', $body);
    if ((!$res['ok'] || !is_array($res['data'])) && prestafacture_is_missing_product_error((string) ($res['error'] ?? ''))) {
        $body['lines'] = prestafacture_lines_without_product_ids($apiLines);
        error_log('[Prestafacture] devis : productId invalide, nouvel essai sans lien produit');
        $res = prestafacture_http('POST', '/devis', $body);
    }
    if (!$res['ok'] || !is_array($res['data'])) {
        $empty['error'] = $res['error'] !== '' ? $res['error'] : 'Création devis impossible.';
        return $empty;
    }

    $id = prestafacture_extract_id($res['data'], 'id', 'devisId', 'quote_id', 'quoteId');
    if ($id === '') {
        $empty['error'] = 'Réponse Prestafacture sans id devis.';
        return $empty;
    }

    return ['ok' => true, 'quote_id' => $id, 'error' => ''];
}

/**
 * POST /public/devis/:id/send
 *
 * @return array{ok: bool, error: string, email_sent: bool}
 */
function prestafacture_send_devis_email(string $devisId, string $customerEmail): array
{
    $fail = ['ok' => false, 'error' => '', 'email_sent' => false];
    $devisId = trim($devisId);
    if ($devisId === '') {
        $fail['error'] = 'id devis invalide.';
        return $fail;
    }
    $email = trim($customerEmail);
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $fail['error'] = 'Email invalide.';
        return $fail;
    }

    $res = prestafacture_http('POST', '/devis/' . $devisId . '/send', [
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
 * Crée un devis Prestafacture puis l’envoie par e-mail au client.
 *
 * @param list<array{description: string, quantity: int|float, unitPrice: float, taxRate?: float}> $lines
 * @return array{ok: bool, quote_id: string, email_sent: bool, error: string, warning: string}
 */
function prestafacture_issue_quote_devis(
    string $customerEmail,
    string $personName,
    array $lines,
    string $internalNote = '',
    float $taxRatePercent = 20.0,
    string $companyName = ''
): array {
    $empty = ['ok' => false, 'quote_id' => '', 'email_sent' => false, 'error' => '', 'warning' => ''];
    if (!prestafacture_configured()) {
        $empty['error'] = 'Prestafacture non configuré.';
        return $empty;
    }

    $taxDecimal = prestafacture_tax_rate_decimal($taxRatePercent);
    $normalized = [];
    foreach ($lines as $line) {
        if (!is_array($line)) {
            continue;
        }
        $unit = (float) ($line['unitPrice'] ?? 0);
        if ($unit <= 0 && isset($line['priceTtc'])) {
            $unit = prestafacture_unit_price_ht((float) $line['priceTtc'], $taxRatePercent);
        }
        $normalizedLine = [
            'description' => (string) ($line['description'] ?? ''),
            'quantity' => $line['quantity'] ?? 1,
            'unitPrice' => $unit,
            'taxRate' => $taxDecimal,
        ];
        if (isset($line['productId']) && is_numeric($line['productId']) && (int) $line['productId'] > 0) {
            $normalizedLine['productId'] = (int) $line['productId'];
        }
        $normalized[] = $normalizedLine;
    }

    $quote = prestafacture_create_quote_devis($customerEmail, $personName, $normalized, $internalNote, $companyName);
    if (!$quote['ok']) {
        $empty['error'] = $quote['error'];
        return $empty;
    }

    $send = prestafacture_send_devis_email($quote['quote_id'], $customerEmail);
    if (!$send['ok']) {
        error_log('[Prestafacture] send devis ' . $quote['quote_id'] . ': ' . $send['error']);
        return [
            'ok' => true,
            'quote_id' => $quote['quote_id'],
            'email_sent' => false,
            'error' => '',
            'warning' => $send['error'],
        ];
    }

    return [
        'ok' => true,
        'quote_id' => $quote['quote_id'],
        'email_sent' => !empty($send['email_sent']),
        'error' => '',
        'warning' => '',
    ];
}
