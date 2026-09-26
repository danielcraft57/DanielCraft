<?php
/**
 * Émission de devis Prestafacture (Prestafacture) - modale prestation, wizard contact, vitrine.
 */
declare(strict_types=1);

require_once __DIR__ . '/prestations-common.php';
require_once __DIR__ . '/prestafacture-common.php';
require_once __DIR__ . '/devis-notification.php';

function devis_clean_field(string $s, int $max = 500): string
{
    $s = trim(strip_tags($s));
    if (function_exists('mb_substr')) {
        return mb_substr($s, 0, $max, 'UTF-8');
    }
    return substr($s, 0, $max);
}

/** @return list<string> */
function devis_email_only_services(): array
{
    return [
        'besoin_a_preciser',
        'projet_sur_mesure',
        'audit_gratuit_site',
        'audit_paid_complet_ia',
    ];
}

function devis_is_vitrine_service(string $service): bool
{
    return in_array($service, ['vitrine_catalog_order', 'vitrine_catalog_devis'], true);
}

function devis_should_issue_quote(string $service, string $prestationSlug = ''): bool
{
    $service = trim($service);
    if ($service !== '' && in_array($service, devis_email_only_services(), true)) {
        return false;
    }
    if ($service !== '' && devis_is_vitrine_service($service)) {
        return true;
    }
    if ($service !== '' && prestations_find_by_service_slug($service) !== null) {
        return true;
    }
    if ($prestationSlug !== '' && prestations_find_by_slug($prestationSlug) !== null) {
        return true;
    }

    return false;
}

/** Taux TVA devis prestations (micro-entreprise : non assujetti). */
function devis_tax_rate_percent(): float
{
    return 0.0;
}

/**
 * Lignes explicites catalogue (`quote_lines`) : temps, VPS, mail offert, etc.
 *
 * @return array{lines: list<array<string, mixed>>, title: string, total_ht: int, item: array<string, mixed>}|null
 */
function devis_build_from_quote_lines(array $item): ?array
{
    $raw = $item['quote_lines'] ?? null;
    if (!is_array($raw) || $raw === []) {
        return null;
    }

    $title = (string) ($item['title'] ?? 'Prestation');
    $lines = [];
    $totalHt = 0;
    $tax = devis_tax_rate_percent();

    foreach ($raw as $row) {
        if (!is_array($row)) {
            continue;
        }
        $label = trim((string) ($row['label'] ?? ''));
        if ($label === '') {
            continue;
        }
        $qty = (float) ($row['quantity'] ?? 1);
        if ($qty <= 0) {
            $qty = 1.0;
        }
        $unit = (float) ($row['amount_eur'] ?? 0);
        $includeZero = !empty($row['include_zero']);
        if ($unit < 0) {
            continue;
        }
        if ($unit == 0.0 && !$includeZero) {
            continue;
        }

        $productId = null;
        $lineSlug = trim((string) ($row['slug'] ?? ''));
        if ($lineSlug !== '') {
            $cat = prestations_find_by_slug($lineSlug);
            if ($cat !== null) {
                $productId = prestafacture_product_id_from_catalog($cat);
            }
        }

        $lines[] = prestafacture_line_from_price_ht(
            mb_substr($label, 0, 160),
            $unit,
            $tax,
            $productId,
            $qty
        );
        $totalHt += (int) round($unit * $qty);
    }

    if ($lines === []) {
        return null;
    }

    return [
        'lines' => $lines,
        'title' => $title,
        'total_ht' => $totalHt,
        'item' => $item,
    ];
}

/**
 * @param list<string|int> $addonIds
 * @return array{lines: list<array<string, mixed>>, title: string, total_ht: int, item: array<string, mixed>}|null
 */
