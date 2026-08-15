#!/usr/bin/env python3
"""Assemble un site vitrine complet à partir des blocs vitrine_site_blocks (Bootstrap 5)."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from vitrine_seo import get_entity
from vitrine_metiers_extra import BUILDERS_EXTRA


def _chrome_nav(slug: str, brand: str, nav: list, page: str, *, cta_label: str, cta_href: str) -> str:
    return block_site_nav(brand, nav, page, cta_label=cta_label, cta_href=cta_href, slug=slug)


def _chrome_foot(slug: str, brand: str, **kwargs) -> str:
    return block_site_footer(brand, entity=get_entity(slug), slug=slug, **kwargs)

from vitrine_site_blocks import (
    block_appointment_form,
    block_cards_bs,
    block_cabinet_contact_form,
    block_chef,
    block_chapters,
    block_cross_links,
    block_cta_band,
    block_dental_appointment_form,
    block_education_enrollment_form,
    block_hotel_reservation_form,
    block_facility_quote_form,
    block_saas_trial_form,
    block_tech_demo_form,
    block_fitness_trial_form,
    block_association_contact_form,
    block_photo_quote_form,
    block_garage_appointment_form,
    block_hero_rich,
    block_industrial_rfq_form,
    block_architecture_brief_form,
    block_legal_consultation_form,
    block_property_estimation_form,
    block_info_bar,
    block_menu_section,
    block_mobile_cta,
    block_reservation_form,
    block_retail_contact_form,
    block_site_footer,
    block_site_nav,
    block_stats,
    block_story,
    block_timeline,
    block_trust,
    wrap_page,
    wrap_page_architecture,
    wrap_page_cabinet,
    wrap_page_education,
    wrap_page_facility,
    wrap_page_saas,
    wrap_page_tech,
    HEAD_SAAS,
    HEAD_SAAS_ONBOARDING,
    HEAD_SAAS_DASHBOARD,
    HEAD_SAAS_EMPTY,
    HEAD_SAAS_NOTIFICATIONS,
    wrap_page_hotel,
    wrap_page_association,
    wrap_page_photo,
    wrap_page_fitness,
    wrap_page_garage,
    wrap_page_industrial,
    wrap_page_legal,
    wrap_page_medical,
    wrap_page_property,
    wrap_page_retail,
    wrap_page_spa,
)
from vitrine_layouts import (
    block_assist_chips,
    block_booking_strip,
    block_slot_card,
    block_spa_fab,
    block_spa_m3_hero,
    block_spa_m3_nav,
    block_spa_m3_phares,
    block_garage_m3_hero,
    block_garage_m3_local,
    block_garage_m3_nav,
    block_garage_m3_stats,
    block_phone_fab,
    block_immo_m3_hero,
    block_immo_m3_listings,
    block_immo_m3_nav,
    block_immo_m3_search,
    block_photo_m3_nav,
    block_photo_m3_masonry,
    block_photo_toast,
    block_plus_fab,
    block_hotel_m3_nav,
    block_hotel_m3_hero,
    block_hotel_m3_booking,
    block_hotel_m3_rooms,
    block_dialog_m3,
    block_fab_menu_m3,
    block_friction_m3,
    block_health_booking_hero_m3,
    block_health_stats_m3,
    block_journey_m3,
    block_marquee_m3,
    block_menu_h_cards_m3,
    block_motives_m3,
    block_nav_rail_m3,
    block_photo_chapters_m3,
    block_pill_appbar_m3,
    block_rail_topbar_m3,
    block_reviews_m3,
    block_snackbar_m3,
    block_sticky_cta_m3,
    block_surface_band_m3,
    block_bento_cards,
    block_compact_features,
    block_comparison_table,
    block_credentials_strip,
    block_faq_accordion,
    block_funnel_steps,
    block_gallery_masonry,
    block_hero_editorial,
    block_hero_overlay,
    block_hero_proof_split,
    block_impact_goal,
    block_hero_split,
    block_hero_split_reverse,
    block_hero_property_search,
    block_hero_technical,
    block_kpi_grid,
    block_listing_grid,
    block_feature_tabs,
    block_hero_saas_product,
    block_hero_tech_glow,
    block_notification_feed,
    block_pricing_tiers,
    block_progress_wizard,
    block_state_morph,
    block_marquee_strip,
    block_motion_progress,
    block_neighborhood_strip,
    block_process_flow,
    block_project_grid,
    block_promo_cards,
    block_schedule_grid,
    block_sector_strip,
    block_service_tiles,
    block_snap_chapters,
    block_spec_grid,
    block_specs_table,
    block_stat_narrative_rows,
    block_cert_strip,
    block_trust_strip,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "vitrines" / "demos"

BRAND = "Brasserie Saint-Jacques"
PHONE = "03 87 75 12 34"
ADDRESS = "12 place Saint-Jacques, 57000 Metz"
MAPS = "https://maps.google.com/?q=12+place+Saint-Jacques+57000+Metz"
NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "carte.html", "label": "La carte"},
    {"file": "histoire.html", "label": "Notre histoire"},
    {"file": "contact.html", "label": "Contact"},
]

CHAPTERS = [
    {
        "title": "Le feu de la cuisine",
        "text": "Four à bois et casseroles en cuivre derrière le passe — la brigade d'Élodie Marchal mijote ici chaque service.",
        "img": "scene-1.png",
        "alt": "Cuisine ouverte avec flammes à Metz",
    },
    {
        "title": "Le bar",
        "text": "Zinc d'origine, presse mosellane et quarante-cinq références en cave — le comptoir où les Messins prennent leur café.",
        "img": "scene-2.png",
        "alt": "Comptoir en zinc de brasserie",
    },
    {
        "title": "La terrasse avec vue",
        "text": "Face à la cathédrale, apéritif et tapas lorrains au soleil — la terrasse se remplit dès les beaux jours.",
        "img": "scene-3.png",
        "alt": "Terrasse face à la cathédrale de Metz",
    },
]

SIGNATURES = [
    {"title": "Menu du marché", "text": "Carte renouvelée chaque semaine selon le marché Saint-Jacques.", "img": "card-1.png", "alt": "Assiette gastronomique lorraine"},
    {"title": "Brunch dominical", "text": "Brioche perdue à la mirabelle — réservation conseillée.", "img": "card-2.png", "alt": "Brunch dominical"},
    {"title": "Privatisation", "text": "Salon du premier pour 40 couverts.", "img": "card-3.png", "alt": "Salon privatisé"},
]

MENU_SECTIONS = [
    {
        "title": "Entrées",
        "items": [
            {"name": "Terrine de canard maison", "desc": "Cornichons, pain de campagne grillé", "price": "12 €", "tags": ["Maison"]},
            {"name": "Salade de Munster", "desc": "Pommes de terre, lardons fumés, vinaigrette moutarde", "price": "11 €", "tags": ["Végétarien"]},
            {"name": "Soupe à l'oignon gratinée", "desc": "Bouillon 24 h, comté", "price": "10 €", "tags": []},
            {"name": "Quiche au cow-gomme", "desc": "Marché Saint-Jacques, salade verte", "price": "13 €", "tags": ["Végétarien"]},
        ],
    },
    {
        "title": "Plats",
        "items": [
            {"name": "Bouchée à la reine", "desc": "Vol-au-vent, champignons, sauce supreme", "price": "24 €", "tags": ["Signature"]},
            {"name": "Jarret confit", "desc": "Purée maison, jus au thym", "price": "22 €", "tags": []},
            {"name": "Sandre du canal", "desc": "Beurre blanc, légumes de Hagondange", "price": "26 €", "tags": []},
            {"name": "Assiette du marché", "desc": "Selon arrivage — demandez au serveur", "price": "21 €", "tags": ["Saison"]},
        ],
    },
    {
        "title": "Desserts",
        "items": [
            {"name": "Clafoutis mirabelle", "desc": "Crème fraîche d'Alsace", "price": "9 €", "tags": ["Maison"]},
            {"name": "Tarte aux quetsches", "desc": "Pâte sablée, glace vanille", "price": "9 €", "tags": []},
            {"name": "Brioche perdue", "desc": "Mirabelles poêlées — brunch dimanche", "price": "11 €", "tags": ["Brunch"]},
        ],
    },
    {
        "title": "Boissons",
        "items": [
            {"name": "Riesling mosellan (verre)", "desc": "Domaine des Trésors, 2022", "price": "6 €", "tags": []},
            {"name": "Bière artisanale Lorraine", "desc": "Pression ou bouteille 33 cl", "price": "5 €", "tags": []},
            {"name": "Café gourmand", "desc": "Trois mignardises maison", "price": "8 €", "tags": []},
        ],
    },
]


def _shell(page: str, title: str, desc: str, main: str) -> str:
    rail = block_nav_rail_m3(
        BRAND,
        NAV,
        page,
        hours="Ouvert aujourd'hui 12:00 - 14:30, 19:00 - 23:00",
        address=ADDRESS,
        phone=PHONE,
        tagline="Metz · depuis 1924",
    )
    top = block_rail_topbar_m3(
        search_placeholder="Reserver une table",
        cta_label="Reserver",
        cta_dialog="resaDialog" if page == "index.html" else "",
        cta_href="contact.html",
    )
    # Modale resa aussi sur les pages internes (bouton topbar / FAB)
    if page != "index.html":
        main += block_dialog_m3(
            dialog_id="resaDialog",
            title="Reserver une table",
            lead="Dis-nous le jour, l'heure et le nombre - on te repond sous 1 h (demo).",
            primary_label="Envoyer la demande",
            primary_href="contact.html",
            fields_html="""<div class="row g-2">
      <div class="col-6"><label class="form-label small">Date</label><input type="date" class="form-control"></div>
      <div class="col-6"><label class="form-label small">Heure</label><input type="time" class="form-control" value="19:30"></div>
      <div class="col-12"><label class="form-label small">Convives</label><input type="number" class="form-control" value="2" min="1" max="12"></div>
    </div>""",
        )
        main += block_fab_menu_m3(
            [
                {"label": "Reserver", "dialog": "resaDialog"},
                {"label": "La carte", "href": "carte.html"},
                {"label": "Appeler", "href": "tel:0387751234"},
            ],
            main_label="Actions brasserie",
        )
    foot = _chrome_foot("restauration", BRAND, phone=PHONE, address=ADDRESS)
    mobile = block_mobile_cta("Réserver", "contact.html", PHONE)
    body = f'<div class="vt-rail-shell">{rail}<div class="vt-rail-main">{top}{main}{foot}{mobile}</div></div>'
    return wrap_page(title, desc, body, slug="restauration", page=page, site_name=BRAND, nav=NAV)


def build_index() -> str:
    main = "<main>"
    main += """<section class="vt-br-hero vt-br-hero--bleed vt-reveal">
  <div class="vt-br-hero-bg" aria-hidden="true">
    <picture><source srcset="images/card-1.webp" type="image/webp"><img src="images/card-1.png" alt="" decoding="async" fetchpriority="high"></picture>
  </div>
  <div class="container vt-br-hero-copy">
    <p class="vt-eyebrow text-uppercase mb-2">Brasserie · Metz · depuis 1924</p>
    <h1 class="vt-display display-4 mb-3">Cuisine de saison &amp; partage</h1>
    <p class="lead mb-4">Terrasse face a la cathedrale, mijotes au feu de bois, vins mosellans - sans usine a touristes.</p>
    <div class="d-flex flex-wrap gap-2">
      <button type="button" class="btn btn-vt-primary btn-lg px-4" data-vt-dialog-open="resaDialog">Reserver une table</button>
      <a class="btn btn-vt-outline btn-lg px-4" href="carte.html">Voir la carte</a>
    </div>
  </div>
</section>"""
    main += block_menu_h_cards_m3(
        [
            {"title": "Terrine de canard", "text": "Cornichons, pain grille", "price": "12 €", "img": "card-1.png", "alt": "Terrine"},
            {"title": "Noix de Saint-Jacques", "text": "Beurre blanc - signature", "price": "18 €", "img": "scene-1.png", "alt": "Saint-Jacques", "featured": True},
            {"title": "Jarret confit", "text": "Puree maison, jus au thym", "price": "22 €", "img": "card-2.png", "alt": "Jarret"},
            {"title": "Clafoutis mirabelle", "text": "Creme fraiche d'Alsace", "price": "9 €", "img": "card-3.png", "alt": "Dessert"},
        ],
        kicker="A la carte ce soir",
        title="Ce que la brigade sort du passe",
        chips=[
            {"label": "Entrees", "active": True},
            {"label": "Plats"},
            {"label": "Poissons"},
            {"label": "Desserts"},
        ],
    )
    main += """<section class="vt-br-split vt-reveal">
  <div class="container">
    <div class="row g-4 align-items-center">
      <div class="col-md-6">
        <figure class="mb-0 vt-br-hero-media">
          <picture><source srcset="images/scene-2.webp" type="image/webp"><img src="images/scene-2.png" class="w-100" alt="Zinc de la brasserie" loading="lazy" decoding="async"></picture>
        </figure>
      </div>
      <div class="col-md-6">
        <p class="vt-eyebrow text-uppercase">Le zinc</p>
        <h2 class="vt-section-title h3">Un comptoir qui a vu des generations</h2>
        <p class="text-secondary">Zinc d'origine, presse mosellane, quarante-cinq references en cave. Tu t'assois, on te sert - comme au cafe du coin, en mieux.</p>
        <a class="btn btn-vt-outline mt-2" href="histoire.html">L'histoire de la maison</a>
      </div>
    </div>
  </div>
</section>"""
    main += block_reviews_m3(
        title="Ce qu'on retient a table",
        rating="4,7/5",
        rating_label="avis",
        reviews=[
            {"name": "Marie L.", "meta": "Terrasse", "text": "Vue cathedrale, service souriant, mirabelle au top.", "stars": 5},
            {"name": "Thomas B.", "meta": "Menu marche", "text": "Carte courte et honnete. Pas de mauvaise surprise.", "stars": 5},
            {"name": "Claire D.", "meta": "Brunch", "text": "Brioche perdue a reserver. Ambiance familiale.", "stars": 5},
        ],
    )
    main += block_cta_band("Table pour ce soir ? On confirme en moins d'une heure.", "Reserver", "contact.html")
    main += block_dialog_m3(
        dialog_id="resaDialog",
        title="Reserver une table",
        lead="Dis-nous le jour, l'heure et le nombre - on te repond sous 1 h (demo, rien n'est envoye).",
        primary_label="Envoyer la demande",
        primary_href="contact.html",
        fields_html="""<div class="row g-2">
      <div class="col-6"><label class="form-label small">Date</label><input type="date" class="form-control"></div>
      <div class="col-6"><label class="form-label small">Heure</label><input type="time" class="form-control" value="19:30"></div>
      <div class="col-12"><label class="form-label small">Convives</label><input type="number" class="form-control" value="2" min="1" max="12"></div>
    </div>""",
    )
    main += block_snackbar_m3("Ajoute au panier demo")
    main += block_fab_menu_m3(
        [
            {"label": "Reserver", "dialog": "resaDialog"},
            {"label": "La carte", "href": "carte.html"},
            {"label": "Appeler", "href": "tel:0387751234"},
        ],
        main_label="Actions brasserie",
    )
    main += block_sticky_cta_m3("Creneau ce soir ?", "Reserver", "contact.html", dialog="resaDialog")
    main += "</main>"
    return _shell("index.html", f"{BRAND} — Accueil", "Brasserie historique à Metz : cuisine lorraine, terrasse place Saint-Jacques et réservation en ligne.", main)


def build_carte() -> str:
    main = "<main>"
    main += block_hero_rich(
        "Une carte qui suit les saisons mosellanes",
        "Du marché à votre assiette — fournisseurs à moins de 80 km.",
        "hero.png",
        "Plats colorés en cuisine lorraine",
        eyebrow="La carte",
        primary_href="contact.html",
        primary_label="Réserver",
        secondary_href="index.html",
        secondary_label="Découvrir la brasserie",
    )
    main += block_menu_section(
        "Entrées, plats & desserts",
        "Prix TTC, service compris. Carte renouvelée chaque semaine selon le marché Saint-Jacques.",
        MENU_SECTIONS,
    )
    main += block_story(
        "Produits du terroir",
        ["Maraîchers de Hagondange, fromager de Saint-Hubert, vigneron de la Moselle — la carte raconte la Lorraine."],
    )
    main += block_cta_band("Allergies ou régimes spécifiques ? Prévenez-nous à la réservation.", "Nous contacter", "contact.html")
    main += "</main>"
    return _shell("carte.html", f"La carte — {BRAND}", "Carte saisonnière : entrées lorraines, plats mijotés et bières artisanales.", main)


def build_histoire() -> str:
    main = "<main>"
    main += block_hero_rich(
        "Cent ans de convivialité messine",
        "De l'auberge des voyageurs à la brasserie contemporaine.",
        "hero.png",
        "Façade historique en pierre jaune",
        eyebrow="Notre histoire",
        primary_href="contact.html",
        primary_label="Réserver une visite",
        secondary_href="carte.html",
        secondary_label="Notre carte",
    )
    main += block_timeline([
        ("1924", "Ouverture de l'auberge Saint-Jacques pour les cheminots."),
        ("1958", "Transformation en brasserie avec zinc d'époque."),
        ("2003", "Rénovation de la verrière Art déco."),
        ("2019", "Élodie Marchal reprend les fourneaux."),
    ])
    main += block_chapters(CHAPTERS)
    main += block_chef(
        "Élodie Marchal",
        "Cheffe · depuis 2019",
        "Formée chez les grandes maisons lorraines, Élodie revisite le bouchée-à-la-reine et la mirabelle sans folklore : produits du marché, technique classique, assiettes généreuses.",
    )
    main += block_trust(
        "Visite guidée le premier samedi du mois — sur réservation.",
        ["Pierre de Jaumont", "Verrière Art déco", "Zinc d'origine", "Famille messine"],
    )
    main += block_cta_band("Visite guidée le premier samedi du mois.", "Réserver une visite", "contact.html")
    main += "</main>"
    return _shell("histoire.html", f"Notre histoire — {BRAND}", "Cent ans d'histoire gastronomique au cœur de Metz.", main)


def build_contact() -> str:
    main = """<main>
<section class="vt-hero-compact py-5 text-center">
  <div class="container">
    <p class="vt-eyebrow text-uppercase">Contact</p>
    <h1 class="vt-display display-6">Réserver ou nous écrire</h1>
    <p class="lead text-secondary">12 place Saint-Jacques, 57000 Metz — réponse sous 2 h.</p>
  </div>
</section>"""
    main += block_reservation_form()
    main += block_cta_band("Groupes de 8 personnes et plus : menu sur mesure et salon privatisable.", "Appeler le restaurant", "tel:0387751234")
    main += "</main>"
    return _shell("contact.html", f"Contact — {BRAND}", "Réservez votre table à Metz, place Saint-Jacques.", main)


# --- Spa Thalie (beaute) — layout M3 maquette (_maquettes-echantillons/images/beaute-m3.png) ---
B_Brand = "Spa Thalie"
B_CITY = "Metz"
B_PHONE = "03 87 17 42 80"
B_ADDRESS = "8 rue des Clercs, 57000 Metz"
B_EMAIL = "bonjour@spa-thalie.fr"
B_MAPS = "https://maps.google.com/?q=8+rue+des+Clercs+57000+Metz"
B_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "soins.html", "label": "Soins"},
    {"file": "soins.html#forfaits", "label": "Forfaits"},
    {"file": "ambiance.html", "label": "Engagements"},
    {"file": "ambiance.html#propos", "label": "À propos"},
    {"file": "contact.html", "label": "Contact"},
]
B_FOOTER_NAV = [
    ("Soins", "soins.html"),
    ("Forfaits", "soins.html#forfaits"),
    ("Engagements", "ambiance.html"),
    ("Carte cadeau", "contact.html"),
    ("Prendre RDV", "contact.html"),
]
B_PHARES = [
    {
        "title": "Soin visage éclat",
        "text": "Nettoyage, massage et masque hydratant pour une peau lumineuse.",
        "img": "card-1.png",
        "alt": "Soin visage éclat",
        "duration": "60 min",
        "price": "75 €",
    },
    {
        "title": "Massage aux pierres chaudes",
        "text": "Chaleur des pierres volcaniques pour dénouer les tensions.",
        "img": "card-2.png",
        "alt": "Massage pierres chaudes",
        "duration": "75 min",
        "price": "95 €",
    },
    {
        "title": "Massage relaxant",
        "text": "Huiles chaudes, rythme lent - idéal après une journée chargée.",
        "img": "scene-2.png",
        "alt": "Massage relaxant",
        "duration": "50 min",
        "price": "70 €",
    },
    {
        "title": "Rituel gommage & enveloppement",
        "text": "Gommage mirabelle et enveloppement pour une peau toute douce.",
        "img": "card-3.png",
        "alt": "Rituel corps spa",
        "duration": "90 min",
        "price": "110 €",
    },
]
B_CHAPTERS_INDEX = [
    {
        "title": "Cabine calme, a deux pas de la gare",
        "text": "Lumiere tamisee, huiles chaudes - tu coupes vraiment le bruit de Metz pendant le soin.",
        "img": "scene-1.png",
        "alt": "Cabine de soin Spa Thalie",
    },
    {
        "title": "Protocoles visage sans vente forcee",
        "text": "Diagnostic court a l'arrivee. On te dit ce qui est utile pour ta peau - et ce qui peut attendre.",
        "img": "scene-2.png",
        "alt": "Soin du visage en institut",
    },
    {
        "title": "Salon de repos apres le soin",
        "text": "Tisane, conseils maison, et le temps de te rhabiller sans te precipiter.",
        "img": "scene-3.png",
        "alt": "Espace detente au spa",
    },
]
B_CHAPTERS_AMBIANCE = [
    {"title": "Accueil", "text": "Thé bio dès l'arrivée et diagnostic de peau personnalisé.", "img": "scene-1.png", "alt": "Accueil spa"},
    {"title": "Cabines doubles", "text": "Massages synchronisés à deux - idéal pour un moment à partager.", "img": "scene-2.png", "alt": "Cabine duo"},
    {"title": "Salon de repos", "text": "Tisanes bio après chaque soin, dans le calme de la cour intérieure.", "img": "scene-3.png", "alt": "Salon de repos"},
]
B_SOINS_SECTIONS = [
    {
        "title": "Soins visage",
        "items": [
            {"name": "Soin visage éclat", "desc": "Nettoyage, massage, masque hydratant", "price": "75 €", "tags": ["60 min"]},
            {"name": "Éclat express", "desc": "Coup de frais entre midi", "price": "59 €", "tags": ["45 min", "Découverte"]},
            {"name": "Cure anti-âge", "desc": "4 séances radiofréquence + sérum HA", "price": "320 €", "tags": ["Cure"]},
        ],
    },
    {
        "title": "Massages & corps",
        "items": [
            {"name": "Massage relaxant", "desc": "Huiles chaudes, rythme lent", "price": "70 €", "tags": ["50 min"]},
            {"name": "Pierres chaudes", "desc": "Détente musculaire profonde", "price": "95 €", "tags": ["75 min"]},
            {"name": "Rituel gommage & enveloppement", "desc": "Gommage mirabelle + enveloppement", "price": "110 €", "tags": ["90 min", "Signature"]},
        ],
    },
    {
        "title": "Forfaits",
        "items": [
            {"name": "Duo bien-être", "desc": "2 soins visage éclat + thé", "price": "135 €", "tags": ["Forfait"]},
            {"name": "Carte cadeau", "desc": "Montant libre, valable 12 mois", "price": "dès 50 €", "tags": ["Cadeau"]},
            {"name": "Atelier maquillage", "desc": "Cours privé 1 h30 avant événement", "price": "70 €", "tags": ["Privé"]},
        ],
    },
]


def _shell_beaute(page: str, title: str, desc: str, main: str) -> str:
    nav = block_spa_m3_nav(
        B_Brand,
        B_NAV,
        page,
        city=B_CITY,
        phone=B_PHONE,
        cta_label="Prendre RDV",
        cta_href="contact.html",
    )
    foot = _chrome_foot(
        "beaute",
        B_Brand,
        phone=B_PHONE,
        address=B_ADDRESS,
        email=B_EMAIL,
        maps_href=B_MAPS,
        nav_links=B_FOOTER_NAV,
        hours_line="Mar–sam 10h–19h · Dim. sur RDV",
    )
    fab = block_spa_fab("contact.html", "Prendre rendez-vous")
    mobile = block_mobile_cta("Prendre RDV", "contact.html", B_PHONE)
    return wrap_page_spa(
        title,
        desc,
        nav + main + foot + fab + mobile,
        slug="beaute",
        page=page,
        site_name=B_Brand,
        nav=B_NAV,
        layout="spa-m3",
    )


def build_beaute_index() -> str:
    main = '<main itemscope itemtype="https://schema.org/WebPage">'
    main += block_spa_m3_hero(
        "L'art du bien-être, près de chez vous.",
        "Soins visage, massages et rituels corps dans un institut calme, à deux minutes de la gare de Metz.",
        "scene-1.png",
        "Cabine de soin Spa Thalie à Metz",
        eyebrow="Institut & spa à Metz",
        primary_href="contact.html",
        primary_label="Prendre RDV",
        facts=[
            {"icon": "⏱", "title": "Ouvert aujourd'hui", "text": "10:00 – 19:00"},
            {"icon": "🎁", "title": "Carte cadeau", "text": "Offrez un moment"},
            {"icon": "📍", "title": "2 min de la Gare", "text": "8 rue des Clercs, Metz"},
        ],
    )
    main += block_spa_m3_phares(
        kicker="Nos soins phares",
        title="Prenez soin de vous",
        chips=[
            {"label": "Soins", "href": "soins.html", "active": True},
            {"label": "Forfaits", "href": "soins.html#forfaits"},
            {"label": "Engagements", "href": "ambiance.html"},
        ],
        cards=B_PHARES,
    )
    main += block_cta_band(
        "Un creneau libre cette semaine ? On confirme sous 2 h.",
        "Choisir mon soin",
        "contact.html",
    )
    main += """<section class="vt-reveal py-5 vt-spa-ritual">
  <div class="container">
    <div class="row g-4">
      <div class="col-md-4"><div class="vt-ritual-step"><span>01</span><h3 class="h6">Tu reserves</h3><p class="small text-secondary mb-0">En ligne ou telephone - confirmation sous 2 h.</p></div></div>
      <div class="col-md-4"><div class="vt-ritual-step"><span>02</span><h3 class="h6">Diagnostic</h3><p class="small text-secondary mb-0">A l'arrivee : ecoute, peaux sensibles bienvenues.</p></div></div>
      <div class="col-md-4"><div class="vt-ritual-step"><span>03</span><h3 class="h6">Le soin</h3><p class="small text-secondary mb-0">Cabine calme, the apres - tu coupes vraiment.</p></div></div>
    </div>
  </div>
</section>"""
    main += """<section class="vt-reveal py-5">
  <div class="container">
    <div class="row g-4 align-items-center">
      <div class="col-lg-7">
        <p class="vt-eyebrow text-uppercase">Carte cadeau</p>
        <h2 class="vt-section-title h3">Offrir un soin sans se tromper</h2>
        <p class="text-secondary mb-3">Montant libre, PDF le jour meme, valable 12 mois.</p>
        <button type="button" class="btn btn-vt-primary" data-vt-dialog-open="giftDialog">Offrir une carte</button>
      </div>
      <div class="col-lg-5">
        <div class="p-4 rounded-4 vt-spa-gift-preview">
          <p class="mb-2 fw-semibold">Exemple</p>
          <p class="small text-secondary mb-0">Rituel gommage 110 euro - PDF sous 10 min (demo).</p>
        </div>
      </div>
    </div>
  </div>
</section>"""
    main += block_dialog_m3(
        dialog_id="rdvDialog",
        title="Prendre RDV",
        lead="Choisis un soin et un creneau - on confirme sous 2 h (demo).",
        primary_label="Confirmer",
        primary_href="contact.html",
        fields_html='<div class="mb-2"><label class="form-label small">Soin</label><select class="form-select"><option>Soin visage eclat</option><option>Massage pierres</option></select></div><div class="mb-2"><label class="form-label small">Quand</label><input type="datetime-local" class="form-control"></div>',
    )
    main += block_dialog_m3(
        dialog_id="giftDialog",
        title="Carte cadeau",
        lead="Montant libre, valable 12 mois (demo).",
        primary_label="Recevoir le PDF",
        primary_href="contact.html",
        fields_html='<div class="mb-2"><label class="form-label small">Montant</label><input type="number" class="form-control" value="75" min="50"></div>',
    )
    main += block_snackbar_m3("Demande envoyee (demo)")
    main += block_fab_menu_m3([
        {"label": "Prendre RDV", "dialog": "rdvDialog"},
        {"label": "Carte cadeau", "dialog": "giftDialog"},
        {"label": "Soins", "href": "soins.html"},
    ], main_label="Actions spa")
    main += "</main>"
    return _shell_beaute(
        "index.html",
        f"{B_Brand} — Institut & spa à Metz",
        "Institut beauté et spa à Metz : soins, massages et RDV en ligne.",
        main,
    )


def build_beaute_soins() -> str:
    main = "<main>"
    main += block_spa_m3_hero(
        "Des protocoles pensés pour votre peau",
        "Express entre midi, rituels complets le week-end - tarifs affichés, sans surprise.",
        "hero.png",
        "Produits de soin en cabine",
        eyebrow="Soins & forfaits",
        primary_href="contact.html",
        primary_label="Prendre RDV",
        facts=[
            {"icon": "⏱", "title": "Diagnostic offert", "text": "À la première visite"},
            {"icon": "🎁", "title": "Carte cadeau", "text": "Valable 12 mois"},
            {"icon": "📍", "title": "Metz centre", "text": "8 rue des Clercs"},
        ],
    )
    main += block_spa_m3_phares(
        kicker="Sélection",
        title="Les plus demandés",
        chips=[
            {"label": "Soins", "href": "#menu-title", "active": True},
            {"label": "Forfaits", "href": "#forfaits"},
            {"label": "Engagements", "href": "ambiance.html"},
        ],
        cards=B_PHARES,
    )
    main += '<div id="forfaits"></div>'
    main += block_menu_section(
        "Catalogue des soins",
        "Tarifs indicatifs TTC. Diagnostic offert à la première visite.",
        B_SOINS_SECTIONS,
    )
    main += block_cta_band("Carte cadeau valable un an - à offrir ou s'offrir.", "Offrir un soin", "contact.html")
    main += "</main>"
    return _shell_beaute("soins.html", f"Soins — {B_Brand}", "Protocoles visage, massages et forfaits à Metz.", main)


def build_beaute_ambiance() -> str:
    main = '<main id="propos">'
    main += block_spa_m3_hero(
        "Un institut calme, près de la gare",
        "Pierre, lumière douce et protocoles clean - le luxe responsable au quotidien.",
        "hero.png",
        "Hall d'accueil Spa Thalie Metz",
        eyebrow="Engagements & à propos",
        primary_href="contact.html",
        primary_label="Planifier une visite",
        facts=[
            {"icon": "⏱", "title": "Visite guidée", "text": "Mercredi 14h–17h"},
            {"icon": "🎁", "title": "Linge local", "text": "Partenaire ESAT"},
            {"icon": "📍", "title": "Eau filtrée", "text": "Produits français"},
        ],
    )
    main += block_story(
        "Nos engagements",
        [
            "Eau filtrée, linge local, partenariat ESAT de Laxou - on préfère le concret au grand discours.",
            "Chaque protocole est expliqué avant le soin : durée, produits, et ce que tu peux attendre.",
        ],
    )
    main += block_chapters(B_CHAPTERS_AMBIANCE)
    main += block_trust(
        "Visite sur RDV mercredi après-midi.",
        ["Clean beauty", "Cour intérieure", "Technologie LED", "Partenaire ESAT"],
    )
    main += block_cta_band("Visite guidée le mercredi 14h–17h.", "Planifier une visite", "contact.html")
    main += "</main>"
    return _shell_beaute("ambiance.html", f"Engagements — {B_Brand}", "Lieux, cabines et engagements du Spa Thalie à Metz.", main)


def build_beaute_contact() -> str:
    main = """<main>
<section class="vt-m3-hero pt-5 pb-4">
  <div class="container">
    <p class="vt-eyebrow text-uppercase">Contact</p>
    <h1 class="vt-display display-6">Réserver votre moment Thalie</h1>
    <p class="lead text-secondary">8 rue des Clercs, 57000 Metz - réponse sous 2 h.</p>
  </div>
