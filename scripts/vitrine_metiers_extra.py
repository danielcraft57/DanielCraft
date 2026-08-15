"""Builders pour 5 nouveaux metiers echantillons (boulangerie, artisan, fleuriste, caviste, osteo)."""
from __future__ import annotations

from vitrine_layouts import (
    block_dialog_m3,
    block_fab_menu_m3,
    block_marquee_m3,
)
from vitrine_seo import get_entity
from vitrine_site_blocks import (
    block_info_bar,
    block_mobile_cta,
    block_site_footer,
    block_site_nav,
    wrap_page,
)

_BOOT = """
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <link rel="stylesheet" href="../shared/vitrine-prose.css">
  <link rel="stylesheet" href="../shared/vitrine-images.css">
  <link rel="stylesheet" href="../shared/vitrine-motion.css">
  <link rel="icon" href="images/icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="stylesheet" href="styles.css">"""

HEAD_BOULANGERIE = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">
{_BOOT}"""

HEAD_ARTISAN = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
{_BOOT}"""

HEAD_FLEURISTE = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Nunito+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
{_BOOT}"""

HEAD_CAVISTE = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
{_BOOT}"""

HEAD_OSTEO = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
{_BOOT}"""


def _nav(brand, nav, page, cta_label, cta_href, slug):
    return block_site_nav(brand, nav, page, cta_label=cta_label, cta_href=cta_href, slug=slug)


def _foot(slug, brand, **kw):
    return block_site_footer(brand, entity=get_entity(slug), slug=slug, **kw)


# --- Boulangerie : Maison Lemaire (Nancy) ---
BL_BRAND = "Maison Lemaire"
BL_PHONE = "03 83 35 12 40"
BL_EMAIL = "bonjour@maison-lemaire.fr"
BL_ADDRESS = "14 allee de la Pepiniere, 54000 Nancy"
BL_MAPS = "https://maps.google.com/?q=14+allee+de+la+Pepiniere+54000+Nancy"
BL_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "pains.html", "label": "Pains"},
    {"file": "patisseries.html", "label": "Patisseries"},
    {"file": "contact.html", "label": "Contact"},
]
BL_FOOT = [("Pains", "pains.html"), ("Patisseries", "patisseries.html"), ("Commander", "contact.html"), ("Horaires", "contact.html")]


def _shell_bl(page, title, desc, main):
    bar = block_info_bar(status="Ouvert · Mar-dim 7h-19h", address=BL_ADDRESS, phone=BL_PHONE, maps_href=BL_MAPS)
    nav = _nav(BL_BRAND, BL_NAV, page, "Commander", "contact.html", "boulangerie")
    foot = _foot("boulangerie", BL_BRAND, phone=BL_PHONE, address=BL_ADDRESS, email=BL_EMAIL, maps_href=BL_MAPS, nav_links=BL_FOOT, hours_line="Nancy · Fournil")
    mobile = block_mobile_cta("Commander", "contact.html", BL_PHONE)
    return wrap_page(title, desc, bar + nav + main + foot + mobile, layout="boulangerie-m3", slug="boulangerie", page=page, site_name=BL_BRAND, nav=BL_NAV, head_assets=HEAD_BOULANGERIE, body_class="vt-body vt-body-boulangerie")


def build_boulangerie_index():
    main = "<main>"
    main += """<section class="vt-bakery-hero vt-reveal">
  <div class="container">
    <p class="vt-eyebrow mb-2">Fournil · Nancy</p>
    <h1 class="vt-display display-4 mb-3">Du levain, du temps, et beaucoup d'amour</h1>
    <p class="lead mb-4">Pains au levain naturel, faconnes a la main chaque jour a Nancy.</p>
    <div class="d-flex flex-wrap gap-2 mb-4">
      <button type="button" class="btn btn-vt-primary btn-lg" data-vt-dialog-open="cmdBl">Commander</button>
      <a class="btn btn-vt-outline btn-lg" href="pains.html">Voir les pains</a>
    </div>
    <div class="d-flex flex-wrap gap-2 mb-4">
      <span class="vt-chip on">Pains au levain</span><span class="vt-chip">Viennoiseries</span><span class="vt-chip">Patisseries</span><span class="vt-chip">Sandwichs</span>
    </div>
    <div class="row g-3 vt-reveal-stagger">
      <div class="col-6 col-lg-3"><article class="vt-bakery-card"><picture><source srcset="images/card-1.webp" type="image/webp"><img src="images/card-1.png" alt="Pain de campagne" loading="lazy"></picture><div class="p-3"><h3 class="h6 mb-1">Pain de campagne</h3><p class="small text-secondary mb-0">4,20 euro</p></div></article></div>
      <div class="col-6 col-lg-3"><article class="vt-bakery-card"><picture><source srcset="images/card-2.webp" type="image/webp"><img src="images/card-2.png" alt="Croissant" loading="lazy"></picture><div class="p-3"><h3 class="h6 mb-1">Croissant pur beurre</h3><p class="small text-secondary mb-0">1,60 euro</p></div></article></div>
      <div class="col-6 col-lg-3"><article class="vt-bakery-card"><picture><source srcset="images/card-3.webp" type="image/webp"><img src="images/card-3.png" alt="Tarte citron" loading="lazy"></picture><div class="p-3"><h3 class="h6 mb-1">Tarte au citron</h3><p class="small text-secondary mb-0">3,90 euro</p></div></article></div>
      <div class="col-6 col-lg-3"><article class="vt-bakery-card"><picture><source srcset="images/gallery-1.webp" type="image/webp"><img src="images/gallery-1.png" alt="Sandwich" loading="lazy"></picture><div class="p-3"><h3 class="h6 mb-1">Sandwich du jour</h3><p class="small text-secondary mb-0">6,50 euro</p></div></article></div>
    </div>
  </div>
