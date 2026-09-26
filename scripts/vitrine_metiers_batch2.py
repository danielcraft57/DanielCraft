"""Builders pour 12 echantillons metiers (batch 2) - Bootstrap 5 + Material Design 3."""
from __future__ import annotations

from vitrine_layouts import (
    block_assist_chips,
    block_dialog_m3,
    block_fab_menu_m3,
    block_journey_m3,
    block_marquee_m3,
    block_pill_appbar_m3,
    block_reviews_m3,
    block_snackbar_m3,
    block_sticky_cta_m3,
    block_surface_band_m3,
)
from vitrine_seo import get_entity
from vitrine_site_blocks import (
    block_info_bar,
    block_site_footer,
    block_site_nav,
    wrap_page,
)

_BOOT = """
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <link rel="stylesheet" href="../shared/vitrine-prose.css">
  <link rel="stylesheet" href="../shared/vitrine-images.css">
  <link rel="stylesheet" href="../shared/vitrine-motion.css">
  <link rel="stylesheet" href="../shared/vitrine-m3.css">
  <link rel="icon" href="images/icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="stylesheet" href="styles.css">"""

HEAD_CHOCO = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
{_BOOT}"""

HEAD_TRAIT = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=Work+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
{_BOOT}"""

HEAD_COIF = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,600;6..96,700&family=Jost:wght@400;500;600;700&display=swap" rel="stylesheet">
{_BOOT}"""

HEAD_KINE = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Figtree:wght@500;600;700;800&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
{_BOOT}"""

HEAD_BANQUE = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Serif:wght@600;700&display=swap" rel="stylesheet">
{_BOOT}"""

HEAD_ASSUR = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lexend:wght@500;600;700&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
{_BOOT}"""

HEAD_LOGI = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
{_BOOT}"""

HEAD_PROMO = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Public+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
{_BOOT}"""

HEAD_NOTAIRE = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant:wght@600;700&family=Mulish:wght@400;500;600;700&display=swap" rel="stylesheet">
{_BOOT}"""

HEAD_YOGA = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Quicksand:wght@400;500;600;700&display=swap" rel="stylesheet">
{_BOOT}"""

HEAD_ELEC = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Archivo:wght@400;500;600;700&display=swap" rel="stylesheet">
{_BOOT}"""

HEAD_GITES = f"""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Literata:opsz,wght@7..72,600;7..72,700&family=Karla:wght@400;500;600;700&display=swap" rel="stylesheet">
{_BOOT}"""


def _nav(brand, nav, page, cta_label, cta_href, slug):
    return block_site_nav(brand, nav, page, cta_label=cta_label, cta_href=cta_href, slug=slug)


def _foot(slug, brand, **kw):
    return block_site_footer(brand, entity=get_entity(slug), slug=slug, **kw)


def _img(src_base, alt, *, eager=False, cls=""):
    attrs = 'decoding="async" fetchpriority="high"' if eager else 'loading="lazy"'
    c = f' class="{cls}"' if cls else ""
    return (
        f"<picture><source srcset=\"images/{src_base}.webp\" type=\"image/webp\">"
        f"<img src=\"images/{src_base}.png\" alt=\"{alt}\" {attrs}{c}></picture>"
    )


def _bottom_nav(items: list[dict], current: str) -> str:
    """Barre Material bottom nav mobile. items: {href|dialog, label, ico, active?}."""
    cells = []
    for it in items:
        label = it["label"]
        ico = it.get("ico", "•")
        active = it.get("active")
        if active is None:
            href = it.get("href", "")
            active = bool(href) and href == current
        on = " is-active" if active else ""
        inner = f'<span class="vt-bn-ico" aria-hidden="true">{ico}</span><span>{label}</span>'
        if it.get("dialog"):
            cells.append(
                f'<button type="button" class="{on.strip()}" data-vt-dialog-open="{it["dialog"]}">{inner}</button>'
            )
        else:
            href = it.get("href", "#")
            cells.append(f'<a class="{on.strip()}" href="{href}">{inner}</a>')
    return (
        '<nav class="vt-bottom-nav" aria-label="Navigation rapide">'
        + "".join(cells)
        + "</nav>"
    )


def _stats_band(items: list[dict]) -> str:
    """Bandeau chiffres .vt-m3-stats / .vt-m3-stat - items: {value, label}."""
    cells = "".join(
        f'<article class="vt-m3-stat"><strong>{it["value"]}</strong><span>{it["label"]}</span></article>'
        for it in items
    )
    return f'<div class="vt-m3-stats" aria-label="En chiffres">{cells}</div>'


def _contact_m3(address: str, phone: str, email: str, tel_href: str, *, title: str = "Parlons-en", lead: str = "") -> str:
    lead_html = f'<p class="text-secondary mb-3">{lead}</p>' if lead else ""
    return f"""<section class="py-5 vt-reveal">
  <div class="container">
    <div class="vt-m3-contact-card mx-auto" style="max-width:32rem">
      <p class="vt-eyebrow mb-1">Contact</p>
      <h1 class="vt-display h2 mb-2">{title}</h1>
      {lead_html}
      <p class="mb-1">{address}</p>
      <div class="vt-m3-contact-actions mb-4">
        <a class="btn btn-vt-primary" href="{tel_href}">{phone}</a>
        <a class="btn btn-vt-outline" href="mailto:{email}">Ecrire</a>
      </div>
      <form action="#" method="get" onsubmit="return false;">
        <div class="vt-m3-field">
          <label class="form-label" for="vt-m3-name">Ton prenom</label>
          <input class="form-control" id="vt-m3-name" name="name" type="text" autocomplete="given-name">
        </div>
        <div class="vt-m3-field">
          <label class="form-label" for="vt-m3-tel">Telephone</label>
          <input class="form-control" id="vt-m3-tel" name="tel" type="tel" autocomplete="tel">
        </div>
        <div class="vt-m3-field">
          <label class="form-label" for="vt-m3-msg">Message</label>
          <textarea class="form-control" id="vt-m3-msg" name="msg" rows="3"></textarea>
        </div>
        <button type="button" class="btn btn-vt-primary w-100" data-vt-snack="Message envoye (demo)">Envoyer</button>
      </form>
    </div>
  </div>
</section>"""


def _progress(active: int = 1) -> str:
    """Barre 3 segments - active = nombre de segments allumes (1 ou 2)."""
    active = max(1, min(2, active))
    segs = "".join(
        f'<span class="{"is-on" if i < active else ""}"></span>' for i in range(3)
    )
    return f'<div class="vt-m3-progress container pt-4" aria-hidden="true">{segs}</div>'


def _chrome_classic(
    *,
    brand: str,
    nav: list[dict],
    page: str,
    cta_label: str,
    cta_href: str,
    slug: str,
    status: str,
    address: str,
    phone: str,
    email: str,
    maps: str,
    foot_links: list,
    hours: str,
    main: str,
    title: str,
    desc: str,
    head: str,
    body_class: str,
    layout: str,
    snack: str,
    bottom_items: list[dict],
    mobile_label: str,
):
    bar = block_info_bar(status=status, address=address, phone=phone, maps_href=maps)
    top = _nav(brand, nav, page, cta_label, cta_href, slug)
    foot = _foot(slug, brand, phone=phone, address=address, email=email, maps_href=maps, nav_links=foot_links, hours_line=hours)
    bn = _bottom_nav(bottom_items, page)
    sn = block_snackbar_m3(snack)
    return wrap_page(
        title,
        desc,
        bar + top + main + foot + sn + bn,
        layout=layout,
        slug=slug,
        page=page,
        site_name=brand,
        nav=nav,
        head_assets=head,
        body_class=body_class,
    )


def _chrome_pill(
    *,
    brand: str,
    nav: list[dict],
    page: str,
    cta_label: str,
    cta_href: str,
    cta_dialog: str,
    slug: str,
    phone: str,
    email: str,
    address: str,
    maps: str,
    foot_links: list,
    hours: str,
    subtitle: str,
    main: str,
    title: str,
    desc: str,
    head: str,
    body_class: str,
    layout: str,
    snack: str,
    bottom_items: list[dict],
):
    app = block_pill_appbar_m3(
        brand,
        nav,
        page,
        phone=phone,
        cta_label=cta_label,
        cta_dialog=cta_dialog if page == "index.html" else "",
        cta_href=cta_href,
        subtitle=subtitle,
    )
    foot = _foot(slug, brand, phone=phone, address=address, email=email, maps_href=maps, nav_links=foot_links, hours_line=hours)
    bn = _bottom_nav(bottom_items, page)
    sn = block_snackbar_m3(snack)
    return wrap_page(
        title,
        desc,
        app + main + foot + sn + bn,
        layout=layout,
        slug=slug,
        page=page,
        site_name=brand,
        nav=nav,
        head_assets=head,
        body_class=body_class,
    )


# --- Chocolaterie : Maison Mirabelle (Metz) ---
CH_BRAND = "Maison Mirabelle"
CH_PHONE = "03 87 18 42 10"
CH_EMAIL = "bonjour@maison-mirabelle.fr"
CH_ADDRESS = "8 rue des Clercs, 57000 Metz"
CH_MAPS = "https://maps.google.com/?q=8+rue+des+Clercs+57000+Metz"
CH_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "chocolats.html", "label": "Chocolats"},
    {"file": "atelier.html", "label": "Atelier"},
    {"file": "contact.html", "label": "Contact"},
]
CH_FOOT = [("Chocolats", "chocolats.html"), ("Atelier", "atelier.html"), ("Commander", "contact.html"), ("Boutique", "contact.html")]
CH_BN = [
    {"href": "index.html", "label": "Accueil", "ico": "🏠"},
    {"href": "chocolats.html", "label": "Chocolats", "ico": "📋"},
    {"href": "tel:0387184210", "label": "Appeler", "ico": "📞"},
    {"href": "contact.html", "label": "Contact", "ico": "✉"},
]


def _shell_ch(page, title, desc, main):
    return _chrome_classic(
        brand=CH_BRAND, nav=CH_NAV, page=page, cta_label="Commander", cta_href="contact.html", slug="chocolaterie",
        status="Boutique · Mar-sam 9h-19h", address=CH_ADDRESS, phone=CH_PHONE, email=CH_EMAIL, maps=CH_MAPS,
        foot_links=CH_FOOT, hours="Metz · Chocolaterie", main=main, title=title, desc=desc, head=HEAD_CHOCO,
        body_class="vt-body vt-body-chocolaterie", layout="chocolaterie-m3", snack="Commande enregistree (demo)",
        bottom_items=CH_BN, mobile_label="Commander",
    )


def build_chocolaterie_index():
    main = "<main>"
    main += f"""<section class="vt-hero-bleed vt-reveal">
  {_img("hero", "Vitrine chocolats Maison Mirabelle Metz", eager=True, cls="vt-hero-bleed-img")}
  <div class="vt-hero-bleed-copy">
    <div class="container">
      <p class="vt-eyebrow mb-2">Chocolaterie · Metz</p>
      <h1 class="vt-display display-3 mb-3">Du cacao, de la mirabelle, et du temps</h1>
      <p class="lead mb-4">Tablettes, bonbons et commandes pour les fetes - faits a la boutique, rue des Clercs.</p>
      <div class="vt-hero-actions">
        <button type="button" class="btn btn-vt-primary btn-lg" data-vt-dialog-open="cmdCh">Commander</button>
        <a class="btn btn-vt-outline btn-lg" href="chocolats.html">Voir les chocolats</a>
      </div>
    </div>
  </div>
</section>"""
    main += block_assist_chips([
        {"label": "Ganaches", "href": "chocolats.html", "active": True},
        {"label": "Tablettes", "href": "chocolats.html"},
        {"label": "Atelier", "href": "atelier.html"},
        {"label": "Entreprise", "href": "contact.html"},
    ], aria="Raccourcis boutique")
    main += block_marquee_m3(["Mirabelle", "Ganache", "Tablettes", "Coffrets", "Ateliers"])
    main += """<section class="py-5 vt-reveal"><div class="container">
  <p class="vt-eyebrow">Selection</p>
  <h2 class="vt-display h3 mb-4">Ce qu'on sort de l'atelier</h2>
  <div class="row g-3 vt-reveal-stagger">
    <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-1", "Bonbons ganache") + """<div class="p-3"><h3 class="h6 mb-1">Bonbons ganache</h3><p class="small text-secondary mb-0">Assortiments du weekend.</p></div></article></div>
    <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-2", "Tablette mirabelle") + """<div class="p-3"><h3 class="h6 mb-1">Tablette mirabelle</h3><p class="small text-secondary mb-0">Edition saison Grand Est.</p></div></article></div>
    <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-3", "Coffret cadeau") + """<div class="p-3"><h3 class="h6 mb-1">Coffrets cadeaux</h3><p class="small text-secondary mb-0">Pour offrir sans faire le nareux.</p></div></article></div>
  </div>
