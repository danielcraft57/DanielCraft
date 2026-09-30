"""Redesign Movento vague D - 9 metiers conseil / archi / logistique / photo / asso.

Slugs : electricien, architecture, promoteur, comptable, assurance, notaire,
logistique, photographie, association.

Personnalites distinctes par metier (nav + hero + sections).
Filenames HTML en ASCII. Accents OK dans les libelles visibles.
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
    block_movento_pill_nav,
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

HEAD_CONDENSED = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Instrument+Serif&display=swap" rel="stylesheet">
{_BOOT}"""

HEAD_TECH = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
{_BOOT}"""


def _fl(nav):
    return [(p["label"], p["file"]) for p in nav]


def _tel(phone: str) -> str:
    return "tel:" + "".join(c for c in phone if c.isdigit())


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


# --- Electricien : Volt & Clanche - bleed + steps + quote ---
EL = dict(
    brand="Volt & Clanche",
    phone="03 87 91 20 45",
    email="urgence@volt-clanche.fr",
    address="Zone artisanale Sud, 57070 Metz",
    maps="https://maps.google.com/?q=Metz+57070+electricien",
    nav=[
        {"file": "index.html", "label": "Accueil"},
        {"file": "services.html", "label": "Services"},
        {"file": "zones.html", "label": "Zones"},
        {"file": "contact.html", "label": "Devis"},
    ],
)


def build_electricien_index():
    m = "<main>"
    m += block_hero_movento_bleed(
        "Panne, tableau, mise aux normes",
        "Électricien à Metz : urgence, rénov, devis avant d'ouvrir le tableau.",
        "hero.png",
        "Électricien Volt et Clanche Metz",
        badge="Metz · Montigny · Woippy",
        primary_href="contact.html",
        primary_label="Devis gratuit",
        phone_href=_tel(EL["phone"]),
        phone_label="Appeler",
        secondary_href="services.html",
        secondary_label="Voir les services",
    )
    m += block_movento_steps(
        "Comment ça se passe",
        [
            ("Tu appelles", "Urgence ou devis - on te dit si on peut passer aujourd'hui."),
            ("On digne sur place", "Photos, devis oral net, tu valides avant qu'on touche."),
            ("On repart propre", "Tableau rangé, facture claire, numéro direct."),
        ],
        lead="Dis voir ce qui saute - on démêle ça.",
    )
    m += block_movento_quote(
        "Arrivés entre midi, devis avant d'ouvrir le tableau. Nickel.",
        author="Thomas",
        role="Metz Sud",
    )
    m += block_movento_contact("Urgence ou devis", EL["address"], cta_label="Envoyer", phone=EL["phone"], address=EL["address"])
    m += "</main>"
    return _shell(
        slug="electricien",
        brand=EL["brand"],
        phone=EL["phone"],
        address=EL["address"],
        email=EL["email"],
        maps=EL["maps"],
        nav=EL["nav"],
        page="index.html",
        title=f"{EL['brand']} - Électricien Metz",
        desc="Électricien à Metz : urgence, rénovation, devis clair.",
        main=m,
        cta="Devis",
        hours="Metz · Électricité",
        head=HEAD_CONDENSED,
        body_extra="vt-mv-electricien",
        layout="movento-electricien",
        nav_kind="solid",
    )


def build_electricien_services():
    m = "<main>"
    m += block_snap_chapter("Dépannage", "Coupure, court-circuit - arrivée moyenne annoncée.", "scene-1.png", "Dépannage", cta_href="contact.html", cta_label="Appeler")
    m += block_snap_chapter("Rénovation", "Tableau et circuits - devis avant démontage.", "card-2.png", "Rénovation", reverse=True)
    m += "</main>"
    return _shell(slug="electricien", brand=EL["brand"], phone=EL["phone"], address=EL["address"], email=EL["email"], maps=EL["maps"], nav=EL["nav"], page="services.html", title=f"Services - {EL['brand']}", desc="Services électricien Metz.", main=m, cta="Devis", hours="Metz · Électricité", head=HEAD_CONDENSED, body_extra="vt-mv-electricien", layout="movento-electricien", nav_kind="solid")


def build_electricien_zones():
    m = f"""<main><section class="vt-mv-services"><div class="vt-mv-wrap">
    <p class="vt-mv-eyebrow">Zones</p>
    <h1 class="vt-mv-section-title">Metz et alentours</h1>
    <p class="vt-mv-lead">Metz, Montigny, Woippy, Longeville - urgence et devis.</p>
    <p class="mt-4"><a class="vt-mv-btn vt-mv-btn-primary" href="{_tel(EL['phone'])}">Appeler</a></p>
    </div></section></main>"""
    return _shell(slug="electricien", brand=EL["brand"], phone=EL["phone"], address=EL["address"], email=EL["email"], maps=EL["maps"], nav=EL["nav"], page="zones.html", title=f"Zones - {EL['brand']}", desc="Zones électricien Metz.", main=m, cta="Devis", hours="Metz", head=HEAD_CONDENSED, body_extra="vt-mv-electricien", layout="movento-electricien", nav_kind="solid")


def build_electricien_contact():
    m = "<main>" + block_movento_contact("Devis", EL["address"], cta_label="Envoyer", phone=EL["phone"], address=EL["address"]) + "</main>"
    return _shell(slug="electricien", brand=EL["brand"], phone=EL["phone"], address=EL["address"], email=EL["email"], maps=EL["maps"], nav=EL["nav"], page="contact.html", title=f"Contact - {EL['brand']}", desc="Contacter Volt & Clanche Metz.", main=m, cta="Devis", hours="Metz · Électricité", head=HEAD_CONDENSED, body_extra="vt-mv-electricien", layout="movento-electricien", nav_kind="solid")


# --- Architecture : Atelier Nord-Est - magazine + feature_rows ---
AR = dict(
    brand="Atelier Nord-Est",
    phone="03 87 66 12 34",
    email="contact@atelier-nord-est.fr",
    address="14 rue du XXe Corps, 57000 Metz",
    maps="https://maps.google.com/?q=14+rue+du+XXe+Corps+57000+Metz",
    nav=[
        {"file": "index.html", "label": "Accueil"},
        {"file": "projets.html", "label": "Projets"},
        {"file": "methode.html", "label": "Méthode"},
        {"file": "contact.html", "label": "Brief"},
    ],
)


def build_architecture_index():
    m = "<main>"
    m += block_hero_movento_magazine(
        "Plans clairs, chantier suivi",
        "Architecture à Metz : rénovation, extension, permis - un atelier, un interlocuteur.",
        "hero.png",
        "Atelier Nord-Est Metz",
        eyebrow="Metz · Architecture",
        primary_href="contact.html",
        primary_label="Envoyer un brief",
        kicker="Atelier local",
    )
    m += block_movento_feature_rows(
        "Missions",
        [
            ("Projets", "Maisons et locaux - intention puis détail.", "card-1.png", "Projet architecture"),
            ("Méthode", "Esquisse, permis, suivi - étapes datées.", "card-2.png", "Méthode"),
            ("Chantier", "Visites et comptes-rendus photo.", "card-3.png", "Chantier"),
        ],
        lead="Des bandes photo + texte, pas trois cartes clones.",
    )
    m += block_movento_steps(
        "Ton parcours",
        [
            ("Brief", "Besoin, budget, délai - on note net."),
            ("Esquisse", "Options claires avant le permis."),
            ("Suivi", "Chantier photographié - tu sais où on en est."),
        ],
    )
    m += block_movento_contact("Brief projet", AR["address"], cta_label="Envoyer", phone=AR["phone"], address=AR["address"])
    m += "</main>"
    return _shell(
        slug="architecture",
        brand=AR["brand"],
        phone=AR["phone"],
        address=AR["address"],
        email=AR["email"],
        maps=AR["maps"],
        nav=AR["nav"],
        page="index.html",
        title=f"{AR['brand']} - Architecture Metz",
        desc="Atelier d'architecture à Metz : projets, méthode, brief.",
        main=m,
        cta="Brief",
        hours="Metz · Architecture",
        head=HEAD_TECH,
        body_extra="vt-mv-architecture",
        layout="movento-architecture",
        nav_kind="underline",
    )


def build_architecture_projets():
    m = "<main>" + block_snap_chapter("Projets", "Rénovation et neuf - sélection de réalisations.", "scene-1.png", "Projets", cta_href="contact.html", cta_label="Brief") + "</main>"
    return _shell(slug="architecture", brand=AR["brand"], phone=AR["phone"], address=AR["address"], email=AR["email"], maps=AR["maps"], nav=AR["nav"], page="projets.html", title=f"Projets - {AR['brand']}", desc="Projets Atelier Nord-Est.", main=m, cta="Brief", hours="Metz · Architecture", head=HEAD_TECH, body_extra="vt-mv-architecture", layout="movento-architecture", nav_kind="underline")


def build_architecture_methode():
    m = "<main>" + block_snap_chapter("Méthode", "Esquisse, permis, chantier - tu sais où on en est.", "scene-2.png", "Méthode", reverse=True) + "</main>"
    return _shell(slug="architecture", brand=AR["brand"], phone=AR["phone"], address=AR["address"], email=AR["email"], maps=AR["maps"], nav=AR["nav"], page="methode.html", title=f"Méthode - {AR['brand']}", desc="Méthode Atelier Nord-Est.", main=m, cta="Brief", hours="Metz · Architecture", head=HEAD_TECH, body_extra="vt-mv-architecture", layout="movento-architecture", nav_kind="underline")


def build_architecture_contact():
    m = "<main>" + block_movento_contact("Brief", AR["address"], cta_label="Envoyer", phone=AR["phone"], address=AR["address"]) + "</main>"
    return _shell(slug="architecture", brand=AR["brand"], phone=AR["phone"], address=AR["address"], email=AR["email"], maps=AR["maps"], nav=AR["nav"], page="contact.html", title=f"Contact - {AR['brand']}", desc="Contacter Atelier Nord-Est Metz.", main=m, cta="Brief", hours="Metz · Architecture", head=HEAD_TECH, body_extra="vt-mv-architecture", layout="movento-architecture", nav_kind="underline")


# --- Promoteur : Habitat Horizon - split + steps + stat ---
PR = dict(
    brand="Habitat Horizon",
    phone="03 83 19 44 70",
    email="projets@habitat-horizon.fr",
    address="28 boulevard Joffre, 54000 Nancy",
    maps="https://maps.google.com/?q=28+boulevard+Joffre+54000+Nancy",
    nav=[
        {"file": "index.html", "label": "Accueil"},
        {"file": "programmes.html", "label": "Programmes"},
        {"file": "accompagnement.html", "label": "Accompagnement"},
        {"file": "contact.html", "label": "Contact"},
    ],
)


def build_promoteur_index():
    m = "<main>"
    m += block_hero_movento_split(
        "Programmes neufs, parcours clair",
        "Promotion immobilière à Nancy - lots, planning, accompagnement sans jargon.",
        "hero.png",
        "Habitat Horizon Nancy",
        eyebrow="Nancy · Promotion immobilière",
        primary_href="programmes.html",
        primary_label="Voir les programmes",
        secondary_href="contact.html",
        secondary_label="Nous contacter",
        glass_pills=["Lots", "Planning", "Accompagnement"],
    )
    m += block_movento_stat_band(
        [("Nancy", "programmes"), ("Lots", "disponibles"), ("Suivi", "chantier"), ("1", "contact")]
    )
    m += block_movento_steps(
        "Parcours acheteur",
        [
            ("Programme", "Plans et prix indicatifs - sans roman."),
            ("Réservation", "Étapes datées jusqu'à la livraison."),
            ("Remise des clés", "Visites showroom et chantier sur RDV."),
        ],
    )
    m += block_movento_contact("Demande d'info", PR["address"], cta_label="Envoyer", phone=PR["phone"], address=PR["address"])
    m += "</main>"
    return _shell(
        slug="promoteur",
        brand=PR["brand"],
        phone=PR["phone"],
        address=PR["address"],
        email=PR["email"],
        maps=PR["maps"],
        nav=PR["nav"],
        page="index.html",
        title=f"{PR['brand']} - Promoteurs Nancy",
        desc="Promoteurs à Nancy : programmes neufs, accompagnement.",
        main=m,
        cta="Contact",
        hours="Nancy · Promotion",
        head=HEAD_SERIF,
        body_extra="vt-mv-promoteur",
        layout="movento-promoteur",
        nav_kind="pill",
    )


def build_promoteur_programmes():
    m = "<main>" + block_snap_chapter("Programmes", "Lots et typologies - disponibilités à jour.", "scene-1.png", "Programmes", cta_href="contact.html", cta_label="Info lot") + "</main>"
    return _shell(slug="promoteur", brand=PR["brand"], phone=PR["phone"], address=PR["address"], email=PR["email"], maps=PR["maps"], nav=PR["nav"], page="programmes.html", title=f"Programmes - {PR['brand']}", desc="Programmes Habitat Horizon.", main=m, cta="Contact", hours="Nancy · Promotion", head=HEAD_SERIF, body_extra="vt-mv-promoteur", layout="movento-promoteur", nav_kind="pill")


def build_promoteur_accompagnement():
    m = "<main>" + block_snap_chapter("Accompagnement", "De la réservation à la remise des clés.", "scene-2.png", "Accompagnement", reverse=True) + "</main>"
    return _shell(slug="promoteur", brand=PR["brand"], phone=PR["phone"], address=PR["address"], email=PR["email"], maps=PR["maps"], nav=PR["nav"], page="accompagnement.html", title=f"Accompagnement - {PR['brand']}", desc="Accompagnement Habitat Horizon.", main=m, cta="Contact", hours="Nancy · Promotion", head=HEAD_SERIF, body_extra="vt-mv-promoteur", layout="movento-promoteur", nav_kind="pill")


def build_promoteur_contact():
    m = "<main>" + block_movento_contact("Contact", PR["address"], cta_label="Envoyer", phone=PR["phone"], address=PR["address"]) + "</main>"
    return _shell(slug="promoteur", brand=PR["brand"], phone=PR["phone"], address=PR["address"], email=PR["email"], maps=PR["maps"], nav=PR["nav"], page="contact.html", title=f"Contact - {PR['brand']}", desc="Contacter Habitat Horizon Nancy.", main=m, cta="Contact", hours="Nancy · Promotion", head=HEAD_SERIF, body_extra="vt-mv-promoteur", layout="movento-promoteur", nav_kind="pill")


# --- Comptable : Verlaine & Associes - center + steps + quote ---
CP = dict(
    brand="Verlaine & Associés",
    phone="03 87 75 90 12",
    email="contact@verlaine-associes.fr",
    address="14 rue Serpenoise, 57000 Metz",
    maps="https://maps.google.com/?q=14+rue+Serpenoise+57000+Metz",
    nav=[
        {"file": "index.html", "label": "Accueil"},
        {"file": "expertises.html", "label": "Expertises"},
        {"file": "methode.html", "label": "Méthode"},
        {"file": "contact.html", "label": "RDV"},
    ],
)


def build_comptable_index():
    m = "<main>"
    m += block_hero_movento_center(
        "Compta claire pour TPE et PME",
        "Cabinet à Metz : tenue, paie, bilan - rendez-vous sans jargon.",
        eyebrow="Metz · Expertise comptable",
        primary_href="contact.html",
        primary_label="Prendre RDV",
        secondary_href="expertises.html",
        secondary_label="Expertises",
    )
    m += block_movento_steps(
        "Méthode",
        [
            ("Écoute", "Tu expliques l'activité - on cadre le périmètre."),
            ("Outils", "Points réguliers, zéro surprise."),
            ("Bilan", "Lecture simple des chiffres."),
        ],
        lead="Cabinet sobre - pas de grille de cartes photo.",
    )
    m += block_movento_quote(
        "Ils tiennent les délais annoncés. Ça change tout quand tu es TPE.",
        author="Olivier",
        role="dirigeant, Metz",
    )
    m += block_movento_contact("Prendre RDV", CP["address"], cta_label="Envoyer", phone=CP["phone"], address=CP["address"])
    m += "</main>"
    return _shell(
        slug="comptable",
        brand=CP["brand"],
        phone=CP["phone"],
        address=CP["address"],
        email=CP["email"],
        maps=CP["maps"],
        nav=CP["nav"],
        page="index.html",
        title=f"{CP['brand']} - Expert-comptable Metz",
        desc="Cabinet comptable à Metz : tenue, paie, bilan.",
        main=m,
        cta="RDV",
        hours="Metz · Comptable",
        head=HEAD_SERIF,
        body_extra="vt-mv-comptable",
        layout="movento-comptable",
        nav_kind="minimal",
    )


def build_comptable_expertises():
    m = "<main>" + block_snap_chapter("Expertises", "Tenue, paie, fiscal - périmètre cadré dès le début.", "scene-1.png", "Expertises", cta_href="contact.html", cta_label="RDV") + "</main>"
    return _shell(slug="comptable", brand=CP["brand"], phone=CP["phone"], address=CP["address"], email=CP["email"], maps=CP["maps"], nav=CP["nav"], page="expertises.html", title=f"Expertises - {CP['brand']}", desc="Expertises Verlaine Metz.", main=m, cta="RDV", hours="Metz · Comptable", head=HEAD_SERIF, body_extra="vt-mv-comptable", layout="movento-comptable", nav_kind="minimal")


def build_comptable_methode():
    m = "<main>" + block_snap_chapter("Méthode", "Outils partagés, points mensuels, zéro surprise.", "scene-2.png", "Méthode", reverse=True) + "</main>"
    return _shell(slug="comptable", brand=CP["brand"], phone=CP["phone"], address=CP["address"], email=CP["email"], maps=CP["maps"], nav=CP["nav"], page="methode.html", title=f"Méthode - {CP['brand']}", desc="Méthode Verlaine Metz.", main=m, cta="RDV", hours="Metz · Comptable", head=HEAD_SERIF, body_extra="vt-mv-comptable", layout="movento-comptable", nav_kind="minimal")


def build_comptable_contact():
    m = "<main>" + block_movento_contact("RDV", CP["address"], cta_label="Envoyer", phone=CP["phone"], address=CP["address"]) + "</main>"
    return _shell(slug="comptable", brand=CP["brand"], phone=CP["phone"], address=CP["address"], email=CP["email"], maps=CP["maps"], nav=CP["nav"], page="contact.html", title=f"Contact - {CP['brand']}", desc="RDV Verlaine & Associés Metz.", main=m, cta="RDV", hours="Metz · Comptable", head=HEAD_SERIF, body_extra="vt-mv-comptable", layout="movento-comptable", nav_kind="minimal")


# --- Assurance : Couverture Est - underline + split + feature_rows ---
AS = dict(
    brand="Couverture Est",
    phone="03 88 41 72 60",
    email="bonjour@couverture-est.fr",
    address="45 avenue de la Forêt Noire, 67000 Strasbourg",
    maps="https://maps.google.com/?q=45+avenue+de+la+Foret+Noire+67000+Strasbourg",
    nav=[
        {"file": "index.html", "label": "Accueil"},
        {"file": "particuliers.html", "label": "Particuliers"},
        {"file": "pros.html", "label": "Pros"},
        {"file": "contact.html", "label": "Devis"},
    ],
)


def build_assurance_index():
    m = "<main>"
    m += block_hero_movento_split(
        "Assurances expliquées, devis simple",
        "Courtier à Strasbourg - particuliers et pros, contrats démêlés sans blabla.",
        "hero.png",
        "Couverture Est Strasbourg",
        eyebrow="Strasbourg · Courtage",
        primary_href="contact.html",
        primary_label="Demander un devis",
        secondary_href="particuliers.html",
        secondary_label="Particuliers",
        glass_pills=["Auto", "Habitation", "Pro"],
    )
    m += block_movento_feature_rows(
        "Offres",
        [
            ("Particuliers", "Auto, habitation, santé - on compare.", "card-1.png", "Assurance particuliers"),
            ("Pros", "RC pro, locaux, flotte.", "card-2.png", "Assurance pro"),
            ("Sinistre", "On t'oriente - pas seul face au dossier.", "card-3.png", "Sinistre"),
        ],
    )
    m += block_movento_quote(
        "Comparatif clair, un seul conseiller. J'ai compris mon contrat pour une fois.",
        author="Léa",
        role="Strasbourg",
    )
    m += block_movento_contact("Devis", AS["address"], cta_label="Envoyer", phone=AS["phone"], address=AS["address"])
    m += "</main>"
    return _shell(
        slug="assurance",
        brand=AS["brand"],
        phone=AS["phone"],
        address=AS["address"],
        email=AS["email"],
        maps=AS["maps"],
        nav=AS["nav"],
        page="index.html",
        title=f"{AS['brand']} - Assurance Strasbourg",
        desc="Courtier assurance à Strasbourg : particuliers et pros.",
        main=m,
        cta="Devis",
        hours="Strasbourg · Assurance",
        head=HEAD_SERIF,
        body_extra="vt-mv-assurance",
        layout="movento-assurance",
        nav_kind="underline",
    )


def build_assurance_particuliers():
    m = "<main>" + block_snap_chapter("Particuliers", "Auto, habitation, santé - devis comparé.", "scene-1.png", "Particuliers", cta_href="contact.html", cta_label="Devis") + "</main>"
    return _shell(slug="assurance", brand=AS["brand"], phone=AS["phone"], address=AS["address"], email=AS["email"], maps=AS["maps"], nav=AS["nav"], page="particuliers.html", title=f"Particuliers - {AS['brand']}", desc="Assurances particuliers Strasbourg.", main=m, cta="Devis", hours="Strasbourg · Assurance", head=HEAD_SERIF, body_extra="vt-mv-assurance", layout="movento-assurance", nav_kind="underline")


def build_assurance_pros():
    m = "<main>" + block_snap_chapter("Pros", "RC pro, locaux, flotte - besoins cadrés.", "scene-2.png", "Pros", reverse=True) + "</main>"
    return _shell(slug="assurance", brand=AS["brand"], phone=AS["phone"], address=AS["address"], email=AS["email"], maps=AS["maps"], nav=AS["nav"], page="pros.html", title=f"Pros - {AS['brand']}", desc="Assurances pros Strasbourg.", main=m, cta="Devis", hours="Strasbourg · Assurance", head=HEAD_SERIF, body_extra="vt-mv-assurance", layout="movento-assurance", nav_kind="underline")


def build_assurance_contact():
    m = "<main>" + block_movento_contact("Devis", AS["address"], cta_label="Envoyer", phone=AS["phone"], address=AS["address"]) + "</main>"
    return _shell(slug="assurance", brand=AS["brand"], phone=AS["phone"], address=AS["address"], email=AS["email"], maps=AS["maps"], nav=AS["nav"], page="contact.html", title=f"Contact - {AS['brand']}", desc="Devis Couverture Est Strasbourg.", main=m, cta="Devis", hours="Strasbourg · Assurance", head=HEAD_SERIF, body_extra="vt-mv-assurance", layout="movento-assurance", nav_kind="underline")


# --- Notaire : Etude Deschamps - minimal + center + services ---
NO = dict(
    brand="Étude Deschamps",
    phone="03 87 75 33 10",
    email="contact@etude-deschamps.fr",
    address="17 en Fournirue, 57000 Metz",
    maps="https://maps.google.com/?q=17+en+Fournirue+57000+Metz",
    nav=[
        {"file": "index.html", "label": "Accueil"},
        {"file": "domaines.html", "label": "Domaines"},
        {"file": "equipe.html", "label": "Équipe"},
        {"file": "contact.html", "label": "RDV"},
    ],
)


def build_notaire_index():
    m = "<main>"
    m += block_hero_movento_center(
        "Actes clairs, étude accessible",
        "Notaires à Metz - immobilier, famille, entreprise. RDV et délais annoncés.",
        eyebrow="Metz · Étude notariale",
        primary_href="contact.html",
        primary_label="Prendre RDV",
        secondary_href="domaines.html",
        secondary_label="Domaines",
    )
    m += block_movento_services(
        "Domaines",
        [
            {"title": "Immobilier", "text": "Vente, achat, donation - étapes datées.", "img": "card-1.png", "alt": "Notaire immobilier"},
            {"title": "Famille", "text": "Succession, mariage - écoute discrète.", "img": "card-2.png", "alt": "Notaire famille"},
            {"title": "Entreprise", "text": "Cession, statuts - avec ton conseil.", "img": "card-3.png", "alt": "Notaire entreprise"},
        ],
    )
    m += block_movento_quote(
        "Délais annoncés tenus. Un contact principal, pas dix interlocuteurs.",
        author="Hélène",
        role="Metz Fournirue",
    )
    m += block_movento_contact("Prendre RDV", NO["address"], cta_label="Envoyer", phone=NO["phone"], address=NO["address"])
    m += "</main>"
    return _shell(
        slug="notaire",
        brand=NO["brand"],
        phone=NO["phone"],
        address=NO["address"],
        email=NO["email"],
        maps=NO["maps"],
        nav=NO["nav"],
        page="index.html",
        title=f"{NO['brand']} - Notaire Metz",
        desc="Étude notariale à Metz : immobilier, famille, entreprise.",
        main=m,
        cta="RDV",
        hours="Metz · Notaire",
        head=HEAD_SERIF,
        body_extra="vt-mv-notaire",
        layout="movento-notaire",
        nav_kind="minimal",
    )


def build_notaire_domaines():
    m = "<main>" + block_snap_chapter("Domaines", "Immobilier, famille, entreprise - fiche claire par sujet.", "scene-1.png", "Domaines", cta_href="contact.html", cta_label="RDV") + "</main>"
    return _shell(slug="notaire", brand=NO["brand"], phone=NO["phone"], address=NO["address"], email=NO["email"], maps=NO["maps"], nav=NO["nav"], page="domaines.html", title=f"Domaines - {NO['brand']}", desc="Domaines Étude Deschamps.", main=m, cta="RDV", hours="Metz · Notaire", head=HEAD_SERIF, body_extra="vt-mv-notaire", layout="movento-notaire", nav_kind="minimal")


def build_notaire_equipe():
    m = "<main>" + block_snap_chapter("Équipe", "Notaires et clercs - un contact principal.", "scene-2.png", "Équipe", reverse=True) + "</main>"
    return _shell(slug="notaire", brand=NO["brand"], phone=NO["phone"], address=NO["address"], email=NO["email"], maps=NO["maps"], nav=NO["nav"], page="equipe.html", title=f"Équipe - {NO['brand']}", desc="Équipe Étude Deschamps.", main=m, cta="RDV", hours="Metz · Notaire", head=HEAD_SERIF, body_extra="vt-mv-notaire", layout="movento-notaire", nav_kind="minimal")


def build_notaire_contact():
    m = "<main>" + block_movento_contact("RDV", NO["address"], cta_label="Envoyer", phone=NO["phone"], address=NO["address"]) + "</main>"
    return _shell(slug="notaire", brand=NO["brand"], phone=NO["phone"], address=NO["address"], email=NO["email"], maps=NO["maps"], nav=NO["nav"], page="contact.html", title=f"Contact - {NO['brand']}", desc="RDV Étude Deschamps Metz.", main=m, cta="RDV", hours="Metz · Notaire", head=HEAD_SERIF, body_extra="vt-mv-notaire", layout="movento-notaire", nav_kind="minimal")


# --- Logistique : Flux Lorraine - solid + bleed + feature_rows ---
LO = dict(
    brand="Flux Lorraine",
    phone="03 29 34 81 50",
    email="ops@flux-lorraine.fr",
    address="Zone industrielle de la Voivre, 88000 Épinal",
    maps="https://maps.google.com/?q=Zone+industrielle+Voivre+88000+Epinal",
    nav=[
        {"file": "index.html", "label": "Accueil"},
        {"file": "services.html", "label": "Services"},
        {"file": "zones.html", "label": "Zones"},
        {"file": "contact.html", "label": "Devis"},
    ],
)


def build_logistique_index():
    m = "<main>"
    m += block_hero_movento_bleed(
        "Stockage et flux qui tiennent",
        "Logistique à Épinal : entrepôt, préparation, livraison Grand Est - devis opérationnel.",
        "hero.png",
        "Entrepôt Flux Lorraine Épinal",
        badge="Épinal · Voivre",
        primary_href="contact.html",
        primary_label="Demander un devis",
        phone_href=_tel(LO["phone"]),
        phone_label="Appeler ops",
        secondary_href="services.html",
        secondary_label="Services",
    )
    m += block_movento_feature_rows(
        "Capacités",
        [
            ("Stockage", "Emplacements et inventaire connus.", "card-1.png", "Entrepôt"),
            ("Préparation", "Commandes, colis, étiquetage.", "card-2.png", "Préparation commandes"),
            ("Livraison", "Tournées Grand Est - tracking simple.", "card-3.png", "Livraison"),
        ],
        lead="Brief clair. On avance.",
    )
    m += block_movento_steps(
        "Mise en place",
        [
            ("Cadrage", "Volumes, SLA, zones - on note net."),
            ("Intégration", "Flux testés avant le go-live."),
            ("Ops joignable", "Un numéro - pas une usine à tickets."),
        ],
    )
    m += block_movento_contact("Devis ops", LO["address"], cta_label="Envoyer", phone=LO["phone"], address=LO["address"])
    m += "</main>"
    return _shell(
        slug="logistique",
        brand=LO["brand"],
        phone=LO["phone"],
        address=LO["address"],
        email=LO["email"],
        maps=LO["maps"],
        nav=LO["nav"],
        page="index.html",
        title=f"{LO['brand']} - Logistique Épinal",
        desc="Logistique à Épinal : stockage, préparation, livraison Grand Est.",
        main=m,
        cta="Devis",
        hours="Épinal · Logistique",
        head=HEAD_TECH,
        body_extra="vt-mv-logistique",
        layout="movento-logistique",
        nav_kind="solid",
    )


def build_logistique_services():
    m = "<main>" + block_snap_chapter("Services", "Stockage, prep, transport - périmètre cadré.", "scene-1.png", "Services", cta_href="contact.html", cta_label="Devis") + "</main>"
    return _shell(slug="logistique", brand=LO["brand"], phone=LO["phone"], address=LO["address"], email=LO["email"], maps=LO["maps"], nav=LO["nav"], page="services.html", title=f"Services - {LO['brand']}", desc="Services Flux Lorraine.", main=m, cta="Devis", hours="Épinal · Logistique", head=HEAD_TECH, body_extra="vt-mv-logistique", layout="movento-logistique", nav_kind="solid")


def build_logistique_zones():
    m = f"""<main><section class="vt-mv-services"><div class="vt-mv-wrap">
    <p class="vt-mv-eyebrow">Zones</p>
    <h1 class="vt-mv-section-title">Grand Est</h1>
    <p class="vt-mv-lead">Vosges, Moselle, Meurthe-et-Moselle - tournées planifiées.</p>
    <p class="mt-4"><a class="vt-mv-btn vt-mv-btn-primary" href="contact.html">Demander un devis</a></p>
    </div></section></main>"""
    return _shell(slug="logistique", brand=LO["brand"], phone=LO["phone"], address=LO["address"], email=LO["email"], maps=LO["maps"], nav=LO["nav"], page="zones.html", title=f"Zones - {LO['brand']}", desc="Zones Flux Lorraine.", main=m, cta="Devis", hours="Épinal", head=HEAD_TECH, body_extra="vt-mv-logistique", layout="movento-logistique", nav_kind="solid")


def build_logistique_contact():
    m = "<main>" + block_movento_contact("Devis", LO["address"], cta_label="Envoyer", phone=LO["phone"], address=LO["address"]) + "</main>"
    return _shell(slug="logistique", brand=LO["brand"], phone=LO["phone"], address=LO["address"], email=LO["email"], maps=LO["maps"], nav=LO["nav"], page="contact.html", title=f"Contact - {LO['brand']}", desc="Devis Flux Lorraine Épinal.", main=m, cta="Devis", hours="Épinal · Logistique", head=HEAD_TECH, body_extra="vt-mv-logistique", layout="movento-logistique", nav_kind="solid")


# --- Photographie : Studio Lumiere Grise - pill + magazine + snap + quote ---
PH = dict(
    brand="Studio Lumière Grise",
    phone="03 87 21 45 60",
    email="bonjour@lumiere-grise.fr",
    address="12 rue des Clercs, 57000 Metz",
    maps="https://maps.google.com/?q=12+rue+des+Clercs+57000+Metz",
    nav=[
        {"file": "index.html", "label": "Accueil"},
        {"file": "portfolio.html", "label": "Portfolio"},
        {"file": "prestations.html", "label": "Prestations"},
        {"file": "contact.html", "label": "Devis"},
    ],
)


def build_photographie_index():
    m = "<main>"
    m += block_hero_movento_magazine(
        "Images qui portent ta marque",
        "Studio à Metz : reportage, portrait, produit - devis et moodboard avant shoot.",
        "hero.png",
        "Studio Lumière Grise Metz",
        eyebrow="Metz · Clercs",
        primary_href="portfolio.html",
        primary_label="Voir le portfolio",
        kicker="Studio photo",
    )
    m += block_snap_chapter(
        "Reportage & produit",
        "Événement, équipe, packshots - on cadre le ton avant d'appuyer.",
        "scene-1.png",
        "Reportage photo Metz",
        cta_href="contact.html",
        cta_label="Demander un devis",
    )
    m += block_movento_quote(
        "Moodboard clair, shoot fluide. Les images collent à la marque.",
        author="Inès",
        role="commerce Metz",
    )
    m += block_movento_contact("Devis shoot", PH["address"], cta_label="Envoyer", phone=PH["phone"], address=PH["address"])
    m += "</main>"
    return _shell(
        slug="photographie",
        brand=PH["brand"],
        phone=PH["phone"],
        address=PH["address"],
        email=PH["email"],
        maps=PH["maps"],
        nav=PH["nav"],
        page="index.html",
        title=f"{PH['brand']} - Photographe Metz",
        desc="Studio photo à Metz : portfolio, reportage, produit.",
        main=m,
        cta="Devis",
        hours="Metz · Photo",
        head=HEAD_TECH,
        body_extra="vt-mv-photo",
        layout="movento-photo",
        nav_kind="pill",
    )


def build_photographie_portfolio():
    m = "<main>" + block_snap_chapter("Portfolio", "Sélection récente - on adapte au ton de ta marque.", "scene-1.png", "Portfolio", cta_href="contact.html", cta_label="Devis") + "</main>"
    return _shell(slug="photographie", brand=PH["brand"], phone=PH["phone"], address=PH["address"], email=PH["email"], maps=PH["maps"], nav=PH["nav"], page="portfolio.html", title=f"Portfolio - {PH['brand']}", desc="Portfolio Lumière Grise.", main=m, cta="Devis", hours="Metz · Photo", head=HEAD_TECH, body_extra="vt-mv-photo", layout="movento-photo", nav_kind="pill")


def build_photographie_prestations():
    m = "<main>" + block_snap_chapter("Prestations", "Formules studio et extérieur - forfaits clairs.", "scene-2.png", "Prestations", reverse=True) + "</main>"
    return _shell(slug="photographie", brand=PH["brand"], phone=PH["phone"], address=PH["address"], email=PH["email"], maps=PH["maps"], nav=PH["nav"], page="prestations.html", title=f"Prestations - {PH['brand']}", desc="Prestations Lumière Grise.", main=m, cta="Devis", hours="Metz · Photo", head=HEAD_TECH, body_extra="vt-mv-photo", layout="movento-photo", nav_kind="pill")


def build_photographie_contact():
    m = "<main>" + block_movento_contact("Devis", PH["address"], cta_label="Envoyer", phone=PH["phone"], address=PH["address"]) + "</main>"
    return _shell(slug="photographie", brand=PH["brand"], phone=PH["phone"], address=PH["address"], email=PH["email"], maps=PH["maps"], nav=PH["nav"], page="contact.html", title=f"Contact - {PH['brand']}", desc="Devis Studio Lumière Grise Metz.", main=m, cta="Devis", hours="Metz · Photo", head=HEAD_TECH, body_extra="vt-mv-photo", layout="movento-photo", nav_kind="pill")


# --- Association : Solidarites Metz Metropole - underline + split + quote + steps ---
ASS = dict(
    brand="Solidarités Metz Métropole",
    phone="03 87 34 56 78",
    email="contact@solidarites-metz.fr",
    address="22 rue du Sablon, 57000 Metz",
    maps="https://maps.google.com/?q=22+rue+du+Sablon+57000+Metz",
    nav=[
        {"file": "index.html", "label": "Accueil"},
        {"file": "actions.html", "label": "Actions"},
        {"file": "benevolat.html", "label": "Bénévolat"},
        {"file": "contact.html", "label": "Contact"},
    ],
)


def build_association_index():
    m = "<main>"
    m += block_hero_movento_split(
        "Agir local, ensemble",
        "Association à Metz : actions terrain, bénévolat, dons - infos claires, permanences affichées.",
        "hero.png",
        "Solidarités Metz Métropole",
        eyebrow="Metz · Association",
        primary_href="benevolat.html",
        primary_label="Devenir bénévole",
        secondary_href="actions.html",
        secondary_label="Nos actions",
        glass_pills=["Actions", "Bénévolat", "Dons"],
    )
    m += block_movento_quote(
        "On m'a intégré en une permanence. Missions claires, pas de blabla.",
        author="Karim",
        role="bénévole Sablon",
    )
    m += block_movento_steps(
        "S'engager",
        [
            ("Tu écris ou tu passes", "Permanences lun-ven affichées."),
            ("On te présente une mission", "Courte ou régulière - cadre clair."),
            ("Tu agis sur le terrain", "Aide, accompagnement, événements."),
        ],
    )
    m += block_movento_contact("Nous écrire", ASS["address"], cta_label="Envoyer", phone=ASS["phone"], address=ASS["address"])
    m += "</main>"
    return _shell(
        slug="association",
        brand=ASS["brand"],
        phone=ASS["phone"],
        address=ASS["address"],
        email=ASS["email"],
        maps=ASS["maps"],
        nav=ASS["nav"],
        page="index.html",
        title=f"{ASS['brand']} - Association Metz",
        desc="Association à Metz : actions, bénévolat, contact.",
        main=m,
        cta="Contact",
        hours="Metz · Association",
        head=HEAD_SERIF,
        body_extra="vt-mv-association",
        layout="movento-association",
        nav_kind="underline",
    )


def build_association_actions():
    m = "<main>" + block_snap_chapter("Nos actions", "Sur le terrain - calendrier et besoins du mois.", "scene-1.png", "Actions", cta_href="benevolat.html", cta_label="Bénévolat") + "</main>"
    return _shell(slug="association", brand=ASS["brand"], phone=ASS["phone"], address=ASS["address"], email=ASS["email"], maps=ASS["maps"], nav=ASS["nav"], page="actions.html", title=f"Actions - {ASS['brand']}", desc="Actions Solidarités Metz.", main=m, cta="Contact", hours="Metz · Association", head=HEAD_SERIF, body_extra="vt-mv-association", layout="movento-association", nav_kind="underline")


def build_association_benevolat():
    m = "<main>" + block_snap_chapter("Bénévolat", "Missions courtes ou régulières - on t'explique le cadre.", "scene-2.png", "Bénévolat", reverse=True, cta_href="contact.html", cta_label="S'inscrire") + "</main>"
    return _shell(slug="association", brand=ASS["brand"], phone=ASS["phone"], address=ASS["address"], email=ASS["email"], maps=ASS["maps"], nav=ASS["nav"], page="benevolat.html", title=f"Bénévolat - {ASS['brand']}", desc="Bénévolat Solidarités Metz.", main=m, cta="Contact", hours="Metz · Association", head=HEAD_SERIF, body_extra="vt-mv-association", layout="movento-association", nav_kind="underline")


def build_association_contact():
    m = "<main>" + block_movento_contact("Contact", ASS["address"], cta_label="Envoyer", phone=ASS["phone"], address=ASS["address"]) + "</main>"
    return _shell(slug="association", brand=ASS["brand"], phone=ASS["phone"], address=ASS["address"], email=ASS["email"], maps=ASS["maps"], nav=ASS["nav"], page="contact.html", title=f"Contact - {ASS['brand']}", desc="Contacter Solidarités Metz Métropole.", main=m, cta="Contact", hours="Metz · Association", head=HEAD_SERIF, body_extra="vt-mv-association", layout="movento-association", nav_kind="underline")


BUILDERS_MOVENTO_VAGUE_D = {
    "electricien": [
        ("index.html", build_electricien_index),
        ("services.html", build_electricien_services),
        ("zones.html", build_electricien_zones),
        ("contact.html", build_electricien_contact),
    ],
    "architecture": [
        ("index.html", build_architecture_index),
        ("projets.html", build_architecture_projets),
        ("methode.html", build_architecture_methode),
        ("contact.html", build_architecture_contact),
    ],
    "promoteur": [
        ("index.html", build_promoteur_index),
        ("programmes.html", build_promoteur_programmes),
        ("accompagnement.html", build_promoteur_accompagnement),
        ("contact.html", build_promoteur_contact),
    ],
    "comptable": [
        ("index.html", build_comptable_index),
        ("expertises.html", build_comptable_expertises),
        ("methode.html", build_comptable_methode),
        ("contact.html", build_comptable_contact),
    ],
    "assurance": [
        ("index.html", build_assurance_index),
        ("particuliers.html", build_assurance_particuliers),
        ("pros.html", build_assurance_pros),
        ("contact.html", build_assurance_contact),
    ],
    "notaire": [
        ("index.html", build_notaire_index),
        ("domaines.html", build_notaire_domaines),
        ("equipe.html", build_notaire_equipe),
        ("contact.html", build_notaire_contact),
    ],
    "logistique": [
        ("index.html", build_logistique_index),
        ("services.html", build_logistique_services),
        ("zones.html", build_logistique_zones),
        ("contact.html", build_logistique_contact),
    ],
    "photographie": [
        ("index.html", build_photographie_index),
        ("portfolio.html", build_photographie_portfolio),
        ("prestations.html", build_photographie_prestations),
        ("contact.html", build_photographie_contact),
    ],
    "association": [
        ("index.html", build_association_index),
        ("actions.html", build_association_actions),
        ("benevolat.html", build_association_benevolat),
        ("contact.html", build_association_contact),
    ],
}
