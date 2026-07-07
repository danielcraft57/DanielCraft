#!/usr/bin/env python3
"""Génère 8 vitrines métier IA (batch A) via write_ai_site."""
from __future__ import annotations

import html as html_lib
from vitrine_ai_lib import write_ai_site


def esc(s: str) -> str:
    return html_lib.escape(s, quote=True)


def hero_img(alt: str) -> str:
    return f"""<figure class="ai-hero-img">
  <img src="images/hero.png" alt="{esc(alt)}" width="1200" height="520" fetchpriority="high" decoding="async">
</figure>"""


def card_img(n: int, alt: str) -> str:
    return f"""<figure class="ai-card-img">
  <img src="images/card-{n}.png" alt="{esc(alt)}" loading="lazy" decoding="async">
</figure>"""


def stats_row(items: list[tuple[str, str]]) -> str:
    return "".join(
        f'<div class="ai-stat"><strong>{esc(v)}</strong><span>{esc(l)}</span></div>'
        for v, l in items
    )


def contact_form(cta: str = "Envoyer ma demande") -> str:
    return f"""<form class="ai-form" action="#" method="get" aria-label="Formulaire de contact">
  <label>Nom <input name="nom" type="text" autocomplete="name"></label>
  <label>E-mail <input name="email" type="email" autocomplete="email"></label>
  <label>Message <textarea name="message" rows="4"></textarea></label>
  <button class="vt-btn ai-cta" type="submit">{esc(cta)}</button>
  <p class="ai-form-note">Démonstration — aucune donnée transmise.</p>
</form>"""


def body_shell(
    brand: str,
    nav_links: str,
    hero_inner: str,
    stats: str,
    offers: str,
    trust: str,
    contact_title: str,
    contact_cta: str,
    *,
    nav_cta: str = "Contact",
) -> str:
    return f"""<a class="ai-skip" href="#contenu">Aller au contenu</a>
<header class="ai-nav">
  <a class="ai-logo" href="#accueil">{esc(brand)}</a>
  <nav aria-label="Navigation principale">{nav_links}</nav>
  <a class="vt-btn ai-nav-cta" href="#contact">{esc(nav_cta)}</a>
</header>
<main id="contenu">
  <section id="accueil" class="ai-hero">{hero_inner}</section>
  <section class="ai-stats" aria-label="Chiffres clés">{stats}</section>
  <section id="offres" class="ai-offers">
    <div class="ai-wrap">
      <h2>Nos offres</h2>
      <p class="ai-lead">Des services pensés pour le Grand Est, livrés avec exigence.</p>
      <div class="ai-cards">{offers}</div>
    </div>
  </section>
  <section id="confiance" class="ai-trust">{trust}</section>
  <section id="contact" class="ai-contact">
    <div class="ai-wrap ai-contact-inner">
      <h2>{esc(contact_title)}</h2>
      {contact_form(contact_cta)}
    </div>
  </section>
</main>"""