</div></section>"""
    main += block_journey_m3(
        "De la vitrine au cornet",
        [
            {"title": "Tu passes (ou tu ecris)", "text": "Entre midi ou apres le boulot - on regarde voir ce qui reste.", "emotion": "Curieux"},
            {"title": "On goute ensemble", "text": "Comme au marche : un chtuque avant de remplir le cornet.", "emotion": "Confiance"},
            {"title": "On prepare", "text": "Commande entreprise ou cadeau - carton propre, delai tenu.", "emotion": "Soulage"},
            {"title": "Tu repars content", "text": "Et tu sais deja ce que tu reprendras la prochaine fois.", "emotion": "Content"},
        ],
        kicker="Comment ca se passe",
        lead="Simple, a la boutique - pas de parcours a rallonge.",
    )
    main += block_reviews_m3(
        title="Ce qu'on entend au comptoir",
        kicker="Avis",
        rating="4,9/5",
        reviews=[
            {"text": "Les ganaches mirabelle, on y revient entre midi.", "name": "Claire", "meta": "Metz", "stars": 5},
            {"text": "Commande entreprise simple, carton propre, delai tenu.", "name": "Marc", "meta": "Thionville", "stars": 5},
            {"text": "Atelier gosse - il a adore couatcher autour du chocolat.", "name": "Sophie", "meta": "Montigny", "stars": 5},
        ],
    )
    main += block_surface_band_m3(
        '<div class="container py-4">' + _stats_band([
            {"value": "2014", "label": "Ouverture Metz"},
            {"value": "40+", "label": "Recettes maison"},
            {"value": "2 j", "label": "Delai commande"},
            {"value": "4,9", "label": "Note clients"},
        ]) + "</div>",
        tone="soft",
        aria_label="Chiffres boutique",
    )
    main += """<section class="vt-cta-sticky py-4 vt-reveal"><div class="container d-flex flex-wrap align-items-center justify-content-between gap-3">
  <div><h2 class="h5 mb-1">Un chtuque de douceur a emporter ?</h2><p class="small text-secondary mb-0">Viens avec ta liste - on prepare le cornet.</p></div>
  <a class="btn btn-vt-primary" href="contact.html">Passer commande</a>
</div></section>"""
    main += block_dialog_m3(dialog_id="cmdCh", title="Commander", lead="Retrait boutique - on te confirme (demo).", primary_label="Envoyer", primary_href="contact.html", fields_html='<div class="mb-2 vt-m3-field"><label class="form-label small">Produit</label><select class="form-select"><option>Assortiment 12</option><option>Tablette mirabelle</option><option>Coffret entreprise</option></select></div><div class="mb-2 vt-m3-field"><label class="form-label small">Date de retrait</label><input class="form-control" type="date"></div>')
    main += block_fab_menu_m3([{"label": "Commander", "dialog": "cmdCh"}, {"label": "Chocolats", "href": "chocolats.html"}, {"label": "Appeler", "href": "tel:0387184210"}], main_label="Actions boutique")
    main += block_sticky_cta_m3("Envie d'un cornet ?", "Commander", "contact.html", dialog="cmdCh")
    main += "</main>"
    return _shell_ch("index.html", f"{CH_BRAND} - Chocolaterie Metz", "Chocolaterie a Metz : tablettes, bonbons, coffrets et ateliers.", main)


def build_chocolaterie_chocolats():
    main = f"""<main>{_progress(1)}<section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Chocolats</p><h1 class="vt-display h2 mb-3">Ganaches, pralines, tablettes</h1><p class="lead text-secondary mb-4">Selection du jour - farines et fruits locaux quand c'est la saison.</p><div class="row g-4"><div class="col-md-4"><article class="vt-svc-card">{_img("scene-1", "Ganache")} <div class="p-3"><h2 class="h6">Ganaches</h2><p class="small text-secondary mb-0">Cremeux, pas trop sucres.</p></div></article></div><div class="col-md-4"><article class="vt-svc-card">{_img("scene-2", "Praline")} <div class="p-3"><h2 class="h6">Pralines</h2><p class="small text-secondary mb-0">Noisette et amande.</p></div></article></div><div class="col-md-4"><article class="vt-svc-card">{_img("scene-3", "Tablette")} <div class="p-3"><h2 class="h6">Tablettes</h2><p class="small text-secondary mb-0">Origines tracees.</p></div></article></div></div><a class="btn btn-vt-primary mt-4" href="contact.html">Commander</a></div></section></main>"""
    return _shell_ch("chocolats.html", f"Chocolats - {CH_BRAND}", "Chocolats Maison Mirabelle Metz.", main)


def build_chocolaterie_atelier():
    main = f"""<main>{_progress(2)}<section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Atelier</p><h1 class="vt-display h2 mb-3">Viens voir comment ca se tempre</h1><p class="lead text-secondary mb-4">Ateliers enfants et adultes - places limitees, sur reservation.</p><a class="btn btn-vt-primary" href="contact.html">Reserver un atelier</a></div></section></main>"""
    return _shell_ch("atelier.html", f"Atelier - {CH_BRAND}", "Ateliers chocolat Maison Mirabelle Metz.", main)


def build_chocolaterie_contact():
    main = f"<main>{_progress(2)}" + _contact_m3(CH_ADDRESS, CH_PHONE, CH_EMAIL, "tel:0387184210", title="Passer a la boutique", lead="Rue des Clercs - on peut juste couatcher 5 minutes.") + "</main>"
    return _shell_ch("contact.html", f"Contact - {CH_BRAND}", "Contacter Maison Mirabelle Metz.", main)


# --- Traiteur : Table & Cornet (Nancy) ---
TR_BRAND = "Table & Cornet"
TR_PHONE = "03 83 27 61 40"
TR_EMAIL = "events@table-cornet.fr"
TR_ADDRESS = "19 rue Stanislas, 54000 Nancy"
TR_MAPS = "https://maps.google.com/?q=19+rue+Stanislas+54000+Nancy"
TR_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "menus.html", "label": "Menus"},
    {"file": "evenements.html", "label": "Evenements"},
    {"file": "contact.html", "label": "Contact"},
]
TR_FOOT = [("Menus", "menus.html"), ("Evenements", "evenements.html"), ("Devis", "contact.html"), ("Cuisine", "contact.html")]
TR_BN = [
    {"href": "index.html", "label": "Accueil", "ico": "🏠"},
    {"href": "menus.html", "label": "Menus", "ico": "📋"},
    {"href": "tel:0383276140", "label": "Appeler", "ico": "📞"},
    {"href": "contact.html", "label": "Devis", "ico": "✉"},
]


def _shell_tr(page, title, desc, main):
    return _chrome_classic(
        brand=TR_BRAND, nav=TR_NAV, page=page, cta_label="Demander un devis", cta_href="contact.html", slug="traiteur",
        status="Traiteur · Sur devis", address=TR_ADDRESS, phone=TR_PHONE, email=TR_EMAIL, maps=TR_MAPS,
        foot_links=TR_FOOT, hours="Nancy · Traiteur", main=main, title=title, desc=desc, head=HEAD_TRAIT,
        body_class="vt-body vt-body-traiteur", layout="traiteur-m3", snack="Devis demande (demo)",
        bottom_items=TR_BN, mobile_label="Devis",
    )


def build_traiteur_index():
    main = "<main>"
    main += f"""<section class="vt-hero-bleed vt-reveal">
  {_img("hero", "Buffet elegant Table et Cornet Nancy", eager=True, cls="vt-hero-bleed-img")}
  <div class="vt-hero-bleed-copy">
    <div class="container">
      <p class="vt-eyebrow mb-2">Traiteur · Nancy</p>
      <h1 class="vt-display display-3 mb-3">Ta table est prete - le reste, on s'en charge</h1>
      <p class="lead mb-4">Mariages, seminaires, cocktails - cuisine soignee, service discret.</p>
      <div class="vt-hero-actions">
        <button type="button" class="btn btn-vt-primary btn-lg" data-vt-dialog-open="devisTr">Demander un devis</button>
        <a class="btn btn-vt-outline btn-lg" href="menus.html">Voir les menus</a>
      </div>
    </div>
  </div>
</section>"""
    main += block_assist_chips([
        {"label": "Mariage", "href": "evenements.html", "active": True},
        {"label": "Entreprise", "href": "evenements.html"},
        {"label": "Menus", "href": "menus.html"},
        {"label": "Devis", "href": "contact.html"},
    ])
    main += """<section class="py-5 vt-reveal"><div class="container">
  <p class="vt-eyebrow">Formules</p>
  <h2 class="vt-display h3 mb-4">Trois facons de recevoir</h2>
  <div class="row g-3">
    <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-1", "Cocktail") + """<div class="p-3"><h3 class="h6">Cocktail dinatoire</h3><p class="small text-secondary mb-0">Bouchées, vins, rythme fluide.</p></div></article></div>
    <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-2", "Assis") + """<div class="p-3"><h3 class="h6">Repas assis</h3><p class="small text-secondary mb-0">Menus saison, service a l'assiette.</p></div></article></div>
    <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-3", "Bureau") + """<div class="p-3"><h3 class="h6">Plateaux bureau</h3><p class="small text-secondary mb-0">Entre midi, sans stress.</p></div></article></div>
  </div>
</div></section>"""
    main += block_journey_m3(
        "De l'idee au service",
        [
            {"title": "Brief rapide", "text": "Dis voir la date, le lieu, le nombre - on demele le menu.", "emotion": "Clair"},
            {"title": "Degustation", "text": "Tu goutes avant de remplir le cornet - pas de surprise.", "emotion": "Rassure"},
            {"title": "Jour J", "text": "On arrive, on dresse, tu restes avec tes invites.", "emotion": "Zen"},
            {"title": "Apres", "text": "Rangement compris - tu rentres sans vaisselle.", "emotion": "Soulage"},
        ],
        lead="Nancy et alentours - on vient avec le materiel.",
    )
    main += block_reviews_m3(
        title="Ils ont recu avec nous",
        reviews=[
            {"text": "Mariage a 90 - rien n'a tire, tout etait chaud.", "name": "Elodie", "meta": "Vandoeuvre", "stars": 5},
            {"text": "Seminaire client : devis clair, zero surprise.", "name": "Julien", "meta": "Nancy", "stars": 5},
            {"text": "Plateaux bureau entre midi - livrés a l'heure.", "name": "Sara", "meta": "Laxou", "stars": 4},
        ],
    )
    main += block_surface_band_m3(
        '<div class="container py-4">' + _stats_band([
            {"value": "12 ans", "label": "Sur le terrain"},
            {"value": "40-200", "label": "Convives"},
            {"value": "48 h", "label": "Devis type"},
            {"value": "Nancy", "label": "Base cuisine"},
        ]) + "</div>",
        tone="soft",
    )
    main += """<section class="vt-cta-sticky py-4"><div class="container d-flex flex-wrap justify-content-between gap-3 align-items-center">
  <p class="mb-0 fw-semibold">Dis voir la date - on demele le menu ensemble.</p>
  <a class="btn btn-vt-primary" href="contact.html">Parler de ton evenement</a>
