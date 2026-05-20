<?php
/**
 * Crée une session Stripe Checkout pour une fiche vitrine (POST JSON ou form).
 * Corps : vitrine_slug (requis), email (optionnel).
 */

declare(strict_types=1);

require_once __DIR__ . '/stripe-common.php';

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

$contentType = isset($_SERVER['CONTENT_TYPE']) ? strtolower((string) $_SERVER['CONTENT_TYPE']) : '';
if (str_contains($contentType, 'application/json')) {
    $raw = file_get_contents('php://input');
    $json = is_string($raw) ? json_decode($raw, true) : null;
    if (is_array($json)) {
        $slug = trim((string) ($json['vitrine_slug'] ?? ''));
        $email = trim((string) ($json['email'] ?? ''));
    }
} else {
    $slug = isset($_POST['vitrine_slug']) ? trim((string) $_POST['vitrine_slug']) : '';
    $email = isset($_POST['email']) ? trim((string) $_POST['email']) : '';
}

if ($slug === '') {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'vitrine_slug obligatoire.']);
    exit;
}

$item = stripe_find_vitrine_item($slug);
if ($item === null) {
    http_response_code(404);
    echo json_encode(['success' => false, 'error' => 'Modèle introuvable.']);
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

$result = stripe_create_checkout_session($slug, $email);
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
