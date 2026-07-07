#!/usr/bin/env python3
"""Batch B — 9 vitrines métier Grand Est (designs uniques via write_ai_site)."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from vitrine_ai_lib import write_ai_site  # noqa: E402


def _cards(slug: str, items: list[tuple[str, str, str]]) -> str:
    out = []
    for i, (title, desc, alt) in enumerate(items, 1):
        out.append(f"""<article class="card">
  <figure class="vitrine-figure"><img src="images/card-{i}.png" alt="{alt}" loading="lazy" decoding="async"></figure>
  <h3>{title}</h3><p>{desc}</p>
</article>""")
    return "\n".join(out)


def site_education() -> str:
    slug = "education"
    body = """
<a class="skip" href="#contenu">Aller au contenu</a>
<header class="top">
  <div class="bar"><a class="brand" href="#">Institut Mercure</a>
  <nav><a href="#parcours">Parcours</a><a href="#offres">Offres</a><a href="#contact">Contact</a></nav></div>
</header>
<main id="contenu">
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-copy">
        <p class="eyebrow">Grand Est · Nancy &amp; Metz</p>
        <h1>Former aujourd'hui les métiers de demain</h1>
        <p class="lead">Alternance, certifications Qualiopi et parcours VAE pour adultes en reconversion — ancrés en Lorraine depuis 1998.</p>
        <div class="cta-row"><a class="btn btn--primary" href="#offres">Découvrir nos formations</a><a class="btn btn--ghost" href="#contact">Demander un entretien</a></div>
      </div>
      <figure class="hero-img vitrine-figure"><img src="images/hero.png" alt="Campus Institut Mercure Nancy" fetchpriority="high" decoding="async"></figure>
    </div>
  </section>
  <section class="stats" aria-label="Chiffres clés">
    <div class="stats-grid"><div><strong>1 240</strong><span>apprenants / an</span></div>
    <div><strong>38</strong><span>parcours certifiants</span></div><div><strong>94 %</strong><span>taux d'insertion</span></div></div>
  </section>
  <section id="parcours" class="section">
    <h2>Votre parcours en 4 étapes</h2>
    <ol class="timeline">
      <li><span class="step">01</span><div><h3>Diagnostic</h3><p>Entretien individuel et positionnement compétences à Nancy ou en visio.</p></div></li>
      <li><span class="step">02</span><div><h3>Formation</h3><p>Modules hybrides : présentiel, FOAD et tutorat entreprise.</p></div></li>
      <li><span class="step">03</span><div><h3>Certification</h3><p>Passage des blocs RNCP ou Titre Pro devant jury régional.</p></div></li>
      <li><span class="step">04</span><div><h3>Insertion</h3><p>Ateliers CV, réseau 180 entreprises partenaires Grand Est.</p></div></li>
    </ol>
  </section>
  <section id="offres" class="section section--alt">
    <h2>Nos domaines phares</h2>
    <p class="sub">Des parcours courts et certifiants, finançables OPCO et CPF.</p>
    <div class="cards">""" + _cards(slug, [
        ("Digital &amp; data", "Marketing digital, no-code et gestion de projet agile — 6 à 12 mois.", "Formation digital"),
        ("Management", "Encadrement d'équipe, QHSE et conduite du changement pour cadres.", "Formation management"),
        ("Métiers techniques", "SST, électricité, maintenance industrielle — alternance possible.", "Formation technique"),
    ]) + """
    </div>
  </section>
  <section class="trust">
    <blockquote><p>« Mercure m'a permis de valider mon titre Responsable QHSE en 9 mois tout en travaillant à Thionville. »</p>
    <cite>— Karim B., diplômé 2025</cite></blockquote>
    <p class="badges">Qualiopi · Datadock · Réseau CCI Grand Est</p>
  </section>
  <section id="contact" class="section contact">
    <h2>Parlons de votre projet</h2>
    <form class="form" action="#" method="post">
      <label>Nom <input type="text" name="nom" required></label>
      <label>Email <input type="email" name="email" required></label>
      <label>Formation visée <select name="formation"><option>Digital</option><option>Management</option><option>Technique</option></select></label>
      <label>Message <textarea name="msg" rows="3"></textarea></label>
      <button type="submit" class="btn btn--primary">Envoyer ma demande</button>
    </form>
  </section>
</main>"""
    css = """
