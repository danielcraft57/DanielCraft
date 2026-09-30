"""Builders Movento pour 3 secteurs manquants : btp, communication, transport.

ADN design : docs/MOVENTO-INSPIRATION.md (bleed Angelo, split Dental / agency).
Fiction Grand Est - pas de copie d'assets Movento.
"""
from __future__ import annotations

from vitrine_layouts import (
    block_before_after,
    block_hero_movento_bleed,
    block_hero_movento_center,
    block_hero_movento_magazine,
    block_movento_bar_nav,
    block_movento_contact,
    block_movento_feature_rows,
    block_movento_footer,
    block_movento_pill_nav,
    block_movento_quote,
    block_movento_stat_band,
    block_movento_steps,
    block_snap_chapter,
)
from vitrine_seo import get_entity
from vitrine_site_blocks import (
    block_mobile_cta,
    block_site_footer,
    wrap_page,
)

_BOOT = """
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <link rel="stylesheet" href="../shared/vitrine-prose.css">
  <link rel="stylesheet" href="../shared/vitrine-images.css">
  <link rel="stylesheet" href="../shared/vitrine-motion.css">
  <link rel="stylesheet" href="../shared/vitrine-movento.css">
  <link rel="icon" href="images/icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="stylesheet" href="styles.css">"""

HEAD_BTP = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Instrument+Serif&display=swap" rel="stylesheet">
{_BOOT}"""

HEAD_COM = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
{_BOOT}"""