</div></section>"""
    main += block_dialog_m3(dialog_id="devisTr", title="Devis evenement", lead="Quelques infos - on te rappel (demo).", primary_label="Envoyer", primary_href="contact.html", fields_html='<div class="mb-2 vt-m3-field"><label class="form-label small">Type</label><select class="form-select"><option>Mariage</option><option>Entreprise</option><option>Prive</option></select></div><div class="mb-2 vt-m3-field"><label class="form-label small">Nombre de convives</label><input class="form-control" type="number" min="10" value="40"></div>')
    main += block_fab_menu_m3([{"label": "Devis", "dialog": "devisTr"}, {"label": "Menus", "href": "menus.html"}, {"label": "Appeler", "href": "tel:0383276140"}], main_label="Actions traiteur")
    main += block_sticky_cta_m3("Date a poser ?", "Devis", "contact.html", dialog="devisTr")
    main += "</main>"
    return _shell_tr("index.html", f"{TR_BRAND} - Traiteur Nancy", "Traiteur a Nancy : cocktails, repas assis, plateaux bureau.", main)


def build_traiteur_menus():
    main = f"""<main>{_progress(1)}<section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Menus</p><h1 class="vt-display h2 mb-3">Menus de saison</h1><p class="lead text-secondary mb-4">On adapte selon le marche - regarde voir les bases.</p><div class="row g-4"><div class="col-md-4">{_img("scene-1", "Entree")}</div><div class="col-md-4">{_img("scene-2", "Plat")}</div><div class="col-md-4">{_img("scene-3", "Dessert")}</div></div><a class="btn btn-vt-primary mt-4" href="contact.html">Demander un devis</a></div></section></main>"""
    return _shell_tr("menus.html", f"Menus - {TR_BRAND}", "Menus traiteur Table et Cornet Nancy.", main)


def build_traiteur_evenements():
    main = f"""<main>{_progress(2)}<section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Evenements</p><h1 class="vt-display h2 mb-3">Du mariage au seminaire</h1><p class="lead text-secondary">Lieux partenaires a Nancy et alentours - on vient avec le materiel.</p></div></section></main>"""
    return _shell_tr("evenements.html", f"Evenements - {TR_BRAND}", "Evenements traiteur Nancy.", main)


def build_traiteur_contact():
    main = f"<main>{_progress(2)}" + _contact_m3(TR_ADDRESS, TR_PHONE, TR_EMAIL, "tel:0383276140", title="Parler de ton projet", lead="Viens avec la date - on cadre vite.") + "</main>"
    return _shell_tr("contact.html", f"Contact - {TR_BRAND}", "Contacter Table et Cornet Nancy.", main)


# --- Coiffure : Salon Rivage (Thionville) ---
CF_BRAND = "Salon Rivage"
CF_PHONE = "03 82 54 19 30"
CF_EMAIL = "rdv@salon-rivage.fr"
CF_ADDRESS = "12 avenue de la Liberte, 57100 Thionville"
CF_MAPS = "https://maps.google.com/?q=12+avenue+de+la+Liberte+57100+Thionville"
CF_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "soins.html", "label": "Soins"},
    {"file": "equipe.html", "label": "Equipe"},
    {"file": "contact.html", "label": "Contact"},
]
CF_FOOT = [("Soins", "soins.html"), ("Equipe", "equipe.html"), ("RDV", "contact.html"), ("Tarifs", "soins.html")]
CF_BN = [
    {"href": "index.html", "label": "Accueil", "ico": "🏠"},
    {"href": "soins.html", "label": "Soins", "ico": "📋"},
    {"href": "tel:0382541930", "label": "Appeler", "ico": "📞"},
    {"href": "contact.html", "label": "RDV", "ico": "✉"},
]


def _shell_cf(page, title, desc, main):
    return _chrome_pill(
        brand=CF_BRAND, nav=CF_NAV, page=page, cta_label="Prendre RDV", cta_href="contact.html",
        cta_dialog="rdvCf", slug="coiffure", phone=CF_PHONE, email=CF_EMAIL, address=CF_ADDRESS, maps=CF_MAPS,
        foot_links=CF_FOOT, hours="Thionville · Coiffure", subtitle="Salon · Thionville",
        main=main, title=title, desc=desc, head=HEAD_COIF,
        body_class="vt-body vt-body-coiffure vt-body-pill", layout="coiffure-m3",
        snack="RDV demande (demo)", bottom_items=CF_BN,
    )


def build_coiffure_index():
    main = "<main>"
    main += f"""<section class="vt-hero-bleed vt-hero-magazine vt-reveal">
  {_img("hero", "Salon Rivage Thionville", eager=True, cls="vt-hero-bleed-img")}
  <div class="vt-hero-bleed-copy">
    <div class="container">
      <p class="vt-eyebrow mb-2">Coiffure · Thionville</p>
      <h1 class="vt-display display-3 mb-3">Coupe, couleur, attitude</h1>
      <p class="lead mb-4">Un salon calme au bord de la Moselle - tu ressors avec une tete qui te ressemble.</p>
      <div class="vt-hero-actions">
        <button type="button" class="btn btn-vt-primary btn-lg" data-vt-dialog-open="rdvCf">Prendre rendez-vous</button>
        <a class="btn btn-vt-outline btn-lg" href="soins.html">Voir les soins</a>
      </div>
    </div>
  </div>
</section>"""
    main += block_assist_chips([
        {"label": "Coupe", "href": "soins.html", "active": True},
        {"label": "Couleur", "href": "soins.html"},
        {"label": "Equipe", "href": "equipe.html"},
        {"label": "RDV", "href": "contact.html"},
    ])
    main += """<section class="py-5 vt-reveal"><div class="container">
  <div class="row g-4 align-items-center">
    <div class="col-lg-5"><p class="vt-eyebrow">Magazine</p><h2 class="vt-display h3 mb-3">Looks du mois</h2><p class="text-secondary">Inspiration, pas copie - on adapte a ta chevelure.</p></div>
    <div class="col-lg-7"><div class="row g-3">
      <div class="col-4">""" + _img("card-1", "Coupe courte") + """</div>
      <div class="col-4">""" + _img("card-2", "Balayage") + """</div>
      <div class="col-4">""" + _img("card-3", "Brushing") + """</div>
    </div></div>
  </div>
</div></section>"""
    main += block_journey_m3(
        "Ton creneau, sans stress",
        [
            {"title": "Tu reserves", "text": "En ligne ou au salon - creneau visible.", "emotion": "Simple"},
            {"title": "On ecoute", "text": "Avant de couper : ce que tu veux vraiment.", "emotion": "Ecoute"},
            {"title": "On fait", "text": "Coupe, couleur, brushing - a ton rythme.", "emotion": "Bien"},
            {"title": "Tu repars", "text": "Avec les gestes pour tenir la coiffure chez toi.", "emotion": "Fier"},
        ],
    )
    main += block_reviews_m3(
        title="Ce qu'on entend au salon",
        reviews=[
            {"text": "Enfin un salon ou on ecoute avant de couper.", "name": "Ines", "meta": "Yutz", "stars": 5},
            {"text": "Balayage naturel - j'ai pas fait le nareux sur le prix.", "name": "Chloe", "meta": "Thionville", "stars": 5},
            {"text": "Creneau tenu, ambiance calme, cafe offert.", "name": "Hugo", "meta": "Hayange", "stars": 4},
        ],
    )
    main += block_surface_band_m3(
        '<div class="container py-4">' + _stats_band([
            {"value": "3", "label": "Coiffeurs"},
            {"value": "Mar-sam", "label": "Ouverture"},
            {"value": "28 €", "label": "Coupe des"},
            {"value": "Moselle", "label": "Vue rivage"},
        ]) + "</div>",
        tone="soft",
    )
    main += """<section class="vt-cta-sticky py-4"><div class="container d-flex flex-wrap justify-content-between gap-3 align-items-center">
  <p class="mb-0">Creneau libre cette semaine ? Guette voir les horaires.</p>
  <a class="btn btn-vt-primary" href="contact.html">Reserver</a>
</div></section>"""
    main += block_dialog_m3(dialog_id="rdvCf", title="Prendre RDV", lead="On te confirme par SMS (demo).", primary_label="Envoyer", primary_href="contact.html", fields_html='<div class="mb-2 vt-m3-field"><label class="form-label small">Prestation</label><select class="form-select"><option>Coupe</option><option>Couleur</option><option>Brushing</option></select></div><div class="mb-2 vt-m3-field"><label class="form-label small">Telephone</label><input class="form-control" type="tel"></div>')
    main += block_fab_menu_m3([{"label": "RDV", "dialog": "rdvCf"}, {"label": "Soins", "href": "soins.html"}, {"label": "Appeler", "href": "tel:0382541930"}], main_label="Actions salon")
    main += block_sticky_cta_m3("Creneau cette semaine ?", "RDV", "contact.html", dialog="rdvCf")
    main += "</main>"
    return _shell_cf("index.html", f"{CF_BRAND} - Coiffure Thionville", "Salon de coiffure a Thionville : coupe, couleur, soins.", main)


def build_coiffure_soins():
    main = f"""<main>{_progress(1)}<section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Soins</p><h1 class="vt-display h2 mb-3">Coupe, couleur, soin</h1><div class="row g-4"><div class="col-md-4"><article class="vt-svc-card">{_img("scene-1", "Coupe")}<div class="p-3"><h2 class="h6">Coupe</h2><p class="small text-secondary mb-0">A partir de 28 euro.</p></div></article></div><div class="col-md-4"><article class="vt-svc-card">{_img("scene-2", "Couleur")}<div class="p-3"><h2 class="h6">Couleur</h2><p class="small text-secondary mb-0">Diagnostic avant.</p></div></article></div><div class="col-md-4"><article class="vt-svc-card">{_img("scene-3", "Soin")}<div class="p-3"><h2 class="h6">Soin intensif</h2><p class="small text-secondary mb-0">Cheveux fatigues.</p></div></article></div></div></div></section></main>"""
    return _shell_cf("soins.html", f"Soins - {CF_BRAND}", "Soins et tarifs Salon Rivage.", main)


def build_coiffure_equipe():
    main = f"""<main>{_progress(2)}<section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Equipe</p><h1 class="vt-display h2 mb-3">Trois coiffeurs, une meme exigence</h1><p class="lead text-secondary">Tu choisis ton interlocuteur - pas de roulette russe.</p></div></section></main>"""
    return _shell_cf("equipe.html", f"Equipe - {CF_BRAND}", "Equipe Salon Rivage Thionville.", main)


def build_coiffure_contact():
    main = f"<main>{_progress(2)}" + _contact_m3(CF_ADDRESS, CF_PHONE, CF_EMAIL, "tel:0382541930", title="Prendre rendez-vous", lead="Avenue de la Liberte - parking a deux pas.") + "</main>"
    return _shell_cf("contact.html", f"Contact - {CF_BRAND}", "RDV Salon Rivage Thionville.", main)


# --- Kine : Kinesia Metz ---
KI_BRAND = "Kinesia Metz"
KI_PHONE = "03 87 63 28 15"
KI_EMAIL = "accueil@kinesia-metz.fr"
KI_ADDRESS = "5 rue Serpenoise, 57000 Metz"
KI_MAPS = "https://maps.google.com/?q=5+rue+Serpenoise+57000+Metz"
KI_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "soins.html", "label": "Soins"},
    {"file": "equipe.html", "label": "Equipe"},
    {"file": "contact.html", "label": "Contact"},
]
KI_FOOT = [("Soins", "soins.html"), ("Equipe", "equipe.html"), ("RDV", "contact.html"), ("Acces", "contact.html")]
KI_BN = [
    {"href": "index.html", "label": "Accueil", "ico": "🏠"},
    {"href": "soins.html", "label": "Soins", "ico": "📋"},
    {"href": "tel:0387632815", "label": "Appeler", "ico": "📞"},
    {"href": "contact.html", "label": "RDV", "ico": "✉"},
]


def _shell_ki(page, title, desc, main):
    return _chrome_pill(
        brand=KI_BRAND, nav=KI_NAV, page=page, cta_label="Prendre RDV", cta_href="contact.html",
        cta_dialog="rdvKi", slug="kine", phone=KI_PHONE, email=KI_EMAIL, address=KI_ADDRESS, maps=KI_MAPS,
        foot_links=KI_FOOT, hours="Metz · Kinesitherapie", subtitle="Cabinet · Metz",
        main=main, title=title, desc=desc, head=HEAD_KINE,
        body_class="vt-body vt-body-kine vt-body-pill", layout="kine-m3",
        snack="Demande RDV enregistree (demo)", bottom_items=KI_BN,
    )


def build_kine_index():
    main = "<main>"
    main += f"""<section class="vt-hero-split vt-reveal">
  <div class="container">
    <div class="row g-4 align-items-center">
      <div class="col-lg-6">
        <p class="vt-eyebrow mb-2">Kinesitherapie · Metz</p>
        <h1 class="vt-display display-4 mb-3">Reprendre appui, sans attendre sur un miracle</h1>
        <p class="lead mb-4">Sport, post-op, dos - creneaux visibles, equipe a l'ecoute.</p>
        <div class="vt-hero-actions">
          <button type="button" class="btn btn-vt-primary btn-lg" data-vt-dialog-open="rdvKi">Voir les creneaux</button>
          <a class="btn btn-vt-outline btn-lg" href="soins.html">Nos soins</a>
        </div>
        <ul class="vt-trust-list mt-4"><li>Conventionne</li><li>Acces PMR</li><li>Parking proche</li></ul>
      </div>
      <div class="col-lg-6">{_img("hero", "Salle de soins Kinesia Metz", eager=True, cls="vt-hero-rounded")}</div>
    </div>
  </div>
</section>"""
    main += block_assist_chips([
        {"label": "Sport", "href": "soins.html", "active": True},
        {"label": "Dos", "href": "soins.html"},
        {"label": "Post-op", "href": "soins.html"},
        {"label": "RDV", "href": "contact.html"},
    ])
    main += """<section class="py-5 vt-reveal"><div class="container"><div class="row g-3">
  <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-1", "Sport") + """<div class="p-3"><h3 class="h6">Traumatologie sport</h3></div></article></div>
  <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-2", "Dos") + """<div class="p-3"><h3 class="h6">Rachis et posture</h3></div></article></div>
  <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-3", "Respi") + """<div class="p-3"><h3 class="h6">Respiratoire</h3></div></article></div>