SITES: list[dict] = [
    {
        "slug": "technologie",
        "title": "Synapse Lorraine — Éditeur SaaS B2B",
        "description": "Synapse Lorraine : plateforme SaaS B2B pour PME industrielles en Moselle. Workflows, API et hébergement souverain Grand Est.",
        "layout": "dark-terminal",
        "brand": "Synapse Lorraine",
        "h1": "L'OS métier des équipes qui livrent",
        "lead": "Workflows, API REST et tableaux de bord temps réel — hébergés à Thionville, conformes RGPD, déployés en 48 h.",
        "nav_links": '<a href="#offres">Modules</a><a href="#confiance">Clients</a>',
        "nav_cta": "Demander une démo",
        "stats": [("120+", "clients B2B"), ("99,9 %", "SLA cloud"), ("48 h", "time-to-value")],
        "offers": [
            ("Flow Engine", "Automatisez vos processus métier sans code.", 1),
            ("Data Hub", "Connectez ERP, CRM et BI dans un seul socle.", 2),
            ("Secure API", "Auth OAuth2, webhooks et audit trail natifs.", 3),
        ],
        "trust": """<blockquote class="ai-quote">
  <p>« Synapse a remplacé trois outils disparates. Nos équipes logistique gagnent 6 h par semaine. »</p>
  <footer>— Claire M., directrice ops · PME Moselle-Est</footer>
</blockquote>""",
        "contact_title": "Planifier une démo",
        "contact_cta": "Réserver un créneau",
        "css": """:root{--bg:#0a0e17;--surface:#111827;--accent:#22d3ee;--text:#e2e8f0;--muted:#64748b;--border:#1e293b}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text)}
.ai-skip{position:absolute;left:-9999px}.ai-skip:focus{left:1rem;top:1rem;background:#fff;color:#000;padding:.5rem 1rem;z-index:99}
.ai-nav{display:flex;align-items:center;gap:1.25rem;padding:.85rem 1.5rem;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(10,14,23,.92);backdrop-filter:blur(10px);z-index:50}
.ai-logo{font-weight:800;color:#fff;text-decoration:none;font-size:1.05rem;letter-spacing:-.02em}
.ai-nav nav{display:flex;gap:1.25rem;flex:1}.ai-nav a{color:var(--muted);text-decoration:none;font-weight:500;font-size:.95rem}
.ai-nav-cta{background:var(--accent)!important;color:#0a0e17!important;font-size:.9rem;padding:.55rem 1.1rem!important}
.ai-hero{padding:clamp(2.5rem,6vw,4.5rem) 1.5rem;background:radial-gradient(ellipse at 20% 0%,#164e63 0%,transparent 50%),var(--bg)}
.ai-hero-grid{max-width:72rem;margin:0 auto;display:grid;gap:2.5rem;align-items:center}
@media(min-width:900px){.ai-hero-grid{grid-template-columns:1fr 1fr}}
.ai-hero .vt-eyebrow{color:var(--accent);margin:0 0 .75rem}
.ai-hero h1{color:#fff;margin:0 0 1rem;font-size:clamp(2rem,4.5vw,2.75rem)}
.ai-hero .ai-lead{color:var(--muted);margin:0 0 1.5rem;max-width:55ch}
.ai-hero-actions{display:flex;flex-wrap:wrap;gap:.75rem}
.ai-hero-actions .vt-btn{background:var(--accent);color:#0a0e17;border:none}
.ai-hero-actions .ai-ghost{color:var(--text);text-decoration:none;display:inline-flex;align-items:center;min-height:44px;padding:0 1rem;border:1px solid var(--border);border-radius:.5rem}
.ai-hero-img{margin:0;border-radius:12px;overflow:hidden;border:1px solid var(--border);box-shadow:0 0 40px rgba(34,211,238,.12)}
.ai-hero-img img{width:100%;display:block;object-fit:cover;max-height:340px}
.ai-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;padding:1.5rem;background:var(--surface);border-block:1px solid var(--border);max-width:72rem;margin:0 auto}
.ai-stat{text-align:center;padding:.5rem}.ai-stat strong{display:block;font-size:clamp(1.5rem,3vw,2rem);color:var(--accent)}.ai-stat span{font-size:.85rem;color:var(--muted)}
.ai-wrap{max-width:72rem;margin:0 auto;padding:var(--vt-section-y,3rem) 1.5rem}
.ai-offers h2,.ai-contact h2{text-align:center;margin:0 0 .5rem;color:#fff}
.ai-offers .ai-lead{text-align:center;color:var(--muted);margin:0 auto 2rem;max-width:50ch}
.ai-cards{display:grid;gap:1.25rem}@media(min-width:768px){.ai-cards{grid-template-columns:repeat(3,1fr)}}
.ai-card{background:var(--surface);border:1px solid var(--border);border-radius:12px;overflow:hidden}
.ai-card-img{margin:0}.ai-card-img img{width:100%;height:180px;object-fit:cover;display:block}
.ai-card h3{margin:1rem 1rem .35rem;font-size:1.05rem;color:#fff}.ai-card p{margin:0 1rem 1.25rem;font-size:.92rem;color:var(--muted)}
.ai-trust{padding:3rem 1.5rem;background:linear-gradient(135deg,#0f172a,#111827)}
.ai-quote{max-width:42rem;margin:0 auto;text-align:center;border-left:none;padding:0}
.ai-quote p{font-size:1.125rem;font-style:italic;color:#cbd5e1;margin:0 0 1rem}
.ai-quote footer{color:var(--muted);font-size:.9rem}
.ai-contact{background:var(--surface)}.ai-contact-inner{max-width:32rem}
.ai-form{display:grid;gap:1rem}.ai-form label{display:grid;gap:.35rem;font-weight:500;font-size:.9rem;color:var(--muted)}
.ai-form input,.ai-form textarea{background:#0a0e17;border:1px solid var(--border);border-radius:8px;padding:.65rem .85rem;color:var(--text);font:inherit}
.ai-cta{width:100%;background:var(--accent)!important;color:#0a0e17!important;border:none}
.ai-form-note{text-align:center;font-size:.8rem;color:var(--muted);margin:0}
.ai-foot{padding:1.5rem;text-align:center;border-top:1px solid var(--border);color:var(--muted);font-size:.85rem}
""",
    },
    {
        "slug": "restauration",
        "title": "Brasserie Saint-Jacques — Restaurant Lorraine",
        "description": "Brasserie Saint-Jacques à Metz : cuisine de saison, carte du jour et réservation en ligne. Ambiance chaleureuse au cœur de la Lorraine.",
        "layout": "brasserie-chaleur",
        "brand": "Brasserie Saint-Jacques",
        "h1": "La convivialité lorraine, assiette après assiette",
        "lead": "Produits locaux, carte de saison et salle voûtée du XVIIIᵉ — réservez votre table en deux clics, Metz centre.",
        "nav_links": '<a href="#offres">Carte</a><a href="#confiance">Avis</a>',
        "nav_cta": "Réserver",
        "stats": [("1987", "depuis"), ("4,8/5", "Google"), ("85", "couverts")],
        "offers": [
            ("Brunch du dimanche", "Œufs Bénédicte, viennoiseries maison et jus pressés.", 1),
            ("Carte du soir", "Entrecôte Moselle, truite du canal et gratin dauphinois.", 2),
            ("Privatisation", "Repas de groupe, anniversaires et séminaires gourmands.", 3),
        ],
        "trust": """<div class="ai-trust-grid">
  <p class="ai-trust-lead">« Une adresse incontournable — service attentionné et produits du terroir. »</p>
  <div class="ai-badges">
    <span>Maître Restaurateur</span><span>Produits du terroir</span><span>Metz centre</span>
  </div>
</div>""",
        "contact_title": "Réserver une table",
        "contact_cta": "Confirmer ma réservation",
        "css": """:root{--cream:#faf6f0;--brown:#3d2914;--gold:#b8860b;--rust:#8b4513;--warm:#d4a574}
body{margin:0;background:var(--cream);color:var(--brown)}
.ai-skip{position:absolute;left:-9999px}.ai-skip:focus{left:1rem;top:1rem;background:#fff;padding:.5rem;z-index:99}
.ai-nav{display:flex;align-items:center;gap:1rem;padding:1rem 1.5rem;background:#fff;border-bottom:2px solid var(--warm);position:sticky;top:0;z-index:50;box-shadow:0 2px 12px rgba(61,41,20,.08)}
.ai-logo{font-family:Georgia,serif;font-weight:700;font-size:1.2rem;color:var(--rust);text-decoration:none}
.ai-nav nav{display:flex;gap:1.25rem;flex:1}.ai-nav a{color:var(--brown);text-decoration:none;font-weight:500}
.ai-nav-cta{background:var(--rust)!important;color:#fff!important}
.ai-hero{padding:0;background:linear-gradient(180deg,#fff 0%,var(--cream) 100%)}
.ai-hero-split{max-width:72rem;margin:0 auto;display:grid}@media(min-width:900px){.ai-hero-split{grid-template-columns:1.1fr .9fr}}
.ai-hero-text{padding:clamp(2rem,5vw,3.5rem) 1.5rem}
.ai-hero .vt-eyebrow{color:var(--gold);margin:0 0 .5rem}
.ai-hero h1{font-family:Georgia,serif;color:var(--rust);margin:0 0 1rem;line-height:1.15}
.ai-hero .ai-lead{margin:0 0 1.5rem;max-width:50ch}
.ai-hero-actions .vt-btn{background:var(--rust);color:#fff;border:none}
.ai-hero-actions .ai-ghost{color:var(--brown);text-decoration:underline;margin-left:1rem;display:inline-flex;align-items:center;min-height:44px}
.ai-hero-img{margin:0;overflow:hidden}.ai-hero-img img{width:100%;height:100%;min-height:320px;object-fit:cover;display:block}
.ai-stats{display:flex;justify-content:center;gap:3rem;padding:1.75rem 1.5rem;background:var(--rust);color:#fff;flex-wrap:wrap}
.ai-stat{text-align:center}.ai-stat strong{display:block;font-family:Georgia,serif;font-size:1.75rem}.ai-stat span{font-size:.85rem;opacity:.85}
.ai-wrap{max-width:72rem;margin:0 auto;padding:var(--vt-section-y,3rem) 1.5rem}
.ai-offers h2,.ai-contact h2{font-family:Georgia,serif;text-align:center;color:var(--rust);margin:0 0 .5rem}
.ai-offers .ai-lead{text-align:center;margin:0 auto 2rem;color:#6b5344;max-width:50ch}
.ai-cards{display:grid;gap:1.5rem}@media(min-width:768px){.ai-cards{grid-template-columns:repeat(3,1fr)}}
.ai-card{background:#fff;border-radius:16px;overflow:hidden;box-shadow:0 4px 20px rgba(61,41,20,.1)}
.ai-card-img{margin:0}.ai-card-img img{width:100%;height:200px;object-fit:cover}
.ai-card h3{font-family:Georgia,serif;margin:1rem 1rem .35rem;color:var(--rust)}.ai-card p{margin:0 1rem 1.25rem;font-size:.95rem;color:#6b5344}
.ai-trust{padding:2.5rem 1.5rem;background:#fff;text-align:center}
.ai-trust-lead{font-family:Georgia,serif;font-size:1.2rem;font-style:italic;color:var(--brown);max-width:40rem;margin:0 auto 1.25rem}
.ai-badges{display:flex;flex-wrap:wrap;justify-content:center;gap:.75rem}
.ai-badges span{background:var(--cream);border:1px solid var(--warm);padding:.4rem 1rem;border-radius:99px;font-size:.85rem;font-weight:600;color:var(--rust)}
.ai-contact{background:var(--cream)}.ai-contact-inner{max-width:28rem}
.ai-form{display:grid;gap:1rem}.ai-form label{display:grid;gap:.3rem;font-weight:600;font-size:.9rem}
.ai-form input,.ai-form textarea{border:1px solid var(--warm);border-radius:8px;padding:.65rem;font:inherit;background:#fff}
.ai-cta{width:100%;background:var(--rust)!important;color:#fff!important}
.ai-form-note{text-align:center;font-size:.8rem;color:#6b5344;margin:0}
.ai-foot{padding:1.5rem;text-align:center;background:var(--brown);color:rgba(255,255,255,.8);font-size:.85rem}
.ai-foot a{color:#fff}
""",
    },
    {
        "slug": "beaute",
        "title": "Spa Thalie — Institut spa élégant",
        "description": "Spa Thalie à Nancy : soins visage, massages et rituels bien-être dans un cadre rose nude. Réservation en ligne, équipe certifiée.",
        "layout": "spa-rose-nude",
        "brand": "Spa Thalie",
        "h1": "Le rituel beauté qui vous ressemble",
        "lead": "Soins sur mesure, ambiance feutrée et produits clean — votre parenthèse bien-être au cœur de Nancy, Grand Est.",
        "nav_links": '<a href="#offres">Soins</a><a href="#confiance">Témoignages</a>',
        "nav_cta": "Prendre RDV",
        "stats": [("12 ans", "d'expertise"), ("4,9/5", "avis clients"), ("18", "rituels")],
        "offers": [
            ("Soin éclat visage", "Gommage doux, massage Kobido et masque hydratant 75 min.", 1),
            ("Massage pierres chaudes", "Détente profonde aux huiles essentielles bio.", 2),
            ("Forfait mariée", "Préparation peau, manucure et coiffure partenaires.", 3),
        ],
        "trust": """<blockquote class="ai-quote">
  <p>« Un havre de paix — l'équipe est d'une douceur rare, je ressors transformée à chaque visite. »</p>
  <footer>Sophie L. · cliente fidèle depuis 2019</footer>
</blockquote>""",
        "contact_title": "Réserver votre soin",
        "contact_cta": "Demander un créneau",
        "css": """:root{--rose:#e8c4c4;--nude:#f5ebe0;--blush:#c9a0a0;--text:#4a3728;--soft:#fdf8f5}
body{margin:0;background:var(--soft);color:var(--text)}
.ai-skip{position:absolute;left:-9999px}.ai-skip:focus{left:1rem;top:1rem;background:#fff;padding:.5rem;z-index:99}
.ai-nav{display:flex;align-items:center;gap:1rem;padding:1rem 2rem;background:rgba(253,248,245,.95);backdrop-filter:blur(8px);position:sticky;top:0;z-index:50;border-bottom:1px solid var(--rose)}
.ai-logo{font-weight:300;font-size:1.35rem;letter-spacing:.15em;text-transform:uppercase;color:var(--blush);text-decoration:none}
.ai-nav nav{display:flex;gap:1.5rem;flex:1}.ai-nav a{color:var(--text);text-decoration:none;font-weight:400;letter-spacing:.03em}
.ai-nav-cta{background:var(--blush)!important;color:#fff!important;border-radius:99px!important}
.ai-hero{padding:clamp(2rem,5vw,4rem) 1.5rem;text-align:center;background:linear-gradient(180deg,var(--nude),var(--soft))}
.ai-hero-center{max-width:52rem;margin:0 auto}
.ai-hero .vt-eyebrow{color:var(--blush);margin:0 0 .75rem}
.ai-hero h1{font-weight:300;letter-spacing:-.01em;color:var(--text);margin:0 0 1rem}
.ai-hero .ai-lead{margin:0 auto 1.5rem;max-width:48ch}
.ai-hero-actions{margin-bottom:2rem}.ai-hero-actions .vt-btn{background:var(--blush);color:#fff;border:none;border-radius:99px}
.ai-hero-img{margin:0 auto;max-width:640px;border-radius:50% 50% 12px 12px;overflow:hidden;box-shadow:0 20px 60px rgba(201,160,160,.25)}
.ai-hero-img img{width:100%;display:block;object-fit:cover;max-height:380px}
.ai-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;padding:2rem 1.5rem;background:var(--nude);max-width:48rem;margin:0 auto;border-radius:24px}
.ai-stat{text-align:center}.ai-stat strong{display:block;font-size:1.5rem;font-weight:300;color:var(--blush)}.ai-stat span{font-size:.8rem;letter-spacing:.05em;text-transform:uppercase}
.ai-wrap{max-width:68rem;margin:0 auto;padding:var(--vt-section-y,3rem) 1.5rem}
.ai-offers h2,.ai-contact h2{text-align:center;font-weight:300;letter-spacing:.08em;text-transform:uppercase;color:var(--blush);margin:0 0 .5rem}
.ai-offers .ai-lead{text-align:center;margin:0 auto 2.5rem;max-width:45ch;color:#7a6a5a}
.ai-cards{display:grid;gap:2rem}@media(min-width:768px){.ai-cards{grid-template-columns:repeat(3,1fr)}}
.ai-card{text-align:center;background:#fff;border-radius:20px;padding:0 0 1.5rem;box-shadow:0 8px 30px rgba(201,160,160,.12)}
.ai-card-img{margin:0;border-radius:20px 20px 0 0;overflow:hidden}.ai-card-img img{width:100%;height:200px;object-fit:cover}
.ai-card h3{font-weight:400;margin:1.25rem 1rem .5rem;color:var(--text)}.ai-card p{margin:0 1rem;font-size:.92rem;color:#7a6a5a}
.ai-trust{padding:3rem 1.5rem;text-align:center;background:var(--nude)}
.ai-quote{max-width:36rem;margin:0 auto;border:none;padding:0}
.ai-quote p{font-style:italic;font-size:1.1rem;line-height:1.7;margin:0 0 1rem;color:var(--text)}
.ai-quote footer{color:var(--blush);font-size:.9rem;letter-spacing:.03em}
.ai-contact{background:var(--soft)}.ai-contact-inner{max-width:26rem}
.ai-form{display:grid;gap:1rem}.ai-form label{display:grid;gap:.3rem;font-size:.85rem;letter-spacing:.04em;text-transform:uppercase;color:var(--blush)}
.ai-form input,.ai-form textarea{border:1px solid var(--rose);border-radius:12px;padding:.75rem;font:inherit;background:#fff}
.ai-cta{width:100%;background:var(--blush)!important;color:#fff!important;border-radius:99px!important}
.ai-form-note{text-align:center;font-size:.8rem;color:#7a6a5a;margin:0}
.ai-foot{padding:1.5rem;text-align:center;background:var(--nude);color:var(--text);font-size:.85rem}
""",
    },
    {
        "slug": "odontologie",
        "title": "Centre dentaire Mosaïque — Metz",
        "description": "Centre dentaire Mosaïque à Metz : soins préventifs, orthodontie et implantologie. Équipe rassurante, devis transparent, urgences.",
        "layout": "dental-blue-health",
        "brand": "Centre dentaire Mosaïque",
        "h1": "Votre sourire, pris en charge sereinement",
        "lead": "Implantologie, orthodontie invisible et soins préventifs — cabinet moderne à Metz, équipe à l'écoute, devis clair avant tout acte.",
        "nav_links": '<a href="#offres">Soins</a><a href="#confiance">Engagements</a>',
        "nav_cta": "Prendre RDV",
        "stats": [("15 ans", "d'expérience"), ("6", "praticiens"), ("4,9/5", "satisfaction")],
        "offers": [
            ("Prévention", "Détartrage, bilan annuel et conseils d'hygiène personnalisés.", 1),
            ("Orthodontie", "Aligneurs transparents et suivi numérique 3D.", 2),
            ("Implants", "Pose guidée, devis détaillé et garantie écrite.", 3),
        ],
        "trust": """<div class="ai-trust-grid">
  <h3>Nos engagements santé</h3>
  <ul class="ai-checklist">
    <li>Devis signé avant tout soin</li>
    <li>Matériel stérilisé certifié</li>
    <li>Urgences dentaires sous 24 h</li>
    <li>Tiers payant mutuelle accepté</li>
  </ul>
</div>""",
        "contact_title": "Demander un rendez-vous",
        "contact_cta": "Envoyer ma demande",
        "css": """:root{--blue:#0284c7;--light:#e0f2fe;--sky:#f0f9ff;--text:#0c4a6e;--white:#fff}
body{margin:0;background:var(--sky);color:var(--text)}
.ai-skip{position:absolute;left:-9999px}.ai-skip:focus{left:1rem;top:1rem;background:#fff;padding:.5rem;z-index:99}
.ai-nav{display:flex;align-items:center;gap:1rem;padding:.85rem 1.5rem;background:var(--white);position:sticky;top:0;z-index:50;box-shadow:0 1px 8px rgba(2,132,199,.1)}
.ai-logo{font-weight:700;color:var(--blue);text-decoration:none;font-size:1rem}
.ai-nav nav{display:flex;gap:1.25rem;flex:1}.ai-nav a{color:var(--text);text-decoration:none;font-weight:500}
.ai-nav-cta{background:var(--blue)!important;color:#fff!important}
.ai-hero{padding:clamp(2rem,5vw,3.5rem) 1.5rem;background:linear-gradient(135deg,var(--blue),#0369a1);color:#fff}
.ai-hero-grid{max-width:72rem;margin:0 auto;display:grid;gap:2rem;align-items:center}@media(min-width:900px){.ai-hero-grid{grid-template-columns:1fr 1fr}}
.ai-hero .vt-eyebrow{opacity:.9;margin:0 0 .5rem}
.ai-hero h1{color:#fff;margin:0 0 1rem}
.ai-hero .ai-lead{opacity:.92;margin:0 0 1.5rem;max-width:52ch}
.ai-hero-actions .vt-btn{background:#fff;color:var(--blue);border:none}
.ai-hero-actions .ai-ghost{color:#fff;text-decoration:none;display:inline-flex;align-items:center;min-height:44px;margin-left:.75rem;padding:0 1rem;border:1px solid rgba(255,255,255,.5);border-radius:.5rem}
.ai-hero-img{margin:0;border-radius:16px;overflow:hidden;box-shadow:0 12px 40px rgba(0,0,0,.2)}.ai-hero-img img{width:100%;display:block;object-fit:cover;max-height:320px}
.ai-stats{display:grid;grid-template-columns:repeat(3,1fr);background:var(--white);padding:1.5rem;max-width:72rem;margin:-1rem auto 0;border-radius:12px;box-shadow:0 4px 20px rgba(2,132,199,.12);position:relative;z-index:2}
.ai-stat{text-align:center;padding:.5rem}.ai-stat strong{display:block;font-size:1.6rem;color:var(--blue)}.ai-stat span{font-size:.85rem;color:#64748b}
.ai-wrap{max-width:72rem;margin:0 auto;padding:var(--vt-section-y,3rem) 1.5rem}
.ai-offers h2,.ai-contact h2{text-align:center;color:var(--blue);margin:0 0 .5rem}
.ai-offers .ai-lead{text-align:center;margin:0 auto 2rem;color:#64748b;max-width:50ch}
.ai-cards{display:grid;gap:1.25rem}@media(min-width:768px){.ai-cards{grid-template-columns:repeat(3,1fr)}}
.ai-card{background:var(--white);border-radius:12px;overflow:hidden;border:1px solid var(--light);transition:box-shadow .2s}
.ai-card:hover{box-shadow:0 8px 24px rgba(2,132,199,.12)}
.ai-card-img{margin:0}.ai-card-img img{width:100%;height:180px;object-fit:cover}
.ai-card h3{margin:1rem 1rem .35rem;color:var(--blue)}.ai-card p{margin:0 1rem 1.25rem;font-size:.92rem;color:#64748b}
.ai-trust{padding:2.5rem 1.5rem;background:var(--light);text-align:center}
.ai-trust-grid h3{color:var(--blue);margin:0 0 1rem}
.ai-checklist{list-style:none;padding:0;margin:0 auto;max-width:24rem;text-align:left}
.ai-checklist li{padding:.5rem 0 .5rem 1.75rem;position:relative;font-weight:500}
.ai-checklist li::before{content:"✓";position:absolute;left:0;color:var(--blue);font-weight:700}
.ai-contact{background:var(--white)}.ai-contact-inner{max-width:28rem}
.ai-form{display:grid;gap:1rem}.ai-form label{display:grid;gap:.3rem;font-weight:600;font-size:.9rem;color:var(--text)}
.ai-form input,.ai-form textarea{border:1px solid var(--light);border-radius:8px;padding:.65rem;font:inherit;background:var(--sky)}
.ai-cta{width:100%;background:var(--blue)!important;color:#fff!important}
.ai-form-note{text-align:center;font-size:.8rem;color:#64748b;margin:0}
.ai-foot{padding:1.5rem;text-align:center;background:var(--blue);color:rgba(255,255,255,.9);font-size:.85rem}
.ai-foot a{color:#fff}
""",
    },
    {
        "slug": "industrie",
        "title": "Précisite Usinage — Usinage industriel Moselle",
        "description": "Précisite Usinage à Thionville : fraisage CNC, tournage de précision et prototypage rapide pour l'industrie lorraine.",
        "layout": "industrial-amber-steel",
        "brand": "Précisite Usinage",
        "h1": "La précision au micron, livrée à l'heure",
        "lead": "Fraisage 5 axes, tournage CNC et contrôle tridimensionnel — atelier certifié ISO 9001, Moselle-Est, délais tenus.",
        "nav_links": '<a href="#offres">Capacités</a><a href="#confiance">Certifications</a>',
        "nav_cta": "Demander un devis",
        "stats": [("±5 µm", "tolérance"), ("ISO", "9001"), ("72 h", "devis")],
        "offers": [
            ("Fraisage 5 axes", "Pièces complexes aluminium, acier et titane.", 1),
            ("Tournage CNC", "Séries moyennes et grandes, barres jusqu'à Ø 400 mm.", 2),
            ("Prototypage rapide", "Du plan au premier échantillon en 5 jours ouvrés.", 3),
        ],
        "trust": """<div class="ai-trust-grid">
  <p>« Délais respectés, qualité constante — notre sous-traitant de confiance depuis 2018. »</p>
  <div class="ai-badges"><span>ISO 9001</span><span>Matériaux certifiés</span><span>Moselle-Est</span></div>
</div>""",
        "contact_title": "Demander un devis",
        "contact_cta": "Envoyer mon cahier des charges",
        "css": """:root{--steel:#1c1c1e;--amber:#f59e0b;--dark:#0f0f10;--gray:#71717a;--panel:#27272a}
body{margin:0;background:var(--dark);color:#e4e4e7}
.ai-skip{position:absolute;left:-9999px}.ai-skip:focus{left:1rem;top:1rem;background:#fff;color:#000;padding:.5rem;z-index:99}
.ai-nav{display:flex;align-items:center;gap:1rem;padding:.85rem 1.5rem;background:var(--steel);border-bottom:3px solid var(--amber);position:sticky;top:0;z-index:50}
.ai-logo{font-weight:800;text-transform:uppercase;letter-spacing:.06em;color:var(--amber);text-decoration:none;font-size:.95rem}
.ai-nav nav{display:flex;gap:1.25rem;flex:1}.ai-nav a{color:#a1a1aa;text-decoration:none;font-weight:500;font-size:.9rem;text-transform:uppercase;letter-spacing:.04em}
.ai-nav-cta{background:var(--amber)!important;color:var(--dark)!important;font-weight:700!important;text-transform:uppercase;letter-spacing:.03em}
.ai-hero{padding:clamp(2rem,5vw,4rem) 1.5rem;background:repeating-linear-gradient(-45deg,transparent,transparent 4px,rgba(245,158,11,.03) 4px,rgba(245,158,11,.03) 8px),var(--dark)}
.ai-hero-grid{max-width:72rem;margin:0 auto;display:grid;gap:2rem;align-items:center}@media(min-width:900px){.ai-hero-grid{grid-template-columns:.95fr 1.05fr}}
.ai-hero .vt-eyebrow{color:var(--amber);margin:0 0 .5rem}
.ai-hero h1{color:#fff;margin:0 0 1rem;text-transform:uppercase;letter-spacing:-.02em;font-size:clamp(1.75rem,4vw,2.5rem)}
.ai-hero .ai-lead{color:var(--gray);margin:0 0 1.5rem;max-width:52ch}
.ai-hero-actions .vt-btn{background:var(--amber);color:var(--dark);border:none;font-weight:700;text-transform:uppercase;letter-spacing:.03em}
.ai-hero-actions .ai-ghost{color:var(--amber);text-decoration:none;display:inline-flex;align-items:center;min-height:44px;margin-left:.75rem;font-weight:600}
.ai-hero-img{margin:0;border:2px solid var(--amber);overflow:hidden}.ai-hero-img img{width:100%;display:block;object-fit:cover;max-height:360px;filter:contrast(1.05)}
.ai-stats{display:grid;grid-template-columns:repeat(3,1fr);border-top:3px solid var(--amber);border-bottom:3px solid var(--amber);background:var(--steel);padding:1.25rem 1.5rem;max-width:72rem;margin:0 auto}
.ai-stat{text-align:center}.ai-stat strong{display:block;font-size:1.75rem;color:var(--amber);font-weight:800}.ai-stat span{font-size:.8rem;color:var(--gray);text-transform:uppercase;letter-spacing:.06em}
.ai-wrap{max-width:72rem;margin:0 auto;padding:var(--vt-section-y,3rem) 1.5rem}
.ai-offers h2,.ai-contact h2{text-align:center;color:var(--amber);margin:0 0 .5rem;text-transform:uppercase;letter-spacing:.06em}
.ai-offers .ai-lead{text-align:center;color:var(--gray);margin:0 auto 2rem;max-width:50ch}
.ai-cards{display:grid;gap:1.25rem}@media(min-width:768px){.ai-cards{grid-template-columns:repeat(3,1fr)}}
.ai-card{background:var(--panel);border-left:4px solid var(--amber);overflow:hidden}
.ai-card-img{margin:0}.ai-card-img img{width:100%;height:180px;object-fit:cover;opacity:.9}
.ai-card h3{margin:1rem 1rem .35rem;color:#fff;text-transform:uppercase;font-size:.95rem;letter-spacing:.04em}.ai-card p{margin:0 1rem 1.25rem;font-size:.9rem;color:var(--gray)}
.ai-trust{padding:2.5rem 1.5rem;text-align:center;background:var(--steel)}
.ai-trust-grid p{font-size:1.05rem;font-style:italic;color:#d4d4d8;max-width:40rem;margin:0 auto 1.25rem}
.ai-badges{display:flex;flex-wrap:wrap;justify-content:center;gap:.75rem}
.ai-badges span{border:1px solid var(--amber);color:var(--amber);padding:.35rem .9rem;font-size:.8rem;font-weight:700;text-transform:uppercase;letter-spacing:.05em}
.ai-contact{background:var(--panel)}.ai-contact-inner{max-width:30rem}
.ai-form{display:grid;gap:1rem}.ai-form label{display:grid;gap:.3rem;font-weight:600;font-size:.85rem;color:var(--gray);text-transform:uppercase;letter-spacing:.04em}
.ai-form input,.ai-form textarea{background:var(--dark);border:1px solid #3f3f46;border-radius:0;padding:.65rem;color:#fff;font:inherit}
.ai-cta{width:100%;background:var(--amber)!important;color:var(--dark)!important;border-radius:0!important;font-weight:700!important;text-transform:uppercase}
.ai-form-note{text-align:center;font-size:.8rem;color:var(--gray);margin:0}
.ai-foot{padding:1.5rem;text-align:center;border-top:3px solid var(--amber);color:var(--gray);font-size:.85rem}
""",
    },
    {
        "slug": "association",
        "title": "Solidarités Metz Métropole — ESS",
        "description": "Solidarités Metz Métropole : insertion, aide alimentaire et accompagnement social en Économie Sociale et Solidaire, Moselle.",
        "layout": "ess-green-solidarity",
        "brand": "Solidarités Metz Métropole",
        "h1": "Agir ensemble pour un territoire plus juste",
        "lead": "Insertion professionnelle, aide alimentaire et accompagnement social — une ESS ancrée à Metz, portée par 120 bénévoles et 45 salariés.",
        "nav_links": '<a href="#offres">Actions</a><a href="#confiance">Impact</a>',
        "nav_cta": "Faire un don",
        "stats": [("120", "bénévoles"), ("3 200", "familles aidées"), ("45", "salariés")],
        "offers": [
            ("Aide alimentaire", "Épicerie solidaire et paniers hebdomadaires à prix modiques.", 1),
            ("Insertion emploi", "Ateliers CV, stages et mise en relation avec les employeurs locaux.", 2),
            ("Accompagnement social", "Permanences juridiques, logement et accès aux droits.", 3),
        ],
        "trust": """<blockquote class="ai-quote">
  <p>« Grâce au parcours insertion, j'ai retrouvé un CDI en trois mois. Une équipe humaine et exigeante. »</p>
  <footer>Marc D. · bénéficiaire 2025 · Metz</footer>
</blockquote>""",
        "contact_title": "Devenir bénévole ou donateur",
        "contact_cta": "Je m'engage",
        "css": """:root{--green:#15803d;--leaf:#22c55e;--mint:#dcfce7;--forest:#14532d;--text:#1a2e1a}
body{margin:0;background:#f7fdf8;color:var(--text)}
.ai-skip{position:absolute;left:-9999px}.ai-skip:focus{left:1rem;top:1rem;background:#fff;padding:.5rem;z-index:99}
.ai-nav{display:flex;align-items:center;gap:1rem;padding:1rem 1.5rem;background:#fff;border-bottom:3px solid var(--leaf);position:sticky;top:0;z-index:50}
.ai-logo{font-weight:700;color:var(--forest);text-decoration:none;font-size:.95rem;line-height:1.3;max-width:14rem}
.ai-nav nav{display:flex;gap:1.25rem;flex:1}.ai-nav a{color:var(--text);text-decoration:none;font-weight:500}
.ai-nav-cta{background:var(--green)!important;color:#fff!important}
.ai-hero{padding:clamp(2rem,5vw,3.5rem) 1.5rem;background:linear-gradient(160deg,var(--forest) 0%,var(--green) 100%);color:#fff;position:relative;overflow:hidden}
.ai-hero::after{content:"";position:absolute;right:-10%;bottom:-20%;width:50%;height:80%;background:radial-gradient(circle,rgba(34,197,94,.2),transparent 70%);pointer-events:none}
.ai-hero-grid{max-width:72rem;margin:0 auto;display:grid;gap:2rem;align-items:center;position:relative;z-index:1}@media(min-width:900px){.ai-hero-grid{grid-template-columns:1fr 1fr}}
.ai-hero .vt-eyebrow{opacity:.9;margin:0 0 .5rem}
.ai-hero h1{color:#fff;margin:0 0 1rem}
.ai-hero .ai-lead{opacity:.92;margin:0 0 1.5rem;max-width:52ch}
.ai-hero-actions .vt-btn{background:var(--leaf);color:var(--forest);border:none;font-weight:700}
.ai-hero-actions .ai-ghost{color:#fff;text-decoration:none;display:inline-flex;align-items:center;min-height:44px;margin-left:.75rem;padding:0 1rem;border:2px solid rgba(255,255,255,.6);border-radius:.5rem;font-weight:600}
.ai-hero-img{margin:0;border-radius:16px;overflow:hidden;box-shadow:0 12px 40px rgba(0,0,0,.25)}.ai-hero-img img{width:100%;display:block;object-fit:cover;max-height:320px}
.ai-stats{display:flex;justify-content:center;gap:2.5rem;padding:1.75rem 1.5rem;background:var(--mint);flex-wrap:wrap}
.ai-stat{text-align:center}.ai-stat strong{display:block;font-size:1.75rem;color:var(--forest)}.ai-stat span{font-size:.85rem;color:var(--green);font-weight:600}
.ai-wrap{max-width:72rem;margin:0 auto;padding:var(--vt-section-y,3rem) 1.5rem}
.ai-offers h2,.ai-contact h2{text-align:center;color:var(--forest);margin:0 0 .5rem}
.ai-offers .ai-lead{text-align:center;margin:0 auto 2rem;color:#4b5563;max-width:50ch}
.ai-cards{display:grid;gap:1.25rem}@media(min-width:768px){.ai-cards{grid-template-columns:repeat(3,1fr)}}
.ai-card{background:#fff;border-radius:16px;overflow:hidden;box-shadow:0 4px 16px rgba(21,128,61,.1);border-top:4px solid var(--leaf)}
.ai-card-img{margin:0}.ai-card-img img{width:100%;height:180px;object-fit:cover}
.ai-card h3{margin:1rem 1rem .35rem;color:var(--forest)}.ai-card p{margin:0 1rem 1.25rem;font-size:.92rem;color:#4b5563}
.ai-trust{padding:2.5rem 1.5rem;background:var(--mint);text-align:center}
.ai-quote{max-width:40rem;margin:0 auto;border:none;padding:0}
.ai-quote p{font-size:1.1rem;font-style:italic;color:var(--text);margin:0 0 1rem;line-height:1.6}
.ai-quote footer{color:var(--green);font-weight:600;font-size:.9rem}
.ai-contact{background:#fff}.ai-contact-inner{max-width:28rem}
.ai-form{display:grid;gap:1rem}.ai-form label{display:grid;gap:.3rem;font-weight:600;font-size:.9rem;color:var(--forest)}
.ai-form input,.ai-form textarea{border:2px solid var(--mint);border-radius:10px;padding:.65rem;font:inherit;background:#f7fdf8}
.ai-cta{width:100%;background:var(--green)!important;color:#fff!important}
.ai-form-note{text-align:center;font-size:.8rem;color:#6b7280;margin:0}
.ai-foot{padding:1.5rem;text-align:center;background:var(--forest);color:rgba(255,255,255,.85);font-size:.85rem}
.ai-foot a{color:#fff}
""",
    },
    {
        "slug": "commerce",
        "title": "Halles Thionville — Épicerie & drive",
        "description": "Halles Thionville : primeurs, épicerie fine et drive en 45 minutes. Produits locaux et circuit court en Moselle.",
        "layout": "market-forest-green",
        "brand": "Halles Thionville",
        "h1": "Votre marché de quartier, en ligne comme en magasin",
        "lead": "Primeurs mosellans, traiteur maison et click & collect en 45 min — Halles Thionville, le goût du terroir livré près de chez vous.",
        "nav_links": '<a href="#offres">Rayons</a><a href="#confiance">Engagements</a>',
        "nav_cta": "Commander",
        "stats": [("1962", "depuis"), ("4,8/5", "avis clients"), ("45 min", "drive")],
        "offers": [
            ("Primeurs", "Fruits et légumes circuit court, arrivages du matin.", 1),
            ("Traiteur", "Plats mijotés, charcuterie artisanale et plateaux.", 2),
            ("Drive express", "Commande en ligne, retrait parking en 45 minutes.", 3),
        ],
        "trust": """<div class="ai-trust-grid">
  <h3>Nos engagements</h3>
  <ul class="ai-checklist">
    <li>Producteurs mosellans prioritaires</li>
    <li>Emballages recyclables</li>
    <li>Prix affichés au kilo, sans surprise</li>
    <li>Fidélité : 1 € = 1 point</li>
  </ul>
</div>""",
        "contact_title": "Une question ? Contactez-nous",
        "contact_cta": "Envoyer ma demande",
        "css": """:root{--forest:#1b5e20;--leaf:#43a047;--sage:#e8f5e9;--bark:#33691e;--cream:#f1f8e9}
body{margin:0;background:var(--cream);color:#1b3a1b}
.ai-skip{position:absolute;left:-9999px}.ai-skip:focus{left:1rem;top:1rem;background:#fff;padding:.5rem;z-index:99}
.ai-nav{display:flex;align-items:center;gap:1rem;padding:1rem 1.5rem;background:var(--forest);position:sticky;top:0;z-index:50}
.ai-logo{font-weight:800;color:#fff;text-decoration:none;font-size:1.1rem}
.ai-nav nav{display:flex;gap:1.25rem;flex:1}.ai-nav a{color:rgba(255,255,255,.85);text-decoration:none;font-weight:500}
.ai-nav-cta{background:var(--leaf)!important;color:#fff!important}
.ai-hero{padding:0;display:grid}@media(min-width:900px){.ai-hero{grid-template-columns:1fr 1fr;min-height:420px}}
.ai-hero-img{margin:0;order:-1}@media(min-width:900px){.ai-hero-img{order:1}}.ai-hero-img img{width:100%;height:100%;min-height:280px;object-fit:cover;display:block}
.ai-hero-text{padding:clamp(2rem,5vw,3rem) 1.5rem;display:flex;flex-direction:column;justify-content:center;background:var(--sage)}
.ai-hero .vt-eyebrow{color:var(--bark);margin:0 0 .5rem}
.ai-hero h1{color:var(--forest);margin:0 0 1rem}
.ai-hero .ai-lead{margin:0 0 1.5rem;max-width:48ch;color:#2e5a2e}
.ai-hero-actions .vt-btn{background:var(--forest);color:#fff;border:none}
.ai-hero-actions .ai-ghost{color:var(--bark);text-decoration:underline;display:inline-flex;align-items:center;min-height:44px;margin-left:.75rem;font-weight:600}
.ai-stats{display:grid;grid-template-columns:repeat(3,1fr);background:var(--forest);color:#fff;padding:1.5rem;text-align:center}
.ai-stat strong{display:block;font-size:1.6rem;color:var(--leaf)}.ai-stat span{font-size:.85rem;opacity:.85}
.ai-wrap{max-width:72rem;margin:0 auto;padding:var(--vt-section-y,3rem) 1.5rem}
.ai-offers h2,.ai-contact h2{text-align:center;color:var(--forest);margin:0 0 .5rem}
.ai-offers .ai-lead{text-align:center;margin:0 auto 2rem;color:#4a6741;max-width:50ch}
.ai-cards{display:grid;gap:1.25rem}@media(min-width:768px){.ai-cards{grid-template-columns:repeat(3,1fr)}}
.ai-card{background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 4px 16px rgba(27,94,32,.12)}
.ai-card-img{margin:0}.ai-card-img img{width:100%;height:190px;object-fit:cover}
.ai-card h3{margin:1rem 1rem .35rem;color:var(--forest)}.ai-card p{margin:0 1rem 1.25rem;font-size:.92rem;color:#4a6741}
.ai-trust{padding:2.5rem 1.5rem;background:var(--sage);text-align:center}
.ai-trust-grid h3{color:var(--forest);margin:0 0 1rem}
.ai-checklist{list-style:none;padding:0;margin:0 auto;max-width:26rem;text-align:left}
.ai-checklist li{padding:.45rem 0 .45rem 1.75rem;position:relative;font-weight:500;color:#2e5a2e}
.ai-checklist li::before{content:"🌿";position:absolute;left:0}
.ai-contact{background:#fff}.ai-contact-inner{max-width:28rem}
.ai-form{display:grid;gap:1rem}.ai-form label{display:grid;gap:.3rem;font-weight:600;font-size:.9rem;color:var(--forest)}
.ai-form input,.ai-form textarea{border:1px solid #a5d6a7;border-radius:8px;padding:.65rem;font:inherit;background:var(--cream)}
.ai-cta{width:100%;background:var(--forest)!important;color:#fff!important}
.ai-form-note{text-align:center;font-size:.8rem;color:#6b8065;margin:0}
.ai-foot{padding:1.5rem;text-align:center;background:var(--bark);color:rgba(255,255,255,.9);font-size:.85rem}
.ai-foot a{color:#fff}
""",
    },
    {
        "slug": "comptable",
        "title": "Verlaine & Associés — Cabinet comptable Metz",
        "description": "Verlaine & Associés : expert-comptable à Metz et Thionville. Tenue, paie, conseil et bilan flash sous 48 h pour dirigeants.",
        "layout": "cabinet-navy-pro",
        "brand": "Verlaine & Associés",
        "h1": "Vos chiffres, expliqués sans jargon",
        "lead": "Tenue comptable, paie et conseil dirigeant pour PME de Metz et Thionville — réactivité, transparence et bilan flash sous 48 h.",
        "nav_links": '<a href="#offres">Services</a><a href="#confiance">Références</a>',
        "nav_cta": "Consultation",
        "stats": [("25 ans", "d'expérience"), ("800+", "clients"), ("48 h", "bilan flash")],
        "offers": [
            ("Tenue comptable", "Liasse fiscale, TVA et tableaux de bord mensuels.", 1),
            ("Paie & social", "Bulletins, DSN et veille conventionnelle.", 2),
            ("Conseil dirigeant", "Pilotage, restructuration et transmission.", 3),
        ],
        "trust": """<blockquote class="ai-quote">
  <p>« Un cabinet réactif qui parle vrai — nos décisions sont éclairées, nos échéances toujours tenues. »</p>
  <footer>Philippe R. · gérant PME · Thionville</footer>
</blockquote>""",
        "contact_title": "Premier échange gratuit",
        "contact_cta": "Demander un rendez-vous",
        "css": """:root{--navy:#0c2340;--blue:#1565c0;--gold:#c9a227;--slate:#eceff1;--text:#1a2332}
body{margin:0;background:#fff;color:var(--text)}
.ai-skip{position:absolute;left:-9999px}.ai-skip:focus{left:1rem;top:1rem;background:#fff;padding:.5rem;z-index:99}
.ai-nav{display:flex;align-items:center;gap:1rem;padding:.9rem 2rem;background:var(--navy);position:sticky;top:0;z-index:50}
.ai-logo{font-weight:600;color:#fff;text-decoration:none;font-size:1.05rem;letter-spacing:.02em}
.ai-logo em{font-style:normal;color:var(--gold)}
.ai-nav nav{display:flex;gap:1.5rem;flex:1}.ai-nav a{color:rgba(255,255,255,.8);text-decoration:none;font-weight:400;font-size:.95rem}
.ai-nav-cta{background:var(--gold)!important;color:var(--navy)!important;font-weight:700!important}
.ai-hero{padding:clamp(2.5rem,5vw,4rem) 1.5rem;background:linear-gradient(135deg,var(--navy) 60%,#1a3a5c);color:#fff}
.ai-hero-center{max-width:56rem;margin:0 auto;text-align:center}
.ai-hero .vt-eyebrow{color:var(--gold);margin:0 0 .75rem}
.ai-hero h1{color:#fff;margin:0 auto 1rem;max-width:20ch}
.ai-hero .ai-lead{margin:0 auto 1.5rem;max-width:52ch;opacity:.9}
.ai-hero-actions{margin-bottom:2rem}.ai-hero-actions .vt-btn{background:var(--gold);color:var(--navy);border:none;font-weight:700}
.ai-hero-actions .ai-ghost{color:#fff;text-decoration:none;display:inline-flex;align-items:center;min-height:44px;margin-left:.75rem;padding:0 1rem;border:1px solid rgba(255,255,255,.4);border-radius:.5rem}
.ai-hero-img{margin:0 auto;max-width:720px;border-radius:8px;overflow:hidden;border:2px solid rgba(201,162,39,.4);box-shadow:0 16px 48px rgba(0,0,0,.3)}
.ai-hero-img img{width:100%;display:block;object-fit:cover;max-height:300px}
.ai-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;padding:0 1.5rem 2rem;max-width:56rem;margin:-1rem auto 0;background:#fff;border-radius:8px;box-shadow:0 4px 24px rgba(12,35,64,.12);position:relative;z-index:2}
.ai-stat{text-align:center;padding:1.25rem .5rem;border-right:1px solid var(--slate)}.ai-stat:last-child{border-right:none}
.ai-stat strong{display:block;font-size:1.5rem;color:var(--navy)}.ai-stat span{font-size:.8rem;color:#64748b;text-transform:uppercase;letter-spacing:.04em}
.ai-wrap{max-width:68rem;margin:0 auto;padding:var(--vt-section-y,3rem) 1.5rem}
.ai-offers h2,.ai-contact h2{text-align:center;color:var(--navy);margin:0 0 .5rem;font-weight:600}
.ai-offers .ai-lead{text-align:center;margin:0 auto 2.5rem;color:#64748b;max-width:48ch}
.ai-cards{display:grid;gap:1.5rem}@media(min-width:768px){.ai-cards{grid-template-columns:repeat(3,1fr)}}
.ai-card{background:var(--slate);border-radius:8px;overflow:hidden;border-top:3px solid var(--gold)}
.ai-card-img{margin:0}.ai-card-img img{width:100%;height:180px;object-fit:cover}
.ai-card h3{margin:1rem 1rem .35rem;color:var(--navy);font-weight:600}.ai-card p{margin:0 1rem 1.25rem;font-size:.92rem;color:#64748b}
.ai-trust{padding:3rem 1.5rem;background:var(--navy);color:#fff;text-align:center}
.ai-quote{max-width:38rem;margin:0 auto;border:none;padding:0}
.ai-quote p{font-size:1.1rem;font-style:italic;opacity:.92;margin:0 0 1rem;line-height:1.6}
.ai-quote footer{color:var(--gold);font-size:.9rem;font-weight:500}
.ai-contact{background:var(--slate)}.ai-contact-inner{max-width:28rem}
.ai-form{display:grid;gap:1rem}.ai-form label{display:grid;gap:.3rem;font-weight:600;font-size:.9rem;color:var(--navy)}
.ai-form input,.ai-form textarea{border:1px solid #cfd8dc;border-radius:6px;padding:.65rem;font:inherit;background:#fff}
.ai-cta{width:100%;background:var(--navy)!important;color:#fff!important}
.ai-form-note{text-align:center;font-size:.8rem;color:#64748b;margin:0}
.ai-foot{padding:1.5rem;text-align:center;background:var(--navy);color:rgba(255,255,255,.75);font-size:.85rem;border-top:3px solid var(--gold)}
.ai-foot a{color:var(--gold)}
""",
    },
]