HEAD_TRANSPORT = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Instrument+Serif&display=swap" rel="stylesheet">
{_BOOT}"""


def _foot_links(nav: list[dict]) -> list[tuple[str, str]]:
    return [(p["label"], p["file"]) for p in nav]


# --- BTP : Chantiers Est Construction (Nancy) - bleed Angelo ---
BTP_BRAND = "Chantiers Est Construction"
BTP_PHONE = "03 83 40 18 22"
BTP_EMAIL = "devis@chantiers-est.fr"
BTP_ADDRESS = "12 rue de la Digue, 54000 Nancy"
BTP_MAPS = "https://maps.google.com/?q=12+rue+de+la+Digue+54000+Nancy"
BTP_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "realisations.html", "label": "Réalisations"},
    {"file": "savoir-faire.html", "label": "Savoir-faire"},
    {"file": "contact.html", "label": "Contact"},
]


def _shell_btp(page: str, title: str, desc: str, main: str, *, nav_kind: str = "solid") -> str:
    if nav_kind == "pill":
        nav = block_movento_pill_nav(
            BTP_BRAND,
            BTP_NAV,
            page,
            cta_label="Devis gratuit",
            cta_href="contact.html",
            phone=BTP_PHONE,
        )
    else:
        nav = block_movento_bar_nav(
            BTP_BRAND,
            BTP_NAV,
            page,
            cta_label="Devis gratuit",
            cta_href="contact.html",
            phone=BTP_PHONE,
            variant=nav_kind,
        )
    foot = block_site_footer(
        BTP_BRAND,
        entity=get_entity("btp"),
        slug="btp",
        phone=BTP_PHONE,
        address=BTP_ADDRESS,
        email=BTP_EMAIL,
        maps_href=BTP_MAPS,
        nav_links=_foot_links(BTP_NAV),
        hours_line="Nancy · Chantier Grand Est",
    )
    mobile = block_mobile_cta("Devis", "contact.html", BTP_PHONE)
    body = nav + main + foot + mobile
    return wrap_page(
        title,
        desc,
        body,
        layout="movento-btp",
        slug="btp",
        page=page,
        site_name=BTP_BRAND,
        nav=BTP_NAV,
        head_assets=HEAD_BTP,
        body_class="vt-body vt-body-movento vt-body-btp",
    )


def build_btp_index() -> str:
    main = "<main>"
    main += block_hero_movento_bleed(
        "Du gros oeuvre au dernier coup de pinceau",
        "Entreprise générale à Nancy : maçonnerie, rénovation et suivi de chantier - un seul interlocuteur.",
        "hero.png",
        "Chantier rénovation façade à Nancy",
        badge="Nancy · Laxou · Vandoeuvre et alentours",
        primary_href="contact.html",
        primary_label="Demander un devis",
        phone_href="tel:0383401822",
        phone_label="Appeler maintenant",
        secondary_href="realisations.html",
        secondary_label="Voir les réalisations",
    )
    main += block_movento_steps(
        "Comment ça se passe",
        [
            ("Brief chantier", "Adresse, besoin, délai - on note net."),
            ("Devis clair", "Rappel sous 48 h - tu valides avant démarrage."),
            ("Suivi photo", "Un chef de chantier, photos chaque semaine."),
        ],
        lead="Comme au magasin : tu vois le devis avant de remplir le cornet.",
    )
    main += block_movento_quote(
        "Photos chaque vendredi, zéro surprise sur le devis. On a signé pour l'extension aussi.",
        author="Sandrine",
        role="Laxou",
    )
    main += block_before_after(
        "gallery-1.png",
        "gallery-2.png",
        before_alt="Maison avant travaux Nancy",
        after_alt="Maison après rénovation Nancy",
        title="Avant / après",
    )
    main += block_movento_contact(
        "Parlons de ton chantier",
        "Dis voir ce qui bloque - on démêle ça ensemble. Réponse sous 48 h.",
        cta_label="Envoyer ma demande",
        phone=BTP_PHONE,
        address=BTP_ADDRESS,
    )
    main += "</main>"
    return _shell_btp(
        "index.html",
        f"{BTP_BRAND} - Entreprise BTP Nancy",
        "Entreprise générale du bâtiment à Nancy : rénovation, extension, ravalement. Devis clair, suivi photo.",
        main,
        nav_kind="solid",
    )


def build_btp_realisations() -> str:
    main = "<main>"
    main += block_snap_chapter(
        "Maison familiale Laxou",
        "Élévation + reamenagement - 9 mois, un chef de chantier dedie, photos chaque vendredi.",
        "scene-1.png",
        "Maison renovee a Laxou",
        reverse=False,
        cta_href="contact.html",
        cta_label="Un projet similaire ?",
    )
    main += block_snap_chapter(
        "Commerce Nancy centre",
        "Ravalement pierre + vitrine - chantier de nuit pour ne pas freiner la boutique.",
        "scene-2.png",
        "Façade commerce après ravalement",
        reverse=True,
    )
    main += block_snap_chapter(
        "Extension Vandoeuvre",
        "Ossature + isolation - livré hors d'eau hors d'air en 11 semaines.",
        "scene-3.png",
        "Extension moderne Vandoeuvre",
        reverse=False,
        cta_href="contact.html",
        cta_label="Demander un devis",
    )
    main += "</main>"
    return _shell_btp(
        "realisations.html",
        f"Réalisations - {BTP_BRAND}",
        "Chantiers BTP livres à Nancy, Laxou et Vandoeuvre - rénovations et extensions.",
        main,
    )


def build_btp_savoir() -> str:
    main = f"""<main>
<section class="vt-mv-services">
  <div class="vt-mv-wrap">
    <p class="vt-mv-eyebrow">Methode</p>
    <h1 class="vt-mv-section-title">Pas de surprise en cours de chantier</h1>
    <p class="vt-mv-lead">Brief clair. Planning affiche. Un interlocuteur. On avance.</p>
    <ol class="vt-mv-services-grid" style="list-style:none;padding:0;counter-reset:step">
      <li class="vt-mv-card vt-mv-card-body"><strong>1. Visite & devis</strong><p class="mb-0 small text-secondary">Sur place sous 5 jours - chiffrage ligne par ligne.</p></li>
      <li class="vt-mv-card vt-mv-card-body"><strong>2. Planning photo</strong><p class="mb-0 small text-secondary">Jalons, livraisons materiaux, points hebdo.</p></li>
      <li class="vt-mv-card vt-mv-card-body"><strong>3. Réception</strong><p class="mb-0 small text-secondary">PV, garanties, et on reste joignable après.</p></li>
    </ol>
    <p class="mt-4"><a class="vt-mv-btn vt-mv-btn-primary" href="contact.html">Lancer un devis</a></p>
  </div>