</div></div></section>"""
    main += block_journey_m3(
        "Du premier appel a la reprise",
        [
            {"title": "Tu appelles", "text": "Ordonnance en poche - on trouve un creneau.", "emotion": "Soulage"},
            {"title": "Bilan", "text": "On explique sans jargon - objectifs clairs.", "emotion": "Compris"},
            {"title": "Seances", "text": "Exercices a la maison, suivi au cabinet.", "emotion": "Progres"},
            {"title": "Autonomie", "text": "Tu repars avec une paire de gestes utiles.", "emotion": "Libre"},
        ],
    )
    main += block_reviews_m3(
        title="Patients du centre-ville",
        reviews=[
            {"text": "RDV sous 48 h apres mon operation - nickel.", "name": "Thomas", "meta": "Metz", "stars": 5},
            {"text": "Explications claires, exercices faciles a suivre.", "name": "Nadia", "meta": "Longeville", "stars": 5},
            {"text": "Cabinet propre, acces facile rue Serpenoise.", "name": "Paul", "meta": "Metz", "stars": 4},
        ],
    )
    main += block_surface_band_m3(
        '<div class="container py-4">' + _stats_band([
            {"value": "4", "label": "Praticiens"},
            {"value": "48 h", "label": "Delai typique"},
            {"value": "PMR", "label": "Acces"},
            {"value": "Metz", "label": "Centre"},
        ]) + "</div>",
        tone="soft",
    )
    main += """<section class="vt-cta-sticky py-4"><div class="container d-flex flex-wrap justify-content-between gap-3 align-items-center">
  <p class="mb-0">Ordonnance en poche ? On trouve un creneau.</p>
  <a class="btn btn-vt-primary" href="contact.html">Prendre RDV</a>
</div></section>"""
    main += block_dialog_m3(dialog_id="rdvKi", title="Demande de RDV", lead="On te rappelle pour confirmer (demo).", primary_label="Envoyer", primary_href="contact.html", fields_html='<div class="mb-2 vt-m3-field"><label class="form-label small">Motif</label><select class="form-select"><option>Sport</option><option>Dos</option><option>Post-op</option><option>Autre</option></select></div><div class="mb-2 vt-m3-field"><label class="form-label small">Telephone</label><input class="form-control" type="tel"></div>')
    main += block_fab_menu_m3([{"label": "RDV", "dialog": "rdvKi"}, {"label": "Soins", "href": "soins.html"}, {"label": "Appeler", "href": "tel:0387632815"}], main_label="Actions cabinet")
    main += block_sticky_cta_m3("Besoin d'un creneau ?", "RDV", "contact.html", dialog="rdvKi")
    main += "</main>"
    return _shell_ki("index.html", f"{KI_BRAND} - Kinesitherapie Metz", "Cabinet de kinesitherapie a Metz : sport, dos, post-op.", main)


def build_kine_soins():
    main = f"""<main>{_progress(1)}<section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Soins</p><h1 class="vt-display h2 mb-3">Ce qu'on prend en charge</h1><div class="row g-4"><div class="col-md-4">{_img("scene-1", "Reeducation")}</div><div class="col-md-4">{_img("scene-2", "Sport")}</div><div class="col-md-4">{_img("scene-3", "Bilan")}</div></div></div></section></main>"""
    return _shell_ki("soins.html", f"Soins - {KI_BRAND}", "Soins kinesitherapie Metz.", main)


def build_kine_equipe():
    main = f"""<main>{_progress(2)}<section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Equipe</p><h1 class="vt-display h2 mb-3">Quatre kine, un meme cabinet</h1><p class="lead text-secondary">Tu restes avec le meme praticien quand c'est possible.</p></div></section></main>"""
    return _shell_ki("equipe.html", f"Equipe - {KI_BRAND}", "Equipe Kinesia Metz.", main)


def build_kine_contact():
    main = f"<main>{_progress(2)}" + _contact_m3(KI_ADDRESS, KI_PHONE, KI_EMAIL, "tel:0387632815", title="Prendre rendez-vous", lead="Rue Serpenoise - parking a proximite.") + "</main>"
    return _shell_ki("contact.html", f"Contact - {KI_BRAND}", "RDV Kinesia Metz.", main)


# --- Banque : Banque des Ponts (Metz) ---
BA_BRAND = "Banque des Ponts"
BA_PHONE = "03 87 15 90 20"
BA_EMAIL = "conseil@banque-des-ponts.fr"
BA_ADDRESS = "3 place de la Comedie, 57000 Metz"
BA_MAPS = "https://maps.google.com/?q=3+place+de+la+Comedie+57000+Metz"
BA_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "offres.html", "label": "Offres"},
    {"file": "entreprises.html", "label": "Entreprises"},
    {"file": "contact.html", "label": "Contact"},
]
BA_FOOT = [("Offres", "offres.html"), ("Entreprises", "entreprises.html"), ("Rendez-vous", "contact.html"), ("Agences", "contact.html")]
BA_BN = [
    {"href": "index.html", "label": "Accueil", "ico": "🏠"},
    {"href": "offres.html", "label": "Offres", "ico": "📋"},
    {"href": "tel:0387159020", "label": "Appeler", "ico": "📞"},
    {"href": "contact.html", "label": "RDV", "ico": "✉"},
]


def _shell_ba(page, title, desc, main):
    return _chrome_classic(
        brand=BA_BRAND, nav=BA_NAV, page=page, cta_label="Prendre RDV", cta_href="contact.html", slug="banque",
        status="Agence · Lun-ven 9h-17h30", address=BA_ADDRESS, phone=BA_PHONE, email=BA_EMAIL, maps=BA_MAPS,
        foot_links=BA_FOOT, hours="Metz · Banque locale", main=main, title=title, desc=desc, head=HEAD_BANQUE,
        body_class="vt-body vt-body-banque", layout="banque-m3", snack="RDV conseiller (demo)",
        bottom_items=BA_BN, mobile_label="RDV",
    )


def build_banque_index():
    main = "<main>"
    main += f"""<section class="vt-hero-bleed vt-hero-corporate vt-reveal">
  {_img("hero", "Agence Banque des Ponts Metz", eager=True, cls="vt-hero-bleed-img")}
  <div class="vt-hero-bleed-copy">
    <div class="container">
      <p class="vt-eyebrow mb-2">Banque locale · Metz</p>
      <h1 class="vt-display display-3 mb-3">Tes projets, un interlocuteur qui reste</h1>
      <p class="lead mb-4">Comptes, credit, epargne - decisions prises ici, pas a l'autre bout du pays.</p>
      <div class="vt-hero-actions">
        <a class="btn btn-vt-primary btn-lg" href="contact.html">Prendre rendez-vous</a>
        <a class="btn btn-vt-outline btn-lg" href="offres.html">Voir les offres</a>
      </div>
    </div>
  </div>
</section>"""
    main += block_assist_chips([
        {"label": "Particuliers", "href": "offres.html", "active": True},
        {"label": "Pros", "href": "entreprises.html"},
        {"label": "Epargne", "href": "offres.html"},
        {"label": "RDV", "href": "contact.html"},
    ])
    main += """<section class="py-5 vt-reveal"><div class="container"><div class="row g-3">
  <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-1", "Particuliers") + """<div class="p-3"><h3 class="h6">Particuliers</h3><p class="small text-secondary mb-0">Compte, carte, credit habitat.</p></div></article></div>
  <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-2", "Pros") + """<div class="p-3"><h3 class="h6">Professionnels</h3><p class="small text-secondary mb-0">Tresorerie et investissements.</p></div></article></div>
  <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-3", "Epargne") + """<div class="p-3"><h3 class="h6">Epargne</h3><p class="small text-secondary mb-0">Objectifs clairs, horizons realistes.</p></div></article></div>
</div></div></section>"""
    main += block_journey_m3(
        "Un RDV a l'agence, sans blabla",
        [
            {"title": "Tu prends RDV", "text": "En ligne ou au telephone - creneau sous 48 h.", "emotion": "Simple"},
            {"title": "On demele", "text": "Besoin, budget, delai - une paire de scenarios.", "emotion": "Clair"},
            {"title": "Decision locale", "text": "Ton dossier reste a Metz - pas perdu dans un call center.", "emotion": "Confiance"},
            {"title": "Suivi", "text": "Le meme conseiller quand tu reviens.", "emotion": "Serein"},
        ],
    )
    main += block_reviews_m3(
        title="Clients de l'agence",
        reviews=[
            {"text": "Credit habitat : reponse nette, interlocuteur unique.", "name": "Antoine", "meta": "Metz", "stars": 5},
            {"text": "Compte pro ouvert sans faire le nareux sur les pieces.", "name": "Leila", "meta": "Thionville", "stars": 4},
            {"text": "On peut se parler entre midi a l'agence.", "name": "Bruno", "meta": "Montigny", "stars": 5},
        ],
    )
    main += block_surface_band_m3(
        '<div class="container py-4">' + _stats_band([
            {"value": "1", "label": "Agence centre"},
            {"value": "48 h", "label": "RDV type"},
            {"value": "TPE", "label": "Accompagnees"},
            {"value": "Metz", "label": "Decisions"},
        ]) + "</div>",
        tone="soft",
    )
    main += """<section class="vt-cta-sticky py-4"><div class="container d-flex flex-wrap justify-content-between gap-3 align-items-center">
  <p class="mb-0">Besoin d'un credit ? On demele ca a l'agence.</p>
  <a class="btn btn-vt-primary" href="contact.html">Parler a un conseiller</a>
</div></section>"""
    main += block_fab_menu_m3([{"label": "RDV", "href": "contact.html"}, {"label": "Offres", "href": "offres.html"}, {"label": "Appeler", "href": "tel:0387159020"}], main_label="Actions banque")
    main += block_sticky_cta_m3("Parler a un conseiller ?", "RDV", "contact.html")
    main += "</main>"
    return _shell_ba("index.html", f"{BA_BRAND} - Banque Metz", "Banque locale a Metz : particuliers, pros, epargne.", main)


def build_banque_offres():
    main = f"""<main>{_progress(1)}<section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Offres</p><h1 class="vt-display h2 mb-3">Une paire d'offres utiles</h1><div class="row g-4"><div class="col-md-4">{_img("scene-1", "Compte")}</div><div class="col-md-4">{_img("scene-2", "Credit")}</div><div class="col-md-4">{_img("scene-3", "Epargne")}</div></div></div></section></main>"""
    return _shell_ba("offres.html", f"Offres - {BA_BRAND}", "Offres Banque des Ponts Metz.", main)


def build_banque_entreprises():
    main = f"""<main>{_progress(2)}<section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Entreprises</p><h1 class="vt-display h2 mb-3">Accompagner les TPE du Grand Est</h1><p class="lead text-secondary">Lignes de credit, encaissement, conseil - un referent unique.</p></div></section></main>"""
    return _shell_ba("entreprises.html", f"Entreprises - {BA_BRAND}", "Offres entreprises Banque des Ponts.", main)


def build_banque_contact():
    main = f"<main>{_progress(2)}" + _contact_m3(BA_ADDRESS, BA_PHONE, BA_EMAIL, "tel:0387159020", title="Prendre rendez-vous", lead="Place de la Comedie - agence de plein pied.") + "</main>"
    return _shell_ba("contact.html", f"Contact - {BA_BRAND}", "Contacter Banque des Ponts Metz.", main)


# --- Assurance : Couverture Est (Strasbourg) ---
AS_BRAND = "Couverture Est"
AS_PHONE = "03 88 41 72 60"
AS_EMAIL = "bonjour@couverture-est.fr"
AS_ADDRESS = "45 avenue de la Foret Noire, 67000 Strasbourg"
AS_MAPS = "https://maps.google.com/?q=45+avenue+de+la+Foret+Noire+67000+Strasbourg"
AS_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "particuliers.html", "label": "Particuliers"},
    {"file": "pros.html", "label": "Pros"},
    {"file": "contact.html", "label": "Contact"},
]
AS_FOOT = [("Particuliers", "particuliers.html"), ("Pros", "pros.html"), ("Devis", "contact.html"), ("Sinistre", "contact.html")]
AS_BN = [
    {"href": "index.html", "label": "Accueil", "ico": "🏠"},
    {"href": "particuliers.html", "label": "Offres", "ico": "📋"},
    {"href": "tel:0388417260", "label": "Appeler", "ico": "📞"},
    {"href": "contact.html", "label": "Devis", "ico": "✉"},
]


def _shell_as(page, title, desc, main):
    return _chrome_classic(
        brand=AS_BRAND, nav=AS_NAV, page=page, cta_label="Demander un devis", cta_href="contact.html", slug="assurance",
        status="Conseil · Lun-ven 9h-18h", address=AS_ADDRESS, phone=AS_PHONE, email=AS_EMAIL, maps=AS_MAPS,
        foot_links=AS_FOOT, hours="Strasbourg · Assurance", main=main, title=title, desc=desc, head=HEAD_ASSUR,
        body_class="vt-body vt-body-assurance", layout="assurance-m3", snack="Devis demande (demo)",
        bottom_items=AS_BN, mobile_label="Devis",
    )


