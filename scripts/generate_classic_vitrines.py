#!/usr/bin/env python3
"""Génère des démos vitrine : nav → hero 2 col → stats → 3 offres → confiance → contact."""
from __future__ import annotations

import html as html_lib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEMOS = ROOT / "assets" / "vitrines" / "demos"
JSON_PATH = ROOT / "src" / "data" / "vitrines.json"

SHARED_TAIL = """
  <link rel="stylesheet" href="../shared/vitrine-prose.css">
  <link rel="stylesheet" href="../shared/vitrine-images.css">
  <link rel="stylesheet" href="../shared/vitrine-media.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/glightbox@3.2.0/dist/css/glightbox.min.css" crossorigin="anonymous">
  <link rel="stylesheet" href="styles.css">"""

SHARED_JS = """
  <script src="https://cdn.jsdelivr.net/npm/glightbox@3.2.0/dist/js/glightbox.min.js" crossorigin="anonymous"></script>
  <script src="../shared/vitrine-images.js"></script>"""

CONTENT: dict[str, tuple[str, list[str], str, str]] = {
    "commerce": ("hero.png", ["card-1.png", "card-2.png", "card-3.png"],
                 "Votre marché de quartier, en ligne comme en magasin",
                 "Halles Thionville — primeurs, traiteur et drive en 45 minutes. Click & collect, horaires clairs, fidélité simple."),
    "comptable": ("hero.png", ["card-1.png", "card-2.png", "card-3.png"],
                  "Vos chiffres, expliqués sans jargon",
                  "Verlaine & Associés accompagne les dirigeants de Metz et Thionville : tenue, paie, conseil et bilan flash sous 48 h."),
    "immobilier": ("hero.png", ["card-1.png", "card-2.png", "card-3.png"],
                   "Estimation gratuite, mandat signé sereinement",
                   "Patrimoine Lorraine — vente, location et gestion locative en Moselle. Visites qualifiées et suivi jusqu'à l'acte."),
    "education": ("hero.png", ["card-1.png", "card-2.png", "card-3.png"],
                  "Former aujourd'hui les métiers de demain",
                  "Institut Mercure à Nancy : alternance, certifications reconnues et parcours VAE pour adultes en reconversion."),
    "services": ("hero.png", ["card-1.png", "card-2.png", "card-3.png"],
                 "Des locaux impeccables, des équipes sereines",
                 "Proprio Facility — accueil, propreté et facility management pour sites tertiaires en Lorraine. Devis sous 48 h."),
    "juridique": ("hero.png", ["card-1.png", "card-2.png", "card-3.png"],
                  "Le droit des affaires, en langage clair",
                  "Rivière & Partenaires — sociétés, social et contentieux pour PME messines. Premier échange structuré, forfait découverte."),
    "etablissement": ("hero.png", ["card-1.png", "card-2.png", "card-3.png"],
                      "L'art de recevoir, au cœur de Nancy",
                      "Hôtel Stanislas Collection — chambres 4*, spa, séminaires et room service. Réservation visible dès la page d'accueil."),
    "architecture": ("hero.png", ["card-1.png", "card-2.png", "card-3.png"],
                     "Construire avec mesure et lumière",
                     "Atelier Nord-Est — résidentiel, tertiaire et suivi de chantier à Metz. Portfolio projets et brief en ligne."),
    "automobile": ("hero.png", ["card-1.png", "card-2.png", "card-3.png"],
                   "Entretien, pneus, carrosserie — sans surprise",
                   "Garage Central Plappeville — devis transparent, véhicule de courtoisie, toutes marques. Prise de RDV en deux clics."),
    "fitness": ("hero.png", ["card-1.png", "card-2.png", "card-3.png"],
                "Bougez, progressez, respirez",
                "Pulse Fitness Metz — 1 200 m², 40 cours par semaine, essai gratuit. HIIT, yoga, cycling : choisissez votre rythme."),
    "photographie": ("hero.png", ["card-1.png", "card-2.png", "card-3.png"],
                     "Capturer l'essentiel, livrer l'émotion",
                     "Studio Lumière Grise — mariages, corporate et portraits en Grand Est. Devis personnalisé sous 24 h."),
}

