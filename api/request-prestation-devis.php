<?php
/**
 * Demande de devis prestation : enregistrement + envoi e-mail via Facturio (devis).
 * POST multipart ou form-urlencoded.
 */

declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');

$origin = isset($_SERVER['HTTP_ORIGIN']) ? (string) $_SERVER['HTTP_ORIGIN'] : '';
if (preg_match('#^https?://(www\.)?danielcraft\.fr$#', $origin)) {
    header('Access-Control-Allow-Origin: ' . $origin);
} elseif ($origin !== '' && preg_match('#^https?://(127\.0\.0\.1|localhost)(:\d+)?$#i', $origin)) {
    header('Access-Control-Allow-Origin: ' . $origin);
}
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'error' => 'Méthode non autorisée'], JSON_UNESCAPED_UNICODE);
    exit;
}

require_once __DIR__ . '/prestations-common.php';
require_once __DIR__ . '/facturio-common.php';

function devis_clean(string $s, int $max = 500): string
{
    $s = trim(strip_tags($s));
    if (function_exists('mb_substr')) {
        return mb_substr($s, 0, $max, 'UTF-8');
    }
    return substr($s, 0, $max);
}

$name = devis_clean((string) ($_POST['name'] ?? ''), 120);
$email = trim((string) ($_POST['email'] ?? ''));
$phone = devis_clean((string) ($_POST['phone'] ?? ''), 40);
$company = devis_clean((string) ($_POST['company'] ?? ''), 120);
$message = devis_clean((string) ($_POST['message'] ?? ''), 4000);
$prestationSlug = devis_clean((string) ($_POST['prestation_slug'] ?? ''), 80);
$serviceSlug = devis_clean((string) ($_POST['service_slug'] ?? ''), 80);
$totalRaw = trim((string) ($_POST['total_eur'] ?? ''));
$totalEur = (int) preg_replace('/\D+/', '', $totalRaw);

$addonIds = $_POST['addon_id'] ?? [];
if (!is_array($addonIds)) {
    $addonIds = $addonIds !== '' ? [(string) $addonIds] : [];
}

if ($name === '' || strlen($name) < 2) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'Indiquez votre nom.'], JSON_UNESCAPED_UNICODE);
    exit;
}
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'Adresse e-mail invalide.'], JSON_UNESCAPED_UNICODE);
    exit;
}

$item = prestations_find_by_slug($prestationSlug);
if ($item === null && $serviceSlug !== '') {
    $item = prestations_find_by_service_slug($serviceSlug);
}
if ($item === null) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'Prestation introuvable.'], JSON_UNESCAPED_UNICODE);
    exit;
}

$title = (string) ($item['title'] ?? 'Prestation');
$basePrice = (int) ($item['price_eur'] ?? 0);
if ($totalEur <= 0) {
    $totalEur = $basePrice;
}

$lines = [];
$lines[] = [
    'description' => $title,
    'quantity' => 1,
    'unitPrice' => facturio_unit_price_ht((float) $basePrice, 20.0),
];

$addonsCatalog = is_array($item['addons'] ?? null) ? $item['addons'] : [];
$addonsById = [];
foreach ($addonsCatalog as $a) {
    if (is_array($a) && isset($a['id'])) {
        $addonsById[(string) $a['id']] = $a;
    }
}
foreach ($addonIds as $aid) {
    $aid = devis_clean((string) $aid, 64);
    if ($aid === '' || !isset($addonsById[$aid])) {
        continue;
    }
    $addon = $addonsById[$aid];
    $addonTitle = (string) ($addon['title'] ?? 'Option');
    $addonPrice = (int) ($addon['price_eur'] ?? 0);
    if ($addonPrice <= 0) {
        continue;
    }
    $lines[] = [
        'description' => $title . ' — ' . $addonTitle,
        'quantity' => 1,
        'unitPrice' => facturio_unit_price_ht((float) $addonPrice, 20.0),
    ];
}

$clientName = $company !== '' ? $company . ' — ' . $name : $name;
$noteParts = [];
if ($phone !== '') {
    $noteParts[] = 'Tél. : ' . $phone;
}
if ($message !== '') {
    $noteParts[] = $message;
}
$noteParts[] = 'Demande depuis danielcraft.fr/prestations/' . ($item['slug'] ?? $prestationSlug);
$internalNote = implode("\n", $noteParts);

facturio_bootstrap();
$quoteResult = facturio_issue_quote_devis(
    $email,
    $clientName,
    $lines,
    $internalNote,
    20.0
);

if (!$quoteResult['ok']) {
    error_log('[prestation-devis] Facturio: ' . ($quoteResult['error'] ?? 'erreur'));
    if (facturio_configured()) {
        http_response_code(502);
        echo json_encode([
            'success' => false,
            'error' => 'Le devis n’a pas pu être envoyé pour le moment. Écrivez à contact@danielcraft.fr.',
        ], JSON_UNESCAPED_UNICODE);
        exit;
    }
    // Local sans Facturio : succès simulé pour tests
    echo json_encode([
        'success' => true,
        'message' => 'Demande reçue (Facturio non configuré en local). En production, le devis part par e-mail.',
        'quote_id' => '',
    ], JSON_UNESCAPED_UNICODE);
    exit;
}

$msg = 'Merci ! Votre devis a été enregistré et envoyé à ' . $email . '.';
if (empty($quoteResult['email_sent'])) {
    $msg = 'Merci ! Votre devis est enregistré. Si vous ne le voyez pas, vérifiez les spams ou contactez-nous.';
}

echo json_encode([
    'success' => true,
    'message' => $msg,
    'quote_id' => $quoteResult['quote_id'] ?? '',
], JSON_UNESCAPED_UNICODE);
