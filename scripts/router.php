<?php
/**
 * Routeur pour le serveur PHP intégré :
 *   php -S 127.0.0.1:8000 -t dist dist/router.php
 *
 * Copié vers dist/ au build. Gère :
 * - exécution des .php sous /api/
 * - URLs sans .html (pages racine, blog, vitrines, prestations, projets…)
 * - index.html dans les sous-dossiers
 */
declare(strict_types=1);

$uri = urldecode(parse_url($_SERVER['REQUEST_URI'] ?? '/', PHP_URL_PATH) ?: '/');
$root = __DIR__;
$file = $root . $uri;

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

// Fichier existant (assets, .php, images…) → serveur PHP natif
if ($uri !== '/' && is_file($absolute)) {
    return false;
}

$resolved = dc_resolve_static($root, $uri);
if ($resolved !== null) {
    header('Content-Type: text/html; charset=UTF-8');
    readfile($resolved);
    return true;
}

return false;
