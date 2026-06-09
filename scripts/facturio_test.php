#!/usr/bin/env php
<?php
/**
 * Test Facturio API (sans créer de vrai devis client).
 * Usage: php scripts/facturio_test.php
 *        php scripts/facturio_test.php --dry-devis
 */
declare(strict_types=1);

$root = dirname(__DIR__);
require_once $root . '/api/env.php';
require_once $root . '/api/facturio-common.php';

facturio_bootstrap();

echo 'configured: ' . (facturio_configured() ? 'yes' : 'no') . PHP_EOL;
echo 'base: ' . facturio_api_base() . PHP_EOL;

$ping = facturio_http('GET', '');
echo 'GET /public: ok=' . ($ping['ok'] ? 'yes' : 'no')
    . ' status=' . $ping['status']
    . ' error=' . ($ping['error'] ?: '-') . PHP_EOL;
if (is_array($ping['data'])) {
    echo 'summary: ' . json_encode($ping['data'], JSON_UNESCAPED_UNICODE) . PHP_EOL;
}

if (!in_array('--dry-devis', $argv ?? [], true)) {
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
$create = facturio_create_quote_devis(
    'test-devis-' . gmdate('YmdHis') . '@example.invalid',
    'Test DanielCraft',
    $lines,
    'Test automatique scripts/facturio_test.php — à supprimer'
);
echo 'POST /devis: ok=' . ($create['ok'] ? 'yes' : 'no')
    . ' id=' . ($create['quote_id'] ?: '-')
    . ' error=' . ($create['error'] ?: '-') . PHP_EOL;

exit($create['ok'] ? 0 : 1);