function devis_build_catalog_quote(string $serviceSlug, array $addonIds = [], string $prestationSlug = ''): ?array
{
    $item = null;
    if ($prestationSlug !== '') {
        $item = prestations_find_by_slug($prestationSlug);
    }
    if ($item === null) {
        $item = prestations_find_by_service_slug($serviceSlug);
    }
    if ($item === null) {
        return null;
    }

    $fromLines = devis_build_from_quote_lines($item);
    if ($fromLines !== null) {
        // Options addons encore possibles par-dessus un devis déjà découpé.
        $addonsCatalog = is_array($item['addons'] ?? null) ? $item['addons'] : [];
        $addonsById = [];
        foreach ($addonsCatalog as $a) {
            if (is_array($a) && isset($a['id'])) {
                $addonsById[(string) $a['id']] = $a;
            }
        }
        $tax = devis_tax_rate_percent();
        foreach ($addonIds as $aid) {
            $aid = devis_clean_field((string) $aid, 64);
            if ($aid === '' || !isset($addonsById[$aid])) {
                continue;
            }
            $addon = $addonsById[$aid];
            $addonTitle = (string) ($addon['title'] ?? 'Option');
            $addonPrice = (int) ($addon['price_eur'] ?? 0);
            if ($addonPrice <= 0) {
                continue;
            }
            $fromLines['lines'][] = prestafacture_line_from_price_ht(
                prestafacture_prestation_line_label($item, $addonTitle),
                (float) $addonPrice,
                $tax,
                prestafacture_product_id_from_catalog($addon)
            );
            $fromLines['total_ht'] += $addonPrice;
        }

        return $fromLines;
    }

    $title = (string) ($item['title'] ?? 'Prestation');
    $tax = devis_tax_rate_percent();
    $expandIncludes = !empty($item['quote_expand_includes'])
        && is_array($item['includes_slugs'] ?? null)
        && ($item['includes_slugs'] ?? []) !== [];

    // Pack « détail année 1 » : une ligne par prestation incluse (mensuel × 12).
    if ($expandIncludes) {
        $lines = [];
        $totalHt = 0;
        $mainSlug = trim((string) ($item['slug'] ?? ''));
        $seen = [];
        foreach ($item['includes_slugs'] as $incSlug) {
            $incSlug = trim((string) $incSlug);
            if ($incSlug === '' || $incSlug === $mainSlug || isset($seen[$incSlug])) {
                continue;
            }
            $extra = prestations_find_by_slug($incSlug);
            if ($extra === null) {
                continue;
            }
            $unit = (int) ($extra['price_eur'] ?? 0);
            $includeZero = $unit === 0 && str_contains(
                function_exists('mb_strtolower')
                    ? mb_strtolower((string) ($extra['price_label'] ?? ''), 'UTF-8')
                    : strtolower((string) ($extra['price_label'] ?? '')),
                'offert'
            );
            if ($unit < 0 || ($unit === 0 && !$includeZero)) {
                continue;
            }
            $qty = devis_item_is_monthly($extra) ? 12 : 1;
            $seen[$incSlug] = true;
            $lines[] = prestafacture_line_from_price_ht(
                devis_year1_line_label($extra),
                (float) $unit,
                $tax,
                prestafacture_product_id_from_catalog($extra),
                (float) $qty
            );
            $totalHt += $unit * $qty;
        }
        if ($lines === []) {
            return null;
        }

        return [
            'lines' => $lines,
            'title' => $title,
            'total_ht' => $totalHt,
            'item' => $item,
        ];
    }

    $basePrice = (int) ($item['price_eur'] ?? 0);
    $lines = [];
    $mainProductId = prestafacture_product_id_from_catalog($item);
    $lines[] = prestafacture_line_from_price_ht(
        prestafacture_prestation_line_label($item),
        (float) $basePrice,
        $tax,
        $mainProductId
    );

    $totalHt = $basePrice;
    $addonsCatalog = is_array($item['addons'] ?? null) ? $item['addons'] : [];
    $addonsById = [];
    foreach ($addonsCatalog as $a) {
        if (is_array($a) && isset($a['id'])) {
            $addonsById[(string) $a['id']] = $a;
        }
    }
    $skipSkus = [];
    foreach ($addonIds as $aid) {
        $aid = devis_clean_field((string) $aid, 64);
        if ($aid === '' || !isset($addonsById[$aid])) {
            continue;
        }
        $addon = $addonsById[$aid];
        $addonTitle = (string) ($addon['title'] ?? 'Option');
        $addonPrice = (int) ($addon['price_eur'] ?? 0);
        if ($addonPrice <= 0) {
            continue;
        }
        $addonSku = strtoupper(trim((string) ($addon['prestafacture_sku'] ?? '')));
        if ($addonSku !== '') {
            $skipSkus[$addonSku] = true;
        }
        $addonProductId = prestafacture_product_id_from_catalog($addon);
        $lines[] = prestafacture_line_from_price_ht(
            prestafacture_prestation_line_label($item, $addonTitle),
            (float) $addonPrice,
            $tax,
            $addonProductId
        );
        $totalHt += $addonPrice;
    }

    foreach (devis_year1_entries($item) as $extraRow) {
        $extra = $extraRow['item'];
        $sku = strtoupper(trim((string) ($extra['prestafacture_sku'] ?? '')));
        if ($sku !== '' && isset($skipSkus[$sku])) {
            continue;
        }
        $qty = (int) $extraRow['quantity'];
        $unit = (int) ($extra['price_eur'] ?? 0);
        $lines[] = prestafacture_line_from_price_ht(
            devis_year1_line_label($extra),
            (float) $unit,
            $tax,
            prestafacture_product_id_from_catalog($extra),
            (float) $qty
        );
        $totalHt += $unit * $qty;
    }

    return [
        'lines' => $lines,
        'title' => $title,
        'total_ht' => $totalHt,
        'item' => $item,
    ];
}

