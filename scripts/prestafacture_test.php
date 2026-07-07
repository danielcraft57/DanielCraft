#!/usr/bin/env php
<?php
/**
 * Test Prestafacture API (sans créer de vrai devis client).
 * Usage: php scripts/prestafacture_test.php
 *        php scripts/prestafacture_test.php --dry-devis
 */
declare(strict_types=1);

$root = dirname(__DIR__);
require_once $root . '/api/env.php';
require_once $root . '/api/prestafacture-common.php';

prestafacture_bootstrap();

echo 'configured: ' . (prestafacture_configured() ? 'yes' : 'no') . PHP_EOL;
echo 'base: ' . prestafacture_api_base() . PHP_EOL;

$ping = prestafacture_http('GET', '');
echo 'GET /public: ok=' . ($ping['ok'] ? 'yes' : 'no')
    . ' status=' . $ping['status']
    . ' error=' . ($ping['error'] ?: '-') . PHP_EOL;
if (is_array($ping['data'])) {
    echo 'summary: ' . json_encode($ping['data'], JSON_UNESCAPED_UNICODE) . PHP_EOL;
}

$argv = $argv ?? [];
$testClient = in_array('--test-client', $argv, true);
$dryDevis = in_array('--dry-devis', $argv, true);

if ($testClient) {
    $probeEmail = 'test-client-' . gmdate('YmdHis') . '@example.invalid';
    echo 'ensure client: ' . $probeEmail . PHP_EOL;
    $ensured = prestafacture_ensure_client_id($probeEmail, 'Marie Dupont', 'Société Test');
    echo 'ensure: ok=' . ($ensured['ok'] ? 'yes' : 'no')
        . ' id=' . ($ensured['client_id'] ?: '-')
        . ' created=' . (!empty($ensured['created']) ? 'yes' : 'no')
        . ' error=' . ($ensured['error'] ?: '-') . PHP_EOL;

    if ($ensured['ok']) {
        $again = prestafacture_ensure_client_id($probeEmail, 'Marie Dupont', 'Société Test');
        echo 'ensure (2e fois): ok=' . ($again['ok'] ? 'yes' : 'no')
            . ' id=' . ($again['client_id'] ?: '-')
            . ' created=' . (!empty($again['created']) ? 'yes' : 'no')
            . ' error=' . ($again['error'] ?: '-') . PHP_EOL;
        exit($again['ok'] && empty($again['created']) ? 0 : 1);
    }
    exit(1);
}

if (!$dryDevis) {
    exit($ping['ok'] ? 0 : 1);
}

$lines = [
    [
        'description' => 'Test devis DanielCraft (script)',
        'quantity' => 1,
        'unitPrice' => 408.33,
        'taxRate' => 0.2,
    ],
];
$create = prestafacture_create_quote_devis(
    'test-devis-' . gmdate('YmdHis') . '@example.invalid',
    'Test DanielCraft',
    $lines,
    'Test automatique scripts/prestafacture_test.php — à supprimer'
);
echo 'POST /devis: ok=' . ($create['ok'] ? 'yes' : 'no')
    . ' id=' . ($create['quote_id'] ?: '-')
    . ' error=' . ($create['error'] ?: '-') . PHP_EOL;

exit($create['ok'] ? 0 : 1);
