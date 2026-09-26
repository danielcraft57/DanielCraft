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
        self::assertSame('Site vitrine pro (jusqu\'à 5 pages)', $built['title']);
        // quote_lines : 141+338+115+66+0 = 660
        self::assertSame(660, $built['total_ht']);
        self::assertCount(5, $built['lines']);
        self::assertSame(0.0, (float) $built['lines'][0]['taxRate']);
    }

    public function test_build_catalog_quote_essentiel_detail(): void
    {
        $built = devis_build_catalog_quote('pack_vitrine_essentiel');
        self::assertNotNull($built);
        self::assertSame(460, $built['total_ht']);
        self::assertGreaterThanOrEqual(5, count($built['lines']));
    }

    public function test_build_catalog_quote_complet(): void
    {
        $built = devis_build_catalog_quote('pack_complet_annee1');
        self::assertNotNull($built);
        self::assertSame(1132, $built['total_ht']);
        self::assertSame(12.0, (float) $built['lines'][5]['quantity']);
    }

    public function test_build_catalog_quote_ia_includes_year1_maint(): void
    {
        $built = devis_build_catalog_quote('ia_faq_site');
        self::assertNotNull($built);
        self::assertSame(990 + 69 * 12, $built['total_ht']);
        self::assertGreaterThanOrEqual(2, count($built['lines']));
    }

    public function test_mail_pro_and_serenite_pack_exist(): void
    {
        self::assertNotNull(prestations_find_by_slug('mail-pro'));
        self::assertNotNull(prestations_find_by_slug('pack-serenite-sobriete'));
        $mail = prestations_find_by_service_slug('maint_mail_pro');
        self::assertSame(0, (int) ($mail['price_eur'] ?? -1));
        $vps = prestations_find_by_slug('hebergement-domaine');
        self::assertSame(66, (int) ($vps['price_eur'] ?? 0));
        $entretien = prestations_find_by_slug('entretien-mensuel');
        self::assertSame(56, (int) ($entretien['price_eur'] ?? 0));
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
