<?php
/**
 * Ancien checkout Stripe des fiches exemples (devantures).
 * Les exemples ne se vendent plus — devis / contact uniquement.
 */

declare(strict_types=1);

require_once __DIR__ . '/env.php';

api_bootstrap_env();
api_json_headers();

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204);
    exit;
}

http_response_code(410);
echo json_encode([
    'success' => false,
    'error' => 'Les echantillons de sites ne se paient plus. Contactez DanielCraft pour un site sur mesure.',
], JSON_UNESCAPED_UNICODE);
