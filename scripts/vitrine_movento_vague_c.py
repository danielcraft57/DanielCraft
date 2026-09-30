"""Redesign Movento vague C - 9 metiers food / bien-etre / sante.

Slugs : boulangerie, chocolaterie, traiteur, fleuriste, caviste,
coiffure, yoga, kine, osteo.

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
    block_movento_menu_list,
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

HEAD_WARM = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
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


# --- Boulangerie : Maison Lemaire - magazine + menu_list + solid ---
BL = dict(
    brand="Maison Lemaire",
    phone="03 83 35 12 40",
    email="bonjour@maison-lemaire.fr",
    address="14 allée de la Pépinière, 54000 Nancy",
    maps="https://maps.google.com/?q=14+allee+de+la+Pepiniere+54000+Nancy",
    nav=[
        {"file": "index.html", "label": "Accueil"},
        {"file": "pains.html", "label": "Pains"},
        {"file": "patisseries.html", "label": "Pâtisseries"},
        {"file": "contact.html", "label": "Contact"},
    ],
)


def build_boulangerie_index():
    m = "<main>"
    m += block_hero_movento_magazine(
        "Le fournil, version claire",
        "Pains au levain, viennoiseries et pâtisseries à Nancy - tu commandes avant, tu récupères chaud.",
        "hero.png",
        "Fournil Maison Lemaire Nancy",
        eyebrow="Nancy · Fournil artisanal",
        primary_href="contact.html",
        primary_label="Commander",
        kicker="Ouvert dès 7 h",
    )
    m += block_movento_menu_list(
        "Au comptoir (aperçu)",
        [
            ("Tradition levain", "Fournée du matin", "1,35 €"),
            ("Croissant beurre", "Pur beurre AOP", "1,40 €"),
            ("Tarte mirabelle", "Week-end seulement", "3,80 €"),
        ],
        lead="Comme au marché : tu goûtes avant de remplir le cornet.",
        cta_href="contact.html",
        cta_label="Commander pour demain",
    )
    m += block_movento_quote(
        "Pain encore chaud à 7 h 10. On y revient chaque samedi.",
        author="Julien",
        role="Nancy Pépinière",
    )
    m += block_movento_contact(
        "Commander pour demain", BL["address"], cta_label="Envoyer", phone=BL["phone"], address=BL["address"]
    )
    m += "</main>"
    return _shell(
        slug="boulangerie",
        brand=BL["brand"],
        phone=BL["phone"],
        address=BL["address"],
        email=BL["email"],
        maps=BL["maps"],
        nav=BL["nav"],
        page="index.html",
        title=f"{BL['brand']} - Boulangerie Nancy",
        desc="Boulangerie artisanale à Nancy : pains au levain, viennoiseries, commande simple.",
        main=m,
        cta="Commander",
        hours="Nancy · Fournil",
        head=HEAD_WARM,
        body_extra="vt-body-boulangerie vt-mv-boulangerie",
        layout="movento-boulangerie",
        nav_kind="solid",
    )


def build_boulangerie_pains():
    m = "<main>" + block_snap_chapter("Pains au levain", "Tradition, campagne, graines - fournées du jour affichées.", "scene-1.png", "Pains", cta_href="contact.html", cta_label="Commander") + "</main>"
    return _shell(slug="boulangerie", brand=BL["brand"], phone=BL["phone"], address=BL["address"], email=BL["email"], maps=BL["maps"], nav=BL["nav"], page="pains.html", title=f"Pains - {BL['brand']}", desc="Pains au levain Maison Lemaire Nancy.", main=m, cta="Commander", hours="Nancy · Fournil", head=HEAD_WARM, body_extra="vt-body-boulangerie vt-mv-boulangerie", layout="movento-boulangerie", nav_kind="solid")


def build_boulangerie_patisseries():
    m = "<main>" + block_snap_chapter("Pâtisseries & viennoiseries", "Du croissant du matin à la tarte du dimanche.", "scene-2.png", "Pâtisseries", reverse=True) + "</main>"
    return _shell(slug="boulangerie", brand=BL["brand"], phone=BL["phone"], address=BL["address"], email=BL["email"], maps=BL["maps"], nav=BL["nav"], page="patisseries.html", title=f"Pâtisseries - {BL['brand']}", desc="Pâtisseries Maison Lemaire Nancy.", main=m, cta="Commander", hours="Nancy · Fournil", head=HEAD_WARM, body_extra="vt-body-boulangerie vt-mv-boulangerie", layout="movento-boulangerie", nav_kind="solid")


def build_boulangerie_contact():
    m = "<main>" + block_movento_contact("Commander", BL["address"], cta_label="Envoyer", phone=BL["phone"], address=BL["address"]) + "</main>"
    return _shell(slug="boulangerie", brand=BL["brand"], phone=BL["phone"], address=BL["address"], email=BL["email"], maps=BL["maps"], nav=BL["nav"], page="contact.html", title=f"Contact - {BL['brand']}", desc="Commander chez Maison Lemaire Nancy.", main=m, cta="Commander", hours="Nancy · Fournil", head=HEAD_WARM, body_extra="vt-body-boulangerie vt-mv-boulangerie", layout="movento-boulangerie", nav_kind="solid")


# --- Chocolaterie : Maison Mirabelle - center + quote + pill ---
CH = dict(
    brand="Maison Mirabelle",
    phone="03 87 18 42 10",
    email="bonjour@maison-mirabelle.fr",
    address="8 rue des Clercs, 57000 Metz",
    maps="https://maps.google.com/?q=8+rue+des+Clercs+57000+Metz",
    nav=[
        {"file": "index.html", "label": "Accueil"},
        {"file": "chocolats.html", "label": "Chocolats"},
        {"file": "atelier.html", "label": "Atelier"},
        {"file": "contact.html", "label": "Contact"},
    ],
)


def build_chocolaterie_index():
    m = "<main>"
    m += block_hero_movento_center(
        "Chocolat qui sent le vrai",
        "Tablettes, praliné et saison - boutique Clercs à Metz, commande pour les fêtes sans stress.",
        eyebrow="Metz · Chocolaterie",
        primary_href="contact.html",
        primary_label="Commander",
        secondary_href="chocolats.html",
        secondary_label="Voir les chocolats",
        img="hero.png",
        alt="Chocolaterie Maison Mirabelle Metz",
    )
    m += block_movento_steps(
        "Commander pour les fêtes",
        [
            ("Tu choisis", "Tablettes, boîtes, saison - stocks affichés."),
            ("On confirme", "Date de retrait ou livraison quartier."),
            ("Tu récupères", "Emballage prêt - sans file d'attente inutile."),
        ],
        lead="Pas trois cartes clones - un vrai déroulé.",
    )
    m += block_movento_quote(
        "Commande Noël récupérée pile à l'heure. Praliné nickel.",
        author="Claire",
        role="cliente Clercs",
    )
    m += block_movento_contact("Commander", CH["address"], cta_label="Envoyer", phone=CH["phone"], address=CH["address"])
    m += "</main>"
    return _shell(
        slug="chocolaterie",
        brand=CH["brand"],
        phone=CH["phone"],
        address=CH["address"],
        email=CH["email"],
        maps=CH["maps"],
        nav=CH["nav"],
        page="index.html",
        title=f"{CH['brand']} - Chocolaterie Metz",
        desc="Chocolaterie à Metz : tablettes, praliné, commandes fêtes.",
        main=m,
        cta="Commander",
        hours="Metz · Chocolaterie",
        head=HEAD_WARM,
        body_extra="vt-mv-chocolaterie",
        layout="movento-chocolaterie",
        nav_kind="minimal",
    )


def build_chocolaterie_chocolats():
    m = "<main>" + block_snap_chapter("Chocolats", "Tablettes et boîtes - sélection courte, goût long.", "scene-1.png", "Chocolats", cta_href="contact.html", cta_label="Commander") + "</main>"
    return _shell(slug="chocolaterie", brand=CH["brand"], phone=CH["phone"], address=CH["address"], email=CH["email"], maps=CH["maps"], nav=CH["nav"], page="chocolats.html", title=f"Chocolats - {CH['brand']}", desc="Chocolats Maison Mirabelle Metz.", main=m, cta="Commander", hours="Metz · Chocolaterie", head=HEAD_WARM, body_extra="vt-mv-chocolaterie", layout="movento-chocolaterie", nav_kind="minimal")


def build_chocolaterie_atelier():
    m = "<main>" + block_snap_chapter("L'atelier", "On voit travailler - et on explique sans jargon.", "scene-2.png", "Atelier", reverse=True) + "</main>"
    return _shell(slug="chocolaterie", brand=CH["brand"], phone=CH["phone"], address=CH["address"], email=CH["email"], maps=CH["maps"], nav=CH["nav"], page="atelier.html", title=f"Atelier - {CH['brand']}", desc="Atelier Maison Mirabelle Metz.", main=m, cta="Commander", hours="Metz · Chocolaterie", head=HEAD_WARM, body_extra="vt-mv-chocolaterie", layout="movento-chocolaterie", nav_kind="minimal")


def build_chocolaterie_contact():
    m = "<main>" + block_movento_contact("Commander", CH["address"], cta_label="Envoyer", phone=CH["phone"], address=CH["address"]) + "</main>"
    return _shell(slug="chocolaterie", brand=CH["brand"], phone=CH["phone"], address=CH["address"], email=CH["email"], maps=CH["maps"], nav=CH["nav"], page="contact.html", title=f"Contact - {CH['brand']}", desc="Contacter Maison Mirabelle Metz.", main=m, cta="Commander", hours="Metz · Chocolaterie", head=HEAD_WARM, body_extra="vt-mv-chocolaterie", layout="movento-chocolaterie", nav_kind="minimal")


# --- Traiteur : Table & Cornet - bleed + feature_rows ---
TR = dict(
    brand="Table & Cornet",
    phone="03 83 27 61 40",
    email="events@table-cornet.fr",
    address="19 rue Stanislas, 54000 Nancy",
    maps="https://maps.google.com/?q=19+rue+Stanislas+54000+Nancy",
    nav=[
        {"file": "index.html", "label": "Accueil"},
        {"file": "menus.html", "label": "Menus"},
        {"file": "evenements.html", "label": "Événements"},
        {"file": "contact.html", "label": "Devis"},
    ],
)


def build_traiteur_index():
    m = "<main>"
    m += block_hero_movento_bleed(
        "Réceptions sans prise de tête",
        "Menus, buffets et événements à Nancy - devis clair, livraison à l'heure.",
        "hero.png",
        "Traiteur Table et Cornet Nancy",
        badge="Nancy · Traiteur événements",
        primary_href="contact.html",
        primary_label="Demander un devis",
        phone_href=_tel(TR["phone"]),
        phone_label="Appeler",
        secondary_href="menus.html",
        secondary_label="Voir les menus",
    )
    m += block_movento_feature_rows(
        "Formules",
        [
            ("Menus", "Assis ou buffet - tu choisis le ton.", "card-1.png", "Menus traiteur"),
            ("Événements", "Mariage, entreprise, fête de famille.", "card-2.png", "Événement"),
            ("Livraison", "Horaires tenus - on confirme la veille.", "card-3.png", "Livraison traiteur"),
        ],
        lead="Des bandes photo + texte, pas trois cartes identiques.",
    )
    m += block_movento_steps(
        "Comment ça se passe",
        [
            ("Brief", "Date, lieu, nombre - on note net."),
            ("Devis", "Sous 48 h type - prix affiché."),
            ("Jour J", "Livraison ou service - un seul interlocuteur."),
        ],
    )
    m += block_movento_contact("Devis événement", TR["address"], cta_label="Envoyer", phone=TR["phone"], address=TR["address"])
    m += "</main>"
    return _shell(
        slug="traiteur",
        brand=TR["brand"],
        phone=TR["phone"],
        address=TR["address"],
        email=TR["email"],
        maps=TR["maps"],
        nav=TR["nav"],
        page="index.html",
        title=f"{TR['brand']} - Traiteur Nancy",
        desc="Traiteur à Nancy : menus, buffets, devis événements.",
        main=m,
        cta="Devis",
        hours="Nancy · Traiteur",
        head=HEAD_WARM,
        body_extra="vt-mv-traiteur",
        layout="movento-traiteur",
        nav_kind="solid",
    )


def build_traiteur_menus():
    m = "<main>" + block_snap_chapter("Menus", "Formules saisonnières - prix affichés sans surprise.", "scene-1.png", "Menus", cta_href="contact.html", cta_label="Devis") + "</main>"
    return _shell(slug="traiteur", brand=TR["brand"], phone=TR["phone"], address=TR["address"], email=TR["email"], maps=TR["maps"], nav=TR["nav"], page="menus.html", title=f"Menus - {TR['brand']}", desc="Menus Table & Cornet Nancy.", main=m, cta="Devis", hours="Nancy · Traiteur", head=HEAD_WARM, body_extra="vt-mv-traiteur", layout="movento-traiteur", nav_kind="solid")


def build_traiteur_evenements():
    m = "<main>" + block_snap_chapter("Événements", "Mariage, séminaire, fête - on cadre le brief ensemble.", "scene-2.png", "Événements", reverse=True) + "</main>"
    return _shell(slug="traiteur", brand=TR["brand"], phone=TR["phone"], address=TR["address"], email=TR["email"], maps=TR["maps"], nav=TR["nav"], page="evenements.html", title=f"Événements - {TR['brand']}", desc="Événements Table & Cornet.", main=m, cta="Devis", hours="Nancy · Traiteur", head=HEAD_WARM, body_extra="vt-mv-traiteur", layout="movento-traiteur", nav_kind="solid")


def build_traiteur_contact():
    m = "<main>" + block_movento_contact("Devis", TR["address"], cta_label="Envoyer", phone=TR["phone"], address=TR["address"]) + "</main>"
    return _shell(slug="traiteur", brand=TR["brand"], phone=TR["phone"], address=TR["address"], email=TR["email"], maps=TR["maps"], nav=TR["nav"], page="contact.html", title=f"Contact - {TR['brand']}", desc="Devis traiteur Nancy.", main=m, cta="Devis", hours="Nancy · Traiteur", head=HEAD_WARM, body_extra="vt-mv-traiteur", layout="movento-traiteur", nav_kind="solid")


# --- Fleuriste : Atelier Corolle - split + quote + menu ---
FL = dict(
    brand="Atelier Corolle",
    phone="03 88 24 17 50",
    email="bonjour@atelier-corolle.fr",
    address="22 rue de l'Orangerie, 67000 Strasbourg",
    maps="https://maps.google.com/?q=22+rue+de+l+Orangerie+67000+Strasbourg",
    nav=[
        {"file": "index.html", "label": "Accueil"},
        {"file": "collections.html", "label": "Collections"},
        {"file": "mariage.html", "label": "Mariage"},
        {"file": "contact.html", "label": "Commander"},
    ],
)


def build_fleuriste_index():
    m = "<main>"
    m += block_hero_movento_split(
        "Bouquets de saison, livraison douce",
        "Fleuriste Orangerie à Strasbourg - compositions, mariage, livraison quartier.",
        "hero.png",
        "Atelier Corolle Strasbourg",
        eyebrow="Strasbourg · Orangerie",
        primary_href="contact.html",
        primary_label="Commander",
        secondary_href="collections.html",
        secondary_label="Collections",
        glass_pills=["Saison", "Mariage", "Livraison"],
    )
    m += block_movento_quote(
        "Bouquet livré pile pour l'anniversaire. Couleurs juste ce qu'il faut.",
        author="Émilie",
        role="Orangerie",
    )
    m += block_movento_menu_list(
        "Collections du moment",
        [
            ("Bouquet marché", "Saison · taille M", "45 €"),
            ("Composition table", "Vase inclus", "65 €"),
            ("Essai mariage", "Sur RDV atelier", "sur devis"),
        ],
        lead="Prix affichés - on ajuste selon ton budget.",
        cta_href="contact.html",
        cta_label="Commander un bouquet",
    )
    m += block_movento_contact("Commander un bouquet", FL["address"], cta_label="Envoyer", phone=FL["phone"], address=FL["address"])
    m += "</main>"
    return _shell(
        slug="fleuriste",
        brand=FL["brand"],
        phone=FL["phone"],
        address=FL["address"],
        email=FL["email"],
        maps=FL["maps"],
        nav=FL["nav"],
        page="index.html",
        title=f"{FL['brand']} - Fleuriste Strasbourg",
        desc="Fleuriste à Strasbourg : bouquets, mariage, livraison.",
        main=m,
        cta="Commander",
        hours="Strasbourg · Fleuriste",
        head=HEAD_SERIF,
        body_extra="vt-body-fleuriste vt-mv-fleuriste",
        layout="movento-fleuriste",
        nav_kind="pill",
    )


def build_fleuriste_collections():
    m = "<main>" + block_snap_chapter("Collections", "Bouquets de saison - on ajuste selon ton budget.", "scene-1.png", "Collections", cta_href="contact.html", cta_label="Commander") + "</main>"
    return _shell(slug="fleuriste", brand=FL["brand"], phone=FL["phone"], address=FL["address"], email=FL["email"], maps=FL["maps"], nav=FL["nav"], page="collections.html", title=f"Collections - {FL['brand']}", desc="Collections Atelier Corolle.", main=m, cta="Commander", hours="Strasbourg · Fleuriste", head=HEAD_SERIF, body_extra="vt-body-fleuriste vt-mv-fleuriste", layout="movento-fleuriste", nav_kind="pill")


def build_fleuriste_mariage():
    m = "<main>" + block_snap_chapter("Mariage", "Essai bouquet, arche, boutonnières - un seul fil.", "scene-2.png", "Mariage", reverse=True) + "</main>"
    return _shell(slug="fleuriste", brand=FL["brand"], phone=FL["phone"], address=FL["address"], email=FL["email"], maps=FL["maps"], nav=FL["nav"], page="mariage.html", title=f"Mariage - {FL['brand']}", desc="Fleurs de mariage Strasbourg.", main=m, cta="Commander", hours="Strasbourg · Fleuriste", head=HEAD_SERIF, body_extra="vt-body-fleuriste vt-mv-fleuriste", layout="movento-fleuriste", nav_kind="pill")


def build_fleuriste_contact():
    m = "<main>" + block_movento_contact("Commander", FL["address"], cta_label="Envoyer", phone=FL["phone"], address=FL["address"]) + "</main>"
    return _shell(slug="fleuriste", brand=FL["brand"], phone=FL["phone"], address=FL["address"], email=FL["email"], maps=FL["maps"], nav=FL["nav"], page="contact.html", title=f"Contact - {FL['brand']}", desc="Contacter Atelier Corolle Strasbourg.", main=m, cta="Commander", hours="Strasbourg · Fleuriste", head=HEAD_SERIF, body_extra="vt-body-fleuriste vt-mv-fleuriste", layout="movento-fleuriste", nav_kind="pill")


# --- Caviste : Cave de la Gare - magazine + feature_rows ---
CV = dict(
    brand="Cave de la Gare",
    phone="03 82 53 18 90",
    email="cave@cavedelagare.fr",
    address="5 place de la Gare, 57100 Thionville",
    maps="https://maps.google.com/?q=5+place+de+la+Gare+57100+Thionville",
    nav=[
        {"file": "index.html", "label": "Accueil"},
        {"file": "vins.html", "label": "Vins"},
        {"file": "cave.html", "label": "La cave"},
        {"file": "contact.html", "label": "Contact"},
    ],
)


def build_caviste_index():
    m = "<main>"
    m += block_hero_movento_magazine(
        "Une cave qui conseille vraiment",
        "Sélection courte à Thionville - dégustations samedi, conseils sans snobisme.",
        "hero.png",
        "Cave de la Gare Thionville",
        eyebrow="Thionville · Place de la Gare",
        primary_href="vins.html",
        primary_label="Voir les vins",
        kicker="Dégustations samedi",
    )
    m += block_movento_stat_band(
        [("Samedi", "dégustations"), ("Conseil", "sur place"), ("France", "+ Europe"), ("Panier", "click & collect")]
    )
    m += block_movento_feature_rows(
        "En rayon",
        [
            ("Vins", "Sélection courte - on explique pourquoi.", "card-1.png", "Bouteilles de vin"),
            ("La cave", "Ambiance, température, conseils accords.", "card-2.png", "Cave à vin"),
            ("Dégustations", "Samedi - places limitées.", "card-3.png", "Dégustation"),
        ],
    )
    m += block_movento_contact("Réserver une dégustation", CV["address"], cta_label="Envoyer", phone=CV["phone"], address=CV["address"])
    m += "</main>"
    return _shell(
        slug="caviste",
        brand=CV["brand"],
        phone=CV["phone"],
        address=CV["address"],
        email=CV["email"],
        maps=CV["maps"],
        nav=CV["nav"],
        page="index.html",
        title=f"{CV['brand']} - Caviste Thionville",
        desc="Caviste à Thionville : sélection, conseils, dégustations.",
        main=m,
        cta="Contact",
        hours="Thionville · Caviste",
        head=HEAD_SERIF,
        body_extra="vt-body-caviste vt-mv-caviste",
        layout="movento-caviste",
        nav_kind="underline",
    )


def build_caviste_vins():
    m = "<main>" + block_snap_chapter("Vins", "Sélection courte - France et Europe, prix affichés.", "scene-1.png", "Vins", cta_href="contact.html", cta_label="Demander conseil") + "</main>"
    return _shell(slug="caviste", brand=CV["brand"], phone=CV["phone"], address=CV["address"], email=CV["email"], maps=CV["maps"], nav=CV["nav"], page="vins.html", title=f"Vins - {CV['brand']}", desc="Catalogue Cave de la Gare.", main=m, cta="Contact", hours="Thionville · Caviste", head=HEAD_SERIF, body_extra="vt-body-caviste vt-mv-caviste", layout="movento-caviste", nav_kind="underline")


def build_caviste_cave():
    m = "<main>" + block_snap_chapter("La cave", "Place de la Gare - on prend le temps.", "scene-2.png", "Cave", reverse=True) + "</main>"
    return _shell(slug="caviste", brand=CV["brand"], phone=CV["phone"], address=CV["address"], email=CV["email"], maps=CV["maps"], nav=CV["nav"], page="cave.html", title=f"La cave - {CV['brand']}", desc="La cave Cave de la Gare.", main=m, cta="Contact", hours="Thionville · Caviste", head=HEAD_SERIF, body_extra="vt-body-caviste vt-mv-caviste", layout="movento-caviste", nav_kind="underline")


def build_caviste_contact():
    m = "<main>" + block_movento_contact("Contact", CV["address"], cta_label="Envoyer", phone=CV["phone"], address=CV["address"]) + "</main>"
    return _shell(slug="caviste", brand=CV["brand"], phone=CV["phone"], address=CV["address"], email=CV["email"], maps=CV["maps"], nav=CV["nav"], page="contact.html", title=f"Contact - {CV['brand']}", desc="Contacter Cave de la Gare.", main=m, cta="Contact", hours="Thionville · Caviste", head=HEAD_SERIF, body_extra="vt-body-caviste vt-mv-caviste", layout="movento-caviste", nav_kind="underline")


# --- Coiffure : Salon Rivage - center + menu ---
CF = dict(
    brand="Salon Rivage",
    phone="03 82 54 19 30",
    email="rdv@salon-rivage.fr",
    address="12 avenue de la Liberté, 57100 Thionville",
    maps="https://maps.google.com/?q=12+avenue+de+la+Liberte+57100+Thionville",
    nav=[
        {"file": "index.html", "label": "Accueil"},
        {"file": "soins.html", "label": "Soins"},
        {"file": "equipe.html", "label": "Équipe"},
        {"file": "contact.html", "label": "RDV"},
    ],
)


def build_coiffure_index():
    m = "<main>"
    m += block_hero_movento_center(
        "Coupe, couleur, du temps pour toi",
        "Salon à Thionville - fiches soins claires, RDV simple, équipe à l'écoute.",
        eyebrow="Thionville · Coiffure",
        primary_href="contact.html",
        primary_label="Prendre RDV",
        secondary_href="soins.html",
        secondary_label="Voir les soins",
        img="hero.png",
        alt="Salon Rivage Thionville",
    )
    m += block_movento_menu_list(
        "Carte des soins (aperçu)",
        [
            ("Coupe femme", "Shampoing + coiffage", "38 €"),
            ("Couleur", "Diagnostic avant", "à partir de 55 €"),
            ("Soin masque", "Sans upsell forcé", "18 €"),
        ],
        lead="Tarifs affichés - tu réserves, on confirme.",
        cta_href="contact.html",
        cta_label="Prendre RDV",
    )
    m += block_movento_quote(
        "Même coiffeuse à chaque fois. Ça change tout.",
        author="Nadia",
        role="Thionville",
    )
    m += block_movento_contact("Prendre RDV", CF["address"], cta_label="Envoyer", phone=CF["phone"], address=CF["address"])
    m += "</main>"
    return _shell(
        slug="coiffure",
        brand=CF["brand"],
        phone=CF["phone"],
        address=CF["address"],
        email=CF["email"],
        maps=CF["maps"],
        nav=CF["nav"],
        page="index.html",
        title=f"{CF['brand']} - Coiffure Thionville",
        desc="Salon de coiffure à Thionville : coupe, couleur, RDV.",
        main=m,
        cta="RDV",
        hours="Thionville · Coiffure",
        head=HEAD_SERIF,
        body_extra="vt-mv-coiffure",
        layout="movento-coiffure",
        nav_kind="minimal",
    )


def build_coiffure_soins():
    m = "<main>" + block_snap_chapter("Soins", "Coupe, couleur, soins - tarifs sur la fiche.", "scene-1.png", "Soins", cta_href="contact.html", cta_label="RDV") + "</main>"
    return _shell(slug="coiffure", brand=CF["brand"], phone=CF["phone"], address=CF["address"], email=CF["email"], maps=CF["maps"], nav=CF["nav"], page="soins.html", title=f"Soins - {CF['brand']}", desc="Soins Salon Rivage.", main=m, cta="RDV", hours="Thionville · Coiffure", head=HEAD_SERIF, body_extra="vt-mv-coiffure", layout="movento-coiffure", nav_kind="minimal")


def build_coiffure_equipe():
    m = "<main>" + block_snap_chapter("L'équipe", "Tu retrouves la même personne - pas de roulette.", "scene-2.png", "Équipe", reverse=True) + "</main>"
    return _shell(slug="coiffure", brand=CF["brand"], phone=CF["phone"], address=CF["address"], email=CF["email"], maps=CF["maps"], nav=CF["nav"], page="equipe.html", title=f"Équipe - {CF['brand']}", desc="Équipe Salon Rivage.", main=m, cta="RDV", hours="Thionville · Coiffure", head=HEAD_SERIF, body_extra="vt-mv-coiffure", layout="movento-coiffure", nav_kind="minimal")


def build_coiffure_contact():
    m = "<main>" + block_movento_contact("RDV", CF["address"], cta_label="Envoyer", phone=CF["phone"], address=CF["address"]) + "</main>"
    return _shell(slug="coiffure", brand=CF["brand"], phone=CF["phone"], address=CF["address"], email=CF["email"], maps=CF["maps"], nav=CF["nav"], page="contact.html", title=f"Contact - {CF['brand']}", desc="RDV Salon Rivage Thionville.", main=m, cta="RDV", hours="Thionville · Coiffure", head=HEAD_SERIF, body_extra="vt-mv-coiffure", layout="movento-coiffure", nav_kind="minimal")


# --- Yoga : Studio Souffle - bleed + steps ---
YO = dict(
    brand="Studio Souffle",
    phone="03 87 42 56 80",
    email="hello@studio-souffle.fr",
    address="11 rue du Palais, 57000 Metz",
    maps="https://maps.google.com/?q=11+rue+du+Palais+57000+Metz",
    nav=[
        {"file": "index.html", "label": "Accueil"},
        {"file": "cours.html", "label": "Cours"},
        {"file": "planning.html", "label": "Planning"},
        {"file": "contact.html", "label": "Essai"},
    ],
)


def build_yoga_index():
    m = "<main>"
    m += block_hero_movento_bleed(
        "Respirer à Metz, sans pression",
        "Cours de yoga rue du Palais - niveaux clairs, essai simple, planning lisible.",
        "hero.png",
        "Studio Souffle Metz",
        badge="Metz · Yoga",
        primary_href="contact.html",
        primary_label="Réserver un essai",
        phone_href=_tel(YO["phone"]),
        phone_label="Appeler",
        secondary_href="planning.html",
        secondary_label="Voir le planning",
    )
    m += block_movento_steps(
        "Premier essai",
        [
            ("Tu choisis un créneau", "Planning affiché - petits groupes."),
            ("On t'oriente", "Hatha, vinyasa ou douceur - selon ton niveau."),
            ("Tu goûtes", "Une séance - sans abonnement forcé."),
        ],
        lead="Pas de grille de cartes photo : un vrai parcours.",
    )
    m += block_movento_quote(
        "Studio calme, prof claire. J'ai repris sans me sentir nulle.",
        author="Sophie",
        role="Metz centre",
    )
    m += block_movento_contact("Réserver un essai", YO["address"], cta_label="Envoyer", phone=YO["phone"], address=YO["address"])
    m += "</main>"
    return _shell(
        slug="yoga",
        brand=YO["brand"],
        phone=YO["phone"],
        address=YO["address"],
        email=YO["email"],
        maps=YO["maps"],
        nav=YO["nav"],
        page="index.html",
        title=f"{YO['brand']} - Yoga Metz",
        desc="Studio de yoga à Metz : cours, planning, essai.",
        main=m,
        cta="Essai",
        hours="Metz · Yoga",
        head=HEAD_SERIF,
        body_extra="vt-mv-yoga",
        layout="movento-yoga",
        nav_kind="solid",
    )


def build_yoga_cours():
    m = "<main>" + block_snap_chapter("Cours", "Niveaux et durées - tu sais où tu mets les pieds.", "scene-1.png", "Cours", cta_href="contact.html", cta_label="Essai") + "</main>"
    return _shell(slug="yoga", brand=YO["brand"], phone=YO["phone"], address=YO["address"], email=YO["email"], maps=YO["maps"], nav=YO["nav"], page="cours.html", title=f"Cours - {YO['brand']}", desc="Cours Studio Souffle Metz.", main=m, cta="Essai", hours="Metz · Yoga", head=HEAD_SERIF, body_extra="vt-mv-yoga", layout="movento-yoga", nav_kind="solid")


def build_yoga_planning():
    m = "<main>" + block_snap_chapter("Planning", "Semaine type - on confirme les places au téléphone.", "scene-2.png", "Planning", reverse=True) + "</main>"
    return _shell(slug="yoga", brand=YO["brand"], phone=YO["phone"], address=YO["address"], email=YO["email"], maps=YO["maps"], nav=YO["nav"], page="planning.html", title=f"Planning - {YO['brand']}", desc="Planning Studio Souffle.", main=m, cta="Essai", hours="Metz · Yoga", head=HEAD_SERIF, body_extra="vt-mv-yoga", layout="movento-yoga", nav_kind="solid")


def build_yoga_contact():
    m = "<main>" + block_movento_contact("Essai", YO["address"], cta_label="Envoyer", phone=YO["phone"], address=YO["address"]) + "</main>"
    return _shell(slug="yoga", brand=YO["brand"], phone=YO["phone"], address=YO["address"], email=YO["email"], maps=YO["maps"], nav=YO["nav"], page="contact.html", title=f"Contact - {YO['brand']}", desc="Essai Studio Souffle Metz.", main=m, cta="Essai", hours="Metz · Yoga", head=HEAD_SERIF, body_extra="vt-mv-yoga", layout="movento-yoga", nav_kind="solid")


# --- Kine : Kinesia Metz - split + steps + stat ---
KI = dict(
    brand="Kinesia Metz",
    phone="03 87 63 28 15",
    email="accueil@kinesia-metz.fr",
    address="5 rue Serpenoise, 57000 Metz",
    maps="https://maps.google.com/?q=5+rue+Serpenoise+57000+Metz",
    nav=[
        {"file": "index.html", "label": "Accueil"},
        {"file": "soins.html", "label": "Soins"},
        {"file": "equipe.html", "label": "Équipe"},
        {"file": "contact.html", "label": "RDV"},
    ],
)


def build_kine_index():
    m = "<main>"
    m += block_hero_movento_split(
        "Remettre le corps en marche",
        "Kinésithérapie à Metz - RDV clair, soins expliqués, équipe stable.",
        "hero.png",
        "Cabinet Kinesia Metz",
        eyebrow="Metz · Kinésithérapie",
        primary_href="contact.html",
        primary_label="Prendre RDV",
        secondary_href="soins.html",
        secondary_label="Voir les soins",
        glass_pills=["Sport", "Post-op", "Douleur"],
    )
    m += block_movento_stat_band(
        [("RDV", "rapide"), ("Ordo", "acceptée"), ("Sport", "suivi"), ("Serpenoise", "cabinet")]
    )
    m += block_movento_steps(
        "Parcours patient",
        [
            ("Appel / formulaire", "Tu décris la douleur ou le besoin."),
            ("Créneau", "On confirme sous 24 h ouvrées."),
            ("Séance", "Protocole expliqué - objectifs clairs."),
        ],
    )
    m += block_movento_contact("Prendre RDV", KI["address"], cta_label="Envoyer", phone=KI["phone"], address=KI["address"])
    m += "</main>"
    return _shell(
        slug="kine",
        brand=KI["brand"],
        phone=KI["phone"],
        address=KI["address"],
        email=KI["email"],
        maps=KI["maps"],
        nav=KI["nav"],
        page="index.html",
        title=f"{KI['brand']} - Kiné Metz",
        desc="Cabinet de kinésithérapie à Metz : RDV, soins, équipe.",
        main=m,
        cta="RDV",
        hours="Metz · Kiné",
        head=HEAD_SERIF,
        body_extra="vt-mv-kine",
        layout="movento-kine",
        nav_kind="pill",
    )


def build_kine_soins():
    m = "<main>" + block_snap_chapter("Soins", "Protocoles clairs - tu sais ce qu'on fait et pourquoi.", "scene-1.png", "Soins", cta_href="contact.html", cta_label="RDV") + "</main>"
    return _shell(slug="kine", brand=KI["brand"], phone=KI["phone"], address=KI["address"], email=KI["email"], maps=KI["maps"], nav=KI["nav"], page="soins.html", title=f"Soins - {KI['brand']}", desc="Soins Kinesia Metz.", main=m, cta="RDV", hours="Metz · Kiné", head=HEAD_SERIF, body_extra="vt-mv-kine", layout="movento-kine", nav_kind="pill")


def build_kine_equipe():
    m = "<main>" + block_snap_chapter("Équipe", "Thérapeutes identifiés - suivi cohérent.", "scene-2.png", "Équipe", reverse=True) + "</main>"
    return _shell(slug="kine", brand=KI["brand"], phone=KI["phone"], address=KI["address"], email=KI["email"], maps=KI["maps"], nav=KI["nav"], page="equipe.html", title=f"Équipe - {KI['brand']}", desc="Équipe Kinesia Metz.", main=m, cta="RDV", hours="Metz · Kiné", head=HEAD_SERIF, body_extra="vt-mv-kine", layout="movento-kine", nav_kind="pill")


def build_kine_contact():
    m = "<main>" + block_movento_contact("RDV", KI["address"], cta_label="Envoyer", phone=KI["phone"], address=KI["address"]) + "</main>"
    return _shell(slug="kine", brand=KI["brand"], phone=KI["phone"], address=KI["address"], email=KI["email"], maps=KI["maps"], nav=KI["nav"], page="contact.html", title=f"Contact - {KI['brand']}", desc="RDV Kinesia Metz.", main=m, cta="RDV", hours="Metz · Kiné", head=HEAD_SERIF, body_extra="vt-mv-kine", layout="movento-kine", nav_kind="pill")


# --- Osteo : Cabinet des Ponts - center + services + quote ---
OS = dict(
    brand="Cabinet des Ponts",
    phone="03 87 36 22 10",
    email="rdv@cabinet-des-ponts.fr",
    address="9 quai Félix Maréchal, 57000 Metz",
    maps="https://maps.google.com/?q=9+quai+Felix+Marechal+57000+Metz",
    nav=[
        {"file": "index.html", "label": "Accueil"},
        {"file": "soins.html", "label": "Soins"},
        {"file": "tarifs.html", "label": "Tarifs"},
        {"file": "contact.html", "label": "RDV"},
    ],
)


def build_osteo_index():
    m = "<main>"
    m += block_hero_movento_center(
        "Ostéopathie douce, RDV simple",
        "Cabinet sur le quai à Metz - consultations sur RDV, soins expliqués, tarifs affichés.",
        eyebrow="Metz · Ostéopathie",
        primary_href="contact.html",
        primary_label="Prendre RDV",
        secondary_href="soins.html",
        secondary_label="Voir les soins",
        img="hero.png",
        alt="Cabinet des Ponts Metz",
    )
    m += block_movento_services(
        "Motifs fréquents",
        [
            {"title": "Dos & cervicales", "text": "Séances cadencées - objectifs clairs.", "img": "card-1.png", "alt": "Ostéopathie dos"},
            {"title": "Sport", "text": "Préparation et récupération.", "img": "card-2.png", "alt": "Ostéo sport"},
            {"title": "Bébé / grossesse", "text": "Accueil adapté - sur RDV.", "img": "card-3.png", "alt": "Ostéo bébé"},
        ],
        lead="Pas la peine de faire le nareux avec les tarifs : prix affichés.",
    )
    m += block_movento_quote(
        "Explications claires, séance douce. RDV sous 48 h comme annoncé.",
        author="Marc",
        role="Metz Quais",
    )
    m += block_movento_contact("Prendre RDV", OS["address"], cta_label="Envoyer", phone=OS["phone"], address=OS["address"])
    m += "</main>"
    return _shell(
        slug="osteo",
        brand=OS["brand"],
        phone=OS["phone"],
        address=OS["address"],
        email=OS["email"],
        maps=OS["maps"],
        nav=OS["nav"],
        page="index.html",
        title=f"{OS['brand']} - Ostéopathe Metz",
        desc="Cabinet d'ostéopathie à Metz : RDV, soins, tarifs.",
        main=m,
        cta="RDV",
        hours="Metz · Ostéopathie",
        head=HEAD_SERIF,
        body_extra="vt-body-osteo vt-mv-osteo",
        layout="movento-osteo",
        nav_kind="underline",
    )


def build_osteo_soins():
    m = "<main>" + block_snap_chapter("Soins", "Approche douce - on explique chaque étape.", "scene-1.png", "Soins", cta_href="contact.html", cta_label="RDV") + "</main>"
    return _shell(slug="osteo", brand=OS["brand"], phone=OS["phone"], address=OS["address"], email=OS["email"], maps=OS["maps"], nav=OS["nav"], page="soins.html", title=f"Soins - {OS['brand']}", desc="Soins Cabinet des Ponts.", main=m, cta="RDV", hours="Metz · Ostéopathie", head=HEAD_SERIF, body_extra="vt-body-osteo vt-mv-osteo", layout="movento-osteo", nav_kind="underline")


def build_osteo_tarifs():
    m = "<main>" + block_snap_chapter("Tarifs", "Prix affichés - pas la peine de faire le nareux.", "scene-2.png", "Tarifs", reverse=True) + "</main>"
    return _shell(slug="osteo", brand=OS["brand"], phone=OS["phone"], address=OS["address"], email=OS["email"], maps=OS["maps"], nav=OS["nav"], page="tarifs.html", title=f"Tarifs - {OS['brand']}", desc="Tarifs ostéopathie Metz.", main=m, cta="RDV", hours="Metz · Ostéopathie", head=HEAD_SERIF, body_extra="vt-body-osteo vt-mv-osteo", layout="movento-osteo", nav_kind="underline")


def build_osteo_contact():
    m = "<main>" + block_movento_contact("RDV", OS["address"], cta_label="Envoyer", phone=OS["phone"], address=OS["address"]) + "</main>"
    return _shell(slug="osteo", brand=OS["brand"], phone=OS["phone"], address=OS["address"], email=OS["email"], maps=OS["maps"], nav=OS["nav"], page="contact.html", title=f"Contact - {OS['brand']}", desc="RDV Cabinet des Ponts Metz.", main=m, cta="RDV", hours="Metz · Ostéopathie", head=HEAD_SERIF, body_extra="vt-body-osteo vt-mv-osteo", layout="movento-osteo", nav_kind="underline")


BUILDERS_MOVENTO_VAGUE_C = {
    "boulangerie": [
        ("index.html", build_boulangerie_index),
        ("pains.html", build_boulangerie_pains),
        ("patisseries.html", build_boulangerie_patisseries),
        ("contact.html", build_boulangerie_contact),
    ],
    "chocolaterie": [
        ("index.html", build_chocolaterie_index),
        ("chocolats.html", build_chocolaterie_chocolats),
        ("atelier.html", build_chocolaterie_atelier),
        ("contact.html", build_chocolaterie_contact),
    ],
    "traiteur": [
        ("index.html", build_traiteur_index),
        ("menus.html", build_traiteur_menus),
        ("evenements.html", build_traiteur_evenements),
        ("contact.html", build_traiteur_contact),
    ],
    "fleuriste": [
        ("index.html", build_fleuriste_index),
        ("collections.html", build_fleuriste_collections),
        ("mariage.html", build_fleuriste_mariage),
        ("contact.html", build_fleuriste_contact),
    ],
    "caviste": [
        ("index.html", build_caviste_index),
        ("vins.html", build_caviste_vins),
        ("cave.html", build_caviste_cave),
        ("contact.html", build_caviste_contact),
    ],
    "coiffure": [
        ("index.html", build_coiffure_index),
        ("soins.html", build_coiffure_soins),
        ("equipe.html", build_coiffure_equipe),
        ("contact.html", build_coiffure_contact),
    ],
    "yoga": [
        ("index.html", build_yoga_index),
        ("cours.html", build_yoga_cours),
        ("planning.html", build_yoga_planning),
        ("contact.html", build_yoga_contact),
    ],
    "kine": [
        ("index.html", build_kine_index),
        ("soins.html", build_kine_soins),
        ("equipe.html", build_kine_equipe),
        ("contact.html", build_kine_contact),
    ],
    "osteo": [
        ("index.html", build_osteo_index),
        ("soins.html", build_osteo_soins),
        ("tarifs.html", build_osteo_tarifs),
        ("contact.html", build_osteo_contact),
    ],
}