:root{--c:#2563eb;--c-dark:#1e40af;--bg:#f8fafc;--text:#0f172a}
*{box-sizing:border-box}body{margin:0;font-family:"Plus Jakarta Sans",system-ui,sans-serif;font-size:17px;line-height:1.6;color:var(--text)}
.skip{position:absolute;left:-9999px}.skip:focus{left:1rem;top:1rem;z-index:99;background:#fff;padding:.5rem}
.top{background:#fff;border-bottom:1px solid #e2e8f0;position:sticky;top:0;z-index:50}
.bar{max-width:72rem;margin:0 auto;padding:1rem;display:flex;flex-wrap:wrap;gap:1rem;align-items:center;justify-content:space-between}
.brand{font-weight:800;color:var(--c);text-decoration:none;font-size:1.15rem}
nav a{margin-left:1rem;color:#475569;text-decoration:none;font-weight:500}
.hero{background:linear-gradient(135deg,var(--c),var(--c-dark));color:#fff;padding:clamp(2.5rem,6vw,4rem) 1rem}
.hero-inner{max-width:72rem;margin:0 auto;display:grid;gap:2rem;align-items:center}
@media(min-width:900px){.hero-inner{grid-template-columns:1fr 1fr}}
.eyebrow{font-size:.8rem;text-transform:uppercase;letter-spacing:.08em;opacity:.9}
.hero h1{font-size:clamp(2rem,4.5vw,2.75rem);line-height:1.15;margin:.5rem 0 1rem;max-width:18ch}
.lead{max-width:55ch;opacity:.95;margin-bottom:1.5rem}
.cta-row{display:flex;flex-wrap:wrap;gap:.75rem}
.btn{display:inline-flex;align-items:center;justify-content:center;min-height:44px;padding:.75rem 1.5rem;border-radius:.5rem;font-weight:600;text-decoration:none;border:none;cursor:pointer;font-size:1rem}
.btn--primary{background:#fff;color:var(--c-dark)}.btn--ghost{border:1px solid rgba(255,255,255,.7);color:#fff;background:transparent}
.hero-img img{width:100%;border-radius:.75rem;max-height:320px;object-fit:cover}
.stats{background:var(--c-dark);color:#fff;padding:2rem 1rem}
.stats-grid{max-width:72rem;margin:0 auto;display:grid;gap:1.5rem;text-align:center}
@media(min-width:640px){.stats-grid{grid-template-columns:repeat(3,1fr)}}
.stats strong{display:block;font-size:2rem;font-weight:800}
.section{max-width:72rem;margin:0 auto;padding:clamp(3rem,8vw,5rem) 1rem}
.section--alt{background:var(--bg)}
.section h2{margin:0 0 .5rem;font-size:clamp(1.5rem,3vw,1.95rem)}
.sub{color:#64748b;margin-bottom:2rem}
.timeline{list-style:none;padding:0;margin:2rem 0 0;display:grid;gap:1.25rem}
@media(min-width:768px){.timeline{grid-template-columns:repeat(2,1fr)}}
.timeline li{display:flex;gap:1rem;align-items:flex-start;background:#fff;border:1px solid #e2e8f0;border-radius:.75rem;padding:1.25rem}
.step{font-weight:800;color:var(--c);font-size:1.25rem;min-width:2.5rem}
.timeline h3{margin:0 0 .25rem;font-size:1rem}
.timeline p{margin:0;color:#64748b;font-size:.95rem}
.cards{display:grid;gap:1.5rem}
@media(min-width:768px){.cards{grid-template-columns:repeat(3,1fr)}}
.card{background:#fff;border-radius:.75rem;overflow:hidden;border:1px solid #e2e8f0}
.card img{width:100%;height:200px;object-fit:cover}
.card h3,.card p{padding:0 1rem}.card h3{margin-top:1rem}.card p{color:#64748b;padding-bottom:1rem;font-size:.95rem}
.trust{background:var(--c);color:#fff;text-align:center;padding:3rem 1.5rem}
.trust blockquote{margin:0;font-size:1.15rem;max-width:50ch;margin-inline:auto}
.trust cite{display:block;margin-top:1rem;opacity:.85;font-style:normal;font-size:.9rem}
.badges{margin-top:1.5rem;font-size:.85rem;opacity:.8}
.contact .form{display:grid;gap:1rem;max-width:28rem;margin-top:1.5rem}
.form label{display:grid;gap:.35rem;font-weight:500;font-size:.9rem}
.form input,.form select,.form textarea{padding:.65rem .75rem;border:1px solid #cbd5e1;border-radius:.5rem;font:inherit}
.ai-foot{text-align:center;padding:1.5rem;color:#64748b;border-top:1px solid #e2e8f0}
"""
    write_ai_site(slug, "Institut Mercure — Formation pro | démo",
                  "Institut Mercure à Nancy : alternance, certifications et VAE en Grand Est.",
                  body, css, layout="timeline-formation")
    return slug


def site_services() -> str:
    slug = "services"
    body = """
<a class="skip" href="#contenu">Aller au contenu</a>
<header class="nav"><span class="logo">Proprio Facility</span>
<nav><a href="#services">Services</a><a href="#zones">Zones</a><a href="#devis">Devis</a></nav></header>
<main id="contenu">
  <section class="hero">
    <div class="hero-wrap">
      <p class="tag">Facility management · Metz &amp; Luxembourg</p>
      <h1>Votre immeuble, notre quotidien</h1>
      <p class="lead">Maintenance multi-technique, propreté et accueil pour copropriétés, bureaux et sites tertiaires en Moselle.</p>
      <a class="cta" href="#devis">Demander un devis sous 48 h</a>
    </div>
    <figure class="hero-visual"><img src="images/hero.png" alt="Équipe Proprio Facility en intervention" fetchpriority="high"></figure>
    <div class="float-cards">
      <div class="fc"><strong>24/7</strong><span>Astreinte technique</span></div>
      <div class="fc"><strong>ISO 9001</strong><span>Process certifiés</span></div>
    </div>
  </section>
  <section class="band"><div><b>320</b> sites gérés</div><div><b>18</b> techniciens</div><div><b>&lt; 2 h</b> délai moyen</div></section>
  <section id="services" class="sec">
    <h2>Une offre modulaire</h2>
    <div class="icon-grid">
      <article><span class="ico">🔧</span><h3>Maintenance</h3><p>Plomberie, électricité, CVC — contrats préventifs et curatifs.</p></article>
      <article><span class="ico">✨</span><h3>Propreté</h3><p>Nettoyage quotidien, vitrerie et remise en état après travaux.</p></article>
      <article><span class="ico">🏢</span><h3>Accueil</h3><p>Standard, badgeuse et gestion des fournisseurs sur site.</p></article>
    </div>
  </section>
  <section id="zones" class="sec sec--teal">
    <h2>Intervention Grand Est</h2>
    <p>Metz, Thionville, Forbach, Luxembourg frontalier — une seule équipe, un seul interlocuteur.</p>
    <div class="cards">""" + _cards(slug, [
        ("Résidences", "Syndics et bailleurs : ascenseurs, parties communes, espaces verts.", "Gestion résidences"),
        ("Tertiaire", "Bureaux et commerces : conformité ERP et audits sécurité.", "Facility tertiaire"),
        ("Industrie légère", "Entrepôts et ateliers : maintenance planifiée hors production.", "Site industriel"),
    ]) + """
    </div>
  </section>
  <section class="quote"><p>« Depuis Proprio Facility, plus aucune réclamation ascenseur non traitée. »</p><cite>— Syndic Les Faïenceries, Metz</cite></section>
  <section id="devis" class="sec contact">
    <h2>Devis gratuit</h2>
    <form class="form"><label>Société <input type="text" required></label><label>Surface (m²) <input type="number"></label><label>Email <input type="email" required></label><button type="submit" class="cta">Recevoir mon estimation</button></form>
  </section>
</main>"""
    css = """
:root{--teal:#0d9488;--teal-d:#0f766e;--cream:#f0fdfa}
body{margin:0;font-family:"Plus Jakarta Sans",system-ui,sans-serif;font-size:17px;color:#134e4a;background:#fff}
.skip{position:absolute;left:-9999px}.skip:focus{left:1rem;top:1rem;background:#fff;padding:.5rem;z-index:99}
.nav{display:flex;align-items:center;justify-content:space-between;padding:1rem 1.5rem;border-bottom:1px solid #ccfbf1;position:sticky;top:0;background:rgba(255,255,255,.95);z-index:40}
.logo{font-weight:800;color:var(--teal)}.nav a{margin-left:1rem;color:#475569;text-decoration:none;font-weight:500}
.hero{position:relative;background:var(--cream);padding:3rem 1.5rem 5rem;overflow:hidden}
.hero-wrap{max-width:32rem;position:relative;z-index:2}
.tag{color:var(--teal);font-weight:600;font-size:.85rem;text-transform:uppercase;letter-spacing:.05em}
.hero h1{font-size:clamp(2rem,5vw,2.8rem);line-height:1.1;margin:.5rem 0 1rem;color:#042f2e}
.lead{color:#115e59;margin-bottom:1.5rem;max-width:45ch}
.cta{display:inline-flex;align-items:center;min-height:44px;padding:.75rem 1.5rem;background:var(--teal);color:#fff;text-decoration:none;border-radius:999px;font-weight:600;border:none;cursor:pointer}
.hero-visual{position:absolute;right:0;top:50%;transform:translateY(-50%);width:min(50%,480px);z-index:1}
.hero-visual img{width:100%;border-radius:1rem 0 0 1rem;box-shadow:-12px 12px 40px rgba(13,148,136,.2)}
.float-cards{position:absolute;bottom:2rem;left:1.5rem;display:flex;gap:1rem;z-index:3}
.fc{background:#fff;padding:1rem 1.25rem;border-radius:.75rem;box-shadow:0 4px 20px rgba(0,0,0,.08);border-left:4px solid var(--teal)}
.fc strong{display:block;font-size:1.25rem;color:var(--teal-d)}
.fc span{font-size:.8rem;color:#64748b}
.band{display:flex;justify-content:center;flex-wrap:wrap;gap:2rem;padding:1.5rem;background:var(--teal-d);color:#fff;font-size:1.1rem}
.band b{font-size:1.5rem;margin-right:.25rem}
.sec{max-width:72rem;margin:0 auto;padding:4rem 1.5rem}
.sec--teal{background:var(--cream)}
.sec h2{margin-bottom:1.5rem}
.icon-grid{display:grid;gap:1.5rem}
@media(min-width:700px){.icon-grid{grid-template-columns:repeat(3,1fr)}}
.icon-grid article{background:#fff;border:1px solid #99f6e4;border-radius:1rem;padding:1.5rem}
.ico{font-size:2rem}.icon-grid h3{margin:.5rem 0}
.icon-grid p{color:#64748b;font-size:.95rem;margin:0}
.cards{display:grid;gap:1.25rem;margin-top:2rem}
@media(min-width:768px){.cards{grid-template-columns:repeat(3,1fr)}}
.card{background:#fff;border-radius:.75rem;overflow:hidden}
.card img{width:100%;height:180px;object-fit:cover}
.card h3,.card p{padding:0 1rem}.card p{color:#64748b;padding-bottom:1rem;font-size:.95rem}
.quote{text-align:center;padding:2.5rem 1.5rem;background:var(--teal);color:#fff}
.quote cite{display:block;margin-top:.75rem;opacity:.85;font-style:normal;font-size:.9rem}
.form{display:grid;gap:1rem;max-width:24rem}
.form label{display:grid;gap:.3rem;font-weight:500}
.form input{padding:.65rem;border:1px solid #99f6e4;border-radius:.5rem;font:inherit}
@media(max-width:800px){.hero-visual{position:static;transform:none;width:100%;margin-top:2rem}.float-cards{position:static;margin-top:1rem}}
.ai-foot{text-align:center;padding:1.5rem;color:#64748b}
"""
    write_ai_site(slug, "Proprio Facility — Facility management | démo",
                  "Maintenance, propreté et accueil pour immeubles et bureaux en Moselle.",
                  body, css, layout="asymmetric-teal")
    return slug


def site_etablissement() -> str:
    slug = "etablissement"
    body = """
<header class="lux-nav"><a href="#" class="lux-logo">Hôtel Stanislas Collection</a>
<nav><a href="#suites">Suites</a><a href="#experience">Expérience</a><a href="#reserver">Réserver</a></nav></header>
<main id="contenu">
  <section class="lux-hero">
    <img src="images/hero.png" alt="Suite Stanislas Nancy" class="lux-hero-bg">
    <div class="lux-hero-overlay">
      <p class="lux-eyebrow">Nancy · Place Stanislas</p>
      <h1>L'art de recevoir, à la lorraine</h1>
      <p>5 étoiles, 42 chambres et un spa thermal — au cœur du patrimoine UNESCO.</p>
      <a href="#reserver" class="lux-btn">Réserver votre séjour</a>
    </div>
  </section>
  <div class="lux-stats"><span><em>42</em> chambres &amp; suites</span><span><em>1835</em> bâtisse historique</span><span><em>4.9</em> note clients</span></div>
  <section id="suites" class="lux-sec">
    <h2>Nos univers</h2>
    <div class="lux-grid">""" + _cards(slug, [
        ("Suite Stanislas", "Vue place, parquet d'époque et salon privé — 65 m² de raffinement.", "Suite Stanislas"),
        ("Chambre Jardin", "Terrasse ombragée sur cour intérieure, calme absolu.", "Chambre jardin"),
        ("Penthouse Lorraine", "Dernier étage, jacuzzi et panorama 360° sur la ville.", "Penthouse"),
    ]) + """
    </div>
  </section>
  <section id="experience" class="lux-sec lux-sec--dark">
    <div class="lux-split">
      <div><h2>Une expérience sensorielle</h2>
      <ul class="lux-list"><li>Restaurant Le Opéra — cuisine du terroir revisitée</li><li>Spa thermal 400 m² — soins vinotherapy</li><li>Conciergerie Clefs d'Or — transferts Metz-Nancy</li></ul></div>
      <blockquote>« Le plus beau réveil de ma vie, face à la place Stanislas. »<cite>— Élodie M., Paris</cite></blockquote>
    </div>
  </section>
  <section id="reserver" class="lux-sec lux-book">
    <h2>Réserver</h2>
    <form class="lux-form"><div class="row"><label>Arrivée <input type="date"></label><label>Départ <input type="date"></label></div>
    <label>Email <input type="email" required></label><button type="submit" class="lux-btn">Vérifier les disponibilités</button></form>
  </section>
</main>"""
    css = """
:root{--gold:#b8956a;--dark:#2c2419;--cream:#faf6f0}
body{margin:0;font-family:"Plus Jakarta Sans",Georgia,serif;font-size:17px;color:var(--dark);background:var(--cream)}
.lux-nav{display:flex;justify-content:space-between;align-items:center;padding:1.25rem 2rem;position:fixed;width:100%;z-index:50;background:linear-gradient(to bottom,rgba(44,36,25,.85),transparent)}
.lux-logo{color:#fff;text-decoration:none;font-weight:600;letter-spacing:.04em}
.lux-nav a{color:rgba(255,255,255,.9);text-decoration:none;margin-left:1.5rem;font-size:.9rem}
.lux-hero{position:relative;height:min(90vh,720px);display:flex;align-items:flex-end}
.lux-hero-bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.lux-hero-overlay{position:relative;z-index:2;padding:3rem 2rem;background:linear-gradient(transparent,rgba(44,36,25,.75));color:#fff;width:100%}
.lux-eyebrow{text-transform:uppercase;letter-spacing:.15em;font-size:.75rem;color:var(--gold)}
.lux-hero h1{font-size:clamp(2.2rem,5vw,3.2rem);margin:.5rem 0;font-weight:400;max-width:16ch}
.lux-btn{display:inline-flex;align-items:center;min-height:44px;padding:.85rem 2rem;background:var(--gold);color:#fff;text-decoration:none;border:none;font:inherit;letter-spacing:.05em;cursor:pointer;margin-top:1rem}
.lux-stats{display:flex;justify-content:center;flex-wrap:wrap;gap:2rem;padding:2rem;background:var(--dark);color:#fff}
.lux-stats em{font-style:normal;font-size:1.75rem;color:var(--gold);display:block}
.lux-sec{max-width:72rem;margin:0 auto;padding:4rem 1.5rem}
.lux-sec h2{font-weight:400;font-size:clamp(1.6rem,3vw,2.2rem);margin-bottom:2rem;text-align:center}
.lux-grid{display:grid;gap:1.5rem}
@media(min-width:768px){.lux-grid{grid-template-columns:repeat(3,1fr)}}
.card{text-align:center}.card img{width:100%;height:260px;object-fit:cover}
.card h3{margin:1rem 0 .5rem;font-weight:500}.card p{color:#6b5d4d;font-size:.95rem;padding:0 1rem 1rem}
.lux-sec--dark{background:var(--dark);color:#fff;max-width:none}
.lux-split{max-width:72rem;margin:0 auto;display:grid;gap:2rem;padding:0 1.5rem}
@media(min-width:800px){.lux-split{grid-template-columns:1fr 1fr;align-items:center}}
.lux-list{list-style:none;padding:0;line-height:2}
.lux-list li::before{content:"◆ ";color:var(--gold)}
blockquote{border-left:2px solid var(--gold);padding-left:1.5rem;margin:0;font-style:italic}
blockquote cite{display:block;margin-top:1rem;font-style:normal;font-size:.85rem;opacity:.7}
.lux-form{max-width:28rem;margin:0 auto}
.lux-form .row{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
.lux-form label{display:grid;gap:.35rem;margin-bottom:1rem}
.lux-form input{padding:.65rem;border:1px solid #d4c4a8;font:inherit;background:#fff}
.ai-foot{text-align:center;padding:2rem;color:#6b5d4d}
"""
    write_ai_site(slug, "Hôtel Stanislas Collection — Luxe Nancy | démo",
                  "Hôtel 5 étoiles face à la place Stanislas : suites, spa et gastronomie.",
                  body, css, layout="fullscreen-luxe")
    return slug


def site_automobile() -> str:
    slug = "automobile"
    body = """
<header class="gar-nav"><div class="gar-brand">Garage Central <small>Plappeville</small></div>
<ul><li><a href="#prestations">Prestations</a></li><li><a href="#engagements">Engagements</a></li><li><a href="#rdv">RDV</a></li></ul></header>
<main id="contenu">
  <section class="gar-hero">
    <div class="gar-hero-text">
      <span class="gar-badge">Depuis 1987 · Moselle</span>
      <h1>La mécanique sans compromis</h1>
      <p>Entretien, diagnostic et carrosserie pour particuliers et flottes — à 10 min de Metz.</p>
      <a href="#rdv" class="gar-cta">Prendre rendez-vous</a>
    </div>
    <div class="gar-hero-img"><img src="images/hero.png" alt="Atelier Garage Central Plappeville"></div>
  </section>
  <section class="gar-stats"><div><strong>12 000</strong> véhicules / an</div><div><strong>4.8★</strong> Google</div><div><strong>0€</strong> devis gratuit</div></section>
  <section id="prestations" class="gar-sec">
    <h2>Ce qu'on fait sur votre auto</h2>
    <div class="gar-services">
      <article class="gar-svc"><h3>Entretien</h3><ul><li>Vidange &amp; filtres</li><li>Distribution</li><li>Climatisation</li></ul></article>
      <article class="gar-svc gar-svc--hot"><h3>Diagnostic</h3><ul><li>Valise multimarque</li><li>Pré-contrôle technique</li><li>Électronique embarquée</li></ul></article>
      <article class="gar-svc"><h3>Carrosserie</h3><ul><li>Débosselage sans peinture</li><li>Pare-brise</li><li>Peinture cabine</li></ul></article>
    </div>
    <div class="gar-cards">""" + _cards(slug, [
        ("Flottes pro", "Contrats d'entretien pour artisans et PME mosellanes.", "Flottes professionnelles"),
        ("Véhicules premium", "Mercedes, BMW, Audi — pièces d'origine ou équivalent.", "Véhicule premium"),
        ("Véhicules utilitaires", "Fourgons et pick-up : préparation CT et hayons.", "Utilitaire"),
    ]) + """
    </div>
  </section>
  <section id="engagements" class="gar-band"><p>Véhicule de courtoisie · Devis détaillé avant intervention · Garantie pièces 2 ans</p></section>
  <section id="rdv" class="gar-sec gar-contact">
    <h2>Demande de rendez-vous</h2>
    <form><label>Immatriculation <input type="text" placeholder="AB-123-CD"></label><label>Téléphone <input type="tel" required></label><label>Prestation <select><option>Entretien</option><option>Diagnostic</option><option>Carrosserie</option></select></label><button type="submit" class="gar-cta">Confirmer</button></form>
  </section>
</main>"""
    css = """
:root{--red:#dc2626;--black:#0a0a0a;--gray:#1f1f1f}
body{margin:0;font-family:"Plus Jakarta Sans",system-ui,sans-serif;font-size:17px;background:var(--black);color:#f5f5f5}
.gar-nav{display:flex;justify-content:space-between;align-items:center;padding:1rem 1.5rem;background:var(--gray);border-bottom:3px solid var(--red);position:sticky;top:0;z-index:40}
.gar-brand{font-weight:800;font-size:1.2rem;text-transform:uppercase}.gar-brand small{display:block;font-size:.65rem;font-weight:500;color:#a3a3a3;letter-spacing:.1em}
.gar-nav ul{list-style:none;display:flex;gap:1.25rem;margin:0;padding:0}
.gar-nav a{color:#d4d4d4;text-decoration:none;font-weight:600;font-size:.9rem}
.gar-hero{display:grid;min-height:420px}
@media(min-width:900px){.gar-hero{grid-template-columns:1fr 1fr}}
.gar-hero-text{padding:3rem 1.5rem;display:flex;flex-direction:column;justify-content:center;background:linear-gradient(135deg,var(--black),var(--gray));clip-path:polygon(0 0,100% 0,95% 100%,0 100%)}
.gar-badge{background:var(--red);color:#fff;font-size:.75rem;font-weight:700;padding:.3rem .75rem;border-radius:2px;width:fit-content;text-transform:uppercase}
.gar-hero h1{font-size:clamp(2rem,5vw,3rem);margin:1rem 0;line-height:1.05;text-transform:uppercase}
.gar-hero p{color:#a3a3a3;max-width:40ch;margin-bottom:1.5rem}
.gar-cta{display:inline-flex;align-items:center;min-height:44px;padding:.75rem 1.75rem;background:var(--red);color:#fff;text-decoration:none;font-weight:700;text-transform:uppercase;border:none;cursor:pointer;clip-path:polygon(0 0,calc(100% - 12px) 0,100% 100%,0 100%)}
.gar-hero-img img{width:100%;height:100%;min-height:280px;object-fit:cover}
.gar-stats{display:flex;justify-content:center;flex-wrap:wrap;gap:2rem;padding:1.5rem;background:var(--red);font-weight:700}
.gar-stats strong{display:block;font-size:1.75rem}
.gar-sec{max-width:72rem;margin:0 auto;padding:4rem 1.5rem}
.gar-sec h2{text-transform:uppercase;letter-spacing:.05em;margin-bottom:2rem}
.gar-services{display:grid;gap:1rem;margin-bottom:3rem}
@media(min-width:700px){.gar-services{grid-template-columns:repeat(3,1fr)}}
.gar-svc{background:var(--gray);padding:1.5rem;border-left:4px solid #525252}
.gar-svc--hot{border-color:var(--red);background:linear-gradient(135deg,#2a0a0a,var(--gray))}
.gar-svc h3{margin:0 0 1rem;color:var(--red);text-transform:uppercase;font-size:.95rem}
.gar-svc ul{margin:0;padding-left:1.1rem;color:#a3a3a3;font-size:.9rem}
.gar-cards{display:grid;gap:1.25rem}
@media(min-width:768px){.gar-cards{grid-template-columns:repeat(3,1fr)}}
.card{background:var(--gray);border-radius:4px;overflow:hidden}
.card img{width:100%;height:180px;object-fit:cover;filter:grayscale(30%)}
.card h3,.card p{padding:0 1rem}.card p{color:#a3a3a3;font-size:.9rem;padding-bottom:1rem}
.gar-band{background:var(--gray);text-align:center;padding:1.5rem;border-top:1px solid #333;border-bottom:1px solid #333}
.gar-band p{margin:0;color:#d4d4d4;font-weight:500}
.gar-contact form{display:grid;gap:1rem;max-width:24rem}
.gar-contact label{display:grid;gap:.3rem;font-size:.9rem}
.gar-contact input,.gar-contact select{padding:.65rem;background:#262626;border:1px solid #404040;color:#fff;font:inherit;border-radius:0}
.ai-foot{text-align:center;padding:1.5rem;color:#737373;border-top:1px solid #333}
"""
    write_ai_site(slug, "Garage Central Plappeville — Mécanique Metz | démo",
                  "Garage automobile à Plappeville : entretien, diagnostic et carrosserie.",
                  body, css, layout="angular-garage")
    return slug


def site_immobilier() -> str:
    slug = "immobilier"
    body = """
<header class="immo-head"><a href="#" class="immo-logo">Patrimoine Lorraine</a>
<nav><a href="#biens">Biens</a><a href="#expertise">Expertise</a><a href="#estimation">Estimation</a></nav></header>
<main id="contenu">
  <section class="immo-hero">
    <div class="immo-hero-content">
      <h1>Votre patrimoine mérite une attention d'exception</h1>
      <p class="lead">Achat, vente et gestion locative en Moselle, Meurthe-et-Moselle et Luxembourg.</p>
      <form class="immo-search" action="#biens">
        <select><option>Acheter</option><option>Louer</option><option>Vendre</option></select>
        <input type="text" placeholder="Ville ou code postal" aria-label="Localisation">
        <button type="submit">Rechercher</button>
      </form>
    </div>
    <figure><img src="images/hero.png" alt="Maison de maître Metz" fetchpriority="high"></figure>
  </section>
  <section class="immo-kpi"><div><b>186</b> biens en portefeuille</div><div><b>28 j</b> délai vente moyen</div><div><b>97 %</b> clients satisfaits</div></section>
  <section id="biens" class="immo-sec">
    <h2>Sélection du moment</h2>
    <div class="immo-list">""" + _cards(slug, [
        ("Maison de maître — Metz Sablon", "280 m², jardin 800 m², rénovée 2024. 685 000 €", "Maison Metz"),
        ("Appartement haussmannien — Nancy", "4 pièces, parquet, vue parc. 395 000 €", "Appartement Nancy"),
        ("Terrain constructible — Thionville", "Lotissement calme, viabilisé. 145 000 €", "Terrain Thionville"),
    ]) + """
    </div>
  </section>
  <section id="expertise" class="immo-sec immo-sec--sage">
    <div class="immo-cols">
      <div><h2>Notre expertise locale</h2><p>15 ans sur le marché Grand Est. Nous connaissons chaque quartier, chaque fiscalité locale.</p></div>
      <ul><li>Estimation gratuite sous 72 h</li><li>Home staging partenaire</li><li>Gestion locative clé en main</li><li>Accompagnement primo-accédants</li></ul>
    </div>
    <blockquote>« Vendu en 3 semaines, 4 % au-dessus de l'estimation initiale. » — Famille R., Metz</blockquote>
  </section>
  <section id="estimation" class="immo-sec">
    <h2>Estimation gratuite</h2>
    <form class="immo-form"><label>Adresse du bien <input type="text" required></label><label>Email <input type="email" required></label><button type="submit">Recevoir mon estimation</button></form>
  </section>
</main>"""
    css = """
:root{--sage:#6b8f71;--sage-d:#4a6b50;--sage-l:#e8f0e9;--warm:#f7f5f0}
body{margin:0;font-family:"Plus Jakarta Sans",system-ui,sans-serif;font-size:17px;color:#2d3a2f;background:var(--warm)}
.immo-head{display:flex;justify-content:space-between;align-items:center;padding:1rem 1.5rem;background:#fff;box-shadow:0 1px 0 #d4e0d6;position:sticky;top:0;z-index:40}
.immo-logo{font-weight:700;color:var(--sage-d);text-decoration:none;font-size:1.1rem}
.immo-head a{margin-left:1rem;color:#5a6b5c;text-decoration:none;font-weight:500}
.immo-hero{display:grid;background:var(--sage-l)}
@media(min-width:900px){.immo-hero{grid-template-columns:1fr 1fr;min-height:480px}}
.immo-hero-content{padding:3rem 1.5rem;display:flex;flex-direction:column;justify-content:center}
.immo-hero h1{font-size:clamp(1.8rem,4vw,2.5rem);line-height:1.2;color:var(--sage-d);max-width:20ch}
.lead{color:#5a6b5c;margin-bottom:1.5rem;max-width:45ch}
.immo-search{display:flex;flex-wrap:wrap;gap:.5rem}
.immo-search select,.immo-search input{padding:.7rem 1rem;border:1px solid #b8cdb9;border-radius:.5rem;font:inherit;flex:1;min-width:140px}
.immo-search button{min-height:44px;padding:.7rem 1.5rem;background:var(--sage);color:#fff;border:none;border-radius:.5rem;font-weight:600;cursor:pointer}
.immo-hero figure{margin:0}.immo-hero img{width:100%;height:100%;min-height:280px;object-fit:cover}
.immo-kpi{display:flex;justify-content:center;flex-wrap:wrap;gap:2rem;padding:1.5rem;background:var(--sage-d);color:#fff}
.immo-kpi b{font-size:1.5rem;margin-right:.25rem}
.immo-sec{max-width:72rem;margin:0 auto;padding:4rem 1.5rem}
.immo-sec h2{color:var(--sage-d);margin-bottom:1.5rem}
.immo-list{display:grid;gap:1.5rem}
@media(min-width:768px){.immo-list{grid-template-columns:repeat(3,1fr)}}
.card{background:#fff;border-radius:.75rem;overflow:hidden;box-shadow:0 4px 20px rgba(74,107,80,.1)}
.card img{width:100%;height:200px;object-fit:cover}
.card h3{font-size:1rem;margin:1rem 1rem .25rem;color:var(--sage-d)}.card p{padding:0 1rem 1rem;color:#5a6b5c;font-size:.9rem;margin:0}
.immo-sec--sage{background:var(--sage-l)}
.immo-cols{display:grid;gap:2rem;margin-bottom:2rem}
@media(min-width:700px){.immo-cols{grid-template-columns:1fr 1fr}}
.immo-cols ul{margin:0;padding-left:1.2rem;line-height:2;color:#4a5c4d}
blockquote{background:#fff;padding:1.25rem 1.5rem;border-radius:.5rem;border-left:4px solid var(--sage);margin:0;font-style:italic;color:#4a5c4d}
.immo-form{display:grid;gap:1rem;max-width:26rem}
.immo-form label{display:grid;gap:.35rem;font-weight:500}
.immo-form input{padding:.65rem;border:1px solid #b8cdb9;border-radius:.5rem;font:inherit}
.immo-form button{min-height:44px;background:var(--sage);color:#fff;border:none;border-radius:.5rem;font-weight:600;cursor:pointer}
.ai-foot{text-align:center;padding:1.5rem;color:#7a8b7c}
"""
    write_ai_site(slug, "Patrimoine Lorraine — Immobilier Grand Est | démo",
                  "Agence immobilière Moselle : achat, vente et gestion locative.",
                  body, css, layout="search-hero-sage")
    return slug


def site_juridique() -> str:
    slug = "juridique"
    body = """
<header class="law-top"><div class="law-inner"><span class="law-name">Rivière &amp; Partenaires</span>
<nav><a href="#domaines">Domaines</a><a href="#cabinet">Cabinet</a><a href="#consultation">Consultation</a></nav></div></header>
<main id="contenu">
  <section class="law-hero">
    <div class="law-hero-grid">
      <div><p class="law-eyebrow">Avocats · Barreau de Metz</p>
      <h1>Le droit des affaires, sans distance</h1>
      <p>Conseil et contentieux pour PME, dirigeants et particuliers exigeants en Lorraine.</p>
      <a href="#consultation" class="law-btn">Prendre rendez-vous</a></div>
      <figure><img src="images/hero.png" alt="Cabinet Rivière Metz"></figure>
    </div>
  </section>
  <section class="law-stats"><div><span>22</span> ans d'expérience</div><div><span>6</span> associés</div><div><span>850+</span> dossiers / an</div></section>
  <section id="domaines" class="law-sec">
    <h2>Nos domaines d'intervention</h2>
    <div class="law-cols">
      <article><h3>Droit des sociétés</h3><p>Création, cession, pactes d'associés, gouvernance.</p></article>
      <article><h3>Contentieux commercial</h3><p>Recouvrement, rupture contractuelle, arbitrage.</p></article>
      <article><h3>Droit social</h3><p>Licenciement, négociation collective, conformité RH.</p></article>
    </div>
    <div class="law-cards">""" + _cards(slug, [
        ("Transmission d'entreprise", "Accompagnement vendeurs et repreneurs en Moselle.", "Transmission entreprise"),
        ("Immobilier d'affaires", "Baux commerciaux, baux emphytéotiques, contentieux locatif.", "Immobilier affaires"),
        ("Famille &amp; patrimoine", "Divorce, succession, donation-partage.", "Droit famille"),
    ]) + """
    </div>
  </section>
  <section id="cabinet" class="law-sec law-dark">
    <h2>Un cabinet ancré localement</h2>
    <p>Installés avenue Foch à Metz depuis 2003. Nous privilégions l'écoute, la réactivité et la transparence tarifaire — forfaits ou honoraires au temps passé, toujours validés par écrit.</p>
    <p class="law-trust">« Une équipe rigoureuse qui a défendu nos intérêts lors d'une acquisition complexe. » — Directeur financier, PME tertiaire</p>
  </section>
  <section id="consultation" class="law-sec">
    <h2>Demande de consultation</h2>
    <form class="law-form"><label>Nom <input type="text" required></label><label>Domaine <select><option>Sociétés</option><option>Contentieux</option><option>Social</option><option>Famille</option></select></label><label>Email <input type="email" required></label><button type="submit" class="law-btn">Envoyer</button></form>
  </section>
</main>"""
    css = """
:root{--gold:#c9a227;--black:#0f0f0f;--cream:#faf8f4}
body{margin:0;font-family:"Plus Jakarta Sans",Georgia,serif;font-size:17px;color:var(--black);background:var(--cream)}
.law-top{background:var(--black);color:#fff;position:sticky;top:0;z-index:50}
.law-inner{max-width:72rem;margin:0 auto;padding:1rem 1.5rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem}
.law-name{font-weight:600;letter-spacing:.06em;font-size:1.05rem}
.law-top a{color:rgba(255,255,255,.8);text-decoration:none;margin-left:1.25rem;font-size:.9rem}
.law-hero{padding:4rem 1.5rem;background:linear-gradient(180deg,#1a1a1a,var(--black));color:#fff}
.law-hero-grid{max-width:72rem;margin:0 auto;display:grid;gap:2rem;align-items:center}
@media(min-width:900px){.law-hero-grid{grid-template-columns:1fr 1fr}}
.law-eyebrow{color:var(--gold);font-size:.8rem;text-transform:uppercase;letter-spacing:.12em}
.law-hero h1{font-size:clamp(2rem,4vw,2.6rem);font-weight:400;margin:.75rem 0;max-width:18ch;line-height:1.2}
.law-hero p{opacity:.85;max-width:45ch;margin-bottom:1.5rem}
.law-btn{display:inline-flex;align-items:center;min-height:44px;padding:.75rem 1.75rem;background:var(--gold);color:var(--black);text-decoration:none;font-weight:600;border:none;cursor:pointer;font:inherit}
.law-hero img{width:100%;border-radius:2px;max-height:340px;object-fit:cover;border:1px solid rgba(201,162,39,.3)}
.law-stats{display:flex;justify-content:center;flex-wrap:wrap;gap:2.5rem;padding:2rem;background:var(--gold);color:var(--black);font-weight:600}
.law-stats span{display:block;font-size:2rem;font-weight:800}
.law-sec{max-width:72rem;margin:0 auto;padding:4rem 1.5rem}
.law-sec h2{font-weight:400;font-size:clamp(1.5rem,3vw,2rem);margin-bottom:1.5rem;border-bottom:1px solid #e8e0d0;padding-bottom:.75rem}
.law-cols{display:grid;gap:1.5rem;margin-bottom:3rem}
@media(min-width:700px){.law-cols{grid-template-columns:repeat(3,1fr)}}
.law-cols article{border-top:3px solid var(--gold);padding-top:1rem}
.law-cols h3{font-size:1rem;margin:0 0 .5rem}.law-cols p{color:#5c5346;font-size:.95rem;margin:0}
.law-cards{display:grid;gap:1.25rem}
@media(min-width:768px){.law-cards{grid-template-columns:repeat(3,1fr)}}
.card{background:#fff;border:1px solid #e8e0d0}.card img{width:100%;height:180px;object-fit:cover;filter:sepia(15%)}
.card h3,.card p{padding:0 1rem}.card p{color:#5c5346;font-size:.9rem;padding-bottom:1rem}
.law-dark{background:var(--black);color:#fff;max-width:none}
.law-dark .law-sec,.law-dark{max-width:none;padding:4rem 1.5rem}
.law-dark h2,.law-dark p{max-width:65ch;margin-inline:auto;text-align:center;border:none}
.law-trust{margin-top:2rem;font-style:italic;color:var(--gold)}
.law-form{display:grid;gap:1rem;max-width:24rem}
.law-form label{display:grid;gap:.3rem;font-size:.9rem}
.law-form input,.law-form select{padding:.65rem;border:1px solid #d4c9b0;font:inherit;background:#fff}
.ai-foot{text-align:center;padding:1.5rem;color:#8a7d6b}
"""
    write_ai_site(slug, "Rivière & Partenaires — Avocats Metz | démo",
                  "Cabinet d'avocats à Metz : droit des affaires, social et contentieux.",
                  body, css, layout="gold-law-columns")
    return slug


def site_architecture() -> str:
    slug = "architecture"
    body = """
<header class="arc-bar"><a href="#" class="arc-logo">Atelier Nord-Est</a>
<span class="arc-meta">Architecture · Metz · Nancy</span></header>
<main id="contenu">
  <section class="arc-hero">
    <h1>Formes<br>utiles.</h1>
    <p class="arc-sub">Réhabilitation, extension et conception neuve — sobriété matérielle, exigence spatiale.</p>
    <figure class="arc-hero-img"><img src="images/hero.png" alt="Projet Atelier Nord-Est" fetchpriority="high"></figure>
  </section>
  <section class="arc-stats"><div>48 <small>projets livrés</small></div><div>12 <small>architectes</small></div><div>3 <small>prix régionaux</small></div></section>
  <section id="projets" class="arc-sec">
    <h2>Projets récents</h2>
    <div class="arc-mag">""" + _cards(slug, [
        ("Maison L — Metz Queuleu", "Extension bois sur bâtisse 1930, label Bâtiment Durable.", "Maison L Metz"),
        ("Médiathèque de Thionville", "Concours public — lumière zénithale et acoustique.", "Médiathèque Thionville"),
        ("Bureaux Verdun", "Réhabilitation caserne — 2 400 m² tertiaires.", "Bureaux Verdun"),
    ]) + """
    </div>
  </section>
  <section class="arc-approach">
    <div class="arc-line"></div>
    <h2>Notre approche</h2>
    <p>Nous travaillons la matière, la lumière et le contexte lorraine. Chaque projet commence par une écoute du lieu — pas par un style imposé.</p>
    <ul><li>Diagnostic patrimonial</li><li>Maquette numérique 3D</li><li>Suivi de chantier</li></ul>
  </section>
  <section id="contact" class="arc-sec arc-contact">
    <h2>Discuter d'un projet</h2>
    <form><label>Nom <input type="text"></label><label>Type <select><option>Réhabilitation</option><option>Extension</option><option>Neuf</option></select></label><label>Email <input type="email" required></label><button type="submit">Envoyer</button></form>
  </section>
</main>"""
    css = """
:root{--black:#111;--white:#fafafa;--gray:#888}
body{margin:0;font-family:"Plus Jakarta Sans",system-ui,sans-serif;font-size:17px;color:var(--black);background:var(--white)}
.arc-bar{display:flex;justify-content:space-between;align-items:baseline;padding:1.5rem 2rem;border-bottom:1px solid #e5e5e5;position:sticky;top:0;background:var(--white);z-index:40}
.arc-logo{font-weight:800;text-decoration:none;color:var(--black);font-size:1rem;letter-spacing:-.02em}
.arc-meta{font-size:.75rem;color:var(--gray);text-transform:uppercase;letter-spacing:.15em}
.arc-hero{padding:clamp(3rem,10vw,7rem) 2rem 2rem;max-width:72rem;margin:0 auto}
.arc-hero h1{font-size:clamp(3.5rem,12vw,7rem);font-weight:800;line-height:.9;margin:0;letter-spacing:-.04em}
.arc-sub{font-size:1.15rem;color:var(--gray);max-width:32ch;margin:1.5rem 0 3rem}
.arc-hero-img{margin:0}.arc-hero-img img{width:100%;max-height:520px;object-fit:cover;display:block}
.arc-stats{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid #e5e5e5;border-bottom:1px solid #e5e5e5;text-align:center;padding:2rem 1rem}
.arc-stats div{font-size:2.5rem;font-weight:800}.arc-stats small{display:block;font-size:.7rem;font-weight:500;color:var(--gray);text-transform:uppercase;letter-spacing:.1em;margin-top:.25rem}
.arc-sec{max-width:72rem;margin:0 auto;padding:5rem 2rem}
.arc-sec h2{font-size:.8rem;text-transform:uppercase;letter-spacing:.2em;font-weight:600;margin-bottom:2rem}
.arc-mag{display:grid;gap:2rem}
@media(min-width:900px){.arc-mag{grid-template-columns:1.2fr .8fr .8fr}.arc-mag .card:first-child{grid-row:span 2}.arc-mag .card:first-child img{height:100%;min-height:400px}}
.card{margin:0}.card img{width:100%;height:240px;object-fit:cover;display:block}
.card h3{font-size:.95rem;font-weight:600;margin:1rem 0 .25rem}.card p{font-size:.85rem;color:var(--gray);margin:0 0 1rem}
.arc-approach{padding:5rem 2rem;max-width:40rem;margin:0 auto;text-align:center}
.arc-line{width:40px;height:1px;background:var(--black);margin:0 auto 2rem}
.arc-approach h2{font-size:1.5rem;text-transform:none;letter-spacing:0;font-weight:600}
.arc-approach p{color:var(--gray);line-height:1.7}
.arc-approach ul{list-style:none;padding:0;display:flex;justify-content:center;gap:2rem;flex-wrap:wrap;margin-top:2rem;font-size:.85rem;text-transform:uppercase;letter-spacing:.08em}
.arc-contact{border-top:1px solid #e5e5e5}
.arc-contact form{display:grid;gap:1rem;max-width:20rem}
.arc-contact label{display:grid;gap:.3rem;font-size:.8rem;text-transform:uppercase;letter-spacing:.05em}
.arc-contact input,.arc-contact select{padding:.6rem 0;border:none;border-bottom:1px solid #ccc;font:inherit;background:transparent}
.arc-contact button{margin-top:1rem;min-height:44px;background:var(--black);color:#fff;border:none;padding:.75rem 2rem;font:inherit;cursor:pointer}
.ai-foot{text-align:center;padding:2rem;color:var(--gray);font-size:.8rem}
"""
    write_ai_site(slug, "Atelier Nord-Est — Architecture Lorraine | démo",
                  "Agence d'architecture à Metz : réhabilitation, extension et neuf.",
                  body, css, layout="magazine-minimal")
    return slug


def site_fitness() -> str:
    slug = "fitness"
    body = """
<header class="pf-nav"><span class="pf-logo">PULSE<span>FITNESS</span></span>
<nav><a href="#cours">Cours</a><a href="#planning">Planning</a><a href="#essai">Essai</a></nav></header>
<main id="contenu">
  <section class="pf-hero">
    <div class="pf-hero-left">
      <p class="pf-tag">Metz · Sablon</p>
      <h1>DÉPASSEZ<br>VOS LIMITES</h1>
      <p>Cross-training, cycling et yoga — 1 200 m², coachs certifiés, ouvert 6h–23h.</p>
      <a href="#essai" class="pf-cta">Séance découverte gratuite</a>
    </div>
    <div class="pf-hero-right"><img src="images/hero.png" alt="Salle Pulse Fitness Metz"></div>
  </section>
  <section class="pf-stats"><div><b>1 200</b> m²</div><div><b>45</b> cours / semaine</div><div><b>6h–23h</b> ouvert</div></section>
  <section id="cours" class="pf-sec">
    <h2>Nos disciplines</h2>
    <div class="pf-cards">""" + _cards(slug, [
        ("HIIT &amp; Cross", "Fractionné haute intensité — 45 min, tous niveaux.", "Cours HIIT"),
        ("Cycling", "Studio immersive, playlists live, 30 ou 50 min.", "Cours cycling"),
        ("Yoga Flow", "Mobilité et récupération — matin et soir.", "Cours yoga"),
    ]) + """
    </div>
  </section>
  <section id="planning" class="pf-sec pf-dark">
    <h2>Planning de la semaine</h2>
    <table class="pf-table"><thead><tr><th></th><th>Lun</th><th>Mar</th><th>Mer</th><th>Jeu</th><th>Ven</th></tr></thead>
    <tbody><tr><td>6h30</td><td>Yoga</td><td>—</td><td>HIIT</td><td>—</td><td>Cycling</td></tr>
    <tr><td>12h15</td><td>—</td><td>Cross</td><td>—</td><td>Cross</td><td>—</td></tr>
    <tr><td>19h00</td><td>Cycling</td><td>HIIT</td><td>Yoga</td><td>HIIT</td><td>Cross</td></tr></tbody></table>
    <p class="pf-quote">« L'ambiance est incroyable, j'ai perdu 8 kg en 4 mois sans m'ennuyer. » — Julie, membre depuis 2024</p>
  </section>
  <section id="essai" class="pf-sec">
    <h2>Réserver mon essai</h2>
    <form class="pf-form"><label>Prénom <input type="text" required></label><label>Téléphone <input type="tel" required></label><label>Cours souhaité <select><option>HIIT</option><option>Cycling</option><option>Yoga</option></select></label><button type="submit" class="pf-cta">Je réserve</button></form>
  </section>
</main>"""
    css = """
:root{--lime:#84cc16;--lime-d:#65a30d;--black:#0a0a0a}
body{margin:0;font-family:"Plus Jakarta Sans",system-ui,sans-serif;font-size:17px;background:var(--black);color:#fff}
.pf-nav{display:flex;justify-content:space-between;align-items:center;padding:1rem 1.5rem;border-bottom:2px solid var(--lime);position:sticky;top:0;background:rgba(10,10,10,.95);z-index:40}
.pf-logo{font-weight:900;font-size:1.3rem;letter-spacing:.05em}.pf-logo span{color:var(--lime)}
.pf-nav a{color:#a3a3a3;text-decoration:none;margin-left:1rem;font-weight:600;font-size:.85rem;text-transform:uppercase}
.pf-hero{display:grid;min-height:440px}
@media(min-width:900px){.pf-hero{grid-template-columns:1fr 1fr}}
.pf-hero-left{padding:3rem 1.5rem;display:flex;flex-direction:column;justify-content:center}
.pf-tag{color:var(--lime);font-weight:700;font-size:.8rem;text-transform:uppercase;letter-spacing:.1em}
.pf-hero h1{font-size:clamp(2.5rem,7vw,4.5rem);line-height:.95;margin:1rem 0;font-weight:900;font-style:italic}
.pf-hero-left p{color:#a3a3a3;max-width:38ch;margin-bottom:1.5rem}
.pf-cta{display:inline-flex;align-items:center;min-height:44px;padding:.85rem 2rem;background:var(--lime);color:var(--black);text-decoration:none;font-weight:800;text-transform:uppercase;border:none;cursor:pointer;transform:skewX(-6deg)}
.pf-hero-right img{width:100%;height:100%;min-height:280px;object-fit:cover;filter:contrast(1.1)}
.pf-stats{display:flex;justify-content:center;flex-wrap:wrap;gap:2rem;padding:1.25rem;background:var(--lime);color:var(--black);font-weight:800;text-transform:uppercase;font-size:.9rem}
.pf-stats b{font-size:1.5rem;margin-right:.25rem}
.pf-sec{max-width:72rem;margin:0 auto;padding:4rem 1.5rem}
.pf-sec h2{text-transform:uppercase;letter-spacing:.08em;font-size:1.1rem;margin-bottom:2rem;color:var(--lime)}
.pf-cards{display:grid;gap:1.25rem}
@media(min-width:768px){.pf-cards{grid-template-columns:repeat(3,1fr)}}
.card{background:#171717;border:1px solid #333;overflow:hidden}
.card img{width:100%;height:200px;object-fit:cover}
.card h3,.card p{padding:0 1rem}.card h3{margin-top:1rem}.card p{color:#a3a3a3;font-size:.9rem;padding-bottom:1rem}
.pf-dark{background:#111;max-width:none;padding:4rem 1.5rem}
.pf-table{width:100%;border-collapse:collapse;font-size:.85rem;margin-bottom:2rem}
.pf-table th,.pf-table td{padding:.6rem;border:1px solid #333;text-align:center}
.pf-table th{background:var(--lime);color:var(--black)}
.pf-quote{text-align:center;font-style:italic;color:#a3a3a3;max-width:45ch;margin:0 auto}
.pf-form{display:grid;gap:1rem;max-width:22rem}
.pf-form label{display:grid;gap:.3rem;font-size:.85rem;text-transform:uppercase;font-weight:600}
.pf-form input,.pf-form select{padding:.65rem;background:#171717;border:1px solid #333;color:#fff;font:inherit}
.ai-foot{text-align:center;padding:1.5rem;color:#525252;border-top:1px solid #222}
"""
    write_ai_site(slug, "Pulse Fitness Metz — Salle de sport | démo",
                  "Salle de sport à Metz : cross-training, cycling, yoga — essai gratuit.",
                  body, css, layout="energetic-schedule")
    return slug


def site_photographie() -> str:
    slug = "photographie"
    body = """
<header class="ph-nav"><a href="#" class="ph-brand">Studio Lumière Grise</a>
<nav><a href="#portfolio">Portfolio</a><a href="#services">Services</a><a href="#devis">Devis</a></nav></header>
<main id="contenu">
  <section class="ph-hero">
    <div class="ph-hero-text">
      <p class="ph-label">Photographie éditoriale · Metz</p>
      <h1>Capturer l'essentiel, dans la pénombre et la clarté.</h1>
      <a href="#portfolio" class="ph-link">Voir le portfolio →</a>
    </div>
    <figure class="ph-hero-frame"><img src="images/hero.png" alt="Portrait éditorial Studio Lumière Grise"></figure>
  </section>
  <section class="ph-band"><span>12 ans d'expérience</span><span>·</span><span>Publications Vogue Hommes, Les Inrocks</span><span>·</span><span>180+ clients</span></section>
  <section id="portfolio" class="ph-sec">
    <h2>Sélection</h2>
    <div class="ph-masonry">""" + _cards(slug, [
        ("Portrait corporate", "Dirigeants et équipes — lumière naturelle, retouches discrètes.", "Portrait corporate"),
        ("Mariage documentaire", "Reportage intimiste, noir et blanc et couleur.", "Mariage documentaire"),
        ("Architecture &amp; design", "Mise en valeur de volumes et matériaux.", "Photo architecture"),
    ]) + """
    </div>
  </section>
  <section id="services" class="ph-sec ph-services">
    <div class="ph-svc-grid">
      <article><h3>Portrait</h3><p>À partir de 350 € — studio ou sur site.</p></article>
      <article><h3>Événement</h3><p>Demi-journée ou journée — livraison sous 10 jours.</p></article>
      <article><h3>Éditorial</h3><p>Direction artistique et post-production incluse.</p></article>
    </div>
    <blockquote>« Des images qui racontent notre marque sans effet superflu. » — Agence K., Nancy</blockquote>
  </section>
  <section id="devis" class="ph-sec ph-contact">
    <h2>Demande de devis</h2>
    <form><label>Nom <input type="text" required></label><label>Type de projet <select><option>Portrait</option><option>Mariage</option><option>Corporate</option><option>Éditorial</option></select></label><label>Email <input type="email" required></label><button type="submit">Envoyer</button></form>
  </section>
</main>"""
    css = """
:root{--gray:#6b7280;--gray-d:#374151;--gray-l:#f3f4f6;--accent:#9ca3af}
body{margin:0;font-family:"Plus Jakarta Sans",system-ui,sans-serif;font-size:17px;color:var(--gray-d);background:#fff}
.ph-nav{display:flex;justify-content:space-between;align-items:center;padding:1.25rem 2rem;border-bottom:1px solid #e5e7eb;position:sticky;top:0;background:rgba(255,255,255,.97);z-index:40}
.ph-brand{font-weight:600;color:var(--gray-d);text-decoration:none;letter-spacing:.02em}
.ph-nav a{margin-left:1.5rem;color:var(--gray);text-decoration:none;font-size:.9rem}
.ph-hero{display:grid;gap:2rem;padding:3rem 2rem;max-width:72rem;margin:0 auto;align-items:center}
@media(min-width:900px){.ph-hero{grid-template-columns:1fr 1.1fr;min-height:70vh}}
.ph-label{font-size:.75rem;text-transform:uppercase;letter-spacing:.2em;color:var(--gray)}
.ph-hero h1{font-size:clamp(1.8rem,4vw,2.8rem);font-weight:400;line-height:1.3;margin:1rem 0 1.5rem;max-width:22ch;color:var(--gray-d)}
.ph-link{color:var(--gray-d);text-decoration:none;border-bottom:1px solid var(--gray-d);padding-bottom:2px;font-size:.95rem}
.ph-hero-frame{margin:0}.ph-hero-frame img{width:100%;max-height:560px;object-fit:cover;display:block;filter:grayscale(40%)}
.ph-band{display:flex;justify-content:center;flex-wrap:wrap;gap:.75rem;padding:1rem 1.5rem;background:var(--gray-l);color:var(--gray);font-size:.85rem}
.ph-sec{max-width:72rem;margin:0 auto;padding:4rem 2rem}
.ph-sec h2{font-size:.75rem;text-transform:uppercase;letter-spacing:.25em;color:var(--gray);margin-bottom:2rem;font-weight:500}
.ph-masonry{display:grid;gap:1.5rem}
@media(min-width:768px){.ph-masonry{grid-template-columns:repeat(3,1fr)}.ph-masonry .card:nth-child(2){margin-top:2rem}}
.card{margin:0}.card img{width:100%;height:280px;object-fit:cover;display:block;filter:grayscale(50%)}
.card h3{font-weight:500;font-size:1rem;margin:1rem 0 .35rem}.card p{font-size:.9rem;color:var(--gray);margin:0 0 1rem;line-height:1.5}
.ph-services{background:var(--gray-l)}
.ph-svc-grid{display:grid;gap:1.5rem;margin-bottom:2rem}
@media(min-width:700px){.ph-svc-grid{grid-template-columns:repeat(3,1fr)}}
.ph-svc-grid article{background:#fff;padding:1.5rem;border-left:2px solid var(--gray)}
.ph-svc-grid h3{margin:0 0 .5rem;font-weight:500}.ph-svc-grid p{margin:0;color:var(--gray);font-size:.9rem}
blockquote{font-style:italic;color:var(--gray);border:none;margin:0;padding:0;text-align:center;max-width:40ch;margin-inline:auto}
.ph-contact form{display:grid;gap:1rem;max-width:22rem}
.ph-contact label{display:grid;gap:.35rem;font-size:.85rem;color:var(--gray)}
.ph-contact input,.ph-contact select{padding:.6rem 0;border:none;border-bottom:1px solid #d1d5db;font:inherit;background:transparent}
.ph-contact button{margin-top:.5rem;min-height:44px;background:var(--gray-d);color:#fff;border:none;padding:.75rem 1.5rem;font:inherit;cursor:pointer}
.ai-foot{text-align:center;padding:2rem;color:var(--gray);font-size:.85rem}
"""
    write_ai_site(slug, "Studio Lumière Grise — Photo éditoriale Metz | démo",
                  "Photographe éditorial à Metz : portrait, mariage et corporate.",
                  body, css, layout="editorial-masonry")
    return slug


def run() -> list[str]:
    builders = [
        site_education,
        site_services,
        site_etablissement,
        site_automobile,
        site_immobilier,
        site_juridique,
        site_architecture,
        site_fitness,
        site_photographie,
    ]
    ok: list[str] = []
    for fn in builders:
        slug = fn()
        ok.append(slug)
        print(f"OK {slug}")
    return ok


if __name__ == "__main__":
    slugs = run()
    print(f"\n{len(slugs)} vitrines écrites : {', '.join(slugs)}")
