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
}