</section>"""
    main += block_dialog_m3(dialog_id="cmdBl", title="Commander", lead="Retrait au fournil - on te confirme (demo).", primary_label="Envoyer", primary_href="contact.html", fields_html='<div class="mb-2"><label class="form-label small">Produit</label><select class="form-select"><option>Pain de campagne</option><option>Croissants x4</option><option>Assortiment</option></select></div><div class="mb-2"><label class="form-label small">Heure de retrait</label><input class="form-control" type="time" value="11:30"></div>')
    main += block_fab_menu_m3([{"label": "Commander", "dialog": "cmdBl"}, {"label": "Pains", "href": "pains.html"}, {"label": "Appeler", "href": "tel:0383351240"}], main_label="Actions fournil")
    main += "</main>"
    return _shell_bl("index.html", f"{BL_BRAND} — Boulangerie Nancy", "Boulangerie artisanale a Nancy : pains au levain, viennoiseries et patisseries.", main)


def build_boulangerie_pains():
    main = f"""<main><section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Pains</p><h1 class="vt-display h2 mb-3">Levain naturel, cuisson de nuit</h1><p class="lead text-secondary mb-4">Campagne, seigle, complets - farines locales.</p><div class="row g-3"><div class="col-md-4"><article class="vt-bakery-card"><picture><source srcset="images/scene-1.webp" type="image/webp"><img src="images/scene-1.png" alt="Levain" loading="lazy"></picture><div class="p-3"><h2 class="h6">Campagne 800 g</h2><p class="small text-secondary mb-0">Croute epaisse, mie alveolee.</p></div></article></div><div class="col-md-4"><article class="vt-bakery-card"><picture><source srcset="images/scene-2.webp" type="image/webp"><img src="images/scene-2.png" alt="Seigle" loading="lazy"></picture><div class="p-3"><h2 class="h6">Seigle</h2><p class="small text-secondary mb-0">Ideal fromages et tartines.</p></div></article></div><div class="col-md-4"><article class="vt-bakery-card"><picture><source srcset="images/scene-3.webp" type="image/webp"><img src="images/scene-3.png" alt="Complet" loading="lazy"></picture><div class="p-3"><h2 class="h6">Complet</h2><p class="small text-secondary mb-0">Farine stone-ground.</p></div></article></div></div><a class="btn btn-vt-primary mt-4" href="contact.html">Commander</a></div></section></main>"""
    return _shell_bl("pains.html", f"Pains — {BL_BRAND}", "Pains au levain Maison Lemaire Nancy.", main)


def build_boulangerie_patisseries():
    main = f"""<main><section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Patisseries</p><h1 class="vt-display h2 mb-3">Du croissant au schneck</h1><p class="lead text-secondary mb-4">Beurre AOP, mirabelle en saison.</p><a class="btn btn-vt-primary" href="contact.html">Reserver un gateau</a></div></section></main>"""
    return _shell_bl("patisseries.html", f"Patisseries — {BL_BRAND}", "Patisseries et viennoiseries Maison Lemaire.", main)


def build_boulangerie_contact():
    main = f"""<main><section class="py-5 text-center vt-reveal"><div class="container"><p class="vt-eyebrow">Contact</p><h1 class="vt-display h2">Passer commande</h1><p class="lead text-secondary">{BL_ADDRESS}</p><p><a class="btn btn-vt-primary" href="tel:0383351240">{BL_PHONE}</a></p><p class="small text-secondary">{BL_EMAIL}</p></div></section></main>"""
    return _shell_bl("contact.html", f"Contact — {BL_BRAND}", "Commander chez Maison Lemaire Nancy.", main)


# --- Artisan : Clanche & Cuivre (Metz) ---
AR_BRAND = "Clanche & Cuivre"
AR_PHONE = "03 87 21 90 40"
AR_EMAIL = "urgence@clanche-cuivre.fr"
AR_ADDRESS = "Zone artisanale Nord, 57070 Metz"
AR_MAPS = "https://maps.google.com/?q=Metz+57070"
AR_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "services.html", "label": "Services"},
    {"file": "zones.html", "label": "Zones"},
    {"file": "contact.html", "label": "Contact"},
]
AR_FOOT = [("Services", "services.html"), ("Zones", "zones.html"), ("Devis", "contact.html"), ("Urgence", "tel:0387219040")]


def _shell_ar(page, title, desc, main):
    bar = block_info_bar(status="Urgence 24/7 · Metz", address=AR_ADDRESS, phone=AR_PHONE, maps_href=AR_MAPS)
    nav = _nav(AR_BRAND, AR_NAV, page, "Devis gratuit", "contact.html", "artisan")
    foot = _foot("artisan", AR_BRAND, phone=AR_PHONE, address=AR_ADDRESS, email=AR_EMAIL, maps_href=AR_MAPS, nav_links=AR_FOOT, hours_line="Metz · Plomberie")
    mobile = block_mobile_cta("Appeler", "tel:0387219040", AR_PHONE)
    return wrap_page(title, desc, bar + nav + main + foot + mobile, layout="artisan-m3", slug="artisan", page=page, site_name=AR_BRAND, nav=AR_NAV, head_assets=HEAD_ARTISAN, body_class="vt-body vt-body-artisan")


def build_artisan_index():
    main = "<main>"
    main += """<section class="vt-art-hero vt-reveal">
  <div class="container">
    <div class="row g-4 align-items-start">
      <div class="col-lg-6">
        <p class="vt-eyebrow mb-2">Plombier · Metz</p>
        <h1 class="vt-display display-4 mb-3">Intervention rapide 24h/24</h1>
        <p class="lead mb-3">Depannage, salle de bain, chauffage - arrivee moyenne 30 min.</p>
        <ul class="vt-art-bullets mb-4"><li>24h/24 · 7j/7</li><li>Devis clair avant travaux</li><li>Travail garanti</li></ul>
        <div class="d-flex flex-wrap gap-2">
          <button type="button" class="btn btn-vt-primary btn-lg" data-vt-dialog-open="devisArt">Devis gratuit</button>
          <a class="btn btn-vt-outline btn-lg" href="tel:0387219040">Appeler</a>
        </div>
      </div>
      <div class="col-lg-6">
        <div class="vt-art-form">
          <h2 class="h5 mb-2">Demande de devis</h2>
          <p class="small text-secondary mb-3">Reponse sous 30 min (demo).</p>
          <button type="button" class="btn btn-vt-primary w-100" data-vt-dialog-open="devisArt">Ouvrir le formulaire</button>
        </div>
      </div>
    </div>
    <div class="row g-3 mt-4">
      <div class="col-md-3"><article class="vt-art-svc"><picture><source srcset="images/card-1.webp" type="image/webp"><img src="images/card-1.png" alt="Depannage" loading="lazy"></picture><h3 class="h6 mt-2">Depannage</h3></article></div>
      <div class="col-md-3"><article class="vt-art-svc"><picture><source srcset="images/card-2.webp" type="image/webp"><img src="images/card-2.png" alt="SDB" loading="lazy"></picture><h3 class="h6 mt-2">Salle de bain</h3></article></div>
      <div class="col-md-3"><article class="vt-art-svc"><picture><source srcset="images/card-3.webp" type="image/webp"><img src="images/card-3.png" alt="Chauffage" loading="lazy"></picture><h3 class="h6 mt-2">Chauffage</h3></article></div>
      <div class="col-md-3"><article class="vt-art-svc"><picture><source srcset="images/scene-1.webp" type="image/webp"><img src="images/scene-1.png" alt="Chaudiere" loading="lazy"></picture><h3 class="h6 mt-2">Chaudiere</h3></article></div>
    </div>
  </div>