</section>"""
    main += block_appointment_form(brand=B_Brand, address=B_ADDRESS, phone=B_PHONE, email=B_EMAIL)
    main += block_cta_band("Annulation gratuite 24 h avant.", "Appeler l'institut", "tel:0387174280")
    main += "</main>"
    return _shell_beaute("contact.html", f"Contact — {B_Brand}", "RDV et accès au Spa Thalie à Metz.", main)


# --- Centre Mosaïque (odontologie) — layout split / bento / entonnoir ---
O_BRAND = "Centre dentaire Mosaïque"
O_PHONE = "03 82 88 45 00"
O_ADDRESS = "42 avenue de la République, 57100 Thionville"
O_MAPS = "https://maps.google.com/?q=42+avenue+de+la+République+57100+Thionville"
O_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "soins.html", "label": "Nos soins"},
    {"file": "equipe.html", "label": "L'équipe"},
    {"file": "contact.html", "label": "Contact"},
]
O_FOOTER_NAV = [
    ("Nos soins", "soins.html"),
    ("L'équipe", "equipe.html"),
    ("Premier RDV offert", "contact.html"),
    ("Urgences", "contact.html"),
]
O_BENTO = [
    {"title": "Prévention", "text": "Détartrage, scellements et bilans annuels pour toute la famille.", "img": "card-1.png", "alt": "Contrôle dentaire", "size": "lg"},
    {"title": "Esthétique", "text": "Facettes et blanchiment professionnel — résultat naturel.", "img": "card-2.png", "alt": "Sourire blanchi", "size": "sm"},
    {"title": "Implants", "text": "Pose guidée par ordinateur, suivi personnalisé.", "img": "card-3.png", "alt": "Implant dentaire", "size": "sm"},
]
O_COMPACT_INDEX = [
    {"title": "Imagerie 3D", "text": "Panoramique et scanner intra-oral pour un diagnostic précis.", "img": "scene-1.png", "alt": "Équipement dentaire numérique"},
    {"title": "Salles de soins", "text": "Fauteuils ergonomiques et musique au casque pour votre confort.", "img": "scene-2.png", "alt": "Salle de soins dentaire moderne"},
    {"title": "Espace enfants", "text": "Coin ludique et protocole douceur pour les plus jeunes.", "img": "scene-3.png", "alt": "Espace enfants au cabinet"},
]
O_COMPACT_SOINS = [
    {"title": "Parcours implant", "text": "De la pose à la couronne en 3 rendez-vous planifiés.", "img": "scene-1.png", "alt": "Pose d'implant"},
    {"title": "Soins enfants", "text": "Pédodontie bienveillante dès 3 ans.", "img": "scene-2.png", "alt": "Dentiste avec enfant"},
    {"title": "Urgences", "text": "Douleur aiguë : appelez avant 11 h, créneaux réservés chaque jour.", "img": "scene-3.png", "alt": "Urgence dentaire"},
]
O_COMPACT_EQUIPE = [
    {"title": "Dr Leroy", "text": "15 ans d'expérience en implantologie et chirurgie guidée.", "img": "scene-1.png", "alt": "Chirurgien-dentiste"},
    {"title": "Dr Ben Saïd", "text": "Spécialiste orthodontie et aligneurs invisibles.", "img": "scene-2.png", "alt": "Orthodontiste"},
    {"title": "Assistantes", "text": "Coordination des RDV et suivi post-opératoire au quotidien.", "img": "scene-3.png", "alt": "Assistantes dentaires"},
]
O_SOINS_SECTIONS = [
    {
        "title": "Prévention & soins courants",
        "items": [
            {"name": "Détartrage", "desc": "Séance complète — remboursé Sécu", "price": "45 €", "tags": ["Sécu"]},
            {"name": "Bilan annuel", "desc": "Examen + radiographie si nécessaire", "price": "28 €", "tags": ["Enfant"]},
            {"name": "Scellement de sillons", "desc": "Prévention caries dès 6 ans", "price": "35 €", "tags": []},
        ],
    },
    {
        "title": "Prothèses & esthétique",
        "items": [
            {"name": "Couronne céramique", "desc": "Devis personnalisé sous 48 h", "price": "sur devis", "tags": ["Devis"]},
            {"name": "Blanchiment professionnel", "desc": "Résultat naturel en une séance", "price": "350 €", "tags": ["Esthétique"]},
            {"name": "Facette céramique", "desc": "Par dent, pose en 2 séances", "price": "sur devis", "tags": []},
        ],
    },
    {
        "title": "Orthodontie & implants",
        "items": [
            {"name": "Aligneurs adulte", "desc": "Orthodontie invisible — bilan offert", "price": "dès 2 800 €", "tags": ["Adulte"]},
            {"name": "Implant unitaire", "desc": "Pose guidée par ordinateur", "price": "sur devis", "tags": ["3 RDV"]},
            {"name": "Urgence douleur", "desc": "Créneau réservé — appelez avant 11 h", "price": "55 €", "tags": ["Urgence"]},
        ],
    },
]


def _shell_odontologie(page: str, title: str, desc: str, main: str) -> str:
    app = block_pill_appbar_m3(
        O_BRAND,
        O_NAV,
        page,
        phone=O_PHONE,
        cta_label="Prendre rendez-vous",
        cta_dialog="rdvDent" if page == "index.html" else "",
        cta_href="contact.html",
        subtitle="Cabinet dentaire",
    )
    foot = _chrome_foot("odontologie", 
        O_BRAND,
        phone=O_PHONE,
        address=O_ADDRESS,
        maps_href=O_MAPS,
        nav_links=O_FOOTER_NAV,
        hours_line="Lun–ven 8h30–19h · Sam 8h–12h",
    )
    mobile = block_mobile_cta("Prendre RDV", "contact.html", O_PHONE)
    if page != "index.html":
        main += block_dialog_m3(
            dialog_id="rdvDent",
            title="Demander un RDV",
            lead="On te rappelle sous 24 h (demo).",
            primary_label="Envoyer",
            primary_href="contact.html",
            fields_html='<div class="mb-2"><label class="form-label small">Motif</label><select class="form-select"><option>Controle</option><option>Douleur</option><option>Devis</option></select></div><div class="mb-2"><label class="form-label small">Telephone</label><input class="form-control" type="tel"></div>',
        )
    return wrap_page_medical(title, desc, app + main + foot + mobile, slug="odontologie", page=page, site_name=O_BRAND, nav=O_NAV)


def build_odontologie_index() -> str:
    main = "<main>"
    main += block_health_booking_hero_m3(
        "Ton dentiste a Thionville, sans stress",
        "Quatre praticiens, explications claires et un agenda simple - tu choisis ton creneau, on confirme.",
        badge="Soins doux & personnalises",
        primary_label="Voir plus de disponibilites",
        dialog="rdvDent",
        inset_img="scene-1.png",
        inset_alt="Salle de soins moderne",
        status="Consultations sur rendez-vous",
        times=["09:00", "11:00", "14:30"],
    )
    main += block_health_stats_m3(
        [
            {"icon": "👥", "value": "1 200+", "label": "Patients accompagnes"},
            {"icon": "★", "value": "5/5", "label": "Avis Google"},
            {"icon": "📅", "value": "8 ans", "label": "D'experience a Thionville"},
            {"icon": "📍", "value": "Centre", "label": "Cabinet facilement accessible"},
        ]
    )
    main += """<section class="vt-reveal py-5 vt-odonto-urgency">
  <div class="container">
    <div class="row g-4 align-items-center">
      <div class="col-lg-7">
        <p class="vt-eyebrow text-uppercase">Urgences</p>
        <h2 class="vt-section-title h3">Douleur ce matin ?</h2>
        <p class="text-secondary mb-3">Creneaux d'urgence avant 11 h. Appele - on priorise, sans jargon.</p>
        <div class="d-flex flex-wrap gap-2">
          <a class="btn btn-vt-primary" href="tel:0382884500">Appeler le 03 82 88 45 00</a>
          <button type="button" class="btn btn-vt-outline" data-vt-dialog-open="rdvDent">Demander un RDV</button>
        </div>
      </div>
      <div class="col-lg-5">
        <article class="vt-care-card">
          <h3 class="h6">Premier RDV decouverte</h3>
          <p class="small text-secondary mb-0">Offert. Devis avant chaque acte - tu sais ou tu mets les pieds.</p>
        </article>
      </div>
    </div>
  </div>
</section>"""
    main += block_dialog_m3(
        dialog_id="rdvDent",
        title="Demander un RDV",
        lead="Motif + telephone - on te rappelle sous 24 h (demo).",
        primary_label="Envoyer",
        primary_href="contact.html",
        fields_html='<div class="mb-2"><label class="form-label small">Motif</label><select class="form-select"><option>Controle</option><option>Douleur</option><option>Devis</option><option>Enfant</option></select></div><div class="mb-2"><label class="form-label small">Creneau souhaite</label><select class="form-select"><option>09:00</option><option>11:00</option><option>14:30</option><option>Autre</option></select></div><div class="mb-2"><label class="form-label small">Telephone</label><input class="form-control" type="tel" placeholder="06 ..."></div>',
    )
    main += block_snackbar_m3("Demande RDV enregistree (demo)")
    main += block_fab_menu_m3([
        {"label": "RDV", "dialog": "rdvDent"},
        {"label": "Soins", "href": "soins.html"},
        {"label": "Urgence", "href": "tel:0382884500"},
    ], main_label="Actions cabinet")
    main += "</main>"
    return _shell_odontologie(
        "index.html",
        f"{O_BRAND} — Thionville",
        "Cabinet dentaire à Thionville : soins, prévention et orthodontie pour enfants et adultes.",
        main,
    )


def build_odontologie_soins() -> str:
    main = "<main>"
    main += block_hero_split(
        "Des soins adaptés à chaque âge",
        "Tarifs affichés en salle d'attente et tiers payant accepté.",
        "hero.png",
        "Instruments dentaires stériles",
        eyebrow="Nos soins",
        primary_href="contact.html",
        primary_label="Demander un devis",
        secondary_href="index.html",
        secondary_label="Retour accueil",
    )
    main += block_menu_section(
        "Actes courants",
        "Prix indicatifs TTC. Grille complète affichée en salle d'attente et envoyée avec chaque devis.",
        O_SOINS_SECTIONS,
    )
    main += block_compact_features(O_COMPACT_SOINS)
    main += block_cta_band("Question sur un devis ? Demandez un rappel.", "Être rappelé", "contact.html")
    main += "</main>"
    return _shell_odontologie(
        "soins.html",
        f"Nos soins — {O_BRAND}",
        "Soins conservateurs, prothèses et orthodontie à Thionville.",
        main,
    )


def build_odontologie_equipe() -> str:
    main = "<main>"
    main += block_hero_split(
        "Quatre praticiens, une même exigence",
        "Formation continue et congrès européens — écoute, pédagogie et douceur.",
        "hero.png",
        "Équipe dentaire en blouse",
        eyebrow="L'équipe",
        primary_href="contact.html",
        primary_label="Prendre RDV",
        secondary_href="soins.html",
        secondary_label="Nos soins",
    )
    main += block_story(
        "Nos valeurs",
        [
            "Ouvert en 2018 avenue de la République, Mosaïque accueille familles et seniors avec des créneaux le samedi matin.",
            "Nous expliquons chaque geste avant de commencer — votre confiance est notre priorité.",
        ],
    )
    main += block_compact_features(O_COMPACT_EQUIPE)
    main += block_trust(
        "Visite du plateau technique sur demande lors du premier RDV.",
        ["Implantologie", "Orthodontie", "Pédodontie", "Formation continue"],
    )
    main += block_cta_band("Rejoignez une équipe en croissance.", "Candidater", "contact.html")
    main += "</main>"
    return _shell_odontologie(
        "equipe.html",
        f"L'équipe — {O_BRAND}",
        "Chirurgiens-dentistes et assistantes à Thionville.",
        main,
    )


def build_odontologie_contact() -> str:
    main = """<main>
<section class="vt-hero-compact py-5 text-center">
  <div class="container">
    <p class="vt-eyebrow text-uppercase">Contact</p>
    <h1 class="vt-display display-6">Prendre rendez-vous</h1>
    <p class="lead text-secondary">42 avenue de la République, 57100 Thionville — réponse sous 2 h.</p>
  </div>
</section>"""
    main += block_dental_appointment_form(brand=O_BRAND, address=O_ADDRESS, phone=O_PHONE)
    main += block_cta_band("Urgence : 03 82 88 45 00 avant 11 h.", "Appeler le cabinet", "tel:0382884500")
    main += "</main>"
    return _shell_odontologie(
        "contact.html",
        f"Contact — {O_BRAND}",
        "RDV et urgences dentaires à Thionville.",
        main,
    )


# --- Garage Central (automobile) — layout M3 maquette (_maquettes-echantillons/images/automobile-m3.png) ---
A_BRAND = "Garage Central"
A_BRAND_FULL = "Garage Central Plappeville"
A_PHONE = "03 87 65 43 21"
A_ADDRESS = "Zone artisanale des Gravières, 57050 Plappeville"
A_MAPS = "https://maps.google.com/?q=Zone+artisanale+des+Gravières+57050+Plappeville"
A_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "services.html", "label": "Services"},
    {"file": "atelier.html", "label": "À propos"},
    {"file": "atelier.html#avis", "label": "Avis"},
    {"file": "contact.html", "label": "Contact"},
]
A_FOOTER_NAV = [
    ("Services", "services.html"),
    ("L'atelier", "atelier.html"),
    ("Prendre RDV", "contact.html"),
    ("Devis assurance", "contact.html"),
]
A_SERVICE_CARDS_M3 = [
    {
        "icon": "🔧",
        "title": "Entretien",
        "text": "Vidange, freins, révisions constructeur - devis avant intervention.",
        "href": "services.html",
    },
    {
        "icon": "🛞",
        "title": "Pneus",
        "text": "Montage, équilibrage, géométrie - été comme hiver.",
        "href": "services.html",
    },
    {
        "icon": "🎨",
        "title": "Carrosserie",
        "text": "Devis assurance 24 h, cabine peinture, débosselage.",
        "href": "services.html",
    },
]
A_CARDS = [
    {"title": "Entretien", "text": "Révisions constructeur respectées.", "img": "card-1.png", "alt": "Révision automobile"},
    {"title": "Pneumatiques", "text": "Été, hiver, toutes marques.", "img": "card-2.png", "alt": "Montage de pneus"},
    {"title": "Carrosserie", "text": "Devis assurance en 24 h.", "img": "card-3.png", "alt": "Réparation carrosserie"},
]
A_CHAPTERS_INDEX = [
    {"title": "Le pont élévateur", "text": "Diagnostic rapide et transparence sur les pièces à changer.", "img": "scene-1.png", "alt": "Pont élévateur en atelier"},
    {"title": "La carrosserie", "text": "Peinture cabine et débosselage sans peinture.", "img": "scene-2.png", "alt": "Atelier carrosserie"},
    {"title": "Le parc pneus", "text": "Montage, équilibrage et géométrie - toutes dimensions.", "img": "scene-3.png", "alt": "Stock de pneus en garage"},
]
A_COMPACT_SERVICES = [
    {"title": "Freinage", "text": "Disques, plaquettes et liquide de frein.", "img": "scene-1.png", "alt": "Freins automobile"},
    {"title": "Échappement", "text": "Ligne complète et catalyseur.", "img": "scene-2.png", "alt": "Échappement"},
    {"title": "Hybride", "text": "Formation Bosch pour les véhicules rechargeables.", "img": "scene-3.png", "alt": "Véhicule hybride en atelier"},
]
A_COMPACT_ATELIER = [
    {"title": "Accueil", "text": "Café et wifi en salle d'attente.", "img": "scene-1.png", "alt": "Accueil garage"},
    {"title": "Outillage", "text": "Clés dynamométriques et documentation constructeur.", "img": "scene-2.png", "alt": "Outillage professionnel"},
    {"title": "Propreté", "text": "Véhicule rendu lavé intérieur/extérieur.", "img": "scene-3.png", "alt": "Lavage véhicule"},
]
A_SERVICES_MENU = [
    {
        "title": "Entretien courant",
        "items": [
            {"name": "Vidange + filtres", "desc": "Huile premium et filtre à huile", "price": "89 €", "tags": ["1 h"]},
            {"name": "Révision complète", "desc": "Selon carnet constructeur", "price": "dès 149 €", "tags": ["Multimarque"]},
            {"name": "Contrôle anti-pollution", "desc": "Créneaux sans attente", "price": "45 €", "tags": []},
        ],
    },
    {
        "title": "Mécanique",
        "items": [
            {"name": "Kit distribution", "desc": "Courroie + pompe à eau", "price": "sur devis", "tags": ["Garantie 2 ans"]},
            {"name": "Freinage complet", "desc": "Disques et plaquettes AV/AR", "price": "dès 220 €", "tags": []},
            {"name": "Embrayage", "desc": "Kit + main-d'œuvre", "price": "sur devis", "tags": []},
        ],
    },
    {
        "title": "Pneus & confort",
        "items": [
            {"name": "Montage 4 pneus", "desc": "Équilibrage inclus", "price": "60 €", "tags": ["Toutes marques"]},
            {"name": "Géométrie", "desc": "Parallélisme train avant", "price": "75 €", "tags": []},
            {"name": "Climatisation", "desc": "Recharge gaz + désinfection", "price": "95 €", "tags": []},
        ],
    },
]


def _shell_automobile(page: str, title: str, desc: str, main: str) -> str:
    nav = block_garage_m3_nav(
        A_BRAND_FULL,
        A_NAV,
        page,
        cta_label="Prendre RDV",
        cta_href="contact.html",
    )
    foot = _chrome_foot(
        "automobile",
        A_BRAND_FULL,
        phone=A_PHONE,
        address=A_ADDRESS,
        maps_href=A_MAPS,
        nav_links=A_FOOTER_NAV,
        hours_line="Lun–ven 8h–18h · Sam 8h–12h",
    )
    fab = block_phone_fab(A_PHONE, "Appeler le garage")
    mobile = block_mobile_cta("Prendre RDV", "contact.html", A_PHONE)
    return wrap_page_garage(
        title,
        desc,
        nav + main + foot + fab + mobile,
        slug="automobile",
        page=page,
        site_name=A_BRAND_FULL,
        nav=A_NAV,
        layout="garage-m3",
    )


def build_automobile_index() -> str:
    main = '<main itemscope itemtype="https://schema.org/WebPage">'
    main += block_garage_m3_hero(
        "Votre garage de confiance",
        "Entretien, pneus, carrosserie et plus encore : un service complet pour votre véhicule, toute l'année.",
        "hero.png",
        "Façade et atelier Garage Central Plappeville",
        location="Plappeville, à 10 min de Metz",
        primary_href="services.html",
        primary_label="Découvrir nos services",
        service_cards=A_SERVICE_CARDS_M3,
    )
    main += block_garage_m3_stats(
        [
            {"icon": "🛡", "value": "25+", "label": "Années d'expérience"},
            {"icon": "👥", "value": "1200+", "label": "Clients satisfaits"},
            {"icon": "★", "value": "4,8/5", "label": "Avis Google"},
            {"icon": "⏱", "value": "48 h", "label": "Délai moyen de RDV"},
        ]
    )
    main += block_garage_m3_local(
        "Un garage local, un service de proximité",
        "Devis clair avant chaque intervention, pièces de qualité et conseils sans blabla - entre Metz et Woippy depuis 1972.",
        ["Devis clairs et gratuits", "Pièces de qualité", "Conseils personnalisés"],
        href="contact.html",
        cta="Prendre RDV",
    )
    main += """<section class="vt-reveal py-5 vt-garage-timeline">
  <div class="container">
    <p class="vt-eyebrow text-uppercase">Suivi SMS</p>
    <h2 class="vt-section-title h3 mb-4">Tu sais ou en est la voiture</h2>
    <ol class="vt-timeline list-unstyled mb-0">
      <li><strong>Message</strong> - photo ou bruit, on te dit si c'est urgent</li>
      <li><strong>Devis</strong> - rien ne part sans ton OK</li>
      <li><strong>Atelier</strong> - SMS a chaque etape</li>
      <li><strong>Cles</strong> - voiture lavee, garantie affichee</li>
    </ol>
    <div class="mt-4">
      <button type="button" class="btn btn-vt-primary" data-vt-dialog-open="devisDialog">Envoyer une photo pour devis</button>
    </div>
  </div>
</section>"""
    main += block_dialog_m3(
        dialog_id="devisDialog",
        title="Devis par photo",
        lead="Decris le probleme - on te repond sous 2 h (demo).",
        primary_label="Envoyer",
        primary_href="contact.html",
        fields_html='<div class="mb-2"><label class="form-label small">Description</label><textarea class="form-control" rows="3" placeholder="Voyant moteur, bruit frein..."></textarea></div><div class="mb-2"><label class="form-label small">Telephone</label><input class="form-control" type="tel"></div>',
    )
    main += block_snackbar_m3("Devis demande (demo)")
    main += block_fab_menu_m3([
        {"label": "Devis photo", "dialog": "devisDialog"},
        {"label": "Services", "href": "services.html"},
        {"label": "Appeler", "href": "tel:0387654321"},
    ], main_label="Actions garage")
    main += block_sticky_cta_m3("Besoin d'un creneau ?", "Devis", "contact.html", dialog="devisDialog")
    main += "</main>"
    return _shell_automobile(
        "index.html",
        f"{A_BRAND_FULL} — Mécanique & carrosserie",
        "Garage auto à Plappeville : entretien, pneus, carrosserie - à 10 min de Metz.",
        main,
    )


def build_automobile_services() -> str:
    main = "<main>"
    main += block_garage_m3_hero(
        "Tout pour rouler serein",
        "De la vidange à la distribution, expertise multimarque à Plappeville.",
        "hero.png",
        "Mécanicien au travail",
        location="Services atelier",
        primary_href="contact.html",
        primary_label="Demander un devis",
        service_cards=A_SERVICE_CARDS_M3,
    )
    main += block_menu_section(
        "Tarifs indicatifs",
        "Devis gratuit en atelier ou par photo. Prix TTC main-d'œuvre incluse sauf mention.",
        A_SERVICES_MENU,
    )
    main += block_compact_features(A_COMPACT_SERVICES)
    main += block_cta_band("Devis gratuit en atelier ou par photo.", "Demander un devis", "contact.html")
    main += "</main>"
    return _shell_automobile(
        "services.html",
        f"Services — {A_BRAND_FULL}",
        "Mécanique, pneus, climatisation et diagnostic à Plappeville.",
        main,
    )


def build_automobile_atelier() -> str:
    main = '<main id="avis">'
    main += block_garage_m3_hero(
        "900 m² dédiés à votre véhicule",
        "Ponts, cabine peinture et espace diagnostic - une équipe de quartier qui connaît les routes messines.",
        "hero.png",
        "Vue d'ensemble de l'atelier",
        location="L'atelier · Plappeville",
        primary_href="contact.html",
        primary_label="Planifier une visite",
        service_cards=A_SERVICE_CARDS_M3[:2]
        + [
            {
                "icon": "★",
                "title": "Avis clients",
                "text": "4,8/5 sur Google - devis clair et voiture rendue propre.",
                "href": "#avis",
            }
        ],
    )
    main += block_story(
        "L'équipe",
        ["Six mécaniciens, deux carrossiers et une coordinatrice accueil - tous formés aux normes constructeur."],
    )
    main += block_compact_features(A_COMPACT_ATELIER)
    main += block_chapters(A_CHAPTERS_INDEX)
    main += block_cta_band("Visite de l'atelier sur rendez-vous.", "Planifier une visite", "contact.html")
    main += "</main>"
    return _shell_automobile(
        "atelier.html",
        f"À propos — {A_BRAND_FULL}",
        "Équipe, outils et méthode de travail à Plappeville.",
        main,
    )


def build_automobile_contact() -> str:
    main = """<main>
<section class="vt-g-hero pt-5 pb-3">
  <div class="container">
    <p class="vt-g-pin mb-2"><span aria-hidden="true">📍</span> Plappeville</p>
    <h1 class="vt-display display-6">Nous contacter</h1>
    <p class="lead text-secondary">Zone artisanale des Gravières, 57050 Plappeville.</p>
  </div>
</section>"""
    main += block_garage_appointment_form(brand=A_BRAND_FULL, address=A_ADDRESS, phone=A_PHONE)
    main += block_cta_band("Panne sur autoroute ? Dépannage 24h/24.", "Appeler le dépannage", "tel:0387654321")
    main += "</main>"
    return _shell_automobile(
        "contact.html",
        f"Contact — {A_BRAND_FULL}",
        "RDV atelier à Plappeville.",
        main,
    )


# --- Halles Thionville (commerce) — éditorial + promos + entonnoir drive ---
C_BRAND = "Halles Thionville"
C_PHONE = "03 82 53 40 00"
C_EMAIL = "service@halles-thionville.fr"
C_ADDRESS = "Rue du Mail, 57100 Thionville"
C_MAPS = "https://maps.google.com/?q=Rue+du+Mail+57100+Thionville"
C_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "rayons.html", "label": "Rayons"},
    {"file": "drive.html", "label": "Drive"},
    {"file": "contact.html", "label": "Contact"},
]
C_FOOTER_NAV = [
    ("Rayons", "rayons.html"),
    ("Drive", "drive.html"),
    ("Carte Halles+", "contact.html"),
    ("Promos", "rayons.html"),
]
C_CARDS = [
    {"title": "Click & collect", "text": "Commande en ligne, retrait en 2 h.", "img": "card-1.png", "alt": "Retrait drive"},
    {"title": "Carte fidélité", "text": "1 € dépensé = 1 point, avantages exclusifs.", "img": "card-2.png", "alt": "Carte de fidélité"},
    {"title": "Livraison", "text": "Sur Thionville et Yutz en soirée.", "img": "card-3.png", "alt": "Livraison à domicile"},
]
C_CHAPTERS_INDEX = [
    {"title": "Boucherie", "text": "Viandes label rouge et préparations maison.", "img": "scene-1.png", "alt": "Boucherie artisanale"},
    {"title": "Boulangerie", "text": "Four sur place dès 7 h.", "img": "scene-2.png", "alt": "Pain frais en rayon"},
    {"title": "Fruits & légumes", "text": "Arrivages quotidiens de Serémange et Corny.", "img": "scene-3.png", "alt": "Rayon fruits et légumes"},
]
C_COMPACT_RAYONS = [
    {"title": "Poissonnerie", "text": "Arrivages mer du Nord 3 fois par semaine.", "img": "scene-1.png", "alt": "Poissonnerie"},
    {"title": "Cave", "text": "Vins mosellans et conseils sommelier.", "img": "scene-2.png", "alt": "Cave à vins"},
    {"title": "Surgelés", "text": "Gamme premium et surgelés maison.", "img": "scene-3.png", "alt": "Surgelés"},
]
C_BENTO_DRIVE = [
    {"title": "Emplacements couverts", "text": "15 places — été comme hiver.", "img": "gallery-1.png", "alt": "Abris couverts", "size": "lg"},
    {"title": "Suivi commande", "text": "Application et SMS à l'approche.", "img": "gallery-2.png", "alt": "Suivi en temps réel", "size": "sm"},
    {"title": "Fraîcheur garantie", "text": "Préparateurs formés aux produits frais.", "img": "scene-1.png", "alt": "Préparation commande", "size": "sm"},
]
C_RAYONS_MENU = [
    {
        "title": "Frais du jour",
        "items": [
            {"name": "Boucherie label rouge", "desc": "Préparations maison", "price": "dès 8 €", "tags": ["Local"]},
            {"name": "Poissonnerie", "desc": "Arrivages mer du Nord", "price": "dès 6 €", "tags": ["Mer"]},
            {"name": "Traiteur & sushi", "desc": "Préparé sur place", "price": "dès 5 €", "tags": ["Jour"]},
        ],
    },
    {
        "title": "Épicerie & bio",
        "items": [
            {"name": "Marques mosellanes", "desc": "200 refs origine locale", "price": "var.", "tags": ["Moselle"]},
            {"name": "Sans gluten", "desc": "Aisle dédiée", "price": "var.", "tags": []},
            {"name": "Vrac bio", "desc": "Céréales et cosmétiques", "price": "au poids", "tags": ["Bio"]},
        ],
    },
    {
        "title": "Promos semaine",
        "items": [
            {"name": "Fruits de saison", "desc": "Producteurs Serémange", "price": "−20 %", "tags": ["Promo"]},
            {"name": "Fromages AOP", "desc": "Sélection fromager", "price": "−15 %", "tags": []},
            {"name": "Vins mosellans", "desc": "Cave conseillée", "price": "dès 7 €", "tags": ["Moselle"]},
        ],
    },
]


def _shell_commerce(page: str, title: str, desc: str, main: str) -> str:
    rail = block_nav_rail_m3(
        C_BRAND,
        C_NAV,
        page,
        hours="Lun-sam 8h-20h · Dim 9h-12h30",
        address=C_ADDRESS,
        phone=C_PHONE,
        tagline="Thionville · frais & drive",
    )
    top = block_rail_topbar_m3(
        search_placeholder="Chercher un produit",
        cta_label="Drive 2 h",
        cta_dialog="driveDialog" if page == "index.html" else "",
        cta_href="drive.html",
    )
    foot = _chrome_foot("commerce", 
        C_BRAND,
        phone=C_PHONE,
        address=C_ADDRESS,
        email=C_EMAIL,
        maps_href=C_MAPS,
        nav_links=C_FOOTER_NAV,
        hours_line="Lun–sam 8h–20h · Dim 9h–12h30",
    )
    mobile = block_mobile_cta("Drive 2 h", "drive.html", C_PHONE)
    if page != "index.html":
        main += block_dialog_m3(
            dialog_id="driveDialog",
            title="Drive en 2 h",
            lead="Creneau de retrait - frais offerts 1ere commande (demo).",
            primary_label="Continuer",
            primary_href="drive.html",
            fields_html='<div class="mb-2"><label class="form-label small">Creneau</label><select class="form-select"><option>Aujourd\'hui 17h-18h</option><option>Aujourd\'hui 18h-19h</option></select></div>',
        )
        main += block_fab_menu_m3(
            [
                {"label": "Drive", "dialog": "driveDialog"},
                {"label": "Rayons", "href": "rayons.html"},
                {"label": "Halles+", "href": "contact.html"},
            ],
            main_label="Actions halles",
        )
    body = f'<div class="vt-rail-shell">{rail}<div class="vt-rail-main">{top}{main}{foot}{mobile}</div></div>'
    return wrap_page_retail(title, desc, body, slug="commerce", page=page, site_name=C_BRAND, nav=C_NAV)


def build_commerce_index() -> str:
    main = "<main>"
    main += block_marquee_m3([
        "Livraison locale offerte des 35 euro",
        "Drive en 2 h",
        "Producteurs mosellans",
        "Halles+ : 1 euro = 1 point",
    ])
    main += """<section class="vt-retail-hero vt-retail-hero--bleed vt-reveal">
  <div class="vt-retail-hero-bg" aria-hidden="true">
    <picture><source srcset="images/scene-1.webp" type="image/webp"><img src="images/scene-1.png" alt="" decoding="async" fetchpriority="high"></picture>
  </div>
  <div class="container vt-retail-hero-copy">
    <p class="vt-eyebrow text-uppercase mb-2">Thionville · Halles</p>
    <h1 class="vt-display display-4 mb-2">Le marche du quotidien, version moderne</h1>
    <p class="lead mb-4">3200 m2, boucherie artisanale, drive en 2 h chrono - sans l'usine a caddies.</p>
    <div class="d-flex flex-wrap gap-2 mb-2">
      <button type="button" class="btn btn-vt-primary btn-lg" data-vt-dialog-open="driveDialog">Commander en drive</button>
      <a class="btn btn-vt-outline btn-lg" href="rayons.html">Voir les rayons</a>
    </div>
  </div>
</section>"""
    main += block_menu_h_cards_m3(
        [
            {"title": "Fraicheur du jour", "text": "Fruits et legumes locaux", "price": "Promo", "img": "scene-1.png", "alt": "Rayon frais"},
            {"title": "Boucherie", "text": "Decoupe a la demande", "price": "Sur place", "img": "scene-2.png", "alt": "Boucherie", "featured": True},
            {"title": "Fromages", "text": "Affineurs du coin", "price": "A la coupe", "img": "card-1.png", "alt": "Fromage"},
            {"title": "Drive 2 h", "text": "Retrait parking", "price": "Gratuit*", "img": "scene-3.png", "alt": "Drive"},
        ],
        kicker="Cette semaine",
        title="Ce qui sort des Halles",
        chips=[
            {"label": "Tous", "active": True},
            {"label": "Frais"},
            {"label": "Promos"},
            {"label": "Local"},
            {"label": "Drive"},
        ],
    )
    main += """<section class="vt-reveal py-5">
  <div class="container">
    <div class="row g-3">
      <div class="col-md-4"><article class="vt-gold-card h-100"><h3 class="h6">Drive express</h3><p class="small mb-3">Commande en ligne, retrait en 2 h - frais offerts 1ere fois.</p><button type="button" class="btn btn-sm btn-vt-primary" data-vt-dialog-open="driveDialog">Lancer</button></article></div>
      <div class="col-md-4"><article class="vt-gold-card h-100"><h3 class="h6">Halles+</h3><p class="small mb-3">1 euro = 1 point. Promos reservees, cafe offert de temps en temps.</p><button type="button" class="btn btn-sm btn-vt-outline" data-vt-dialog-open="fidelityDialog">Creer ma carte</button></article></div>
      <div class="col-md-4"><article class="vt-gold-card h-100"><h3 class="h6">Producteurs</h3><p class="small mb-3">40 fournisseurs mosellans - degustation le samedi.</p><a class="btn btn-sm btn-vt-outline" href="rayons.html">Voir</a></article></div>
    </div>
  </div>
