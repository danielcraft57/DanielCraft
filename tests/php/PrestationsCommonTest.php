<?php

declare(strict_types=1);

namespace DanielCraft\Tests;

use PHPUnit\Framework\TestCase;

final class PrestationsCommonTest extends TestCase
{
    protected function setUp(): void
    {
        require_once DANIELCRAFT_REPO_ROOT . '/api/prestations-common.php';
    }

    public function test_find_site_vitrine_by_slug(): void
    {
        $item = prestations_find_by_slug('site-vitrine');
        self::assertIsArray($item);
        self::assertSame('site-vitrine', $item['slug'] ?? null);
    }

    public function test_find_by_service_slug(): void
    {
        $item = prestations_find_by_service_slug('pack_vitrine');
        self::assertIsArray($item);
        self::assertSame('site-vitrine', $item['slug'] ?? null);
    }

    public function test_unknown_slug_returns_null(): void
    {
        self::assertNull(prestations_find_by_slug('slug-inexistant-xyz'));
    }
}