def hero_block(site: dict) -> str:
    slug = site["slug"]
    alt = site["brand"]
    img = hero_img(alt)

    if slug == "technologie":
        return f"""<div class="ai-hero-grid">
  <div>
    <p class="vt-eyebrow">Grand Est · Moselle</p>
    <h1>{esc(site["h1"])}</h1>
    <p class="ai-lead">{esc(site["lead"])}</p>
    <div class="ai-hero-actions">
      <a class="vt-btn" href="#offres">Voir les modules</a>
      <a class="ai-ghost" href="#contact">Parler à un expert</a>
    </div>
  </div>
  {img}
</div>"""

    if slug == "restauration":
        return f"""<div class="ai-hero-split">
  <div class="ai-hero-text">
    <p class="vt-eyebrow">Metz · Lorraine</p>
    <h1>{esc(site["h1"])}</h1>
    <p class="ai-lead">{esc(site["lead"])}</p>
    <div class="ai-hero-actions">
      <a class="vt-btn" href="#contact">Réserver une table</a>
      <a class="ai-ghost" href="#offres">Voir la carte</a>
    </div>
  </div>
  {img}
</div>"""

    if slug == "beaute":
        return f"""<div class="ai-hero-center">
  <p class="vt-eyebrow">Nancy · Grand Est</p>
  <h1>{esc(site["h1"])}</h1>
  <p class="ai-lead">{esc(site["lead"])}</p>
  <div class="ai-hero-actions"><a class="vt-btn" href="#contact">Prendre rendez-vous</a></div>
  {img}
</div>"""

    if slug == "odontologie":
        return f"""<div class="ai-hero-grid">
  <div>
    <p class="vt-eyebrow">Metz · Santé bucco-dentaire</p>
    <h1>{esc(site["h1"])}</h1>
    <p class="ai-lead">{esc(site["lead"])}</p>
    <div class="ai-hero-actions">
      <a class="vt-btn" href="#contact">Prendre RDV</a>
      <a class="ai-ghost" href="#offres">Nos soins</a>
    </div>
  </div>
  {img}
</div>"""

    if slug == "industrie":
        return f"""<div class="ai-hero-grid">
  <div>
    <p class="vt-eyebrow">Thionville · Moselle-Est</p>
    <h1>{esc(site["h1"])}</h1>
    <p class="ai-lead">{esc(site["lead"])}</p>
    <div class="ai-hero-actions">
      <a class="vt-btn" href="#contact">Demander un devis</a>
      <a class="ai-ghost" href="#offres">Capacités →</a>
    </div>
  </div>
  {img}
</div>"""

    if slug == "association":
        return f"""<div class="ai-hero-grid">
  <div>
    <p class="vt-eyebrow">Metz Métropole · ESS</p>
    <h1>{esc(site["h1"])}</h1>
    <p class="ai-lead">{esc(site["lead"])}</p>
    <div class="ai-hero-actions">
      <a class="vt-btn" href="#contact">Devenir bénévole</a>
      <a class="ai-ghost" href="#contact">Faire un don</a>
    </div>
  </div>
  {img}
</div>"""

    if slug == "commerce":
        return f"""{img}
  <div class="ai-hero-text">
    <p class="vt-eyebrow">Thionville · Moselle</p>
    <h1>{esc(site["h1"])}</h1>
    <p class="ai-lead">{esc(site["lead"])}</p>
    <div class="ai-hero-actions">
      <a class="vt-btn" href="#offres">Voir les rayons</a>
      <a class="ai-ghost" href="#contact">Commander</a>
    </div>
  </div>"""

    # comptable
    return f"""<div class="ai-hero-center">
  <p class="vt-eyebrow">Metz &amp; Thionville · Expert-comptable</p>
  <h1>{esc(site["h1"])}</h1>
  <p class="ai-lead">{esc(site["lead"])}</p>
  <div class="ai-hero-actions">
    <a class="vt-btn" href="#contact">Consultation gratuite</a>
    <a class="ai-ghost" href="#offres">Nos services</a>
  </div>
  {img}
</div>"""


def build_site(site: dict) -> None:
    offers_html = "".join(
        f"""<article class="ai-card">
  {card_img(n, title)}
  <h3>{esc(title)}</h3>
  <p>{esc(desc)}</p>
</article>"""
        for title, desc, n in site["offers"]
    )

    brand_display = site["brand"]
    if site["slug"] == "comptable":
        brand_display = "Verlaine <em>&amp; Associés</em>"

    body = body_shell(
        brand_display,
        site["nav_links"],
        hero_block(site),
        stats_row(site["stats"]),
        offers_html,
        site["trust"],
        site["contact_title"],
        site["contact_cta"],
        nav_cta=site["nav_cta"],
    )

    write_ai_site(
        site["slug"],
        site["title"],
        site["description"],
        body,
        site["css"],
        layout=site["layout"],
    )


def run() -> list[str]:
    ok: list[str] = []
    for site in SITES:
        build_site(site)
        ok.append(site["slug"])
        print(f"OK {site['slug']}")
    return ok


if __name__ == "__main__":
    run()