OFFERS: dict[str, list[tuple[str, str]]] = {
    "commerce": [("Primeurs", "Circuit court mosellan."), ("Traiteur", "Plats et plateaux."), ("Drive", "Retrait 45 min.")],
    "comptable": [("Tenue", "Liasse et TVA."), ("Paie", "Bulletins & DSN."), ("Conseil", "Pilotage dirigeant.")],
    "immobilier": [("Vente", "Mandats et visites."), ("Gestion", "Location."), ("Investissement", "Études rendement.")],
    "education": [("Digital", "Certifiant."), ("Management", "Leadership."), ("Technique", "SST & métiers.")],
    "services": [("Maintenance", "Préventif."), ("Accueil", "Standard."), ("Conciergerie", "Sur mesure.")],
    "banque": [("Particuliers", "Comptes."), ("Pros", "Crédit."), ("Agences", "Réseau local.")],
    "juridique": [("Sociétés", "Pactes & AG."), ("Social", "Contrats."), ("Contentieux", "Médiation.")],
    "etablissement": [("Chambres", "4* confort."), ("Spa", "Rituels."), ("Séminaires", "Pro & privé.")],
    "architecture": [("Résidentiel", "Logements."), ("Tertiaire", "Bureaux."), ("MOE", "Suivi.")],
    "automobile": [("Entretien", "Révisions."), ("Pneus", "Montage."), ("Carrosserie", "Peinture.")],
    "fitness": [("HIIT", "Cardio."), ("Yoga", "Zen."), ("Cycling", "Vélo.")],
    "chocolatier": [("Ganaches", "Maison."), ("Tablettes", "Origines."), ("Coffrets", "Entreprise.")],
    "photographie": [("Mariage", "Reportage."), ("Corporate", "Équipes."), ("Portrait", "Studio.")],
}

STATS: dict[str, list[tuple[str, str]]] = {
    "commerce": [("1962", "depuis"), ("4,8", "sur 5"), ("45 min", "drive")],
    "comptable": [("25 ans", "expérience"), ("800+", "clients"), ("48 h", "devis")],
    "immobilier": [("340+", "ventes/an"), ("28 ans", "agence"), ("4,8", "clients")],
    "education": [("1200", "apprenants"), ("35", "parcours"), ("92%", "insertion")],
    "services": [("ISO", "9001"), ("24/7", "astreinte"), ("200+", "sites")],
    "banque": [("12", "agences"), ("1987", "fondée"), ("4,9", "accueil")],
    "juridique": [("1992", "cabinet"), ("6", "associés"), ("Metz", "Barreau")],
    "etablissement": [("87", "chambres"), ("4*", "étoiles"), ("Nancy", "centre")],
    "architecture": [("48", "projets"), ("12", "architectes"), ("MOE", "clé en main")],
    "automobile": [("35 ans", "atelier"), ("2 h", "devis"), ("Toutes", "marques")],
    "fitness": [("1200 m²", "club"), ("40+", "cours/sem."), ("7j/7", "ouvert")],
    "chocolatier": [("1998", "maison"), ("Bean-to-bar", ""), ("Nancy", "centre")],
    "photographie": [("240+", "mariages"), ("15 ans", "studio"), ("GE", "tournée")],
}

THEMES: dict[str, tuple[str, str]] = {
    "commerce": ("#1b5e20", "linear-gradient(135deg,#1b5e20 0%,#43a047 100%)"),
    "comptable": ("#0d47a1", "linear-gradient(135deg,#0d47a1,#1976d2)"),
    "immobilier": ("#1a3c34", "linear-gradient(135deg,rgba(26,60,52,.95),rgba(45,90,78,.9))"),
    "education": ("#1d4ed8", "linear-gradient(135deg,#1e3a5f,#2563eb)"),
    "services": ("#0f766e", "linear-gradient(135deg,#0d4f4f,#14b8a6)"),
    "banque": ("#0c2340", "linear-gradient(135deg,#0c2340,#0077c8)"),
    "juridique": ("#0f172a", "linear-gradient(135deg,#0f172a,#334155)"),
    "etablissement": ("#4e342e", "linear-gradient(135deg,#3e2723,#6d4c41)"),
    "architecture": ("#111", "linear-gradient(135deg,#0a0a0a,#424242)"),
    "automobile": ("#c62828", "linear-gradient(135deg,#1a1a1a,#b71c1c)"),
    "fitness": ("#65a30d", "linear-gradient(135deg,#14532d,#166534)"),
    "chocolatier": ("#5d4037", "linear-gradient(135deg,#3e2723,#8d6e63)"),
    "photographie": ("#37474f", "linear-gradient(135deg,#263238,#546e7a)"),
}

