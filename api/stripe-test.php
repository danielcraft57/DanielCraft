<?php
/**
 * Test de connexion Stripe (GET, usage admin / dev uniquement).
 * ?key=STRIPE_TEST_KEY si STRIPE_TEST_KEY est défini dans .env
 */

declare(strict_types=1);

require_once __DIR__ . '/stripe-common.php';

api_json_headers();

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'GET') {
    http_response_code(405);
    echo json_encode(['success' => false, 'error' => 'GET uniquement']);
    exit;
}

$expected = getenv('STRIPE_TEST_KEY') ?: '';
$provided = isset($_GET['key']) ? (string) $_GET['key'] : '';
if ($expected !== '' && !hash_equals($expected, $provided)) {
    http_response_code(403);
    echo json_encode(['success' => false, 'error' => 'Clé de test invalide.']);
    exit;
}

$pk = stripe_publishable_key();
$sk = stripe_secret_key();
if ($sk === '') {
    http_response_code(500);
    echo json_encode([
        'success' => false,
        'error' => 'STRIPE_SECRET_KEY absente du .env',
        'publishable_configured' => $pk !== '',
    ]);
    exit;
}

$res = stripe_api('GET', '/balance');
if (!$res['ok']) {
    http_response_code(502);
    echo json_encode([
        'success' => false,
        'error' => $res['error'],
        'publishable_prefix' => $pk !== '' ? substr($pk, 0, 12) . '…' : '',
        'secret_prefix' => substr($sk, 0, 12) . '…',
    ]);
    exit;
}

$livemode = isset($res['data']['livemode']) ? (bool) $res['data']['livemode'] : null;

echo json_encode([
    'success' => true,
    'livemode' => $livemode,
    'publishable_configured' => $pk !== '',
    'site_base' => api_site_base(),
    'message' => 'Connexion Stripe OK.',
]);