</section>"""
    main += block_dialog_m3(
        dialog_id="driveDialog",
        title="Drive en 2 h",
        lead="Creneau de retrait - frais offerts 1ere commande (demo).",
        primary_label="Continuer",
        primary_href="drive.html",
        fields_html='<div class="mb-2"><label class="form-label small">Creneau</label><select class="form-select"><option>Aujourd\'hui 17h-18h</option><option>Aujourd\'hui 18h-19h</option><option>Demain 10h-11h</option></select></div><div class="mb-2"><label class="form-label small">Telephone</label><input class="form-control" type="tel" placeholder="06 ..."></div>',
    )
    main += block_dialog_m3(
        dialog_id="fidelityDialog",
        title="Carte Halles+",
        lead="1 euro = 1 point. Avantages et promos reservees (demo).",
        primary_label="Creer ma carte",
        primary_href="contact.html",
        fields_html='<div class="mb-2"><label class="form-label small">Prenom</label><input class="form-control"></div><div class="mb-2"><label class="form-label small">Email</label><input class="form-control" type="email"></div>',
    )
    main += block_snackbar_m3("Ajoute au panier (demo)")
    main += block_fab_menu_m3([
        {"label": "Drive", "dialog": "driveDialog"},
        {"label": "Halles+", "dialog": "fidelityDialog"},
        {"label": "Rayons", "href": "rayons.html"},
    ], main_label="Actions halles")
    main += "</main>"
    return _shell_commerce(
        "index.html",
        f"{C_BRAND} — Commerce & drive",
        "Supermarché de proximité à Thionville : frais, drive et programme fidélité.",
        main,
    )


def build_commerce_rayons() -> str:
    main = "<main>"
    main += block_hero_split(
        "Des rayons qui respirent la fraîcheur",
        "Produits locaux mis en avant chaque semaine.",
        "hero.png",
        "Rayon épicerie fine",
        eyebrow="Nos rayons",
        primary_href="drive.html",
        primary_label="Commander",
        secondary_href="index.html",
        secondary_label="Accueil",
    )
    main += block_menu_section(
        "Sélection & promos",
        "Étiquetage origine Moselle sur 200 références permanentes. Catalogue promo hebdomadaire en ligne.",
        C_RAYONS_MENU,
    )
    main += block_cards_bs("Univers", [
        {"title": "Frais", "text": "Crèmerie, traiteur et sushi du jour.", "img": "card-1.png", "alt": "Rayon frais"},
        {"title": "Épicerie", "text": "Marques régionales et sans gluten.", "img": "card-2.png", "alt": "Étagères épicerie"},
        {"title": "Bio & vrac", "text": "Cosmétiques et céréales en vrac.", "img": "card-3.png", "alt": "Rayon vrac bio"},
    ])
    main += block_compact_features(C_COMPACT_RAYONS)
    main += block_cta_band("Catalogue promo hebdomadaire en ligne.", "Voir les promos", "contact.html")
    main += "</main>"
    return _shell_commerce(
        "rayons.html",
        f"Rayons — {C_BRAND}",
        "Boucherie, poissonnerie, épicerie et bio à Thionville.",
        main,
    )


def build_commerce_drive() -> str:
    main = "<main>"
    main += block_hero_rich(
        "Faites vos courses sans sortir de voiture",
        "15 emplacements couverts, prêt en 2 h.",
        "hero.png",
        "Point drive couvert",
        eyebrow="Click & collect",
        primary_href="contact.html",
        primary_label="Commander",
        secondary_href="rayons.html",
        secondary_label="Voir les rayons",
    )
    main += block_funnel_steps("Comment ça marche", [
        ("Commandez en ligne", "Sur halles-thionville.fr — choisissez vos produits et votre créneau."),
        ("Nous préparons", "Préparateurs formés à la fraîcheur — substitution si produit indisponible."),
        ("Retrait express", "Chargez votre coffre — paiement en ligne ou à la borne."),
    ])
    main += block_bento_cards(C_BENTO_DRIVE)
    main += block_story(
        "Simple et rapide",
        ["Commandez sur halles-thionville.fr, choisissez votre créneau, nous préparons et chargeons votre coffre."],
    )
    main += block_trust(
        "Première commande : frais de préparation offerts.",
        ["2 h chrono", "15 emplacements", "Paiement flexible", "Fraîcheur garantie"],
    )
    main += block_cta_band("Première commande : frais de préparation offerts.", "Commander", "contact.html")
    main += "</main>"
    return _shell_commerce(
        "drive.html",
        f"Drive — {C_BRAND}",
        "Click & collect et retrait express à Thionville.",
        main,
    )


def build_commerce_contact() -> str:
    main = """<main>
<section class="vt-hero-compact py-5 text-center">
  <div class="container">
    <p class="vt-eyebrow text-uppercase">Contact</p>
    <h1 class="vt-display display-6">Une question ? On vous répond</h1>
    <p class="lead text-secondary">Rue du Mail, 57100 Thionville.</p>
  </div>
</section>"""
    main += block_retail_contact_form(brand=C_BRAND, address=C_ADDRESS, phone=C_PHONE, email=C_EMAIL)
    main += block_cta_band("Réclamation ou suggestion : formulaire dédié.", "Nous écrire", "contact.html")
    main += "</main>"
    return _shell_commerce(
        "contact.html",
        f"Contact — {C_BRAND}",
        "Horaires, accès et service client.",
        main,
    )


# --- Verlaine & Associés (comptable) — preuve sociale + tableau + FAQ ---
CP_BRAND = "Verlaine & Associés"
CP_PHONE = "03 87 75 90 12"
CP_EMAIL = "contact@verlaine-associes.fr"
CP_ADDRESS = "14 rue Serpenoise, 57000 Metz"
CP_MAPS = "https://maps.google.com/?q=14+rue+Serpenoise+57000+Metz"
CP_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "expertises.html", "label": "Expertises"},
    {"file": "methode.html", "label": "Notre méthode"},
    {"file": "contact.html", "label": "Contact"},
]
CP_FOOTER_NAV = [
    ("Expertises", "expertises.html"),
    ("Notre méthode", "methode.html"),
    ("Consultation", "contact.html"),
    ("Bilan flash", "contact.html"),
]
CP_CARDS = [
    {"title": "Tenue comptable", "text": "Liasse fiscale, TVA et tableaux de bord mensuels.", "img": "card-1.png", "alt": "Tenue comptable"},
    {"title": "Paie & social", "text": "Bulletins, DSN et veille conventionnelle.", "img": "card-2.png", "alt": "Paie et DSN"},
    {"title": "Conseil dirigeant", "text": "Pilotage, restructuration et transmission.", "img": "card-3.png", "alt": "Conseil dirigeant"},
]
CP_STAT_NARRATIVE = [
    {"stat": "48 h", "stat_label": "Bilan flash", "title": "Tenue & fiscalité", "text": "Liasse, TVA et reporting mensuel — vous savez où vous en êtes.", "img": "scene-1.png", "alt": "Expertises comptables"},
    {"stat": "100 %", "stat_label": "DSN conforme", "title": "Paie & social", "text": "Bulletins, déclarations et veille conventionnelle pour vos équipes.", "img": "scene-2.png", "alt": "Équipe paie"},
    {"stat": "1", "stat_label": "Interlocuteur dédié", "title": "Conseil dirigeant", "text": "Pilotage, restructuration et transmission — décisions éclairées.", "img": "scene-3.png", "alt": "Conseil PME"},
]
CP_EXPERTISES_MENU = [
    {
        "title": "Tenue & obligations",
        "items": [
            {"name": "Tenue comptable annuelle", "desc": "Saisie, liasse fiscale, TVA", "price": "dès 180 €/mois", "tags": ["PME"]},
            {"name": "Bilan flash", "desc": "Situation intermédiaire sous 48 h", "price": "290 €", "tags": ["Express"]},
            {"name": "Création d'entreprise", "desc": "Statuts, immatriculation, premiers pas", "price": "sur devis", "tags": []},
        ],
    },
    {
        "title": "Paie & social",
        "items": [
            {"name": "Paie mensuelle", "desc": "Par bulletin — DSN incluse", "price": "dès 35 €", "tags": ["/ salarié"]},
            {"name": "Audit social", "desc": "Conformité et optimisation charges", "price": "sur devis", "tags": []},
            {"name": "Formation dirigeant", "desc": "Obligations employeur en 2 h", "price": "190 €", "tags": []},
        ],
    },
    {
        "title": "Conseil & pilotage",
        "items": [
            {"name": "Tableau de bord", "desc": "KPI mensuels personnalisés", "price": "inclus premium", "tags": []},
            {"name": "Transmission", "desc": "Cession, reprise, évaluation", "price": "sur devis", "tags": ["Dirigeant"]},
            {"name": "Accompagnement levée", "desc": "Business plan et dossiers financeurs", "price": "sur devis", "tags": []},
        ],
    },
]
CP_FAQ = [
    ("Quels documents pour un premier rendez-vous ?", "Derniers bilans, KBIS, statuts et liste des échéances fiscales en cours. Nous complétons ensemble si besoin."),
    ("Combien coûte une tenue comptable ?", "À partir de 180 €/mois pour une TPE sans salarié. Devis personnalisé après diagnostic gratuit."),
    ("Pouvez-vous reprendre un dossier en cours d'année ?", "Oui — reprise sous 15 jours ouvrés avec inventaire des pièces manquantes."),
    ("Intervenez-vous à Thionville ?", "Oui — permanence hebdomadaire et RDV visio pour les clients du bassin thionvillois."),
    ("Le bilan flash, c'est quoi ?", "Un état de situation intermédiaire livré sous 48 h pour une décision urgente (investissement, crédit, cession)."),
]


def _shell_comptable(page: str, title: str, desc: str, main: str) -> str:
    bar = block_info_bar(status="Cabinet ouvert · Lun–ven 9h–18h", address=CP_ADDRESS, phone=CP_PHONE, maps_href=CP_MAPS)
    nav = _chrome_nav("comptable", CP_BRAND, CP_NAV, page, cta_label="Prendre RDV", cta_href="contact.html")
    foot = _chrome_foot("comptable", 
        CP_BRAND,
        phone=CP_PHONE,
        address=CP_ADDRESS,
        email=CP_EMAIL,
        maps_href=CP_MAPS,
        nav_links=CP_FOOTER_NAV,
        hours_line="Lun–ven 9h–18h · Metz & Thionville",
    )
    mobile = block_mobile_cta("Prendre RDV", "contact.html", CP_PHONE)
    return wrap_page_cabinet(title, desc, bar + nav + main + foot + mobile, slug="comptable", page=page, site_name=CP_BRAND, nav=CP_NAV)


def build_comptable_index() -> str:
    main = "<main>"
    main += block_hero_proof_split(
        "Vos chiffres, expliqués sans jargon",
        "Tenue comptable, paie et conseil dirigeant pour PME de Metz et Thionville.",
        eyebrow="Metz & Thionville · Expert-comptable",
        quote="Un cabinet réactif qui parle vrai — nos décisions sont éclairées, nos échéances toujours tenues.",
        quote_author="Philippe R.",
        quote_role="Gérant PME · Thionville",
        stats=[("25 ans", "d'expérience"), ("800+", "clients"), ("48 h", "bilan flash")],
        primary_href="contact.html",
        primary_label="Consultation gratuite",
        secondary_href="expertises.html",
        secondary_label="Nos expertises",
    )
    main += block_credentials_strip([
        ("OEC", "Ordre des experts-comptables"),
        ("DEC", "Diplôme d'expertise comptable"),
        ("ISO", "Processus qualité"),
        ("PME", "Spécialiste dirigeants"),
    ])
    main += """<section class="vt-reveal py-5">
  <div class="container">
    <div class="row g-4 align-items-center">
      <div class="col-lg-6">
        <p class="vt-eyebrow">Diagnostic</p>
        <h2 class="vt-section-title h3">30 min pour y voir clair</h2>
        <p class="text-secondary mb-3">On regarde ta situation, tes echeances, et on te dit ce qui bloque - sans jargon.</p>
        <button type="button" class="btn btn-vt-primary" data-vt-dialog-open="diagDialog">Reserver mon diagnostic</button>
      </div>
      <div class="col-lg-6">
        <div class="row g-3">
          <div class="col-6"><article class="vt-care-card h-100"><strong class="d-block">Bilan flash</strong><span class="small text-secondary">Sous 48 h</span></article></div>
          <div class="col-6"><article class="vt-care-card h-100"><strong class="d-block">Paie</strong><span class="small text-secondary">DSN a jour</span></article></div>
          <div class="col-6"><article class="vt-care-card h-100"><strong class="d-block">Tableau de bord</strong><span class="small text-secondary">Chaque mois</span></article></div>
          <div class="col-6"><article class="vt-care-card h-100"><strong class="d-block">1 interlocuteur</strong><span class="small text-secondary">Toujours le meme</span></article></div>
        </div>
      </div>
    </div>
  </div>
</section>"""
    main += block_dialog_m3(
        dialog_id="diagDialog",
        title="Diagnostic gratuit",
        lead="Dis-nous ton besoin - on te propose un creneau sous 24 h (demo).",
        primary_label="Envoyer",
        primary_href="contact.html",
        fields_html='<div class="mb-2"><label class="form-label small">Sujet</label><select class="form-select"><option>Tenue comptable</option><option>Paie</option><option>Bilan flash</option><option>Transmission</option></select></div><div class="mb-2"><label class="form-label small">Telephone</label><input class="form-control" type="tel"></div>',
    )
    main += block_snackbar_m3("Demande recue (demo)")
    main += block_fab_menu_m3([
        {"label": "Diagnostic", "dialog": "diagDialog"},
        {"label": "Expertises", "href": "expertises.html"},
        {"label": "Appeler", "href": "tel:0387759012"},
    ], main_label="Actions cabinet")
    main += "</main>"
    return _shell_comptable(
        "index.html",
        f"{CP_BRAND} — Expert-comptable Metz",
        "Cabinet d'expertise comptable à Metz, partenaire des PME lorraines depuis 1986.",
        main,
    )


def build_comptable_expertises() -> str:
    main = "<main>"
    main += block_hero_split(
        "Des expertises calibrées pour les dirigeants",
        "Tenue, paie et conseil — chaque prestation adaptée au stade de votre entreprise.",
        "hero.png",
        "Expertises comptables Metz",
        eyebrow="Expertises",
        primary_href="contact.html",
        primary_label="Demander un devis",
        secondary_href="methode.html",
        secondary_label="Notre méthode",
    )
    main += block_stat_narrative_rows(CP_STAT_NARRATIVE)
    main += block_menu_section(
        "Forfaits indicatifs",
        "Devis personnalisé après diagnostic gratuit. Tarifs TTC hors exceptionnel.",
        CP_EXPERTISES_MENU,
    )
    main += block_cta_band("Une question sur cette offre ?", "Nous contacter", "contact.html")
    main += "</main>"
    return _shell_comptable(
        "expertises.html",
        f"Expertises — {CP_BRAND}",
        "Tenue comptable, paie et conseil dirigeant à Metz.",
        main,
    )


def build_comptable_methode() -> str:
    main = "<main>"
    main += block_hero_editorial(
        "Une méthode en trois temps",
        "Écoute, action et suivi — transparence à chaque étape.",
        "hero.png",
        "Méthode Verlaine & Associés",
        eyebrow="Notre méthode",
        primary_href="contact.html",
        primary_label="Prendre RDV",
        secondary_href="expertises.html",
        secondary_label="Nos expertises",
    )
    main += block_timeline([
        ("1986", "Fondation du cabinet à Metz."),
        ("2010", "Ouverture permanence Thionville."),
        ("2020", "Certification qualité et outils cloud clients."),
        ("2024", "800 clients accompagnés en Grand Est."),
    ])
    main += block_funnel_steps("Notre démarche", [
        ("Écoute", "Diagnostic gratuit et définition des objectifs."),
        ("Action", "Mise en œuvre avec points d'étape réguliers."),
        ("Suivi", "Bilan et ajustements pour pérenniser les résultats."),
    ])
    main += block_faq_accordion("Questions fréquentes", CP_FAQ)
    main += block_cta_band("Rencontrons-nous à Metz.", "Prendre RDV", "contact.html")
    main += "</main>"
    return _shell_comptable(
        "methode.html",
        f"Notre méthode — {CP_BRAND}",
        "Approche et valeurs du cabinet comptable à Metz.",
        main,
    )


def build_comptable_contact() -> str:
    main = """<main>
<section class="vt-hero-compact py-5 text-center">
  <div class="container">
    <p class="vt-eyebrow text-uppercase">Contact</p>
    <h1 class="vt-display display-6">Parlons de votre projet</h1>
    <p class="lead text-secondary">Metz, Grand Est — réponse sous 24 h ouvrées.</p>
  </div>
</section>"""
    main += block_cabinet_contact_form(brand=CP_BRAND, address=CP_ADDRESS, phone=CP_PHONE, email=CP_EMAIL)
    main += block_cta_band("Démonstration — aucune donnée transmise.", "Envoyer ma demande", "contact.html")
    main += "</main>"
    return _shell_comptable(
        "contact.html",
        f"Contact — {CP_BRAND}",
        "Contactez Verlaine & Associés à Metz.",
        main,
    )


# --- Précisite Usinage (industrie) — specs + certs + flux horizontal ---
I_BRAND = "Précisite Usinage"
I_PHONE = "03 87 22 44 66"
I_EMAIL = "devis@precisite-usinage.fr"
I_ADDRESS = "ZI des Hauts Champs, 57970 Yutz"
I_MAPS = "https://maps.google.com/?q=ZI+des+Hauts+Champs+57970+Yutz"
I_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "savoir-faire.html", "label": "Savoir-faire"},
    {"file": "qualite.html", "label": "Qualité"},
    {"file": "contact.html", "label": "Contact"},
]
I_FOOTER_NAV = [
    ("Savoir-faire", "savoir-faire.html"),
    ("Qualité", "qualite.html"),
    ("Demander un devis", "contact.html"),
    ("Certifications", "qualite.html"),
]
I_CARDS = [
    {"title": "Usinage 5 axes", "text": "Pièces complexes aéro et automobile en une prise.", "img": "card-1.png", "alt": "Usinage 5 axes"},
    {"title": "Tournage CNC", "text": "Barres Ø 65 mm — séries moyennes et grandes.", "img": "card-2.png", "alt": "Tournage CNC"},
    {"title": "Métrologie 3D", "text": "MMT et scan laser — rapport de mesure livré.", "img": "card-3.png", "alt": "Contrôle qualité"},
]
I_CHAPTERS = [
    {"title": "Usinage 5 axes", "text": "12 centres simultanés — aluminium, acier, titane jusqu'à 800 mm.", "img": "scene-1.png", "alt": "Centre 5 axes en action"},
    {"title": "Métrologie 3D", "text": "Contrôle 100 % des lots critiques — laboratoire COFRAC sur site.", "img": "scene-2.png", "alt": "Métrologie 3D"},
    {"title": "Équipe & réactivité", "text": "85 collaborateurs — devis RFQ sous 48 h, production 3x8.", "img": "scene-3.png", "alt": "Équipe production"},
]
I_SPEC_ROWS = [
    ("Tolérance habituelle", "±0,01 mm (±5 µm sur demande)"),
    ("Dimensions max.", "800 × 600 × 500 mm"),
    ("Matériaux", "Alu, aciers, inox, titane, plastiques techniques"),
    ("Finition", "Ra 0,4 µm — polissage et traitements"),
    ("Capacité série", "1 à 50 000 pièces / an"),
    ("Délai prototype", "10 à 15 jours ouvrés"),
]


def _shell_industrie(page: str, title: str, desc: str, main: str) -> str:
    bar = block_info_bar(status="Production · Lun–ven 7h–18h", address=I_ADDRESS, phone=I_PHONE, maps_href=I_MAPS)
    nav = _chrome_nav("industrie", I_BRAND, I_NAV, page, cta_label="Demander un devis", cta_href="contact.html")
    foot = _chrome_foot("industrie", 
        I_BRAND,
        phone=I_PHONE,
        address=I_ADDRESS,
        email=I_EMAIL,
        maps_href=I_MAPS,
        nav_links=I_FOOTER_NAV,
        hours_line="Lun–ven 7h–18h · Yutz",
    )
    mobile = block_mobile_cta("Devis RFQ", "contact.html", I_PHONE)
    return wrap_page_industrial(title, desc, bar + nav + main + foot + mobile, slug="industrie", page=page, site_name=I_BRAND, nav=I_NAV)


def build_industrie_index() -> str:
    main = "<main>"
    main += block_hero_technical(
        "Tolérances micron pour l'auto et l'aéro",
        "Usinage 5 axes, métrologie 3D et réponse RFQ sous 48 h — Yutz, Lorraine.",
        "hero.png",
        "Vue d'ensemble Précisite Usinage à Yutz",
        eyebrow="Usinage de précision · Yutz",
        specs=[("±5 µm", "Tolérance"), ("5 axes", "CNC"), ("12 000 m²", "Atelier"), ("48 h", "Devis RFQ")],
        primary_href="contact.html",
        primary_label="Demander un devis",
        secondary_href="savoir-faire.html",
        secondary_label="Capacités",
    )
    main += block_spec_grid("Capacités machine", [
        {"label": "Fraisage", "value": "5 axes", "detail": "12 centres — pièces 800 mm"},
        {"label": "Tournage", "value": "Ø 65", "detail": "Barres et chutés — CBN"},
        {"label": "Contrôle", "value": "3D", "detail": "MMT + scan laser"},
        {"label": "Série", "value": "50k", "detail": "pièces / an max."},
    ])
    main += block_cert_strip([
        ("ISO", "9001:2015", "Management qualité"),
        ("IATF", "16949", "Automobile"),
        ("EN", "9100", "Aéronautique"),
        ("COFRAC", "Métrologie", "Labo interne"),
    ])
    main += block_process_flow("Parcours RFQ → livraison", [
        ("RFQ", "Réception plans STEP/IGES et cahier des charges."),
        ("Façabilité", "Étude procédé et devis sous 48 h."),
        ("Proto", "Premier article contrôlé et validé."),
        ("Série", "Production traçable et livraison JIT."),
    ])
    main += """<section class="vt-reveal py-5">
  <div class="container text-center">
    <p class="vt-eyebrow">RFQ</p>
    <h2 class="vt-section-title h3 mb-3">Envoie ton plan, on repond sous 48 h</h2>
    <p class="text-secondary mb-4">STEP, IGES ou PDF - on te dit si c'est faisable et a quel prix, sans blabla commercial.</p>
    <button type="button" class="btn btn-vt-primary btn-lg" data-vt-dialog-open="rfqDialog">Ouvrir une RFQ</button>
  </div>
</section>"""
    main += block_dialog_m3(
        dialog_id="rfqDialog",
        title="Demande RFQ",
        lead="Reference piece + delai souhaite - reponse technique sous 48 h (demo).",
        primary_label="Envoyer",
        primary_href="contact.html",
        fields_html='<div class="mb-2"><label class="form-label small">Reference</label><input class="form-control" placeholder="REF-2026-..."></div><div class="mb-2"><label class="form-label small">Quantite</label><input class="form-control" type="number" value="100"></div><div class="mb-2"><label class="form-label small">Email</label><input class="form-control" type="email"></div>',
    )
    main += block_snackbar_m3("RFQ enregistree (demo)")
    main += block_fab_menu_m3([
        {"label": "RFQ", "dialog": "rfqDialog"},
        {"label": "Capacites", "href": "savoir-faire.html"},
        {"label": "Qualite", "href": "qualite.html"},
    ], main_label="Actions usinage")
    main += "</main>"
    return _shell_industrie(
        "index.html",
        f"{I_BRAND} — Usinage de précision Yutz",
        "Usinage de précision à Yutz pour l'automobile et l'aéronautique en Lorraine.",
        main,
    )


def build_industrie_savoir_faire() -> str:
    main = "<main>"
    main += block_hero_split(
        "Savoir-faire usinage et contrôle",
        "Du prototype à la série — un interlocuteur technique dédié.",
        "hero.png",
        "Parc machines Précisite",
        eyebrow="Savoir-faire",
        primary_href="contact.html",
        primary_label="Envoyer une RFQ",
        secondary_href="qualite.html",
        secondary_label="Qualité",
    )
    main += block_specs_table("Fiche capacités", I_SPEC_ROWS)
    main += block_chapters(I_CHAPTERS)
    main += block_cards_bs("Procédés", I_CARDS)
    main += block_cta_band("Une question technique sur votre pièce ?", "Nous contacter", "contact.html")
    main += "</main>"
    return _shell_industrie(
        "savoir-faire.html",
        f"Savoir-faire — {I_BRAND}",
        "Capacités d'usinage 5 axes, tournage et métrologie à Yutz.",
        main,
    )


def build_industrie_qualite() -> str:
    main = "<main>"
    main += block_hero_editorial(
        "Qualité certifiée, traçabilité totale",
        "ISO 9001, IATF 16949 et laboratoire métrologie COFRAC.",
        "hero.png",
        "Atelier certifié Yutz",
        eyebrow="Qualité",
        primary_href="contact.html",
        primary_label="Demander un devis",
        secondary_href="savoir-faire.html",
        secondary_label="Savoir-faire",
    )
    main += block_cert_strip([
        ("ISO", "9001:2015", "Certifié Bureau Veritas"),
        ("IATF", "16949", "Automobile — audit 2025"),
        ("EN", "9100", "Aéronautique — en cours"),
        ("PPAP", "Niveau 3", "Premier article validé"),
    ])
    main += block_timeline([
        ("2010", "Création de Précisite Usinage à Yutz."),
        ("2016", "Extension atelier — 6 nouveaux centres 5 axes."),
        ("2020", "Certification IATF 16949 et labo métrologie."),
        ("2024", "12 000 m² — 85 collaborateurs."),
    ])
    main += block_comparison_table("Engagements qualité", [
        ("Traçabilité", "Lots sans identification", "Fiche matière + gamme + rapport 3D"),
        ("Premier article", "Validation client tardive", "PPAP et rapport de mesure systématiques"),
        ("Non-conformité", "Retouche non tracée", "8D et containment sous 24 h"),
        ("Audit", "Surprise en série", "Audits clients programmés et ouverts"),
    ])
    main += block_trust(
        "Culture premier article conforme — amélioration continue et audits clients.",
        ["PPAP", "8D", "COFRAC", "Traçabilité"],
    )
    main += block_cta_band("Rencontrons-nous sur site à Yutz.", "Demander un devis", "contact.html")
    main += "</main>"
    return _shell_industrie(
        "qualite.html",
        f"Qualité — {I_BRAND}",
        "Certifications et démarche qualité Précisite Usinage.",
        main,
    )


def build_industrie_contact() -> str:
    main = """<main>
<section class="vt-hero-compact py-5 text-center">
  <div class="container">
    <p class="vt-eyebrow text-uppercase">Contact</p>
    <h1 class="vt-display display-6">Parlons de votre projet</h1>
    <p class="lead text-secondary">Yutz, Grand Est — réponse technique sous 48 h.</p>
  </div>
</section>"""
    main += block_industrial_rfq_form(brand=I_BRAND, address=I_ADDRESS, phone=I_PHONE, email=I_EMAIL)
    main += block_cta_band("Démonstration — aucune donnée transmise.", "Envoyer ma demande", "contact.html")
    main += "</main>"
    return _shell_industrie(
        "contact.html",
        f"Contact — {I_BRAND}",
        "Demande de devis RFQ — Précisite Usinage Yutz.",
        main,
    )


# --- Patrimoine Lorraine (immobilier) — layout M3 maquette (_maquettes-echantillons/images/immobilier-m3.png) ---
IM_BRAND = "Patrimoine Lorraine"
IM_BRAND_FULL = "Patrimoine Lorraine Metz"
IM_PHONE = "03 87 36 12 14"
IM_EMAIL = "contact@patrimoine-lorraine.fr"
IM_ADDRESS = "14 rue des Clercs, 57000 Metz"
IM_MAPS = "https://maps.google.com/?q=14+rue+des+Clercs+57000+Metz"
IM_NAV = [
    {"file": "biens.html", "label": "Acheter"},
    {"file": "estimation.html", "label": "Vendre"},
    {"file": "index.html#agence", "label": "L'agence"},
    {"file": "estimation.html", "label": "Estimation"},
    {"file": "biens.html", "label": "Nos biens"},
    {"file": "contact.html", "label": "Contact"},
]
IM_FOOTER_NAV = [
    ("Nos biens", "biens.html"),
    ("Estimation", "estimation.html"),
    ("Estimer mon bien", "contact.html"),
    ("Gestion locative", "biens.html"),
]
IM_LISTINGS = [
    {
        "title": "Appartement 3 pièces",
        "price": "249 000 €",
        "address": "14 Rue des Clercs, 57000 Metz",
        "city": "Metz · Centre",
        "kind": "Vente",
        "surface": "68 m²",
        "rooms": "2 ch.",
        "baths": "1 sdb",
        "dpe": "D",
        "img": "card-2.png",
        "alt": "Appartement Metz centre",
        "specs": "68 m² · 3 pièces",
        "text": "Proche cathédrale, parquet et balcon.",
    },
    {
        "title": "Maison de maître",
        "price": "685 000 €",
        "address": "Metz Sablon",
        "city": "Metz · Sablon",
        "kind": "Vente",
        "surface": "280 m²",
        "rooms": "6 pièces",
        "baths": "jardin",
        "dpe": "C",
        "img": "card-1.png",
        "alt": "Maison Metz Sablon",
        "badge": "Coup de cœur",
        "specs": "280 m² · 6 pièces · jardin 800 m²",
        "text": "Rénovée 2024, garage double.",
    },
    {
        "title": "Appartement haussmannien",
        "price": "395 000 €",
        "address": "Nancy centre",
        "city": "Nancy · Centre",
        "kind": "Vente",
        "surface": "95 m²",
        "rooms": "3 ch.",
        "baths": "1 sdb",
        "dpe": "B",
        "img": "scene-1.png",
        "alt": "Appartement Nancy centre",
        "specs": "95 m² · 4 pièces · 2e étage",
        "text": "Parquet, moulures, vue parc.",
    },
]
IM_LISTINGS_EXTRA = [
    {
        "title": "Loft contemporain",
        "price": "289 000 €",
        "address": "Nancy",
        "city": "Nancy",
        "kind": "Vente",
        "surface": "72 m²",
        "rooms": "2 ch.",
        "baths": "1 sdb",
        "dpe": "C",
        "img": "gallery-1.png",
        "alt": "Loft Nancy",
        "specs": "72 m² · 3 pièces",
        "text": "Ancien atelier reconverti, terrasse.",
    },
    {
        "title": "Duplex centre",
        "price": "420 000 €",
        "address": "Metz Centre",
        "city": "Metz · Centre",
        "kind": "Vente",
        "surface": "110 m²",
        "rooms": "3 ch.",
        "baths": "2 sdb",
        "dpe": "C",
        "img": "scene-2.png",
        "alt": "Duplex Metz",
        "specs": "110 m² · 5 pièces",
        "text": "Proche cathédrale, deux parkings.",
    },
    {
        "title": "Maison récente",
        "price": "365 000 €",
        "address": "Laxou",
        "city": "Laxou",
        "kind": "Vente",
        "surface": "130 m²",
        "rooms": "4 ch.",
        "baths": "jardin",
        "dpe": "B",
        "img": "scene-3.png",
        "alt": "Maison Laxou",
        "badge": "Nouveau",
        "specs": "130 m² · 5 pièces",
        "text": "RT 2012, jardin clos, écoles à pied.",
    },
]
IM_CHAPTERS = [
    {"title": "Visites qualifiées", "text": "Chaque visite est préparée - dossier complet, quartier, fiscalité locale.", "img": "scene-1.png", "alt": "Visite appartement"},
    {"title": "Équipe locale", "text": "Ancrée à Metz et Nancy - on connaît chaque micro-marché mosellan.", "img": "scene-2.png", "alt": "Équipe agence"},
    {"title": "Jusqu'à l'acte", "text": "340+ ventes par an - suivi notarial et accompagnement primo-accédants.", "img": "scene-3.png", "alt": "Remise des clés"},
]
IM_CARDS = [
    {"title": "Vente", "text": "Mandats exclusifs, home staging et diffusion ciblée.", "img": "card-1.png", "alt": "Vente immobilière"},
    {"title": "Achat", "text": "Sélection de biens, financement et négociation.", "img": "card-2.png", "alt": "Achat immobilier"},
    {"title": "Gestion locative", "text": "Baux, quittances et états des lieux - clé en main.", "img": "card-3.png", "alt": "Gestion locative"},
]


def _shell_immobilier(page: str, title: str, desc: str, main: str) -> str:
    nav = block_immo_m3_nav(
        IM_BRAND_FULL,
        IM_NAV,
        page,
        phone=IM_PHONE,
        cta_label="Estimation gratuite",
        cta_href="estimation.html",
    )
    foot = _chrome_foot(
        "immobilier",
        IM_BRAND_FULL,
        phone=IM_PHONE,
        address=IM_ADDRESS,
        email=IM_EMAIL,
        maps_href=IM_MAPS,
        nav_links=IM_FOOTER_NAV,
        hours_line="Lun–ven 9h–19h · Sam 10h–13h",
    )
    mobile = block_mobile_cta("Estimation", "estimation.html", IM_PHONE)
    return wrap_page_property(
        title,
        desc,
        nav + main + foot + mobile,
        slug="immobilier",
        page=page,
        site_name=IM_BRAND_FULL,
        nav=IM_NAV,
        layout="immo-m3",
    )


def build_immobilier_index() -> str:
    main = '<main itemscope itemtype="https://schema.org/WebPage">'
    main += block_immo_m3_hero(
        "Votre projet immobilier, notre expertise à Metz",
        "Achat, vente, estimation : un accompagnement sur-mesure au cœur de la Lorraine.",
        "hero.png",
        "Vue de Metz — Patrimoine Lorraine",
        primary_href="estimation.html",
        primary_label="Estimation gratuite",
        secondary_href="biens.html",
        secondary_label="Découvrir nos biens",
    )
    main += block_immo_m3_search(action="biens.html")
    main += block_immo_m3_listings(
        "Sélection",
        IM_LISTINGS,
        count_label="36 biens disponibles",
        cta_href="biens.html",
        cta_label="Voir tous les biens",
    )
    main += '<div id="agence"></div>'
    main += """<section class="vt-reveal py-5 vt-immo-quartiers">
  <div class="container">
    <div class="row g-4 align-items-center">
      <div class="col-lg-6">
        <p class="vt-eyebrow text-uppercase">Quartiers</p>
        <h2 class="vt-section-title h3 mb-3">On connait Metz, pas juste les portails</h2>
        <div class="d-flex flex-wrap gap-2 mb-4">
          <span class="badge rounded-pill text-bg-light px-3 py-2">Sablon</span>
          <span class="badge rounded-pill text-bg-light px-3 py-2">Queuleu</span>
          <span class="badge rounded-pill text-bg-light px-3 py-2">Devant-les-Ponts</span>
          <span class="badge rounded-pill text-bg-light px-3 py-2">Montigny</span>
        </div>
        <div class="d-flex flex-wrap gap-2">
          <button type="button" class="btn btn-vt-primary" data-vt-dialog-open="estimDialog">Estimation sous 72 h</button>
          <button type="button" class="btn btn-vt-outline" data-vt-dialog-open="visitDialog">Demander une visite</button>
        </div>
      </div>
      <div class="col-lg-6">
        <article class="vt-immo-pulse-card">
          <p class="small text-uppercase fw-bold mb-2">Alerte bien</p>
          <p class="mb-2">Nouveau · T3 Queuleu · 289 000 euro</p>
          <p class="small text-secondary mb-3">Balcon, cave, proche tram - dispo visite ce week-end.</p>
          <button type="button" class="btn btn-sm btn-vt-primary" data-vt-dialog-open="visitDialog">Reserver un creneau</button>
        </article>
      </div>
    </div>
  </div>