FW: dict[str, str] = {
    "commerce": "bootstrap", "comptable": "bootstrap", "immobilier": "bootstrap",
    "education": "tailwind", "services": "tailwind", "juridique": "tailwind",
    "etablissement": "pico", "architecture": "pico",
    "automobile": "daisy", "fitness": "daisy",
    "photographie": "openprops",
}


def esc(s: str) -> str:
    return html_lib.escape(s, quote=True)


def head_block(fw: str, page_title: str, meta_desc: str) -> str:
    base = (
        f'  <meta charset="utf-8">\n'
        f'  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f'  <meta name="description" content="{esc(meta_desc)}">\n'
        f"  <title>{esc(page_title)}</title>"
    )
    libs = {
        "bootstrap": """
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" crossorigin="anonymous">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" crossorigin="anonymous" referrerpolicy="no-referrer">""",
        "tailwind": """
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" crossorigin="anonymous" referrerpolicy="no-referrer">""",
        "pico": """
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" crossorigin="anonymous" referrerpolicy="no-referrer">""",
        "daisy": """
  <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" crossorigin="anonymous" referrerpolicy="no-referrer">""",
        "openprops": """
  <link rel="stylesheet" href="https://unpkg.com/open-props/normalize.min.css">
  <link rel="stylesheet" href="https://unpkg.com/open-props/open-props.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" crossorigin="anonymous" referrerpolicy="no-referrer">""",
    }
    return base + libs[fw] + SHARED_TAIL


def foot_scripts(fw: str) -> str:
    if fw == "bootstrap":
        return (
            '  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" crossorigin="anonymous"></script>'
            + SHARED_JS
        )
    return SHARED_JS


def hero_figure(hero: str, brand: str, gal: str, img_class: str = "w-100") -> str:
    return f"""<figure class="vitrine-figure vitrine-hero-visual vitrine-figure--ken mb-0">
              <a href="images/{esc(hero)}" class="glightbox" data-gallery="{gal}">
                <img src="images/{esc(hero)}" width="1200" height="520" alt="{esc(brand)}" fetchpriority="high" decoding="async" class="{img_class}">
              </a>
            </figure>"""


def card_bootstrap(tit: str, txt: str, img: str, gal: str) -> str:
    return f"""
          <div class="col-md-4 vitrine-img-reveal">
            <article class="card vt-card h-100 border-0 shadow-sm overflow-hidden">
              <figure class="vitrine-figure vitrine-card-visual mb-0">
                <a href="images/{esc(img)}" class="glightbox" data-gallery="{gal}" data-glightbox="title: {esc(tit)}">
                  <img src="images/{esc(img)}" alt="{esc(tit)}" loading="lazy" decoding="async">
                </a>
              </figure>
              <div class="card-body"><h3 class="h5 vt-brand">{esc(tit)}</h3><p class="text-muted mb-0">{esc(txt)}</p></div>
            </article>
          </div>"""


def card_tailwind(tit: str, txt: str, img: str, gal: str) -> str:
    return f"""
        <article class="bg-white rounded-xl shadow-md overflow-hidden vitrine-img-reveal">
          <figure class="vitrine-figure vitrine-card-visual mb-0">
            <a href="images/{esc(img)}" class="glightbox block" data-gallery="{gal}" data-glightbox="title: {esc(tit)}">
              <img src="images/{esc(img)}" alt="{esc(tit)}" class="w-full h-52 object-cover" loading="lazy" decoding="async">
            </a>
          </figure>
          <div class="p-5"><h3 class="text-lg font-semibold vt-brand">{esc(tit)}</h3><p class="text-slate-600 text-sm mt-1">{esc(txt)}</p></div>
        </article>"""


