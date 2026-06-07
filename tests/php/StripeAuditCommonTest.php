<?php

declare(strict_types=1);

namespace DanielCraft\Tests;

use PHPUnit\Framework\TestCase;

final class StripeAuditCommonTest extends TestCase
{
    protected function setUp(): void
    {
        require_once DANIELCRAFT_REPO_ROOT . '/api/stripe-audit-common.php';
    }

    public function test_unit_amount_from_price_cents(): void
    {
        self::assertSame(19900, stripe_audit_unit_amount_cents(['price_cents' => 19900]));
    }

    public function test_unit_amount_from_price_eur(): void
    {
        self::assertSame(19900, stripe_audit_unit_amount_cents(['price_eur' => 199]));
    }

    public function test_find_audit_item_by_slug(): void
    {
        $item = stripe_find_audit_item('audit-complet-ia');
        self::assertIsArray($item);
        self::assertSame(199, $item['price_eur'] ?? null);
    }

    public function test_rejects_invalid_slug(): void
    {
        self::assertNull(stripe_find_audit_item('../hack'));
        self::assertNull(stripe_find_audit_item(''));
    }

    public function test_checkout_params_include_site_url(): void
    {
        $item = stripe_find_audit_item('audit-complet-ia');
        self::assertIsArray($item);

        $params = stripe_audit_checkout_session_params(
            $item,
            'audit-complet-ia',
            'https://client.fr',
            'Jean Test'
        );

        self::assertStringContainsString('https://client.fr', (string) $params['line_items[0][price_data][product_data][description]']);
        self::assertSame('Jean Test', $params['metadata[customer_name]'] ?? null);
    }
}