</section>"""
    main += block_dialog_m3(
        dialog_id="estimDialog",
        title="Estimation gratuite",
        lead="Adresse et type de bien - rapport sous 72 h (demo).",
        primary_label="Demander",
        primary_href="estimation.html",
        fields_html='<div class="mb-2"><label class="form-label small">Adresse</label><input class="form-control" placeholder="Metz..."></div><div class="mb-2"><label class="form-label small">Type</label><select class="form-select"><option>Appartement</option><option>Maison</option></select></div>',
    )
    main += block_dialog_m3(
        dialog_id="visitDialog",
        title="Demander une visite",
        lead="On te propose 2 creneaux sous 24 h (demo).",
        primary_label="Envoyer",
        primary_href="contact.html",
        fields_html='<div class="mb-2"><label class="form-label small">Bien / quartier</label><input class="form-control" placeholder="Queuleu, Sablon..."></div><div class="mb-2"><label class="form-label small">Telephone</label><input class="form-control" type="tel"></div>',
    )
    main += block_fab_menu_m3([
        {"label": "Estimation", "dialog": "estimDialog"},
        {"label": "Visite", "dialog": "visitDialog"},
        {"label": "Biens", "href": "biens.html"},
    ], main_label="Actions immo")
    main += "</main>"
    return _shell_immobilier(
        "index.html",
        f"{IM_BRAND} — Immobilier Metz",
        "Agence immobilière à Metz : vente, location et estimation sur le Grand Est.",
        main,
    )


def build_immobilier_biens() -> str:
    all_listings = IM_LISTINGS + IM_LISTINGS_EXTRA
    main = "<main>"
    main += block_immo_m3_hero(
        "Nos biens en Moselle",
        "Maisons, appartements et terrains - sélection actualisée chaque semaine.",
        "hero.png",
        "Sélection Patrimoine Lorraine",
        primary_href="contact.html",
        primary_label="Demander une visite",
        secondary_href="estimation.html",
        secondary_label="Estimer mon bien",
    )
    main += block_immo_m3_search(action="biens.html")
    main += block_immo_m3_listings("Toutes nos annonces", all_listings, count_label=f"{len(all_listings)} biens sélectionnés")
    main += block_funnel_steps("Parcours acquéreur", [
        ("Recherche", "Définir critères, budget et secteur avec un conseiller."),
        ("Visites", "Sélection qualifiée - dossiers complets avant chaque visite."),
        ("Offre", "Négociation et montage financement accompagnés."),
        ("Acte", "Suivi notarial jusqu'à la remise des clés."),
    ])
    main += block_cta_band("Un bien vous intéresse ?", "Nous contacter", "contact.html")
    main += "</main>"
    return _shell_immobilier(
        "biens.html",
        f"Nos biens — {IM_BRAND}",
        "Annonces immobilières Metz, Nancy et Moselle.",
        main,
    )


def build_immobilier_estimation() -> str:
    main = "<main>"
    main += block_immo_m3_hero(
        "Estimation gratuite sous 72 h",
        "Analyse marché locale, visite optionnelle et fourchette de prix argumentée.",
        "hero.png",
        "Estimation immobilière Metz",
        primary_href="contact.html",
        primary_label="Demander une estimation",
        secondary_href="biens.html",
        secondary_label="Voir nos biens",
    )
    main += block_funnel_steps("Notre méthode d'estimation", [
        ("Visite", "Diagnostic du bien, état, travaux et environnement."),
        ("Marché", "Comparables récents dans votre quartier."),
        ("Rapport", "Fourchette de prix et conseils de mise en valeur."),
        ("Mandat", "Si vous vendez - stratégie de commercialisation."),
    ])
    main += block_property_estimation_form(brand=IM_BRAND, address=IM_ADDRESS, phone=IM_PHONE, email=IM_EMAIL)
    main += "</main>"
    return _shell_immobilier(
        "estimation.html",
        f"Estimation — {IM_BRAND}",
        "Estimation gratuite de votre bien à Metz et en Moselle.",
        main,
    )


def build_immobilier_contact() -> str:
    main = """<main>
<section class="vt-immo-hero pt-5 pb-3">
  <div class="container">
    <h1 class="vt-display display-6">Parlons de votre projet</h1>
    <p class="lead text-secondary">14 rue des Clercs, Metz - réponse sous 24 h.</p>
  </div>
</section>"""
    main += block_property_estimation_form(brand=IM_BRAND, address=IM_ADDRESS, phone=IM_PHONE, email=IM_EMAIL)
    main += block_cta_band("Démonstration - aucune donnée transmise.", "Envoyer ma demande", "contact.html")
    main += "</main>"
    return _shell_immobilier(
        "contact.html",
        f"Contact — {IM_BRAND}",
        "Contactez Patrimoine Lorraine à Metz.",
        main,
    )


# --- Rivière & Partenaires (juridique) — hero overlay + tuiles expertises + FAQ ---
JU_BRAND = "Rivière & Partenaires"
JU_PHONE = "03 87 75 90 12"
JU_EMAIL = "contact@riviere-partenaires.fr"
JU_ADDRESS = "12 avenue Foch, 57000 Metz"
JU_MAPS = "https://maps.google.com/?q=12+avenue+Foch+57000+Metz"
JU_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "expertises.html", "label": "Expertises"},
    {"file": "accompagnement.html", "label": "Accompagnement"},
    {"file": "contact.html", "label": "Contact"},
]
JU_FOOTER_NAV = [
    ("Expertises", "expertises.html"),
    ("Accompagnement", "accompagnement.html"),
    ("Consultation", "contact.html"),
    ("Barreau Metz", "index.html"),
]
JU_CARDS = [
    {"title": "Droit des sociétés", "text": "Création, pactes d'associés, AG et gouvernance PME.", "img": "card-1.png", "alt": "Droit des sociétés"},
    {"title": "Droit social", "text": "Contrats, licenciement, CSE et négociation collective.", "img": "card-2.png", "alt": "Droit social"},
    {"title": "Contentieux", "text": "Recouvrement, rupture contractuelle et médiation.", "img": "card-3.png", "alt": "Contentieux commercial"},
]
JU_CHAPTERS = [
    {"title": "Écoute structurée", "text": "Premier rendez-vous — diagnostic confidentiel et feuille de route.", "img": "scene-1.png", "alt": "Consultation avocat Metz"},
    {"title": "Équipe collégiale", "text": "6 associés — spécialisation par domaine, Barreau de Metz.", "img": "scene-2.png", "alt": "Équipe avocats"},
    {"title": "Jusqu'à l'acte", "text": "850+ dossiers par an — suivi contentieux et transactions.", "img": "scene-3.png", "alt": "Signature acte"},
]
JU_PRACTICE_TILES = [
    {"title": "Sociétés", "items": ["Pactes & AG", "Restructuration", "Gouvernance PME"], "hot": True},
    {"title": "Social", "items": ["Contrats travail", "Licenciement", "Conformité RH"]},
    {"title": "Contentieux", "items": ["Recouvrement", "Médiation", "Prud'hommes"]},
]
JU_EXPERTISE_MENU = [
    {
        "title": "Droit des affaires",
        "items": [
            {"name": "Création de société", "desc": "Statuts, pacte, immatriculation", "price": "dès 890 € HT", "tags": ["PME"]},
            {"name": "Pacte d'associés", "desc": "Gouvernance et clauses de sortie", "price": "sur devis", "tags": []},
            {"name": "Transmission", "desc": "Cession, earn-out, garantie d'actif-passif", "price": "sur devis", "tags": ["Dirigeant"]},
        ],
    },
    {
        "title": "Social & contentieux",
        "items": [
            {"name": "Licenciement", "desc": "Conseil employeur ou salarié", "price": "forfait dès 1 200 €", "tags": []},
            {"name": "Recouvrement", "desc": "Mise en demeure à saisie", "price": "honoraires au résultat", "tags": []},
            {"name": "Médiation commerciale", "desc": "Règlement amiable avant procès", "price": "290 € HT / séance", "tags": ["Express"]},
        ],
    },
]
JU_FAQ = [
    ("Comment se déroule la première consultation ?", "Entretien confidentiel de 45 min — analyse de votre situation et proposition de stratégie. Forfait découverte 290 € HT."),
    ("Quels sont vos honoraires ?", "Forfaits validés par écrit ou honoraires au temps passé — devis transparent avant toute mission."),
    ("Intervenez-vous hors Metz ?", "Oui — permanences Thionville et visio pour clients Grand Est."),
    ("Pouvez-vous représenter mon entreprise au tribunal ?", "Oui — contentieux commercial, prud'hommes et tribunaux administratifs."),
    ("Le secret professionnel est-il garanti ?", "Absolument — cadre déontologique du Barreau de Metz."),
]


def _shell_juridique(page: str, title: str, desc: str, main: str) -> str:
    bar = block_info_bar(status="Cabinet ouvert · Lun–ven 9h–18h", address=JU_ADDRESS, phone=JU_PHONE, maps_href=JU_MAPS)
    nav = _chrome_nav("juridique", JU_BRAND, JU_NAV, page, cta_label="Consultation", cta_href="contact.html")
    foot = _chrome_foot("juridique", 
        JU_BRAND,
        phone=JU_PHONE,
        address=JU_ADDRESS,
        email=JU_EMAIL,
        maps_href=JU_MAPS,
        nav_links=JU_FOOTER_NAV,
        hours_line="Lun–ven 9h–18h · Barreau de Metz",
    )
    mobile = block_mobile_cta("Consultation", "contact.html", JU_PHONE)
    return wrap_page_legal(title, desc, bar + nav + main + foot + mobile, slug="juridique", page=page, site_name=JU_BRAND, nav=JU_NAV)


def build_juridique_index() -> str:
    main = "<main>"
    main += """<section class="vt-legal-hero vt-reveal">
  <div class="container">
    <div class="row g-4 g-xl-5 align-items-center">
      <div class="col-lg-6">
        <p class="vt-eyebrow mb-2">Avocats · Barreau de Metz</p>
        <h1 class="vt-display display-4 mb-3">Le droit, explique clairement</h1>
        <p class="lead mb-4">A vos cotes a chaque etape - rigueur, humanite et transparence, sans jargon inutile.</p>
        <div class="d-flex flex-wrap gap-2">
          <button type="button" class="btn btn-vt-primary btn-lg" data-vt-dialog-open="rdvJur">Prendre RDV</button>
          <a class="btn btn-vt-outline btn-lg" href="expertises.html">Domaines</a>
        </div>
      </div>
      <div class="col-lg-6">
        <figure class="vt-legal-hero-media mb-0">
          <picture><source srcset="images/hero.webp" type="image/webp"><img src="images/hero.png" alt="Cabinet a Metz" decoding="async" fetchpriority="high"></picture>
        </figure>
      </div>
    </div>
  </div>
</section>"""
    main += """<section class="vt-cred-band vt-reveal">
  <div class="container">
    <div class="row g-3">
      <div class="col-md-3"><div class="vt-cred-item"><span class="vt-cred-ico" aria-hidden="true">§</span><div><strong>Barreau de Metz</strong><p class="small text-secondary mb-0">Inscrits au barreau</p></div></div></div>
      <div class="col-md-3"><div class="vt-cred-item"><span class="vt-cred-ico" aria-hidden="true">◎</span><div><strong>Mediation</strong><p class="small text-secondary mb-0">Modes amiables privilegies</p></div></div></div>
      <div class="col-md-3"><div class="vt-cred-item"><span class="vt-cred-ico" aria-hidden="true">◈</span><div><strong>Droit des affaires</strong><p class="small text-secondary mb-0">Conseil et contentieux</p></div></div></div>
      <div class="col-md-3"><div class="vt-cred-item"><span class="vt-cred-ico" aria-hidden="true">◇</span><div><strong>Droit de la famille</strong><p class="small text-secondary mb-0">Ecoute et confidentialite</p></div></div></div>
    </div>
  </div>
</section>"""
    main += """<section class="vt-reveal py-5">
  <div class="container">
    <p class="vt-eyebrow">Notre methode</p>
    <h2 class="vt-section-title h3 mb-4">Un accompagnement en 4 etapes</h2>
    <div class="row g-3 pt-2">
      <div class="col-md-3"><article class="vt-method-step"><span>1</span><h3 class="h6 mt-2">Ecoute</h3><p class="small text-secondary mb-0">On prend le temps de comprendre ta situation et tes objectifs.</p></article></div>
      <div class="col-md-3"><article class="vt-method-step"><span>2</span><h3 class="h6 mt-2">Analyse</h3><p class="small text-secondary mb-0">Faits, droit applicable, enjeux du dossier.</p></article></div>
      <div class="col-md-3"><article class="vt-method-step"><span>3</span><h3 class="h6 mt-2">Strategie</h3><p class="small text-secondary mb-0">On definit avec toi la voie la plus adaptee.</p></article></div>
      <div class="col-md-3"><article class="vt-method-step"><span>4</span><h3 class="h6 mt-2">Suivi</h3><p class="small text-secondary mb-0">Tu es informe a chaque etape, sans zone d'ombre.</p></article></div>
    </div>
  </div>
</section>"""
    main += block_dialog_m3(
        dialog_id="rdvJur",
        title="Prendre RDV",
        lead="Premier echange 45 min - on te rappelle sous 24 h (demo).",
        primary_label="Envoyer",
        primary_href="contact.html",
        fields_html='<div class="mb-2"><label class="form-label small">Sujet</label><select class="form-select"><option>Affaires</option><option>Social</option><option>Famille</option><option>Contentieux</option></select></div><div class="mb-2"><label class="form-label small">Telephone</label><input class="form-control" type="tel"></div>',
    )
    main += block_fab_menu_m3([
        {"label": "RDV", "dialog": "rdvJur"},
        {"label": "Expertises", "href": "expertises.html"},
        {"label": "Appeler", "href": "tel:0387759012"},
    ], main_label="Actions cabinet")
    main += "</main>"
    return _shell_juridique(
        "index.html",
        f"{JU_BRAND} — Avocats Metz",
        "Cabinet d'avocats à Metz : droit des affaires, social et contentieux pour PME.",
        main,
    )


def build_juridique_expertises() -> str:
    main = "<main>"
    main += block_hero_split(
        "Expertises juridiques",
        "Sociétés, social, contentieux — une équipe par domaine.",
        "hero.png",
        "Expertises Rivière & Partenaires",
        eyebrow="Expertises",
        primary_href="contact.html",
        primary_label="Consultation",
        secondary_href="accompagnement.html",
        secondary_label="Notre méthode",
    )
    main += block_menu_section(
        "Honoraires indicatifs",
        "Forfaits et honoraires au temps passé — devis écrit avant engagement.",
        JU_EXPERTISE_MENU,
    )
    main += block_chapters(JU_CHAPTERS)
    main += block_cards_bs("Nos domaines", JU_CARDS)
    main += block_comparison_table("Notre approche", [
        ("Premier contact", "Orientation floue", "Diagnostic 45 min — feuille de route"),
        ("Honoraires", "Surprise en fin de dossier", "Forfait ou devis validé par écrit"),
        ("Contentieux", "Procès systématique", "Médiation et stratégie amiable d'abord"),
        ("Suivi", "Interlocuteur variable", "Associé référent dédié"),
    ])
    main += block_cta_band("Une question sur une expertise ?", "Nous contacter", "contact.html")
    main += "</main>"
    return _shell_juridique(
        "expertises.html",
        f"Expertises — {JU_BRAND}",
        "Droit des sociétés, social et contentieux à Metz.",
        main,
    )


def build_juridique_accompagnement() -> str:
    main = "<main>"
    main += block_hero_editorial(
        "Accompagnement sur mesure",
        "Écoute, action et suivi — méthode en trois temps pour dirigeants.",
        "hero.png",
        "Accompagnement juridique Metz",
        eyebrow="Accompagnement",
        primary_href="contact.html",
        primary_label="Consultation",
        secondary_href="expertises.html",
        secondary_label="Expertises",
    )
    main += block_funnel_steps("Notre méthode", [
        ("Écoute", "Diagnostic confidentiel et définition des objectifs."),
        ("Action", "Stratégie juridique et mise en œuvre avec points d'étape."),
        ("Suivi", "Bilan, ajustements et veille pour pérenniser les résultats."),
    ])
    main += block_timeline([
        ("1992", "Création du cabinet à Metz."),
        ("2003", "Installation 12 avenue Foch."),
        ("2016", "6 associés — extension droit social."),
        ("2024", "850+ dossiers — médiation certifiée."),
    ])
    main += block_chapters(JU_CHAPTERS)
    main += block_stat_narrative_rows([
        {"stat": "45 min", "stat_label": "Consultation", "title": "Forfait découverte", "text": "Analyse de situation et premières recommandations.", "img": "scene-1.png", "alt": "Consultation"},
        {"stat": "100 %", "stat_label": "Confidentiel", "title": "Secret professionnel", "text": "Cadre déontologique strict du Barreau de Metz.", "img": "scene-2.png", "alt": "Équipe"},
        {"stat": "290 €", "stat_label": "HT forfait", "title": "Transparence", "text": "Honoraires validés par écrit avant toute mission.", "img": "scene-3.png", "alt": "Signature"},
    ])
    main += block_cta_band("Rencontrons-nous à Metz.", "Consultation", "contact.html")
    main += "</main>"
    return _shell_juridique(
        "accompagnement.html",
        f"Accompagnement — {JU_BRAND}",
        "Méthode d'accompagnement juridique Rivière & Partenaires.",
        main,
    )


def build_juridique_contact() -> str:
    main = """<main>
<section class="vt-hero-compact py-5 text-center">
  <div class="container">
    <p class="vt-eyebrow text-uppercase">Contact</p>
    <h1 class="vt-display display-6">Parlons de votre projet</h1>
    <p class="lead text-secondary">Metz, Grand Est — réponse sous 24 h ouvrées.</p>
  </div>
</section>"""
    main += block_legal_consultation_form(brand=JU_BRAND, address=JU_ADDRESS, phone=JU_PHONE, email=JU_EMAIL)
    main += block_cta_band("Démonstration — aucune donnée transmise.", "Envoyer ma demande", "contact.html")
    main += "</main>"
    return _shell_juridique(
        "contact.html",
        f"Contact — {JU_BRAND}",
        "Contactez Rivière & Partenaires à Metz.",
        main,
    )


# --- Atelier Nord-Est (architecture) — hero éditorial + bento magazine + grille projets ---
AR_BRAND = "Atelier Nord-Est"
AR_PHONE = "03 87 66 12 34"
AR_EMAIL = "contact@atelier-nord-est.fr"
AR_ADDRESS = "14 rue du XXe Corps, 57000 Metz"
AR_MAPS = "https://maps.google.com/?q=14+rue+du+XXe+Corps+57000+Metz"
AR_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "projets.html", "label": "Projets"},
    {"file": "methode.html", "label": "Méthode"},
    {"file": "contact.html", "label": "Contact"},
]
AR_FOOTER_NAV = [
    ("Projets", "projets.html"),
    ("Méthode", "methode.html"),
    ("Brief projet", "contact.html"),
    ("RE2020", "methode.html"),
]
AR_PROJECTS = [
    {"title": "Réhabilitation maison Jaumont", "year": "2023", "specs": "Metz centre · 180 m²", "text": "Pierre Jaumont, isolation thermique et extension bois.", "img": "card-1.png", "alt": "Réhabilitation Jaumont", "badge": "Patrimoine"},
    {"title": "12 logements RE2020", "year": "2024", "specs": "Laxou · collectif", "text": "Structure bois, balcons filants, label E+C-.", "img": "card-2.png", "alt": "Logements Laxou"},
    {"title": "Extension école Metz", "year": "2022", "specs": "ERP · 1 200 m²", "text": "Aile contemporaine bois-verre, classe énergétique A.", "img": "card-3.png", "alt": "Extension école"},
]
AR_PROJECTS_EXTRA = [
    {"title": "Médiathèque Thionville", "year": "2021", "specs": "ERP · 2 400 m²", "text": "Façade bois, lumière zénithale, accessibilité PMR.", "img": "gallery-2.png", "alt": "Médiathèque Thionville"},
    {"title": "Loft Sablon", "year": "2024", "specs": "Metz · 95 m²", "text": "Réhabilitation loft industriel, structure apparente.", "img": "gallery-1.png", "alt": "Loft Metz", "badge": "Coup de cœur"},
    {"title": "Maison passive Nancy", "year": "2023", "specs": "Nancy · 140 m²", "text": "Ossature bois, triple vitrage, VMC double flux.", "img": "scene-3.png", "alt": "Maison passive"},
]
AR_BENTO = [
    {"title": "Réhabilitation Jaumont", "text": "Metz centre — pierre et extension contemporaine.", "img": "card-1.png", "alt": "Jaumont", "size": "lg"},
    {"title": "Logements RE2020", "text": "Laxou — 12 logements bois.", "img": "card-2.png", "alt": "Laxou"},
    {"title": "Médiathèque", "text": "Thionville — ERP durable.", "img": "gallery-2.png", "alt": "Thionville"},
]
AR_CHAPTERS = [
    {"title": "Esquisse à permis", "text": "Programme, esquisse et dépôt permis — un interlocuteur dédié.", "img": "scene-1.png", "alt": "Maquette projet"},
    {"title": "Équipe pluridisciplinaire", "text": "12 collaborateurs — architecture, BET et suivi de chantier.", "img": "scene-2.png", "alt": "Équipe atelier"},
    {"title": "Réhabilitation patrimoine", "text": "Jaumont, brique et structures contemporaines en Lorraine.", "img": "scene-3.png", "alt": "Chantier Metz"},
]
AR_CARDS = [
    {"title": "Réhabilitation", "text": "Patrimoine mosellan, RE2020 et confort d'usage.", "img": "card-1.png", "alt": "Réhabilitation"},
    {"title": "Logement neuf", "text": "Collectif et individuel — bois et basse consommation.", "img": "card-2.png", "alt": "Logement neuf"},
    {"title": "Équipements publics", "text": "Écoles, médiathèques, équipements sportifs.", "img": "card-3.png", "alt": "ERP"},
]
AR_COMPACT = [
    {"title": "Réhabilitation patrimoine", "text": "Jaumont, brique, extensions bois respectueuses du tissu urbain.", "img": "card-1.png", "alt": "Patrimoine"},
    {"title": "Conception RE2020", "text": "Bilan carbone, matériaux biosourcés, performance énergétique.", "img": "card-2.png", "alt": "RE2020"},
    {"title": "Suivi de chantier", "text": "OPC, réunions de chantier et réception des travaux.", "img": "scene-3.png", "alt": "Chantier"},
]


def _shell_architecture(page: str, title: str, desc: str, main: str) -> str:
    bar = block_info_bar(status="Atelier ouvert · Lun–ven 9h–18h", address=AR_ADDRESS, phone=AR_PHONE, maps_href=AR_MAPS)
    nav = _chrome_nav("architecture", AR_BRAND, AR_NAV, page, cta_label="Brief projet", cta_href="contact.html")
    foot = _chrome_foot("architecture", 
        AR_BRAND,
        phone=AR_PHONE,
        address=AR_ADDRESS,
        email=AR_EMAIL,
        maps_href=AR_MAPS,
        nav_links=AR_FOOTER_NAV,
        hours_line="Lun–ven 9h–18h · Metz",
    )
    mobile = block_mobile_cta("Brief projet", "contact.html", AR_PHONE)
    return wrap_page_architecture(title, desc, bar + nav + main + foot + mobile, slug="architecture", page=page, site_name=AR_BRAND, nav=AR_NAV)


def build_architecture_index() -> str:
    main = "<main>"
    main += """<section class="vt-arch-hero vt-reveal">
  <div class="vt-arch-hero-bg" aria-hidden="true">
    <picture><source srcset="images/hero.webp" type="image/webp"><img src="images/hero.png" alt="" decoding="async" fetchpriority="high"></picture>
  </div>
  <div class="container vt-arch-hero-copy">
    <p class="vt-eyebrow mb-2">Architecture · Grand Est</p>
    <h1 class="vt-display display-3 mb-3">Architecture sensible</h1>
    <p class="lead mb-4">Rehabilitation, logements et equipements - ancrage lorrain, detail soigne.</p>
    <div class="d-flex flex-wrap gap-2">
      <a class="btn btn-vt-primary btn-lg" href="projets.html">Voir les projets</a>
      <button type="button" class="btn btn-vt-outline btn-lg" data-vt-dialog-open="briefArch">Brief projet</button>
    </div>
  </div>
</section>"""
    main += """<section class="vt-reveal py-5">
  <div class="container">
    <p class="vt-eyebrow">Selection</p>
    <h2 class="vt-section-title h3 mb-4">Realisations recentes</h2>
    <div class="vt-arch-rail vt-reveal-stagger">
      <article class="vt-arch-card"><picture><source srcset="images/card-1.webp" type="image/webp"><img src="images/card-1.png" alt="Maison Jaumont" loading="lazy"></picture><div class="vt-arch-card-body"><h3 class="h6 mb-1">Maison Jaumont</h3><p class="small mb-0">Metz · 2023</p></div></article>
      <article class="vt-arch-card"><picture><source srcset="images/card-2.webp" type="image/webp"><img src="images/card-2.png" alt="Logements Laxou" loading="lazy"></picture><div class="vt-arch-card-body"><h3 class="h6 mb-1">Collectif Laxou</h3><p class="small mb-0">RE2020 · 2024</p></div></article>
      <article class="vt-arch-card"><picture><source srcset="images/gallery-2.webp" type="image/webp"><img src="images/gallery-2.png" alt="Equipement Thionville" loading="lazy"></picture><div class="vt-arch-card-body"><h3 class="h6 mb-1">ERP Thionville</h3><p class="small mb-0">Bois &amp; verre</p></div></article>
      <article class="vt-arch-card"><picture><source srcset="images/gallery-1.webp" type="image/webp"><img src="images/gallery-1.png" alt="Interieur" loading="lazy"></picture><div class="vt-arch-card-body"><h3 class="h6 mb-1">Interieur Sablon</h3><p class="small mb-0">Logement · 2024</p></div></article>
    </div>
  </div>
</section>"""
    main += block_dialog_m3(
        dialog_id="briefArch",
        title="Brief projet",
        lead="Type de projet + localisation - on te repond sous 48 h (demo).",
        primary_label="Envoyer",
        primary_href="contact.html",
        fields_html='<div class="mb-2"><label class="form-label small">Type</label><select class="form-select"><option>Rehabilitation</option><option>Logement neuf</option><option>ERP / public</option></select></div><div class="mb-2"><label class="form-label small">Ville</label><input class="form-control" placeholder="Metz, Nancy..."></div>',
    )
    main += block_fab_menu_m3([
        {"label": "Brief", "dialog": "briefArch"},
        {"label": "Projets", "href": "projets.html"},
        {"label": "Methode", "href": "methode.html"},
    ], main_label="Actions atelier")
    main += "</main>"
    return _shell_architecture(
        "index.html",
        f"{AR_BRAND} — Architecture Metz",
        "Agence d'architecture à Metz : réhabilitation, logements et équipements publics.",
        main,
    )


def build_architecture_projets() -> str:
    all_projects = AR_PROJECTS + AR_PROJECTS_EXTRA
    main = "<main>"
    main += block_hero_split(
        "Nos projets",
        "Réhabilitation, logements et ERP — portfolio Moselle et Grand Est.",
        "hero.png",
        "Portfolio Atelier Nord-Est",
        eyebrow="Projets",
        primary_href="contact.html",
        primary_label="Brief projet",
        secondary_href="methode.html",
        secondary_label="Notre méthode",
    )
    main += block_project_grid("Portfolio", all_projects)
    main += block_bento_cards(AR_BENTO)
    main += block_cards_bs("Expertises", AR_CARDS)
    main += block_cta_band("Un projet similaire ?", "Nous contacter", "contact.html")
    main += "</main>"
    return _shell_architecture(
        "projets.html",
        f"Projets — {AR_BRAND}",
        "Portfolio architecture Atelier Nord-Est — Metz et Moselle.",
        main,
    )


def build_architecture_methode() -> str:
    main = "<main>"
    main += block_hero_split_reverse(
        "De l'esquisse à la réception",
        "Méthode en 4 phases — permis, chantier et RE2020.",
        "hero.png",
        "Méthode Atelier Nord-Est",
        eyebrow="Méthode",
        primary_href="contact.html",
        primary_label="Brief projet",
        secondary_href="projets.html",
        secondary_label="Voir les projets",
    )
    main += block_process_flow("Parcours projet", [
        ("Programme", "Brief, faisabilité et esquisse architecturale."),
        ("Permis", "APS, APD, dépôt et suivi instruction."),
        ("Chantier", "DCE, consultation entreprises, OPC."),
        ("Réception", "Livraison, DOE et garanties."),
    ])
    main += block_timeline([
        ("2008", "Création de l'atelier à Metz."),
        ("2014", "Premier projet RE2020 livré."),
        ("2019", "Extension équipe — 12 collaborateurs."),
        ("2024", "85+ projets — label E+C-."),
    ])
    main += block_chapters(AR_CHAPTERS)
    main += block_funnel_steps("Accompagnement maître d'ouvrage", [
        ("Brief", "Programme, budget et contraintes du site."),
        ("Conception", "Esquisse, permis et choix des matériaux."),
        ("Réalisation", "Suivi chantier et coordination BET."),
        ("Usage", "Réception et accompagnement post-livraison."),
    ])
    main += block_cta_band("Parlons de votre programme.", "Brief projet", "contact.html")
    main += "</main>"
    return _shell_architecture(
        "methode.html",
        f"Méthode — {AR_BRAND}",
        "Méthode de conception Atelier Nord-Est — Metz.",
        main,
    )


def build_architecture_contact() -> str:
    main = """<main>
<section class="vt-hero-compact py-5 text-center">
  <div class="container">
    <p class="vt-eyebrow text-uppercase">Contact</p>
    <h1 class="vt-display display-6">Brief projet</h1>
    <p class="lead text-secondary">Metz — réponse sous 48 h.</p>
  </div>
