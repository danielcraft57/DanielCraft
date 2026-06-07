<?php

declare(strict_types=1);

namespace DanielCraft\Tests;

use PHPUnit\Framework\TestCase;

final class StripeAuditFulfillmentTest extends TestCase
{
    protected function setUp(): void
    {
        require_once DANIELCRAFT_REPO_ROOT . '/api/stripe-audit-fulfillment.php';
    }

    public function test_session_is_paid_audit_with_product_type(): void
    {
        $session = [
            'payment_status' => 'paid',
            'metadata' => ['product_type' => 'audit_ia'],
        ];
        self::assertTrue(stripe_session_is_paid_audit($session));
    }

    public function test_session_is_not_paid_when_unpaid(): void
    {
        $session = [
            'payment_status' => 'unpaid',
            'metadata' => ['product_type' => 'audit_ia'],
        ];
        self::assertFalse(stripe_session_is_paid_audit($session));
    }

    public function test_session_context_extracts_metadata(): void
    {
        $session = [
            'customer_email' => 'client@exemple.fr',
            'metadata' => [
                'customer_name' => 'Loïc',
                'site_url' => 'https://exemple.fr',
                'audit_slug' => 'audit-complet-ia',
            ],
        ];

        $ctx = stripe_audit_session_context($session);
        self::assertSame('client@exemple.fr', $ctx['email']);
        self::assertSame('Loïc', $ctx['name']);
        self::assertSame('https://exemple.fr', $ctx['site_url']);
        self::assertSame('audit-complet-ia', $ctx['slug']);
    }
}