</section>"""
    main += block_dialog_m3(dialog_id="devisArt", title="Devis gratuit", lead="Decris le souci - on te rappelle (demo).", primary_label="Envoyer", primary_href="contact.html", fields_html='<div class="mb-2"><label class="form-label small">Type</label><select class="form-select"><option>Fuite</option><option>Debouchage</option><option>Chauffage</option><option>Salle de bain</option></select></div><div class="mb-2"><label class="form-label small">Telephone</label><input class="form-control" type="tel"></div>')
    main += block_fab_menu_m3([{"label": "Devis", "dialog": "devisArt"}, {"label": "Appeler", "href": "tel:0387219040"}, {"label": "Zones", "href": "zones.html"}], main_label="Actions urgence")
    main += "</main>"
    return _shell_ar("index.html", f"{AR_BRAND} — Plombier Metz", "Plombier urgence a Metz : depannage 24/7, devis clair.", main)


def build_artisan_services():
    main = """<main><section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Services</p><h1 class="vt-display h2 mb-3">Ce qu'on prend en charge</h1><div class="row g-3"><div class="col-md-4"><article class="vt-art-svc p-3"><h2 class="h6">Depannage</h2><p class="small text-secondary mb-0">Fuite, WC, robinetterie.</p></article></div><div class="col-md-4"><article class="vt-art-svc p-3"><h2 class="h6">Renovation SDB</h2><p class="small text-secondary mb-0">Du devis a la reception.</p></article></div><div class="col-md-4"><article class="vt-art-svc p-3"><h2 class="h6">Chauffage</h2><p class="small text-secondary mb-0">Entretien et remplacement.</p></article></div></div></div></section></main>"""
    return _shell_ar("services.html", f"Services — {AR_BRAND}", "Services plomberie Clanche & Cuivre Metz.", main)


