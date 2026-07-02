<?php
/**
 * Audit premium après paiement Stripe — vérifie la session, facture Facturio, lance l’audit complet.
 *
 * POST JSON : website, email, stripe_session_id (requis), company (honeypot)
 */

declare(strict_types=1);

require_once __DIR__ . '/stripe-audit-fulfillment.php';

pl_bootstrap();
facturio_bootstrap();
api_json_headers();

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    pl_json_error(405, 'Méthode non autorisée');
}

$contentType = isset($_SERVER['CONTENT_TYPE']) ? strtolower((string) $_SERVER['CONTENT_TYPE']) : '';
$website = '';
$email = '';
$sessionId = '';
$honeypot = '';

if (str_contains($contentType, 'application/json')) {
    $raw = file_get_contents('php://input');
    $decoded = json_decode($raw ?: '', true);
    if (is_array($decoded)) {
        $website = isset($decoded['website']) ? (string) $decoded['website'] : '';
        $email = isset($decoded['email']) ? (string) $decoded['email'] : '';
        $sessionId = isset($decoded['stripe_session_id']) ? trim((string) $decoded['stripe_session_id']) : '';
        if ($sessionId === '' && isset($decoded['session_id'])) {
            $sessionId = trim((string) $decoded['session_id']);
        }
        $honeypot = isset($decoded['company']) ? (string) $decoded['company'] : '';
    }
} else {
    $website = isset($_POST['website']) ? (string) $_POST['website'] : '';
    if ($website === '' && isset($_POST['site_url'])) {
        $website = (string) $_POST['site_url'];
    }
    $email = isset($_POST['email']) ? (string) $_POST['email'] : '';
    $sessionId = isset($_POST['stripe_session_id']) ? trim((string) $_POST['stripe_session_id']) : '';
    $honeypot = isset($_POST['company']) ? (string) $_POST['company'] : '';
}

$website = pl_normalize_website(trim(strip_tags($website)));
$email = trim((string) $email);
$honeypot = trim(strip_tags($honeypot));

if ($honeypot !== '') {
    echo json_encode(['success' => true, 'message' => 'Commande en cours de traitement.'], JSON_UNESCAPED_UNICODE);
    exit;
}

if ($sessionId === '') {
    pl_json_error(400, 'Session de paiement manquante. Rechargez la page après le paiement Stripe.');
}

set_time_limit(120);

try {
    $fulfill = stripe_fulfill_audit_checkout_session($sessionId);
} catch (Throwable $e) {
    error_log('[request-paid-audit] ' . $e->getMessage());
    pl_json_error(502, 'Erreur serveur lors de la finalisation. Réessayez ou contactez le support.');
}
if (!$fulfill['ok']) {
    $status = 502;
    if (str_contains($fulfill['error'], 'non confirmé') || str_contains($fulfill['error'], 'invalide')) {
        $status = 400;
    }
    pl_json_error($status, $fulfill['error'] !== '' ? $fulfill['error'] : 'Impossible de finaliser la commande.');
}

$message = 'Merci ! Votre commande est finalisée : facture enregistrée et audit complet lancé.';
if ($fulfill['invoice_ok'] && $fulfill['audit_ok']) {
    $message = 'Merci ! Facture émise dans Facturio, audit complet en cours — emails sous 24 h ouvrées.';
} elseif ($fulfill['invoice_ok'] && !$fulfill['audit_ok']) {
    $message = 'Facture enregistrée. L’audit n’a pas démarré : contact@danielcraft.fr avec votre email.';
} elseif (!$fulfill['invoice_ok'] && $fulfill['audit_ok']) {
    $message = 'Votre audit complet est en cours. Vous recevrez le rapport par email.';
}

echo json_encode([
    'success' => true,
    'queued' => $fulfill['audit_ok'],
    'invoice_ok' => $fulfill['invoice_ok'],
    'message' => $message,
], JSON_UNESCAPED_UNICODE);
