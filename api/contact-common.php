<?php
/**
 * Validation et libellés du formulaire de contact (testable sans HTTP).
 */

declare(strict_types=1);

require_once __DIR__ . '/env.php';

/** @return list<string> */
function contact_allowed_need_categories(): array
{
    return [
        'site', 'visibilite', 'assistant', 'entretien', 'autre',
        'web', 'backend', 'mobile', 'desktop', 'tools', 'specialized', 'learning', 'other',
    ];
}

function contact_service_label(string $slug): string
{
    static $map = [
        'pack_vitrine' => 'Site vitrine (490€)',
        'pack_identite' => 'Identité & visibilité multi-supports (990€)',
        'pack_seo_complet' => 'SEO Google + ChatGPT — pack (699€)',
        'audit_gratuit_site' => 'Audit gratuit site web (offre découverte)',
        'audit_paid_complet_ia' => 'Audit complet IA (payant)',
        'seo_basique_290' => 'SEO basique — audit + corrections (290€)',
        'seo_chatgpt_490' => 'SEO ChatGPT / découvrabilité IA (490€)',
        'ia_faq_site' => 'Assistant IA FAQ site web (990€)',
        'ia_support_client' => 'Assistant IA support client / email (1200€)',
        'ia_contenu_web' => 'Générateur de contenus web par IA (650€)',
        'ia_redaction_pro' => 'Assistant IA rédaction commerciale (490€)',
        'ia_analyse_donnees' => 'Analyse de données avec IA (1450€)',
        'ia_chatbot_ecom' => 'Chatbot IA e-commerce (1600€)',
        'ia_automatisation' => 'Automatisation de tâches avec IA (1200€)',
        'ia_abo_mensuel' => 'Maintenance mensuelle assistant IA (75€/mois)',
        'ia_evolution' => 'Évolution fonctionnalités IA (dès 330€)',
        'ia_audit' => 'Audit utilisation IA (400€)',
        'tech_conseil_archi' => 'Conseil technique / architecture (380€)',
        'tech_integration_crm' => 'Intégration CRM ou outil métier (dès 290€)',
        'tech_migration_donnees' => 'Migration de données (330€)',
        'tech_api_webhook' => 'Intégration API / webhook (dès 150€)',
        'tech_perf_rapport' => 'Rapport de performances (120€)',
        'site_page_supp' => 'Page supplémentaire site vitrine (65€/page)',
        'site_form_avance' => 'Formulaire avancé / intégration (99€)',
        'site_refonte_visuelle' => 'Refonte visuelle légère (330€)',
        'site_maj_contenu_5h' => 'Mise à jour contenu — pack 5h (170€)',
        'maint_site_mensuel' => 'Maintenance site mensuelle (39€/mois)',
        'maint_hebergement' => 'Hébergement + domaine (79€/an)',
        'maint_backup' => 'Backup & sécurisation (99€)',
        'maint_ssl' => 'SSL + configuration (45€)',
        'maint_support_abo' => 'Support / abonnement (25€/mois)',
        'maint_depannage_2h' => 'Dépannage forfait 2h (120€)',
        'maint_accompagnement_h' => 'Accompagnement technique à l\'heure (60€/h)',
        'maint_support_prio_h' => 'Support prioritaire à l\'heure (70€/h)',
        'besoin_a_preciser' => 'Besoin à préciser ensemble',
        'projet_sur_mesure' => 'Projet sur mesure / autre',
        'vitrine_catalog_order' => 'Pré-commande depuis le catalogue (sans paiement sur le site)',
        'vitrine_catalog_devis' => 'Devis / questions — fiche catalogue',
    ];
    if (isset($map[$slug])) {
        return $map[$slug];
    }
    if (preg_match('/^[a-z0-9_]{1,80}$/', $slug)) {
        return ucwords(str_replace('_', ' ', $slug));
    }
    return 'Prestation (réf. invalide)';
}

function contact_project_type_label(string $slug): string
{
    static $map = [
        'site' => 'Un site internet',
        'visibilite' => 'Être visible sur Google',
        'assistant' => 'Un assistant sur mon site',
        'entretien' => 'Entretien & dépannage',
        'autre' => 'Je ne sais pas encore',
        'web' => 'Développement Web',
        'backend' => 'Backend & APIs',
        'mobile' => 'Application mobile',
        'desktop' => 'Application desktop',
        'tools' => 'Outils & automatisation',
        'specialized' => 'Spécialisé (data, finance, IoT…)',
        'learning' => 'Veille / apprentissage / proto',
        'other' => 'Autre / à préciser',
    ];
    return $map[$slug] ?? $slug;
}

function contact_normalize_site_url(string $url): string
{
    if ($url === '') {
        return '';
    }
    if (!preg_match('#^https?://#i', $url)) {
        $url = 'https://' . ltrim($url, '/');
    }
    return $url;
}

/**
 * @param array<string, mixed> $raw
 * @return array{errors: list<string>, data: array<string, string>}
 */