def build_artisan_zones():
    main = """<main><section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Zones</p><h1 class="vt-display h2 mb-3">Metz et alentours</h1><p class="lead text-secondary">Metz, Montigny, Woippy, Longeville, Plappeville - 30 min en moyenne.</p></div></section></main>"""
    return _shell_ar("zones.html", f"Zones — {AR_BRAND}", "Zones d'intervention plombier Metz.", main)


def build_artisan_contact():
    main = f"""<main><section class="py-5 text-center vt-reveal"><div class="container"><p class="vt-eyebrow">Contact</p><h1 class="vt-display h2">Urgence ou devis</h1><p class="lead text-secondary">{AR_ADDRESS}</p><p><a class="btn btn-vt-primary" href="tel:0387219040">{AR_PHONE}</a></p></div></section></main>"""
    return _shell_ar("contact.html", f"Contact — {AR_BRAND}", "Contacter Clanche & Cuivre Metz.", main)


# --- Fleuriste : Atelier Corolle (Strasbourg) ---
FL_BRAND = "Atelier Corolle"
FL_PHONE = "03 88 24 17 50"
FL_EMAIL = "bonjour@atelier-corolle.fr"
FL_ADDRESS = "22 rue de l'Orangerie, 67000 Strasbourg"
FL_MAPS = "https://maps.google.com/?q=22+rue+de+l+Orangerie+67000+Strasbourg"
FL_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "collections.html", "label": "Collections"},
    {"file": "mariage.html", "label": "Mariage"},
    {"file": "contact.html", "label": "Contact"},
]
FL_FOOT = [("Collections", "collections.html"), ("Mariage", "mariage.html"), ("Livraison", "contact.html"), ("Atelier", "contact.html")]


def _shell_fl(page, title, desc, main):
    bar = block_info_bar(status="Livraison Orangerie · Strasbourg", address=FL_ADDRESS, phone=FL_PHONE, maps_href=FL_MAPS)
    nav = _nav(FL_BRAND, FL_NAV, page, "Commander", "contact.html", "fleuriste")
    foot = _foot("fleuriste", FL_BRAND, phone=FL_PHONE, address=FL_ADDRESS, email=FL_EMAIL, maps_href=FL_MAPS, nav_links=FL_FOOT, hours_line="Strasbourg · Fleuriste")
    mobile = block_mobile_cta("Commander", "contact.html", FL_PHONE)
    return wrap_page(title, desc, bar + nav + main + foot + mobile, layout="fleuriste-m3", slug="fleuriste", page=page, site_name=FL_BRAND, nav=FL_NAV, head_assets=HEAD_FLEURISTE, body_class="vt-body vt-body-fleuriste")