def build_assurance_index():
    main = "<main>"
    main += f"""<section class="vt-hero-split vt-reveal">
  <div class="container">
    <div class="row g-4 align-items-center">
      <div class="col-lg-6">
        <p class="vt-eyebrow mb-2">Assurance · Strasbourg</p>
        <h1 class="vt-display display-4 mb-3">Couvrir ce qui compte - sans jargon</h1>
        <p class="lead mb-4">Auto, habitation, pro - on compare, on explique, tu decides.</p>
        <div class="vt-hero-actions">
          <button type="button" class="btn btn-vt-primary btn-lg" data-vt-dialog-open="devisAs">Demander un devis</button>
          <a class="btn btn-vt-outline btn-lg" href="particuliers.html">Particuliers</a>
        </div>
      </div>
      <div class="col-lg-6">{_img("hero", "Bureau Couverture Est Strasbourg", eager=True, cls="vt-hero-rounded")}</div>
    </div>
  </div>
</section>"""
    main += block_assist_chips([
        {"label": "Auto", "href": "particuliers.html", "active": True},
        {"label": "Habitation", "href": "particuliers.html"},
        {"label": "Pros", "href": "pros.html"},
        {"label": "Devis", "href": "contact.html"},
    ])
    main += """<section class="py-5 vt-reveal"><div class="container"><div class="row g-3">
  <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-1", "Auto") + """<div class="p-3"><h3 class="h6">Auto &amp; deux-roues</h3></div></article></div>
  <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-2", "Habitation") + """<div class="p-3"><h3 class="h6">Habitation</h3></div></article></div>
  <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-3", "Pro") + """<div class="p-3"><h3 class="h6">Professionnels</h3></div></article></div>
</div></div></section>"""
    main += block_journey_m3(
        "Comparer sans se perdre",
        [
            {"title": "Tu arrives avec ton contrat", "text": "Ou juste ton besoin - on part de la.", "emotion": "Simple"},
            {"title": "On compare", "text": "Garanties en francais clair, pas de roman.", "emotion": "Clair"},
            {"title": "Tu choisis", "text": "Pas la peine de faire le nareux : prix affiche.", "emotion": "Tranquille"},
            {"title": "Sinistre", "text": "Un seul contact - on suit le dossier.", "emotion": "Soutenu"},
        ],
    )
    main += block_reviews_m3(
        title="Ils ont change de contrat",
        reviews=[
            {"text": "Sinistre auto : dossier suivi, pas renvoye de service en service.", "name": "Paul", "meta": "Illkirch", "stars": 5},
            {"text": "Habitation : explications simples, devis en 24 h.", "name": "Marie", "meta": "Strasbourg", "stars": 5},
            {"text": "RC pro pour mon atelier - ca demele vite.", "name": "Karim", "meta": "Schiltigheim", "stars": 4},
        ],
    )
    main += block_surface_band_m3(
        '<div class="container py-4">' + _stats_band([
            {"value": "24 h", "label": "Devis type"},
            {"value": "1", "label": "Interlocuteur"},
            {"value": "Auto+", "label": "Familles"},
            {"value": "67", "label": "Base locale"},
        ]) + "</div>",
        tone="soft",
    )
    main += """<section class="vt-cta-sticky py-4"><div class="container d-flex flex-wrap justify-content-between gap-3 align-items-center">
  <p class="mb-0">Contrat a revoir ? Viens avec ton contrat actuel.</p>
  <a class="btn btn-vt-primary" href="contact.html">Obtenir un devis</a>
</div></section>"""
    main += block_dialog_m3(dialog_id="devisAs", title="Devis assurance", lead="On te recontacte sous 24 h (demo).", primary_label="Envoyer", primary_href="contact.html", fields_html='<div class="mb-2 vt-m3-field"><label class="form-label small">Besoin</label><select class="form-select"><option>Auto</option><option>Habitation</option><option>Pro</option></select></div>')
    main += block_fab_menu_m3([{"label": "Devis", "dialog": "devisAs"}, {"label": "Particuliers", "href": "particuliers.html"}, {"label": "Appeler", "href": "tel:0388417260"}], main_label="Actions assurance")
    main += block_sticky_cta_m3("Contrat a revoir ?", "Devis", "contact.html", dialog="devisAs")
    main += "</main>"
    return _shell_as("index.html", f"{AS_BRAND} - Assurance Strasbourg", "Courtier assurance a Strasbourg : auto, habitation, pro.", main)


def build_assurance_particuliers():
    main = f"""<main>{_progress(1)}<section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Particuliers</p><h1 class="vt-display h2 mb-3">Auto, maison, sante complementaire</h1><div class="row g-4"><div class="col-md-4">{_img("scene-1", "Auto")}</div><div class="col-md-4">{_img("scene-2", "Maison")}</div><div class="col-md-4">{_img("scene-3", "Famille")}</div></div></div></section></main>"""
    return _shell_as("particuliers.html", f"Particuliers - {AS_BRAND}", "Assurances particuliers Couverture Est.", main)


def build_assurance_pros():
    main = f"""<main>{_progress(2)}<section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Pros</p><h1 class="vt-display h2 mb-3">Proteger ton activite</h1><p class="lead text-secondary">RC pro, locaux, flotte - pour artisans et commerces du Grand Est.</p></div></section></main>"""
    return _shell_as("pros.html", f"Pros - {AS_BRAND}", "Assurances professionnelles Strasbourg.", main)


def build_assurance_contact():
    main = f"<main>{_progress(2)}" + _contact_m3(AS_ADDRESS, AS_PHONE, AS_EMAIL, "tel:0388417260", title="Demander un devis", lead="Avenue de la Foret Noire - on peut couatcher 15 minutes.") + "</main>"
    return _shell_as("contact.html", f"Contact - {AS_BRAND}", "Contacter Couverture Est Strasbourg.", main)


# --- Logistique : Flux Lorraine (Epinal) ---
LO_BRAND = "Flux Lorraine"
LO_PHONE = "03 29 34 81 50"
LO_EMAIL = "ops@flux-lorraine.fr"
LO_ADDRESS = "Zone industrielle de la Voivre, 88000 Epinal"
LO_MAPS = "https://maps.google.com/?q=Zone+industrielle+Voivre+88000+Epinal"
LO_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "services.html", "label": "Services"},
    {"file": "zones.html", "label": "Zones"},
    {"file": "contact.html", "label": "Contact"},
]
LO_FOOT = [("Services", "services.html"), ("Zones", "zones.html"), ("Devis", "contact.html"), ("Entrepot", "contact.html")]
LO_BN = [
    {"href": "index.html", "label": "Accueil", "ico": "🏠"},
    {"href": "services.html", "label": "Services", "ico": "📋"},
    {"href": "tel:0329348150", "label": "Appeler", "ico": "📞"},
    {"href": "contact.html", "label": "Devis", "ico": "✉"},
]


def _shell_lo(page, title, desc, main):
    return _chrome_classic(
        brand=LO_BRAND, nav=LO_NAV, page=page, cta_label="Demander un devis", cta_href="contact.html", slug="logistique",
        status="Ops · Lun-sam 6h-20h", address=LO_ADDRESS, phone=LO_PHONE, email=LO_EMAIL, maps=LO_MAPS,
        foot_links=LO_FOOT, hours="Epinal · Logistique", main=main, title=title, desc=desc, head=HEAD_LOGI,
        body_class="vt-body vt-body-logistique", layout="logistique-m3", snack="RFQ enregistree (demo)",
        bottom_items=LO_BN, mobile_label="Devis",
    )


def build_logistique_index():
    main = "<main>"
    main += f"""<section class="vt-hero-bleed vt-hero-industrial vt-reveal">
  {_img("hero", "Entrepot Flux Lorraine Epinal", eager=True, cls="vt-hero-bleed-img")}
  <div class="vt-hero-bleed-copy">
    <div class="container">
      <p class="vt-eyebrow mb-2">Logistique · Epinal</p>
      <h1 class="vt-display display-3 mb-3">Stockage, picking, livraison - sur le terrain</h1>
      <p class="lead mb-4">B2B Grand Est : entrepot, preparation de commandes, tours reguliers.</p>
      <div class="vt-hero-actions">
        <a class="btn btn-vt-primary btn-lg" href="contact.html">Demander un devis</a>
        <a class="btn btn-vt-outline btn-lg" href="services.html">Nos services</a>
      </div>
    </div>
  </div>
</section>"""
    main += block_assist_chips([
        {"label": "Stockage", "href": "services.html", "active": True},
        {"label": "Picking", "href": "services.html"},
        {"label": "Zones", "href": "zones.html"},
        {"label": "Devis", "href": "contact.html"},
    ])
    main += """<section class="py-5 vt-reveal"><div class="container"><div class="row g-3">
  <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-1", "Stockage") + """<div class="p-3"><h3 class="h6">Stockage</h3><p class="small text-secondary mb-0">Palettes et lots securises.</p></div></article></div>
  <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-2", "Picking") + """<div class="p-3"><h3 class="h6">Preparation</h3><p class="small text-secondary mb-0">Commandes a l'heure.</p></div></article></div>
  <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-3", "Livraison") + """<div class="p-3"><h3 class="h6">Livraison</h3><p class="small text-secondary mb-0">Tours Lorraine &amp; Grand Est.</p></div></article></div>
</div></div></section>"""
    main += block_journey_m3(
        "Du brief au quai",
        [
            {"title": "Tu poses le volume", "text": "Palettes, rythme, destinations - on ecoute.", "emotion": "Cadre"},
            {"title": "On propose", "text": "Slot entrepot + tours - devis net.", "emotion": "Clair"},
            {"title": "On execute", "text": "Picking, expedition, suivi temps reel.", "emotion": "Fiable"},
            {"title": "Tu scales", "text": "Pics saisonniers sans changer de partenaire.", "emotion": "Soulage"},
        ],
    )
    main += block_reviews_m3(
        title="Clients ops",
        reviews=[
            {"text": "Pics de Noel absorbes - picking a l'heure.", "name": "Agence Nord", "meta": "Nancy", "stars": 5},
            {"text": "Entrepot propre, inventaire fiable.", "name": "SME Vosges", "meta": "Epinal", "stars": 5},
            {"text": "Tours Metz-Nancy reguliers, contact unique.", "name": "Distrib Est", "meta": "Metz", "stars": 4},
        ],
    )
    main += block_surface_band_m3(
        '<div class="container py-4">' + _stats_band([
            {"value": "6h-20h", "label": "Ops"},
            {"value": "3", "label": "Regions"},
            {"value": "B2B", "label": "Focus"},
            {"value": "ZI", "label": "Voivre"},
        ]) + "</div>",
        tone="soft",
    )
    main += """<section class="vt-cta-sticky py-4"><div class="container d-flex flex-wrap justify-content-between gap-3 align-items-center">
  <p class="mb-0">Volume a absorber ? Dis voir ton flux.</p>
  <a class="btn btn-vt-primary" href="contact.html">Parler ops</a>
</div></section>"""
    main += block_fab_menu_m3([{"label": "Devis", "href": "contact.html"}, {"label": "Services", "href": "services.html"}, {"label": "Appeler", "href": "tel:0329348150"}], main_label="Actions logistique")
    main += block_sticky_cta_m3("Volume a poser ?", "Devis", "contact.html")
    main += "</main>"
    return _shell_lo("index.html", f"{LO_BRAND} - Logistique Epinal", "Logistique B2B a Epinal : stockage, picking, livraison.", main)


def build_logistique_services():
    main = f"""<main>{_progress(1)}<section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Services</p><h1 class="vt-display h2 mb-3">Ce qu'on fait pour toi</h1><div class="row g-4"><div class="col-md-4">{_img("scene-1", "Quai")}</div><div class="col-md-4">{_img("scene-2", "Rayonnage")}</div><div class="col-md-4">{_img("scene-3", "Camion")}</div></div></div></section></main>"""
    return _shell_lo("services.html", f"Services - {LO_BRAND}", "Services Flux Lorraine Epinal.", main)


def build_logistique_zones():
    main = f"""<main>{_progress(2)}<section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Zones</p><h1 class="vt-display h2 mb-3">Epinal, Nancy, Metz et au-dela</h1><p class="lead text-secondary">Tours reguliers Vosges, Meurthe-et-Moselle, Moselle.</p></div></section></main>"""
    return _shell_lo("zones.html", f"Zones - {LO_BRAND}", "Zones de livraison Flux Lorraine.", main)


def build_logistique_contact():
    main = f"<main>{_progress(2)}" + _contact_m3(LO_ADDRESS, LO_PHONE, LO_EMAIL, "tel:0329348150", title="Demander un devis", lead="ZI de la Voivre - on repond vite aux ops.") + "</main>"
    return _shell_lo("contact.html", f"Contact - {LO_BRAND}", "Contacter Flux Lorraine Epinal.", main)