</section>
</main>"""
    return _shell_btp(
        "savoir-faire.html",
        f"Savoir-faire - {BTP_BRAND}",
        "Methode chantier Chantiers Est Construction : devis, planning photo, reception.",
        main,
    )


def build_btp_contact() -> str:
    main = "<main>"
    main += block_movento_contact(
        "Devis chantier",
        f"Telephone {BTP_PHONE} · {BTP_ADDRESS}",
        cta_label="Envoyer",
        phone=BTP_PHONE,
        address=BTP_ADDRESS,
    )
    main += "</main>"
    return _shell_btp(
        "contact.html",
        f"Contact - {BTP_BRAND}",
        "Contacter Chantiers Est Construction à Nancy pour un devis BTP.",
        main,
    )


# --- Communication : Studio Signal Metz - split agency ---
COM_BRAND = "Studio Signal"
COM_PHONE = "03 87 36 90 14"
COM_EMAIL = "brief@studiosignal.metz"
COM_ADDRESS = "8 rue des Clercs, 57000 Metz"
COM_MAPS = "https://maps.google.com/?q=8+rue+des+Clercs+57000+Metz"
COM_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "cases.html", "label": "Cases"},
    {"file": "offres.html", "label": "Offres"},
    {"file": "contact.html", "label": "Contact"},
]


def _shell_com(page: str, title: str, desc: str, main: str) -> str:
    nav = block_movento_pill_nav(
        COM_BRAND,
        COM_NAV,
        page,
        cta_label="Brief gratuit",
        cta_href="contact.html",
        phone=COM_PHONE,
    )
    foot = block_site_footer(
        COM_BRAND,
        entity=get_entity("communication"),
        slug="communication",
        phone=COM_PHONE,
        address=COM_ADDRESS,
        email=COM_EMAIL,
        maps_href=COM_MAPS,
        nav_links=_foot_links(COM_NAV),
        hours_line="Metz · Agence com",
    )
    mobile = block_mobile_cta("Brief", "contact.html", COM_PHONE)
    body = nav + main + foot + mobile
    return wrap_page(
        title,
        desc,
        body,
        layout="movento-com",
        slug="communication",
        page=page,
        site_name=COM_BRAND,
        nav=COM_NAV,
        head_assets=HEAD_COM,
        body_class="vt-body vt-body-movento vt-body-com",
    )


def build_com_index() -> str:
    main = "<main>"
    main += block_hero_movento_split(
        "Des marques qui se voient",
        "Agence de communication à Metz : identité, site, campagnes locales - on démêle ton message.",
        "hero.png",
        "Équipe creative Studio Signal Metz",
        eyebrow="Metz · Grand Est",
        primary_href="contact.html",
        primary_label="Envoyer un brief",
        secondary_href="cases.html",
        secondary_label="Voir les cases",
        glass_pills=["Identité", "Site web", "Campagnes locales"],
    )
    main += block_movento_proof(
        [
            ("40+", "marques locales"),
            ("3 sem.", "identité type"),
            ("1", "interlocuteur"),
            ("0", "jargon inutile"),
        ]
    )
    main += block_movento_services(
        "Ce qu'on livre",
        [
            {
                "title": "Identité visuelle",
                "text": "Logo, couleurs, ton - une charte que ton equipe peut vraiment utiliser.",
                "img": "card-1.png",
                "alt": "Moodboard identité visuelle",
            },
            {
                "title": "Site qui convertit",
                "text": "Pages claires, numero visible, CTA net - fait pour le commerce local.",
                "img": "card-2.png",
                "alt": "Maquette site web sur ecran",
            },
            {
                "title": "Campagnes de terrain",
                "text": "Affiches, reseaux, print marche - une paire d'actions concretes, pas un roman.",
                "img": "card-3.png",
                "alt": "Campagne affichage locale",
            },
        ],
        lead="Viens avec ton besoin - on en parle entre midi si tu veux.",
    )
    main += block_snap_chapter(
        "Signal clair, pas de bruit",
        "On coupe le blabla agence. Brief court, propositions nettes, tu valides vite.",
        "scene-1.png",
        "Atelier brief creatif Metz",
        reverse=False,
        cta_href="contact.html",
        cta_label="Lancer un brief",
    )
    main += block_movento_contact(
        "Envoie ton brief",
        "Meme un message de 5 lignes suffit. On te rappelle.",
        cta_label="Envoyer",
        phone=COM_PHONE,
        address=COM_ADDRESS,
    )
    main += "</main>"
    return _shell_com(
        "index.html",
        f"{COM_BRAND} - Agence communication Metz",
        "Agence de communication à Metz : identité, sites et campagnes pour commerces du Grand Est.",
        main,
    )


def build_com_cases() -> str:
    main = "<main>"
    main += block_snap_chapter(
        "Brasserie Saint-Jacques",
        "Refonte menu + photos + page reservation - tables pleines le week-end suivant.",
        "scene-1.png",
        "Case resto Metz",
        reverse=False,
    )
    main += block_snap_chapter(
        "Halles Thionville",
        "Campagne drive + fidélité - message simple, flyers marche, retargeting leger.",
        "scene-2.png",
        "Case retail Thionville",
        reverse=True,
    )
    main += block_snap_chapter(
        "Pulse Fitness",
        "Identité + landing essai gratuit - inscriptions en un clic sur telephone.",
        "scene-3.png",
        "Case sport Metz",
        reverse=False,
        cta_href="contact.html",
        cta_label="Un projet comme ca ?",
    )
    main += "</main>"
    return _shell_com(
        "cases.html",
        f"Cases - {COM_BRAND}",
        "Réalisations Studio Signal Metz : restos, commerces, sport.",
        main,
    )


def build_com_offres() -> str:
    main = f"""<main>