def card_generic(tit: str, txt: str, img: str, gal: str) -> str:
    return f"""
        <article class="vt-card vitrine-img-reveal">
          <figure class="vitrine-figure vitrine-card-visual mb-0">
            <a href="images/{esc(img)}" class="glightbox" data-gallery="{gal}" data-glightbox="title: {esc(tit)}">
              <img src="images/{esc(img)}" alt="{esc(tit)}" loading="lazy" decoding="async">
            </a>
          </figure>
          <h3 class="vt-brand">{esc(tit)}</h3><p>{esc(txt)}</p>
        </article>"""


def stats_bootstrap(slug: str) -> str:
    return "".join(
        f'<div class="col-md-4"><strong class="vt-stat">{esc(a)}</strong><span>{esc(b)}</span></div>'
        for a, b in STATS[slug]
    )


def stats_tailwind(slug: str) -> str:
    return "".join(
        f'<div><strong class="vt-stat block text-3xl">{esc(a)}</strong><span class="opacity-90">{esc(b)}</span></div>'
        for a, b in STATS[slug]
    )


def stats_generic(slug: str) -> str:
    return "".join(
        f'<div><strong class="vt-stat">{esc(a)}</strong><span>{esc(b)}</span></div>'
        for a, b in STATS[slug]
    )


def body_bootstrap(brand: str, h1: str, lead: str, hero: str, gal: str, cards: str, stats: str) -> str:
    hf = hero_figure(hero, brand, gal)
    return f"""
  <a class="skip-link" href="#contenu">Aller au contenu principal</a>
  <nav class="navbar navbar-expand-lg bg-white border-bottom sticky-top shadow-sm" aria-label="Navigation principale">
    <div class="container-fluid px-4">
      <a class="navbar-brand vt-brand fs-5" href="#accueil">{esc(brand)}</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navMain" aria-label="Menu"><span class="navbar-toggler-icon"></span></button>
      <div class="collapse navbar-collapse" id="navMain">
        <ul class="navbar-nav ms-auto gap-lg-2">
          <li class="nav-item"><a class="nav-link" href="#offres">Offres</a></li>
          <li class="nav-item"><a class="nav-link" href="#engagements">Engagements</a></li>
          <li class="nav-item"><a class="nav-link fw-semibold" href="#contact">Contact</a></li>
        </ul>
      </div>
    </div>
  </nav>
  <main id="contenu" tabindex="-1">
    <section id="accueil" class="vt-hero text-white">
      <div class="container">
        <div class="row align-items-center g-5">
          <div class="col-lg-6 vitrine-img-reveal">
            <p class="vt-eyebrow text-uppercase small mb-2">Grand Est · Lorraine</p>
            <h1 class="mb-3">{esc(h1)}</h1>
            <p class="lead mb-4 opacity-90">{esc(lead)}</p>
            <a class="btn btn-lg vt-btn me-2" href="#offres">Voir nos offres</a>
            <a class="btn btn-lg btn-outline-light" href="#contact">Nous contacter</a>
          </div>
          <div class="col-lg-6">{hf}</div>
        </div>
      </div>
    </section>
    <section class="vt-stats py-4" aria-label="Chiffres clés"><div class="container"><div class="row text-center g-3">{stats}</div></div></section>
    <section id="offres" class="py-5"><div class="container">
      <h2 class="vt-brand display-6 text-center mb-2">Ce que nous proposons</h2>
      <p class="text-center text-muted mb-5 col-lg-8 mx-auto">Services clairs, visuels lisibles, appel à l'action visible.</p>
      <div class="row g-4">{cards}</div>
    </div></section>
    <section id="engagements" class="py-5 vt-muted"><div class="container col-lg-8 text-center">
      <h2 class="vt-brand h3 mb-3">Pourquoi nous faire confiance</h2>
      <p class="text-muted mb-0">Réactivité, transparence et ancrage local — une vitrine qui transforme les visites en demandes.</p>
    </div></section>
    <section id="contact" class="py-5"><div class="container col-lg-7">
      <h2 class="vt-brand text-center mb-4">Contact</h2>
      <form class="row g-3" action="#" method="get" aria-label="Formulaire de contact">
        <div class="col-md-6"><label class="form-label" for="nom">Nom</label><input class="form-control" id="nom" name="nom" type="text" autocomplete="name"></div>
        <div class="col-md-6"><label class="form-label" for="email">E-mail</label><input class="form-control" id="email" name="email" type="email" autocomplete="email"></div>
        <div class="col-12"><label class="form-label" for="msg">Message</label><textarea class="form-control" id="msg" name="message" rows="4"></textarea></div>
        <div class="col-12 text-center"><button class="btn vt-btn btn-lg" type="submit">Envoyer ma demande</button>
        <p class="small text-muted mt-2 mb-0">Démonstration — aucune donnée transmise.</p></div>
      </form>
      <p class="text-center mt-4"><a href="../index.html">← Retour au hub des vitrines</a></p>
    </div></section>
  </main>
  <footer class="vt-footer py-4 text-center"><p class="mb-0 small">Maquette — démonstration DanielCraft</p></footer>"""


