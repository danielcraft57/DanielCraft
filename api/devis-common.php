<?php
/**
 * Émission de devis Prestafacture (Prestafacture) — modale prestation, wizard contact, vitrine.
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

    $title = (string) ($item['title'] ?? 'Prestation');
    $basePrice = (int) ($item['price_eur'] ?? 0);
    $lines = [];
    $mainProductId = prestafacture_product_id_from_catalog($item);
    $lines[] = prestafacture_line_from_price_ht(
        prestafacture_prestation_line_label($item),
        (float) $basePrice,
        20.0,
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
        $addonProductId = prestafacture_product_id_from_catalog($addon);
        $lines[] = prestafacture_line_from_price_ht(
            prestafacture_prestation_line_label($item, $addonTitle),
            (float) $addonPrice,
            20.0,
            $addonProductId
        );
        $totalHt += $addonPrice;
    }

    return [
        'lines' => $lines,
        'title' => $title,
        'total_ht' => $totalHt,
        'item' => $item,
    ];
}

/**
 * @return array{lines: list<array<string, mixed>>, title: string, total_ht: int}
 */
function devis_build_vitrine_quote(string $service, string $vitrineTitle, string $vitrineSlug, int $priceHt): array
{
    $ref = $vitrineTitle !== '' ? $vitrineTitle : $vitrineSlug;
    if ($service === 'vitrine_catalog_devis') {
        $label = 'Devis modèle catalogue — ' . $ref;
    } else {
        $label = 'Modèle site vitrine — ' . $ref;
    }
    if ($priceHt <= 0) {
        $priceHt = 42;
    }

    return [
        'lines' => [
            prestafacture_line_from_price_ht($label, (float) $priceHt, 20.0, null),
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
        20.0,
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
 * Wizard contact / vitrine : tente l’émission Prestafacture si le service le permet.
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
