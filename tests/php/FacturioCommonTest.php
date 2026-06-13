<?php

declare(strict_types=1);

namespace DanielCraft\Tests;

use PHPUnit\Framework\TestCase;

final class FacturioCommonTest extends TestCase
{
    protected function setUp(): void
    {
        require_once DANIELCRAFT_REPO_ROOT . '/api/facturio-common.php';
    }

    public function test_tax_rate_percent_to_decimal(): void
    {
        self::assertSame(0.2, facturio_tax_rate_decimal(20.0));
        self::assertSame(0.2, facturio_tax_rate_decimal(0.2));
    }

    public function test_unit_price_ht_from_ttc(): void
    {
        $ht = facturio_unit_price_ht(199.0, 20.0);
        self::assertEqualsWithDelta(165.8333, $ht, 0.001);
    }

    public function test_line_from_catalog_price_ht(): void
    {
        $line = facturio_line_from_price_ht('Site vitrine', 490.0, 20.0);
        self::assertSame('Site vitrine', $line['description']);
        self::assertSame(490.0, $line['unitPrice']);
        self::assertSame(0.2, $line['taxRate']);
        self::assertArrayNotHasKey('productId', $line);
    }

    public function test_line_with_facturio_product_id(): void
    {
        $line = facturio_line_from_price_ht('Site vitrine', 490.0, 20.0, 1);
        self::assertSame(1, $line['productId']);
    }

    public function test_product_id_from_catalog(): void
    {
        self::assertNull(facturio_product_id_from_catalog([]));
        self::assertSame(1, facturio_product_id_from_catalog(['facturio_product_id' => 1]));
        self::assertNull(facturio_product_id_from_catalog(['facturio_product_id' => 0]));
    }

    public function test_parse_api_error_adds_scope_hint_on_403(): void
    {
        $msg = facturio_parse_api_error(403, ['message' => 'Permission API manquante : devis.write']);
        self::assertStringContainsString('devis.write', $msg);
        self::assertStringContainsString('clients.read', $msg);
        self::assertStringContainsString('scopes', $msg);
    }

    public function test_client_fields_person_without_company(): void
    {
        $fields = facturio_client_fields_from_contact('Marie Dupont');
        self::assertSame('Marie Dupont', $fields['name']);
        self::assertFalse($fields['isCompany']);
    }

    public function test_client_fields_company(): void
    {
        $fields = facturio_client_fields_from_contact('Marie Dupont', 'Société Dupont');
        self::assertSame('Société Dupont', $fields['name']);
        self::assertTrue($fields['isCompany']);
    }

    public function test_client_display_name(): void
    {
        self::assertSame('Marie Dupont', facturio_client_display_name('Marie Dupont'));
        self::assertSame(
            'Société Dupont — Marie Dupont',
            facturio_client_display_name('Marie Dupont', 'Société Dupont')
        );
    }

    public function test_is_missing_product_error(): void
    {
        self::assertTrue(facturio_is_missing_product_error("Produit avec l'ID 957 introuvable"));
        self::assertFalse(facturio_is_missing_product_error('Permission API manquante'));
    }

    public function test_lines_without_product_ids(): void
    {
        $lines = facturio_lines_without_product_ids([
            ['description' => 'Test', 'productId' => 957, 'unitPrice' => 10],
        ]);
        self::assertArrayNotHasKey('productId', $lines[0]);
    }
}