<section class="vt-mv-services">
  <div class="vt-mv-wrap">
    <p class="vt-mv-eyebrow">Offres</p>
    <h1 class="vt-mv-section-title">Trois portees d'entree</h1>
    <p class="vt-mv-lead">Prix affiche sur devis PDF - pas la peine de faire le nareux.</p>
    <div class="vt-mv-services-grid">
      <article class="vt-mv-card vt-mv-card-body"><h3 class="h5">Starter signal</h3><p class="small text-secondary mb-0">Logo + couleurs + 1 page accueil. Ideal si tu débutes.</p></article>
      <article class="vt-mv-card vt-mv-card-body"><h3 class="h5">Vitrine complete</h3><p class="small text-secondary mb-0">Identité + site multi-pages + photos IA cadrees.</p></article>
      <article class="vt-mv-card vt-mv-card-body"><h3 class="h5">Campagne locale</h3><p class="small text-secondary mb-0">Print + digital + suivi 30 jours. Une paire d'actions mesurables.</p></article>
    </div>
    <p class="mt-4"><a class="vt-mv-btn vt-mv-btn-primary" href="contact.html">Demander un devis</a></p>
  </div>
</section>
</main>"""
    return _shell_com(
        "offres.html",
        f"Offres - {COM_BRAND}",
        "Offres Studio Signal Metz : starter, vitrine, campagne locale.",
        main,
    )


def build_com_contact() -> str:
    main = "<main>"
    main += block_movento_contact(
        "Brief en 5 lignes",
        f"{COM_ADDRESS} · {COM_PHONE}",
        cta_label="Envoyer",
        phone=COM_PHONE,
        address=COM_ADDRESS,
    )
    main += "</main>"
    return _shell_com(
        "contact.html",
        f"Contact - {COM_BRAND}",
        "Contacter Studio Signal Metz pour un brief communication.",
        main,
    )


# --- Transport : Navette Orne & Moselle - bleed CargoX ---
TR_BRAND = "Navette Orne & Moselle"
TR_PHONE = "03 87 55 20 40"
TR_EMAIL = "courses@orne-moselle.fr"
TR_ADDRESS = "Zone des Gravières, 57140 Woippy"
TR_MAPS = "https://maps.google.com/?q=Woippy+57140"
TR_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "zones.html", "label": "Zones"},
    {"file": "tarifs.html", "label": "Tarifs"},
    {"file": "contact.html", "label": "Contact"},
]


def _shell_tr(page: str, title: str, desc: str, main: str) -> str:
    nav = block_movento_pill_nav(
        TR_BRAND,
        TR_NAV,
        page,
        cta_label="Réserver",
        cta_href="contact.html",
        phone=TR_PHONE,
    )
    foot = block_site_footer(
        TR_BRAND,
        entity=get_entity("transport"),
        slug="transport",
        phone=TR_PHONE,
        address=TR_ADDRESS,
        email=TR_EMAIL,
        maps_href=TR_MAPS,
        nav_links=_foot_links(TR_NAV),
        hours_line="Woippy · VTC & navettes",
    )
    mobile = block_mobile_cta("Réserver", "contact.html", TR_PHONE)
    body = nav + main + foot + mobile
    return wrap_page(
        title,
        desc,
        body,
        layout="movento-transport",
        slug="transport",
        page=page,
        site_name=TR_BRAND,
        nav=TR_NAV,
        head_assets=HEAD_TRANSPORT,
        body_class="vt-body vt-body-movento vt-body-transport",
    )


def build_tr_index() -> str:
    main = "<main>"
    main += block_hero_movento_bleed(
        "De Metz à Thionville, sans stress",
        "VTC, navettes gare/aéroport et transferts pro - flotte propre, chauffeur local, prix annoncé.",
        "hero.png",
        "Vehicule VTC Navette Orne et Moselle",
        badge="Metz · Thionville · Luxembourg frontière",
        primary_href="contact.html",
        primary_label="Réserver une course",
        phone_href="tel:0387552040",
        phone_label="Appeler la centrale",
        secondary_href="tarifs.html",
        secondary_label="Voir les tarifs",
    )
    main += block_movento_proof(
        [
            ("15 min", "prise en charge type"),
            ("7j/7", "centrale"),
            ("100 %", "prix affiché"),
            ("0", "surprise peage"),
        ]
    )
    main += block_movento_services(
        "Courses qu'on fait bien",
        [
            {
                "title": "Gare & aéroport",
                "text": "Metz-Ville, Lorraine TGV, Lux-Findel - on t'attend avec le panneau.",
                "img": "card-1.png",
                "alt": "Prise en charge gare Metz",
            },
            {
                "title": "Trajets pro",
                "text": "RDV client, salon, hôpital - facture entreprise propre.",
                "img": "card-2.png",
                "alt": "Transfert professionnel berline",
            },
            {
                "title": "Navette groupe",
                "text": "Mariage, événement, équipe chantier - van 8 places sur demande.",
                "img": "card-3.png",
                "alt": "Van navette groupe",
            },
        ],
        lead="J'attends pas sur un miracle : adresse, heure, on confirme.",
    )
    main += block_snap_chapter(
        "Chauffeurs du coin",
        "On connaît les bouchons de l'A31 et les sorties mosellanes. Pas de GPS perdu.",
        "scene-1.png",
        "Chauffeur local Moselle",
        reverse=False,
        cta_href="contact.html",
        cta_label="Réserver",
    )
    main += block_movento_contact(
        "Réserve ta course",
        "Dis voir le trajet - on te confirme le prix avant de démarrer.",
        cta_label="Envoyer",
        phone=TR_PHONE,
        address=TR_ADDRESS,
    )
    main += "</main>"
    return _shell_tr(
        "index.html",
        f"{TR_BRAND} - VTC Metz Thionville",
        "VTC et navettes Metz, Thionville, aéroport Luxembourg - prix affiché, chauffeur local.",
        main,
    )


def build_tr_zones() -> str:
    main = "<main>"
    main += block_snap_chapter(
        "Metz & agglo",
        "Centre, Borny, Woippy, Montigny - prise en charge rapide.",
        "scene-1.png",
        "Zone Metz",
        reverse=False,
    )
    main += block_snap_chapter(
        "Thionville & Nord",
        "Yutz, Hayange, frontière Lux - trajets quotidiens.",
        "scene-2.png",
        "Zone Thionville",
        reverse=True,
    )
    main += block_snap_chapter(
        "Longue distance",
        "Paris, Strasbourg, Nancy - devis fixe avant depart.",
        "scene-3.png",
        "Autoroute A31",
        reverse=False,
        cta_href="contact.html",
        cta_label="Demander un devis",
    )
    main += "</main>"
    return _shell_tr(
        "zones.html",
        f"Zones - {TR_BRAND}",
        "Zones de prise en charge Navette Orne et Moselle : Metz, Thionville, longue distance.",
        main,
    )


def build_tr_tarifs() -> str:
    main = f"""<main>
