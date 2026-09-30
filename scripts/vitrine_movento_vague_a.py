"""Redesign Movento vague A - 8 flagships existants.

Slugs : artisan, automobile, beaute, commerce, immobilier, juridique,
odontologie, restauration.

Reutilise marques / photos existantes. ADN : docs/MOVENTO-INSPIRATION.md.
Personnalites distinctes par metier (nav + hero + sections).
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

HEAD_CONDENSED = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
{_BOOT}"""

HEAD_GARAMOND = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
{_BOOT}"""

HEAD_BASKERVILLE = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
{_BOOT}"""

HEAD_FRAUNCES = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
{_BOOT}"""

HEAD_SYNE = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Syne:wght@600;700;800&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
{_BOOT}"""

HEAD_BRICOLAGE = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Karla:wght@400;500;600;700&display=swap" rel="stylesheet">
{_BOOT}"""


def _foot_links(nav: list[dict]) -> list[tuple[str, str]]:
    return [(p["label"], p["file"]) for p in nav]


def _shell(
    *,
    slug: str,
    brand: str,
    phone: str,
    address: str,
    email: str,
    maps: str,
    nav: list[dict],
    page: str,
    title: str,
    desc: str,
    main: str,
    cta_label: str,
    hours: str,
    head: str,
    body_extra: str,
    layout: str,
    nav_kind: str = "pill",
) -> str:
    if nav_kind == "pill":
        header = block_movento_pill_nav(
            brand, nav, page, cta_label=cta_label, cta_href="contact.html", phone=phone
        )
    else:
        header = block_movento_bar_nav(
            brand,
            nav,
            page,
            cta_label=cta_label,
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
        nav_links=_foot_links(nav),
        hours_line=hours,
    )
    mobile = block_mobile_cta(cta_label, "contact.html", phone)
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


# --- Artisan : Clanche & Cuivre (bleed Angelo) ---
AR = {
    "brand": "Clanche & Cuivre",
    "phone": "03 87 21 90 40",
    "email": "urgence@clanche-cuivre.fr",
    "address": "Zone artisanale Nord, 57070 Metz",
    "maps": "https://maps.google.com/?q=Metz+57070",
    "nav": [
        {"file": "index.html", "label": "Accueil"},
        {"file": "services.html", "label": "Services"},
        {"file": "zones.html", "label": "Zones"},
        {"file": "contact.html", "label": "Contact"},
    ],
}


def build_artisan_index():
    m = "<main>"
    m += block_hero_movento_bleed(
        "Fuite, bouchon, chauffage - on arrive",
        "Plombier urgence à Metz : devis clair avant travaux, intervention 24h/24.",
        "hero.png",
        "Plombier en intervention à Metz",
        badge="Metz · Montigny · Woippy et alentours",
        primary_href="contact.html",
        primary_label="Devis gratuit",
        phone_href="tel:0387219040",
        phone_label="Appeler maintenant",
        secondary_href="services.html",
        secondary_label="Voir les services",
    )
    m += block_movento_stat_band(
        [("30 min", "arrivée moyenne"), ("24/7", "urgence"), ("0", "surprise devis"), ("15 ans", "terrain")]
    )
    m += block_movento_steps(
        "Comment ça se passe",
        [
            ("Tu appelles", "Urgence ou devis - on te dit si on peut passer aujourd'hui."),
            ("On digne sur place", "Photos, devis oral net, tu valides avant qu'on touche."),
            ("On repart propre", "Chantier rangé, facture claire, numéro direct si ça reclanche."),
        ],
        lead="Pas trois cartes clones - un vrai déroulé d'intervention.",
    )
    m += block_movento_quote(
        "Ils sont venus entre midi, devis avant d'ouvrir la clanche. Nickel.",
        author="Marie",
        role="Metz Nord",
    )
    m += block_movento_contact(
        "Urgence ou devis",
        "Dis voir ce qui bloque - on démêle ça.",
        cta_label="Envoyer",
        phone=AR["phone"],
        address=AR["address"],
    )
    m += "</main>"
    return _shell(
        slug="artisan",
        brand=AR["brand"],
        phone=AR["phone"],
        address=AR["address"],
        email=AR["email"],
        maps=AR["maps"],
        nav=AR["nav"],
        page="index.html",
        title=f"{AR['brand']} - Plombier Metz",
        desc="Plombier urgence à Metz : dépannage 24/7, devis clair, zones d'intervention.",
        main=m,
        cta_label="Devis",
        hours="Metz · Plomberie 24/7",
        head=HEAD_CONDENSED,
        body_extra="vt-body-artisan vt-mv-artisan",
        layout="movento-artisan",
        nav_kind="solid",
    )


def build_artisan_services():
    m = "<main>"
    m += block_snap_chapter("Dépannage express", "Fuite, débouchage, WC - arrivée moyenne 30 min sur Metz.", "scene-1.png", "Dépannage", cta_href="contact.html", cta_label="Appeler")
    m += block_snap_chapter("Rénovation SDB", "Devis détaillé, planning, réception - un seul interlocuteur.", "card-2.png", "Salle de bain", reverse=True)
    m += block_snap_chapter("Chauffage", "Entretien annuel ou panne en hiver - on reste joignable.", "card-3.png", "Chauffage", cta_href="contact.html", cta_label="Devis")
    m += "</main>"
    return _shell(slug="artisan", brand=AR["brand"], phone=AR["phone"], address=AR["address"], email=AR["email"], maps=AR["maps"], nav=AR["nav"], page="services.html", title=f"Services - {AR['brand']}", desc="Services plomberie Clanche & Cuivre Metz.", main=m, cta_label="Devis", hours="Metz · Plomberie", head=HEAD_CONDENSED, body_extra="vt-body-artisan vt-mv-artisan", layout="movento-artisan")


def build_artisan_zones():
    m = f"""<main><section class="vt-mv-services"><div class="vt-mv-wrap">
    <p class="vt-mv-eyebrow">Zones</p>
    <h1 class="vt-mv-section-title">Metz et alentours</h1>
    <p class="vt-mv-lead">Metz, Montigny, Woippy, Longeville, Plappeville - 30 min en moyenne.</p>
    <p class="mt-4"><a class="vt-mv-btn vt-mv-btn-primary" href="tel:0387219040">Appeler</a></p>
    </div></section></main>"""
    return _shell(slug="artisan", brand=AR["brand"], phone=AR["phone"], address=AR["address"], email=AR["email"], maps=AR["maps"], nav=AR["nav"], page="zones.html", title=f"Zones - {AR['brand']}", desc="Zones d'intervention plombier Metz.", main=m, cta_label="Devis", hours="Metz", head=HEAD_CONDENSED, body_extra="vt-body-artisan vt-mv-artisan", layout="movento-artisan")


def build_artisan_contact():
    m = "<main>" + block_movento_contact("Urgence ou devis", f"{AR['address']} · {AR['phone']}", cta_label="Envoyer", phone=AR["phone"], address=AR["address"]) + "</main>"
    return _shell(slug="artisan", brand=AR["brand"], phone=AR["phone"], address=AR["address"], email=AR["email"], maps=AR["maps"], nav=AR["nav"], page="contact.html", title=f"Contact - {AR['brand']}", desc="Contacter Clanche & Cuivre Metz.", main=m, cta_label="Devis", hours="Metz", head=HEAD_CONDENSED, body_extra="vt-body-artisan vt-mv-artisan", layout="movento-artisan")


# --- Automobile : Garage Central (bleed Hunsy) ---
AU = {
    "brand": "Garage Central Plappeville",
    "phone": "03 87 65 43 21",
    "email": "rdv@garage-central-plappeville.fr",
    "address": "Zone artisanale des Gravieres, 57050 Plappeville",
    "maps": "https://maps.google.com/?q=Plappeville+57050",
    "nav": [
        {"file": "index.html", "label": "Accueil"},
        {"file": "services.html", "label": "Services"},
        {"file": "atelier.html", "label": "Atelier"},
        {"file": "contact.html", "label": "RDV"},
    ],
}


def build_automobile_index():
    m = "<main>"
    m += block_hero_movento_magazine(
        "L'atelier qui parle clair",
        "Entretien, pneus, carrosserie à Plappeville - devis avant de toucher à ta caisse.",
        "hero.png",
        "Atelier garage Plappeville",
        eyebrow="Plappeville · Metz Ouest",
        primary_href="contact.html",
        primary_label="Prendre RDV",
        kicker="Garage indépendant",
    )
    m += block_movento_feature_rows(
        "Sous le capot",
        [
            ("Entretien", "Vidange, freins, distribution - planning sans jargon.", "card-1.png", "Entretien auto"),
            ("Pneus", "Monte, équilibre, stockage saisonnier.", "card-2.png", "Pneus"),
            ("Carrosserie", "Chocs, peinture, devis photo sous 24 h.", "card-3.png", "Carrosserie"),
        ],
        lead="Des bandes photo + texte, pas trois cartes identiques.",
    )
    m += block_movento_proof([("1 h", "diagnostic type"), ("Toutes", "marques"), ("Photos", "avant/après"), ("Garantie", "pièces + main")])
    m += block_movento_contact(
        "Prendre RDV",
        f"{AU['address']} · {AU['phone']}",
        cta_label="Envoyer",
        phone=AU["phone"],
        address=AU["address"],
    )
    m += "</main>"
    return _shell(
        slug="automobile",
        brand=AU["brand"],
        phone=AU["phone"],
        address=AU["address"],
        email=AU["email"],
        maps=AU["maps"],
        nav=AU["nav"],
        page="index.html",
        title=f"{AU['brand']} - Garage Plappeville",
        desc="Garage Plappeville : entretien, pneus, carrosserie, devis clair.",
        main=m,
        cta_label="RDV",
        hours="Plappeville · Garage",
        head=HEAD_CONDENSED,
        body_extra="vt-body-auto vt-mv-auto",
        layout="movento-auto",
        nav_kind="solid",
    )


def build_automobile_services():
    m = "<main>"
    m += block_snap_chapter("Entretien & controle", "Revision, freins, climatisation - devis avant travaux.", "scene-1.png", "Entretien", cta_href="contact.html", cta_label="RDV")
    m += block_snap_chapter("Pneus & geometrie", "Toutes dimensions, stockage ete/hiver.", "card-2.png", "Pneus", reverse=True)
    m += block_snap_chapter("Carrosserie", "Devis photo sous 24 h.", "card-3.png", "Carrosserie")
    m += "</main>"
    return _shell(slug="automobile", brand=AU["brand"], phone=AU["phone"], address=AU["address"], email=AU["email"], maps=AU["maps"], nav=AU["nav"], page="services.html", title=f"Services - {AU['brand']}", desc="Services garage Plappeville.", main=m, cta_label="RDV", hours="Garage", head=HEAD_CONDENSED, body_extra="vt-body-garage vt-mv-auto", layout="movento-auto")


def build_automobile_atelier():
    m = "<main>" + block_snap_chapter("L'équipe sur le terrain", "Mécaniciens formés, outillage a jour, photos de suivi.", "scene-2.png", "Atelier", cta_href="contact.html", cta_label="Prendre RDV") + "</main>"
    return _shell(slug="automobile", brand=AU["brand"], phone=AU["phone"], address=AU["address"], email=AU["email"], maps=AU["maps"], nav=AU["nav"], page="atelier.html", title=f"Atelier - {AU['brand']}", desc="Atelier Garage Central Plappeville.", main=m, cta_label="RDV", hours="Garage", head=HEAD_CONDENSED, body_extra="vt-body-garage vt-mv-auto", layout="movento-auto")


def build_automobile_contact():
    m = "<main>" + block_movento_contact("RDV atelier", f"{AU['address']}", cta_label="Envoyer", phone=AU["phone"], address=AU["address"]) + "</main>"
    return _shell(slug="automobile", brand=AU["brand"], phone=AU["phone"], address=AU["address"], email=AU["email"], maps=AU["maps"], nav=AU["nav"], page="contact.html", title=f"Contact - {AU['brand']}", desc="RDV garage Plappeville.", main=m, cta_label="RDV", hours="Garage", head=HEAD_CONDENSED, body_extra="vt-body-garage vt-mv-auto", layout="movento-auto")


# --- Beaute : Spa Thalie (soft / Serene) ---
BE = {
    "brand": "Spa Thalie",
    "phone": "03 87 17 42 80",
    "email": "bonjour@spa-thalie.fr",
    "address": "8 rue des Clercs, 57000 Metz",
    "maps": "https://maps.google.com/?q=8+rue+des+Clercs+57000+Metz",
    "nav": [
        {"file": "index.html", "label": "Accueil"},
        {"file": "soins.html", "label": "Soins"},
        {"file": "ambiance.html", "label": "Ambiance"},
        {"file": "contact.html", "label": "RDV"},
    ],
}


def build_beaute_index():
    m = "<main>"
    m += block_hero_movento_center(
        "Du calme, rue des Clercs",
        "Institut et spa : fiches soins claires, RDV simple, sans jargon.",
        eyebrow="Metz centre · Institut & spa",
        primary_href="contact.html",
        primary_label="Prendre RDV",
        secondary_href="soins.html",
        secondary_label="Voir les soins",
        img="hero.png",
        alt="Espace spa Thalie Metz",
    )
    m += block_movento_quote(
        "On entre, on souffle. Les soins sont expliqués sans roman.",
        author="Camille",
        role="cliente Clercs",
    )
    m += block_movento_menu_list(
        "Carte des soins (aperçu)",
        [
            ("Éclat visage", "60 min · nettoyage + masque", "65 €"),
            ("Massage dos", "45 min · huiles bio", "55 €"),
            ("Rituel duo", "90 min · deux cabines", "140 €"),
        ],
        lead="Prix affichés - tu réserves, on confirme.",
        cta_href="contact.html",
        cta_label="Réserver un créneau",
    )
    m += "</main>"
    return _shell(
        slug="beaute",
        brand=BE["brand"],
        phone=BE["phone"],
        address=BE["address"],
        email=BE["email"],
        maps=BE["maps"],
        nav=BE["nav"],
        page="index.html",
        title=f"{BE['brand']} - Spa Metz",
        desc="Institut et spa à Metz : soins, RDV, engagements.",
        main=m,
        cta_label="RDV",
        hours="Metz · Spa",
        head=HEAD_GARAMOND,
        body_extra="vt-body-spa vt-mv-beaute",
        layout="movento-beaute",
        nav_kind="minimal",
    )


def build_beaute_soins():
    m = "<main>" + block_snap_chapter("Carte des soins", "Formules visage et corps - durees et prix sur la fiche.", "scene-1.png", "Soins", cta_href="contact.html", cta_label="Réserver") + "</main>"
    return _shell(slug="beaute", brand=BE["brand"], phone=BE["phone"], address=BE["address"], email=BE["email"], maps=BE["maps"], nav=BE["nav"], page="soins.html", title=f"Soins - {BE['brand']}", desc="Soins Spa Thalie Metz.", main=m, cta_label="RDV", hours="Spa", head=HEAD_SERIF, body_extra="vt-body-spa vt-mv-beaute", layout="movento-beaute")


def build_beaute_ambiance():
    m = "<main>" + block_snap_chapter("L'espace", "Cabines calmes, lumiere douce, rue des Clercs.", "scene-2.png", "Ambiance spa", reverse=True) + "</main>"
    return _shell(slug="beaute", brand=BE["brand"], phone=BE["phone"], address=BE["address"], email=BE["email"], maps=BE["maps"], nav=BE["nav"], page="ambiance.html", title=f"Ambiance - {BE['brand']}", desc="Ambiance Spa Thalie.", main=m, cta_label="RDV", hours="Spa", head=HEAD_SERIF, body_extra="vt-body-spa vt-mv-beaute", layout="movento-beaute")


def build_beaute_contact():
    m = "<main>" + block_movento_contact("Prendre RDV", BE["address"], cta_label="Envoyer", phone=BE["phone"], address=BE["address"]) + "</main>"
    return _shell(slug="beaute", brand=BE["brand"], phone=BE["phone"], address=BE["address"], email=BE["email"], maps=BE["maps"], nav=BE["nav"], page="contact.html", title=f"Contact - {BE['brand']}", desc="RDV Spa Thalie Metz.", main=m, cta_label="RDV", hours="Spa", head=HEAD_SERIF, body_extra="vt-body-spa vt-mv-beaute", layout="movento-beaute")


# --- Commerce : Halles Thionville (warm Beanro) ---
CO = {
    "brand": "Halles Thionville",
    "phone": "03 82 53 40 00",
    "email": "bonjour@halles-thionville.fr",
    "address": "Rue du Mail, 57100 Thionville",
    "maps": "https://maps.google.com/?q=Halles+Thionville",
    "nav": [
        {"file": "index.html", "label": "Accueil"},
        {"file": "rayons.html", "label": "Rayons"},
        {"file": "drive.html", "label": "Drive"},
        {"file": "contact.html", "label": "Contact"},
    ],
}


def build_commerce_index():
    m = "<main>"
    m += block_hero_movento_split(
        "Le marché, version web",
        "Rayons, click & collect et fidélité - commerce de proximité à Thionville.",
        "hero.png",
        "Halles Thionville",
        eyebrow="Thionville · Drive & magasin",
        primary_href="drive.html",
        primary_label="Commander en drive",
        secondary_href="rayons.html",
        secondary_label="Voir les rayons",
        glass_pills=["Frais", "Local", "Drive"],
    )
    m += block_movento_stat_band(
        [("7j/7", "ouvert"), ("2 h", "retrait drive"), ("Fid", "carte"), ("Local", "producteurs")]
    )
    m += block_movento_feature_rows(
        "Comme au magasin",
        [
            ("Frais du jour", "Fruits, fromages, boucherie - photos du matin.", "card-1.png", "Rayon frais"),
            ("Drive", "Tu commandes, tu passes entre midi.", "card-2.png", "Drive"),
            ("Fidélité", "Avantages simples, sans usine à points.", "card-3.png", "Fidélité"),
        ],
    )
    m += block_movento_contact("Une question ?", CO["address"], cta_label="Envoyer", phone=CO["phone"], address=CO["address"])
    m += "</main>"
    return _shell(
        slug="commerce",
        brand=CO["brand"],
        phone=CO["phone"],
        address=CO["address"],
        email=CO["email"],
        maps=CO["maps"],
        nav=CO["nav"],
        page="index.html",
        title=f"{CO['brand']} - Commerce Thionville",
        desc="Commerce et drive Halles Thionville.",
        main=m,
        cta_label="Drive",
        hours="Thionville · Halles",
        head=HEAD_BRICOLAGE,
        body_extra="vt-body-retail vt-mv-commerce",
        layout="movento-commerce",
        nav_kind="underline",
    )


def build_commerce_rayons():
    m = "<main>" + block_snap_chapter("Rayons", "Frais, épicerie, cave - navigue comme en boutique.", "scene-1.png", "Rayons", cta_href="drive.html", cta_label="Passer en drive") + "</main>"
    return _shell(slug="commerce", brand=CO["brand"], phone=CO["phone"], address=CO["address"], email=CO["email"], maps=CO["maps"], nav=CO["nav"], page="rayons.html", title=f"Rayons - {CO['brand']}", desc="Rayons Halles Thionville.", main=m, cta_label="Drive", hours="Halles", head=HEAD_SERIF, body_extra="vt-body-retail vt-mv-commerce", layout="movento-commerce")


def build_commerce_drive():
    m = "<main>" + block_snap_chapter("Click & collect", "Commande en ligne, retrait au Mail.", "scene-2.png", "Drive", reverse=True, cta_href="contact.html", cta_label="Aide commande") + "</main>"
    return _shell(slug="commerce", brand=CO["brand"], phone=CO["phone"], address=CO["address"], email=CO["email"], maps=CO["maps"], nav=CO["nav"], page="drive.html", title=f"Drive - {CO['brand']}", desc="Drive Halles Thionville.", main=m, cta_label="Drive", hours="Halles", head=HEAD_SERIF, body_extra="vt-body-retail vt-mv-commerce", layout="movento-commerce")


def build_commerce_contact():
    m = "<main>" + block_movento_contact("Contact magasin", CO["address"], cta_label="Envoyer", phone=CO["phone"], address=CO["address"]) + "</main>"
    return _shell(slug="commerce", brand=CO["brand"], phone=CO["phone"], address=CO["address"], email=CO["email"], maps=CO["maps"], nav=CO["nav"], page="contact.html", title=f"Contact - {CO['brand']}", desc="Contact Halles Thionville.", main=m, cta_label="Contact", hours="Halles", head=HEAD_SERIF, body_extra="vt-body-retail vt-mv-commerce", layout="movento-commerce")


# --- Immobilier : Patrimoine Lorraine (split editorial) ---
IM = {
    "brand": "Patrimoine Lorraine",
    "phone": "03 87 36 12 14",
    "email": "accueil@patrimoine-lorraine.fr",
    "address": "14 rue des Clercs, 57000 Metz",
    "maps": "https://maps.google.com/?q=14+rue+des+Clercs+57000+Metz",
    "nav": [
        {"file": "index.html", "label": "Accueil"},
        {"file": "biens.html", "label": "Biens"},
        {"file": "estimation.html", "label": "Estimation"},
        {"file": "contact.html", "label": "Contact"},
    ],
}


def build_immobilier_index():
    m = "<main>"
    m += block_hero_movento_magazine(
        "Vendre ou louer, sans brouillon",
        "Agence à Metz : sélection de biens, estimation gratuite, gestion locative.",
        "hero.png",
        "Agence immobilière Metz",
        eyebrow="Metz · Transaction & gestion",
        primary_href="estimation.html",
        primary_label="Estimation gratuite",
        kicker="Patrimoine local",
    )
    m += block_movento_steps(
        "Ton parcours",
        [
            ("Brief", "Budget, quartier, délai - on note net."),
            ("Visites", "Créneaux groupés, comptes-rendus photo."),
            ("Offre", "Négociation + dossier - un seul interlocuteur."),
        ],
    )
    m += block_movento_services(
        "Pour vendeurs et acquéreurs",
        [
            {"title": "Biens en carte", "text": "Photos nettes, prix affiché, quartier explicite.", "img": "card-1.png", "alt": "Bien immobilier"},
            {"title": "Estimation", "text": "Visite + fourchette - sans engagement.", "img": "card-2.png", "alt": "Estimation"},
            {"title": "Gestion", "text": "Loyers, état des lieux, suivi locataire.", "img": "card-3.png", "alt": "Gestion locative"},
        ],
    )
    m += block_movento_contact("Parler à un conseiller", IM["address"], cta_label="Envoyer", phone=IM["phone"], address=IM["address"])
    m += "</main>"
    return _shell(
        slug="immobilier",
        brand=IM["brand"],
        phone=IM["phone"],
        address=IM["address"],
        email=IM["email"],
        maps=IM["maps"],
        nav=IM["nav"],
        page="index.html",
        title=f"{IM['brand']} - Agence Metz",
        desc="Agence immobilière Metz : biens, estimation, gestion.",
        main=m,
        cta_label="Estimation",
        hours="Metz · Immobilier",
        head=HEAD_FRAUNCES,
        body_extra="vt-body-property vt-mv-immo",
        layout="movento-immo",
        nav_kind="underline",
    )


def build_immobilier_biens():
    m = "<main>" + block_snap_chapter("Selection", "Appartements et maisons - filtre ville et budget.", "scene-1.png", "Biens", cta_href="contact.html", cta_label="Être rappele") + "</main>"
    return _shell(slug="immobilier", brand=IM["brand"], phone=IM["phone"], address=IM["address"], email=IM["email"], maps=IM["maps"], nav=IM["nav"], page="biens.html", title=f"Biens - {IM['brand']}", desc="Biens Patrimoine Lorraine.", main=m, cta_label="Contact", hours="Immo", head=HEAD_SERIF, body_extra="vt-body-property vt-mv-immo", layout="movento-immo")


def build_immobilier_estimation():
    m = "<main>" + block_movento_contact("Estimation gratuite", "Adresse + type de bien - on te rappelle.", cta_label="Demander", phone=IM["phone"], address=IM["address"]) + "</main>"
    return _shell(slug="immobilier", brand=IM["brand"], phone=IM["phone"], address=IM["address"], email=IM["email"], maps=IM["maps"], nav=IM["nav"], page="estimation.html", title=f"Estimation - {IM['brand']}", desc="Estimation immobiliere Metz.", main=m, cta_label="Estimation", hours="Immo", head=HEAD_SERIF, body_extra="vt-body-property vt-mv-immo", layout="movento-immo")


def build_immobilier_contact():
    m = "<main>" + block_movento_contact("Contact agence", IM["address"], cta_label="Envoyer", phone=IM["phone"], address=IM["address"]) + "</main>"
    return _shell(slug="immobilier", brand=IM["brand"], phone=IM["phone"], address=IM["address"], email=IM["email"], maps=IM["maps"], nav=IM["nav"], page="contact.html", title=f"Contact - {IM['brand']}", desc="Contact Patrimoine Lorraine.", main=m, cta_label="Contact", hours="Immo", head=HEAD_SERIF, body_extra="vt-body-property vt-mv-immo", layout="movento-immo")


# --- Juridique : Rivière & Partenaires (split sobre) ---
JU = {
    "brand": "Rivière & Partenaires",
    "phone": "03 87 75 90 12",
    "email": "cabinet@riviere-avocats.fr",
    "address": "12 avenue Foch, 57000 Metz",
    "maps": "https://maps.google.com/?q=12+avenue+Foch+57000+Metz",
    "nav": [
        {"file": "index.html", "label": "Accueil"},
        {"file": "expertises.html", "label": "Expertises"},
        {"file": "accompagnement.html", "label": "Methode"},
        {"file": "contact.html", "label": "Contact"},
    ],
}


def build_juridique_index():
    m = "<main>"
    m += block_hero_movento_center(
        "Le droit, expliqué net",
        "Cabinet d'avocats à Metz : affaires, social, contentieux - premier échange clair.",
        eyebrow="Metz · Droit des affaires & social",
        primary_href="contact.html",
        primary_label="Prendre RDV",
        secondary_href="expertises.html",
        secondary_label="Expertises",
    )
    m += block_movento_steps(
        "Méthode",
        [
            ("Écoute", "Tu expliques le dossier - on cadré le périmètre."),
            ("Devis", "Honoraires avant acte - pas de roman inutile."),
            ("Calendrier", "Échéances claires, un associé référent."),
        ],
        lead="Pas de grille de cartes photo : un cabinet sobre.",
    )
    m += block_movento_quote(
        "Ils ont tenu le devis annoncé. Ça change tout quand tu es PME.",
        author="Olivier",
        role="dirigeant, Nancy",
    )
    m += block_movento_contact("Consultation", "Décris le sujet - on te rappelle.", cta_label="Envoyer", phone=JU["phone"], address=JU["address"])
    m += "</main>"
    return _shell(
        slug="juridique",
        brand=JU["brand"],
        phone=JU["phone"],
        address=JU["address"],
        email=JU["email"],
        maps=JU["maps"],
        nav=JU["nav"],
        page="index.html",
        title=f"{JU['brand']} - Avocats Metz",
        desc="Cabinet d'avocats Metz : affaires, social, contentieux.",
        main=m,
        cta_label="RDV",
        hours="Metz · Avocats",
        head=HEAD_BASKERVILLE,
        body_extra="vt-body-legal vt-mv-legal",
        layout="movento-legal",
        nav_kind="underline",
    )


def build_juridique_expertises():
    m = "<main>" + block_snap_chapter("Domaines", "Affaires, social, contentieux - périmètre clair des le premier appel.", "scene-1.png", "Expertises") + "</main>"
    return _shell(slug="juridique", brand=JU["brand"], phone=JU["phone"], address=JU["address"], email=JU["email"], maps=JU["maps"], nav=JU["nav"], page="expertises.html", title=f"Expertises - {JU['brand']}", desc="Expertises cabinet Rivière Metz.", main=m, cta_label="RDV", hours="Avocats", head=HEAD_SERIF, body_extra="vt-body-legal vt-mv-legal", layout="movento-legal")


def build_juridique_accompagnement():
    m = "<main>" + block_snap_chapter("Methode", "Écoute, devis, calendrier - pas de roman inutile.", "scene-2.png", "Methode", reverse=True, cta_href="contact.html", cta_label="Prendre RDV") + "</main>"
    return _shell(slug="juridique", brand=JU["brand"], phone=JU["phone"], address=JU["address"], email=JU["email"], maps=JU["maps"], nav=JU["nav"], page="accompagnement.html", title=f"Methode - {JU['brand']}", desc="Methode cabinet avocats Metz.", main=m, cta_label="RDV", hours="Avocats", head=HEAD_SERIF, body_extra="vt-body-legal vt-mv-legal", layout="movento-legal")


def build_juridique_contact():
    m = "<main>" + block_movento_contact("Prendre RDV", JU["address"], cta_label="Envoyer", phone=JU["phone"], address=JU["address"]) + "</main>"
    return _shell(slug="juridique", brand=JU["brand"], phone=JU["phone"], address=JU["address"], email=JU["email"], maps=JU["maps"], nav=JU["nav"], page="contact.html", title=f"Contact - {JU['brand']}", desc="Contact avocats Metz.", main=m, cta_label="RDV", hours="Avocats", head=HEAD_SERIF, body_extra="vt-body-legal vt-mv-legal", layout="movento-legal")


# --- Odontologie : Centre Mosaïque (split Dental) ---
OD = {
    "brand": "Centre dentaire Mosaïque",
    "phone": "03 82 88 45 00",
    "email": "accueil@dentaire-mosaique.fr",
    "address": "42 avenue de la République, 57100 Thionville",
    "maps": "https://maps.google.com/?q=Thionville+57100",
    "nav": [
        {"file": "index.html", "label": "Accueil"},
        {"file": "soins.html", "label": "Soins"},
        {"file": "equipe.html", "label": "Équipe"},
        {"file": "contact.html", "label": "RDV"},
    ],
}


def build_odontologie_index():
    m = "<main>"
    m += block_hero_movento_split(
        "Soins dentaires, sans flou",
        "Cabinet à Thionville : tarifs lisibles, prévention, rappel telephonique.",
        "hero.png",
        "Cabinet dentaire Thionville",
        eyebrow="Thionville · Centre dentaire",
        primary_href="contact.html",
        primary_label="Demander un RDV",
        secondary_href="soins.html",
        secondary_label="Voir les soins",
        glass_pills=["Prévention", "Esthétique", "Urgence"],
    )
    m += block_movento_stat_band(
        [("Devis", "avant acte"), ("Mutuelle", "aide"), ("Rappel", "sous 24 h"), ("Enfants", "OK")]
    )
    m += block_movento_steps(
        "Parcours patient",
        [
            ("Appel / formulaire", "Tu décris la douleur ou le besoin."),
            ("Créneau", "On confirme sous 24 h ouvrées."),
            ("Soin + devis", "Explication avant, facture nette après."),
        ],
    )
    m += block_movento_contact("Demande de RDV", OD["address"], cta_label="Envoyer", phone=OD["phone"], address=OD["address"])
    m += "</main>"
    return _shell(
        slug="odontologie",
        brand=OD["brand"],
        phone=OD["phone"],
        address=OD["address"],
        email=OD["email"],
        maps=OD["maps"],
        nav=OD["nav"],
        page="index.html",
        title=f"{OD['brand']} - Dentiste Thionville",
        desc="Cabinet dentaire Thionville : soins, tarifs, RDV.",
        main=m,
        cta_label="RDV",
        hours="Thionville · Dentaire",
        head=HEAD_SYNE,
        body_extra="vt-body-medical vt-mv-dental",
        layout="movento-dental",
        nav_kind="pill",
    )


def build_odontologie_soins():
    m = "<main>" + block_snap_chapter("Soins proposes", "Prévention, restauration, esthétique - grille tarifaire sur place.", "scene-1.png", "Soins", cta_href="contact.html", cta_label="RDV") + "</main>"
    return _shell(slug="odontologie", brand=OD["brand"], phone=OD["phone"], address=OD["address"], email=OD["email"], maps=OD["maps"], nav=OD["nav"], page="soins.html", title=f"Soins - {OD['brand']}", desc="Soins dentaires Thionville.", main=m, cta_label="RDV", hours="Dentaire", head=HEAD_SERIF, body_extra="vt-body-medical vt-mv-dental", layout="movento-dental")


def build_odontologie_equipe():
    m = "<main>" + block_snap_chapter("L'équipe", "Praticiens et assistantes - un seul numéro pour le secrétariat.", "scene-2.png", "Équipe", reverse=True) + "</main>"
    return _shell(slug="odontologie", brand=OD["brand"], phone=OD["phone"], address=OD["address"], email=OD["email"], maps=OD["maps"], nav=OD["nav"], page="equipe.html", title=f"Équipe - {OD['brand']}", desc="Équipe centre dentaire Thionville.", main=m, cta_label="RDV", hours="Dentaire", head=HEAD_SERIF, body_extra="vt-body-medical vt-mv-dental", layout="movento-dental")


def build_odontologie_contact():
    m = "<main>" + block_movento_contact("Demander un RDV", OD["address"], cta_label="Envoyer", phone=OD["phone"], address=OD["address"]) + "</main>"
    return _shell(slug="odontologie", brand=OD["brand"], phone=OD["phone"], address=OD["address"], email=OD["email"], maps=OD["maps"], nav=OD["nav"], page="contact.html", title=f"Contact - {OD['brand']}", desc="RDV dentaire Thionville.", main=m, cta_label="RDV", hours="Dentaire", head=HEAD_SERIF, body_extra="vt-body-medical vt-mv-dental", layout="movento-dental")


# --- Restauration : Brasserie Saint-Jacques (split Fiamma) ---
RE = {
    "brand": "Brasserie Saint-Jacques",
    "phone": "03 87 75 12 34",
    "email": "reservation@brasserie-saint-jacques.fr",
    "address": "12 place Saint-Jacques, 57000 Metz",
    "maps": "https://maps.google.com/?q=12+place+Saint-Jacques+57000+Metz",
    "nav": [
        {"file": "index.html", "label": "Accueil"},
        {"file": "carte.html", "label": "Carte"},
        {"file": "histoire.html", "label": "Histoire"},
        {"file": "contact.html", "label": "Réserver"},
    ],
}


def build_restauration_index():
    m = "<main>"
    m += block_hero_movento_magazine(
        "La table qui réchauffe Metz",
        "Brasserie place Saint-Jacques : carte saisonnière, terrasse, réservation simple.",
        "hero.png",
        "Salle brasserie Metz",
        eyebrow="Metz · Brasserie depuis 1924",
        primary_href="contact.html",
        primary_label="Réserver une table",
        kicker="Depuis 1924",
    )
    m += block_movento_menu_list(
        "Aperçu carte",
        [
            ("Quiche Lorraine", "Salade verte, vinaigrette maison", "16 €"),
            ("Baeckeoffe", "Jarret, pommes de terre, vin blanc", "24 €"),
            ("Tarte mirabelle", "Glace vanille", "9 €"),
        ],
        lead="Carte HTML, pas un PDF flou - tu réserves en deux clics.",
        cta_href="contact.html",
        cta_label="Réserver",
    )
    m += block_movento_quote(
        "La terrasse face a la cathédrale, et le jazz le vendredi. On y revient.",
        author="Léa",
        role="Metz centre",
    )
    m += block_movento_contact("Réserver", RE["address"], cta_label="Envoyer", phone=RE["phone"], address=RE["address"])
    m += "</main>"
    return _shell(
        slug="restauration",
        brand=RE["brand"],
        phone=RE["phone"],
        address=RE["address"],
        email=RE["email"],
        maps=RE["maps"],
        nav=RE["nav"],
        page="index.html",
        title=f"{RE['brand']} - Restaurant Metz",
        desc="Brasserie Metz : carte, terrasse, réservation.",
        main=m,
        cta_label="Réserver",
        hours="Metz · Brasserie",
        head=HEAD_FRAUNCES,
        body_extra="vt-body-restau vt-mv-restau",
        layout="movento-restau",
        nav_kind="minimal",
    )


def build_restauration_carte():
    m = "<main>" + block_snap_chapter("La carte", "Entrées, plats, desserts - mise à jour saisonnière.", "scene-1.png", "Carte", cta_href="contact.html", cta_label="Réserver") + "</main>"
    return _shell(slug="restauration", brand=RE["brand"], phone=RE["phone"], address=RE["address"], email=RE["email"], maps=RE["maps"], nav=RE["nav"], page="carte.html", title=f"Carte - {RE['brand']}", desc="Carte Brasserie Saint-Jacques Metz.", main=m, cta_label="Réserver", hours="Brasserie", head=HEAD_SERIF, body_extra="vt-body-restau vt-mv-restau", layout="movento-restau")


def build_restauration_histoire():
    m = "<main>" + block_snap_chapter("Depuis 1924", "Verrière Art déco, zinc d'origine, cuisine ouverte.", "scene-2.png", "Histoire", reverse=True) + "</main>"
    return _shell(slug="restauration", brand=RE["brand"], phone=RE["phone"], address=RE["address"], email=RE["email"], maps=RE["maps"], nav=RE["nav"], page="histoire.html", title=f"Histoire - {RE['brand']}", desc="Histoire Brasserie Saint-Jacques.", main=m, cta_label="Réserver", hours="Brasserie", head=HEAD_SERIF, body_extra="vt-body-restau vt-mv-restau", layout="movento-restau")


def build_restauration_contact():
    m = "<main>" + block_movento_contact("Réserver une table", RE["address"], cta_label="Envoyer", phone=RE["phone"], address=RE["address"]) + "</main>"
    return _shell(slug="restauration", brand=RE["brand"], phone=RE["phone"], address=RE["address"], email=RE["email"], maps=RE["maps"], nav=RE["nav"], page="contact.html", title=f"Réservation - {RE['brand']}", desc="Réserver Brasserie Saint-Jacques Metz.", main=m, cta_label="Réserver", hours="Brasserie", head=HEAD_SERIF, body_extra="vt-body-restau vt-mv-restau", layout="movento-restau")


BUILDERS_MOVENTO_VAGUE_A = {
    "artisan": [
        ("index.html", build_artisan_index),
        ("services.html", build_artisan_services),
        ("zones.html", build_artisan_zones),
        ("contact.html", build_artisan_contact),
    ],
    "automobile": [
        ("index.html", build_automobile_index),
        ("services.html", build_automobile_services),
        ("atelier.html", build_automobile_atelier),
        ("contact.html", build_automobile_contact),
    ],
    "beaute": [
        ("index.html", build_beaute_index),
        ("soins.html", build_beaute_soins),
        ("ambiance.html", build_beaute_ambiance),
        ("contact.html", build_beaute_contact),
    ],
    "commerce": [
        ("index.html", build_commerce_index),
        ("rayons.html", build_commerce_rayons),
        ("drive.html", build_commerce_drive),
        ("contact.html", build_commerce_contact),
    ],
    "immobilier": [
        ("index.html", build_immobilier_index),
        ("biens.html", build_immobilier_biens),
        ("estimation.html", build_immobilier_estimation),
        ("contact.html", build_immobilier_contact),
    ],
    "juridique": [
        ("index.html", build_juridique_index),
        ("expertises.html", build_juridique_expertises),
        ("accompagnement.html", build_juridique_accompagnement),
        ("contact.html", build_juridique_contact),
    ],
    "odontologie": [
        ("index.html", build_odontologie_index),
        ("soins.html", build_odontologie_soins),
        ("equipe.html", build_odontologie_equipe),
        ("contact.html", build_odontologie_contact),
    ],
    "restauration": [
        ("index.html", build_restauration_index),
        ("carte.html", build_restauration_carte),
        ("histoire.html", build_restauration_histoire),
        ("contact.html", build_restauration_contact),
    ],
}
