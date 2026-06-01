<?php
/**
 * Routeur pour le serveur PHP intégré : php -S localhost:8000 -t dist router.php
 * Copié vers dist/ au build ; résout /audit, /analyse, etc.
 */
$uri = urldecode(parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH));
$file = __DIR__ . $uri;

if ($uri !== '/' && is_file($file)) {
    return false;
}

$html = $file . '.html';
if ($uri !== '/' && is_file($html)) {
    require $html;
    return true;
}

if (is_dir($file) && is_file($file . DIRECTORY_SEPARATOR . 'index.html')) {
    require $file . DIRECTORY_SEPARATOR . 'index.html';
    return true;
}

return false;
