<?php
/**
 * Demande de devis prestation : enregistrement + envoi e-mail via Prestafacture (devis).
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

require_once __DIR__ . '/devis-common.php';

$prestationSlug = devis_clean_field((string) ($_POST['prestation_slug'] ?? ''), 80);
$serviceSlug = devis_clean_field((string) ($_POST['service_slug'] ?? ''), 80);

$sourcePath = '/prestations/';
if ($prestationSlug !== '') {
    $sourcePath .= $prestationSlug . '/';
}

$addonIds = $_POST['addon_id'] ?? [];
if (!is_array($addonIds)) {
    $addonIds = $addonIds !== '' ? [(string) $addonIds] : [];
}

$result = devis_issue_from_input([
    'name' => (string) ($_POST['name'] ?? ''),
    'email' => (string) ($_POST['email'] ?? ''),
    'phone' => (string) ($_POST['phone'] ?? ''),
    'company' => (string) ($_POST['company'] ?? ''),
    'message' => (string) ($_POST['message'] ?? ''),
    'prestation_slug' => $prestationSlug,
    'service_slug' => $serviceSlug !== '' ? $serviceSlug : $prestationSlug,
    'addon_ids' => $addonIds,
    'source_path' => $sourcePath,
]);

devis_emit_json($result['http_status'], $result['payload']);