# --- Promoteur : Habitat Horizon (Nancy) ---
PR_BRAND = "Habitat Horizon"
PR_PHONE = "03 83 19 44 70"
PR_EMAIL = "projets@habitat-horizon.fr"
PR_ADDRESS = "28 boulevard Joffre, 54000 Nancy"
PR_MAPS = "https://maps.google.com/?q=28+boulevard+Joffre+54000+Nancy"
PR_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "programmes.html", "label": "Programmes"},
    {"file": "accompagnement.html", "label": "Accompagnement"},
    {"file": "contact.html", "label": "Contact"},
]
PR_FOOT = [("Programmes", "programmes.html"), ("Accompagnement", "accompagnement.html"), ("Contact", "contact.html"), ("Bureau", "contact.html")]
PR_BN = [
    {"href": "index.html", "label": "Accueil", "ico": "🏠"},
    {"href": "programmes.html", "label": "Programmes", "ico": "📋"},
    {"href": "tel:0383194470", "label": "Appeler", "ico": "📞"},
    {"href": "contact.html", "label": "Visite", "ico": "✉"},
]


def _shell_pr(page, title, desc, main):
    return _chrome_classic(
        brand=PR_BRAND, nav=PR_NAV, page=page, cta_label="Visiter un programme", cta_href="contact.html", slug="promoteur",
        status="Bureau ventes · Sur RDV", address=PR_ADDRESS, phone=PR_PHONE, email=PR_EMAIL, maps=PR_MAPS,
        foot_links=PR_FOOT, hours="Nancy · Promoteur", main=main, title=title, desc=desc, head=HEAD_PROMO,
        body_class="vt-body vt-body-promoteur", layout="promoteur-m3", snack="Visite demandee (demo)",
        bottom_items=PR_BN, mobile_label="Visite",
    )


def build_promoteur_index():
    main = "<main>"
    main += f"""<section class="vt-hero-bleed vt-reveal">
  {_img("hero", "Residence Habitat Horizon Nancy", eager=True, cls="vt-hero-bleed-img")}
  <div class="vt-hero-bleed-copy">
    <div class="container">
      <p class="vt-eyebrow mb-2">Promoteur · Nancy</p>
      <h1 class="vt-display display-3 mb-3">Des logements penses pour y vivre vraiment</h1>
      <p class="lead mb-4">Programmes neufs autour de Nancy - plans clairs, accompagnement jusqu'aux cles.</p>
      <div class="vt-hero-actions">
        <a class="btn btn-vt-primary btn-lg" href="programmes.html">Voir les programmes</a>
        <a class="btn btn-vt-outline btn-lg" href="contact.html">Prendre RDV</a>
      </div>
    </div>
  </div>
</section>"""
    main += block_assist_chips([
        {"label": "T2", "href": "programmes.html", "active": True},
        {"label": "T3-T4", "href": "programmes.html"},
        {"label": "Maisons", "href": "programmes.html"},
        {"label": "Visite", "href": "contact.html"},
    ])
    main += """<section class="py-5 vt-reveal"><div class="container"><div class="row g-3">
  <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-1", "T2") + """<div class="p-3"><h3 class="h6">Studios &amp; T2</h3><p class="small text-secondary mb-0">Investissement ou premier toit.</p></div></article></div>
  <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-2", "T3") + """<div class="p-3"><h3 class="h6">T3 &amp; T4</h3><p class="small text-secondary mb-0">Familles, balcons, rangements.</p></div></article></div>
  <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-3", "Jardin") + """<div class="p-3"><h3 class="h6">Maisons de ville</h3><p class="small text-secondary mb-0">Jardin, garage, calme.</p></div></article></div>
</div></div></section>"""
    main += block_journey_m3(
        "Du plan a la remise des cles",
        [
            {"title": "Visite showroom", "text": "Plans, maquettes, questions sans filtre.", "emotion": "Curieux"},
            {"title": "Reservation", "text": "Lot choisi, calendrier clair.", "emotion": "Engage"},
            {"title": "Chantier", "text": "Un contact pour les finitions et le suivi.", "emotion": "Suivi"},
            {"title": "Remise", "text": "Reception, cles, checklist - on reste joignable.", "emotion": "Chez soi"},
        ],
    )
    main += block_reviews_m3(
        title="Acheteurs autour de Nancy",
        reviews=[
            {"text": "Showroom clair - on a choisi sans pression.", "name": "Famille Klein", "meta": "Vandoeuvre", "stars": 5},
            {"text": "Suivi chantier : un seul interlocuteur, top.", "name": "Julie", "meta": "Nancy", "stars": 5},
            {"text": "Livraison dans les delais annonces.", "name": "Marc", "meta": "Laxou", "stars": 4},
        ],
    )
    main += block_surface_band_m3(
        '<div class="container py-4">' + _stats_band([
            {"value": "3", "label": "Programmes"},
            {"value": "Nancy", "label": "Secteur"},
            {"value": "1", "label": "Contact"},
            {"value": "VEFA", "label": "Cadre"},
        ]) + "</div>",
        tone="soft",
    )
    main += """<section class="vt-cta-sticky py-4"><div class="container d-flex flex-wrap justify-content-between gap-3 align-items-center">
  <p class="mb-0">Envie de visiter ? On ouvre le showroom.</p>
  <a class="btn btn-vt-primary" href="contact.html">Prendre RDV</a>
</div></section>"""
    main += block_fab_menu_m3([{"label": "RDV", "href": "contact.html"}, {"label": "Programmes", "href": "programmes.html"}, {"label": "Appeler", "href": "tel:0383194470"}], main_label="Actions promoteur")
    main += block_sticky_cta_m3("Visiter un programme ?", "RDV", "contact.html")
    main += "</main>"
    return _shell_pr("index.html", f"{PR_BRAND} - Promoteur Nancy", "Promoteur immobilier a Nancy : programmes neufs.", main)


def build_promoteur_programmes():
    main = f"""<main>{_progress(1)}<section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Programmes</p><h1 class="vt-display h2 mb-3">En commercialisation</h1><div class="row g-4"><div class="col-md-4">{_img("scene-1", "Residence A")}</div><div class="col-md-4">{_img("scene-2", "Residence B")}</div><div class="col-md-4">{_img("scene-3", "Maison")}</div></div></div></section></main>"""
    return _shell_pr("programmes.html", f"Programmes - {PR_BRAND}", "Programmes Habitat Horizon Nancy.", main)


def build_promoteur_accompagnement():
    main = f"""<main>{_progress(2)}<section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Accompagnement</p><h1 class="vt-display h2 mb-3">Du plan a la remise des cles</h1><p class="lead text-secondary">Choix des finitions, suivi chantier, reception - un seul contact.</p></div></section></main>"""
    return _shell_pr("accompagnement.html", f"Accompagnement - {PR_BRAND}", "Accompagnement acheteur Habitat Horizon.", main)


def build_promoteur_contact():
    main = f"<main>{_progress(2)}" + _contact_m3(PR_ADDRESS, PR_PHONE, PR_EMAIL, "tel:0383194470", title="Visiter un programme", lead="Boulevard Joffre - bureau ventes sur RDV.") + "</main>"
    return _shell_pr("contact.html", f"Contact - {PR_BRAND}", "Contacter Habitat Horizon Nancy.", main)


# --- Notaire : Etude Deschamps (Metz) ---
NO_BRAND = "Etude Deschamps"
NO_PHONE = "03 87 75 33 10"
NO_EMAIL = "contact@etude-deschamps.fr"
NO_ADDRESS = "17 en Fournirue, 57000 Metz"
NO_MAPS = "https://maps.google.com/?q=17+en+Fournirue+57000+Metz"
NO_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "domaines.html", "label": "Domaines"},
    {"file": "equipe.html", "label": "Equipe"},
    {"file": "contact.html", "label": "Contact"},
]
NO_FOOT = [("Domaines", "domaines.html"), ("Equipe", "equipe.html"), ("RDV", "contact.html"), ("Etude", "contact.html")]
NO_BN = [
    {"href": "index.html", "label": "Accueil", "ico": "🏠"},
    {"href": "domaines.html", "label": "Domaines", "ico": "📋"},
    {"href": "tel:0387753310", "label": "Appeler", "ico": "📞"},
    {"href": "contact.html", "label": "RDV", "ico": "✉"},
]


def _shell_no(page, title, desc, main):
    return _chrome_classic(
        brand=NO_BRAND, nav=NO_NAV, page=page, cta_label="Prendre RDV", cta_href="contact.html", slug="notaire",
        status="Etude · Lun-ven 9h-12h / 14h-18h", address=NO_ADDRESS, phone=NO_PHONE, email=NO_EMAIL, maps=NO_MAPS,
        foot_links=NO_FOOT, hours="Metz · Notaire", main=main, title=title, desc=desc, head=HEAD_NOTAIRE,
        body_class="vt-body vt-body-notaire", layout="notaire-m3", snack="RDV etude (demo)",
        bottom_items=NO_BN, mobile_label="RDV",
    )


def build_notaire_index():
    main = "<main>"
    main += f"""<section class="vt-hero-split vt-reveal">
  <div class="container">
    <div class="row g-4 align-items-center">
      <div class="col-lg-6">
        <p class="vt-eyebrow mb-2">Notaire · Metz</p>
        <h1 class="vt-display display-4 mb-3">Actes clairs, echanges sobres</h1>
        <p class="lead mb-4">Immobilier, famille, entreprise - on t'explique chaque etape avant de signer.</p>
        <div class="vt-hero-actions">
          <a class="btn btn-vt-primary btn-lg" href="contact.html">Prendre rendez-vous</a>
          <a class="btn btn-vt-outline btn-lg" href="domaines.html">Nos domaines</a>
        </div>
      </div>
      <div class="col-lg-6">{_img("hero", "Etude Deschamps Metz", eager=True, cls="vt-hero-rounded")}</div>
    </div>
  </div>
</section>"""
    main += block_assist_chips([
        {"label": "Immobilier", "href": "domaines.html", "active": True},
        {"label": "Famille", "href": "domaines.html"},
        {"label": "Entreprise", "href": "domaines.html"},
        {"label": "RDV", "href": "contact.html"},
    ])
    main += """<section class="py-5 vt-reveal"><div class="container"><div class="row g-3">
  <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-1", "Immobilier") + """<div class="p-3"><h3 class="h6">Immobilier</h3></div></article></div>
  <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-2", "Famille") + """<div class="p-3"><h3 class="h6">Famille &amp; succession</h3></div></article></div>
  <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-3", "Entreprise") + """<div class="p-3"><h3 class="h6">Entreprise</h3></div></article></div>
</div></div></section>"""
    main += block_journey_m3(
        "Avant de signer",
        [
            {"title": "Premier echange", "text": "Tu poses le besoin - on liste les pieces.", "emotion": "Clair"},
            {"title": "Preparation", "text": "Dossier assemble, questions repondues.", "emotion": "Prepare"},
            {"title": "Signature", "text": "Chaque clause expliquee - pas de surprise.", "emotion": "Serein"},
            {"title": "Apres", "text": "Actes remis, suivi si besoin.", "emotion": "Termine"},
        ],
    )
    main += block_reviews_m3(
        title="Clients de l'etude",
        reviews=[
            {"text": "Vente immo : delais tenus, explications nettes.", "name": "Famille Ort", "meta": "Metz", "stars": 5},
            {"text": "Succession demelee sans jargon inutile.", "name": "Helene", "meta": "Thionville", "stars": 5},
            {"text": "RDV entre midi possible - pratique.", "name": "David", "meta": "Montigny", "stars": 4},
        ],
    )
    main += block_surface_band_m3(
        '<div class="container py-4">' + _stats_band([
            {"value": "3", "label": "Domaines"},
            {"value": "Metz", "label": "Etude"},
            {"value": "1", "label": "Contact dossier"},
            {"value": "Lun-ven", "label": "Ouverture"},
        ]) + "</div>",
        tone="soft",
    )
    main += """<section class="vt-cta-sticky py-4"><div class="container d-flex flex-wrap justify-content-between gap-3 align-items-center">
  <p class="mb-0">Dossier a preparer ? On liste les pieces ensemble.</p>
  <a class="btn btn-vt-primary" href="contact.html">Contacter l'etude</a>
</div></section>"""
    main += block_fab_menu_m3([{"label": "RDV", "href": "contact.html"}, {"label": "Domaines", "href": "domaines.html"}, {"label": "Appeler", "href": "tel:0387753310"}], main_label="Actions etude")
    main += block_sticky_cta_m3("Dossier a poser ?", "RDV", "contact.html")
    main += "</main>"
    return _shell_no("index.html", f"{NO_BRAND} - Notaire Metz", "Etude notariale a Metz : immobilier, famille, entreprise.", main)


def build_notaire_domaines():
    main = f"""<main>{_progress(1)}<section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Domaines</p><h1 class="vt-display h2 mb-3">Nos domaines d'intervention</h1><div class="row g-4"><div class="col-md-4">{_img("scene-1", "Vente")}</div><div class="col-md-4">{_img("scene-2", "Succession")}</div><div class="col-md-4">{_img("scene-3", "Societe")}</div></div></div></section></main>"""
    return _shell_no("domaines.html", f"Domaines - {NO_BRAND}", "Domaines Etude Deschamps Metz.", main)