</section>"""
    main += block_architecture_brief_form(brand=AR_BRAND, address=AR_ADDRESS, phone=AR_PHONE, email=AR_EMAIL)
    main += block_cta_band("Démonstration — aucune donnée transmise.", "Envoyer mon brief", "contact.html")
    main += "</main>"
    return _shell_architecture(
        "contact.html",
        f"Contact — {AR_BRAND}",
        "Contactez Atelier Nord-Est à Metz.",
        main,
    )


# --- Pulse Fitness Metz (fitness) — hero overlay sombre + planning + tarifs ---
FIT_BRAND = "Pulse Fitness Metz"
FIT_PHONE = "03 87 55 40 00"
FIT_EMAIL = "contact@pulse-fitness-metz.fr"
FIT_ADDRESS = "42 avenue de Strasbourg, 57000 Metz"
FIT_MAPS = "https://maps.google.com/?q=42+avenue+de+Strasbourg+57000+Metz"
FIT_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "cours.html", "label": "Cours"},
    {"file": "tarifs.html", "label": "Tarifs"},
    {"file": "contact.html", "label": "Contact"},
]
FIT_FOOTER_NAV = [
    ("Cours", "cours.html"),
    ("Tarifs", "tarifs.html"),
    ("Essai gratuit", "contact.html"),
    ("Planning", "cours.html#planning"),
]
FIT_SCHEDULE_HEADERS = ["", "Lun", "Mar", "Mer", "Jeu", "Ven"]
FIT_SCHEDULE_ROWS = [
    ["6h30", "Yoga", "—", "HIIT", "—", "Cycling"],
    ["12h15", "—", "Cross", "—", "Cross", "—"],
    ["19h00", "Cycling", "HIIT", "Yoga", "HIIT", "Cross"],
]
FIT_CARDS = [
    {"title": "HIIT & Cross", "text": "Fractionné haute intensité — 45 min, tous niveaux.", "img": "card-1.png", "alt": "Cours HIIT"},
    {"title": "Cycling", "text": "Studio immersif, playlists live — 30 ou 50 min.", "img": "card-2.png", "alt": "Studio cycling"},
    {"title": "Yoga Flow", "text": "Mobilité et récupération — matin et soir.", "img": "card-3.png", "alt": "Cours yoga"},
]
FIT_CHAPTERS = [
    {"title": "HIIT encadré", "text": "Coachs certifiés, groupes limités à 16 personnes.", "img": "scene-1.png", "alt": "Cours HIIT"},
    {"title": "Studio cycling", "text": "20 vélos, écran LED et ambiance immersive.", "img": "scene-2.png", "alt": "Cycling"},
    {"title": "Yoga & récup", "text": "Espace zen pour compléter votre entraînement.", "img": "scene-3.png", "alt": "Yoga Flow"},
]
FIT_PROMOS = [
    {"title": "Essai gratuit", "text": "1 séance offerte — HIIT, cycling ou yoga.", "href": "contact.html", "label": "Réserver", "accent": "lime"},
    {"title": "-20 % étudiants", "text": "Sur présentation de la carte — sans engagement.", "href": "tarifs.html", "label": "Voir tarifs", "accent": "dark"},
    {"title": "Parrainage", "text": "1 mois offert pour chaque ami inscrit.", "href": "contact.html", "label": "En profiter", "accent": "lime"},
]
FIT_PRICING = [
    {
        "title": "Abonnements",
        "items": [
            {"name": "Mensuel illimité", "desc": "Cours + musculation — sans engagement", "price": "49 €", "tags": ["Le + choisi"]},
            {"name": "Annuel", "desc": "12 mois — 2 mois offerts", "price": "490 €", "tags": ["-17 %"]},
            {"name": "Étudiant", "desc": "Sur carte — accès 6h–23h", "price": "39 €", "tags": ["-20 %"]},
        ],
    },
    {
        "title": "Carnets & options",
        "items": [
            {"name": "Carnet 10 séances", "desc": "Valable 3 mois — tous cours", "price": "120 €", "tags": []},
            {"name": "Coaching privé", "desc": "Séance 1h avec coach dédié", "price": "65 €", "tags": ["Sur RDV"]},
            {"name": "Pass journée", "desc": "Découverte musculation + 1 cours", "price": "15 €", "tags": ["Essai"]},
        ],
    },
]
FIT_FAQ = [
    ("Faut-il réserver les cours ?", "Les cours collectifs se réservent via l'app — places limitées. La musculation libre est en accès libre."),
    ("Y a-t-il un vestiaire ?", "Vestiaires hommes/femmes, douches et casiers sécurisés inclus dans l'abonnement."),
    ("Puis-je suspendre mon abonnement ?", "Oui — 1 mois de suspension par an sur justificatif (déménagement, blessure)."),
]


def _shell_fitness(page: str, title: str, desc: str, main: str) -> str:
    bar = block_info_bar(status="Ouvert 6h–23h · 7j/7", address=FIT_ADDRESS, phone=FIT_PHONE, maps_href=FIT_MAPS)
    nav = _chrome_nav("fitness", FIT_BRAND, FIT_NAV, page, cta_label="Essai gratuit", cta_href="contact.html")
    foot = _chrome_foot("fitness", 
        FIT_BRAND,
        phone=FIT_PHONE,
        address=FIT_ADDRESS,
        email=FIT_EMAIL,
        maps_href=FIT_MAPS,
        nav_links=FIT_FOOTER_NAV,
        hours_line="6h–23h · Metz Sablon",
    )
    mobile = block_mobile_cta("Essai gratuit", "contact.html", FIT_PHONE)
    return wrap_page_fitness(title, desc, bar + nav + main + foot + mobile, slug="fitness", page=page, site_name=FIT_BRAND, nav=FIT_NAV)


def build_fitness_index() -> str:
    main = "<main>"
    main += block_hero_overlay(
        "Dépassez vos limites",
        "Cross-training, cycling et yoga — 1 200 m², coachs certifiés, ouvert 6h–23h à Metz Sablon.",
        "hero.png",
        "Salle Pulse Fitness Metz",
        eyebrow="Metz · Sablon",
        primary_href="contact.html",
        primary_label="Séance découverte gratuite",
        secondary_href="cours.html",
        secondary_label="Voir les cours",
    )
    main += block_stats([("1 200 m²", "Surface"), ("45", "Cours / semaine"), ("6h–23h", "Ouverture"), ("8", "Coachs")])
    main += block_service_tiles("Disciplines phares", [
        {"title": "HIIT & Cross", "items": ["45 min tous niveaux", "Coach certifié", "Groupes limités"], "hot": True},
        {"title": "Cycling", "items": ["Studio 20 places", "Playlists live", "30 ou 50 min"], "hot": False},
        {"title": "Yoga Flow", "items": ["Matin & soir", "Mobilité", "Récupération active"], "hot": False},
    ])
    main += block_schedule_grid(
        "Planning de la semaine",
        "Réservez votre créneau via l'app — places limitées.",
        FIT_SCHEDULE_HEADERS,
        FIT_SCHEDULE_ROWS,
        quote="L'ambiance est incroyable, j'ai perdu 8 kg en 4 mois sans m'ennuyer.",
        quote_author="Julie, membre depuis 2024",
    )
    main += """<section class="vt-reveal py-5 text-center">
  <div class="container">
    <p class="vt-eyebrow">Essai</p>
    <h2 class="vt-section-title h3 mb-3">Une seance pour tester, sans engagement</h2>
    <p class="text-secondary mb-4">Choisis un cours, on te reserve une place - vestiaire et serviette inclus.</p>
    <button type="button" class="btn btn-vt-primary btn-lg" data-vt-dialog-open="essaiDialog">Reserver mon essai</button>
  </div>
</section>"""
    main += block_dialog_m3(
        dialog_id="essaiDialog",
        title="Essai gratuit",
        lead="Cours + creneau - confirmation sous 2 h (demo).",
        primary_label="Reserver",
        primary_href="contact.html",
        fields_html='<div class="mb-2"><label class="form-label small">Cours</label><select class="form-select"><option>HIIT</option><option>Cycling</option><option>Yoga</option><option>Musculation libre</option></select></div><div class="mb-2"><label class="form-label small">Quand</label><input type="datetime-local" class="form-control"></div><div class="mb-2"><label class="form-label small">Telephone</label><input class="form-control" type="tel"></div>',
    )
    main += block_snackbar_m3("Essai reserve (demo)")
    main += block_fab_menu_m3([
        {"label": "Essai", "dialog": "essaiDialog"},
        {"label": "Cours", "href": "cours.html"},
        {"label": "Tarifs", "href": "tarifs.html"},
    ], main_label="Actions salle")
    main += block_sticky_cta_m3("Pret a bouger ?", "Essai", "contact.html", dialog="essaiDialog")
    main += "</main>"
    return _shell_fitness(
        "index.html",
        f"{FIT_BRAND} — Salle de sport Metz",
        "Salle de sport à Metz : cours collectifs, musculation et coaching — essai gratuit.",
        main,
    )


def build_fitness_cours() -> str:
    main = "<main>"
    main += block_hero_split(
        "Cours collectifs",
        "HIIT, cycling et yoga — encadrés par des coachs certifiés, du débutant au confirmé.",
        "hero.png",
        "Cours Pulse Fitness Metz",
        eyebrow="Cours",
        primary_href="contact.html",
        primary_label="Essai gratuit",
        secondary_href="tarifs.html",
        secondary_label="Voir les tarifs",
    )
    main += block_cards_bs("Toutes les disciplines", FIT_CARDS)
    main += '<div id="planning" class="vt-anchor" aria-hidden="true"></div>'
    main += block_schedule_grid(
        "Planning hebdomadaire",
        "Les créneaux évoluent chaque trimestre — consultez l'app pour les dernières mises à jour.",
        FIT_SCHEDULE_HEADERS,
        FIT_SCHEDULE_ROWS,
    )
    main += block_chapters(FIT_CHAPTERS)
    main += block_funnel_steps("Votre première séance", [
        ("Réserver", "Choisissez un cours via le formulaire ou par téléphone."),
        ("Accueil", "Brief coach de 10 min — niveau et objectifs."),
        ("Séance", "Cours encadré ou musculation libre selon votre choix."),
        ("Bilan", "Devis personnalisé sans engagement à la fin."),
    ])
    main += block_cta_band("Réservez votre essai gratuit.", "Je réserve", "contact.html")
    main += "</main>"
    return _shell_fitness(
        "cours.html",
        f"Cours — {FIT_BRAND}",
        "Cours collectifs HIIT, cycling et yoga à Metz — Pulse Fitness.",
        main,
    )


def build_fitness_tarifs() -> str:
    main = "<main>"
    main += block_hero_proof_split(
        "Formules flexibles",
        lead="Sans engagement sur le mensuel — 2 mois offerts sur l'annuel.",
        eyebrow="Tarifs",
        quote="J'ai testé trois salles à Metz — Pulse est la seule où je me sens vraiment accompagnée.",
        quote_author="Marc",
        quote_role="Membre annuel",
        stats=[("49 €", "Mensuel"), ("490 €", "Annuel"), ("-20 %", "Étudiants"), ("15 €", "Pass jour")],
        primary_href="contact.html",
        primary_label="Essai gratuit",
        secondary_href="cours.html",
        secondary_label="Voir les cours",
    )
    main += block_menu_section(
        "Grille tarifaire",
        "Tous les abonnements incluent vestiaires, casiers et accès musculation libre.",
        FIT_PRICING,
    )
    main += block_specs_table(
        "Comparer les formules",
        [
            ("Cours collectifs", "Illimité (mensuel et annuel)"),
            ("Musculation libre", "Inclus"),
            ("Coaching privé", "Option — 1 séance offerte à l'annuel"),
            ("Engagement", "Aucun (mensuel) · 12 mois (annuel)"),
        ],
    )
    main += block_faq_accordion("Questions fréquentes", FIT_FAQ)
    main += block_promo_cards(FIT_PROMOS)
    main += block_cta_band("Essai gratuit — sans carte bancaire.", "Réserver", "contact.html")
    main += "</main>"
    return _shell_fitness(
        "tarifs.html",
        f"Tarifs — {FIT_BRAND}",
        "Tarifs salle de sport Metz — abonnements et carnets Pulse Fitness.",
        main,
    )


def build_fitness_contact() -> str:
    main = """<main>
<section class="vt-hero-compact py-5 text-center">
  <div class="container">
    <p class="vt-eyebrow text-uppercase">Contact</p>
    <h1 class="vt-display display-6">Essai gratuit</h1>
    <p class="lead text-secondary">Metz Sablon — réponse sous 24 h.</p>
  </div>
</section>"""
    main += block_fitness_trial_form(brand=FIT_BRAND, address=FIT_ADDRESS, phone=FIT_PHONE, email=FIT_EMAIL)
    main += block_cta_band("Démonstration — aucune donnée transmise.", "Retour accueil", "index.html")
    main += "</main>"
    return _shell_fitness(
        "contact.html",
        f"Contact — {FIT_BRAND}",
        "Contactez Pulse Fitness Metz — essai gratuit.",
        main,
    )


# --- Studio Lumière Grise (photographie) — layout M3 maquette (_maquettes-echantillons/images/photographie-m3.png) ---
PH_BRAND = "Studio Lumière Grise"
PH_PHONE = "03 87 21 45 60"
PH_EMAIL = "bonjour@lumiere-grise.fr"
PH_ADDRESS = "12 rue des Clercs, 57000 Metz"
PH_MAPS = "https://maps.google.com/?q=12+rue+des+Clercs+57000+Metz"
PH_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "portfolio.html", "label": "Portfolio"},
    {"file": "prestations.html", "label": "Prestations"},
    {"file": "contact.html", "label": "Contact"},
]
PH_FOOTER_NAV = [
    ("Portfolio", "portfolio.html"),
    ("Prestations", "prestations.html"),
    ("Devis", "contact.html"),
    ("Mariage", "portfolio.html"),
]
PH_MASONRY = [
    {"title": "Architecture", "text": "Volumes et lumière.", "img": "gallery-2.png", "alt": "Photo architecture"},
    {"title": "Mariage", "text": "Reportage documentaire.", "img": "scene-1.png", "alt": "Mariage documentaire"},
    {"title": "Produit", "text": "Nature morte éditoriale.", "img": "card-3.png", "alt": "Photo produit"},
    {"title": "Paysage", "text": "Grand Est.", "img": "hero.png", "alt": "Paysage"},
    {"title": "Corporate", "text": "Équipes et dirigeants.", "img": "card-1.png", "alt": "Portrait corporate"},
    {"title": "Événement", "text": "Séminaires et soirées.", "img": "card-2.png", "alt": "Événement"},
    {"title": "Table", "text": "Lifestyle.", "img": "scene-3.png", "alt": "Lifestyle"},
    {"title": "Couple", "text": "Golden hour.", "img": "gallery-1.png", "alt": "Couple"},
    {"title": "Studio", "text": "Noir et blanc.", "img": "scene-2.png", "alt": "Studio"},
]
PH_PROJECTS = [
    {"title": "Mariage Château des Lumières", "year": "2024", "specs": "Metz · reportage", "text": "Journée complète, 420 photos livrées.", "img": "gallery-1.png", "alt": "Mariage Metz", "badge": "Mariage"},
    {"title": "Portraits PME Grand Est", "year": "2024", "specs": "Corporate · 12 dirigeants", "text": "Série homogène pour site et LinkedIn.", "img": "scene-2.png", "alt": "Portrait corporate"},
    {"title": "Résidence contemporaine", "year": "2023", "specs": "Architecture · intérieur", "text": "Lumière zénithale et matériaux bruts.", "img": "gallery-2.png", "alt": "Architecture photo"},
    {"title": "Lookbook mode locale", "year": "2023", "specs": "Éditorial", "text": "Direction artistique et post-production.", "img": "card-3.png", "alt": "Éditorial mode", "badge": "Éditorial"},
    {"title": "Naissance & famille", "year": "2024", "specs": "Lifestyle · Metz", "text": "Séance à domicile, tons doux.", "img": "scene-3.png", "alt": "Photo famille"},
    {"title": "Événement corporate", "year": "2022", "specs": "Séminaire · 200 pers.", "text": "Reportage et portraits instantanés.", "img": "card-2.png", "alt": "Événement"},
]
PH_BENTO = [
    {"title": "Mariage", "text": "Reportage documentaire - Metz et Grand Est.", "img": "gallery-1.png", "alt": "Mariage", "size": "lg"},
    {"title": "Corporate", "text": "Portraits dirigeants et équipes.", "img": "scene-2.png", "alt": "Corporate"},
    {"title": "Éditorial", "text": "Direction artistique incluse.", "img": "card-3.png", "alt": "Éditorial"},
]
PH_CHAPTERS = [
    {"title": "Écoute & brief", "text": "Échange sur votre univers, vos références et vos contraintes.", "img": "scene-3.png", "alt": "Brief créatif"},
    {"title": "Shooting", "text": "Lumière naturelle ou studio - direction bienveillante.", "img": "scene-1.png", "alt": "Séance photo"},
    {"title": "Livraison", "text": "Galerie web privée, retouches et tirages sur demande.", "img": "scene-2.png", "alt": "Livraison photos"},
]
PH_CARDS = [
    {"title": "Portrait", "text": "Studio ou sur site - à partir de 350 €.", "img": "card-1.png", "alt": "Portrait"},
    {"title": "Mariage", "text": "Journée complète + album - sur devis.", "img": "card-2.png", "alt": "Mariage"},
    {"title": "Éditorial", "text": "Lookbook et direction artistique.", "img": "card-3.png", "alt": "Éditorial"},
]
PH_PRICING = [
    {
        "title": "Portraits & studio",
        "items": [
            {"name": "Portrait individuel", "desc": "Studio Metz - 1 tenue, 5 retouches", "price": "350 €", "tags": ["1 h"]},
            {"name": "Portrait équipe", "desc": "Jusqu'à 8 personnes - fond uni", "price": "690 €", "tags": ["Demi-journée"]},
            {"name": "Book artiste", "desc": "2 h studio + direction", "price": "520 €", "tags": []},
        ],
    },
    {
        "title": "Événements & mariage",
        "items": [
            {"name": "Mariage journée", "desc": "Préparatifs à soirée - galerie web", "price": "1 890 €", "tags": ["Grand Est"]},
            {"name": "Demi-journée événement", "desc": "Séminaire, inauguration, soirée", "price": "750 €", "tags": []},
            {"name": "Album premium", "desc": "30 pages - design inclus", "price": "390 €", "tags": ["Option"]},
        ],
    },
]
PH_FAQ = [
    ("Combien de photos sont livrées ?", "Mariage : 400 à 600 photos retouchées. Portrait : 15 à 25 selon la formule."),
    ("Vous déplacez-vous hors Metz ?", "Oui - Grand Est sans supplément jusqu'à 80 km, au-delà sur devis."),
    ("Délai de livraison ?", "Galerie web sous 10 jours ouvrés. Album sous 4 semaines."),
]
PH_CREDENTIALS = [
    ("240+", "mariages"),
    ("15 ans", "d'expérience"),
    ("Publications", "Les Inrocks, GEO"),
]


def _shell_photo(page: str, title: str, desc: str, main: str) -> str:
    nav = block_photo_m3_nav(
        PH_BRAND,
        city="Metz",
        chips=[
            {"label": "Mariage", "href": "prestations.html", "active": page == "prestations.html"},
            {"label": "Corporate", "href": "portfolio.html"},
        ],
        cta_label="Demander un devis",
        cta_href="contact.html",
    )
    foot = _chrome_foot(
        "photographie",
        PH_BRAND,
        phone=PH_PHONE,
        address=PH_ADDRESS,
        email=PH_EMAIL,
        maps_href=PH_MAPS,
        nav_links=PH_FOOTER_NAV,
        hours_line="Sur rendez-vous · Metz",
    )
    fab = block_plus_fab("contact.html", "Nouveau projet")
    mobile = block_mobile_cta("Devis", "contact.html", PH_PHONE)
    return wrap_page_photo(
        title,
        desc,
        nav + main + foot + fab + mobile,
        slug="photographie",
        page=page,
        site_name=PH_BRAND,
        nav=PH_NAV,
        layout="photo-m3",
    )


def build_photographie_index() -> str:
    main = "<main>"
    main += block_photo_m3_masonry(PH_MASONRY)
    main += block_photo_toast("Votre demande a bien été envoyée", close_href="contact.html")
    main += """<section class="vt-reveal py-5 vt-photo-brief">
  <div class="container">
    <div class="row g-4 align-items-center">
      <div class="col-lg-7">
        <p class="vt-eyebrow text-uppercase">Brief rapide</p>
        <h2 class="vt-section-title h3 mb-3">Mariage, portrait, corporate</h2>
        <p class="text-secondary mb-3">Tu coches ce dont tu as besoin - devis clair sous 24 h, galerie web sous 10 jours.</p>
        <button type="button" class="btn btn-vt-primary" data-vt-dialog-open="devisPhoto">Demander un devis</button>
      </div>
      <div class="col-lg-5">
        <div class="vt-photo-pack">
          <button type="button" class="vt-photo-pack-item" data-vt-dialog-open="devisPhoto"><strong>Mariage</strong><span>400-600 photos</span></button>
          <button type="button" class="vt-photo-pack-item" data-vt-dialog-open="devisPhoto"><strong>Portrait</strong><span>15-25 retouchees</span></button>
          <button type="button" class="vt-photo-pack-item" data-vt-dialog-open="devisPhoto"><strong>Corporate</strong><span>Direction homogene</span></button>
        </div>
      </div>
    </div>
  </div>
</section>"""
    main += block_dialog_m3(
        dialog_id="devisPhoto",
        title="Devis photo",
        lead="Date, type de projet, lieu - reponse sous 24 h (demo).",
        primary_label="Envoyer",
        primary_href="contact.html",
        fields_html='<div class="mb-2"><label class="form-label small">Projet</label><select class="form-select"><option>Mariage</option><option>Portrait</option><option>Corporate</option></select></div><div class="mb-2"><label class="form-label small">Date souhaitee</label><input type="date" class="form-control"></div><div class="mb-2"><label class="form-label small">Lieu</label><input class="form-control" placeholder="Metz, Nancy..."></div>',
    )
    main += block_fab_menu_m3([
        {"label": "Devis", "dialog": "devisPhoto"},
        {"label": "Portfolio", "href": "portfolio.html"},
        {"label": "Prestations", "href": "prestations.html"},
    ], main_label="Actions photo")
    main += "</main>"
    return _shell_photo(
        "index.html",
        f"{PH_BRAND} — Photographe Metz",
        "Photographe mariage et corporate à Metz : reportages et portraits.",
        main,
    )


def build_photographie_portfolio() -> str:
    main = "<main>"
    main += block_hero_editorial(
        "Portfolio",
        "Mariages, portraits et séries éditoriales — Nancy et Grand Est.",
        "hero.png",
        "Portfolio Studio Lumière Grise",
        eyebrow="Portfolio",
        primary_href="contact.html",
        primary_label="Demander un devis",
        secondary_href="prestations.html",
        secondary_label="Prestations",
    )
    main += block_project_grid("Réalisations", PH_PROJECTS)
    main += block_gallery_masonry("Séries en cours", PH_MASONRY)
    main += block_bento_cards(PH_BENTO)
    main += block_cta_band("Un projet similaire ?", "Nous contacter", "contact.html")
    main += "</main>"
    return _shell_photo(
        "portfolio.html",
        f"Portfolio — {PH_BRAND}",
        "Portfolio photographie Studio Lumière Grise — Nancy.",
        main,
    )


def build_photographie_prestations() -> str:
    main = "<main>"
    main += block_hero_proof_split(
        "Prestations sur mesure",
        lead="Devis transparent — livrables et délais précisés par écrit.",
        eyebrow="Prestations",
        quote="Julie et Marc ont su capter l'émotion de notre journée sans mise en scène forcée.",
        quote_author="Sophie & Thomas",
        quote_role="Mariage 2024 — Nancy",
        stats=[("350 €", "Portrait"), ("1 890 €", "Mariage"), ("10 j", "Livraison"), ("80 km", "Déplacement inclus")],
        primary_href="contact.html",
        primary_label="Demander un devis",
        secondary_href="portfolio.html",
        secondary_label="Voir le portfolio",
    )
    main += block_menu_section(
        "Tarifs indicatifs",
        "Chaque projet est unique — ce tarif sert de base pour votre devis personnalisé.",
        PH_PRICING,
    )
    main += block_funnel_steps("Parcours client", [
        ("Brief", "Échange visio ou café à Nancy — moodboard et planning."),
        ("Shooting", "Studio ou sur site — direction naturelle."),
        ("Sélection", "Galerie privée — vous choisissez vos favoris."),
        ("Livraison", "Fichiers HD, retouches et tirages optionnels."),
    ])
    main += block_faq_accordion("Questions fréquentes", PH_FAQ)
    main += block_cta_band("Prêt à réserver votre date ?", "Demander un devis", "contact.html")
    main += "</main>"
    return _shell_photo(
        "prestations.html",
        f"Prestations — {PH_BRAND}",
        "Prestations photo Nancy — portrait, mariage, corporate.",
        main,
    )


def build_photographie_contact() -> str:
    main = """<main>
<section class="vt-hero-compact py-5 text-center">
  <div class="container">
    <p class="vt-eyebrow text-uppercase">Contact</p>
    <h1 class="vt-display display-6">Demande de devis</h1>
    <p class="lead text-secondary">Nancy — réponse sous 24 h.</p>
  </div>
</section>"""
    main += block_photo_quote_form(brand=PH_BRAND, address=PH_ADDRESS, phone=PH_PHONE, email=PH_EMAIL)
    main += block_cta_band("Démonstration — aucune donnée transmise.", "Retour accueil", "index.html")
    main += "</main>"
    return _shell_photo(
        "contact.html",
        f"Contact — {PH_BRAND}",
        "Contactez Studio Lumière Grise à Nancy.",
        main,
    )


# --- Solidarités Metz Métropole (association) — hero vert + jauge impact + mobilisation ---
ASS_BRAND = "Solidarités Metz Métropole"
ASS_PHONE = "03 87 34 56 78"
ASS_EMAIL = "contact@solidarites-metz.fr"
ASS_ADDRESS = "22 rue du Sablon, 57000 Metz"
ASS_MAPS = "https://maps.google.com/?q=22+rue+du+Sablon+57000+Metz"
ASS_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "actions.html", "label": "Nos actions"},
    {"file": "benevolat.html", "label": "Bénévolat"},
    {"file": "contact.html", "label": "Contact"},
]
ASS_FOOTER_NAV = [
    ("Nos actions", "actions.html"),
    ("Bénévolat", "benevolat.html"),
    ("Faire un don", "contact.html"),
    ("Transparence", "actions.html"),
]
ASS_CARDS = [
    {"title": "Aide alimentaire", "text": "Épicerie solidaire et paniers hebdomadaires à prix modiques.", "img": "scene-1.png", "alt": "Épicerie solidaire"},
    {"title": "Insertion emploi", "text": "Ateliers CV, stages et mise en relation avec les employeurs.", "img": "scene-2.png", "alt": "Insertion"},
    {"title": "Accompagnement social", "text": "Permanences juridiques, logement et accès aux droits.", "img": "scene-3.png", "alt": "Accompagnement"},
]
ASS_CHAPTERS = [
    {"title": "Épicerie solidaire", "text": "3 200 familles accompagnées — paniers adaptés et accueil bienveillant.", "img": "scene-1.png", "alt": "Épicerie"},
    {"title": "Insertion professionnelle", "text": "Parcours sur 3 à 6 mois — 68 % de retour à l'emploi en 2024.", "img": "scene-2.png", "alt": "Insertion"},
    {"title": "Lien social", "text": "Fêtes de quartier, cuisine partagée et maraudes hivernales.", "img": "gallery-1.png", "alt": "Quartier"},
]
ASS_VOLUNTEER = [
    {"title": "Maraude", "text": "2 h par mois — accompagnement rue et nuit d'hiver.", "img": "card-1.png", "alt": "Maraude"},
    {"title": "Collecte alimentaire", "text": "Samedis ponctuels — en magasin ou en entrepôt.", "img": "card-2.png", "alt": "Collecte"},
    {"title": "Mentor numérique", "text": "Aide aux démarches en ligne — formation 1 journée.", "img": "card-3.png", "alt": "Numérique"},
]
ASS_NARRATIVE = [
    {"stat": "3 200", "stat_label": "Familles aidées", "title": "Aide alimentaire", "text": "Paniers alimentaires et accompagnement social chaque année en Moselle.", "img": "scene-1.png", "alt": "Familles"},
    {"stat": "68 %", "stat_label": "Retour emploi", "title": "Insertion", "text": "Taux de sortie positive des parcours insertion en 2024.", "img": "scene-2.png", "alt": "Emploi"},
    {"stat": "120", "stat_label": "Bénévoles actifs", "title": "Engagement citoyen", "text": "Citoyens engagés — 2 h par mois en moyenne suffisent.", "img": "gallery-2.png", "alt": "Bénévoles"},
]
ASS_FAQ = [
    ("Comment devenir bénévole ?", "Remplissez le formulaire — entretien de 30 min et formation d'accueil incluse."),
    ("Mon don est-il déductible ?", "Oui — 66 % pour les particuliers, reçu fiscal envoyé par e-mail."),
    ("Puis-je aider ponctuellement ?", "Oui — collectes alimentaires, événements et maraudes ponctuelles."),
]


def _shell_association(page: str, title: str, desc: str, main: str) -> str:
    bar = block_info_bar(status="Permanences lun–ven 9h–17h", address=ASS_ADDRESS, phone=ASS_PHONE, maps_href=ASS_MAPS)
    nav = _chrome_nav("association", ASS_BRAND, ASS_NAV, page, cta_label="Faire un don", cta_href="contact.html")
    foot = _chrome_foot("association", 
        ASS_BRAND,
        phone=ASS_PHONE,
        address=ASS_ADDRESS,
        email=ASS_EMAIL,
        maps_href=ASS_MAPS,
        nav_links=ASS_FOOTER_NAV,
        hours_line="Metz Métropole · ESS",
    )
    mobile = block_mobile_cta("Faire un don", "contact.html", ASS_PHONE)
    return wrap_page_association(title, desc, bar + nav + main + foot + mobile, slug="association", page=page, site_name=ASS_BRAND, nav=ASS_NAV)


def build_association_index() -> str:
    main = "<main>"
    main += """<section class="vt-asso-hero vt-reveal">
  <div class="container">
    <div class="row g-4 g-xl-5 align-items-center">
      <div class="col-lg-6">
        <p class="vt-eyebrow mb-2">ESS · Metz Metropole</p>
        <h1 class="vt-display display-4 mb-3">Agir pres de chez toi</h1>
        <p class="lead mb-4">Aide alimentaire, insertion et accompagnement - une solidarite ancree en Moselle.</p>
        <div class="d-flex flex-wrap gap-2">
          <button type="button" class="btn btn-vt-primary btn-lg" data-vt-dialog-open="donDialog">Faire un don</button>
          <a class="btn btn-vt-outline btn-lg" href="benevolat.html">Devenir benevole</a>
        </div>
      </div>
      <div class="col-lg-6">
        <figure class="vt-asso-hero-media mb-0">
          <picture><source srcset="images/hero.webp" type="image/webp"><img src="images/hero.png" alt="Benevoles a Metz" decoding="async" fetchpriority="high"></picture>
        </figure>
      </div>
    </div>
  </div>
</section>"""
    main += """<section class="vt-reveal py-4">
  <div class="container">
    <div class="row g-3">
      <div class="col-6 col-lg-3"><article class="vt-asso-stat"><strong>3 200+</strong><span>Familles aidees</span></article></div>
      <div class="col-6 col-lg-3"><article class="vt-asso-stat"><strong>120</strong><span>Benevoles</span></article></div>
      <div class="col-6 col-lg-3"><article class="vt-asso-stat"><strong>12</strong><span>Communes</span></article></div>
      <div class="col-6 col-lg-3"><article class="vt-asso-stat"><strong>68 %</strong><span>Retour emploi</span></article></div>
    </div>
  </div>
</section>"""
    main += block_impact_goal(
        "Campagne 2026",
        "18 400 €",
        "25 500 €",
        72,
        "72 % de l'objectif - merci a nos 340 donateurs",
    )
    main += block_dialog_m3(
        dialog_id="donDialog",
        title="Faire un don",
        lead="Montant libre - recu fiscal sous 48 h (demo).",
        primary_label="Continuer",
        primary_href="contact.html",
        fields_html='<div class="mb-2"><label class="form-label small">Montant</label><select class="form-select"><option>20 euro</option><option>50 euro</option><option>100 euro</option><option>Autre</option></select></div><div class="mb-2"><label class="form-label small">Email</label><input class="form-control" type="email"></div>',
    )
    main += block_fab_menu_m3([
        {"label": "Donner", "dialog": "donDialog"},
        {"label": "Actions", "href": "actions.html"},
        {"label": "Benevolat", "href": "benevolat.html"},
    ], main_label="Actions asso")
    main += block_sticky_cta_m3("Ton don finance un panier cette semaine", "Donner", "contact.html", dialog="donDialog")
    main += "</main>"
    return _shell_association(
        "index.html",
        f"{ASS_BRAND} — Association Metz",
        "Association d'utilité publique à Metz : aide alimentaire, insertion et bénévolat.",
        main,
    )


def build_association_actions() -> str:
    main = "<main>"
    main += block_hero_split(
        "Nos actions sur le terrain",
        "Épicerie solidaire, insertion et accompagnement — des réponses concrètes en Moselle.",
        "hero.png",
        "Actions Solidarités Metz",
        eyebrow="Nos actions",
        primary_href="contact.html",
        primary_label="Soutenir",
        secondary_href="benevolat.html",
        secondary_label="Bénévolat",
    )
    main += block_compact_features([
        {"title": "Épicerie solidaire", "text": "80 familles/jour — produits frais et hygiène.", "img": "scene-1.png", "alt": "Épicerie"},
        {"title": "Ateliers emploi", "text": "CV, entretien et simulation — chaque mardi.", "img": "scene-2.png", "alt": "Emploi"},
        {"title": "Permanences droits", "text": "Logement, CAF, santé — sur rendez-vous.", "img": "scene-3.png", "alt": "Droits"},
    ])
    main += block_stat_narrative_rows(ASS_NARRATIVE)
    main += block_timeline([
        ("2010", "Création de l'association à Metz."),
        ("2016", "Ouverture de l'épicerie solidaire du Sablon."),
        ("2020", "Label ESS régional et 100 bénévoles."),
        ("2024", "3 200 familles accompagnées — extension Thionville."),
    ])
    main += block_gallery_masonry("Sur le terrain", [
        {"title": "Fête de quartier", "text": "800 participants — juin 2024.", "img": "gallery-1.png", "alt": "Fête"},
        {"title": "Cuisine solidaire", "text": "200 repas partagés chaque semaine.", "img": "gallery-2.png", "alt": "Cuisine"},
        {"title": "Maraude hivernale", "text": "150 nuitées d'accueil d'urgence.", "img": "card-1.png", "alt": "Maraude"},
    ])
    main += block_cta_band("Soutenez nos actions.", "Faire un don", "contact.html")
    main += "</main>"
    return _shell_association(
        "actions.html",
        f"Nos actions — {ASS_BRAND}",
        "Actions solidarité Metz — aide alimentaire, insertion, accompagnement.",
        main,
    )


def build_association_benevolat() -> str:
    main = "<main>"
    main += block_hero_editorial(
        "Rejoignez nos bénévoles",
        "120 citoyens engagés — 2 h par mois suffisent pour faire la différence.",
        "hero.png",
        "Bénévolat Solidarités Metz",
        eyebrow="Bénévolat",
        primary_href="contact.html",
        primary_label="Je candidate",
        secondary_href="actions.html",
        secondary_label="Nos actions",
    )
    main += block_cards_bs("Missions disponibles", ASS_VOLUNTEER)
    main += block_funnel_steps("Votre parcours bénévole", [
        ("Candidature", "Formulaire en ligne — 5 minutes."),
        ("Entretien", "Échange de 30 min avec un référent."),
        ("Formation", "Accueil et posture d'écoute — 1/2 journée."),
        ("Mission", "Créneaux adaptés à votre disponibilité."),
    ])
    main += block_faq_accordion("Questions bénévoles", ASS_FAQ)
    main += block_chapters(ASS_CHAPTERS)
    main += block_cta_band("Prêt à vous engager ?", "Je m'inscris", "contact.html")
    main += "</main>"
    return _shell_association(
        "benevolat.html",
        f"Bénévolat — {ASS_BRAND}",
        "Devenir bénévole à Metz — Solidarités Metz Métropole.",
        main,
    )


def build_association_contact() -> str:
    main = """<main>
<section class="vt-hero-compact py-5 text-center">
  <div class="container">
    <p class="vt-eyebrow text-uppercase">Contact</p>
    <h1 class="vt-display display-6">Don ou bénévolat</h1>
    <p class="lead text-secondary">Metz — réponse sous 48 h.</p>
  </div>
