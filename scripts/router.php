<?php
/**
 * Routeur pour le serveur PHP intégré :
 *   php -S 127.0.0.1:8000 -t dist dist/router.php
 *
 * Copié vers dist/ au build. Gère :
 * - fichiers statiques (/assets/js, /assets/css, images…)
 * - exécution des .php sous /api/
 * - URLs sans .html (pages racine, blog, vitrines, prestations, projets…)
 * - index.html dans les sous-dossiers
 */
declare(strict_types=1);

$uri = urldecode(parse_url($_SERVER['REQUEST_URI'] ?? '/', PHP_URL_PATH) ?: '/');
$root = __DIR__;

/** Types MIME courants pour les assets statiques */
function dc_static_mime(string $ext): string
{
    return match (strtolower($ext)) {
        'css' => 'text/css; charset=UTF-8',
        'js' => 'application/javascript; charset=UTF-8',
        'json' => 'application/json; charset=UTF-8',
        'svg' => 'image/svg+xml',
        'webp' => 'image/webp',
        'png' => 'image/png',
        'jpg', 'jpeg' => 'image/jpeg',
        'gif' => 'image/gif',
        'ico' => 'image/x-icon',
        'woff' => 'font/woff',
        'woff2' => 'font/woff2',
        'ttf' => 'font/ttf',
        'xml' => 'application/xml; charset=UTF-8',
        'txt' => 'text/plain; charset=UTF-8',
        default => 'application/octet-stream',
    };
}

/** @return string|null chemin absolu fichier à servir, ou null si laisser PHP natif */
function dc_resolve_static(string $root, string $uri): ?string
{
    if ($uri === '/' || $uri === '') {
        $index = $root . DIRECTORY_SEPARATOR . 'index.html';
        return is_file($index) ? $index : null;
    }

    $path = $uri;
    $ext = strtolower(pathinfo($path, PATHINFO_EXTENSION));

    if ($path === '/blog' || $path === '/blog/') {
        $candidate = $root . DIRECTORY_SEPARATOR . 'blog' . DIRECTORY_SEPARATOR . 'index.html';
        return is_file($candidate) ? $candidate : null;
    }

    if (str_ends_with($path, '/') && str_starts_with($path, '/blog/')) {
        $candidate = $root . str_replace('/', DIRECTORY_SEPARATOR, rtrim($path, '/') . '/index.html');
        return is_file($candidate) ? $candidate : null;
    }

    if ($ext === '') {
        $blogPrefixes = ['/blog/articles/', '/blog/series/', '/blog/types/'];
        foreach ($blogPrefixes as $prefix) {
            if (str_starts_with($path, $prefix)) {
                $candidate = $root . str_replace('/', DIRECTORY_SEPARATOR, $path . '.html');
                return is_file($candidate) ? $candidate : null;
            }
        }

        $candidate = $root . str_replace('/', DIRECTORY_SEPARATOR, rtrim($path, '/') . '.html');
        if (is_file($candidate)) {
            return $candidate;
        }
    }

    $dir = $root . str_replace('/', DIRECTORY_SEPARATOR, rtrim($path, '/'));
    if (is_dir($dir)) {
        $index = $dir . DIRECTORY_SEPARATOR . 'index.html';
        return is_file($index) ? $index : null;
    }

    return null;
}

$absolute = $root . str_replace('/', DIRECTORY_SEPARATOR, $uri);

// Fichier statique existant (assets, images, favicon…) — servi explicitement
if ($uri !== '/' && is_file($absolute)) {
    $ext = strtolower(pathinfo($uri, PATHINFO_EXTENSION));
    if ($ext !== 'php') {
        header('Content-Type: ' . dc_static_mime($ext));
        header('Cache-Control: no-cache');
        readfile($absolute);
        return true;
    }
    return false;
}

$resolved = dc_resolve_static($root, $uri);
if ($resolved !== null) {
    header('Content-Type: text/html; charset=UTF-8');
    readfile($resolved);
    return true;
}

return false;