def build_notaire_equipe():
    main = f"""<main>{_progress(2)}<section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Equipe</p><h1 class="vt-display h2 mb-3">Notaires et clercs</h1><p class="lead text-secondary">Un interlocuteur dedie pour ton dossier.</p></div></section></main>"""
    return _shell_no("equipe.html", f"Equipe - {NO_BRAND}", "Equipe Etude Deschamps Metz.", main)


def build_notaire_contact():
    main = f"<main>{_progress(2)}" + _contact_m3(NO_ADDRESS, NO_PHONE, NO_EMAIL, "tel:0387753310", title="Prendre rendez-vous", lead="En Fournirue - etude accessible a pied.") + "</main>"
    return _shell_no("contact.html", f"Contact - {NO_BRAND}", "Contacter Etude Deschamps Metz.", main)


# --- Yoga : Studio Souffle (Metz) ---
YO_BRAND = "Studio Souffle"
YO_PHONE = "03 87 42 56 80"
YO_EMAIL = "hello@studio-souffle.fr"
YO_ADDRESS = "11 rue du Palais, 57000 Metz"
YO_MAPS = "https://maps.google.com/?q=11+rue+du+Palais+57000+Metz"
YO_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "cours.html", "label": "Cours"},
    {"file": "planning.html", "label": "Planning"},
    {"file": "contact.html", "label": "Contact"},
]
YO_FOOT = [("Cours", "cours.html"), ("Planning", "planning.html"), ("Essai", "contact.html"), ("Studio", "contact.html")]
YO_BN = [
    {"href": "index.html", "label": "Accueil", "ico": "🏠"},
    {"href": "cours.html", "label": "Cours", "ico": "📋"},
    {"href": "tel:0387425680", "label": "Appeler", "ico": "📞"},
    {"href": "contact.html", "label": "Essai", "ico": "✉"},
]


def _shell_yo(page, title, desc, main):
    return _chrome_pill(
        brand=YO_BRAND, nav=YO_NAV, page=page, cta_label="Essayer un cours", cta_href="contact.html",
        cta_dialog="essaiYo", slug="yoga", phone=YO_PHONE, email=YO_EMAIL, address=YO_ADDRESS, maps=YO_MAPS,
        foot_links=YO_FOOT, hours="Metz · Yoga", subtitle="Studio · Metz",
        main=main, title=title, desc=desc, head=HEAD_YOGA,
        body_class="vt-body vt-body-yoga vt-body-pill", layout="yoga-m3",
        snack="Essai reserve (demo)", bottom_items=YO_BN,
    )


def build_yoga_index():
    main = "<main>"
    main += f"""<section class="vt-hero-bleed vt-hero-wellness vt-reveal">
  {_img("hero", "Studio Souffle Metz", eager=True, cls="vt-hero-bleed-img")}
  <div class="vt-hero-bleed-copy">
    <div class="container">
      <p class="vt-eyebrow mb-2">Yoga · Metz</p>
      <h1 class="vt-display display-3 mb-3">Respirer, bouger, revenir a soi</h1>
      <p class="lead mb-4">Cours doux ou dynamiques - debutants bienvenus, sans pression.</p>
      <div class="vt-hero-actions">
        <button type="button" class="btn btn-vt-primary btn-lg" data-vt-dialog-open="essaiYo">Essayer un cours</button>
        <a class="btn btn-vt-outline btn-lg" href="planning.html">Voir le planning</a>
      </div>
    </div>
  </div>
</section>"""
    main += block_assist_chips([
        {"label": "Hatha", "href": "cours.html", "active": True},
        {"label": "Vinyasa", "href": "cours.html"},
        {"label": "Yin", "href": "cours.html"},
        {"label": "Essai", "href": "contact.html"},
    ])
    main += """<section class="py-5 vt-reveal"><div class="container"><div class="row g-3">
  <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-1", "Hatha") + """<div class="p-3"><h3 class="h6">Hatha</h3><p class="small text-secondary mb-0">Postures posees.</p></div></article></div>
  <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-2", "Vinyasa") + """<div class="p-3"><h3 class="h6">Vinyasa</h3><p class="small text-secondary mb-0">Flux et souffle.</p></div></article></div>
  <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-3", "Yin") + """<div class="p-3"><h3 class="h6">Yin</h3><p class="small text-secondary mb-0">Lenteur et recuperation.</p></div></article></div>
</div></div></section>"""
    main += block_journey_m3(
        "Ton premier cours",
        [
            {"title": "Tu reserves", "text": "Essai offert - viens avec ton tapis (ou le notre).", "emotion": "Leger"},
            {"title": "Accueil", "text": "On te place, sans te mettre en avant.", "emotion": "Accueilli"},
            {"title": "Pratique", "text": "Options pour chaque posture - a ton rythme.", "emotion": "Present"},
            {"title": "Apres", "text": "Un the, deux questions - tu reviens si ca te parle.", "emotion": "Zen"},
        ],
    )
    main += block_reviews_m3(
        title="Eleve·es du studio",
        reviews=[
            {"text": "Premiere seance sans stress - on m'a laisse aller a mon rythme.", "name": "Lea", "meta": "Metz", "stars": 5},
            {"text": "Yin le soir : parfait apres une journee au magasin.", "name": "Nora", "meta": "Montigny", "stars": 5},
            {"text": "Studio calme, rue du Palais - facile a trouver.", "name": "Tom", "meta": "Metz", "stars": 4},
        ],
    )
    main += block_surface_band_m3(
        '<div class="container py-4">' + _stats_band([
            {"value": "3", "label": "Styles"},
            {"value": "7j", "label": "Planning"},
            {"value": "1er", "label": "Essai offert"},
            {"value": "12", "label": "Places max"},
        ]) + "</div>",
        tone="soft",
    )
    main += """<section class="vt-cta-sticky py-4"><div class="container d-flex flex-wrap justify-content-between gap-3 align-items-center">
  <p class="mb-0">Premier cours offert cette semaine - viens avec ton tapis.</p>
  <a class="btn btn-vt-primary" href="contact.html">Reserver l'essai</a>
</div></section>"""
    main += block_dialog_m3(dialog_id="essaiYo", title="Essayer un cours", lead="On te confirme le creneau (demo).", primary_label="Envoyer", primary_href="contact.html", fields_html='<div class="mb-2 vt-m3-field"><label class="form-label small">Style</label><select class="form-select"><option>Hatha</option><option>Vinyasa</option><option>Yin</option></select></div>')
    main += block_fab_menu_m3([{"label": "Essai", "dialog": "essaiYo"}, {"label": "Planning", "href": "planning.html"}, {"label": "Appeler", "href": "tel:0387425680"}], main_label="Actions studio")
    main += block_sticky_cta_m3("Pret a bouger ?", "Essai", "contact.html", dialog="essaiYo")
    main += "</main>"
    return _shell_yo("index.html", f"{YO_BRAND} - Yoga Metz", "Studio de yoga a Metz : hatha, vinyasa, yin.", main)


def build_yoga_cours():
    main = f"""<main>{_progress(1)}<section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Cours</p><h1 class="vt-display h2 mb-3">Les styles proposes</h1><div class="row g-4"><div class="col-md-4">{_img("scene-1", "Hatha")}</div><div class="col-md-4">{_img("scene-2", "Vinyasa")}</div><div class="col-md-4">{_img("scene-3", "Yin")}</div></div></div></section></main>"""
    return _shell_yo("cours.html", f"Cours - {YO_BRAND}", "Cours Studio Souffle Metz.", main)


def build_yoga_planning():
    main = f"""<main>{_progress(2)}<section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Planning</p><h1 class="vt-display h2 mb-3">Semaine type</h1><p class="lead text-secondary">Matins calmes, soirs dynamiques - detail sur demande.</p><a class="btn btn-vt-primary" href="contact.html">Recevoir le planning</a></div></section></main>"""
    return _shell_yo("planning.html", f"Planning - {YO_BRAND}", "Planning Studio Souffle Metz.", main)


def build_yoga_contact():
    main = f"<main>{_progress(2)}" + _contact_m3(YO_ADDRESS, YO_PHONE, YO_EMAIL, "tel:0387425680", title="Essayer un cours", lead="Rue du Palais - studio au calme.") + "</main>"
    return _shell_yo("contact.html", f"Contact - {YO_BRAND}", "Contacter Studio Souffle Metz.", main)


# --- Electricien : Volt & Clanche (Metz) ---
EL_BRAND = "Volt & Clanche"
EL_PHONE = "03 87 91 20 45"
EL_EMAIL = "urgence@volt-clanche.fr"
EL_ADDRESS = "Zone artisanale Sud, 57070 Metz"
EL_MAPS = "https://maps.google.com/?q=Metz+57070+electricien"
EL_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "services.html", "label": "Services"},
    {"file": "zones.html", "label": "Zones"},
    {"file": "contact.html", "label": "Contact"},
]
EL_FOOT = [("Services", "services.html"), ("Zones", "zones.html"), ("Devis", "contact.html"), ("Urgence", "tel:0387912045")]
EL_BN = [
    {"href": "index.html", "label": "Accueil", "ico": "🏠"},
    {"href": "services.html", "label": "Services", "ico": "📋"},
    {"href": "tel:0387912045", "label": "Appeler", "ico": "📞"},
    {"href": "contact.html", "label": "Devis", "ico": "✉"},
]


def _shell_el(page, title, desc, main):
    return _chrome_classic(
        brand=EL_BRAND, nav=EL_NAV, page=page, cta_label="Appeler maintenant", cta_href="tel:0387912045", slug="electricien",
        status="Urgence 24/7 · Metz", address=EL_ADDRESS, phone=EL_PHONE, email=EL_EMAIL, maps=EL_MAPS,
        foot_links=EL_FOOT, hours="Metz · Electricite", main=main, title=title, desc=desc, head=HEAD_ELEC,
        body_class="vt-body vt-body-electricien", layout="electricien-m3", snack="Devis demande (demo)",
        bottom_items=EL_BN, mobile_label="Appeler",
    )


def build_electricien_index():
    main = "<main>"
    main += f"""<section class="vt-hero-urgency vt-reveal">
  <div class="container">
    <div class="row g-4 align-items-start">
      <div class="col-lg-7">
        <p class="vt-eyebrow mb-2">Electricien · Metz</p>
        <h1 class="vt-display display-4 mb-3">Panne, mise aux normes, tableau - on intervient</h1>
        <p class="lead mb-3">Depannage rapide, devis avant travaux, zones Metz et alentours.</p>
        <ul class="vt-trust-list mb-4"><li>Urgence 24h/24</li><li>Devis clair</li><li>Garantie travaux</li></ul>
        <div class="vt-hero-actions">
          <a class="btn btn-vt-primary btn-lg" href="tel:0387912045">Appeler {EL_PHONE}</a>
          <button type="button" class="btn btn-vt-outline btn-lg" data-vt-dialog-open="devisEl">Devis gratuit</button>
        </div>
      </div>
      <div class="col-lg-5">{_img("hero", "Intervention electricien Metz", eager=True, cls="vt-hero-rounded")}</div>
    </div>
    <div class="row g-3 mt-4">
      <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-1", "Depannage") + """<div class="p-3"><h3 class="h6">Depannage</h3></div></article></div>
      <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-2", "Tableau") + """<div class="p-3"><h3 class="h6">Tableau electrique</h3></div></article></div>
      <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-3", "Normes") + """<div class="p-3"><h3 class="h6">Mise aux normes</h3></div></article></div>
    </div>
  </div>
</section>"""
    main += block_assist_chips([
        {"label": "Urgence", "href": "tel:0387912045", "active": True},
        {"label": "Tableau", "href": "services.html"},
        {"label": "Zones", "href": "zones.html"},
        {"label": "Devis", "href": "contact.html"},
    ])
    main += block_journey_m3(
        "De l'appel a la remise en service",
        [
            {"title": "Tu appelles", "text": "Plus de courant ? On demele ca.", "emotion": "Urgent"},
            {"title": "Diag", "text": "Sur place - explication simple du souci.", "emotion": "Compris"},
            {"title": "Devis", "text": "Prix avant travaux - pas de surprise.", "emotion": "Clair"},
            {"title": "Travaux", "text": "Intervention, test, garantie.", "emotion": "Soulage"},
        ],
    )
    main += block_reviews_m3(
        title="Clients depannes",
        reviews=[
            {"text": "Panne un dimanche - arrives vite, devis net.", "name": "Famille Beck", "meta": "Woippy", "stars": 5},
            {"text": "Tableau refait, mise aux normes nickel.", "name": "Carole", "meta": "Metz", "stars": 5},
            {"text": "Comme la clanche : ca ouvre quand il faut.", "name": "Eric", "meta": "Montigny", "stars": 4},
        ],
    )
    main += block_surface_band_m3(
        '<div class="container py-4">' + _stats_band([
            {"value": "24/7", "label": "Urgence"},
            {"value": "Metz+", "label": "Zones"},
            {"value": "Devis", "label": "Avant travaux"},
            {"value": "Garantie", "label": "Incluse"},
        ]) + "</div>",
        tone="soft",
    )
    main += """<section class="vt-cta-sticky py-4 vt-cta-urgent"><div class="container d-flex flex-wrap justify-content-between gap-3 align-items-center">
  <p class="mb-0 fw-bold">Plus de courant ? On demele ca.</p>
  <a class="btn btn-vt-primary" href="tel:0387912045">Appeler maintenant</a>