function devis_item_is_monthly(array $item): bool
{
    $label = function_exists('mb_strtolower')
        ? mb_strtolower(trim((string) ($item['price_label'] ?? '')), 'UTF-8')
        : strtolower(trim((string) ($item['price_label'] ?? '')));

    return $label === 'mensuel' || str_contains($label, 'mois');
}

function devis_year1_line_label(array $item): string
{
    $title = trim(preg_replace('/[\r\n]+/', ' ', (string) ($item['title'] ?? 'Prestation')));
    if (devis_item_is_monthly($item)) {
        return mb_substr($title . ' - 12 mois', 0, 160);
    }
    $period = trim((string) ($item['price_label'] ?? ''));
    if ($period !== '') {
        return mb_substr($title . ' - ' . $period, 0, 160);
    }

    return mb_substr($title, 0, 160);
}

/**
 * Frais fixes + abonnements année 1 attachés à une prestation (catalogue).
 *
 * @return list<array{item: array<string, mixed>, quantity: int, amount_ht: int}>
 */
function devis_year1_entries(array $item): array
{
    $slugs = $item['quote_year1_slugs'] ?? [];
    if (!is_array($slugs) || $slugs === []) {
        return [];
    }
    $mainSlug = trim((string) ($item['slug'] ?? ''));
    $out = [];
    $seen = [];
    foreach ($slugs as $slug) {
        $slug = trim((string) $slug);
        if ($slug === '' || $slug === $mainSlug || isset($seen[$slug])) {
            continue;
        }
        $extra = prestations_find_by_slug($slug);
        if ($extra === null) {
            continue;
        }
        $unit = (int) ($extra['price_eur'] ?? 0);
        if ($unit <= 0) {
            continue;
        }
        $qty = devis_item_is_monthly($extra) ? 12 : 1;
        $seen[$slug] = true;
        $out[] = [
            'item' => $extra,
            'quantity' => $qty,
            'amount_ht' => $unit * $qty,
        ];
    }

    return $out;
}

/**
 * @return array{lines: list<array<string, mixed>>, title: string, total_ht: int}
 */
function devis_build_vitrine_quote(string $service, string $vitrineTitle, string $vitrineSlug, int $priceHt): array
{
    $ref = $vitrineTitle !== '' ? $vitrineTitle : $vitrineSlug;
    if ($service === 'vitrine_catalog_devis') {
        $label = 'Devis modèle catalogue - ' . $ref;
    } else {
        $label = 'Modèle site vitrine - ' . $ref;
    }
    if ($priceHt <= 0) {
        $priceHt = 42;
    }

    return [
        'lines' => [
            prestafacture_line_from_price_ht($label, (float) $priceHt, devis_tax_rate_percent(), null),
        ],
        'title' => $label,
        'total_ht' => $priceHt,
    ];
}

/**
 * @param array<string, string> $data
 */
function devis_build_internal_note(array $data, string $sourcePath): string
{
    $parts = [];
    if (($data['company'] ?? '') !== '') {
        $parts[] = 'Contact : ' . $data['name'];
    }
    if (($data['phone'] ?? '') !== '') {
        $parts[] = 'Tél. : ' . $data['phone'];
    }
    if (($data['project_type'] ?? '') !== '') {
        $parts[] = 'Besoin : ' . contact_project_type_label($data['project_type'])
            . ' (' . $data['project_type'] . ')';
    }
    if (($data['preferred_date'] ?? '') !== '') {
        $parts[] = 'Date proposée : ' . $data['preferred_date'];
    }
    if (($data['preferred_time'] ?? '') !== '') {
        $parts[] = 'Créneau : ' . $data['preferred_time'];
    }
    if (($data['vitrine_slug'] ?? '') !== '') {
        $parts[] = 'Modèle (slug) : ' . $data['vitrine_slug'];
    }
    if (($data['vitrine_title'] ?? '') !== '') {
        $parts[] = 'Modèle : ' . $data['vitrine_title'];
    }
    if (($data['site_url'] ?? '') !== '') {
        $parts[] = 'URL site : ' . $data['site_url'];
    }
    if (($data['billing_address'] ?? '') !== '') {
        $parts[] = "Adresse facturation :\n" . $data['billing_address'];
    }
    if (($data['message'] ?? '') !== '') {
        $parts[] = $data['message'];
    }
    $parts[] = 'Demande depuis danielcraft.fr' . $sourcePath;

    return implode("\n", $parts);
}

