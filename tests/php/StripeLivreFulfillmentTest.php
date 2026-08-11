<?php

declare(strict_types=1);

namespace DanielCraft\Tests;

use PHPUnit\Framework\TestCase;

final class StripeLivreFulfillmentTest extends TestCase
{
    protected function setUp(): void
    {
        require_once DANIELCRAFT_REPO_ROOT . '/api/stripe-livre-fulfillment.php';
    }

    public function test_session_is_paid_livre_with_product_type(): void
    {
        $session = [
            'payment_status' => 'paid',
            'metadata' => ['product_type' => 'livre_pdf', 'livre_slug' => 'html-css-les-bases'],
        ];
        self::assertTrue(stripe_session_is_paid_livre($session));
    }

    public function test_session_is_paid_livre_with_slug_only(): void
    {
        $session = [
            'payment_status' => 'paid',
            'metadata' => ['livre_slug' => 'python-les-bases'],
        ];
        self::assertTrue(stripe_session_is_paid_livre($session));
    }

    public function test_session_is_not_paid_when_unpaid(): void
    {
        $session = [
            'payment_status' => 'unpaid',
            'metadata' => ['product_type' => 'livre_pdf'],
        ];
        self::assertFalse(stripe_session_is_paid_livre($session));
    }

    public function test_session_context_extracts_metadata(): void
    {
        $session = [
            'customer_email' => 'lecteur@exemple.fr',
            'metadata' => [
                'livre_slug' => 'html-css-les-bases',
                'livre_title' => 'HTML & CSS — Les bases',
            ],
        ];

        $ctx = stripe_livre_session_context($session);
        self::assertSame('lecteur@exemple.fr', $ctx['email']);
        self::assertSame('html-css-les-bases', $ctx['slug']);
        self::assertSame('HTML & CSS — Les bases', $ctx['title']);
    }

    public function test_normalize_code_accepts_messy_input(): void
    {
        self::assertSame('DC-ABCD-2345', livre_download_normalize_code('dc abcd-2345'));
        self::assertSame('DC-ABCD-2345', livre_download_normalize_code('ABCD2345'));
        self::assertSame('', livre_download_normalize_code('DC-OOOI-1111'));
    }

    public function test_form_guards_reject_honeypot(): void
    {
        $res = livre_download_verify_form_guards('Bot Corp', '', time() - 5, true);
        self::assertFalse($res['ok']);
        self::assertSame('honeypot', $res['error']);
    }

    public function test_form_guards_reject_too_fast(): void
    {
        $res = livre_download_verify_form_guards('', '', time(), true);
        self::assertFalse($res['ok']);
        self::assertStringContainsString('rapide', $res['error']);
    }

    public function test_form_guards_accept_valid(): void
    {
        $res = livre_download_verify_form_guards('', '', time() - 3, true);
        self::assertTrue($res['ok']);
    }

    public function test_resolve_pdf_files_single_livre(): void
    {
        $item = [
            'slug' => 'html-css-les-bases',
            'kind' => 'livre',
            'title' => 'HTML & CSS — Les bases',
            'pdf' => 'html-css-les-bases.pdf',
        ];
        $files = livre_resolve_pdf_files($item);
        self::assertCount(1, $files);
        self::assertSame('html-css-les-bases.pdf', $files[0]['filename']);
    }

    public function test_resolve_pdf_files_pack(): void
    {
        $item = stripe_find_livre_item('pack-debutant-code');
        if (!is_array($item)) {
            self::markTestSkipped('Catalogue livres indisponible en test.');
        }
        $files = livre_resolve_pdf_files($item);
        self::assertGreaterThanOrEqual(2, count($files));
        foreach ($files as $file) {
            self::assertMatchesRegularExpression('/\.pdf$/i', $file['filename']);
            self::assertNotSame('', $file['label']);
        }
    }
}
