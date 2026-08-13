<?php

declare(strict_types=1);

namespace DanielCraft\Tests;

use PHPUnit\Framework\TestCase;

final class StripeCommonTest extends TestCase
{
    protected function setUp(): void
    {
        require_once DANIELCRAFT_REPO_ROOT . '/api/stripe-common.php';
    }

    public function test_statement_suffix_strips_specials_and_uppercases(): void
    {
        self::assertSame('LIVRE PDF', stripe_statement_descriptor_suffix('livre pdf'));
        self::assertSame('AUDITWEB', stripe_statement_descriptor_suffix("AUDIT*WEB"));
        self::assertSame('', stripe_statement_descriptor_suffix('***'));
    }

    public function test_refund_rejects_invalid_payment_intent(): void
    {
        $res = stripe_refund_payment_intent('not-a-pi');
        self::assertFalse($res['ok']);
        self::assertSame('PaymentIntent invalide.', $res['error']);
        self::assertSame('', $res['refund_id']);
    }
}
