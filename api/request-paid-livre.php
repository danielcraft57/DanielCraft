<?php
/**
 * Livre PDF apres paiement Stripe — facture Prestafacture + lien de telechargement par e-mail.
 *
 * POST JSON : stripe_session_id (requis), email (optionnel), company (honeypot)
 */

declare(strict_types=1);

require_once __DIR__ . '/stripe-livre-fulfillment.php';

prestafacture_bootstrap();
api_json_headers();

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'error' => 'Methode non autorisee'], JSON_UNESCAPED_UNICODE);
    exit;
}

$sessionId = '';
$email = '';
$honeypot = '';

$contentType = isset($_SERVER['CONTENT_TYPE']) ? strtolower((string) $_SERVER['CONTENT_TYPE']) : '';
if (str_contains($contentType, 'application/json')) {
    $raw = file_get_contents('php://input');
    $decoded = json_decode($raw ?: '', true);
    if (is_array($decoded)) {
        $sessionId = isset($decoded['stripe_session_id']) ? trim((string) $decoded['stripe_session_id']) : '';
        if ($sessionId === '' && isset($decoded['session_id'])) {
            $sessionId = trim((string) $decoded['session_id']);
        }
        $email = isset($decoded['email']) ? trim((string) $decoded['email']) : '';
        $honeypot = isset($decoded['company']) ? (string) $decoded['company'] : '';
    }
} else {
    $sessionId = isset($_POST['stripe_session_id']) ? trim((string) $_POST['stripe_session_id']) : '';
    $email = isset($_POST['email']) ? trim((string) $_POST['email']) : '';
    $honeypot = isset($_POST['company']) ? (string) $_POST['company'] : '';
}

$honeypot = trim(strip_tags($honeypot));

if ($honeypot !== '') {
    echo json_encode(['success' => true, 'message' => 'Commande en cours de traitement.'], JSON_UNESCAPED_UNICODE);
    exit;
}

if ($sessionId === '') {
    http_response_code(400);
    echo json_encode([
        'success' => false,
        'error' => 'Session de paiement manquante. Rechargez la page apres le paiement Stripe.',
    ], JSON_UNESCAPED_UNICODE);
    exit;
}

set_time_limit(120);

try {
    $fulfill = stripe_fulfill_livre_checkout_session($sessionId, ['email' => $email]);
} catch (Throwable $e) {
    error_log('[request-paid-livre] ' . $e->getMessage());
    http_response_code(502);
    echo json_encode([
        'success' => false,
        'error' => 'Erreur serveur lors de la finalisation. Reessayez ou contactez le support.',
    ], JSON_UNESCAPED_UNICODE);
    exit;
}

if (!$fulfill['ok']) {
    $status = 502;
    if (str_contains($fulfill['error'], 'non confirme') || str_contains($fulfill['error'], 'invalide')) {
        $status = 400;
    }
    http_response_code($status);
    echo json_encode([
        'success' => false,
        'error' => $fulfill['error'] !== '' ? $fulfill['error'] : 'Impossible de finaliser la commande.',
        'invoice_ok' => !empty($fulfill['invoice_ok']),
        'delivery_ok' => !empty($fulfill['delivery_ok']),
    ], JSON_UNESCAPED_UNICODE);
    exit;
}

$message = 'Merci ! Facture envoyee par e-mail — voici ta page de telechargement.';
if ($fulfill['invoice_ok'] && $fulfill['delivery_ok']) {
    $message = 'Merci ! Facture par e-mail + page de telechargement prete (code unique inclus dans le mail).';
} elseif ($fulfill['delivery_ok'] && !$fulfill['invoice_ok']) {
    $message = 'Page de telechargement prete. La facture suivra des qu\'elle sera disponible.';
} elseif ($fulfill['invoice_ok'] && !$fulfill['delivery_ok']) {
    $message = 'Facture envoyee. Le PDF n\'a pas pu etre livre : contact@danielcraft.fr avec votre e-mail.';
}

echo json_encode([
    'success' => true,
    'invoice_ok' => $fulfill['invoice_ok'],
    'delivery_ok' => $fulfill['delivery_ok'],
    'download_url' => $fulfill['download_url'] ?? '',
    'code' => $fulfill['code'] ?? '',
    'message' => $message,
], JSON_UNESCAPED_UNICODE);