/**
 * @param array<string, mixed> $input
 * @return array{
 *   ok: bool,
 *   http_status: int,
 *   payload: array<string, mixed>,
 *   admin_note: string
 * }
 */
function devis_issue_from_input(array $input): array
{
    require_once __DIR__ . '/contact-common.php';

    $name = devis_clean_field((string) ($input['name'] ?? ''), 120);
    $email = trim((string) ($input['email'] ?? ''));
    $phone = devis_clean_field((string) ($input['phone'] ?? ''), 40);
    $company = devis_clean_field((string) ($input['company'] ?? ''), 120);
    $message = devis_clean_field((string) ($input['message'] ?? ''), 4000);

    $serviceSlug = devis_clean_field((string) ($input['service_slug'] ?? $input['service'] ?? ''), 80);
    $prestationSlug = devis_clean_field((string) ($input['prestation_slug'] ?? ''), 80);
    $sourcePath = devis_clean_field((string) ($input['source_path'] ?? '/nos-offres'), 120);

    $vitrineSlug = devis_clean_field((string) ($input['vitrine_slug'] ?? ''), 80);
    $vitrineTitle = devis_clean_field((string) ($input['vitrine_title'] ?? ''), 220);
    $budgetRaw = trim((string) ($input['budget'] ?? $input['total_eur'] ?? ''));
    $budgetHt = (int) preg_replace('/\D+/', '', $budgetRaw);

    $addonIds = $input['addon_id'] ?? $input['addon_ids'] ?? [];
    if (!is_array($addonIds)) {
        $addonIds = $addonIds !== '' ? [(string) $addonIds] : [];
    }

    $contextData = [
        'name' => $name,
        'phone' => $phone,
        'company' => $company,
        'message' => $message,
        'project_type' => devis_clean_field((string) ($input['project_type'] ?? ''), 40),
        'preferred_date' => devis_clean_field((string) ($input['preferred_date'] ?? ''), 16),
        'preferred_time' => devis_clean_field((string) ($input['preferred_time'] ?? ''), 48),
        'vitrine_slug' => $vitrineSlug,
        'vitrine_title' => $vitrineTitle,
        'site_url' => devis_clean_field((string) ($input['site_url'] ?? ''), 500),
        'billing_address' => devis_clean_field((string) ($input['billing_address'] ?? ''), 1500),
    ];

    if ($name === '' || strlen($name) < 2) {
        return devis_error_response(400, 'Indiquez votre nom.');
    }
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        return devis_error_response(400, 'Adresse e-mail invalide.');
    }
    if (!devis_should_issue_quote($serviceSlug, $prestationSlug)) {
        return devis_error_response(400, 'Prestation sans devis automatique.');
    }

    if (devis_is_vitrine_service($serviceSlug)) {
        $built = devis_build_vitrine_quote($serviceSlug, $vitrineTitle, $vitrineSlug, $budgetHt);
        $sourcePath = '/echantillons/' . ($vitrineSlug !== '' ? $vitrineSlug . '/' : '');
    } else {
        $built = devis_build_catalog_quote($serviceSlug, $addonIds, $prestationSlug);
        if ($built === null) {
            return devis_error_response(400, 'Prestation introuvable.');
        }
    }

    $lines = $built['lines'];
    $title = $built['title'];
    $totalHt = $built['total_ht'];
    $internalNote = devis_build_internal_note($contextData, $sourcePath);
    $clientDisplayName = prestafacture_client_display_name($name, $company);

    prestafacture_bootstrap();
    $quoteResult = prestafacture_issue_quote_devis(
        $email,
        $name,
        $lines,
        $internalNote,
        devis_tax_rate_percent(),
        $company
    );

    if (!$quoteResult['ok']) {
        $prestafactureErr = (string) ($quoteResult['error'] ?? 'erreur');
        error_log('[devis-common] Prestafacture: ' . $prestafactureErr);

        if (prestafacture_configured()) {
            $fallback = devis_notify_fallback(
                $email,
                $clientDisplayName,
                $title,
                $totalHt,
                $lines,
                $internalNote
            );
            if ($fallback['ok']) {
                $msg = $fallback['client_sent']
                    ? 'Merci ! Votre demande est enregistrée. Vous recevrez votre devis PDF sous 24 h ouvrées à ' . $email . '.'
                    : 'Merci ! Votre demande est enregistrée. Le devis vous sera envoyé sous 24 h ouvrées à ' . $email . '.';

                return [
                    'ok' => true,
                    'http_status' => 200,
                    'payload' => [
                        'success' => true,
                        'devis_issued' => true,
                        'fallback' => true,
                        'message' => $msg,
                        'quote_id' => '',
                    ],
                    'admin_note' => 'Devis en attente (fallback e-mail Prestafacture indisponible).',
                ];
            }

            $userError = 'Le devis automatique est momentanément indisponible. Écrivez à contact@danielcraft.fr ou réessayez plus tard.';
            if (
                str_contains($prestafactureErr, 'clients.read')
                || str_contains($prestafactureErr, 'clients.write')
                || str_contains($prestafactureErr, 'devis.write')
                || str_contains($prestafactureErr, 'devis.send')
            ) {
                error_log('[devis-common] Jeton Prestafacture : clients.read, clients.write, devis.read, devis.write, devis.send');
            }

            return devis_error_response(502, $userError, 'prestafacture_unavailable');
        }

        return [
            'ok' => true,
            'http_status' => 200,
            'payload' => [
                'success' => true,
                'devis_issued' => true,
                'message' => 'Demande reçue (Prestafacture non configuré en local). En production, le devis part par e-mail.',
                'quote_id' => '',
            ],
            'admin_note' => 'Devis simulé (Prestafacture non configuré).',
        ];
    }

    $msg = 'Merci ! Votre devis a été enregistré et envoyé à ' . $email . '.';
    if (empty($quoteResult['email_sent'])) {
        $msg = 'Merci ! Votre devis est enregistré. Si vous ne le voyez pas, vérifiez les spams ou contactez-nous.';
    }

    $quoteId = (string) ($quoteResult['quote_id'] ?? '');
    $adminNote = $quoteId !== ''
        ? 'Devis Prestafacture #' . $quoteId . ' émis et envoyé au client.'
        : 'Devis Prestafacture émis (identifiant non retourné).';

    return [
        'ok' => true,
        'http_status' => 200,
        'payload' => [
            'success' => true,
            'devis_issued' => true,
            'message' => $msg,
            'quote_id' => $quoteId,
        ],
        'admin_note' => $adminNote,
    ];
}

