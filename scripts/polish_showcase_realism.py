# -*- coding: utf-8 -*-
"""Remplace ton « démo / fictif » des vitrines showcase par un ton crédible (noms, contacts)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHOWCASE = ROOT / "showcase"


def strip_fictif_markers(html: str) -> str:
    html = re.sub(r"\s*\(fictifs?\)", "", html, flags=re.IGNORECASE)
    html = re.sub(r"\s*\(fictives?\)", "", html, flags=re.IGNORECASE)
    return html


def normalize_typography(html: str) -> str:
    """Apostrophes typographiques → ASCII pour matcher les remplacements."""
    return html.replace("\u2019", "'").replace("\u2018", "'")


# Remplacements ordonnés (les chaînes les plus longues en premier quand pertinent)
SECTOR_PAIRS: dict[str, list[tuple[str, str]]] = {
    "technologie": [
        (
            "NovaStack imagine une suite d’outils pour PME innovantes&nbsp;: API fictives, tableaux de bord de démonstration et automatisations décrites sans aucune obligation contractuelle. Cette page sert à valider hiérarchie typographique, contrastes sur fond sombre, grilles de cartes et formulaires accessibles au clavier.",
            "Synapse Lorraine conçoit des outils métiers pour PME et collectivités&nbsp;: API documentées, tableaux de bord opérationnels et automatisation des flux. Cette page illustre la hiérarchie typographique, les contrastes sur fond sombre et les formulaires accessibles au clavier.",
        ),
        (
            "Nous détaillons ici un discours «&nbsp;produit&nbsp;» volontairement long&nbsp;: livraisons incrémentales simulées, ateliers de cadrage avec parties prenantes inventées, documentation générée pour remplir les colonnes et vérifier le confort de lecture sur plusieurs paragraphes successifs avant les sections techniques.",
            "Nous détaillons ici une approche produit progressive&nbsp;: livraisons incrémentales, ateliers de cadrage avec vos équipes et documentation vivante, pour garder une lecture fluide sur plusieurs paragraphes avant les sections techniques.",
        ),
        (
            "<span>Audit stack &amp; migration Kubernetes (maquette)</span>",
            "<span>Audit stack &amp; migration Kubernetes</span>",
        ),
        (
            "Aucune prestation réelle — parcours graphique pour portfolio.",
            "Échange sous 48&nbsp;h ouvrées — premier diagnostic offert.",
        ),
        (
            "Trois piliers pour structurer la vitrine&nbsp;: plateforme, données et sécurité. Chaque carte résume un positionnement marketing imaginaire, avec des bénéfices rédigés pour tester les intitulés longs et les listes à puces dans les pages suivantes.",
            "Trois piliers pour structurer l’offre&nbsp;: plateforme, données et sécurité. Chaque carte résume un positionnement concret, avec des bénéfices lisibles et des listes à puces adaptées aux pages suivantes.",
        ),
        (
            "Gateway fictive, quotas démo, journaux centralisés imaginaires. Idéal pour captures d’écran de cartes homogènes.",
            "Passerelle sécurisée, quotas configurables et journaux centralisés. Idéal pour industrialiser vos intégrations.",
        ),
        (
            "Pipelines batch et streaming nommés pour l’exemple graphique — aucun jeu de données réel n’est exposé.",
            "Pipelines batch et streaming orchestrés — jeux de données d’essai anonymisés sur demande.",
        ),
        (
            "MFA, SSO et rôles RBAC simulés pour illustrer une offre cybersécurité sur maquette statique.",
            "MFA, SSO et rôles RBAC pour sécuriser l’accès aux applications et aux données sensibles.",
        ),
        (
            "Transparence (fictif)",
            "Transparence &amp; delivery",
        ),
        (
            "<p>NovaStack s’engage, dans cette démo, à décrire des pratiques de delivery alignées sur des standards imaginaires&nbsp;: revue de code systématique inventée, pairs fictifs et rituels de rétrospective hebdomadaire simulés.</p>",
            "<p>Synapse Lorraine applique des pratiques de delivery alignées sur des standards reconnus&nbsp;: revue de code systématique, binômage et rituels de rétrospective hebdomadaire.</p>",
        ),
        (
            "<p>Deuxième paragraphe pour allonger le bloc central&nbsp;: la qualité de service affichée ici ne correspond à aucun SLA réel. Les jalons, indicateurs et barres de progression servent uniquement de repères visuels pour les recettes CSS et les captures Playwright.</p>",
            "<p>Les jalons et indicateurs ci-dessous sont indicatifs&nbsp;: ils illustrent un pilotage projet type et peuvent être adaptés à votre contrat de service.</p>",
        ),
        (
            "Mise en œuvre continue fictive&nbsp;: pipelines GitOps imaginaires, environnements dupliqués en texte, politiques de nommage inventées pour remplir l’espace sans promesse commerciale.",
            "Mise en œuvre continue&nbsp;: pipelines GitOps, environnements dupliqués et politiques de nommage homogènes pour sécuriser les livraisons.",
        ),
        (
            "<strong>Avancement pilote interne (démo)</strong>",
            "<strong>Avancement pilote client</strong>",
        ),
        (
            "Branches, revues et merges décrits pour la maquette.",
            "Branches, revues et merges suivis dans votre forge Git.",
        ),
        (
            "Traces, métriques et budgets d’erreurs simulés.",
            "Traces, métriques et budgets d’erreurs suivis en production.",
        ),
        (
            "<th><i class=\"fa-solid fa-clock mr-2\" aria-hidden=\"true\"></i>Durée fictive</th>",
            "<th><i class=\"fa-solid fa-clock mr-2\" aria-hidden=\"true\"></i>Durée indicative</th>",
        ),
        (
            "<tr><td>Run</td><td>MCO + astreinte imaginaire</td><td>12 mois</td></tr>",
            "<tr><td>Run</td><td>MCO + astreinte planifiée</td><td>12 mois</td></tr>",
        ),
        (
            "<strong>Hébergement&nbsp;?</strong> Région fictive, aucun datacenter réel.",
            "<strong>Hébergement&nbsp;?</strong> Région UE au choix (France / Benelux) selon vos contraintes.",
        ),
        (
            "<strong>RGPD&nbsp;?</strong> Texte placeholder — pas de DPA.",
            "<strong>RGPD&nbsp;?</strong> DPA et registre des traitements fournis avec l’offre entreprise.",
        ),
        (
            "Demande de démo (fictif)",
            "Demande de démo",
        ),
        (
            "<span>Envoyer (démo)</span>",
            "<span>Envoyer</span>",
        ),
        (
            "Whitepaper «&nbsp;Edge &amp; 5G&nbsp;» (PDF fictif)",
            "Livre blanc «&nbsp;Edge &amp; 5G&nbsp;»",
        ),
        (
            "contact@novastack57-demo.local",
            "contact@synapse-lorraine.fr",
        ),
        (
            "Parc Techno fictif, 57000 Ville-Démo",
            "4 parc des Hauts-de-Briey, 57950 Montigny-lès-Metz",
        ),
        (
            "<span>Hub des démos</span>",
            "<span>Index des vitrines</span>",
        ),
        (
            "Vitrine fictive.",
            "Éditeur logiciel — implantation Grand Est.",
        ),
        ("NovaStack Labs 57", "Synapse Lorraine"),
        ("Démo fictive — éditeur logiciel &amp; cloud.", "Éditeur logiciel, API et cloud — présentation."),
        ("image générée", "visuel d’ambiance"),
        (" (démo)", ""),
    ],
    "banque": [
        (
            "Offres, tarifs et témoignages inventés — aucun agrément bancaire, maquette portfolio uniquement.",
            "Offres indicatives et témoignages anonymisés — demandez une proposition personnalisée en agence.",
        ),
        (
            "Agence pilote (fictif)",
            "Agence pilote Metz",
        ),
        (
            "Ouvrir un compte «&nbsp;Horizon&nbsp;» (maquette)",
            "Ouvrir un compte «&nbsp;Horizon&nbsp;»",
        ),
        (
            "Parcours fictif — boutons pour valider les CTA sur fond institutionnel.",
            "Parcours guidé — nos conseillers complètent votre dossier en agence.",
        ),
        (
            "0800 000 000 (fictif)",
            "03 87 18 42 60",
        ),
        (
            "Espace sécurisé — démo",
            "Espace client sécurisé",
        ),
        (
            "Banque des Vosges du Nord — Finance (fictif)",
            "Verlaine Banque Régionale — Finance",
        ),
        (
            "Banque des Vosges du Nord",
            "Verlaine Banque Régionale",
        ),
        (
            "Démo fictive — banque régionale.",
            "Banque régionale — présentation des offres.",
        ),
        ("accueil@bvdn-demo.local", "accueil@verlaine-banque.fr"),
        ("Ville-Démo", "Metz"),
        ("57000 Ville-Démo", "57000 Metz"),
    ],
    "automobile": [
        (
            "Delta Moteurs est un garage fictif&nbsp;: mécaniciens inventés, équipements imaginaires et tarifs indicatifs pour captures d’écran. Aucune intervention réelle n’est planifiée via ce site statique.",
            "Garage Central Plappeville accueille particuliers et professionnels&nbsp;: mécanique générale, pneumatiques et carrosserie. Tarifs indicatifs&nbsp;; devis gratuit sur rendez-vous.",
        ),
        (
            "Ce bloc prolonge le message avec des engagements qualité simulés (contrôle visuel inventé, essai routier fictif, garantie pièces graphique) et une mention de flotte entreprise imaginaire pour tester le texte sur fond graphite.",
            "Contrôle visuel systématique, essai routier après réparation et garantie pièces et main-d’œuvre. Flotte entreprise&nbsp;: planning d’entretien et véhicule de courtoisie sur demande.",
        ),
        (
            "Contrôle technique partenaire (fictif)",
            "Contrôle technique partenaire",
        ),
        (
            "Expertise &amp; carrosserie (fictif)",
            "Expertise &amp; carrosserie",
        ),
        (
            "Rendez-vous (fictif)",
            "Prendre rendez-vous",
        ),
        (
            "<p>Paragraphe long sur la méthode de diagnostic imaginaire&nbsp;: prise en charge prioritaire simulée, prêt véhicule fictif et historique d’interventions rédigé pour la démo.</p>",
            "<p>Diagnostic prioritaire pour les véhicules immobilisés, prêt véhicule selon disponibilité et historique d’interventions consultable à l’atelier.</p>",
        ),
        (
            "<p class=\"is-size-5\">Devis imaginaire, peinture fictive, cabine de séchage simulée.</p>",
            "<p class=\"is-size-5\">Devis photo, peinture bi-couche et cabine de séchage contrôlée.</p>",
        ),
        (
            "<p class=\"is-size-5\">Contrats entreprise inventés, planning d’entretien graphique.</p>",
            "<p class=\"is-size-5\">Contrats entreprise, planning d’entretien et relevé kilométrique.</p>",
        ),
        (
            "atelier@delta-moteurs-demo.local",
            "garage@central-plappeville.fr",
        ),
        ("ZI fictive", "ZI Actipôle, 57140 Norroy-le-Veneur"),
        ("Garage Delta Moteurs — Automobile (fictif)", "Garage Central Plappeville — Automobile"),
        ("Delta Moteurs", "Garage Central"),
        ("<p class=\"is-size-6 has-text-grey-light\">Fictif.</p>", "<p class=\"is-size-6 has-text-grey-light\">Grand Est.</p>"),
        ("Démo fictive — garage &amp; atelier.", "Garage, atelier mécanique et carrosserie."),
    ],
    "chocolatier": [
        (
            "Tablettes, pralinés et ateliers — tout est fictif pour démo portfolio. Cadres larges, prix lisibles.",
            "Tablettes, pralinés et ateliers découverte. Cadres larges, origines lisibles et prix nets.",
        ),
        (
            "Raisin, amande, sel de Guérande fictif.",
            "Raisin, amande, sel de Guérande AOP.",
        ),
        (
            "Lots numérotés fictifs, traçabilité simulée.",
            "Lots numérotés, traçabilité fèves et températures conservées.",
        ),
        (
            "Quatre tablettes « démo » : Madagascar, Pérou, Haïti, Papouasie (noms fictifs).",
            "Quatre tablettes permanentes&nbsp;: Madagascar, Pérou, Haïti, Papouasie.",
        ),
        (
            "«&nbsp;Mendiants équilibrés — avis fictif.&nbsp;»",
            "«&nbsp;Mendiants équilibrés, cacao franc et fruits secs au top.&nbsp;»",
        ),
        (
            "Coffrets sur mesure (fictif)",
            "Coffrets sur mesure",
        ),
        (
            "Lun–Sam 10h–19h · 03 00 00 00 42 (fictif)",
            "Lun–Sam 10h–19h · 03 87 32 18 90",
        ),
        (
            "Maison Cacao &amp; Fleur — Chocolatier (fictif)",
            "Chocolaterie Vialson — Chocolatier",
        ),
        ("Maison Cacao &amp; Fleur", "Chocolaterie Vialson"),
        ("Démo fictive — chocolatier artisanal.", "Chocolatier artisanal — boutique &amp; ateliers."),
        ("Vitrine de démonstration.", "Maison fondée à Metz."),
        (" (démo)", ""),
        ("imaginaires", "indicatifs"),
    ],
    "commerce": [
        (
            "Marché Express est une enseigne fictive mêlant circuits courts imaginaires, drive simulé et comptoir traiteur graphique. Les producteurs cités sont inventés pour habiller les fiches rayon sans lien avec une exploitation réelle.",
            "Les Halles Thionville regroupent primeurs, drive express et comptoir traiteur. Les producteurs partenaires sont sélectionnés sur la semaine et affichés en rayon.",
        ),
        (
            "Ce paragraphe complète le hero avec un discours «&nbsp;commerce de proximité&nbsp;»&nbsp;: rotation des étals simulée, politique anti-gaspillage rédigée pour la maquette et engagements RSE purement illustratifs pour tester la longueur de texte sur fond vert.",
            "Rotation des étals chaque matin, politique anti-gaspillage avec dons aux associations locales et engagements RSE affichés en magasin.",
        ),
        (
            "Trois univers pour varier les cartes et les icônes&nbsp;: frais, bio et cave. Les descriptions reprennent un ton marché couvert imaginaire, avec des références de saison inventées.",
            "Trois univers pour parcourir le magasin&nbsp;: frais, bio et cave. Descriptifs de saison et arrivages du jour.",
        ),
        (
            "<p>Sélection imaginaire sans vente en ligne.</p>",
            "<p>Sélection en magasin&nbsp;; commande drive sur l’app partenaire.</p>",
        ),
        (
            "<p>Nous développons ici un texte long sur les partenariats imaginaires avec producteurs de la région fictive, les tournées de livraison simulées et les actions solidaires inventées pour la maquette.</p>",
            "<p>Partenariats avec producteurs lorraines, tournées de livraison matinales et actions solidaires avec les associations du quartier.</p>",
        ),
        (
            "Retrait drive sous 2&nbsp;h (scénario fictif)",
            "Retrait drive sous 2&nbsp;h",
        ),
        (
            "Engagement local (fictif)",
            "Engagement local",
        ),
        (
            "Carte fidélité (fictif)",
            "Carte fidélité Halles",
        ),
        ("accueil@marche-express-demo.local", "contact@halles-thionville.fr"),
        ("Marché Express", "Halles Thionville"),
        ("Quartier Marché Express — Commerce (fictif)", "Les Halles Thionville — Commerce"),
        ("<p class=\"is-size-6\">Fictif.</p>", "<p class=\"is-size-6\">Thionville.</p>"),
        ("Démo fictive — commerce &amp; drive.", "Commerce de proximité et drive."),
    ],
    "restauration": [
        (
            "Le Bistro Ligne &amp; Comptoir est une fiction gastronomique&nbsp;: chef inventé, fournisseurs imaginaires et carte renouvelée pour les besoins graphiques du portfolio. Aucune réservation ne déclenche de service réel.",
            "La Brasserie Saint-Jacques propose une cuisine de marché au cœur de Metz. Carte renouvelée chaque semaine, réservations conseillées le week-end.",
        ),
        (
            "Nous détaillons ici une ambiance «&nbsp;bistronomie&nbsp;» simulée&nbsp;: produits du marché décrits sans origine vérifiable, accord mets-vins fictif et terrasse ombragée inventée pour enrichir le texte du hero et valider les contrastes sur fond bordeaux.",
            "Ambiance bistronomique, produits du marché lorrain, accords mets-vins au verre et terrasse ombragée place Saint-Jacques.",
        ),
        (
            "Menu déjeuner «&nbsp;comptoir&nbsp;» (offre maquette)",
            "Menu déjeuner «&nbsp;comptoir&nbsp;»",
        ),
        (
            "Le tableau suivant condense des plats imaginaires pour tester les largeurs de colonnes et les alignements de prix. Les montants sont indicatifs et sans valeur commerciale.",
            "Exemple de carte midi&nbsp;; les montants sont indicatifs et peuvent varier selon arrivages.",
        ),
        (
            "<tr><td>Velouté</td><td>Courge, huile noisette imaginaire</td><td>9&nbsp;€</td></tr>",
            "<tr><td>Velouté</td><td>Courge, huile de noisette toastée</td><td>9&nbsp;€</td></tr>",
        ),
        (
            "<tr><td>Poisson</td><td>Filet, citron confit fictif</td><td>26&nbsp;€</td></tr>",
            "<tr><td>Poisson</td><td>Filet, citron confit maison</td><td>26&nbsp;€</td></tr>",
        ),
        (
            "Le savoir-faire (fictif)",
            "Le savoir-faire",
        ),
        (
            "Réservation (fictif)",
            "Réservation",
        ),
        (
            "<p>Paragraphe long&nbsp;: la brigade imaginaire travaille des produits bruts décrits pour la démo, avec une cuisine ouverte simulée et un comptoir fromager inventé. Les alliances de saveurs sont rédigées pour le style, pas pour un menu réel.</p>",
            "<p>Brigade en cuisine ouverte, produits bruts travaillés le jour même et comptoir fromager avec sélection affineur. Les alliances de saveurs suivent les saisons.</p>",
        ),
        (
            "03 00 00 00 77 (fictif) · ",
            "03 87 74 22 31 · ",
        ),
        ("resa@ligne-comptoir-demo.local", "resa@brasserie-saint-jacques.fr"),
        ("Bistro Ligne &amp; Comptoir — Restauration (fictif)", "Brasserie Saint-Jacques — Restauration"),
        ("Bistro Ligne &amp; Comptoir", "Brasserie Saint-Jacques"),
        ("Démo fictive — restaurant &amp; cave.", "Restaurant, cave et réservations."),
    ],
    "education": [
        (
            "Campus Lumière est un organisme de formation entièrement fictif&nbsp;: modules, formateurs et certifications cités sur ce site n’existent pas. L’objectif est de montrer une arborescence pédagogique claire avec tableaux, inscriptions et visuels générés.",
            "L’Institut Mercure propose des parcours certifiants et inter-entreprises en Grand Est. Modules, formateurs et certifications listés ci-dessous sont indicatifs&nbsp;: contactez-nous pour le catalogue à jour.",
        ),
        (
            "Ce second bloc de texte décrit un parcours apprenant imaginaire, avec socle commun simulé, ateliers pratiques inventés et évaluation finale graphique. Aucun financement CPF réel n’est proposé ici.",
            "Parcours apprenant avec socle commun, ateliers pratiques et évaluation finale. Éligibilité CPF selon dossier&nbsp;: nos conseillers vous orientent.",
        ),
        (
            "Session «&nbsp;Data literacy&nbsp;» — calendrier fictif",
            "Session «&nbsp;Data literacy&nbsp;» — calendrier",
        ),
        (
            "<tr><td>Excel avancé</td><td>3 jours</td><td>Présentiel fictif</td></tr>",
            "<tr><td>Excel avancé</td><td>3 jours</td><td>Présentiel Metz</td></tr>",
        ),
        (
            "<tr><td>Green IT</td><td>1 jour</td><td>Hybride imaginaire</td></tr>",
            "<tr><td>Green IT</td><td>1 jour</td><td>Hybride</td></tr>",
        ),
        (
            "Schéma fictif outils pédagogiques",
            "Schéma outils pédagogiques",
        ),
        (
            "<p>Paragraphe dense&nbsp;: positionnement SOC fictif, évaluations formatives simulées, LMS imaginaire et badges numériques sans valeur certificateur. Ce bloc teste la lecture sur fond clair avec encadré accent or.</p>",
            "<p>Positionnement sécurité SOC, évaluations formatives, plateforme LMS et badges numériques associés aux modules validés.</p>",
        ),
        (
            "<p>Nous ajoutons un second paragraphe sur les ressources pédagogiques inventées (vidéos, fiches et quiz) pour valider l’interlignage et les listes à puces dans une même colonne centrée.</p>",
            "<p>Ressources pédagogiques&nbsp;: vidéos, fiches et quiz accessibles pendant et après la formation.</p>",
        ),
        (
            "Équipe fictive, CV d’exemple et domaines de spécialité inventés.",
            "Équipe permanente et intervenants externes, CV et domaines de spécialité détaillés en amont.",
        ),
        (
            "Pré-inscription (fictif)",
            "Pré-inscription",
        ),
        ("formation@campus-lumiere-demo.local", "formations@media-mercure.fr"),
        ("Campus Lumière Académie — Éducation (fictif)", "Institut Mercure — Éducation &amp; formation"),
        ("Campus Lumière", "Institut Mercure"),
        ("Démo fictive — organisme de formation.", "Organisme de formation — catalogue &amp; inscriptions."),
        ("image générée", "photo pédagogie"),
        (" (démo)", ""),
        ("<p class=\"is-size-6\">Fictif.</p>", "<p class=\"is-size-6\">Metz.</p>"),
    ],
    "etablissement": [
        (
            "Nous développons ici une promesse d’expérience imaginaire&nbsp;: petit-déjeuner buffet simulé, conciergerie inventée et partenariats culturels fictifs pour allonger le texte du hero sur fond sombre chaud.",
            "Petit-déjeuner buffet, conciergerie 7j/7 et partenariats culturels avec les institutions du centre historique.",
        ),
        (
            "Literie imaginaire, plateau courtoisie fictif.",
            "Literie haut de gamme, plateau courtoisie et sélection de thés.",
        ),
        (
            "Expérience hôte (fictif)",
            "Expérience hôte",
        ),
        (
            "<p>Paragraphe long&nbsp;: spa imaginaire avec piscine à jets dessinée, sauna finlandais fictif et rituels massages inventés pour remplir la colonne centrale sans promesse thérapeutique.</p>",
            "<p>Espace bien-être avec bassin à jets, sauna finlandais et rituels massages bien-être sur réservation (non médicaux).</p>",
        ),
        (
            "Réservation (fictif)",
            "Réservation",
        ),
        ("booking@hotel-arcades-demo.local", "reservations@stanislas-collection.fr"),
        ("Hôtel des Arcades &amp; Spa — Établissement (fictif)", "Hôtel Stanislas Collection — Établissement"),
        ("Hôtel des Arcades", "Hôtel Stanislas Collection"),
        ("<p class=\"is-size-6 has-text-grey-light\">Fictif.</p>", "<p class=\"is-size-6 has-text-grey-light\">Nancy.</p>"),
        ("Démo fictive — hôtel &amp; spa.", "Hôtel 4&nbsp;étoiles, spa et séminaires."),
    ],
    "beaute": [
        (
            "institut@eclat-pur-demo.local",
            "bonjour@spa-thalie.fr",
        ),
        ("Maison Éclat Pur — Beauté (fictif)", "Spa Thalie — Beauté &amp; bien-être"),
        ("Maison Éclat Pur", "Spa Thalie"),
        ("Démo fictive — institut &amp; spa.", "Institut, spa et soins sur rendez-vous."),
        ("<p class=\"is-size-6\">Fictif.</p>", "<p class=\"is-size-6\">Metz centre.</p>"),
    ],
    "odontologie": [
        (
            "Soins, esthétique et urgences — grille et praticiens entièrement fictifs.",
            "Soins conservateurs, esthétique et urgences du jour — équipe à taille humaine.",
        ),
        (
            "<p><strong>Urgences</strong> · 15h – 17h (fictif)</p>",
            "<p><strong>Urgences</strong> · 15h – 17h (créneaux dédiés)</p>",
        ),
        (
            "<strong>Rappel RDV préventif (fictif)</strong>",
            "<strong>Rappel RDV préventif</strong>",
        ),
        (
            "<tr><td>Couronne</td><td>Zircone, 10 jours fictifs</td><td>780&nbsp;€</td></tr>",
            "<tr><td>Couronne</td><td>Zircone, 10 jours ouvrés</td><td>780&nbsp;€</td></tr>",
        ),
        (
            "Scellement — <strong>28&nbsp;€</strong> / dent (fictif).",
            "Scellement — <strong>28&nbsp;€</strong> / dent.",
        ),
        (
            "Demander un rappel (fictif)",
            "Demander un rappel",
        ),
        (
            "«&nbsp;Urgence : rappel rapide (fictif).&nbsp;»",
            "«&nbsp;Urgence traitée le jour même, équipe réactive.&nbsp;»",
        ),
        (
            "Être rappelé (fictif)",
            "Être rappelé",
        ),
        (
            "placeholder=\"Matin / après-midi (fictif)\"",
            "placeholder=\"Matin / après-midi\"",
        ),
        (
            "03 00 00 00 00 (fictif)",
            "03 87 65 12 40",
        ),
        ("contact@sourire-lorraine-demo.local", "accueil@dentaires-mosaique.fr"),
        ("Cabinet Sourire Lorraine — Odontologie (fictif)", "Centre dentaire Mosaïque — Odontologie"),
        ("Cabinet Sourire Lorraine", "Centre dentaire Mosaïque"),
        ("Démo fictive — cabinet dentaire.", "Cabinet dentaire — soins et parcours patient."),
        ("placeholder=\"06 00 00 00 00\"", "placeholder=\"06 12 34 56 78\""),
    ],
    "services": [
        ("contact@hexa-services-demo.local", "accueil@proprio-facility.fr"),
        ("Hexa Services — Services (fictif)", "Proprio Facility — Services aux entreprises"),
        ("Hexa Services", "Proprio Facility"),
        ("Démo fictive — services &amp; facility.", "Facility management et conciergerie d’entreprise."),
    ],
    "industrie": [
        (
            "*certification imaginaire",
            "*certifications selon procédé",
        ),
        (
            "Acer 42CrMo4, inox 316L, alu 7075 — références inventées. 4&nbsp;500&nbsp;m² imaginaires, deux lignes CN, cellule climatisée fictive.",
            "Acer 42CrMo4, inox 316L, alu 7075 — références courantes. 4&nbsp;500&nbsp;m², deux lignes CN, cellule climatisée.",
        ),
        (
            "Section longue pour tester contrastes sur fond sombre&nbsp;: flux matière imaginaire, ordres de fabrication fictifs, indicateurs OEE d’exemple et revues outils simulées. Les photographies ci-dessous (soudure, plan sur établi) complètent les rendus déjà présents sur la page.",
            "Flux matière, ordres de fabrication, indicateurs OEE et revues outils suivis chaque semaine. Photographies atelier&nbsp;: soudure TIG et lecture de plan sur établi.",
        ),
        (
            "Parc machines inventé — pas de capacité réelle.",
            "Parc machines documenté sur devis — capacités selon planning charge.",
        ),
        (
            "Message Bulma sur fond sombre — rappel que toutes les certifications et tolérances sont imaginaires.",
            "Certifications et tolérances contractuelles précisées sur bon de commande.",
        ),
        (
            "Lancement fictif, kitting, contrôle intermédiaire.",
            "Lancement série, kitting, contrôle intermédiaire.",
        ),
        (
            "Ø max fictif 420&nbsp;mm.",
            "Ø max 420&nbsp;mm.",
        ),
        (
            "«&nbsp;Série 250 nickel — communication à renforcer (fictif).&nbsp;»",
            "«&nbsp;Série 250 nickel — très bon suivi qualité.&nbsp;»",
        ),
        (
            "Dépôt fictif — aucune CAO réelle traitée.",
            "Dépôt sécurisé — traitement CAO sous NDA.",
        ),
        (
            "placeholder=\"Cotes, finitions… (fictif)\"",
            "placeholder=\"Cotes, finitions…\"",
        ),
        (
            "Demander une étude (fictif)",
            "Demander une étude",
        ),
        (
            "Demander un chiffrage (fictif)",
            "Demander un chiffrage",
        ),
        (
            "Devis express (fictif)",
            "Devis express",
        ),
        ("contact@mecano-precision54-demo.local", "devis@precisite.fr"),
        ("Atelier Mécano-Precision 54 — Industrie (fictif)", "Précisite Usinage — Industrie"),
        ("Atelier Mécano-Precision 54", "Précisite Usinage"),
        ("Démo fictive — usinage &amp; mécano-soudure.", "Usinage de précision et mécano-soudure."),
    ],
    "comptable": [
        (
            "TPE / PME jusqu’à 15 salariés — cibles et associés entièrement fictifs.",
            "TPE / PME jusqu’à 15 salariés — accompagnement sur-mesure.",
        ),
        (
            "Six collaborateurs inventés, deux associés fictifs, charte qualité graphique.",
            "Six collaborateurs, deux associés, charte qualité certifiée.",
        ),
        (
            "Paragraphe dense pour valider la grille éditoriale&nbsp;: diagnostic fictif, mapping des flux financiers inventés, calendrier fiscal d’exemple et points de contrôle internes simulés. Les visuels combinent une photo «&nbsp;bureau comptable&nbsp;» et un croquis type dessin technique pour varier les tons.",
            "Diagnostic initial, mapping des flux financiers, calendrier fiscal et points de contrôle interne. Visuels&nbsp;: ambiance cabinet et schéma de processus.",
        ),
        (
            "<strong>DSN à jour (fictif)</strong>",
            "<strong>DSN à jour</strong>",
        ),
        (
            "Forfaits (fictifs)",
            "Forfaits",
        ),
        (
            "Demander un bilan flash (fictif)",
            "Demander un bilan flash",
        ),
        (
            "Bilan flash — prise de contact (fictif)",
            "Bilan flash — prise de contact",
        ),
        (
            "<label class=\"label\" for=\"bf-siren\">SIREN (fictif)</label>",
            "<label class=\"label\" for=\"bf-siren\">SIREN</label>",
        ),
        (
            "<label class=\"label\" for=\"bf-file\">Dernier bilan (fictif)</label>",
            "<label class=\"label\" for=\"bf-file\">Dernier bilan</label>",
        ),
        (
            "Planifier un échange (fictif)",
            "Planifier un échange",
        ),
        (
            "03 00 00 00 01 (fictif)",
            "03 83 35 28 90",
        ),
        ("contact@bilan-carre-demo.local", "cabinet@verlaine-associes.fr"),
        ("Bilan Carré Experts — Comptabilité (fictif)", "Verlaine &amp; Associés — Comptabilité"),
        ("Bilan Carré Experts", "Verlaine &amp; Associés"),
        ("Démo fictive — cabinet comptable.", "Cabinet d’expertise comptable et de conseil."),
    ],
    "association": [
        (
            "Maraude, jeunesse, cuisines solidaires — contenu entièrement fictif pour maquette portfolio.",
            "Maraude, jeunesse et cuisines solidaires au service des quartiers de Metz et alentours.",
        ),
        (
            "Aucune inscription réelle — boutons de maquette pour tester les CTA.",
            "Inscription bénévoles en ligne ou sur place lors des permanences.",
        ),
        (
            "Trois blocs larges pour tester la lisibilité : chiffres inventés, aucune permanence réelle.",
            "Trois axes d’action avec chiffres issus du rapport d’activité consolidé.",
        ),
        (
            "Environ 120 repas chauds / semaine (exemple). Fourgons et tournées imaginaires.",
            "Environ 120 repas chauds / semaine. Fourgons équipés et tournées planifiées.",
        ),
        (
            "18 collégiens suivis, deux séances hebdomadaires, matériel fourni (fictif).",
            "18 collégiens suivis, deux séances hebdomadaires, matériel fourni par la collectivité.",
        ),
        (
            "Simulations d’entretiens sur six mois — partenaires et emplois inventés.",
            "Accompagnement vers l’emploi sur six mois avec partenaires locaux.",
        ),
        (
            "Schéma fictif entraide",
            "Schéma entraide",
        ),
        (
            "Campagne hiver (fictif)",
            "Campagne hiver",
        ),
        (
            "Dix repas maraude (fictif)",
            "Dix repas maraude",
        ),
        (
            "Parler à l’équipe (fictif)",
            "Parler à l’équipe",
        ),
        (
            "Objectif&nbsp;: 12&nbsp;000&nbsp;€ symboliques pour couvrir carburant et denrées imaginaires. Les barres ci-dessous illustrent un composant <strong>progress</strong> Bulma.",
            "Objectif&nbsp;: 12&nbsp;000&nbsp;€ pour carburant et denrées de la maraude hivernale. Les barres illustrent l’avancement de la collecte.",
        ),
        (
            "Zones Nord et Est inventées — cartes et données sans lien avec un territoire réel.",
            "Zones Nord et Est de l’agglomération — données indicatives d’occupation.",
        ),
        (
            "Mairies fictives, épiceries solidaires imaginaires, associations sœurs inventées pour remplir la tuile.",
            "Mairies de quartier, épiceries solidaires et associations partenaires du réseau.",
        ),
        (
            "Témoignages (inventés)",
            "Témoignages",
        ),
        (
            "«&nbsp;Briefings clairs avant chaque tournée — tout est simulé pour la maquette.&nbsp;»",
            "«&nbsp;Briefings clairs avant chaque tournée, matériel fiable sur le terrain.&nbsp;»",
        ),
        (
            "Candidature bénévolat (fictif)",
            "Candidature bénévolat",
        ),
        (
            "<strong>Adresse fictive</strong><br>12 rue des Primevères, 57000 Ville-Démo",
            "<strong>Siège</strong><br>22 rue aux Arènes, 57000 Metz",
        ),
        (
            "Besoin d’un partenariat associatif (maquette)&nbsp;?",
            "Besoin d’un partenariat associatif&nbsp;?",
        ),
        (
            "Association et contenus entièrement fictifs.",
            "Association loi 1901 — reçu fiscal sur demande.",
        ),
        ("contact@main-tendue-57-demo.local", "contact@solidarites-metz.fr"),
        ("benevoles@main-tendue-57-demo.local", "benevoles@solidarites-metz.fr"),
        ("Réseau Main Tendue 57 — Association (fictif)", "Solidarités Metz Métropole — Association"),
        ("Réseau Main Tendue 57", "Solidarités Metz Métropole"),
        ("Main Tendue", "Solidarités Metz"),
        ("Démo fictive — association &amp; solidarité.", "Association — solidarité et lien social."),
    ],
}


def polish_hub() -> None:
    path = SHOWCASE / "index.html"
    html = normalize_typography(path.read_text(encoding="utf-8"))
    pairs = [
        ("<title>Démos vitrine — hub (fictif)</title>", "<title>Vitrines sectorielles — portfolio DanielCraft</title>"),
        ('<p class="badge">Contenu fictif</p>', '<p class="badge">Portfolio</p>'),
        (
            "<h1 id=\"hub-title\">Vitrines démo par secteur</h1>",
            "<h1 id=\"hub-title\">Vitrines sectorielles</h1>",
        ),
        (
            "<p class=\"lead\">Catalogue statique de <strong>quatorze</strong> maquettes sectorielles : chaque vitrine applique une <strong>arborescence différente</strong> (libellés de menu et regroupement de contenu) pour coller aux usages WordPress, Joomla ou Bootstrap, tout en restant sur une seule URL pour les captures Playwright (<code>showcase/screenshot_showcases.py</code>). Aucune statistique de marché n’est affichée&nbsp;: uniquement du contenu fictif pour la mise en page.</p>",
            "<p class=\"lead\">Ce catalogue présente <strong>quatorze</strong> vitrines sectorielles statiques&nbsp;: chacune applique une <strong>arborescence différente</strong> (menus, regroupements de contenu) proche des usages WordPress, Joomla ou Bootstrap. Les textes et coordonnées sont rédigés comme sur un site «&nbsp;réel&nbsp;» pour tester lisibilité, contrastes et formulaires.</p>",
        ),
        (
            "<p>NovaStack Labs 57 — SaaS, API et data fictifs&nbsp;: parcours produit, démo et documentation graphique.</p>",
            "<p>Synapse Lorraine — SaaS, API et data&nbsp;: parcours produit, démo et documentation.</p>",
        ),
        (
            "<p>Hexa Services — nettoyage, facility et conciergerie imaginaires pour tester listes et formulaires.</p>",
            "<p>Proprio Facility — nettoyage, facility et conciergerie pour sites tertiaires.</p>",
        ),
        (
            "<p>Bistro Ligne &amp; Comptoir — carte, réservations et événements inventés, photos générées.</p>",
            "<p>Brasserie Saint-Jacques — carte, réservations et événements, visuels d’ambiance.</p>",
        ),
        (
            "<p>Marché Express — drive, rayons et fidélité fictifs, mises en page type grande distribution.</p>",
            "<p>Halles Thionville — drive, rayons et fidélité, mise en page type grande distribution.</p>",
        ),
        (
            "<p>Campus Lumière — catalogue de modules, inscriptions et pédagogie entièrement factices.</p>",
            "<p>Institut Mercure — catalogue de modules, inscriptions et parcours pédagogiques.</p>",
        ),
        (
            "<p>Hôtel des Arcades &amp; Spa — chambres, séminaires et réservation démo sur fond sombre.</p>",
            "<p>Hôtel Stanislas Collection — chambres, séminaires et réservation sur fond sombre.</p>",
        ),
        (
            "<p>Maison Éclat Pur — soins, spa et institut imaginaire avec palette rose et bordeaux.</p>",
            "<p>Spa Thalie — soins, spa et institut, palette rose et bordeaux.</p>",
        ),
        (
            "<p>Garage Delta Moteurs — atelier, pneus et rendez-vous fictifs, style garage premium sombre.</p>",
            "<p>Garage Central Plappeville — atelier, pneus et rendez-vous, style garage premium sombre.</p>",
        ),
        (
            "<p>Maison Cacao &amp; Fleur — logique <strong>commerce</strong> : maison, boutique &amp; dégustations, goûts &amp; avis.</p>",
            "<p>Chocolaterie Vialson — logique <strong>commerce</strong>&nbsp;: maison, boutique &amp; dégustations, goûts &amp; avis.</p>",
        ),
        (
            "<p>Cabinet Sourire Lorraine — fil <strong>patient</strong> : cabinet, soins, parcours &amp; avis.</p>",
            "<p>Centre dentaire Mosaïque — fil <strong>patient</strong>&nbsp;: cabinet, soins, parcours &amp; avis.</p>",
        ),
        (
            "<p>Banque des Vosges du Nord — découpage <strong>institutionnel</strong> : institution, offres, confiance.</p>",
            "<p>Verlaine Banque Régionale — découpage <strong>institutionnel</strong>&nbsp;: institution, offres, confiance.</p>",
        ),
        (
            "<p>Atelier Mécano-Precision 54 — trame <strong>usine</strong> : capacités, prestations, qualité.</p>",
            "<p>Précisite Usinage — trame <strong>usine</strong>&nbsp;: capacités, prestations, qualité.</p>",
        ),
        (
            "<p>Bilan Carré Experts — squelette <strong>cabinet</strong> : le cabinet, expertises, références.</p>",
            "<p>Verlaine &amp; Associés — squelette <strong>cabinet</strong>&nbsp;: le cabinet, expertises, références.</p>",
        ),
        (
            "<p>Réseau Main Tendue 57 — parcours <strong>solidarité</strong> : mission, agir, impact.</p>",
            "<p>Solidarités Metz Métropole — parcours <strong>solidarité</strong>&nbsp;: mission, agir, impact.</p>",
        ),
        (
            "<p>Les chemins relatifs fonctionnent derrière un serveur statique ; les images PNG sont générées ou de démo et ne représentent aucun lieu réel ; les ancres permettent de valider le <code>scroll-margin</code> et la navigation clavier sur les pages longues.</p>",
            "<p>Les chemins relatifs fonctionnent derrière un serveur statique&nbsp;; les visuels sont des illustrations d’ambiance&nbsp;; les ancres valident le <code>scroll-margin</code> et la navigation clavier sur les pages longues.</p>",
        ),
        (
            "<h2 id=\"indicateurs-title\">Indicateurs de couverture (démo)</h2>",
            "<h2 id=\"indicateurs-title\">Indicateurs de couverture</h2>",
        ),
        (
            "<div class=\"hub-kpi\" aria-label=\"Indicateurs fictifs\">",
            "<div class=\"hub-kpi\" aria-label=\"Indicateurs vitrines\">",
        ),
        (
            "<p class=\"hub-contact__p\"><strong>Usage</strong> — démonstrations internes et portfolio uniquement. Aucune donnée réelle à saisir.</p>",
            "<p class=\"hub-contact__p\"><strong>Usage</strong> — démonstrations portfolio. Les formulaires sont statiques&nbsp;; ne saisissez pas de données personnelles sensibles.</p>",
        ),
    ]
    for old, new in pairs:
        ok = normalize_typography(old)
        nv = normalize_typography(new)
        if ok in html:
            html = html.replace(ok, nv)
    html = strip_fictif_markers(html)
    path.write_text(html, encoding="utf-8")


def polish_sectors() -> None:
    for sector, pairs in SECTOR_PAIRS.items():
        path = SHOWCASE / sector / "index.html"
        if not path.is_file():
            raise SystemExit(f"Manquant: {path}")
        html = normalize_typography(path.read_text(encoding="utf-8"))
        for old, new in pairs:
            ok = normalize_typography(old)
            nv = normalize_typography(new)
            if ok in html:
                html = html.replace(ok, nv)
        html = strip_fictif_markers(html)
        path.write_text(html, encoding="utf-8")


def main() -> None:
    polish_hub()
    polish_sectors()
    print("OK — showcase hub +", len(SECTOR_PAIRS), "vitrines.")


if __name__ == "__main__":
    main()
