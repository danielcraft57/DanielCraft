<?php

declare(strict_types=1);

namespace DanielCraft\Tests;

use PHPUnit\Framework\TestCase;

final class DevisCommonTest extends TestCase
{
    protected function setUp(): void
    {
        require_once DANIELCRAFT_REPO_ROOT . '/api/devis-common.php';
    }

    public function test_should_issue_quote_for_catalog_service(): void
    {
        self::assertTrue(devis_should_issue_quote('pack_vitrine'));
        self::assertTrue(devis_should_issue_quote('', 'site-vitrine'));
    }

    public function test_should_not_issue_quote_for_open_ended_services(): void
    {
        self::assertFalse(devis_should_issue_quote('besoin_a_preciser'));
        self::assertFalse(devis_should_issue_quote('projet_sur_mesure'));
        self::assertFalse(devis_should_issue_quote('audit_gratuit_site'));
    }

    public function test_should_issue_quote_for_vitrine_catalog(): void
    {
        self::assertTrue(devis_should_issue_quote('vitrine_catalog_order'));
        self::assertTrue(devis_should_issue_quote('vitrine_catalog_devis'));
    }

    public function test_build_catalog_quote_includes_base_price(): void
    {
        $built = devis_build_catalog_quote('pack_vitrine');
        self::assertNotNull($built);
        self::assertSame('Site vitrine professionnel', $built['title']);
        self::assertSame(590, $built['total_ht']);
        self::assertCount(1, $built['lines']);
    }

    public function test_build_vitrine_quote_defaults_price(): void
    {
        $built = devis_build_vitrine_quote('vitrine_catalog_order', 'Brasserie Saint-Jacques', 'restauration', 0);
        self::assertSame(42, $built['total_ht']);
        self::assertStringContainsString('Brasserie Saint-Jacques', $built['title']);
    }

    public function test_try_issue_for_contact_skips_open_ended(): void
    {
        $outcome = devis_try_issue_for_contact([
            'name' => 'Marie Dupont',
            'email' => 'marie@exemple.fr',
            'phone' => '06 12 34 56 78',
            'service' => 'besoin_a_preciser',
            'project_type' => 'site',
            'message' => 'Besoin à préciser',
        ]);
        self::assertSame('skip', $outcome['mode']);
    }
}