def build_fleuriste_index():
    main = "<main>"
    main += """<section class="vt-flor-hero vt-reveal">
  <div class="container">
    <div class="row g-4 align-items-center">
      <div class="col-lg-6">
        <p class="vt-eyebrow mb-2">Fleuriste · Strasbourg</p>
        <h1 class="vt-display display-4 mb-3">Fleurs locales, emotions durables</h1>
        <p class="lead mb-4">Compositions de saison, mariage et livraison quartier Orangerie.</p>
        <div class="d-flex flex-wrap gap-2 mb-3">
          <button type="button" class="btn btn-vt-primary" data-vt-dialog-open="cmdFl">Saison</button>
          <a class="btn btn-vt-outline" href="mariage.html">Mariage</a>
          <a class="btn btn-vt-outline" href="contact.html">Livraison</a>
        </div>
      </div>
      <div class="col-lg-6">
        <figure class="vt-flor-media mb-0"><picture><source srcset="images/hero.webp" type="image/webp"><img src="images/hero.png" alt="Bouquet Atelier Corolle" decoding="async" fetchpriority="high"></picture></figure>
      </div>
    </div>
    <div class="row g-3 mt-4">
      <div class="col-md-4"><article class="vt-flor-card"><picture><source srcset="images/card-1.webp" type="image/webp"><img src="images/card-1.png" alt="Collection" loading="lazy"></picture><div class="vt-flor-card-body"><span class="small">COLLECTION</span><h3 class="h6">Douceur de printemps</h3><p class="small mb-0">A partir de 45 euro</p></div></article></div>
      <div class="col-md-4"><article class="vt-flor-card"><picture><source srcset="images/card-2.webp" type="image/webp"><img src="images/card-2.png" alt="Bouquet" loading="lazy"></picture><div class="vt-flor-card-body"><span class="small">BOUQUET</span><h3 class="h6">Champetre local</h3><p class="small mb-0">A partir de 38 euro</p></div></article></div>
      <div class="col-md-4"><article class="vt-flor-card"><picture><source srcset="images/card-3.webp" type="image/webp"><img src="images/card-3.png" alt="Composition" loading="lazy"></picture><div class="vt-flor-card-body"><span class="small">COMPOSITION</span><h3 class="h6">Table d'hotes</h3><p class="small mb-0">A partir de 55 euro</p></div></article></div>
    </div>
  </div>
</section>"""
    main += block_dialog_m3(dialog_id="cmdFl", title="Commander un bouquet", lead="Livraison Strasbourg centre (demo).", primary_label="Continuer", primary_href="contact.html", fields_html='<div class="mb-2"><label class="form-label small">Occasion</label><select class="form-select"><option>Saison</option><option>Anniversaire</option><option>Remerciement</option></select></div>')
    main += block_fab_menu_m3([{"label": "Commander", "dialog": "cmdFl"}, {"label": "Collections", "href": "collections.html"}, {"label": "Mariage", "href": "mariage.html"}], main_label="Actions atelier")
    main += "</main>"
    return _shell_fl("index.html", f"{FL_BRAND} — Fleuriste Strasbourg", "Fleuriste a Strasbourg : bouquets de saison, mariage, livraison.", main)


def build_fleuriste_collections():
    main = """<main><section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Collections</p><h1 class="vt-display h2 mb-3">Inspirations du moment</h1><p class="lead text-secondary">Saisons, couleurs, formats - on compose sur place.</p></div></section></main>"""
    return _shell_fl("collections.html", f"Collections — {FL_BRAND}", "Collections florales Atelier Corolle.", main)


def build_fleuriste_mariage():
    main = """<main><section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Mariage</p><h1 class="vt-display h2 mb-3">Le jour J, en fleurs</h1><p class="lead text-secondary">Bouquet de mariee, boutonnières, arch - devis sur rendez-vous.</p><a class="btn btn-vt-primary" href="contact.html">Parler mariage</a></div></section></main>"""
    return _shell_fl("mariage.html", f"Mariage — {FL_BRAND}", "Fleurs de mariage Atelier Corolle Strasbourg.", main)


