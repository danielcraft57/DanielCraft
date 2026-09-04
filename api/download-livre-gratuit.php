<?php
/**
 * Telechargement PDF d'un livre marque gratuit (GET ?slug=…).
 * Pas de Stripe, pas de token : le catalogue decide.
 */

declare(strict_types=1);

require_once __DIR__ . '/livre-download-common.php';

api_bootstrap_env();

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'GET') {
    http_response_code(405);
    header('Content-Type: text/plain; charset=utf-8');
    echo 'Methode non autorisee';
    exit;
}

$slug = isset($_GET['slug']) ? trim((string) $_GET['slug']) : '';
$fiche = static function (string $s): string {
    $s = trim($s);
    if ($s !== '' && preg_match('/^[a-z0-9-]{1,80}$/', $s)) {
        return api_site_base() . '/bouquins/' . rawurlencode($s) . '/';
    }

    return api_site_base() . '/bouquins/';
};

if ($slug === '' || !preg_match('/^[a-z0-9-]{1,80}$/', $slug)) {
    header('Location: ' . $fiche(''), true, 302);
    exit;
}

$item = stripe_find_livre_item($slug);
if ($item === null) {
    http_response_code(404);
    header('Content-Type: text/plain; charset=utf-8');
    echo 'Livre introuvable.';
    exit;
}

if (!livre_item_is_free($item)) {
    header('Location: ' . $fiche($slug), true, 302);
    exit;
}

$ip = livre_download_client_ip();
if (!livre_download_rate_allow('free:' . $ip, 30, 900)) {
    http_response_code(429);
    header('Content-Type: text/plain; charset=utf-8');
    echo 'Trop de telechargements. Reessaie un peu plus tard.';
    exit;
}

$files = livre_resolve_pdf_files($item);
if ($files === []) {
    http_response_code(404);
    header('Content-Type: text/plain; charset=utf-8');
    echo 'Aucun PDF pour ce livre.';
    exit;
}

$filename = (string) ($files[0]['filename'] ?? '');
$path = livre_pdf_absolute_path($filename);
if ($path === '') {
    http_response_code(404);
    header('Content-Type: text/plain; charset=utf-8');
    echo 'PDF indisponible sur le serveur.';
    exit;
}

livre_download_stream_pdf($path);