def body_tailwind(brand: str, h1: str, lead: str, hero: str, gal: str, cards: str, stats: str) -> str:
    hf = hero_figure(hero, brand, gal, "w-full rounded-xl")
    return f"""
  <a class="skip-link" href="#contenu">Aller au contenu</a>
  <header class="bg-white border-b sticky top-0 z-50 shadow-sm">
    <nav class="max-w-6xl mx-auto px-4 py-3 flex flex-wrap items-center justify-between gap-3" aria-label="Navigation principale">
      <a href="#accueil" class="text-xl font-semibold vt-brand">{esc(brand)}</a>
      <ul class="flex gap-4 text-sm font-medium">
        <li><a href="#offres" class="hover:underline">Offres</a></li>
        <li><a href="#engagements" class="hover:underline">Engagements</a></li>
        <li><a href="#contact" class="font-semibold">Contact</a></li>
      </ul>
    </nav>
  </header>
  <main id="contenu">
    <section id="accueil" class="vt-hero text-white">
      <div class="max-w-6xl mx-auto px-4 py-8 lg:py-10 grid lg:grid-cols-2 gap-8 items-center">
        <div class="vitrine-img-reveal">
          <p class="vt-eyebrow text-xs uppercase tracking-widest mb-2 opacity-90">Grand Est · Lorraine</p>
          <h1 class="text-4xl lg:text-5xl font-bold mb-4 leading-tight">{esc(h1)}</h1>
          <p class="text-lg opacity-90 mb-6">{esc(lead)}</p>
          <div class="flex flex-wrap gap-3">
            <a href="#offres" class="vt-btn inline-block px-6 py-3 rounded-lg font-semibold">Voir nos offres</a>
            <a href="#contact" class="inline-block px-6 py-3 rounded-lg border border-white/80">Nous contacter</a>
          </div>
        </div>
        <div>{hf}</div>
      </div>
    </section>
    <section class="vt-stats py-8" aria-label="Chiffres clés"><div class="max-w-6xl mx-auto px-4 grid md:grid-cols-3 gap-6 text-center">{stats}</div></section>
    <section id="offres" class="py-16 bg-slate-50"><div class="max-w-6xl mx-auto px-4">
      <h2 class="text-3xl font-bold text-center vt-brand mb-2">Ce que nous proposons</h2>
      <p class="text-center text-slate-600 mb-10 max-w-2xl mx-auto">Hiérarchie lisible : comprendre, se projeter, vous contacter.</p>
      <div class="grid md:grid-cols-3 gap-6">{cards}</div>
    </div></section>
    <section id="engagements" class="py-12"><div class="max-w-3xl mx-auto px-4 text-center">
      <h2 class="text-2xl font-bold vt-brand mb-3">Pourquoi nous faire confiance</h2>
      <p class="text-slate-600">Réactivité, transparence et ancrage local.</p>
    </div></section>
    <section id="contact" class="py-16 bg-white"><div class="max-w-xl mx-auto px-4">
      <h2 class="text-2xl font-bold text-center vt-brand mb-6">Contact</h2>
      <form class="grid gap-4" action="#" method="get">
        <label class="block text-sm">Nom <input class="w-full border rounded px-3 py-2 mt-1" name="nom" type="text"></label>
        <label class="block text-sm">E-mail <input class="w-full border rounded px-3 py-2 mt-1" name="email" type="email"></label>
        <label class="block text-sm">Message <textarea class="w-full border rounded px-3 py-2 mt-1" name="message" rows="4"></textarea></label>
        <button class="vt-btn w-full py-3 rounded-lg font-semibold" type="submit">Envoyer ma demande</button>
      </form>
      <p class="text-center mt-6 text-sm"><a href="../index.html" class="underline">← Hub vitrines</a></p>
    </div></section>
  </main>
  <footer class="vt-footer py-6 text-center text-sm">Maquette — DanielCraft</footer>"""