</section>"""
    main += block_association_contact_form(brand=ASS_BRAND, address=ASS_ADDRESS, phone=ASS_PHONE, email=ASS_EMAIL)
    main += block_cta_band("Démonstration — aucune donnée transmise.", "Retour accueil", "index.html")
    main += "</main>"
    return _shell_association(
        "contact.html",
        f"Contact — {ASS_BRAND}",
        "Contactez Solidarités Metz Métropole — don et bénévolat.",
        main,
    )


# --- Institut Mercure (education) — hero technique académique + Qualiopi + parcours ---
EDU_BRAND = "Institut Mercure"
EDU_PHONE = "03 82 88 45 00"
EDU_EMAIL = "contact@institut-mercure.fr"
EDU_ADDRESS = "15 avenue des Deux Fontaines, 57100 Thionville"
EDU_MAPS = "https://maps.google.com/?q=15+avenue+des+Deux+Fontaines+57100+Thionville"
EDU_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "parcours.html", "label": "Parcours"},
    {"file": "campus.html", "label": "Campus"},
    {"file": "contact.html", "label": "Contact"},
]
EDU_FOOTER_NAV = [
    ("Parcours", "parcours.html"),
    ("Campus", "campus.html"),
    ("S'inscrire", "contact.html"),
    ("Qualiopi", "campus.html"),
]
EDU_CARDS = [
    {"title": "Digital & web", "text": "Développeur web en alternance — RNCP niveau 5, 12 mois.", "img": "card-1.png", "alt": "Formation digital"},
    {"title": "Management", "text": "BTS Management et titres pro — leadership et gestion d'équipe.", "img": "card-2.png", "alt": "Formation management"},
    {"title": "Métiers techniques", "text": "Comptabilité, SST et reconversion — financement CPF/OPCO.", "img": "card-3.png", "alt": "Formation technique"},
]
EDU_CHAPTERS = [
    {"title": "Pédagogie active", "text": "Ateliers, projets réels et alternance en entreprise dès le 1er trimestre.", "img": "scene-1.png", "alt": "Salle de cours"},
    {"title": "Insertion professionnelle", "text": "92 % des diplômés en emploi à 6 mois — réseau de 180 partenaires.", "img": "scene-2.png", "alt": "Atelier pratique"},
    {"title": "Accompagnement individuel", "text": "Référent pédagogique, bilan de compétences et VAE sur demande.", "img": "scene-3.png", "alt": "Coaching apprenant"},
]
EDU_NARRATIVE = [
    {"stat": "1 200", "stat_label": "Apprenants/an", "title": "Volume d'activité", "text": "Formations initiales, continues et alternance sur le campus Thionville.", "img": "gallery-1.png", "alt": "Campus"},
    {"stat": "35", "stat_label": "Parcours", "title": "Offre certifiante", "text": "Titres pro, BTS et certificats métiers — digital, gestion et technique.", "img": "gallery-2.png", "alt": "Parcours"},
    {"stat": "92 %", "stat_label": "Insertion", "title": "Résultats emploi", "text": "Taux d'insertion à 6 mois — suivi alumni et job dating trimestriel.", "img": "scene-2.png", "alt": "Insertion"},
]
EDU_PROGRAMS_MENU = [
    {
        "title": "Digital & numérique",
        "items": [
            {"name": "Développeur web", "desc": "Alternance 12 mois — RNCP niveau 5", "price": "CPF / OPCO", "tags": ["Alternance"]},
            {"name": "Marketing digital", "desc": "SEO, réseaux sociaux, e-commerce", "price": "6 mois", "tags": ["Certifiant"]},
            {"name": "Cybersécurité", "desc": "Sensibilisation et fondamentaux", "price": "3 mois", "tags": ["Nouveau"]},
        ],
    },
    {
        "title": "Management & gestion",
        "items": [
            {"name": "BTS Management", "desc": "Commerce opérationnel — 2 ans", "price": "Alternance", "tags": ["BTS"]},
            {"name": "Titre pro RPE", "desc": "Responsable petite entreprise", "price": "18 mois", "tags": ["Titre pro"]},
            {"name": "Gestion de projet", "desc": "Certification courte — 4 mois", "price": "CPF", "tags": []},
        ],
    },
    {
        "title": "Technique & reconversion",
        "items": [
            {"name": "Comptabilité", "desc": "Titre pro assistant comptable", "price": "12 mois", "tags": ["Titre pro"]},
            {"name": "SST initiale", "desc": "Sauveteur secouriste du travail", "price": "3 jours", "tags": ["Express"]},
            {"name": "VAE / bilan", "desc": "Validation des acquis professionnels", "price": "sur devis", "tags": []},
        ],
    },
]
EDU_FAQ = [
    ("Quels financements acceptez-vous ?", "CPF, Pôle emploi, OPCO, Région Grand Est — nous montons le dossier avec vous."),
    ("L'alternance est-elle obligatoire ?", "Non — certains parcours sont en formation continue ou à temps plein."),
    ("Le diplôme est-il reconnu ?", "Oui — titres RNCP, BTS et certifications inscrites au Répertoire national."),
]


def _shell_education(page: str, title: str, desc: str, main: str) -> str:
    bar = block_info_bar(status="Inscriptions ouvertes — rentrée sept. 2026", address=EDU_ADDRESS, phone=EDU_PHONE, maps_href=EDU_MAPS)
    nav = _chrome_nav("education", EDU_BRAND, EDU_NAV, page, cta_label="S'inscrire", cta_href="contact.html")
    foot = _chrome_foot("education", 
        EDU_BRAND,
        phone=EDU_PHONE,
        address=EDU_ADDRESS,
        email=EDU_EMAIL,
        maps_href=EDU_MAPS,
        nav_links=EDU_FOOTER_NAV,
        hours_line="Thionville · Certifié Qualiopi",
    )
    mobile = block_mobile_cta("S'inscrire", "contact.html", EDU_PHONE)
    return wrap_page_education(title, desc, bar + nav + main + foot + mobile, slug="education", page=page, site_name=EDU_BRAND, nav=EDU_NAV)


def build_education_index() -> str:
    main = "<main>"
    main += """<section class="vt-edu-hero vt-reveal">
  <div class="container">
    <div class="row g-4 g-xl-5 align-items-center">
      <div class="col-lg-6">
        <p class="vt-eyebrow mb-2">Formation · Grand Est</p>
        <h1 class="vt-display display-4 mb-3">Competences metiers a Thionville</h1>
        <p class="lead mb-3">Alternance, reconversion et titres reconnus - un campus clair, un accompagnement concret.</p>
        <div class="d-flex flex-wrap gap-2 mb-4">
          <button type="button" class="vt-chip on">Digital</button>
          <button type="button" class="vt-chip">Management</button>
          <button type="button" class="vt-chip">Technique</button>
        </div>
        <div class="d-flex flex-wrap gap-2">
          <button type="button" class="btn btn-vt-primary btn-lg" data-vt-dialog-open="inscEdu">S'inscrire</button>
          <a class="btn btn-vt-outline btn-lg" href="parcours.html">Voir les parcours</a>
        </div>
      </div>
      <div class="col-lg-6">
        <figure class="vt-edu-hero-media mb-0">
          <picture><source srcset="images/hero.webp" type="image/webp"><img src="images/hero.png" alt="Campus Institut Mercure" decoding="async" fetchpriority="high"></picture>
        </figure>
      </div>
    </div>
  </div>
</section>"""
    main += """<section class="vt-reveal py-5">
  <div class="container">
    <p class="vt-eyebrow">Formations phares</p>
    <h2 class="vt-section-title h3 mb-4">Des parcours utiles, avec duree et prix clairs</h2>
    <div class="row g-3 vt-reveal-stagger">
      <div class="col-md-4"><article class="vt-course-card"><picture><source srcset="images/card-1.webp" type="image/webp"><img src="images/card-1.png" alt="Developpeur web" loading="lazy"></picture><div class="vt-course-card-body"><h3 class="h6 mb-2">Developpeur web</h3><p class="small text-secondary mb-3">Alternance 12 mois - titre RNCP.</p><div class="vt-course-meta"><span>12 mois</span><strong>CPF</strong></div></div></article></div>
      <div class="col-md-4"><article class="vt-course-card"><picture><source srcset="images/card-2.webp" type="image/webp"><img src="images/card-2.png" alt="BTS Management" loading="lazy"></picture><div class="vt-course-card-body"><h3 class="h6 mb-2">BTS Management</h3><p class="small text-secondary mb-3">2 ans - entreprise partenaire.</p><div class="vt-course-meta"><span>24 mois</span><strong>OPCO</strong></div></div></article></div>
      <div class="col-md-4"><article class="vt-course-card"><picture><source srcset="images/card-3.webp" type="image/webp"><img src="images/card-3.png" alt="Comptabilite" loading="lazy"></picture><div class="vt-course-card-body"><h3 class="h6 mb-2">Comptabilite</h3><p class="small text-secondary mb-3">Titre pro - reconversion ciblee.</p><div class="vt-course-meta"><span>9 mois</span><strong>des 4 900 euro</strong></div></div></article></div>
    </div>
  </div>
</section>"""
    main += block_dialog_m3(
        dialog_id="inscEdu",
        title="Demande d'inscription",
        lead="Orientation gratuite - on te rappelle sous 48 h (demo).",
        primary_label="Envoyer",
        primary_href="contact.html",
        fields_html='<div class="mb-2"><label class="form-label small">Parcours</label><select class="form-select"><option>Digital</option><option>Management</option><option>Technique</option></select></div><div class="mb-2"><label class="form-label small">Telephone</label><input class="form-control" type="tel"></div>',
    )
    main += block_fab_menu_m3([
        {"label": "S'inscrire", "dialog": "inscEdu"},
        {"label": "Parcours", "href": "parcours.html"},
        {"label": "Campus", "href": "campus.html"},
    ], main_label="Actions campus")
    main += "</main>"
    return _shell_education(
        "index.html",
        f"{EDU_BRAND} — Formation Thionville",
        "Centre de formation professionnelle à Thionville : alternance et reconversion.",
        main,
    )


def build_education_parcours() -> str:
    main = "<main>"
    main += block_hero_split(
        "35 parcours certifiants",
        "Digital, management et technique — du titre pro au BTS, en alternance ou formation continue.",
        "hero.png",
        "Parcours Institut Mercure",
        eyebrow="Nos parcours",
        primary_href="contact.html",
        primary_label="Demande d'inscription",
        secondary_href="campus.html",
        secondary_label="Le campus",
    )
    main += block_menu_section(
        "Catalogue formations 2026",
        "Tarifs indicatifs — devis personnalisé après entretien d'orientation gratuit.",
        EDU_PROGRAMS_MENU,
    )
    main += block_stat_narrative_rows(EDU_NARRATIVE)
    main += block_specs_table("Critères de nos diplômes", [
        ("Reconnaissance", "Titres RNCP, BTS, certifications métiers"),
        ("Durée", "De 3 jours (SST) à 24 mois (BTS)"),
        ("Modalité", "Présentiel, alternance ou blended"),
        ("Financement", "CPF, Pôle emploi, OPCO, Région"),
        ("Suivi", "Référent pédagogique dédié"),
        ("Insertion", "92 % en emploi à 6 mois"),
    ])
    main += block_chapters(EDU_CHAPTERS)
    main += block_cta_band("Une question sur cette offre ?", "Nous contacter", "contact.html")
    main += "</main>"
    return _shell_education(
        "parcours.html",
        f"Parcours — {EDU_BRAND}",
        "Parcours de formation professionnelle à Thionville — Institut Mercure.",
        main,
    )


def build_education_campus() -> str:
    main = "<main>"
    main += block_hero_editorial(
        "Un campus pensé pour réussir",
        "2 400 m² à Thionville — salles équipées, fab lab et espaces coworking pour les apprenants.",
        "hero.png",
        "Campus Institut Mercure",
        eyebrow="Campus Thionville",
        primary_href="contact.html",
        primary_label="Visite guidée",
        secondary_href="parcours.html",
        secondary_label="Nos parcours",
    )
    main += block_stats([("2 400 m²", "Surface"), ("12", "Salles"), ("180", "Entreprises"), ("15 ans", "Expérience")])
    main += block_sector_strip([
        ("Thionville", "Campus principal"),
        ("Metz", "Antenne alternance"),
        ("Luxembourg", "Partenariats transfrontaliers"),
        ("Grand Est", "Réseau régional"),
    ])
    main += block_timeline([
        ("2010", "Création de l'Institut Mercure à Thionville."),
        ("2016", "Extension des locaux et ouverture du fab lab."),
        ("2020", "Certification Qualiopi et partenariats OPCO."),
        ("2024", "1 200 apprenants formés — campus 2 400 m²."),
    ])
    main += block_compact_features([
        {"title": "Salles connectées", "text": "Vidéoprojecteurs, labs code et logiciels métiers.", "img": "scene-1.png", "alt": "Salle de cours"},
        {"title": "Espace entreprise", "text": "Job dating trimestriel et ateliers recruteurs.", "img": "scene-2.png", "alt": "Job dating"},
        {"title": "Vie étudiante", "text": "Coworking, café et permanences pédagogiques.", "img": "scene-3.png", "alt": "Coworking"},
    ])
    main += block_faq_accordion("Questions fréquentes", EDU_FAQ)
    main += block_gallery_masonry("Le campus en images", [
        {"title": "Cours en action", "text": "Ateliers pratiques et projets tutorés.", "img": "gallery-1.png", "alt": "Cours"},
        {"title": "Locaux modernes", "text": "Espaces lumineux rénovés en 2022.", "img": "gallery-2.png", "alt": "Locaux"},
        {"title": "Alternance", "text": "180 entreprises partenaires en Moselle.", "img": "card-1.png", "alt": "Alternance"},
    ])
    main += block_cta_band("Visitez le campus à Thionville.", "Prendre RDV", "contact.html")
    main += "</main>"
    return _shell_education(
        "campus.html",
        f"Campus — {EDU_BRAND}",
        "Campus de formation à Thionville — locaux, équipements et vie étudiante.",
        main,
    )


def build_education_contact() -> str:
    main = """<main>
<section class="vt-hero-compact py-5 text-center">
  <div class="container">
    <p class="vt-eyebrow text-uppercase">Contact</p>
    <h1 class="vt-display display-6">Inscription & orientation</h1>
    <p class="lead text-secondary">Thionville — réponse sous 48 h ouvrées.</p>
  </div>
</section>"""
    main += block_education_enrollment_form(brand=EDU_BRAND, address=EDU_ADDRESS, phone=EDU_PHONE, email=EDU_EMAIL)
    main += block_cta_band("Démonstration — aucune donnée transmise.", "Retour accueil", "index.html")
    main += "</main>"
    return _shell_education(
        "contact.html",
        f"Contact — {EDU_BRAND}",
        "Inscription et orientation — Institut Mercure Thionville.",
        main,
    )


# --- Proprio Facility (services) — hero overlay teal + bento FM + offres promo ---
SV_BRAND = "Proprio Facility"
SV_PHONE = "03 87 65 43 21"
SV_EMAIL = "contact@proprio-facility.fr"
SV_ADDRESS = "8 place Saint-Jacques, 57000 Metz"
SV_MAPS = "https://maps.google.com/?q=8+place+Saint-Jacques+57000+Metz"
SV_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "offres.html", "label": "Offres"},
    {"file": "secteurs.html", "label": "Secteurs"},
    {"file": "contact.html", "label": "Contact"},
]
SV_FOOTER_NAV = [
    ("Offres", "offres.html"),
    ("Secteurs", "secteurs.html"),
    ("Demander un devis", "contact.html"),
    ("ISO 9001", "offres.html"),
]
SV_CARDS = [
    {"title": "Maintenance technique", "text": "CVC, électricité, plomberie — GMAO et astreinte 24/7.", "img": "card-1.png", "alt": "Maintenance immeuble"},
    {"title": "Accueil & standard", "text": "Réception, courrier, gestion visiteurs et badgeuse.", "img": "card-2.png", "alt": "Accueil tertiaire"},
    {"title": "Conciergerie", "text": "Services occupants : réservations, événements, reprographie.", "img": "card-3.png", "alt": "Conciergerie"},
]
SV_BENTO = [
    {"title": "Exploitation multi-sites", "text": "200+ immeubles gérés en Moselle et Meurthe-et-Moselle — reporting unifié.", "img": "gallery-1.png", "alt": "Portefeuille FM", "size": "lg"},
    {"title": "Astreinte 24/7", "text": "Intervention sous 2 h sur panne critique.", "img": "scene-2.png", "alt": "Astreinte", "size": "sm"},
    {"title": "ISO 9001", "text": "Processus certifiés et audits trimestriels.", "img": "scene-3.png", "alt": "Qualité", "size": "sm"},
]
SV_CHAPTERS = [
    {"title": "Audit & cahier des charges", "text": "Visite sur site, cartographie des besoins et SLA négociés.", "img": "scene-1.png", "alt": "Audit FM"},
    {"title": "Exploitation quotidienne", "text": "Équipes dédiées, GMAO et tableaux de bord temps réel.", "img": "scene-2.png", "alt": "Exploitation"},
    {"title": "Reporting & amélioration", "text": "Bilan mensuel, indicateurs KPI et plan d'actions.", "img": "scene-3.png", "alt": "Reporting"},
]
SV_NARRATIVE = [
    {"stat": "200+", "stat_label": "Sites gérés", "title": "Portefeuille Grand Est", "text": "Bureaux, retail et santé — de 500 à 45 000 m² par site.", "img": "gallery-1.png", "alt": "Sites"},
    {"stat": "24/7", "stat_label": "Astreinte", "title": "Réactivité garantie", "text": "Centre d'appels interne — intervention critique sous 2 h.", "img": "scene-2.png", "alt": "Astreinte"},
    {"stat": "98 %", "stat_label": "SLA tenus", "title": "Qualité de service", "text": "Taux de conformité aux engagements contractuels en 2025.", "img": "gallery-2.png", "alt": "SLA"},
]
SV_OFFERS_MENU = [
    {
        "title": "Maintenance & technique",
        "items": [
            {"name": "Essentiel CVC", "desc": "Préventif + curatif — GMAO incluse", "price": "dès 2,80 €/m²", "tags": ["Bureaux"]},
            {"name": "Premium intégré", "desc": "Multi-technique + astreinte 24/7", "price": "sur devis", "tags": ["24/7"]},
            {"name": "Audit énergétique", "desc": "Diagnostic et plan de décarbonation", "price": "forfait", "tags": []},
        ],
    },
    {
        "title": "Services occupants",
        "items": [
            {"name": "Accueil standard", "desc": "Réception lun–ven 8h–19h", "price": "dès 4 200 €/mois", "tags": ["Accueil"]},
            {"name": "Conciergerie+", "desc": "Services premium et événementiel", "price": "sur devis", "tags": ["Premium"]},
            {"name": "Nettoyage tertiaire", "desc": "Plans de nettoyage certifiés", "price": "dès 1,90 €/m²", "tags": []},
        ],
    },
    {
        "title": "Pilotage FM",
        "items": [
            {"name": "Reporting KPI", "desc": "Tableau de bord mensuel digital", "price": "inclus Premium", "tags": ["Digital"]},
            {"name": "Multi-sites", "desc": "Coordination régionale unifiée", "price": "sur devis", "tags": ["200+ sites"]},
            {"name": "Transition écologique", "desc": "ISO 14001 et achats responsables", "price": "accompagnement", "tags": []},
        ],
    },
]
SV_FAQ = [
    ("Intervenez-vous sur des sites multi-bâtiments ?", "Oui — coordination centrale à Metz et équipes locales par site."),
    ("Quel délai pour un devis ?", "Audit sous 10 jours, proposition détaillée sous 5 jours ouvrés après visite."),
    ("Proposez-vous une astreinte week-end ?", "Oui — formule Premium avec astreinte 24/7 incluse."),
]
SV_PROMOS = [
    {"title": "Essentiel", "text": "Maintenance préventive et curative — idéal pour immeubles < 5 000 m².", "href": "contact.html", "label": "Demander un devis", "accent": "teal"},
    {"title": "Premium", "text": "FM intégré : technique, accueil, conciergerie et reporting KPI.", "href": "contact.html", "label": "Nous contacter", "accent": "slate"},
    {"title": "Sur mesure", "text": "Portefeuille multi-sites, SLA personnalisés et transition écologique.", "href": "contact.html", "label": "Parler à un expert", "accent": "cyan"},
]


def _shell_services(page: str, title: str, desc: str, main: str) -> str:
    bar = block_info_bar(status="Astreinte 24/7 · Grand Est", address=SV_ADDRESS, phone=SV_PHONE, maps_href=SV_MAPS)
    nav = _chrome_nav("services", SV_BRAND, SV_NAV, page, cta_label="Demander un devis", cta_href="contact.html")
    foot = _chrome_foot("services", 
        SV_BRAND,
        phone=SV_PHONE,
        address=SV_ADDRESS,
        email=SV_EMAIL,
        maps_href=SV_MAPS,
        nav_links=SV_FOOTER_NAV,
        hours_line="Metz · Facility management",
    )
    mobile = block_mobile_cta("Devis FM", "contact.html", SV_PHONE)
    return wrap_page_facility(title, desc, bar + nav + main + foot + mobile, slug="services", page=page, site_name=SV_BRAND, nav=SV_NAV)


def build_services_index() -> str:
    main = "<main>"
    main += """<section class="vt-svc-hero vt-reveal">
  <div class="container">
    <div class="row g-4 g-xl-5 align-items-center">
      <div class="col-lg-6">
        <p class="vt-eyebrow mb-2">FM · Metz &amp; Grand Est</p>
        <h1 class="vt-display display-4 mb-3">Un site qui tourne, sans friction</h1>
        <p class="lead mb-4">Maintenance, accueil et conciergerie - un interlocuteur unique pour tes immeubles tertiaires.</p>
        <div class="d-flex flex-wrap gap-2">
          <button type="button" class="btn btn-vt-primary btn-lg" data-vt-dialog-open="devisFm">Demander un devis</button>
          <a class="btn btn-vt-outline btn-lg" href="tel:0387654321">Appeler</a>
        </div>
      </div>
      <div class="col-lg-6">
        <figure class="vt-svc-hero-media mb-0">
          <picture><source srcset="images/hero.webp" type="image/webp"><img src="images/hero.png" alt="Hall Proprio Facility" decoding="async" fetchpriority="high"></picture>
        </figure>
      </div>
    </div>
  </div>
</section>"""
    main += """<section class="vt-reveal py-5">
  <div class="container">
    <p class="vt-eyebrow">Services</p>
    <h2 class="vt-section-title h3 mb-4">Trois piliers, un seul partenaire</h2>
    <div class="row g-3">
      <div class="col-md-4"><article class="vt-svc-tile-m3"><h3 class="h6">Maintenance</h3><p class="small text-secondary mb-0">CVC, electricite, GMAO et astreinte 24/7.</p></article></div>
      <div class="col-md-4"><article class="vt-svc-tile-m3"><h3 class="h6">Accueil</h3><p class="small text-secondary mb-0">Standard, visiteurs, courrier et colis.</p></article></div>
      <div class="col-md-4"><article class="vt-svc-tile-m3"><h3 class="h6">Conciergerie</h3><p class="small text-secondary mb-0">Services occupants et evenementiel sur site.</p></article></div>
    </div>
    <div class="vt-trust-row mt-4 d-flex flex-wrap gap-3 justify-content-between align-items-center">
      <span class="small fw-semibold">ISO 9001 · 200+ sites · SLA 98 %</span>
      <a class="btn btn-sm btn-vt-outline" href="offres.html">Voir les offres</a>
    </div>
  </div>
</section>"""
    main += block_dialog_m3(
        dialog_id="devisFm",
        title="Demande de devis",
        lead="Surface + ville - reponse sous 5 jours (demo).",
        primary_label="Envoyer",
        primary_href="contact.html",
        fields_html='<div class="mb-2"><label class="form-label small">Surface (m2)</label><input class="form-control" type="number" placeholder="2500"></div><div class="mb-2"><label class="form-label small">Ville</label><input class="form-control" placeholder="Metz, Nancy..."></div>',
    )
    main += block_fab_menu_m3([
        {"label": "Devis", "dialog": "devisFm"},
        {"label": "Offres", "href": "offres.html"},
        {"label": "Appeler", "href": "tel:0387654321"},
    ], main_label="Actions FM")
    main += "</main>"
    return _shell_services(
        "index.html",
        f"{SV_BRAND} — Facility management Metz",
        "Facility management et conciergerie pour immeubles tertiaires en Lorraine.",
        main,
    )


def build_services_offres() -> str:
    main = "<main>"
    main += block_hero_split(
        "Des offres calibrées pour chaque site",
        "De la maintenance seule au FM intégré — SLA transparents et tarifs au m².",
        "hero.png",
        "Offres Proprio Facility",
        eyebrow="Nos offres",
        primary_href="contact.html",
        primary_label="Demander un devis",
        secondary_href="secteurs.html",
        secondary_label="Secteurs",
    )
    main += block_promo_cards(SV_PROMOS)
    main += block_comparison_table("Comparer nos formules", [
        ("Maintenance CVC", "Externe ou partielle", "Préventif + curatif + GMAO"),
        ("Accueil", "Non inclus", "Réception lun–ven 8h–19h"),
        ("Astreinte", "Heures ouvrées", "24 h / 24 — 7 j / 7"),
        ("Reporting KPI", "Trimestriel", "Mensuel + tableau de bord"),
        ("Multi-sites", "Site isolé", "Coordination régionale"),
    ])
    main += block_menu_section(
        "Grille tarifaire indicative",
        "Devis personnalisé après audit gratuit sur site.",
        SV_OFFERS_MENU,
    )
    main += block_chapters(SV_CHAPTERS)
    main += block_cta_band("Une question sur cette offre ?", "Nous contacter", "contact.html")
    main += "</main>"
    return _shell_services(
        "offres.html",
        f"Offres — {SV_BRAND}",
        "Offres facility management Metz — maintenance, accueil, conciergerie.",
        main,
    )


def build_services_secteurs() -> str:
    main = "<main>"
    main += block_hero_editorial(
        "Un FM adapté à votre secteur",
        "Bureaux, retail, santé et logistique — des équipes formées aux contraintes métier.",
        "hero.png",
        "Secteurs Proprio Facility",
        eyebrow="Secteurs d'activité",
        primary_href="contact.html",
        primary_label="Demander un devis",
        secondary_href="offres.html",
        secondary_label="Nos offres",
    )
    main += block_sector_strip([
        ("Bureaux", "Tertiaire & coworking"),
        ("Retail", "Centres commerciaux"),
        ("Santé", "Cliniques & EHPAD"),
        ("Logistique", "Entrepôts & plateformes"),
    ])
    main += block_stat_narrative_rows(SV_NARRATIVE)
    main += block_timeline([
        ("2010", "Création de Proprio Facility à Metz."),
        ("2016", "Extension retail et premiers contrats multi-sites."),
        ("2020", "Certification ISO 9001 et centre d'astreinte 24/7."),
        ("2024", "200 sites gérés — couverture Grand Est."),
    ])
    main += block_compact_features([
        {"title": "Immeubles de bureaux", "text": "Accueil premium, conciergerie et maintenance intégrée.", "img": "scene-1.png", "alt": "Bureaux Metz"},
        {"title": "Centres commerciaux", "text": "Propreté, sécurité et coordination locataires.", "img": "gallery-1.png", "alt": "Retail"},
        {"title": "Établissements de santé", "text": "Normes hygiène, flux patients et astreinte technique.", "img": "scene-2.png", "alt": "Santé"},
    ])
    main += block_faq_accordion("Questions secteurs", SV_FAQ)
    main += block_gallery_masonry("Références terrain", [
        {"title": "Tour Saint-Jacques", "text": "12 000 m² bureaux — Metz centre.", "img": "gallery-2.png", "alt": "Tour Metz"},
        {"title": "Parc retail Thionville", "text": "28 boutiques — FM intégré.", "img": "card-2.png", "alt": "Retail"},
        {"title": "Clinique privée", "text": "8 500 m² — astreinte 24/7.", "img": "card-3.png", "alt": "Santé"},
    ])
    main += block_cta_band("Rencontrons-nous à Metz.", "Demander un devis", "contact.html")
    main += "</main>"
    return _shell_services(
        "secteurs.html",
        f"Secteurs — {SV_BRAND}",
        "Secteurs facility management — bureaux, retail, santé, logistique en Lorraine.",
        main,
    )


def build_services_contact() -> str:
    main = """<main>
<section class="vt-hero-compact py-5 text-center">
  <div class="container">
    <p class="vt-eyebrow text-uppercase">Contact</p>
    <h1 class="vt-display display-6">Devis facility management</h1>
    <p class="lead text-secondary">Metz — audit gratuit sur site.</p>
  </div>
</section>"""
    main += block_facility_quote_form(brand=SV_BRAND, address=SV_ADDRESS, phone=SV_PHONE, email=SV_EMAIL)
    main += block_cta_band("Démonstration — aucune donnée transmise.", "Retour accueil", "index.html")
    main += "</main>"
    return _shell_services(
        "contact.html",
        f"Contact — {SV_BRAND}",
        "Demande de devis FM — Proprio Facility Metz.",
        main,
    )


# --- Hôtel Stanislas Collection (etablissement) — hero luxe + snap chapters + marquee ---
ET_BRAND = "Hôtel Stanislas Collection"
ET_PHONE = "03 83 54 12 34"
ET_EMAIL = "reservation@stanislas-collection.fr"
ET_ADDRESS = "2 place Stanislas, 54000 Nancy"
ET_MAPS = "https://maps.google.com/?q=2+place+Stanislas+54000+Nancy"
ET_NAV = [
    {"file": "chambres.html", "label": "Chambres & suites"},
    {"file": "index.html#dining", "label": "Restaurant"},
    {"file": "index.html#wellness", "label": "Bien-être"},
    {"file": "seminaires.html", "label": "Séminaires"},
    {"file": "contact.html", "label": "Contact"},
]
ET_FOOTER_NAV = [
    ("Chambres", "chambres.html"),
    ("Séminaires", "seminaires.html"),
    ("Réserver", "contact.html"),
    ("Spa", "index.html"),
]
ET_CARDS = [
    {"title": "Chambre Classique", "text": "28 m² — vue cour ou jardin, literie premium.", "img": "card-1.png", "alt": "Chambre classique"},
    {"title": "Chambre Supérieure", "text": "35 m² — vue place Stanislas, plateau courtoisie.", "img": "card-2.png", "alt": "Chambre supérieure"},
    {"title": "Suite Stanislas", "text": "55 m² — salon séparé, baignoire et service conciergerie.", "img": "card-3.png", "alt": "Suite Stanislas"},
]
ET_SNAP = [
    {"title": "Lobby & réception", "text": "Marbre, laiton et lumière tamisée — accueil 24 h face à la place Stanislas.", "img": "scene-1.png", "alt": "Lobby Nancy"},
    {"title": "Spa & bien-être", "text": "Hammam, sauna et soins signature après une journée de découverte.", "img": "scene-2.png", "alt": "Spa hôtel"},
    {"title": "Gastronomie locale", "text": "Petit-déjeuner lorrain et bar à vins — produits du terroir.", "img": "scene-3.png", "alt": "Restaurant hôtel"},
]
ET_ROOMS_MENU = [
    {
        "title": "Chambres",
        "items": [
            {"name": "Classique", "desc": "28 m² — 1 ou 2 personnes", "price": "dès 129 €", "tags": ["Vue cour"]},
            {"name": "Supérieure", "desc": "35 m² — vue Stanislas", "price": "dès 169 €", "tags": ["Best-seller"]},
            {"name": "Suite Stanislas", "desc": "55 m² — salon & baignoire", "price": "dès 289 €", "tags": ["4★"]},
        ],
    },
    {
        "title": "Forfaits",
        "items": [
            {"name": "Escapade 2 nuits", "desc": "Petit-déj + spa 1 h", "price": "à partir de 310 €", "tags": []},
            {"name": "Romantique", "desc": "Champagne & late check-out", "price": "sur devis", "tags": []},
            {"name": "Long séjour", "desc": "7 nuits et plus — −15 %", "price": "sur devis", "tags": []},
        ],
    },
]
ET_SEMINAR_ROWS = [
    ("Salon Stanislas", "120 m² — 100 pl. — daylight, modularité"),
    ("Salon Daum", "65 m² — 45 pl. — écran 4K, visio"),
    ("Cabinet VIP", "25 m² — 12 pl. — board executive"),
    ("Technique", "Wi-Fi fibre — restauration chef sur place"),
    ("Services", "Accueil dédié — parking 80 places"),
]


def _shell_etablissement(page: str, title: str, desc: str, main: str) -> str:
    nav = block_hotel_m3_nav(
        ET_BRAND,
        ET_NAV,
        page,
        cta_label="Réserver",
        cta_href="contact.html",
    )
    foot = _chrome_foot(
        "etablissement",
        ET_BRAND,
        phone=ET_PHONE,
        address=ET_ADDRESS,
        email=ET_EMAIL,
        maps_href=ET_MAPS,
        nav_links=ET_FOOTER_NAV,
        hours_line="Nancy · Place Stanislas",
    )
    mobile = block_mobile_cta("Réserver", "contact.html", ET_PHONE)
    return wrap_page_hotel(
        title,
        desc,
        nav + main + foot + mobile,
        slug="etablissement",
        page=page,
        site_name=ET_BRAND,
        nav=ET_NAV,
        layout="hotel-m3",
    )


def build_etablissement_index() -> str:
    main = "<main>"
    main += block_hotel_m3_hero(
        "L'élégance intemporelle au cœur de Nancy",
        "Héritage, confort et luxe discret à deux pas de la place Stanislas.",
        "hero.png",
        "Suite Hôtel Stanislas Collection Nancy",
        primary_href="chambres.html",
        primary_label="Découvrir la collection",
    )
    main += block_hotel_m3_booking(action="contact.html", cta_label="Voir les disponibilités")
    main += block_hotel_m3_rooms(
        "Chambres & suites",
        "Des espaces élégants pour se reposer, créer et savourer Nancy.",
        [
            {"title": "Deluxe Room", "meta": "28 m² · lit King", "price": "dès 210 € / nuit", "img": "card-1.png", "alt": "Deluxe Room", "href": "contact.html"},
            {"title": "Executive Room", "meta": "35 m² · lit King", "price": "dès 260 € / nuit", "img": "card-2.png", "alt": "Executive Room", "href": "contact.html"},
            {"title": "Junior Suite", "meta": "45 m² · lit King", "price": "dès 380 € / nuit", "img": "card-3.png", "alt": "Junior Suite", "href": "contact.html"},
        ],
    )
    main += block_cta_band(
        "Meilleur tarif en direct - confirmation sous 2 h.",
        "Voir les disponibilites",
        "contact.html",
    )
    main += """<section class="vt-reveal py-5">
  <div class="container">
    <div class="row g-4 align-items-center">
      <div class="col-lg-6">
        <p class="vt-eyebrow text-uppercase">Tarif direct</p>
        <h2 class="vt-section-title h3">Reserver ici, pas sur une plateforme</h2>
        <p class="text-secondary mb-3">Meilleur tarif, accueil 24 h, spa inclus pour les clients heberges - confirmation sous 2 h.</p>
        <button type="button" class="btn btn-vt-primary" data-vt-dialog-open="resaHotel">Voir les disponibilites</button>
      </div>
      <div class="col-lg-6">
        <div class="vt-hotel-perk-grid">
          <div><strong>Spa</strong><span>Hammam &amp; sauna</span></div>
          <div><strong>Salons</strong><span>Jusqu'a 100 pers.</span></div>
          <div><strong>Parking</strong><span>80 places</span></div>
          <div><strong>Bar</strong><span>Vins du terroir</span></div>
        </div>
      </div>
    </div>
  </div>