def build_fleuriste_contact():
    main = f"""<main><section class="py-5 text-center vt-reveal"><div class="container"><p class="vt-eyebrow">Contact</p><h1 class="vt-display h2">Passer a l'atelier</h1><p class="lead text-secondary">{FL_ADDRESS}</p><p><a class="btn btn-vt-primary" href="tel:0388241750">{FL_PHONE}</a></p></div></section></main>"""
    return _shell_fl("contact.html", f"Contact — {FL_BRAND}", "Contacter Atelier Corolle Strasbourg.", main)


# --- Caviste : Cave de la Gare (Thionville) ---
CV_BRAND = "Cave de la Gare"
CV_PHONE = "03 82 53 18 90"
CV_EMAIL = "cave@cavedelagare.fr"
CV_ADDRESS = "5 place de la Gare, 57100 Thionville"
CV_MAPS = "https://maps.google.com/?q=5+place+de+la+Gare+57100+Thionville"
CV_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "vins.html", "label": "Vins"},
    {"file": "cave.html", "label": "La cave"},
    {"file": "contact.html", "label": "Contact"},
]
CV_FOOT = [("Vins", "vins.html"), ("La cave", "cave.html"), ("Conseils", "contact.html"), ("Panier", "contact.html")]


def _shell_cv(page, title, desc, main):
    bar = block_info_bar(status="Degustations samedi · Thionville", address=CV_ADDRESS, phone=CV_PHONE, maps_href=CV_MAPS)
    nav = _nav(CV_BRAND, CV_NAV, page, "Mon panier", "contact.html", "caviste")
    foot = _foot("caviste", CV_BRAND, phone=CV_PHONE, address=CV_ADDRESS, email=CV_EMAIL, maps_href=CV_MAPS, nav_links=CV_FOOT, hours_line="Thionville · Caviste")
    mobile = block_mobile_cta("Conseiller", "contact.html", CV_PHONE)
    return wrap_page(title, desc, bar + nav + main + foot + mobile, layout="caviste-m3", slug="caviste", page=page, site_name=CV_BRAND, nav=CV_NAV, head_assets=HEAD_CAVISTE, body_class="vt-body vt-body-caviste")


def build_caviste_index():
    main = "<main>"
    main += """<section class="vt-cave-hero vt-reveal">
  <div class="container">
    <p class="vt-eyebrow mb-2">Caviste · Thionville</p>
    <h1 class="vt-display display-4 mb-3">Des vins choisis, pas un rayon geant</h1>
    <p class="lead mb-4">48 references soignees - Lorraine, France, petites maisons.</p>
    <div class="d-flex flex-wrap gap-2 mb-4">
      <button type="button" class="btn btn-vt-primary btn-lg" data-vt-dialog-open="panierCv">Ajouter au panier</button>
      <a class="btn btn-vt-outline btn-lg" href="vins.html">Tous les vins</a>
    </div>
    <div class="row g-3">
      <div class="col-md-6"><article class="vt-cave-card"><div class="d-flex gap-3"><picture><source srcset="images/card-1.webp" type="image/webp"><img src="images/card-1.png" alt="Rouge" loading="lazy"></picture><div><span class="vt-cave-tag">ROUGE</span><h3 class="h6 mb-1">Domaine des Terres Noires 2021</h3><p class="small text-secondary mb-1">Cotes de Toul · Pinot noir</p><strong class="vt-cave-price">24,50 euro</strong></div></div></article></div>
      <div class="col-md-6"><article class="vt-cave-card"><div class="d-flex gap-3"><picture><source srcset="images/card-2.webp" type="image/webp"><img src="images/card-2.png" alt="Blanc" loading="lazy"></picture><div><span class="vt-cave-tag">BLANC</span><h3 class="h6 mb-1">Auxerrois Moselle</h3><p class="small text-secondary mb-1">AOC Moselle · 75 cl</p><strong class="vt-cave-price">18,90 euro</strong></div></div></article></div>
    </div>
  </div>
</section>"""
    main += block_marquee_m3(["Lorraine", "Bourgogne", "Loire", "Bio", "Nature", "Conseil"])
    main += block_dialog_m3(dialog_id="panierCv", title="Ajouter au panier", lead="Demo - rien n'est commande.", primary_label="Voir le panier", primary_href="contact.html", fields_html='<div class="mb-2"><label class="form-label small">Bouteille</label><select class="form-select"><option>Terres Noires 2021</option><option>Auxerrois Moselle</option></select></div>')
    main += block_fab_menu_m3([{"label": "Panier", "dialog": "panierCv"}, {"label": "Vins", "href": "vins.html"}, {"label": "Cave", "href": "cave.html"}], main_label="Actions cave")
    main += "</main>"
    return _shell_cv("index.html", f"{CV_BRAND} — Caviste Thionville", "Caviste a Thionville : selection soignee, conseils, degustations.", main)