def body_generic(brand: str, h1: str, lead: str, hero: str, gal: str, cards: str, stats: str) -> str:
    hf = hero_figure(hero, brand, gal, "")
    return f"""
  <a class="skip-link" href="#contenu">Aller au contenu</a>
  <header class="vt-top">
    <nav class="vt-nav" aria-label="Navigation principale">
      <a class="vt-brand" href="#accueil">{esc(brand)}</a>
      <a href="#offres">Offres</a><a href="#engagements">Engagements</a><a href="#contact">Contact</a>
    </nav>
  </header>
  <main id="contenu">
    <section id="accueil" class="vt-hero">
      <div class="vt-hero-grid">
        <div>
          <p class="vt-eyebrow">Grand Est · Lorraine</p>
          <h1>{esc(h1)}</h1>
          <p class="vt-lead">{esc(lead)}</p>
          <p><a class="vt-btn" href="#offres">Voir nos offres</a> <a href="#contact">Contact</a></p>
        </div>
        <div>{hf}</div>
      </div>
    </section>
    <section class="vt-stats" aria-label="Chiffres clés"><div class="vt-stats-grid">{stats}</div></section>
    <section id="offres"><div class="vt-wrap">
      <h2>Ce que nous proposons</h2>
      <p class="vt-muted-center">Services clairs et visuels pour convertir.</p>
      <div class="vt-cards">{cards}</div>
    </div></section>
    <section id="engagements" class="vt-band"><div class="vt-wrap vt-center">
      <h2>Pourquoi nous faire confiance</h2>
      <p>Réactivité, transparence et ancrage local.</p>
    </div></section>
    <section id="contact"><div class="vt-wrap vt-form">
      <h2>Contact</h2>
      <form action="#" method="get">
        <label>Nom <input name="nom" type="text"></label>
        <label>E-mail <input name="email" type="email"></label>
        <label>Message <textarea name="message" rows="4"></textarea></label>
        <button class="vt-btn" type="submit">Envoyer ma demande</button>
      </form>
      <p><a href="../index.html">← Hub vitrines</a></p>
    </div></section>
  </main>
  <footer class="vt-footer"><p>Maquette — DanielCraft</p></footer>"""


def write_slug(slug: str, brand: str, page_title: str, meta_desc: str) -> None:
    fw = FW[slug]
    hero, imgs, h1, lead = CONTENT[slug]
    gal = slug + "-vis"
    accent, hero_bg = THEMES[slug]
    offers = OFFERS[slug]

    if fw == "bootstrap":
        cards = "".join(card_bootstrap(t, x, i, gal) for (t, x), i in zip(offers, imgs))
        body = body_bootstrap(brand, h1, lead, hero, gal, cards, stats_bootstrap(slug))
    elif fw == "tailwind":
        cards = "".join(card_tailwind(t, x, i, gal) for (t, x), i in zip(offers, imgs))
        body = body_tailwind(brand, h1, lead, hero, gal, cards, stats_tailwind(slug))
    else:
        cards = "".join(card_generic(t, x, i, gal) for (t, x), i in zip(offers, imgs))
        body = body_generic(brand, h1, lead, hero, gal, cards, stats_generic(slug))

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
{head_block(fw, page_title, meta_desc)}
</head>
<body>
{body}
{foot_scripts(fw)}
</body>
</html>
"""

    css = f"""@import url("../shared/vitrine-prose.css");
