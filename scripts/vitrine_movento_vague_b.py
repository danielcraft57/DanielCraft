"""Redesign Movento vague B - 8 flagships restants.

Slugs : industrie, education, services, etablissement, technologie,
fitness, banque, gites.

Personnalites distinctes (nav + hero + sections) - plus de clone
bleed/split + grille services partout.
"""
from __future__ import annotations

from vitrine_layouts import (
    block_hero_movento_bleed,
    block_hero_movento_center,
    block_hero_movento_magazine,
    block_hero_movento_split,
    block_movento_bar_nav,
    block_movento_contact,
    block_movento_feature_rows,
    block_movento_menu_list,
    block_movento_pill_nav,
    block_movento_proof,
    block_movento_quote,
    block_movento_services,
    block_movento_stat_band,
    block_movento_steps,
    block_snap_chapter,
)
from vitrine_seo import get_entity
from vitrine_site_blocks import block_mobile_cta, block_site_footer, wrap_page

_BOOT = """
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <link rel="stylesheet" href="../shared/vitrine-prose.css">
  <link rel="stylesheet" href="../shared/vitrine-images.css">
  <link rel="stylesheet" href="../shared/vitrine-motion.css">
  <link rel="stylesheet" href="../shared/vitrine-movento.css">
  <link rel="icon" href="images/icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="stylesheet" href="styles.css">"""

HEAD_SERIF = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
{_BOOT}"""

HEAD_TECH = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
{_BOOT}"""