def build_caviste_vins():
    main = """<main><section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Vins</p><h1 class="vt-display h2 mb-3">Tous les vins</h1><p class="lead text-secondary">Filtre par couleur, region, budget - on te guide en cave.</p></div></section></main>"""
    return _shell_cv("vins.html", f"Vins — {CV_BRAND}", "Catalogue vins Cave de la Gare Thionville.", main)


def build_caviste_cave():
    main = """<main><section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">La cave</p><h1 class="vt-display h2 mb-3">Place de la Gare</h1><p class="lead text-secondary">Une piece fraiche, des etageres basses, du temps pour discuter.</p></div></section></main>"""
    return _shell_cv("cave.html", f"La cave — {CV_BRAND}", "La cave Cave de la Gare Thionville.", main)


def build_caviste_contact():
    main = f"""<main><section class="py-5 text-center vt-reveal"><div class="container"><p class="vt-eyebrow">Contact</p><h1 class="vt-display h2">Conseil & commande</h1><p class="lead text-secondary">{CV_ADDRESS}</p><p><a class="btn btn-vt-primary" href="tel:0382531890">{CV_PHONE}</a></p></div></section></main>"""
    return _shell_cv("contact.html", f"Contact — {CV_BRAND}", "Contacter Cave de la Gare Thionville.", main)


# --- Osteo : Cabinet des Ponts (Metz) ---
OS_BRAND = "Cabinet des Ponts"
OS_PHONE = "03 87 36 22 10"
OS_EMAIL = "rdv@cabinet-des-ponts.fr"
OS_ADDRESS = "9 quai Felix Maréchal, 57000 Metz"
OS_MAPS = "https://maps.google.com/?q=9+quai+Felix+Marechal+57000+Metz"
OS_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "soins.html", "label": "Soins"},
    {"file": "tarifs.html", "label": "Tarifs"},
    {"file": "contact.html", "label": "Contact"},
]
OS_FOOT = [("Soins", "soins.html"), ("Tarifs", "tarifs.html"), ("RDV", "contact.html"), ("Acces", "contact.html")]


def _shell_os(page, title, desc, main):
    bar = block_info_bar(status="Consultations sur RDV · Metz", address=OS_ADDRESS, phone=OS_PHONE, maps_href=OS_MAPS)
    nav = _nav(OS_BRAND, OS_NAV, page, "Prendre RDV", "contact.html", "osteo")
    foot = _foot("osteo", OS_BRAND, phone=OS_PHONE, address=OS_ADDRESS, email=OS_EMAIL, maps_href=OS_MAPS, nav_links=OS_FOOT, hours_line="Metz · Osteopathie")
    mobile = block_mobile_cta("Prendre RDV", "contact.html", OS_PHONE)
    return wrap_page(title, desc, bar + nav + main + foot + mobile, layout="osteo-m3", slug="osteo", page=page, site_name=OS_BRAND, nav=OS_NAV, head_assets=HEAD_OSTEO, body_class="vt-body vt-body-osteo")