function contact_validate_payload(array $raw): array
{
    $name = isset($raw['name']) ? trim(strip_tags((string) $raw['name'])) : '';
    $email = isset($raw['email']) ? trim((string) $raw['email']) : '';
    $phone = isset($raw['phone']) ? trim(strip_tags((string) $raw['phone'])) : '';
    $service = isset($raw['service']) ? trim(strip_tags((string) $raw['service'])) : '';
    $project_type = isset($raw['project_type']) ? trim(strip_tags((string) $raw['project_type'])) : '';
    $budget = isset($raw['budget']) ? trim(strip_tags((string) $raw['budget'])) : '';
    $message = isset($raw['message']) ? trim(strip_tags((string) $raw['message'])) : '';
    $preferred_date = isset($raw['preferred_date']) ? trim(strip_tags((string) $raw['preferred_date'])) : '';
    $preferred_time = isset($raw['preferred_time']) ? trim(strip_tags((string) $raw['preferred_time'])) : '';
    $vitrine_slug = isset($raw['vitrine_slug']) ? trim(strip_tags((string) $raw['vitrine_slug'])) : '';
    $vitrine_title = isset($raw['vitrine_title']) ? trim(strip_tags((string) $raw['vitrine_title'])) : '';
    $site_url = isset($raw['site_url']) ? trim(strip_tags((string) $raw['site_url'])) : '';
    $site_url = preg_replace('/[\r\n]+/', '', $site_url);
    $billing_address = isset($raw['billing_address']) ? trim(strip_tags((string) $raw['billing_address'])) : '';

    if ($preferred_date !== '' && !preg_match('/^\d{4}-\d{2}-\d{2}$/', $preferred_date)) {
        $preferred_date = '';
    }
    if (strlen($preferred_time) > 48) {
        $preferred_time = substr($preferred_time, 0, 48);
    }
    if ($budget !== '' && strlen($budget) > 32) {
        $budget = substr($budget, 0, 32);
    }

    $errors = [];
    $audit_flow_services = ['audit_gratuit_site', 'audit_paid_complet_ia'];
    $is_audit_flow = in_array($service, $audit_flow_services, true);

    if ($name === '' && !$is_audit_flow) {
        $errors[] = 'Le nom est obligatoire.';
    }

    if ($email === '') {
        $errors[] = 'L\'email est obligatoire.';
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = 'L\'email n\'est pas valide.';
    }

    foreach ([$name, $email, $phone] as $fieldVal) {
        if (preg_match("/[\r\n]/", (string) $fieldVal)) {
            $errors[] = 'Données invalides.';
            break;
        }
    }

    if (preg_match('/https?:\/\/|www\./i', $name) || preg_match('/https?:\/\/|www\./i', $phone)) {
        $errors[] = 'Entrée invalide.';
    }

    if ($message === '' && !$is_audit_flow) {
        $errors[] = 'Le message est obligatoire.';
    }

    if ($is_audit_flow) {
        if ($name === '') {
            $name = 'Demandeur audit';
        }
        if ($message === '') {
            $message = 'Demande audit site web (voir URL ci-dessous).';
        }
    }

    if ($project_type === '' || !in_array($project_type, contact_allowed_need_categories(), true)) {
        $errors[] = 'Le besoin principal est obligatoire.';
    }

    if ($service === '') {
        $errors[] = 'La prestation est obligatoire.';
    } elseif (!preg_match('/^[a-z0-9_]{1,80}$/', $service)) {
        $errors[] = 'Prestation invalide.';
    }

    $vitrine_flow_services = ['vitrine_catalog_order', 'vitrine_catalog_devis'];

    if (in_array($service, $vitrine_flow_services, true)) {
        if ($vitrine_slug === '' || !preg_match('/^[a-z0-9-]{1,80}$/', $vitrine_slug)) {
            $errors[] = 'Référence du modèle manquante ou invalide.';
        }
        if ($vitrine_title === '' || strlen($vitrine_title) > 220) {
            $errors[] = 'Titre du modèle manquant ou trop long.';
        }
        if ($site_url !== '') {
            if (strlen($site_url) > 500) {
                $errors[] = 'URL du site trop longue.';
            } else {
                $site_url = contact_normalize_site_url($site_url);
                if (!filter_var($site_url, FILTER_VALIDATE_URL)) {
                    $errors[] = 'URL du site invalide.';
                }
            }
        }
        if ($service === 'vitrine_catalog_order' && strlen($billing_address) < 8) {
            $errors[] = 'Adresse de facturation trop courte.';
        }
        if (strlen($billing_address) > 1500) {
            $errors[] = 'Adresse de facturation trop longue.';
        }
    } elseif (in_array($service, $audit_flow_services, true)) {
        $vitrine_slug = '';
        $vitrine_title = '';
        $billing_address = '';
        if ($site_url === '') {
            $errors[] = 'L\'URL de votre site est obligatoire pour l\'audit gratuit.';
        } elseif (strlen($site_url) > 500) {
            $errors[] = 'URL du site trop longue.';
        } else {
            $site_url = contact_normalize_site_url($site_url);
            if (!filter_var($site_url, FILTER_VALIDATE_URL)) {
                $errors[] = 'URL du site invalide.';
            }
        }
    } else {
        $vitrine_slug = '';
        $vitrine_title = '';
        $site_url = '';
        $billing_address = '';
    }

    return [
        'errors' => $errors,
        'data' => [
            'name' => $name,
            'email' => $email,
            'phone' => $phone,
            'service' => $service,
            'project_type' => $project_type,
            'budget' => $budget,
            'message' => $message,
            'preferred_date' => $preferred_date,
            'preferred_time' => $preferred_time,
            'vitrine_slug' => $vitrine_slug,
            'vitrine_title' => $vitrine_title,
            'site_url' => $site_url,
            'billing_address' => $billing_address,
        ],
    ];
}
