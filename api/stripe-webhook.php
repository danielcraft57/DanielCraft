<?php
/**
 * Webhook Stripe — checkout.session.completed (audit premium → Prestafacture + ProspectLab).
 */

declare(strict_types=1);

require_once __DIR__ . '/env.php';
require_once __DIR__ . '/stripe-audit-fulfillment.php';

api_bootstrap_env();

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo 'Method not allowed';
    exit;
}

$payload = file_get_contents('php://input');
if ($payload === false || $payload === '') {
    http_response_code(400);
    echo 'Empty payload';
    exit;
}

$secret = trim((string) (getenv('STRIPE_WEBHOOK_SECRET') ?: ''));
if ($secret === '' || $secret === 'REPLACE_ME') {
    error_log('[stripe-webhook] STRIPE_WEBHOOK_SECRET manquant');
    http_response_code(500);
    echo 'Webhook non configuré';
    exit;
}

$sigHeader = isset($_SERVER['HTTP_STRIPE_SIGNATURE']) ? (string) $_SERVER['HTTP_STRIPE_SIGNATURE'] : '';
if ($sigHeader === '' || !stripe_webhook_verify_signature($payload, $sigHeader, $secret)) {
    http_response_code(400);
    echo 'Invalid signature';
    exit;
}

$event = json_decode($payload, true);
if (!is_array($event) || empty($event['type'])) {
    http_response_code(400);
    echo 'Invalid event';
    exit;
}

$type = (string) $event['type'];
if ($type === 'checkout.session.completed') {
    $object = is_array($event['data']['object'] ?? null) ? $event['data']['object'] : [];
    if (stripe_session_is_paid_audit($object)) {
        $sessionId = isset($object['id']) ? (string) $object['id'] : '';
        if ($sessionId !== '') {
            stripe_fulfill_audit_checkout_session($sessionId);
        }
    }
}

http_response_code(200);
echo json_encode(['received' => true]);

/**
 * Vérifie Stripe-Signature (tolerance 5 min).
 */
function stripe_webhook_verify_signature(string $payload, string $sigHeader, string $secret): bool
{
    $parts = explode(',', $sigHeader);
    $timestamp = null;
    $signatures = [];
    foreach ($parts as $part) {
        $kv = explode('=', trim($part), 2);
        if (count($kv) !== 2) {
            continue;
        }
        if ($kv[0] === 't') {
            $timestamp = $kv[1];
        } elseif ($kv[0] === 'v1') {
            $signatures[] = $kv[1];
        }
    }
    if ($timestamp === null || $signatures === []) {
        return false;
    }
    if (abs(time() - (int) $timestamp) > 300) {
        return false;
    }
    $signed = $timestamp . '.' . $payload;
    $expected = hash_hmac('sha256', $signed, $secret);
    foreach ($signatures as $sig) {
        if (hash_equals($expected, $sig)) {
            return true;
        }
    }
    return false;
}