</section>"""
    main += '<div id="dining"></div>'
    main += '<div id="wellness"></div>'
    main += block_dialog_m3(
        dialog_id="resaHotel",
        title="Disponibilites",
        lead="Arrivee, depart, chambres - on confirme sous 2 h (demo).",
        primary_label="Demander",
        primary_href="contact.html",
        fields_html='<div class="row g-2"><div class="col-6"><label class="form-label small">Arrivee</label><input type="date" class="form-control"></div><div class="col-6"><label class="form-label small">Depart</label><input type="date" class="form-control"></div><div class="col-12"><label class="form-label small">Chambre</label><select class="form-select"><option>Deluxe</option><option>Executive</option><option>Junior Suite</option></select></div></div>',
    )
    main += block_fab_menu_m3([
        {"label": "Reserver", "dialog": "resaHotel"},
        {"label": "Chambres", "href": "chambres.html"},
        {"label": "Seminaires", "href": "seminaires.html"},
    ], main_label="Actions hotel")
    main += "</main>"
    return _shell_etablissement(
        "index.html",
        f"{ET_BRAND} — Hôtel Nancy",
        "Hôtel 4 étoiles à Nancy : chambres, spa et séminaires place Stanislas.",
        main,
    )


def build_etablissement_chambres() -> str:
    main = "<main>"
    main += block_hero_editorial(
        "Chambres & suites",
        "Literie premium, insonorisation et vues sur la place Stanislas ou les jardins.",
        "hero.png",
        "Chambre Hôtel Stanislas",
        eyebrow="Hébergement",
        primary_href="contact.html",
        primary_label="Réserver",
        secondary_href="seminaires.html",
        secondary_label="Séminaires",
    )
    main += block_menu_section(
        "Tarifs indicatifs",
        "Meilleur tarif garanti en réservation directe — taxes incluses.",
        ET_ROOMS_MENU,
    )
    main += block_gallery_masonry("Détails & ambiance", [
        {"title": "Vue Stanislas", "text": "Réveil face au patrimoine UNESCO.", "img": "gallery-1.png", "alt": "Vue Stanislas"},
        {"title": "Salle de bain", "text": "Marbre et produits d'accueil.", "img": "gallery-2.png", "alt": "Salle de bain"},
        {"title": "Suite salon", "text": "Espace de travail et détente.", "img": "card-3.png", "alt": "Suite"},
    ])
    main += block_cta_band("Une question sur une chambre ?", "Nous contacter", "contact.html")
    main += "</main>"
    return _shell_etablissement(
        "chambres.html",
        f"Chambres — {ET_BRAND}",
        "Chambres et suites 4 étoiles à Nancy — Hôtel Stanislas Collection.",
        main,
    )


def build_etablissement_seminaires() -> str:
    main = "<main>"
    main += block_hero_split(
        "Séminaires & événements",
        "4 salons modulables jusqu'à 100 personnes — lumière du jour et restauration chef.",
        "hero.png",
        "Salle séminaire Nancy",
        eyebrow="Événements pro",
        primary_href="contact.html",
        primary_label="Demander un devis",
        secondary_href="chambres.html",
        secondary_label="Hébergement",
    )
    main += block_specs_table("Capacités & équipements", ET_SEMINAR_ROWS)
    main += block_compact_features([
        {"title": "Salon Stanislas", "text": "120 m² modulables — plénière ou ateliers parallèles.", "img": "scene-1.png", "alt": "Salon"},
        {"title": "Restauration", "text": "Pauses, déjeuners assis ou cocktail dinatoire.", "img": "scene-3.png", "alt": "Restauration"},
        {"title": "Hébergement groupe", "text": "Tarifs dédiés à partir de 10 chambres.", "img": "scene-2.png", "alt": "Groupe"},
    ])
    main += block_faq_accordion("Questions séminaires", [
        ("Proposez-vous la visioconférence ?", "Oui — fibre, écrans 4K et assistance technique incluse."),
        ("Peut-on privatiser le spa ?", "Sur demande pour les groupes hébergés — devis sur mesure."),
        ("Y a-t-il un parking bus ?", "Oui — accès groupes sur réservation à 80 m."),
    ])
    main += block_cta_band("Organisons votre événement à Nancy.", "Demander un devis", "contact.html")
    main += "</main>"
    return _shell_etablissement(
        "seminaires.html",
        f"Séminaires — {ET_BRAND}",
        "Salles de séminaire et événements à Nancy — Hôtel Stanislas Collection.",
        main,
    )


def build_etablissement_contact() -> str:
    main = """<main>
<section class="vt-hero-compact py-5 text-center vt-reveal">
  <div class="container">
    <p class="vt-eyebrow text-uppercase">Réservation</p>
    <h1 class="vt-display display-6">Votre séjour à Nancy</h1>
    <p class="lead text-secondary">Place Stanislas — confirmation sous 2 h.</p>
  </div>
</section>"""
    main += block_hotel_reservation_form(brand=ET_BRAND, address=ET_ADDRESS, phone=ET_PHONE, email=ET_EMAIL)
    main += block_cta_band("Démonstration — aucune donnée transmise.", "Retour accueil", "index.html")
    main += "</main>"
    return _shell_etablissement(
        "contact.html",
        f"Contact — {ET_BRAND}",
        "Réservation hôtel 4 étoiles Nancy — Stanislas Collection.",
        main,
    )


# --- Synapse Lorraine (technologie) — hero scan + specs + marquee clients ---
TE_BRAND = "Synapse Lorraine"
TE_PHONE = "03 87 12 34 56"
TE_EMAIL = "contact@synapse-lorraine.fr"
TE_ADDRESS = "14 rue Serpenoise, 57000 Metz"
TE_MAPS = "https://maps.google.com/?q=14+rue+Serpenoise+57000+Metz"
TE_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "produit.html", "label": "Produit"},
    {"file": "clients.html", "label": "Clients"},
    {"file": "contact.html", "label": "Contact"},
]
TE_FOOTER_NAV = [
    ("Produit", "produit.html"),
    ("Clients", "clients.html"),
    ("Démo", "contact.html"),
    ("RGPD", "produit.html"),
]
TE_CARDS = [
    {"title": "Data Lake", "text": "Ingestion batch & streaming — connecteurs ERP, MES, IoT.", "img": "card-1.png", "alt": "Dashboard data"},
    {"title": "Intégrations cloud", "text": "API REST, webhooks et connecteurs Azure / AWS.", "img": "card-2.png", "alt": "Intégrations"},
    {"title": "Sécurité entreprise", "text": "SSO, chiffrement et conformité RGPD native.", "img": "card-3.png", "alt": "Sécurité"},
]
TE_TABS = [
    {"label": "Ingestion", "title": "Centralisez vos flux industriels", "text": "Connecteurs OPC-UA, SQL et fichiers plats — schéma unifié en quelques clics.", "img": "scene-1.png", "alt": "Ingestion"},
    {"label": "Analytics", "title": "Tableaux de bord temps réel", "text": "KPI production, qualité et maintenance — alertes configurables.", "img": "scene-2.png", "alt": "Analytics"},
    {"label": "Gouvernance", "title": "Qualité et traçabilité des données", "text": "Catalogue, lineage et droits d'accès par rôle DSI / métier.", "img": "scene-3.png", "alt": "Gouvernance"},
]
TE_NARRATIVE = [
    {"stat": "45", "stat_label": "Clients industriels", "title": "Grand Est", "text": "Automobile, métallurgie et logistique — déploiements on-prem ou cloud.", "img": "gallery-1.png", "alt": "Clients"},
    {"stat": "99.9", "stat_label": "% SLA", "title": "Disponibilité", "text": "Infrastructure redondée — support N2 en français.", "img": "gallery-2.png", "alt": "SLA"},
    {"stat": "48 h", "stat_label": "POC", "title": "Time-to-value", "text": "Premier tableau de bord opérationnel en deux jours ouvrés.", "img": "scene-2.png", "alt": "POC"},
]


def _shell_technologie(page: str, title: str, desc: str, main: str) -> str:
    bar = block_info_bar(status="Support DSI · Lun–ven 8h–19h", address=TE_ADDRESS, phone=TE_PHONE, maps_href=TE_MAPS)
    nav = _chrome_nav("technologie", TE_BRAND, TE_NAV, page, cta_label="Demander une démo", cta_href="contact.html")
    foot = _chrome_foot("technologie", TE_BRAND, phone=TE_PHONE, address=TE_ADDRESS, email=TE_EMAIL, maps_href=TE_MAPS, nav_links=TE_FOOTER_NAV, hours_line="Metz · Éditeur B2B")
    mobile = block_mobile_cta("Démo", "contact.html", TE_PHONE)
    return wrap_page_tech(title, desc, bar + nav + main + foot + mobile, slug="technologie", page=page, site_name=TE_BRAND, nav=TE_NAV)


def build_technologie_index() -> str:
    main = "<main>"
    main += """<section class="vt-reveal py-5">
  <div class="container">
    <div class="row g-4 g-xl-5 align-items-center">
      <div class="col-lg-6">
        <p class="vt-eyebrow mb-2">Editeur B2B · Metz</p>
        <h1 class="vt-display display-4 mb-3">La data industrielle, claire</h1>
        <p class="lead mb-4">Centralise, analyse et partage tes donnees - POC en 48 h, hebergement France.</p>
        <div class="d-flex flex-wrap gap-2">
          <button type="button" class="btn btn-vt-primary btn-lg" data-vt-dialog-open="demoTech">Demander une demo</button>
          <a class="btn btn-vt-outline btn-lg" href="produit.html">Voir le produit</a>
        </div>
      </div>
      <div class="col-lg-6">
        <div class="vt-tech-dash" aria-hidden="true">
          <div class="d-flex justify-content-between small mb-3"><span class="text-secondary">Synapse · live</span><span style="color:var(--vt-cyan)">99.9% SLA</span></div>
          <div class="bar" style="width:92%"></div>
          <div class="bar" style="width:74%"></div>
          <div class="bar" style="width:86%"></div>
          <div class="bar" style="width:61%"></div>
          <p class="small text-secondary mb-0 mt-3">Pipelines · OEE · alertes</p>
        </div>
      </div>
    </div>
  </div>
</section>"""
    main += block_marquee_m3(["Renault", "ArcelorMittal", "Fives", "Safran", "GE Healthcare", "Michelin"])
    main += """<section class="vt-reveal py-5">
  <div class="container">
    <p class="vt-eyebrow">Produit</p>
    <h2 class="vt-section-title h3 mb-4">Trois briques, une stack</h2>
    <div class="row g-3">
      <div class="col-md-4"><article class="vt-tech-feat"><h3 class="h6">Ingestion</h3><p class="small text-secondary mb-0">50+ sources, streaming IoT et ERP.</p></article></div>
      <div class="col-md-4"><article class="vt-tech-feat"><h3 class="h6">Gouvernance</h3><p class="small text-secondary mb-0">Catalogue, qualite, droits et audit.</p></article></div>
      <div class="col-md-4"><article class="vt-tech-feat"><h3 class="h6">Activation</h3><p class="small text-secondary mb-0">Dashboards metier et API sortantes.</p></article></div>
    </div>
  </div>
</section>"""
    main += block_dialog_m3(
        dialog_id="demoTech",
        title="Demander une demo",
        lead="Atelier 2 h avec tes echantillons - on te recontacte (demo).",
        primary_label="Reserver",
        primary_href="contact.html",
        fields_html='<div class="mb-2"><label class="form-label small">Societe</label><input class="form-control"></div><div class="mb-2"><label class="form-label small">Email pro</label><input class="form-control" type="email"></div>',
    )
    main += block_fab_menu_m3([
        {"label": "Demo", "dialog": "demoTech"},
        {"label": "Produit", "href": "produit.html"},
        {"label": "Clients", "href": "clients.html"},
    ], main_label="Actions Synapse")
    main += "</main>"
    return _shell_technologie("index.html", f"{TE_BRAND} — Data industrielle Metz", "Plateforme data B2B à Metz pour DSI et industriels du Grand Est.", main)


def build_technologie_produit() -> str:
    main = "<main>"
    main += block_hero_split("Architecture data unifiée", "Lakehouse, pipelines et catalogues — une stack, un interlocuteur.", "hero.png", "Produit Synapse", eyebrow="Produit", primary_href="contact.html", primary_label="Démo", secondary_href="clients.html", secondary_label="Références")
    main += block_spec_grid("Capacités plateforme", [
        {"label": "Ingestion", "value": "50+", "detail": "sources connectées"},
        {"label": "Latence", "value": "< 5 s", "detail": "streaming IoT"},
        {"label": "Rétention", "value": "7 ans", "detail": "conformité"},
        {"label": "API", "value": "REST", "detail": "webhooks sortants"},
    ])
    main += block_specs_table("Spécifications techniques", [
        ("Déploiement", "SaaS France, VPC dédié ou on-prem"),
        ("Auth", "SSO SAML / OIDC, MFA"),
        ("Formats", "Parquet, JSON, CSV, OPC-UA"),
        ("SLA", "99.9 % disponibilité"),
    ])
    main += block_chapters([
        {"title": "Pipelines visuels", "text": "Orchestration no-code avec versioning Git.", "img": "scene-1.png", "alt": "Pipelines"},
        {"title": "Monitoring qualité", "text": "Règles automatiques et alertes Slack/Teams.", "img": "scene-2.png", "alt": "Qualité"},
        {"title": "Self-service BI", "text": "Exploration métier sans ticket DSI.", "img": "scene-3.png", "alt": "BI"},
    ])
    main += block_cta_band("Voir la plateforme en action.", "Demander une démo", "contact.html")
    main += "</main>"
    return _shell_technologie("produit.html", f"Produit — {TE_BRAND}", "Modules et architecture de la plateforme Synapse Lorraine.", main)


def build_technologie_clients() -> str:
    main = "<main>"
    main += block_hero_editorial("Ils nous font confiance", "Automobile, métallurgie et santé — des déploiements mesurables en Moselle.", "hero.png", "Clients Synapse", eyebrow="Références", primary_href="contact.html", primary_label="Parler à un expert", secondary_href="produit.html", secondary_label="Produit")
    main += block_stat_narrative_rows(TE_NARRATIVE)
    main += block_gallery_masonry("Cas d'usage", [
        {"title": "OEE temps réel", "text": "−18 % arrêts non planifiés — site auto.", "img": "gallery-1.png", "alt": "OEE"},
        {"title": "Traçabilité lot", "text": "Conformité FDA accélérée.", "img": "gallery-2.png", "alt": "Traçabilité"},
        {"title": "Maintenance prédictive", "text": "Capteurs + modèles ML intégrés.", "img": "card-1.png", "alt": "Maintenance"},
    ])
    main += block_faq_accordion("Questions DSI", [
        ("Hébergement France ?", "Oui — datacenters certifiés ISO 27001 en France."),
        ("Intégration ERP ?", "SAP, Oracle, Divalto — connecteurs standards inclus."),
        ("Durée POC ?", "48 h pour un premier dashboard avec vos échantillons."),
    ])
    main += block_cta_band("Échangez avec un architecte data.", "Contact", "contact.html")
    main += "</main>"
    return _shell_technologie("clients.html", f"Clients — {TE_BRAND}", "Références industrielles Synapse Lorraine — Grand Est.", main)


def build_technologie_contact() -> str:
    main = """<main>
<section class="vt-hero-compact py-5 text-center vt-reveal">
  <div class="container">
    <p class="vt-eyebrow text-uppercase">Contact</p>
    <h1 class="vt-display display-6">Démo personnalisée</h1>
    <p class="lead text-secondary">Metz — réponse sous 24 h.</p>
  </div>
</section>"""
    main += block_tech_demo_form(brand=TE_BRAND, address=TE_ADDRESS, phone=TE_PHONE, email=TE_EMAIL)
    main += block_cta_band("Démonstration — aucune donnée transmise.", "Retour accueil", "index.html")
    main += "</main>"
    return _shell_technologie("contact.html", f"Contact — {TE_BRAND}", "Demande de démo Synapse Lorraine — Metz.", main)


# --- FlowMetrics (saas-landing) — orbes + mockup flottant + tabs + pricing ---
FM_BRAND = "FlowMetrics"
FM_EMAIL = "hello@flowmetrics.io"
FM_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "fonctionnalites.html", "label": "Fonctionnalités"},
    {"file": "tarifs.html", "label": "Tarifs"},
    {"file": "contact.html", "label": "Contact"},
]
FM_FOOTER_NAV = [
    ("Fonctionnalités", "fonctionnalites.html"),
    ("Tarifs", "tarifs.html"),
    ("Essai gratuit", "contact.html"),
    ("RGPD", "fonctionnalites.html"),
]
FM_TABS = [
    {"label": "Analytics", "title": "Funnels et rétention en un coup d'œil", "text": "Cohortes, activation et time-to-value — sans SQL.", "img": "scene-1.png", "alt": "Analytics"},
    {"label": "Workflow", "title": "Parcours utilisateur en 3 clics", "text": "Onboarding guidé et checklists intégrées.", "img": "scene-2.png", "alt": "Workflow"},
    {"label": "Intégrations", "title": "Branchez vos outils en minutes", "text": "Segment, Stripe, HubSpot — API ouverte.", "img": "scene-3.png", "alt": "Intégrations"},
]
FM_PRICING = [
    {"name": "Starter", "price": "49 €/mois", "features": ["3 utilisateurs", "Dashboards essentiels", "Export CSV"], "href": "contact.html", "cta": "Essai gratuit", "hot": False},
    {"name": "Growth", "price": "149 €/mois", "features": ["15 utilisateurs", "Funnels avancés", "Alertes Slack"], "href": "contact.html", "cta": "Essai gratuit", "hot": True},
    {"name": "Enterprise", "price": "Sur devis", "features": ["SSO SAML", "VPC dédié", "SLA 99.9 %"], "href": "contact.html", "cta": "Nous contacter", "hot": False},
]


def _shell_saas_landing(page: str, title: str, desc: str, main: str) -> str:
    nav = _chrome_nav("saas-landing", FM_BRAND, FM_NAV, page, cta_label="Essai gratuit", cta_href="contact.html")
    foot = _chrome_foot("saas-landing", FM_BRAND, phone="", address="SaaS · Hébergé en France", email=FM_EMAIL, maps_href="#", nav_links=FM_FOOTER_NAV, hours_line="Support chat 9h–18h")
    mobile = block_mobile_cta("Essai gratuit", "contact.html", "")
    return wrap_page_saas(
        title, desc, nav + main + foot + mobile,
        layout="saas-landing", slug="saas-landing", page=page, site_name=FM_BRAND, nav=FM_NAV,
        brand=FM_BRAND, brand_desc="SaaS analytics pour equipes produit",
        head_assets=HEAD_SAAS, body_class="vt-body vt-body-saas-landing",
    )


def build_saas_landing_index() -> str:
    main = "<main>"
    main += """<section class="vt-saas-hero vt-reveal">
  <div class="container">
    <div class="row g-4 g-xl-5 align-items-center">
      <div class="col-lg-6">
        <p class="vt-eyebrow mb-2">SaaS · Analytics produit</p>
        <h1 class="vt-display display-4 mb-3">Tes donnees, des decisions claires</h1>
        <p class="lead mb-4">Funnels, retention et activation - sans SQL, pour equipes lean.</p>
        <div class="d-flex flex-wrap gap-2">
          <button type="button" class="btn btn-vt-primary btn-lg" data-vt-dialog-open="essaiFm">Essai gratuit 14 j</button>
          <a class="btn btn-vt-outline btn-lg" href="fonctionnalites.html">Fonctionnalites</a>
        </div>
      </div>
      <div class="col-lg-6">
        <div class="vt-saas-mock" aria-hidden="true">
          <div class="d-flex justify-content-between small mb-3"><span class="text-secondary">FlowMetrics</span><span style="color:var(--vt-teal)">live</span></div>
          <div class="bar" style="width:88%"></div>
          <div class="bar" style="width:72%"></div>
          <div class="bar" style="width:64%"></div>
          <p class="small text-secondary mb-0 mt-2">Activation · retention · alertes</p>
        </div>
      </div>
    </div>
  </div>
</section>"""
    main += block_marquee_m3(["Product Hunt", "RGPD", "SOC 2", "API REST", "Slack", "Segment"])
    main += """<section class="vt-reveal py-5">
  <div class="container">
    <p class="vt-eyebrow">Tarifs</p>
    <h2 class="vt-section-title h3 mb-4">Des plans qui scalent avec toi</h2>
    <div class="row g-3">
      <div class="col-md-4"><article class="vt-saas-price"><h3 class="h6">Starter</h3><p class="h4 mb-2">49 euro/mois</p><p class="small text-secondary mb-0">3 users · dashboards · export CSV</p></article></div>
      <div class="col-md-4"><article class="vt-saas-price hot"><h3 class="h6">Growth</h3><p class="h4 mb-2">149 euro/mois</p><p class="small text-secondary mb-0">15 users · funnels · alertes Slack</p></article></div>
      <div class="col-md-4"><article class="vt-saas-price"><h3 class="h6">Enterprise</h3><p class="h4 mb-2">Sur devis</p><p class="small text-secondary mb-0">SSO · VPC · SLA 99.9 %</p></article></div>
    </div>
  </div>
</section>"""
    main += block_dialog_m3(
        dialog_id="essaiFm",
        title="Essai gratuit 14 jours",
        lead="Sans carte bancaire - on te cree un espace demo.",
        primary_label="Demarrer",
        primary_href="contact.html",
        fields_html='<div class="mb-2"><label class="form-label small">Email pro</label><input class="form-control" type="email"></div><div class="mb-2"><label class="form-label small">Societe</label><input class="form-control"></div>',
    )
    main += block_fab_menu_m3([
        {"label": "Essai", "dialog": "essaiFm"},
        {"label": "Tarifs", "href": "tarifs.html"},
        {"label": "Features", "href": "fonctionnalites.html"},
    ], main_label="Actions FlowMetrics")
    main += "</main>"
    return _shell_saas_landing("index.html", f"{FM_BRAND} — Analytics produit", "Landing SaaS analytics — funnels, rétention et activation.", main)


def build_saas_landing_fonctionnalites() -> str:
    main = "<main>"
    main += block_hero_split("Fonctionnalités pensées produit", "De l'event tracking aux alertes — une stack analytics complète.", "hero.png", "FlowMetrics UI", eyebrow="Fonctionnalités", primary_href="contact.html", primary_label="Essai gratuit", secondary_href="tarifs.html", secondary_label="Tarifs")
    main += block_bento_cards([
        {"title": "Event tracking", "text": "SDK JS, mobile et server-side.", "img": "card-1.png", "alt": "Tracking", "size": "lg"},
        {"title": "Alertes", "text": "Seuils et anomalies — Slack, email.", "img": "card-2.png", "alt": "Alertes", "size": "sm"},
        {"title": "Collaboration", "text": "Commentaires et dashboards partagés.", "img": "card-3.png", "alt": "Collab", "size": "sm"},
    ])
    main += block_comparison_table("Avant / après FlowMetrics", [
        ("Sources data", "Excel + 4 outils", "Une plateforme unifiée"),
        ("Time-to-insight", "Jours", "Minutes"),
        ("Onboarding équipe", "Formation longue", "Templates prêts"),
    ])
    main += block_cta_band("Testez toutes les fonctionnalités.", "Essai gratuit", "contact.html")
    main += "</main>"
    return _shell_saas_landing("fonctionnalites.html", f"Fonctionnalités — {FM_BRAND}", "Fonctionnalités analytics FlowMetrics.", main)


def build_saas_landing_tarifs() -> str:
    main = "<main>"
    main += block_hero_editorial("Des tarifs qui scalent avec vous", "Starter pour les petites équipes — Enterprise pour le SSO et le VPC.", "hero.png", "Tarifs FlowMetrics", eyebrow="Tarifs", primary_href="contact.html", primary_label="Essai gratuit", secondary_href="fonctionnalites.html", secondary_label="Fonctionnalités")
    main += block_pricing_tiers("Choisissez votre plan", FM_PRICING)
    main += block_faq_accordion("FAQ tarifs", [
        ("Changement de plan ?", "Upgrade immédiat — downgrade en fin de période."),
        ("Facturation annuelle ?", "−20 % sur les plans Growth et Enterprise."),
        ("Données exportables ?", "Oui — CSV et API à tout moment."),
    ])
    main += block_cta_band("14 jours gratuits — annulez quand vous voulez.", "Démarrer", "contact.html")
    main += "</main>"
    return _shell_saas_landing("tarifs.html", f"Tarifs — {FM_BRAND}", "Tarifs FlowMetrics — Starter, Growth, Enterprise.", main)


def build_saas_landing_contact() -> str:
    main = """<main>
<section class="vt-hero-compact py-5 text-center vt-reveal">
  <div class="container">
    <p class="vt-eyebrow text-uppercase">Essai</p>
    <h1 class="vt-display display-6">14 jours gratuits</h1>
    <p class="lead text-secondary">Sans carte bancaire.</p>
  </div>
</section>"""
    main += block_saas_trial_form(brand=FM_BRAND, email=FM_EMAIL)
    main += block_cta_band("Démonstration — aucune donnée transmise.", "Retour accueil", "index.html")
    main += "</main>"
    return _shell_saas_landing("contact.html", f"Contact — {FM_BRAND}", "Essai gratuit FlowMetrics.", main)


# --- TalentLoop (saas-onboarding) — wizard progression + snap chapters ---
TL_BRAND = "TalentLoop"
TL_EMAIL = "hello@talentloop.io"
TL_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "parcours.html", "label": "Parcours"},
    {"file": "fonctionnalites.html", "label": "Fonctionnalités"},
    {"file": "contact.html", "label": "Contact"},
]
TL_FOOTER_NAV = [
    ("Parcours", "parcours.html"),
    ("Fonctionnalités", "fonctionnalites.html"),
    ("Essai gratuit", "contact.html"),
    ("RGPD", "fonctionnalites.html"),
]
TL_WIZARD = [
    {"label": "Profil", "title": "Bienvenue — profil en 30 secondes", "text": "Nom, poste et date d'arrivée — zéro friction.", "img": "scene-1.png", "alt": "Étape profil"},
    {"label": "Équipe", "title": "Rencontrez votre buddy RH", "text": "Un contact humain assigné dès le jour J.", "img": "scene-2.png", "alt": "Buddy RH"},
    {"label": "Outils", "title": "Accès et intégrations SIRH", "text": "PayFit, Lucca, Teams — connectés en un clic.", "img": "scene-3.png", "alt": "Intégrations"},
    {"label": "Aha", "title": "Première mission visible", "text": "Checklist claire — le collaborateur sait quoi faire.", "img": "gallery-1.png", "alt": "Checklist"},
]
TL_TABS = [
    {"label": "Progression", "title": "Barre de progression par collaborateur", "text": "Suivez l'avancement onboarding en temps réel.", "img": "card-1.png", "alt": "Progression"},
    {"label": "Templates", "title": "Parcours par métier", "text": "Commercial, tech, support — modèles prêts à l'emploi.", "img": "card-2.png", "alt": "Templates"},
    {"label": "Conformité", "title": "RGPD et consentements", "text": "Traçabilité des accords et durées de rétention.", "img": "card-3.png", "alt": "RGPD"},
]
TL_CHAPTERS = [
    {"title": "Moins d'abandon à l'inscription", "text": "Une étape = une intention. Copy orienté valeur à chaque écran.", "img": "scene-1.png", "alt": "Inscription"},
    {"title": "Aha moment visible", "text": "Preview du résultat final — le collaborateur voit où il va.", "img": "scene-2.png", "alt": "Aha moment"},
    {"title": "RH libérées", "text": "Automatisation des tâches répétitives — focus sur l'humain.", "img": "gallery-2.png", "alt": "RH"},
]


def _shell_saas_onboarding(page: str, title: str, desc: str, main: str) -> str:
    nav = _chrome_nav("saas-onboarding", TL_BRAND, TL_NAV, page, cta_label="Essai gratuit", cta_href="contact.html")
    foot = _chrome_foot("saas-onboarding", TL_BRAND, phone="", address="SaaS RH · Hébergé en France", email=TL_EMAIL, maps_href="#", nav_links=TL_FOOTER_NAV, hours_line="Support chat 9h–18h")
    mobile = block_mobile_cta("Essai gratuit", "contact.html", "")
    return wrap_page_saas(
        title, desc, nav + main + foot + mobile,
        layout="saas-onboarding", slug="saas-onboarding", page=page, site_name=TL_BRAND, nav=TL_NAV,
        brand=TL_BRAND, brand_desc="Onboarding RH en 4 etapes",
        head_assets=HEAD_SAAS_ONBOARDING, body_class="vt-body vt-body-saas-onboarding",
    )


def build_saas_onboarding_index() -> str:
    main = "<main>"
    main += """<section class="vt-saas-hero vt-reveal">
  <div class="container">
    <p class="vt-eyebrow mb-2">SaaS · Onboarding RH</p>
    <h1 class="vt-display display-4 mb-3">Onboarding RH en 4 etapes</h1>
    <p class="lead mb-4">Moins d'abandon a l'inscription - un chemin clair jusqu'au aha moment.</p>
    <div class="d-flex flex-wrap gap-2 mb-4">
      <button type="button" class="btn btn-vt-primary btn-lg" data-vt-dialog-open="essaiTl">Essai gratuit 14 j</button>
      <a class="btn btn-vt-outline btn-lg" href="parcours.html">Voir le parcours</a>
    </div>
    <div class="vt-step-rail vt-reveal-stagger">
      <article class="vt-step-card"><span>1</span><h3 class="h6 mt-2 mb-1">Profil</h3><p class="small text-secondary mb-0">30 s - nom, poste, arrivee.</p></article>
      <article class="vt-step-card"><span>2</span><h3 class="h6 mt-2 mb-1">Buddy</h3><p class="small text-secondary mb-0">Un contact humain assigne.</p></article>
      <article class="vt-step-card"><span>3</span><h3 class="h6 mt-2 mb-1">Outils</h3><p class="small text-secondary mb-0">SIRH, messagerie, acces IT.</p></article>
      <article class="vt-step-card"><span>4</span><h3 class="h6 mt-2 mb-1">Mission</h3><p class="small text-secondary mb-0">Premiere checklist claire.</p></article>
    </div>
  </div>
