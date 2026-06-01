<?php
/**
 * Crée une session Stripe Checkout pour l'audit complet IA (POST JSON).
 * Corps : audit_slug (requis), email, site_url, name (optionnels).
 */

declare(strict_types=1);

require_once __DIR__ . '/stripe-audit-common.php';

api_json_headers();

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'error' => 'Méthode non autorisée']);
    exit;
}

$slug = '';
$email = '';
$siteUrl = '';
$name = '';

$contentType = isset($_SERVER['CONTENT_TYPE']) ? strtolower((string) $_SERVER['CONTENT_TYPE']) : '';
if (str_contains($contentType, 'application/json')) {
    $raw = file_get_contents('php://input');
    $json = is_string($raw) ? json_decode($raw, true) : null;
    if (is_array($json)) {
        $slug = trim((string) ($json['audit_slug'] ?? ''));
        $email = trim((string) ($json['email'] ?? ''));
        $siteUrl = trim((string) ($json['site_url'] ?? ''));
        $name = trim((string) ($json['name'] ?? ''));
    }
} else {
    $slug = isset($_POST['audit_slug']) ? trim((string) $_POST['audit_slug']) : '';
    $email = isset($_POST['email']) ? trim((string) $_POST['email']) : '';
    $siteUrl = isset($_POST['site_url']) ? trim((string) $_POST['site_url']) : '';
    $name = isset($_POST['name']) ? trim((string) $_POST['name']) : '';
}

if ($slug === '') {
    $slug = 'audit-complet-ia';
}

if ($siteUrl !== '') {
    if (!preg_match('#^https?://#i', $siteUrl)) {
        $siteUrl = 'https://' . ltrim($siteUrl, '/');
    }
    if (!filter_var($siteUrl, FILTER_VALIDATE_URL)) {
        http_response_code(400);
        echo json_encode(['success' => false, 'error' => 'URL du site invalide.']);
        exit;
    }
}

$item = stripe_find_audit_item($slug);
if ($item === null) {
    http_response_code(404);
    echo json_encode(['success' => false, 'error' => 'Offre audit introuvable.']);
    exit;
}

$staticLink = trim((string) ($item['stripe_payment_link_url'] ?? ''));
if ($staticLink !== '' && filter_var($staticLink, FILTER_VALIDATE_URL)) {
    echo json_encode([
        'success' => true,
        'url' => $staticLink,
        'source' => 'payment_link',
    ]);
    exit;
}

$result = stripe_create_audit_checkout_session($slug, $email, $siteUrl, $name);
if (!$result['ok']) {
    http_response_code(502);
    echo json_encode(['success' => false, 'error' => $result['error']]);
    exit;
}

echo json_encode([
    'success' => true,
    'url' => $result['url'],
    'session_id' => $result['session_id'],
    'source' => 'checkout_session',
]);