<section class="vt-mv-services">
  <div class="vt-mv-wrap">
    <p class="vt-mv-eyebrow">Tarifs indicatifs</p>
    <h1 class="vt-mv-section-title">Prix annonce, peage inclus</h1>
    <p class="vt-mv-lead">Exemples - le devis exact part après ton adresse.</p>
    <div class="vt-mv-services-grid">
      <article class="vt-mv-card vt-mv-card-body"><h3 class="h5">Metz → Gare</h3><p class="small text-secondary mb-0">A partir de 18 euro</p></article>
      <article class="vt-mv-card vt-mv-card-body"><h3 class="h5">Metz → Findel</h3><p class="small text-secondary mb-0">A partir de 75 euro</p></article>
      <article class="vt-mv-card vt-mv-card-body"><h3 class="h5">Thionville → Metz</h3><p class="small text-secondary mb-0">A partir de 45 euro</p></article>
    </div>
    <p class="mt-4"><a class="vt-mv-btn vt-mv-btn-primary" href="contact.html">Confirmer mon trajet</a></p>
  </div>
</section>
</main>"""
    return _shell_tr(
        "tarifs.html",
        f"Tarifs - {TR_BRAND}",
        "Tarifs indicatifs VTC Metz Thionville Luxembourg - peage inclus.",
        main,
    )


def build_tr_contact() -> str:
    main = "<main>"
    main += block_movento_contact(
        "Réserve maintenant",
        f"{TR_ADDRESS} · {TR_PHONE}",
        cta_label="Envoyer",
        phone=TR_PHONE,
        address=TR_ADDRESS,
    )
    main += "</main>"
    return _shell_tr(
        "contact.html",
        f"Contact - {TR_BRAND}",
        "Réserver une course Navette Orne et Moselle.",
        main,
    )


BUILDERS_SECTEURS_MOVENTO = {
    "btp": [
        ("index.html", build_btp_index),
        ("realisations.html", build_btp_realisations),
        ("savoir-faire.html", build_btp_savoir),
        ("contact.html", build_btp_contact),
    ],
    "communication": [
        ("index.html", build_com_index),
        ("cases.html", build_com_cases),
        ("offres.html", build_com_offres),
        ("contact.html", build_com_contact),
    ],
    "transport": [
        ("index.html", build_tr_index),
        ("zones.html", build_tr_zones),
        ("tarifs.html", build_tr_tarifs),
        ("contact.html", build_tr_contact),
    ],
}