</div></section>"""
    main += block_dialog_m3(dialog_id="devisEl", title="Devis gratuit", lead="Decris le souci - on te rappelle (demo).", primary_label="Envoyer", primary_href="contact.html", fields_html='<div class="mb-2 vt-m3-field"><label class="form-label small">Type</label><select class="form-select"><option>Panne</option><option>Tableau</option><option>Mise aux normes</option><option>Eclairage</option></select></div><div class="mb-2 vt-m3-field"><label class="form-label small">Telephone</label><input class="form-control" type="tel"></div>')
    main += block_fab_menu_m3([{"label": "Appeler", "href": "tel:0387912045"}, {"label": "Devis", "dialog": "devisEl"}, {"label": "Zones", "href": "zones.html"}], main_label="Actions urgence")
    main += block_sticky_cta_m3("Panne en cours ?", "Appeler", "tel:0387912045")
    main += "</main>"
    return _shell_el("index.html", f"{EL_BRAND} - Electricien Metz", "Electricien urgence a Metz : depannage, normes, tableaux.", main)


def build_electricien_services():
    main = f"""<main>{_progress(1)}<section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Services</p><h1 class="vt-display h2 mb-3">Ce qu'on prend en charge</h1><div class="row g-4"><div class="col-md-4">{_img("scene-1", "Depannage")}</div><div class="col-md-4">{_img("scene-2", "Renovation")}</div><div class="col-md-4">{_img("scene-3", "IRVE")}</div></div></div></section></main>"""
    return _shell_el("services.html", f"Services - {EL_BRAND}", "Services electricien Volt et Clanche Metz.", main)


def build_electricien_zones():
    main = f"""<main>{_progress(2)}<section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Zones</p><h1 class="vt-display h2 mb-3">Metz et alentours</h1><p class="lead text-secondary">Metz, Montigny, Woippy, Longeville - arrivee rapide.</p></div></section></main>"""
    return _shell_el("zones.html", f"Zones - {EL_BRAND}", "Zones d'intervention electricien Metz.", main)


def build_electricien_contact():
    main = f"<main>{_progress(2)}" + _contact_m3(EL_ADDRESS, EL_PHONE, EL_EMAIL, "tel:0387912045", title="Urgence ou devis", lead="ZA Sud - urgence 24/7 au telephone.") + "</main>"
    return _shell_el("contact.html", f"Contact - {EL_BRAND}", "Contacter Volt et Clanche Metz.", main)


# --- Gites : Les Lucioles (Vosges) ---
GI_BRAND = "Les Lucioles"
GI_PHONE = "03 29 58 14 22"
GI_EMAIL = "bonjour@les-lucioles-vosges.fr"
GI_ADDRESS = "12 chemin des Sapins, 88400 Gerardmer"
GI_MAPS = "https://maps.google.com/?q=Gerardmer+88400+gite"
GI_NAV = [
    {"file": "index.html", "label": "Accueil"},
    {"file": "hebergements.html", "label": "Hebergements"},
    {"file": "sejours.html", "label": "Sejours"},
    {"file": "contact.html", "label": "Contact"},
]
GI_FOOT = [("Hebergements", "hebergements.html"), ("Sejours", "sejours.html"), ("Reserver", "contact.html"), ("Acces", "contact.html")]
GI_BN = [
    {"href": "index.html", "label": "Accueil", "ico": "🏠"},
    {"href": "hebergements.html", "label": "Gites", "ico": "📋"},
    {"href": "tel:0329581422", "label": "Appeler", "ico": "📞"},
    {"href": "contact.html", "label": "Reserver", "ico": "✉"},
]


def _shell_gi(page, title, desc, main):
    return _chrome_classic(
        brand=GI_BRAND, nav=GI_NAV, page=page, cta_label="Reserver", cta_href="contact.html", slug="gites",
        status="Gites · Ouvert toute l'annee", address=GI_ADDRESS, phone=GI_PHONE, email=GI_EMAIL, maps=GI_MAPS,
        foot_links=GI_FOOT, hours="Vosges · Gites", main=main, title=title, desc=desc, head=HEAD_GITES,
        body_class="vt-body vt-body-gites", layout="gites-m3", snack="Demande recue (demo)",
        bottom_items=GI_BN, mobile_label="Reserver",
    )


def build_gites_index():
    main = "<main>"
    main += f"""<section class="vt-hero-bleed vt-hero-hospitality vt-reveal">
  {_img("hero", "Gites Les Lucioles Vosges", eager=True, cls="vt-hero-bleed-img")}
  <div class="vt-hero-bleed-copy">
    <div class="container">
      <p class="vt-eyebrow mb-2">Gites · Vosges</p>
      <h1 class="vt-display display-3 mb-3">Des nuits douces au milieu des sapins</h1>
      <p class="lead mb-4">Trois gites independants a Gerardmer - cheminee, vue foret, petit-dejeuner local.</p>
      <div class="vt-hero-actions">
        <button type="button" class="btn btn-vt-primary btn-lg" data-vt-dialog-open="resaGi">Reserver un sejour</button>
        <a class="btn btn-vt-outline btn-lg" href="hebergements.html">Voir les gites</a>
      </div>
    </div>
  </div>
</section>"""
    main += block_assist_chips([
        {"label": "Clairiere", "href": "hebergements.html", "active": True},
        {"label": "Refuge", "href": "hebergements.html"},
        {"label": "Mezzanine", "href": "hebergements.html"},
        {"label": "Reserver", "href": "contact.html"},
    ])
    main += """<section class="py-5 vt-reveal"><div class="container"><div class="row g-3">
  <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-1", "Gite A") + """<div class="p-3"><h3 class="h6">La Clairiere</h3><p class="small text-secondary mb-0">2-4 pers. · cheminee.</p></div></article></div>
  <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-2", "Gite B") + """<div class="p-3"><h3 class="h6">Le Refuge</h3><p class="small text-secondary mb-0">4-6 pers. · terrasse.</p></div></article></div>
  <div class="col-md-4"><article class="vt-svc-card">""" + _img("card-3", "Gite C") + """<div class="p-3"><h3 class="h6">La Mezzanine</h3><p class="small text-secondary mb-0">2 pers. · vue lac.</p></div></article></div>
</div></div></section>"""
    main += block_journey_m3(
        "Reserver en douceur",
        [
            {"title": "Tu choisis", "text": "Gite, dates - on confirme la dispo.", "emotion": "Envie"},
            {"title": "Accueil", "text": "Cles, plan du coin, une paire d'idees balade.", "emotion": "Bienvenu"},
            {"title": "Sejour", "text": "Cheminee, silence, sapins - a ton rythme.", "emotion": "Repos"},
            {"title": "Depart", "text": "Checkout souple - on peut juste couatcher un the.", "emotion": "Reconnaissant"},
        ],
    )
    main += block_reviews_m3(
        title="Voyageurs des Vosges",
        reviews=[
            {"text": "Weekend en famille - calme, propre, accueil chaleureux.", "name": "Famille Roux", "meta": "Nancy", "stars": 5},
            {"text": "On a meme pu couatcher avec les hotes autour d'un the.", "name": "Amelie", "meta": "Epinal", "stars": 5},
            {"text": "Vue lac depuis la Mezzanine - on revient.", "name": "Liam", "meta": "Strasbourg", "stars": 5},
        ],
    )
    main += block_surface_band_m3(
        '<div class="container py-4">' + _stats_band([
            {"value": "3", "label": "Gites"},
            {"value": "2-6", "label": "Personnes"},
            {"value": "Annee", "label": "Ouverture"},
            {"value": "88400", "label": "Gerardmer"},
        ]) + "</div>",
        tone="soft",
    )
    main += """<section class="vt-cta-sticky py-4"><div class="container d-flex flex-wrap justify-content-between gap-3 align-items-center">
  <p class="mb-0">Dates libres ? Dis voir - on te confirme vite.</p>
  <a class="btn btn-vt-primary" href="contact.html">Reserver</a>
</div></section>"""
    main += block_dialog_m3(dialog_id="resaGi", title="Reserver", lead="On te confirme la disponibilite (demo).", primary_label="Envoyer", primary_href="contact.html", fields_html='<div class="mb-2 vt-m3-field"><label class="form-label small">Gite</label><select class="form-select"><option>La Clairiere</option><option>Le Refuge</option><option>La Mezzanine</option></select></div><div class="mb-2 vt-m3-field"><label class="form-label small">Arrivee</label><input class="form-control" type="date"></div>')
    main += block_fab_menu_m3([{"label": "Reserver", "dialog": "resaGi"}, {"label": "Hebergements", "href": "hebergements.html"}, {"label": "Appeler", "href": "tel:0329581422"}], main_label="Actions gites")
    main += block_sticky_cta_m3("Dates a poser ?", "Reserver", "contact.html", dialog="resaGi")
    main += "</main>"
    return _shell_gi("index.html", f"{GI_BRAND} - Gites Vosges", "Gites a Gerardmer : sejours nature, cheminee, vue foret.", main)


def build_gites_hebergements():
    main = f"""<main>{_progress(1)}<section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Hebergements</p><h1 class="vt-display h2 mb-3">Trois gites, trois ambiances</h1><div class="row g-4"><div class="col-md-4">{_img("scene-1", "Interieur")}</div><div class="col-md-4">{_img("scene-2", "Terrasse")}</div><div class="col-md-4">{_img("scene-3", "Cheminee")}</div></div></div></section></main>"""
    return _shell_gi("hebergements.html", f"Hebergements - {GI_BRAND}", "Hebergements Les Lucioles Vosges.", main)


def build_gites_sejours():
    main = f"""<main>{_progress(2)}<section class="py-5 vt-reveal"><div class="container"><p class="vt-eyebrow">Sejours</p><h1 class="vt-display h2 mb-3">Week-end, semaine, saison</h1><p class="lead text-secondary">Randonnee, ski, lacs - on te file une paire d'idees selon la saison.</p></div></section></main>"""
    return _shell_gi("sejours.html", f"Sejours - {GI_BRAND}", "Idees sejours Les Lucioles Gerardmer.", main)


def build_gites_contact():
    main = f"<main>{_progress(2)}" + _contact_m3(GI_ADDRESS, GI_PHONE, GI_EMAIL, "tel:0329581422", title="Reserver un sejour", lead="Chemin des Sapins - reponse rapide sur les dates.") + "</main>"
    return _shell_gi("contact.html", f"Contact - {GI_BRAND}", "Reserver aux Lucioles Vosges.", main)


BUILDERS_BATCH2 = {
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
    "coiffure": [
        ("index.html", build_coiffure_index),
        ("soins.html", build_coiffure_soins),
        ("equipe.html", build_coiffure_equipe),
        ("contact.html", build_coiffure_contact),
    ],
    "kine": [
        ("index.html", build_kine_index),
        ("soins.html", build_kine_soins),
        ("equipe.html", build_kine_equipe),
        ("contact.html", build_kine_contact),
    ],
    "banque": [
        ("index.html", build_banque_index),
        ("offres.html", build_banque_offres),
        ("entreprises.html", build_banque_entreprises),
        ("contact.html", build_banque_contact),
    ],
    "assurance": [
        ("index.html", build_assurance_index),
        ("particuliers.html", build_assurance_particuliers),
        ("pros.html", build_assurance_pros),
        ("contact.html", build_assurance_contact),
    ],
    "logistique": [
        ("index.html", build_logistique_index),
        ("services.html", build_logistique_services),
        ("zones.html", build_logistique_zones),
        ("contact.html", build_logistique_contact),
    ],
    "promoteur": [
        ("index.html", build_promoteur_index),
        ("programmes.html", build_promoteur_programmes),
        ("accompagnement.html", build_promoteur_accompagnement),
        ("contact.html", build_promoteur_contact),
    ],
    "notaire": [
        ("index.html", build_notaire_index),
        ("domaines.html", build_notaire_domaines),
        ("equipe.html", build_notaire_equipe),
        ("contact.html", build_notaire_contact),
    ],
    "yoga": [
        ("index.html", build_yoga_index),
        ("cours.html", build_yoga_cours),
        ("planning.html", build_yoga_planning),
        ("contact.html", build_yoga_contact),
    ],
    "electricien": [
        ("index.html", build_electricien_index),
        ("services.html", build_electricien_services),
        ("zones.html", build_electricien_zones),
        ("contact.html", build_electricien_contact),
    ],
    "gites": [
        ("index.html", build_gites_index),
        ("hebergements.html", build_gites_hebergements),
        ("sejours.html", build_gites_sejours),
        ("contact.html", build_gites_contact),
    ],
}
