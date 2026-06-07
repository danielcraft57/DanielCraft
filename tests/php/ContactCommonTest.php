<?php

declare(strict_types=1);

namespace DanielCraft\Tests;

use PHPUnit\Framework\TestCase;

final class ContactCommonTest extends TestCase
{
    protected function setUp(): void
    {
        require_once DANIELCRAFT_REPO_ROOT . '/api/contact-common.php';
    }

    public function test_normalize_site_url_adds_https(): void
    {
        self::assertSame('https://exemple.fr', contact_normalize_site_url('exemple.fr'));
        self::assertSame('https://exemple.fr/page', contact_normalize_site_url('https://exemple.fr/page'));
    }

    public function test_project_type_labels_grand_public(): void
    {
        self::assertSame('Un site internet', contact_project_type_label('site'));
        self::assertSame('Être visible sur Google', contact_project_type_label('visibilite'));
    }

    public function test_valid_grand_public_payload(): void
    {
        $result = contact_validate_payload([
            'name' => 'Marie Dupont',
            'email' => 'marie@exemple.fr',
            'phone' => '06 12 34 56 78',
            'project_type' => 'site',
            'service' => 'pack_vitrine',
            'message' => 'Je souhaite un devis pour un site vitrine.',
        ]);

        self::assertSame([], $result['errors']);
        self::assertSame('site', $result['data']['project_type']);
        self::assertSame('pack_vitrine', $result['data']['service']);
    }

    public function test_rejects_missing_need_category(): void
    {
        $result = contact_validate_payload([
            'name' => 'Test',
            'email' => 'test@exemple.fr',
            'service' => 'pack_vitrine',
            'message' => 'Bonjour',
            'project_type' => '',
        ]);

        self::assertContains('Le besoin principal est obligatoire.', $result['errors']);
    }

    public function test_rejects_legacy_only_project_type_when_empty(): void
    {
        $result = contact_validate_payload([
            'name' => 'Test',
            'email' => 'test@exemple.fr',
            'service' => 'pack_vitrine',
            'message' => 'Bonjour',
        ]);

        self::assertContains('Le besoin principal est obligatoire.', $result['errors']);
    }

    public function test_accepts_legacy_project_type_slug(): void
    {
        $result = contact_validate_payload([
            'name' => 'Test',
            'email' => 'test@exemple.fr',
            'project_type' => 'web',
            'service' => 'pack_vitrine',
            'message' => 'Bonjour',
        ]);

        self::assertSame([], $result['errors']);
    }

    public function test_audit_flow_requires_site_url(): void
    {
        $result = contact_validate_payload([
            'email' => 'audit@exemple.fr',
            'project_type' => 'visibilite',
            'service' => 'audit_gratuit_site',
        ]);

        self::assertContains('L\'URL de votre site est obligatoire pour l\'audit gratuit.', $result['errors']);
    }

    public function test_audit_flow_normalizes_site_url(): void
    {
        $result = contact_validate_payload([
            'email' => 'audit@exemple.fr',
            'project_type' => 'visibilite',
            'service' => 'audit_gratuit_site',
            'site_url' => 'mon-site.fr',
        ]);

        self::assertSame([], $result['errors']);
        self::assertSame('https://mon-site.fr', $result['data']['site_url']);
        self::assertSame('Demandeur audit', $result['data']['name']);
    }
}