HEAD_CONDENSED = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Instrument+Serif&display=swap" rel="stylesheet">
{_BOOT}"""


def _fl(nav):
    return [(p["label"], p["file"]) for p in nav]


def _shell(
    *,
    slug,
    brand,
    phone,
    address,
    email,
    maps,
    nav,
    page,
    title,
    desc,
    main,
    cta,
    hours,
    head,
    body_extra,
    layout,
    nav_kind: str = "pill",
):
    if nav_kind == "pill":
        header = block_movento_pill_nav(
            brand, nav, page, cta_label=cta, cta_href="contact.html", phone=phone
        )
    else:
        header = block_movento_bar_nav(
            brand,
            nav,
            page,
            cta_label=cta,
            cta_href="contact.html",
            phone=phone,
            variant=nav_kind,
        )
    foot = block_site_footer(
        brand,
        entity=get_entity(slug),
        slug=slug,
        phone=phone,
        address=address,
        email=email,
        maps_href=maps,
        nav_links=_fl(nav),
        hours_line=hours,
    )
    mobile = block_mobile_cta(cta, "contact.html", phone)
    return wrap_page(
        title,
        desc,
        header + main + foot + mobile,
        layout=layout,
        slug=slug,
        page=page,
        site_name=brand,
        nav=nav,
        head_assets=head,
        body_class=f"vt-body vt-body-movento {body_extra}",
    )


# --- Industrie ---
IN = dict(
    brand="Précisite Usinage",
    phone="03 87 22 44 66",
    email="devis@precisite-usinage.fr",
    address="Zone industrielle des Hauts Champs, 57970 Yutz",
    maps="https://maps.google.com/?q=Yutz+57970",
    nav=[
        {"file": "index.html", "label": "Accueil"},
        {"file": "savoir-faire.html", "label": "Savoir-faire"},
        {"file": "qualite.html", "label": "Qualité"},
        {"file": "contact.html", "label": "Devis"},
    ],
)


def build_industrie_index():
    m = "<main>"
    m += block_hero_movento_magazine(
        "Usinage qui tient les cotes",
        "5 axes, automobile et aéronautique à Yutz - devis express, FAQ qualité.",
        "hero.png",
        "Atelier usinage Yutz",
        eyebrow="Yutz · Moselle",
        primary_href="contact.html",
        primary_label="Demander un devis",
        kicker="Industrie de précision",
    )
    m += block_movento_feature_rows(
        "Ce qu'on livre",
        [
            ("Usinage CNC", "Pièces unitaires et séries - matières courantes.", "card-1.png", "Usinage CNC"),
            ("Contrôle", "Métrologie et PV de conformité.", "card-2.png", "Contrôle qualité"),
            ("Devis RFQ", "Plan + quantité - réponse technique claire.", "card-3.png", "Devis industriel"),
        ],
        lead="Pas de blabla commercial : capacités, délais, preuves.",
    )
    m += block_movento_proof([("5 axes", "CNC"), ("ISO", "contrôles"), ("48 h", "devis type"), ("AO", "prêts")])
    m += block_movento_contact(
        "Devis technique", IN["address"], cta_label="Envoyer", phone=IN["phone"], address=IN["address"]
    )
    m += "</main>"
    return _shell(
        slug="industrie",
        brand=IN["brand"],
        phone=IN["phone"],
        address=IN["address"],
        email=IN["email"],
        maps=IN["maps"],
        nav=IN["nav"],
        page="index.html",
        title=f"{IN['brand']} - Usinage Yutz",
        desc="Usinage de précision Yutz : machines, devis, qualité.",
        main=m,
        cta="Devis",
        hours="Yutz · Industrie",
        head=HEAD_TECH,
        body_extra="vt-mv-industrie",
        layout="movento-industrie",
        nav_kind="solid",
    )


def build_industrie_savoir():
    m = (
        "<main>"
        + block_snap_chapter(
            "Savoir-faire",
            "Tournage, fraisage 5 axes, petits lots.",
            "scene-1.png",
            "Savoir-faire",
            cta_href="contact.html",
            cta_label="Devis",
        )
        + "</main>"
    )
    return _shell(
        slug="industrie",
        brand=IN["brand"],
        phone=IN["phone"],
        address=IN["address"],
        email=IN["email"],
        maps=IN["maps"],
        nav=IN["nav"],
        page="savoir-faire.html",
        title=f"Savoir-faire - {IN['brand']}",
        desc="Savoir-faire Précisite Usinage.",
        main=m,
        cta="Devis",
        hours="Industrie",
        head=HEAD_TECH,
        body_extra="vt-mv-industrie",
        layout="movento-industrie",
        nav_kind="solid",
    )


def build_industrie_qualite():
    m = (
        "<main>"
        + block_snap_chapter(
            "Qualité",
            "Contrôles dimensionnels et traçabilité.",
            "scene-2.png",
            "Qualité",
            reverse=True,
        )
        + "</main>"
    )
    return _shell(
        slug="industrie",
        brand=IN["brand"],
        phone=IN["phone"],
        address=IN["address"],
        email=IN["email"],
        maps=IN["maps"],
        nav=IN["nav"],
        page="qualite.html",
        title=f"Qualité - {IN['brand']}",
        desc="Qualité Précisite Usinage.",
        main=m,
        cta="Devis",
        hours="Industrie",
        head=HEAD_TECH,
        body_extra="vt-mv-industrie",
        layout="movento-industrie",
        nav_kind="solid",
    )


def build_industrie_contact():
    m = (
        "<main>"
        + block_movento_contact(
            "Devis RFQ", IN["address"], cta_label="Envoyer", phone=IN["phone"], address=IN["address"]
        )
        + "</main>"
    )
    return _shell(
        slug="industrie",
        brand=IN["brand"],
        phone=IN["phone"],
        address=IN["address"],
        email=IN["email"],
        maps=IN["maps"],
        nav=IN["nav"],
        page="contact.html",
        title=f"Contact - {IN['brand']}",
        desc="Devis usinage Yutz.",
        main=m,
        cta="Devis",
        hours="Industrie",
        head=HEAD_TECH,
        body_extra="vt-mv-industrie",
        layout="movento-industrie",
        nav_kind="solid",
    )


# --- Education ---
ED = dict(
    brand="Institut Mercure",
    phone="03 87 50 20 30",
    email="inscriptions@institut-mercure.fr",
    address="18 boulevard Paixhans, 57000 Metz",
    maps="https://maps.google.com/?q=Metz+57000",
    nav=[
        {"file": "index.html", "label": "Accueil"},
        {"file": "parcours.html", "label": "Parcours"},
        {"file": "campus.html", "label": "Campus"},
        {"file": "contact.html", "label": "Contact"},
    ],
)


def build_education_index():
    m = "<main>"
    m += block_hero_movento_center(
        "Se former sans se perdre",
        "Centre de formation à Metz : parcours clairs, inscriptions simples, preuves campus.",
        eyebrow="Metz · Formation pro",
        primary_href="contact.html",
        primary_label="Candidater",
        secondary_href="parcours.html",
        secondary_label="Voir les parcours",
        img="hero.png",
        alt="Campus formation Metz",
    )
    m += block_movento_steps(
        "Comment ça se passe",
        [
            ("Tu choisis", "Fiches parcours sans jargon - objectifs nets."),
            ("On cadre", "Dossier + entretien - calendrier affiché."),
            ("Tu avances", "Un interlocuteur, financement orienté."),
        ],
        lead="Qualiopi, alternance, salariés - on démêle ça ensemble.",
    )
    m += block_movento_quote(
        "On m'a dit clairement ce qui était finançable. Pas de roman.",
        author="Claire M.",
        role="Alternante commerce",
    )
    m += block_movento_contact(
        "Poser une question", ED["address"], cta_label="Envoyer", phone=ED["phone"], address=ED["address"]
    )
    m += "</main>"
    return _shell(
        slug="education",
        brand=ED["brand"],
        phone=ED["phone"],
        address=ED["address"],
        email=ED["email"],
        maps=ED["maps"],
        nav=ED["nav"],
        page="index.html",
        title=f"{ED['brand']} - Formation Metz",
        desc="Institut Mercure Metz : formations, admission, financement.",
        main=m,
        cta="Contact",
        hours="Metz · Formation",
        head=HEAD_SERIF,
        body_extra="vt-mv-edu",
        layout="movento-edu",
        nav_kind="pill",
    )


def build_education_parcours():
    m = (
        "<main>"
        + block_snap_chapter(
            "Catalogue",
            "Parcours courts et longs - objectifs et débouchés clairs.",
            "scene-1.png",
            "Parcours",
            cta_href="contact.html",
            cta_label="Candidater",
        )
        + "</main>"
    )
    return _shell(
        slug="education",
        brand=ED["brand"],
        phone=ED["phone"],
        address=ED["address"],
        email=ED["email"],
        maps=ED["maps"],
        nav=ED["nav"],
        page="parcours.html",
        title=f"Parcours - {ED['brand']}",
        desc="Parcours Institut Mercure.",
        main=m,
        cta="Contact",
        hours="Formation",
        head=HEAD_SERIF,
        body_extra="vt-mv-edu",
        layout="movento-edu",
    )


def build_education_campus():
    m = (
        "<main>"
        + block_snap_chapter(
            "Campus", "Locaux à Metz - visite sur RDV.", "scene-2.png", "Campus", reverse=True
        )
        + "</main>"
    )
    return _shell(
        slug="education",
        brand=ED["brand"],
        phone=ED["phone"],
        address=ED["address"],
        email=ED["email"],
        maps=ED["maps"],
        nav=ED["nav"],
        page="campus.html",
        title=f"Campus - {ED['brand']}",
        desc="Campus Institut Mercure Metz.",
        main=m,
        cta="Contact",
        hours="Formation",
        head=HEAD_SERIF,
        body_extra="vt-mv-edu",
        layout="movento-edu",
    )


def build_education_contact():
    m = (
        "<main>"
        + block_movento_contact(
            "Contact", ED["address"], cta_label="Envoyer", phone=ED["phone"], address=ED["address"]
        )
        + "</main>"
    )
    return _shell(
        slug="education",
        brand=ED["brand"],
        phone=ED["phone"],
        address=ED["address"],
        email=ED["email"],
        maps=ED["maps"],
        nav=ED["nav"],
        page="contact.html",
        title=f"Contact - {ED['brand']}",
        desc="Contact Institut Mercure.",
        main=m,
        cta="Contact",
        hours="Formation",
        head=HEAD_SERIF,
        body_extra="vt-mv-edu",
        layout="movento-edu",
    )


# --- Services ---
SV = dict(
    brand="Proprio Facility",
    phone="03 87 40 10 20",
    email="devis@proprio-facility.fr",
    address="Zone Actipole, 57070 Metz",
    maps="https://maps.google.com/?q=Metz+57070",
    nav=[
        {"file": "index.html", "label": "Accueil"},
        {"file": "offres.html", "label": "Offres"},
        {"file": "secteurs.html", "label": "Secteurs"},
        {"file": "contact.html", "label": "Devis"},
    ],
)


def build_services_index():
    m = "<main>"
    m += block_hero_movento_bleed(
        "Le terrain, on le connait",
        "Facility et services aux locaux : nettoyage, maintenance, multi-sites Grand Est.",
        "hero.png",
        "Equipe facility Metz",
        badge="Metz · Facility B2B",
        primary_href="contact.html",
        primary_label="Demander un devis",
        phone_href="tel:0387401020",
        phone_label="Appeler",
        secondary_href="offres.html",
        secondary_label="Voir les offres",
    )
    m += block_movento_steps(
        "Devis sans faire le nareux",
        [
            ("Brief", "Sites, fréquences, contraintes d'accès."),
            ("Proposition", "SLA et prix affichés - PDF direct."),
            ("Terrain", "Une équipe, un interlocuteur."),
        ],
    )
    m += block_movento_services(
        "Offres",
        [
            {"title": "Nettoyage", "text": "Bureaux, commerces, industries - planning clair.", "img": "card-1.png", "alt": "Nettoyage"},
            {"title": "Maintenance", "text": "Petits travaux et suivi technique.", "img": "card-2.png", "alt": "Maintenance"},
            {"title": "Multi-sites", "text": "Une équipe, plusieurs adresses.", "img": "card-3.png", "alt": "Multi-sites"},
        ],
    )
    m += block_movento_contact(
        "Devis facility", SV["address"], cta_label="Envoyer", phone=SV["phone"], address=SV["address"]
    )
    m += "</main>"
    return _shell(
        slug="services",
        brand=SV["brand"],
        phone=SV["phone"],
        address=SV["address"],
        email=SV["email"],
        maps=SV["maps"],
        nav=SV["nav"],
        page="index.html",
        title=f"{SV['brand']} - Services Metz",
        desc="Facility management Metz : nettoyage, maintenance, multi-sites.",
        main=m,
        cta="Devis",
        hours="Metz · Services",
        head=HEAD_CONDENSED,
        body_extra="vt-mv-services",
        layout="movento-services",
        nav_kind="underline",
    )


def build_services_offres():
    m = (
        "<main>"
        + block_snap_chapter(
            "Offres",
            "Packs mensuels ou à la mission - devis PDF.",
            "scene-1.png",
            "Offres",
            cta_href="contact.html",
            cta_label="Devis",
        )
        + "</main>"
    )
    return _shell(
        slug="services",
        brand=SV["brand"],
        phone=SV["phone"],
        address=SV["address"],
        email=SV["email"],
        maps=SV["maps"],
        nav=SV["nav"],
        page="offres.html",
        title=f"Offres - {SV['brand']}",
        desc="Offres Proprio Facility.",
        main=m,
        cta="Devis",
        hours="Services",
        head=HEAD_CONDENSED,
        body_extra="vt-mv-services",
        layout="movento-services",
        nav_kind="underline",
    )


def build_services_secteurs():
    m = (
        "<main>"
        + block_snap_chapter(
            "Secteurs",
            "Bureaux, retail, industrie, collectivités.",
            "scene-2.png",
            "Secteurs",
            reverse=True,
        )
        + "</main>"
    )
    return _shell(
        slug="services",
        brand=SV["brand"],
        phone=SV["phone"],
        address=SV["address"],
        email=SV["email"],
        maps=SV["maps"],
        nav=SV["nav"],
        page="secteurs.html",
        title=f"Secteurs - {SV['brand']}",
        desc="Secteurs Proprio Facility.",
        main=m,
        cta="Devis",
        hours="Services",
        head=HEAD_CONDENSED,
        body_extra="vt-mv-services",
        layout="movento-services",
        nav_kind="underline",
    )


def build_services_contact():
    m = (
        "<main>"
        + block_movento_contact(
            "Devis", SV["address"], cta_label="Envoyer", phone=SV["phone"], address=SV["address"]
        )
        + "</main>"
    )
    return _shell(
        slug="services",
        brand=SV["brand"],
        phone=SV["phone"],
        address=SV["address"],
        email=SV["email"],
        maps=SV["maps"],
        nav=SV["nav"],
        page="contact.html",
        title=f"Contact - {SV['brand']}",
        desc="Contact Proprio Facility.",
        main=m,
        cta="Devis",
        hours="Services",
        head=HEAD_CONDENSED,
        body_extra="vt-mv-services",
        layout="movento-services",
        nav_kind="underline",
    )


# --- Etablissement / Hotellerie ---
ET = dict(
    brand="Hôtel Stanislas Collection",
    phone="03 83 35 20 40",
    email="reservation@stanislas-collection.fr",
    address="Place Stanislas, 54000 Nancy",
    maps="https://maps.google.com/?q=Place+Stanislas+Nancy",
    nav=[
        {"file": "index.html", "label": "Accueil"},
        {"file": "chambres.html", "label": "Chambres"},
        {"file": "seminaires.html", "label": "Séminaires"},
        {"file": "contact.html", "label": "Réserver"},
    ],
)


def build_etablissement_index():
    m = "<main>"
    m += block_hero_movento_magazine(
        "Nancy, version écrin",
        "Hôtel boutique face à Stanislas : chambres, spa, réservation simple.",
        "hero.png",
        "Hotel Stanislas Nancy",
        eyebrow="Nancy · Place Stanislas",
        primary_href="contact.html",
        primary_label="Réserver",
        kicker="Hôtel boutique",
    )
    m += block_movento_menu_list(
        "Chambres",
        [
            ("Classique", "Vue cour, lit king, petit-déj", "à partir de 129 €"),
            ("Place", "Vue Stanislas, balcon", "à partir de 189 €"),
            ("Suite Spa", "Salon + hammam privé", "à partir de 249 €"),
        ],
        lead="Tarifs indicatifs weekend - tu confirmes avant.",
        cta_href="contact.html",
        cta_label="Réserver une date",
    )
    m += block_movento_quote(
        "On a dormi face à la place. Petit-déj sans file d'attente.",
        author="Marc & Léa",
        role="Week-end Nancy",
    )
    m += block_movento_contact(
        "Réserver", ET["address"], cta_label="Envoyer", phone=ET["phone"], address=ET["address"]
    )
    m += "</main>"
    return _shell(
        slug="etablissement",
        brand=ET["brand"],
        phone=ET["phone"],
        address=ET["address"],
        email=ET["email"],
        maps=ET["maps"],
        nav=ET["nav"],
        page="index.html",
        title=f"{ET['brand']} - Nancy",
        desc="Hôtel boutique Nancy Place Stanislas.",
        main=m,
        cta="Réserver",
        hours="Nancy · Hôtel",
        head=HEAD_SERIF,
        body_extra="vt-mv-hotel",
        layout="movento-hotel",
        nav_kind="pill",
    )


def build_etablissement_chambres():
    m = (
        "<main>"
        + block_snap_chapter(
            "Chambres",
            "Du cosy au suite - choix simple.",
            "scene-1.png",
            "Chambres",
            cta_href="contact.html",
            cta_label="Réserver",
        )
        + "</main>"
    )
    return _shell(
        slug="etablissement",
        brand=ET["brand"],
        phone=ET["phone"],
        address=ET["address"],
        email=ET["email"],
        maps=ET["maps"],
        nav=ET["nav"],
        page="chambres.html",
        title=f"Chambres - {ET['brand']}",
        desc="Chambres Hôtel Stanislas.",
        main=m,
        cta="Réserver",
        hours="Hôtel",
        head=HEAD_SERIF,
        body_extra="vt-mv-hotel",
        layout="movento-hotel",
    )


def build_etablissement_seminaires():
    m = (
        "<main>"
        + block_snap_chapter(
            "Séminaires",
            "Salles et pauses - devis entreprise.",
            "scene-2.png",
            "Séminaires",
            reverse=True,
            cta_href="contact.html",
            cta_label="Demander un devis",
        )
        + "</main>"
    )
    return _shell(
        slug="etablissement",
        brand=ET["brand"],
        phone=ET["phone"],
        address=ET["address"],
        email=ET["email"],
        maps=ET["maps"],
        nav=ET["nav"],
        page="seminaires.html",
        title=f"Séminaires - {ET['brand']}",
        desc="Séminaires hôtel Nancy.",
        main=m,
        cta="Réserver",
        hours="Hôtel",
        head=HEAD_SERIF,
        body_extra="vt-mv-hotel",
        layout="movento-hotel",
    )


def build_etablissement_contact():
    m = (
        "<main>"
        + block_movento_contact(
            "Réservation", ET["address"], cta_label="Envoyer", phone=ET["phone"], address=ET["address"]
        )
        + "</main>"
    )
    return _shell(
        slug="etablissement",
        brand=ET["brand"],
        phone=ET["phone"],
        address=ET["address"],
        email=ET["email"],
        maps=ET["maps"],
        nav=ET["nav"],
        page="contact.html",
        title=f"Contact - {ET['brand']}",
        desc="Réserver Hôtel Stanislas Nancy.",
        main=m,
        cta="Réserver",
        hours="Hôtel",
        head=HEAD_SERIF,
        body_extra="vt-mv-hotel",
        layout="movento-hotel",
    )


# --- Technologie ---
TE = dict(
    brand="Synapse Lorraine",
    phone="03 87 60 11 22",
    email="demo@synapse-lorraine.fr",
    address="Technopole, 57070 Metz",
    maps="https://maps.google.com/?q=Metz+Technopole",
    nav=[
        {"file": "index.html", "label": "Accueil"},
        {"file": "produit.html", "label": "Produit"},
        {"file": "clients.html", "label": "Clients"},
        {"file": "contact.html", "label": "Démo"},
    ],
)


def build_technologie_index():
    m = "<main>"
    m += block_hero_movento_split(
        "L'OS métier des équipes qui livrent",
        "SaaS B2B pour PME industrielles : workflows, API, hébergement Grand Est.",
        "hero.png",
        "Produit SaaS Synapse",
        eyebrow="Thionville · SaaS B2B",
        primary_href="contact.html",
        primary_label="Demander une démo",
        secondary_href="produit.html",
        secondary_label="Voir le produit",
        glass_pills=["Workflows", "API", "RGPD"],
    )
    m += block_movento_feature_rows(
        "Modules",
        [
            ("Flow", "Automatise sans usine à plugins.", "card-1.png", "Workflows"),
            ("Data Hub", "Connecte ERP et CRM.", "card-2.png", "Data hub"),
            ("API", "Auth, webhooks, audit trail.", "card-3.png", "API"),
        ],
    )
    m += block_movento_stat_band(
        [("120+", "clients"), ("99,9 %", "SLA"), ("48 h", "time-to-value"), ("EU", "hébergé")]
    )
    m += block_movento_contact(
        "Planifier une démo", TE["address"], cta_label="Envoyer", phone=TE["phone"], address=TE["address"]
    )
    m += "</main>"
    return _shell(
        slug="technologie",
        brand=TE["brand"],
        phone=TE["phone"],
        address=TE["address"],
        email=TE["email"],
        maps=TE["maps"],
        nav=TE["nav"],
        page="index.html",
        title=f"{TE['brand']} - SaaS Lorraine",
        desc="Synapse Lorraine : SaaS B2B workflows et API.",
        main=m,
        cta="Démo",
        hours="Lorraine · Tech",
        head=HEAD_TECH,
        body_extra="vt-mv-tech",
        layout="movento-tech",
        nav_kind="minimal",
    )


def build_technologie_produit():
    m = (
        "<main>"
        + block_snap_chapter(
            "Produit",
            "Modules, sécurité, déploiement.",
            "scene-1.png",
            "Produit",
            cta_href="contact.html",
            cta_label="Démo",
        )
        + "</main>"
    )
    return _shell(
        slug="technologie",
        brand=TE["brand"],
        phone=TE["phone"],
        address=TE["address"],
        email=TE["email"],
        maps=TE["maps"],
        nav=TE["nav"],
        page="produit.html",
        title=f"Produit - {TE['brand']}",
        desc="Produit Synapse Lorraine.",
        main=m,
        cta="Démo",
        hours="Tech",
        head=HEAD_TECH,
        body_extra="vt-mv-tech",
        layout="movento-tech",
        nav_kind="minimal",
    )


def build_technologie_clients():
    m = (
        "<main>"
        + block_snap_chapter(
            "Clients", "PME industrielles du Grand Est.", "scene-2.png", "Clients", reverse=True
        )
        + "</main>"
    )
    return _shell(
        slug="technologie",
        brand=TE["brand"],
        phone=TE["phone"],
        address=TE["address"],
        email=TE["email"],
        maps=TE["maps"],
        nav=TE["nav"],
        page="clients.html",
        title=f"Clients - {TE['brand']}",
        desc="Clients Synapse Lorraine.",
        main=m,
        cta="Démo",
        hours="Tech",
        head=HEAD_TECH,
        body_extra="vt-mv-tech",
        layout="movento-tech",
        nav_kind="minimal",
    )


def build_technologie_contact():
    m = (
        "<main>"
        + block_movento_contact(
            "Démo", TE["address"], cta_label="Envoyer", phone=TE["phone"], address=TE["address"]
        )
        + "</main>"
    )
    return _shell(
        slug="technologie",
        brand=TE["brand"],
        phone=TE["phone"],
        address=TE["address"],
        email=TE["email"],
        maps=TE["maps"],
        nav=TE["nav"],
        page="contact.html",
        title=f"Contact - {TE['brand']}",
        desc="Demander une démo Synapse.",
        main=m,
        cta="Démo",
        hours="Tech",
        head=HEAD_TECH,
        body_extra="vt-mv-tech",
        layout="movento-tech",
        nav_kind="minimal",
    )


# --- Fitness ---
FI = dict(
    brand="Pulse Fitness Metz",
    phone="03 87 55 40 00",
    email="bonjour@pulse-fitness-metz.fr",
    address="42 avenue de Strasbourg, 57000 Metz",
    maps="https://maps.google.com/?q=Metz+57000",
    nav=[
        {"file": "index.html", "label": "Accueil"},
        {"file": "cours.html", "label": "Cours"},
        {"file": "tarifs.html", "label": "Tarifs"},
        {"file": "contact.html", "label": "Essai"},
    ],
)


def build_fitness_index():
    m = "<main>"
    m += block_hero_movento_bleed(
        "Bouge, sans usine à abos",
        "Salle Metz : cours, muscu, essai gratuit - horaires et tarifs nets.",
        "hero.png",
        "Salle de sport Metz",
        badge="Metz · Fitness",
        primary_href="contact.html",
        primary_label="Essai gratuit",
        phone_href="tel:0387554000",
        phone_label="Appeler",
        secondary_href="tarifs.html",
        secondary_label="Voir les tarifs",
    )
    m += block_movento_steps(
        "Ton premier passage",
        [
            ("Tu réserves", "Essai gratuit - créneau en ligne."),
            ("On te balade", "Machines, vestiaires, coaches."),
            ("Tu choisis", "Mensuel ou annuel - prix affiché."),
        ],
    )
    m += block_movento_services(
        "Sur place",
        [
            {"title": "Cours", "text": "Planning de la semaine, sans surprise.", "img": "card-1.png", "alt": "Cours collectif"},
            {"title": "Muscu", "text": "Machines et libre - coaches dispo.", "img": "card-2.png", "alt": "Musculation"},
            {"title": "Tarifs", "text": "Mensuel ou annuel - prix affiché.", "img": "card-3.png", "alt": "Tarifs"},
        ],
    )
    m += block_movento_contact(
        "Réserver un essai", FI["address"], cta_label="Envoyer", phone=FI["phone"], address=FI["address"]
    )
    m += "</main>"
    return _shell(
        slug="fitness",
        brand=FI["brand"],
        phone=FI["phone"],
        address=FI["address"],
        email=FI["email"],
        maps=FI["maps"],
        nav=FI["nav"],
        page="index.html",
        title=f"{FI['brand']} - Salle Metz",
        desc="Salle de sport Metz : cours, tarifs, essai.",
        main=m,
        cta="Essai",
        hours="Metz · Fitness",
        head=HEAD_CONDENSED,
        body_extra="vt-mv-fitness",
        layout="movento-fitness",
        nav_kind="solid",
    )


def build_fitness_cours():
    m = (
        "<main>"
        + block_snap_chapter(
            "Cours",
            "Collectifs et coaching - planning à jour.",
            "scene-1.png",
            "Cours",
            cta_href="contact.html",
            cta_label="Essai",
        )
        + "</main>"
    )
    return _shell(
        slug="fitness",
        brand=FI["brand"],
        phone=FI["phone"],
        address=FI["address"],
        email=FI["email"],
        maps=FI["maps"],
        nav=FI["nav"],
        page="cours.html",
        title=f"Cours - {FI['brand']}",
        desc="Cours Pulse Fitness Metz.",
        main=m,
        cta="Essai",
        hours="Fitness",
        head=HEAD_CONDENSED,
        body_extra="vt-mv-fitness",
        layout="movento-fitness",
        nav_kind="solid",
    )


def build_fitness_tarifs():
    m = (
        "<main>"
        + block_snap_chapter(
            "Tarifs",
            "Sans engagement caché - PDF sur demande.",
            "scene-2.png",
            "Tarifs",
            reverse=True,
            cta_href="contact.html",
            cta_label="Essai gratuit",
        )
        + "</main>"
    )
    return _shell(
        slug="fitness",
        brand=FI["brand"],
        phone=FI["phone"],
        address=FI["address"],
        email=FI["email"],
        maps=FI["maps"],
        nav=FI["nav"],
        page="tarifs.html",
        title=f"Tarifs - {FI['brand']}",
        desc="Tarifs Pulse Fitness Metz.",
        main=m,
        cta="Essai",
        hours="Fitness",
        head=HEAD_CONDENSED,
        body_extra="vt-mv-fitness",
        layout="movento-fitness",
        nav_kind="solid",
    )


def build_fitness_contact():
    m = (
        "<main>"
        + block_movento_contact(
            "Essai gratuit", FI["address"], cta_label="Envoyer", phone=FI["phone"], address=FI["address"]
        )
        + "</main>"
    )
    return _shell(
        slug="fitness",
        brand=FI["brand"],
        phone=FI["phone"],
        address=FI["address"],
        email=FI["email"],
        maps=FI["maps"],
        nav=FI["nav"],
        page="contact.html",
        title=f"Contact - {FI['brand']}",
        desc="Essai Pulse Fitness Metz.",
        main=m,
        cta="Essai",
        hours="Fitness",
        head=HEAD_CONDENSED,
        body_extra="vt-mv-fitness",
        layout="movento-fitness",
        nav_kind="solid",
    )


# --- Banque ---
BA = dict(
    brand="Banque des Ponts",
    phone="03 87 30 40 50",
    email="agence@banque-des-ponts.fr",
    address="1 place de la Comédie, 57000 Metz",
    maps="https://maps.google.com/?q=Metz+Comedie",
    nav=[
        {"file": "index.html", "label": "Accueil"},
        {"file": "offres.html", "label": "Offres"},
        {"file": "entreprises.html", "label": "Entreprises"},
        {"file": "contact.html", "label": "RDV"},
    ],
)


def build_banque_index():
    m = "<main>"
    m += block_hero_movento_center(
        "Une banque de proximité",
        "Particuliers et pros à Metz : RDV agence, parcours clairs, conseiller dédié.",
        eyebrow="Metz · Banque locale",
        primary_href="contact.html",
        primary_label="Prendre RDV",
        secondary_href="offres.html",
        secondary_label="Offres",
        img="hero.png",
        alt="Agence bancaire Metz",
    )
    m += block_movento_steps(
        "Ouvrir un compte",
        [
            ("RDV", "En agence ou visio - sous 48 h."),
            ("Dossier", "Pièces listées, pas de blabla."),
            ("Suivi", "Un conseiller, pas un call-center."),
        ],
    )
    m += block_movento_feature_rows(
        "Parcours",
        [
            ("Particuliers", "Compte, épargne, crédit - sans usine.", "card-1.png", "Particuliers"),
            ("Pros", "TPE et indépendants du Grand Est.", "card-2.png", "Pros"),
            ("RDV", "Tu choisis le créneau - on confirme.", "card-3.png", "RDV banque"),
        ],
    )
    m += block_movento_contact(
        "Prendre RDV", BA["address"], cta_label="Envoyer", phone=BA["phone"], address=BA["address"]
    )
    m += "</main>"
    return _shell(
        slug="banque",
        brand=BA["brand"],
        phone=BA["phone"],
        address=BA["address"],
        email=BA["email"],
        maps=BA["maps"],
        nav=BA["nav"],
        page="index.html",
        title=f"{BA['brand']} - Metz",
        desc="Banque des Ponts Metz : particuliers et pros.",
        main=m,
        cta="RDV",
        hours="Metz · Banque",
        head=HEAD_SERIF,
        body_extra="vt-mv-banque",
        layout="movento-banque",
        nav_kind="pill",
    )


def build_banque_offres():
    m = (
        "<main>"
        + block_snap_chapter(
            "Offres",
            "Ouverture de compte et crédits - devis avant signature.",
            "scene-1.png",
            "Offres",
            cta_href="contact.html",
            cta_label="RDV",
        )
        + "</main>"
    )
    return _shell(
        slug="banque",
        brand=BA["brand"],
        phone=BA["phone"],
        address=BA["address"],
        email=BA["email"],
        maps=BA["maps"],
        nav=BA["nav"],
        page="offres.html",
        title=f"Offres - {BA['brand']}",
        desc="Offres Banque des Ponts.",
        main=m,
        cta="RDV",
        hours="Banque",
        head=HEAD_SERIF,
        body_extra="vt-mv-banque",
        layout="movento-banque",
    )


def build_banque_entreprises():
    m = (
        "<main>"
        + block_snap_chapter(
            "Entreprises", "Comptes pro et accompagnement TPE.", "scene-2.png", "Entreprises", reverse=True
        )
        + "</main>"
    )
    return _shell(
        slug="banque",
        brand=BA["brand"],
        phone=BA["phone"],
        address=BA["address"],
        email=BA["email"],
        maps=BA["maps"],
        nav=BA["nav"],
        page="entreprises.html",
        title=f"Entreprises - {BA['brand']}",
        desc="Offres entreprises Banque des Ponts.",
        main=m,
        cta="RDV",
        hours="Banque",
        head=HEAD_SERIF,
        body_extra="vt-mv-banque",
        layout="movento-banque",
    )


def build_banque_contact():
    m = (
        "<main>"
        + block_movento_contact(
            "RDV agence", BA["address"], cta_label="Envoyer", phone=BA["phone"], address=BA["address"]
        )
        + "</main>"
    )
    return _shell(
        slug="banque",
        brand=BA["brand"],
        phone=BA["phone"],
        address=BA["address"],
        email=BA["email"],
        maps=BA["maps"],
        nav=BA["nav"],
        page="contact.html",
        title=f"Contact - {BA['brand']}",
        desc="RDV Banque des Ponts Metz.",
        main=m,
        cta="RDV",
        hours="Banque",
        head=HEAD_SERIF,
        body_extra="vt-mv-banque",
        layout="movento-banque",
    )


# --- Gites ---
GI = dict(
    brand="Les Lucioles",
    phone="03 29 60 12 40",
    email="sejour@les-lucioles-vosges.fr",
    address="Route des Crêtes, 88230 Le Valtin",
    maps="https://maps.google.com/?q=Le+Valtin+88230",
    nav=[
        {"file": "index.html", "label": "Accueil"},
        {"file": "hebergements.html", "label": "Hébergements"},
        {"file": "sejours.html", "label": "Séjours"},
        {"file": "contact.html", "label": "Réserver"},
    ],
)


def build_gites_index():
    m = "<main>"
    m += block_hero_movento_magazine(
        "Les Vosges, sans usine",
        "Gîtes et séjours nature : hébergements, idées circuits, résa directe.",
        "hero.png",
        "Gite Vosges Les Lucioles",
        eyebrow="Le Valtin · Vosges",
        primary_href="contact.html",
        primary_label="Réserver",
        kicker="Séjours nature",
    )
    m += block_snap_chapter(
        "Cabanes et maisons",
        "Photos réelles, capacités claires, animaux OK sur la plupart des gîtes.",
        "scene-1.png",
        "Hébergement Vosges",
        cta_href="hebergements.html",
        cta_label="Voir les gîtes",
    )
    m += block_movento_quote(
        "On a réservé direct - pas de plateforme, pas de surprise.",
        author="Famille R.",
        role="Week-end Le Valtin",
    )
    m += block_movento_contact(
        "Réserver un séjour", GI["address"], cta_label="Envoyer", phone=GI["phone"], address=GI["address"]
    )
    m += "</main>"
    return _shell(
        slug="gites",
        brand=GI["brand"],
        phone=GI["phone"],
        address=GI["address"],
        email=GI["email"],
        maps=GI["maps"],
        nav=GI["nav"],
        page="index.html",
        title=f"{GI['brand']} - Gîtes Vosges",
        desc="Gîtes Les Lucioles Vosges : séjours nature.",
        main=m,
        cta="Réserver",
        hours="Vosges · Gîtes",
        head=HEAD_SERIF,
        body_extra="vt-mv-gites",
        layout="movento-gites",
        nav_kind="pill",
    )


def build_gites_hebergements():
    m = (
        "<main>"
        + block_snap_chapter(
            "Hébergements",
            "Capacités et équipements - sans surprise.",
            "scene-1.png",
            "Hébergements",
            cta_href="contact.html",
            cta_label="Réserver",
        )
        + "</main>"
    )
    return _shell(
        slug="gites",
        brand=GI["brand"],
        phone=GI["phone"],
        address=GI["address"],
        email=GI["email"],
        maps=GI["maps"],
        nav=GI["nav"],
        page="hebergements.html",
        title=f"Hébergements - {GI['brand']}",
        desc="Hébergements Les Lucioles.",
        main=m,
        cta="Réserver",
        hours="Gîtes",
        head=HEAD_SERIF,
        body_extra="vt-mv-gites",
        layout="movento-gites",
    )


def build_gites_sejours():
    m = (
        "<main>"
        + block_snap_chapter(
            "Séjours", "Idées week-end et semaines.", "scene-2.png", "Séjours", reverse=True
        )
        + "</main>"
    )
    return _shell(
        slug="gites",
        brand=GI["brand"],
        phone=GI["phone"],
        address=GI["address"],
        email=GI["email"],
        maps=GI["maps"],
        nav=GI["nav"],
        page="sejours.html",
        title=f"Séjours - {GI['brand']}",
        desc="Séjours Les Lucioles Vosges.",
        main=m,
        cta="Réserver",
        hours="Gîtes",
        head=HEAD_SERIF,
        body_extra="vt-mv-gites",
        layout="movento-gites",
    )


def build_gites_contact():
    m = (
        "<main>"
        + block_movento_contact(
            "Réservation", GI["address"], cta_label="Envoyer", phone=GI["phone"], address=GI["address"]
        )
        + "</main>"
    )
    return _shell(
        slug="gites",
        brand=GI["brand"],
        phone=GI["phone"],
        address=GI["address"],
        email=GI["email"],
        maps=GI["maps"],
        nav=GI["nav"],
        page="contact.html",
        title=f"Contact - {GI['brand']}",
        desc="Réserver Les Lucioles Vosges.",
        main=m,
        cta="Réserver",
        hours="Gîtes",
        head=HEAD_SERIF,
        body_extra="vt-mv-gites",
        layout="movento-gites",
    )


BUILDERS_MOVENTO_VAGUE_B = {
    "industrie": [
        ("index.html", build_industrie_index),
        ("savoir-faire.html", build_industrie_savoir),
        ("qualite.html", build_industrie_qualite),
        ("contact.html", build_industrie_contact),
    ],
    "education": [
        ("index.html", build_education_index),
        ("parcours.html", build_education_parcours),
        ("campus.html", build_education_campus),
        ("contact.html", build_education_contact),
    ],
    "services": [
        ("index.html", build_services_index),
        ("offres.html", build_services_offres),
        ("secteurs.html", build_services_secteurs),
        ("contact.html", build_services_contact),
    ],
    "etablissement": [
        ("index.html", build_etablissement_index),
        ("chambres.html", build_etablissement_chambres),
        ("seminaires.html", build_etablissement_seminaires),
        ("contact.html", build_etablissement_contact),
    ],
    "technologie": [
        ("index.html", build_technologie_index),
        ("produit.html", build_technologie_produit),
        ("clients.html", build_technologie_clients),
        ("contact.html", build_technologie_contact),
    ],
    "fitness": [
        ("index.html", build_fitness_index),
        ("cours.html", build_fitness_cours),
        ("tarifs.html", build_fitness_tarifs),
        ("contact.html", build_fitness_contact),
    ],
    "banque": [
        ("index.html", build_banque_index),
        ("offres.html", build_banque_offres),
        ("entreprises.html", build_banque_entreprises),
        ("contact.html", build_banque_contact),
    ],
    "gites": [
        ("index.html", build_gites_index),
        ("hebergements.html", build_gites_hebergements),
        ("sejours.html", build_gites_sejours),
        ("contact.html", build_gites_contact),
    ],
}