def build_osteo_index():
    main = "<main>"
    main += """<section class="vt-osteo-hero vt-reveal">
  <div class="container">
    <div class="row g-4 align-items-center">
      <div class="col-lg-6">
        <p class="vt-eyebrow mb-2">Osteopathie · Metz</p>
        <h1 class="vt-display display-4 mb-3">Votre osteopathe a Metz</h1>
        <p class="lead mb-3">Approche douce et personnalisee - pour bouger mieux au quotidien.</p>
        <p class="small mb-3"><span class="vt-chip on">Consultations sur rendez-vous</span></p>
        <div class="vt-osteo-slots mb-3">
          <p class="small fw-semibold mb-2">Quand souhaitez-vous venir ?</p>
          <div class="d-flex flex-wrap gap-2">
            <button type="button" class="vt-chip on" data-vt-dialog-open="rdvOs">09:00</button>
            <button type="button" class="vt-chip" data-vt-dialog-open="rdvOs">11:00</button>
            <button type="button" class="vt-chip" data-vt-dialog-open="rdvOs">14:30</button>
          </div>
        </div>
        <button type="button" class="btn btn-vt-primary btn-lg" data-vt-dialog-open="rdvOs">Prendre RDV</button>
      </div>
      <div class="col-lg-6">
        <figure class="vt-osteo-media mb-0"><picture><source srcset="images/hero.webp" type="image/webp"><img src="images/hero.png" alt="Cabinet osteopathie Metz" decoding="async" fetchpriority="high"></picture></figure>
      </div>
    </div>
    <div class="row g-3 mt-4">
      <div class="col-6 col-lg-3"><article class="vt-osteo-stat"><strong>1 200+</strong><span>Patients</span></article></div>
      <div class="col-6 col-lg-3"><article class="vt-osteo-stat"><strong>5/5</strong><span>Avis Google</span></article></div>
      <div class="col-6 col-lg-3"><article class="vt-osteo-stat"><strong>8 ans</strong><span>A Metz</span></article></div>
      <div class="col-6 col-lg-3"><article class="vt-osteo-stat"><strong>Metz</strong><span>Quai accessible</span></article></div>
    </div>
  </div>
</section>"""
    main += block_dialog_m3(dialog_id="rdvOs", title="Prendre RDV", lead="On te confirme le creneau sous 2 h (demo).", primary_label="Envoyer", primary_href="contact.html", fields_html='<div class="mb-2"><label class="form-label small">Motif</label><select class="form-select"><option>Dos / cervicales</option><option>Sport</option><option>Bebe / femme enceinte</option><option>Autre</option></select></div><div class="mb-2"><label class="form-label small">Telephone</label><input class="form-control" type="tel"></div>')
    main += block_fab_menu_m3([{"label": "RDV", "dialog": "rdvOs"}, {"label": "Tarifs", "href": "tarifs.html"}, {"label": "Appeler", "href": "tel:0387362210"}], main_label="Actions cabinet")
    main += "</main>"
    return _shell_os("index.html", f"{OS_BRAND} — Osteopathe Metz", "Cabinet d'osteopathie a Metz : RDV en ligne, soins doux.", main)


def build_osteo_soins():
    main = """<main><section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Soins</p><h1 class="vt-display h2 mb-3">Pour qui ?</h1><p class="lead text-secondary">Adultes, sportifs, femmes enceintes, nourrissons - seance d'environ 45 min.</p></div></section></main>"""
    return _shell_os("soins.html", f"Soins — {OS_BRAND}", "Soins osteopathie Cabinet des Ponts Metz.", main)


def build_osteo_tarifs():
    main = """<main><section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Tarifs</p><h1 class="vt-display h2 mb-3">Tarifs clairs</h1><p class="lead text-secondary">Seance 55 euro - facture pour mutuelle. Pas de surprise.</p></div></section></main>"""
    return _shell_os("tarifs.html", f"Tarifs — {OS_BRAND}", "Tarifs osteopathie Metz.", main)


def build_osteo_contact():
    main = f"""<main><section class="py-5 text-center vt-reveal"><div class="container"><p class="vt-eyebrow">Contact</p><h1 class="vt-display h2">Prendre rendez-vous</h1><p class="lead text-secondary">{OS_ADDRESS}</p><p><a class="btn btn-vt-primary" href="tel:0387362210">{OS_PHONE}</a></p></div></section></main>"""
    return _shell_os("contact.html", f"Contact — {OS_BRAND}", "RDV osteopathie Cabinet des Ponts Metz.", main)


BUILDERS_EXTRA = {
    "boulangerie": [
        ("index.html", build_boulangerie_index),
        ("pains.html", build_boulangerie_pains),
        ("patisseries.html", build_boulangerie_patisseries),
        ("contact.html", build_boulangerie_contact),
    ],
    "artisan": [
        ("index.html", build_artisan_index),
        ("services.html", build_artisan_services),
        ("zones.html", build_artisan_zones),
        ("contact.html", build_artisan_contact),
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
    "osteo": [
        ("index.html", build_osteo_index),
        ("soins.html", build_osteo_soins),
        ("tarifs.html", build_osteo_tarifs),
        ("contact.html", build_osteo_contact),
    ],
}