html {{ scroll-behavior: smooth; }}
body {{ font-family: var(--vt-font, "Plus Jakarta Sans", system-ui, sans-serif); margin: 0; color: #1a1a1a; font-size: var(--vt-body, 1.0625rem); line-height: var(--vt-lh-body, 1.6); }}
.skip-link {{ position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0); }}
.skip-link:focus {{ position:fixed;left:1rem;top:1rem;z-index:10000;padding:.5rem 1rem;background:#fff;clip:auto;width:auto;height:auto; }}
.vt-brand {{ font-weight: 700; color: {accent}; }}
.vt-hero {{ background: {hero_bg}; color: #fff; padding: clamp(2rem,6vw,4rem) 0; }}
.vt-hero h1 {{ max-width: 16ch; margin: 0 0 1rem; }}
.vt-hero .lead, .vt-lead {{ max-width: min(65ch, 100%); opacity: .95; margin-bottom: 1.5rem; }}
.vt-hero .vitrine-figure--ken img, .vitrine-hero-visual img {{ max-height: 280px; width: 100%; object-fit: cover; border-radius: 0.75rem; }}
.vt-btn {{ background: #fff; color: {accent}; min-height: 44px; padding: 0.75rem 1.5rem; font-weight: 600; border: none; text-decoration: none; display: inline-flex; align-items: center; border-radius: 0.5rem; }}
.vt-stats {{ background: {accent}; color: #fff; padding: 2rem 0; }}
.vt-stat {{ font-size: clamp(1.75rem, 4vw, 2.25rem); display: block; font-weight: 700; }}
.vt-muted, .vt-band {{ background: #f8fafc; }}
.vt-card img {{ width: 100%; height: 220px; object-fit: cover; border-radius: 0.5rem; }}
.vt-footer {{ background: #0f172a; color: rgba(255,255,255,.85); padding: 1.5rem; }}
.vt-top {{ background: #fff; border-bottom: 1px solid #e2e8f0; position: sticky; top: 0; z-index: 40; }}
.vt-nav {{ max-width: 72rem; margin: 0 auto; padding: 1rem; display: flex; flex-wrap: wrap; gap: 1rem; align-items: center; }}
.vt-nav a {{ text-decoration: none; color: inherit; margin-right: .75rem; font-weight: 500; }}
.vt-hero-grid, .vt-stats-grid, .vt-cards {{ max-width: 72rem; margin: 0 auto; padding: 1.25rem 1rem; display: grid; gap: 1.5rem; }}
@media (min-width: 900px) {{
  .vt-hero-grid {{ grid-template-columns: 1fr 1fr; align-items: center; gap: 2.5rem; }}
  .vt-stats-grid {{ grid-template-columns: repeat(3, 1fr); text-align: center; }}
  .vt-cards {{ grid-template-columns: repeat(3, 1fr); }}
}}
.vt-wrap {{ max-width: 72rem; margin: 0 auto; padding: var(--vt-section-y, 3rem) 1rem; }}
.vt-wrap h2 {{ margin-bottom: 0.75rem; }}
.vt-wrap p {{ max-width: min(65ch, 100%); }}
.vt-center {{ text-align: center; }}
.vt-muted-center {{ text-align: center; color: #64748b; margin-bottom: 2rem; max-width: 65ch; margin-inline: auto; }}
.vt-form label {{ display: block; margin-bottom: 1rem; font-weight: 500; }}
.vt-form input, .vt-form textarea {{ width: 100%; padding: 0.65rem; font-size: 1rem; border: 1px solid #cbd5e1; border-radius: 0.375rem; }}
"""

    d = DEMOS / slug
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(html, encoding="utf-8")
    (d / "styles.css").write_text(css, encoding="utf-8")


def main() -> None:
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    for slug in FW:
        it = next(x for x in data["items"] if x["slug"] == slug)
        brand = it["title"]
        h1, lead = CONTENT[slug][2], CONTENT[slug][3]
        page_title = f"{brand} — {it.get('tagline', 'site vitrine')} | démo"
        meta_desc = f"{h1}. {lead}"[:158]
        write_slug(slug, brand, page_title, meta_desc)
        print(f"OK {slug}")


if __name__ == "__main__":
    main()
