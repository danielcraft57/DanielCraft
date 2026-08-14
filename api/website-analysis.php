<?php
/**
 * Proxy securise d'analyse (token cote serveur).
 *
 * Usage:
 *   GET /api/website-analysis.php?website=https://exemple.com&full=1
 *   GET /api/website-analysis.php?website=exemple.com&full=1
 *
 * Securite:
 * - Token en dur (NE PAS versionner en public).
 * - Rate limiting par IP (req/sec + req/min) via fichiers temporaires.
 */

declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');
header('Cache-Control: no-store, no-cache, must-revalidate, max-age=0');
header('Pragma: no-cache');

require_once __DIR__ . '/prospectlab-common.php';

pl_bootstrap();

const LIMIT_PER_SECOND = 2;
const LIMIT_PER_MINUTE = 30;

function json_error(int $status, string $message): void
{
    http_response_code($status);
    echo json_encode(['success' => false, 'error' => $message], JSON_UNESCAPED_UNICODE);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'GET') {
    json_error(405, 'Méthode non autorisée');
}

$ip = pl_client_ip();
pl_rate_limit_or_die('wa:' . $ip . ':sec', LIMIT_PER_SECOND, 1);
pl_rate_limit_or_die('wa:' . $ip . ':min', LIMIT_PER_MINUTE, 60);

$websiteRaw = isset($_GET['website']) ? (string) $_GET['website'] : '';
$full = isset($_GET['full']) ? (string) $_GET['full'] : '1';

$website = pl_sanitize_website_query($websiteRaw);
if ($website === '') {
    json_error(400, 'Paramètre "website" invalide. Utilisez une URL http(s) ou un nom de domaine.');
}

$result = pl_fetch_website_analysis($website, $full);
if (!$result['ok']) {
    json_error((int) ($result['status'] ?? 502), (string) ($result['error'] ?? 'Erreur proxy.'));
}

http_response_code((int) ($result['status'] ?? 200));
echo (string) ($result['body'] ?? '');