/**
 * @return array{ok: bool, http_status: int, payload: array<string, mixed>, admin_note: string}
 */
function devis_error_response(int $status, string $error, string $code = ''): array
{
    $payload = ['success' => false, 'error' => $error];
    if ($code !== '') {
        $payload['error_code'] = $code;
    }

    return [
        'ok' => false,
        'http_status' => $status,
        'payload' => $payload,
        'admin_note' => '',
    ];
}

/**
 * Wizard contact / vitrine : tente l'émission Prestafacture si le service le permet.
 *
 * @param array<string, string> $contactData
 * @return array{
 *   mode: 'skip'|'issued'|'failed',
 *   quote_id?: string,
 *   fallback?: bool,
 *   message?: string,
 *   error?: string,
 *   error_code?: string,
 *   admin_note?: string
 * }
 */
function devis_try_issue_for_contact(array $contactData): array
{
    $service = (string) ($contactData['service'] ?? '');
    if (!devis_should_issue_quote($service)) {
        return ['mode' => 'skip'];
    }

    $input = array_merge($contactData, [
        'service_slug' => $service,
        'source_path' => devis_is_vitrine_service($service) ? '/echantillons/' : '/contact',
    ]);

    $result = devis_issue_from_input($input);
    if (!$result['ok']) {
        return [
            'mode' => 'failed',
            'error' => (string) ($result['payload']['error'] ?? 'Erreur devis'),
            'error_code' => (string) ($result['payload']['error_code'] ?? ''),
        ];
    }

    $payload = $result['payload'];

    return [
        'mode' => 'issued',
        'quote_id' => (string) ($payload['quote_id'] ?? ''),
        'fallback' => !empty($payload['fallback']),
        'message' => (string) ($payload['message'] ?? ''),
        'admin_note' => (string) ($result['admin_note'] ?? ''),
    ];
}

/**
 * Réponse JSON standard pour les endpoints devis.
 *
 * @param array<string, mixed> $payload
 */
function devis_emit_json(int $httpStatus, array $payload): void
{
    http_response_code($httpStatus);
    echo json_encode($payload, JSON_UNESCAPED_UNICODE);
}