</section>"""
    main += block_marquee_m3(["PayFit", "Lucca", "RGPD", "SSO", "Teams", "Slack"])
    main += block_dialog_m3(
        dialog_id="essaiTl",
        title="Essai gratuit 14 jours",
        lead="Sans carte - on te prepare un parcours demo RH.",
        primary_label="Demarrer",
        primary_href="contact.html",
        fields_html='<div class="mb-2"><label class="form-label small">Email RH</label><input class="form-control" type="email"></div><div class="mb-2"><label class="form-label small">Effectif</label><select class="form-select"><option>1-20</option><option>21-100</option><option>100+</option></select></div>',
    )
    main += block_fab_menu_m3([
        {"label": "Essai", "dialog": "essaiTl"},
        {"label": "Parcours", "href": "parcours.html"},
        {"label": "Features", "href": "fonctionnalites.html"},
    ], main_label="Actions TalentLoop")
    main += "</main>"
    return _shell_saas_onboarding("index.html", f"{TL_BRAND} — Onboarding RH", "Onboarding RH TalentLoop — parcours en 4 étapes avec barre de progression.", main)


def build_saas_onboarding_parcours() -> str:
    main = "<main>"
    main += block_hero_editorial("Le parcours en détail", "Chaque écran rapproche le collaborateur de sa première victoire.", "hero.png", "Parcours TalentLoop", eyebrow="Parcours", primary_href="contact.html", primary_label="Essai gratuit", secondary_href="fonctionnalites.html", secondary_label="Fonctionnalités")
    main += block_funnel_steps("4 étapes, zéro friction", [
        ("Profil express", "30 secondes — nom, poste, date d'arrivée."),
        ("Buddy RH", "Un contact humain assigné automatiquement."),
        ("Outils connectés", "SIRH, messagerie, accès IT — tout en un."),
        ("Première mission", "Checklist claire — le aha moment."),
    ])
    main += block_progress_wizard("Essayez le wizard", TL_WIZARD)
    main += block_compact_features([
        {"title": "Copy orienté valeur", "text": "Chaque étape explique le bénéfice immédiat.", "img": "card-1.png", "alt": "Copy"},
        {"title": "Preview résultat", "text": "Le collaborateur voit à quoi ressemble la fin.", "img": "card-2.png", "alt": "Preview"},
        {"title": "Analytics RH", "text": "Time-to-productivity mesuré par équipe.", "img": "card-3.png", "alt": "Analytics"},
    ])
    main += block_cta_band("Testez le parcours complet.", "Essai gratuit", "contact.html")
    main += "</main>"
    return _shell_saas_onboarding("parcours.html", f"Parcours — {TL_BRAND}", "Parcours onboarding TalentLoop en 4 étapes.", main)


def build_saas_onboarding_fonctionnalites() -> str:
    main = "<main>"
    main += block_hero_split("Fonctionnalités pensées RH", "Templates, analytics et conformité — tout pour scaler l'onboarding.", "hero.png", "Fonctionnalités TalentLoop", eyebrow="Fonctionnalités", primary_href="contact.html", primary_label="Essai gratuit", secondary_href="parcours.html", secondary_label="Parcours")
    main += block_bento_cards([
        {"title": "Templates métier", "text": "Commercial, tech, support — prêts à dupliquer.", "img": "card-1.png", "alt": "Templates", "size": "lg"},
        {"title": "Migration assistée", "text": "Import Excel ou SIRH existant.", "img": "card-2.png", "alt": "Migration", "size": "sm"},
        {"title": "Sécurité RGPD", "text": "Consentements et rétention traçables.", "img": "card-3.png", "alt": "RGPD", "size": "sm"},
    ])
    main += block_comparison_table("Avant / après TalentLoop", [
        ("Onboarding", "Emails + PDF", "Parcours guidé interactif"),
        ("Suivi", "Tableur Excel", "Dashboard temps réel"),
        ("Time-to-value", "3 semaines", "8 minutes"),
    ])
    main += block_faq_accordion("FAQ produit", [
        ("Intégration PayFit ?", "Connecteur natif — synchro bidirectionnelle."),
        ("Personnalisation ?", "Logo, couleurs et copy par entreprise."),
        ("Multi-sites ?", "Oui — parcours par établissement."),
    ])
    main += block_cta_band("Découvrez toutes les fonctionnalités.", "Essai gratuit", "contact.html")
    main += "</main>"
    return _shell_saas_onboarding("fonctionnalites.html", f"Fonctionnalités — {TL_BRAND}", "Fonctionnalités onboarding RH TalentLoop.", main)


def build_saas_onboarding_contact() -> str:
    main = """<main>
<section class="vt-hero-compact py-5 text-center vt-reveal">
  <div class="container">
    <p class="vt-eyebrow text-uppercase">Essai</p>
    <h1 class="vt-display display-6">14 jours gratuits</h1>
    <p class="lead text-secondary">Sans carte bancaire.</p>
  </div>
</section>"""
    main += block_saas_trial_form(brand=TL_BRAND, email=TL_EMAIL)
    main += block_cta_band("Démonstration — aucune donnée transmise.", "Retour accueil", "index.html")
    main += "</main>"
    return _shell_saas_onboarding("contact.html", f"Contact — {TL_BRAND}", "Essai gratuit TalentLoop.", main)


# --- MetricPulse (saas-dashboard) — KPI pulse + tabs ---
MD_BRAND = "MetricPulse"
MD_EMAIL = "hello@metricpulse.io"
MD_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "fonctionnalites.html", "label": "Fonctionnalités"},
    {"file": "tarifs.html", "label": "Tarifs"},
    {"file": "contact.html", "label": "Contact"},
]
MD_FOOTER_NAV = [
    ("Fonctionnalités", "fonctionnalites.html"),
    ("Tarifs", "tarifs.html"),
    ("Essai gratuit", "contact.html"),
    ("API", "fonctionnalites.html"),
]
MD_KPIS = [
    {"label": "Activation", "value": "0", "count_end": 78, "count_suffix": " %", "delta": "+12 % vs M-1"},
    {"label": "Time-to-value", "value": "0", "count_end": 4, "count_suffix": " j", "delta": "−2 j"},
    {"label": "Rétention J30", "value": "0", "count_end": 64, "count_suffix": " %", "delta": "+8 %"},
    {"label": "Events / jour", "value": "0", "count_end": 2400, "count_suffix": "", "delta": "Live"},
]
MD_TABS = [
    {"label": "Funnel", "title": "Funnel activation en un coup d'œil", "text": "Repérez les fuites du parcours onboarding.", "img": "scene-1.png", "alt": "Funnel"},
    {"label": "Workflow", "title": "Builder de parcours drag & drop", "text": "Déclencheurs, conditions et actions sans code.", "img": "scene-2.png", "alt": "Workflow"},
    {"label": "Intégrations", "title": "Segment, Mixpanel, Amplitude", "text": "Importez vos events en quelques clics.", "img": "scene-3.png", "alt": "Intégrations"},
]
MD_PRICING = [
    {"name": "Startup", "price": "79 €/mois", "features": ["5 utilisateurs", "3 dashboards", "Funnel basique"], "href": "contact.html", "cta": "Essai gratuit", "hot": False},
    {"name": "Scale", "price": "249 €/mois", "features": ["25 utilisateurs", "Workflows illimités", "Alertes Slack"], "href": "contact.html", "cta": "Essai gratuit", "hot": True},
    {"name": "Enterprise", "price": "Sur devis", "features": ["SSO SAML", "VPC dédié", "SLA 99.9 %"], "href": "contact.html", "cta": "Nous contacter", "hot": False},
]


def _shell_saas_dashboard(page: str, title: str, desc: str, main: str) -> str:
    nav = _chrome_nav("saas-dashboard", MD_BRAND, MD_NAV, page, cta_label="Essai gratuit", cta_href="contact.html")
    foot = _chrome_foot("saas-dashboard", MD_BRAND, phone="", address="SaaS analytics · Hébergé en France", email=MD_EMAIL, maps_href="#", nav_links=MD_FOOTER_NAV, hours_line="Support chat 9h–18h")
    mobile = block_mobile_cta("Essai gratuit", "contact.html", "")
    return wrap_page_saas(
        title, desc, nav + main + foot + mobile,
        layout="saas-dashboard", slug="saas-dashboard", page=page, site_name=MD_BRAND, nav=MD_NAV,
        brand=MD_BRAND, brand_desc="Dashboard activation produit",
        head_assets=HEAD_SAAS_DASHBOARD, body_class="vt-body vt-body-saas-dashboard",
    )


def build_saas_dashboard_index() -> str:
    main = "<main>"
    main += """<section class="vt-saas-hero vt-reveal">
  <div class="container">
    <p class="vt-eyebrow mb-2">SaaS · Activation produit</p>
    <h1 class="vt-display display-4 mb-3">Dashboard activation, live</h1>
    <p class="lead mb-4">KPIs time-to-value, funnel et evenements - une vue par intention.</p>
    <div class="d-flex flex-wrap gap-2 mb-4">
      <button type="button" class="btn btn-vt-primary btn-lg" data-vt-dialog-open="essaiMd">Essai gratuit 14 j</button>
      <a class="btn btn-vt-outline btn-lg" href="fonctionnalites.html">Fonctionnalites</a>
    </div>
    <div class="row g-3">
      <div class="col-6 col-lg-3"><article class="vt-kpi-card"><strong>2,4 j</strong><span>Time-to-value</span></article></div>
      <div class="col-6 col-lg-3"><article class="vt-kpi-card"><strong>+18 %</strong><span>Activation</span></article></div>
      <div class="col-6 col-lg-3"><article class="vt-kpi-card"><strong>61 %</strong><span>Funnel J7</span></article></div>
      <div class="col-6 col-lg-3"><article class="vt-kpi-card"><strong>99.9 %</strong><span>SLA</span></article></div>
    </div>
  </div>
</section>"""
    main += block_marquee_m3(["Segment", "Mixpanel", "Slack", "API REST", "SOC 2", "RGPD"])
    main += block_dialog_m3(
        dialog_id="essaiMd",
        title="Essai gratuit 14 jours",
        lead="Sans CB - dashboard demo avec tes KPI fictifs.",
        primary_label="Demarrer",
        primary_href="contact.html",
        fields_html='<div class="mb-2"><label class="form-label small">Email pro</label><input class="form-control" type="email"></div>',
    )
    main += block_fab_menu_m3([
        {"label": "Essai", "dialog": "essaiMd"},
        {"label": "Features", "href": "fonctionnalites.html"},
        {"label": "Tarifs", "href": "tarifs.html"},
    ], main_label="Actions MetricPulse")
    main += "</main>"
    return _shell_saas_dashboard("index.html", f"{MD_BRAND} — Dashboard activation", "Dashboard produit MetricPulse — KPIs activation et funnel onboarding.", main)


def build_saas_dashboard_fonctionnalites() -> str:
    main = "<main>"
    main += block_hero_split("Fonctionnalités data produit", "Sidebar regroupée par intention — pas par feature brute.", "hero.png", "Fonctionnalités MetricPulse", eyebrow="Fonctionnalités", primary_href="contact.html", primary_label="Essai gratuit", secondary_href="tarifs.html", secondary_label="Tarifs")
    main += block_spec_grid("Modules clés", [
        {"label": "Funnel", "value": "Builder", "detail": "Étapes personnalisables et filtres avancés."},
        {"label": "Cohortes", "value": "J7–J90", "detail": "Rétention comparable par segment."},
        {"label": "Alertes", "value": "Auto", "detail": "Seuils, anomalies et digests programmés."},
        {"label": "Collab", "value": "Live", "detail": "Commentaires et dashboards partagés."},
    ])
    main += block_bento_cards([
        {"title": "Widget KPI", "text": "Sparklines et variation M/M.", "img": "gallery-1.png", "alt": "KPI", "size": "lg"},
        {"title": "Mobile", "text": "Résumé métriques sur smartphone.", "img": "gallery-2.png", "alt": "Mobile", "size": "sm"},
        {"title": "SSO", "text": "SAML et contrôle d'accès par rôle.", "img": "card-3.png", "alt": "SSO", "size": "sm"},
    ])
    main += block_comparison_table("Avant / après MetricPulse", [
        ("Sources", "4 outils + Excel", "Une plateforme unifiée"),
        ("Time-to-insight", "Jours", "Minutes"),
        ("Alertes", "Manuelles", "Automatisées"),
    ])
    main += block_cta_band("Testez toutes les fonctionnalités.", "Essai gratuit", "contact.html")
    main += "</main>"
    return _shell_saas_dashboard("fonctionnalites.html", f"Fonctionnalités — {MD_BRAND}", "Fonctionnalités dashboard MetricPulse.", main)


def build_saas_dashboard_tarifs() -> str:
    main = "<main>"
    main += block_hero_editorial("Tarifs transparents", "Startup pour les petites équipes — Enterprise pour le SSO.", "hero.png", "Tarifs MetricPulse", eyebrow="Tarifs", primary_href="contact.html", primary_label="Essai gratuit", secondary_href="fonctionnalites.html", secondary_label="Fonctionnalités")
    main += block_pricing_tiers("Choisissez votre plan", MD_PRICING)
    main += block_faq_accordion("FAQ tarifs", [
        ("Changement de plan ?", "Upgrade immédiat — downgrade en fin de période."),
        ("Volume events ?", "Plans illimités à partir de Scale."),
        ("Export données ?", "CSV et API à tout moment."),
    ])
    main += block_cta_band("14 jours gratuits.", "Démarrer", "contact.html")
    main += "</main>"
    return _shell_saas_dashboard("tarifs.html", f"Tarifs — {MD_BRAND}", "Tarifs MetricPulse.", main)


def build_saas_dashboard_contact() -> str:
    main = """<main>
<section class="vt-hero-compact py-5 text-center vt-reveal">
  <div class="container">
    <p class="vt-eyebrow text-uppercase">Essai</p>
    <h1 class="vt-display display-6">14 jours gratuits</h1>
    <p class="lead text-secondary">Sans carte bancaire.</p>
  </div>
</section>"""
    main += block_saas_trial_form(brand=MD_BRAND, email=MD_EMAIL)
    main += block_cta_band("Démonstration — aucune donnée transmise.", "Retour accueil", "index.html")
    main += "</main>"
    return _shell_saas_dashboard("contact.html", f"Contact — {MD_BRAND}", "Essai gratuit MetricPulse.", main)


# --- QueryBase (saas-empty) — morph avant/après + recherche ---
QB_BRAND = "QueryBase"
QB_EMAIL = "hello@querybase.io"
QB_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "fonctionnalites.html", "label": "Fonctionnalités"},
    {"file": "tarifs.html", "label": "Tarifs"},
    {"file": "contact.html", "label": "Contact"},
]
QB_FOOTER_NAV = [
    ("Fonctionnalités", "fonctionnalites.html"),
    ("Tarifs", "tarifs.html"),
    ("Essai gratuit", "contact.html"),
    ("Docs", "fonctionnalites.html"),
]
QB_TABS = [
    {"label": "Recherche", "title": "Zéro impasse — suggestions intelligentes", "text": "Synonymes, fautes de frappe et best-sellers alternatifs.", "img": "scene-2.png", "alt": "Recherche"},
    {"label": "Empty state", "title": "États vides orientés action", "text": "CTA clair, jamais un mur blanc.", "img": "scene-1.png", "alt": "Empty state"},
    {"label": "Roadmap", "title": "Vote feature intégré", "text": "L'échec de recherche devient un signal produit.", "img": "scene-3.png", "alt": "Roadmap"},
]
QB_PRICING = [
    {"name": "Solo", "price": "29 €/mois", "features": ["1 projet", "Recherche full-text", "Empty states"], "href": "contact.html", "cta": "Essai gratuit", "hot": False},
    {"name": "Team", "price": "99 €/mois", "features": ["5 projets", "Synonymes IA", "Analytics recherche"], "href": "contact.html", "cta": "Essai gratuit", "hot": True},
    {"name": "Business", "price": "Sur devis", "features": ["Projets illimités", "SSO", "SLA"], "href": "contact.html", "cta": "Nous contacter", "hot": False},
]


def _shell_saas_empty(page: str, title: str, desc: str, main: str) -> str:
    nav = _chrome_nav("saas-empty", QB_BRAND, QB_NAV, page, cta_label="Essai gratuit", cta_href="contact.html")
    foot = _chrome_foot("saas-empty", QB_BRAND, phone="", address="SaaS data · Hébergé en France", email=QB_EMAIL, maps_href="#", nav_links=QB_FOOTER_NAV, hours_line="Support chat 9h–18h")
    mobile = block_mobile_cta("Essai gratuit", "contact.html", "")
    return wrap_page_saas(
        title, desc, nav + main + foot + mobile,
        layout="saas-empty", slug="saas-empty", page=page, site_name=QB_BRAND, nav=QB_NAV,
        brand=QB_BRAND, brand_desc="Empty states et recherche intelligente",
        head_assets=HEAD_SAAS_EMPTY, body_class="vt-body vt-body-saas-empty",
    )


def build_saas_empty_index() -> str:
    main = "<main>"
    main += """<section class="vt-saas-hero vt-reveal">
  <div class="container">
    <p class="vt-eyebrow mb-2">SaaS · Empty states</p>
    <h1 class="vt-display display-4 mb-3">Zero impasse pour tes users</h1>
    <p class="lead mb-4">Recherche vide ? Suggestions, correcteur et vote roadmap - jamais un mur blanc.</p>
    <div class="d-flex flex-wrap gap-2 mb-4">
      <button type="button" class="btn btn-vt-primary btn-lg" data-vt-dialog-open="essaiQb">Essai gratuit 14 j</button>
      <a class="btn btn-vt-outline btn-lg" href="fonctionnalites.html">Fonctionnalites</a>
    </div>
    <div class="row g-3">
      <div class="col-md-6"><article class="vt-morph-card"><span class="tag">Avant</span><h3 class="h6">Recherche vide</h3><p class="small text-secondary mb-0">User perdu, churn silencieux.</p></article></div>
      <div class="col-md-6"><article class="vt-morph-card after"><span class="tag">Apres</span><h3 class="h6">Suggestions utiles</h3><p class="small text-secondary mb-0">CTA clair, signal produit capture.</p></article></div>
    </div>
  </div>
</section>"""
    main += block_dialog_m3(
        dialog_id="essaiQb",
        title="Essai gratuit 14 jours",
        lead="Sans CB - empty states demo dans ton projet.",
        primary_label="Demarrer",
        primary_href="contact.html",
        fields_html='<div class="mb-2"><label class="form-label small">Email pro</label><input class="form-control" type="email"></div>',
    )
    main += block_fab_menu_m3([
        {"label": "Essai", "dialog": "essaiQb"},
        {"label": "Features", "href": "fonctionnalites.html"},
        {"label": "Tarifs", "href": "tarifs.html"},
    ], main_label="Actions QueryBase")
    main += "</main>"
    return _shell_saas_empty("index.html", f"{QB_BRAND} — Empty states", "QueryBase — recherche intelligente et empty states orientés action.", main)


def build_saas_empty_fonctionnalites() -> str:
    main = "<main>"
    main += block_hero_split("Fonctionnalités recherche", "Correcteur, synonymes et analytics — tout pour guider l'utilisateur.", "hero.png", "Fonctionnalités QueryBase", eyebrow="Fonctionnalités", primary_href="contact.html", primary_label="Essai gratuit", secondary_href="tarifs.html", secondary_label="Tarifs")
    main += block_compact_features([
        {"title": "Correcteur d'intention", "text": "Fautes de frappe et synonymes automatiques.", "img": "scene-2.png", "alt": "Correcteur"},
        {"title": "Best-sellers alternatifs", "text": "Quand le résultat exact manque.", "img": "gallery-1.png", "alt": "Alternatifs"},
        {"title": "Migration guidée", "text": "Import progressif — empty to filled.", "img": "card-2.png", "alt": "Migration"},
    ])
    main += block_gallery_masonry("Composants UI", [
        {"title": "Table vide", "text": "CTA add row visible.", "img": "gallery-1.png", "alt": "Table"},
        {"title": "Mobile", "text": "Inbox vide actionnable.", "img": "gallery-2.png", "alt": "Mobile"},
        {"title": "Première intégration", "text": "Connecteurs data source.", "img": "scene-3.png", "alt": "Intégration"},
    ])
    main += block_faq_accordion("FAQ", [
        ("Intégration existante ?", "API REST et webhooks — 5 min de setup."),
        ("Personnalisation ?", "Copy, illustrations et CTA par projet."),
        ("Analytics ?", "Taux de rebond recherche et votes feature."),
    ])
    main += block_cta_band("Découvrez tous les patterns.", "Essai gratuit", "contact.html")
    main += "</main>"
    return _shell_saas_empty("fonctionnalites.html", f"Fonctionnalités — {QB_BRAND}", "Fonctionnalités QueryBase.", main)


def build_saas_empty_tarifs() -> str:
    main = "<main>"
    main += block_hero_editorial("Tarifs simples", "Solo pour démarrer — Team pour scaler.", "hero.png", "Tarifs QueryBase", eyebrow="Tarifs", primary_href="contact.html", primary_label="Essai gratuit", secondary_href="fonctionnalites.html", secondary_label="Fonctionnalités")
    main += block_pricing_tiers("Choisissez votre plan", QB_PRICING)
    main += block_cta_band("14 jours gratuits.", "Démarrer", "contact.html")
    main += "</main>"
    return _shell_saas_empty("tarifs.html", f"Tarifs — {QB_BRAND}", "Tarifs QueryBase.", main)


def build_saas_empty_contact() -> str:
    main = """<main>
<section class="vt-hero-compact py-5 text-center vt-reveal">
  <div class="container">
    <p class="vt-eyebrow text-uppercase">Essai</p>
    <h1 class="vt-display display-6">14 jours gratuits</h1>
    <p class="lead text-secondary">Sans carte bancaire.</p>
  </div>
</section>"""
    main += block_saas_trial_form(brand=QB_BRAND, email=QB_EMAIL)
    main += block_cta_band("Démonstration — aucune donnée transmise.", "Retour accueil", "index.html")
    main += "</main>"
    return _shell_saas_empty("contact.html", f"Contact — {QB_BRAND}", "Essai gratuit QueryBase.", main)


# --- PingFlow (saas-notifications) — feed cascade + tabs ---
PF_BRAND = "PingFlow"
PF_EMAIL = "hello@pingflow.io"
PF_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "fonctionnalites.html", "label": "Fonctionnalités"},
    {"file": "tarifs.html", "label": "Tarifs"},
    {"file": "contact.html", "label": "Contact"},
]
PF_FOOTER_NAV = [
    ("Fonctionnalités", "fonctionnalites.html"),
    ("Tarifs", "tarifs.html"),
    ("Essai gratuit", "contact.html"),
    ("RGPD", "fonctionnalites.html"),
]
PF_NOTIFS = [
    {"type": "Action requise", "title": "Valider la release v2.4", "text": "3 reviewers en attente — deadline demain.", "time": "Il y a 5 min", "urgent": True},
    {"type": "Équipe", "title": "Marie a commenté le brief", "text": "Nouveau message sur le dashboard Q2.", "time": "Il y a 1 h", "urgent": False},
    {"type": "Produit", "title": "Nouveau connecteur Slack", "text": "Disponible dans les intégrations.", "time": "Il y a 3 h", "urgent": False},
    {"type": "Système", "title": "Maintenance planifiée", "text": "Dimanche 3h–5h — aucun impact données.", "time": "Hier", "urgent": False},
]
PF_TABS = [
    {"label": "Inbox", "title": "Centre de notifications unifié", "text": "Filtres par type — action requise, équipe, produit.", "img": "scene-1.png", "alt": "Inbox"},
    {"label": "Routing", "title": "Règles d'alerte configurables", "text": "Triggers, canaux et priorités sans code.", "img": "scene-2.png", "alt": "Routing"},
    {"label": "Push", "title": "Slack, email et webhooks", "text": "Multi-canal avec préférences granulaires.", "img": "scene-3.png", "alt": "Push"},
]
PF_PRICING = [
    {"name": "Starter", "price": "39 €/mois", "features": ["3 utilisateurs", "In-app + email", "Filtres basiques"], "href": "contact.html", "cta": "Essai gratuit", "hot": False},
    {"name": "Pro", "price": "129 €/mois", "features": ["20 utilisateurs", "Slack + webhooks", "Analytics"], "href": "contact.html", "cta": "Essai gratuit", "hot": True},
    {"name": "Enterprise", "price": "Sur devis", "features": ["SSO", "SLA 99.9 %", "Audit log"], "href": "contact.html", "cta": "Nous contacter", "hot": False},
]


def _shell_saas_notifications(page: str, title: str, desc: str, main: str) -> str:
    nav = _chrome_nav("saas-notifications", PF_BRAND, PF_NAV, page, cta_label="Essai gratuit", cta_href="contact.html")
    foot = _chrome_foot("saas-notifications", PF_BRAND, phone="", address="SaaS notifications · Hébergé en France", email=PF_EMAIL, maps_href="#", nav_links=PF_FOOTER_NAV, hours_line="Support chat 9h–18h")
    mobile = block_mobile_cta("Essai gratuit", "contact.html", "")
    return wrap_page_saas(
        title, desc, nav + main + foot + mobile,
        layout="saas-notifications", slug="saas-notifications", page=page, site_name=PF_BRAND, nav=PF_NAV,
        brand=PF_BRAND, brand_desc="Centre notifications in-app",
        head_assets=HEAD_SAAS_NOTIFICATIONS, body_class="vt-body vt-body-saas-notifications",
    )


def build_saas_notifications_index() -> str:
    main = "<main>"
    main += """<section class="vt-saas-hero vt-reveal">
  <div class="container">
    <div class="row g-4 g-xl-5 align-items-start">
      <div class="col-lg-6">
        <p class="vt-eyebrow mb-2">SaaS · Notifications in-app</p>
        <h1 class="vt-display display-4 mb-3">Des notifs qui respectent l'attention</h1>
        <p class="lead mb-4">Hierarchie claire, actions en avant, preferences anti-spam.</p>
        <div class="d-flex flex-wrap gap-2">
          <button type="button" class="btn btn-vt-primary btn-lg" data-vt-dialog-open="essaiPf">Essai gratuit 14 j</button>
          <a class="btn btn-vt-outline btn-lg" href="fonctionnalites.html">Fonctionnalites</a>
        </div>
      </div>
      <div class="col-lg-6">
        <div class="d-flex flex-column gap-2">
          <article class="vt-notif-card urgent"><div class="meta"><span class="badge-u">Action requise</span><span>Il y a 5 min</span></div><strong class="d-block">Valider la release v2.4</strong><p class="small text-secondary mb-0">3 reviewers en attente.</p></article>
          <article class="vt-notif-card"><div class="meta"><span>Equipe</span><span>Il y a 1 h</span></div><strong class="d-block">Marie a commente le brief</strong><p class="small text-secondary mb-0">Nouveau message sur le dashboard Q2.</p></article>
          <article class="vt-notif-card"><div class="meta"><span>Produit</span><span>Il y a 3 h</span></div><strong class="d-block">Nouveau connecteur Slack</strong><p class="small text-secondary mb-0">Dispo dans les integrations.</p></article>
        </div>
      </div>
    </div>
  </div>
</section>"""
    main += block_marquee_m3(["Slack", "Email", "Webhooks", "RGPD", "SOC 2", "API"])
    main += block_dialog_m3(
        dialog_id="essaiPf",
        title="Essai gratuit 14 jours",
        lead="Sans CB - inbox demo avec routing inclus.",
        primary_label="Demarrer",
        primary_href="contact.html",
        fields_html='<div class="mb-2"><label class="form-label small">Email pro</label><input class="form-control" type="email"></div>',
    )
    main += block_fab_menu_m3([
        {"label": "Essai", "dialog": "essaiPf"},
        {"label": "Features", "href": "fonctionnalites.html"},
        {"label": "Tarifs", "href": "tarifs.html"},
    ], main_label="Actions PingFlow")
    main += "</main>"
    return _shell_saas_notifications("index.html", f"{PF_BRAND} — Notifications in-app", "PingFlow — centre de notifications hiérarchisé et actionnable.", main)


def build_saas_notifications_fonctionnalites() -> str:
    main = "<main>"
    main += block_hero_split("Fonctionnalités notifications", "Filtres, routing et préférences — le bon message au bon moment.", "hero.png", "Fonctionnalités PingFlow", eyebrow="Fonctionnalités", primary_href="contact.html", primary_label="Essai gratuit", secondary_href="tarifs.html", secondary_label="Tarifs")
    main += block_bento_cards([
        {"title": "Toasts", "text": "Success, warning, info — variants cohérents.", "img": "gallery-1.png", "alt": "Toasts", "size": "lg"},
        {"title": "Mobile push", "text": "Preview lock screen et in-app.", "img": "gallery-2.png", "alt": "Mobile", "size": "sm"},
        {"title": "Sécurité", "text": "Alertes incident et timeline.", "img": "card-3.png", "alt": "Sécurité", "size": "sm"},
    ])
    main += block_spec_grid("Modules", [
        {"label": "Inbox", "value": "Unifiée", "detail": "Unread, mark all read, filtres."},
        {"label": "Routing", "value": "Règles", "detail": "Triggers et canaux sans code."},
        {"label": "Préférences", "value": "Granulaire", "detail": "Quiet hours et opt-out."},
        {"label": "Analytics", "value": "Live", "detail": "Open rates et temps de réponse."},
    ])
    main += block_comparison_table("Avant / après PingFlow", [
        ("Volume perçu", "Surcharge", "Hiérarchisé"),
        ("Actions", "Passives", "CTA intégrés"),
        ("Consentement", "Ignoré", "Préférences respectées"),
    ])
    main += block_cta_band("Testez toutes les fonctionnalités.", "Essai gratuit", "contact.html")
    main += "</main>"
    return _shell_saas_notifications("fonctionnalites.html", f"Fonctionnalités — {PF_BRAND}", "Fonctionnalités PingFlow.", main)


def build_saas_notifications_tarifs() -> str:
    main = "<main>"
    main += block_hero_editorial("Tarifs adaptés à votre volume", "Starter pour démarrer — Pro pour le multi-canal.", "hero.png", "Tarifs PingFlow", eyebrow="Tarifs", primary_href="contact.html", primary_label="Essai gratuit", secondary_href="fonctionnalites.html", secondary_label="Fonctionnalités")
    main += block_pricing_tiers("Choisissez votre plan", PF_PRICING)
    main += block_faq_accordion("FAQ", [
        ("Limite notifications ?", "Illimitées sur tous les plans."),
        ("RGPD ?", "Consentement et rétention configurables."),
        ("Intégration Slack ?", "Native sur Pro et Enterprise."),
    ])
    main += block_cta_band("14 jours gratuits.", "Démarrer", "contact.html")
    main += "</main>"
    return _shell_saas_notifications("tarifs.html", f"Tarifs — {PF_BRAND}", "Tarifs PingFlow.", main)


def build_saas_notifications_contact() -> str:
    main = """<main>
<section class="vt-hero-compact py-5 text-center vt-reveal">
  <div class="container">
    <p class="vt-eyebrow text-uppercase">Essai</p>
    <h1 class="vt-display display-6">14 jours gratuits</h1>
    <p class="lead text-secondary">Sans carte bancaire.</p>
  </div>
</section>"""
    main += block_saas_trial_form(brand=PF_BRAND, email=PF_EMAIL)
    main += block_cta_band("Démonstration — aucune donnée transmise.", "Retour accueil", "index.html")
    main += "</main>"
    return _shell_saas_notifications("contact.html", f"Contact — {PF_BRAND}", "Essai gratuit PingFlow.", main)


BUILDERS = {
    "restauration": [
        ("index.html", build_index),
        ("carte.html", build_carte),
        ("histoire.html", build_histoire),
        ("contact.html", build_contact),
    ],
    "beaute": [
        ("index.html", build_beaute_index),
        ("soins.html", build_beaute_soins),
        ("ambiance.html", build_beaute_ambiance),
        ("contact.html", build_beaute_contact),
    ],
    "odontologie": [
        ("index.html", build_odontologie_index),
        ("soins.html", build_odontologie_soins),
        ("equipe.html", build_odontologie_equipe),
        ("contact.html", build_odontologie_contact),
    ],
    "automobile": [
        ("index.html", build_automobile_index),
        ("services.html", build_automobile_services),
        ("atelier.html", build_automobile_atelier),
        ("contact.html", build_automobile_contact),
    ],
    "commerce": [
        ("index.html", build_commerce_index),
        ("rayons.html", build_commerce_rayons),
        ("drive.html", build_commerce_drive),
        ("contact.html", build_commerce_contact),
    ],
    "comptable": [
        ("index.html", build_comptable_index),
        ("expertises.html", build_comptable_expertises),
        ("methode.html", build_comptable_methode),
        ("contact.html", build_comptable_contact),
    ],
    "industrie": [
        ("index.html", build_industrie_index),
        ("savoir-faire.html", build_industrie_savoir_faire),
        ("qualite.html", build_industrie_qualite),
        ("contact.html", build_industrie_contact),
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
    "architecture": [
        ("index.html", build_architecture_index),
        ("projets.html", build_architecture_projets),
        ("methode.html", build_architecture_methode),
        ("contact.html", build_architecture_contact),
    ],
    "fitness": [
        ("index.html", build_fitness_index),
        ("cours.html", build_fitness_cours),
        ("tarifs.html", build_fitness_tarifs),
        ("contact.html", build_fitness_contact),
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
    "saas-landing": [
        ("index.html", build_saas_landing_index),
        ("fonctionnalites.html", build_saas_landing_fonctionnalites),
        ("tarifs.html", build_saas_landing_tarifs),
        ("contact.html", build_saas_landing_contact),
    ],
    "saas-onboarding": [
        ("index.html", build_saas_onboarding_index),
        ("parcours.html", build_saas_onboarding_parcours),
        ("fonctionnalites.html", build_saas_onboarding_fonctionnalites),
        ("contact.html", build_saas_onboarding_contact),
    ],
    "saas-dashboard": [
        ("index.html", build_saas_dashboard_index),
        ("fonctionnalites.html", build_saas_dashboard_fonctionnalites),
        ("tarifs.html", build_saas_dashboard_tarifs),
        ("contact.html", build_saas_dashboard_contact),
    ],
    "saas-empty": [
        ("index.html", build_saas_empty_index),
        ("fonctionnalites.html", build_saas_empty_fonctionnalites),
        ("tarifs.html", build_saas_empty_tarifs),
        ("contact.html", build_saas_empty_contact),
    ],
    "saas-notifications": [
        ("index.html", build_saas_notifications_index),
        ("fonctionnalites.html", build_saas_notifications_fonctionnalites),
        ("tarifs.html", build_saas_notifications_tarifs),
        ("contact.html", build_saas_notifications_contact),
    ],
}
BUILDERS.update(BUILDERS_EXTRA)


def main() -> None:
    slug = sys.argv[1] if len(sys.argv) > 1 else "restauration"
    if slug == "--all":
        for s in BUILDERS:
            dest = OUT / s
            dest.mkdir(parents=True, exist_ok=True)
            for fname, fn in BUILDERS[s]:
                (dest / fname).write_text(fn(), encoding="utf-8")
                print(f"[OK] {dest.relative_to(ROOT) / fname}")
        return
    pages = BUILDERS.get(slug)
    if not pages:
        raise SystemExit(f"Slug inconnu : {slug}. Disponibles : {', '.join(BUILDERS)}")
    dest = OUT / slug
    dest.mkdir(parents=True, exist_ok=True)
    for fname, fn in pages:
        (dest / fname).write_text(fn(), encoding="utf-8")
        print(f"[OK] {dest.relative_to(ROOT) / fname}")


if __name__ == "__main__":
    main()
