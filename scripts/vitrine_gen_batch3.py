# Batch 3: architecture, fitness, photographie, technologie, restauration
from vitrine_gen_lib import fig, write_demo

HUB = '<p class="hub-back"><a href="../index.html">← Hub vitrines</a></p>'
SWIPER = """  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css">
  <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>"""
AOS = """  <link href="https://unpkg.com/aos@2.3.4/dist/aos.css" rel="stylesheet">
  <script src="https://unpkg.com/aos@2.3.4/dist/aos.js"></script>"""


def run_batch3():
    gen_architecture()
    gen_fitness()
    gen_photographie()
    gen_technologie()
    gen_restauration()


def gen_architecture():
    g = "arch"
    body = f"""
<header class="arch-bar"><a href="#projets">Projets</a><a href="#contact">Contact</a></header>
<main id="contenu">
  <section id="accueil" class="arch-intro vt-reveal"><h1>Atelier<br>Nord-Est</h1><p>Architecture · Metz</p></section>
  <section id="projets" class="arch-grid vt-reveal">
    <article class="arch-panel"><span class="arch-num">01</span>{fig(g,"projet-metz.svg","24 logements Metz",lazy=False)}<h3>Metz Queuleu</h3></article>
    <article class="arch-panel arch-panel--off"><span class="arch-num">02</span>{fig(g,"projet-lux.svg","Siège Luxembourg")}<h3>Luxembourg</h3></article>
    <article class="arch-panel"><span class="arch-num">03</span>{fig(g,"projet-verdun.svg","Réhab Verdun")}<h3>Verdun</h3></article>
    <article class="arch-panel arch-panel--off">{fig(g,"hero.svg","Façade contemporaine")}</article>
  </section>
  <section id="contact" class="vt-reveal arch-contact"><h2>Brief projet</h2><form><input placeholder="Nom"><button type="button">Envoyer (démo)</button></form>{HUB}</section>
</main>
"""
    css = """
body{margin:0;background:#f5f3ef;color:#0a0a0a;font-family:monospace}
.arch-bar{display:flex;justify-content:flex-end;gap:2rem;padding:1.5rem;border-bottom:3px solid #0a0a0a}
.arch-intro{padding:4rem 1.5rem}
.arch-intro h1{font-size:clamp(3rem,10vw,7rem);line-height:.9;margin:0}
.arch-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:1rem;padding:1rem}
.arch-panel{position:relative;padding:1rem;border:2px solid #0a0a0a;transition:.25s}
.arch-panel--off{transform:translate(12px,12px);background:#0a0a0a;color:#f5f3ef}
.arch-panel:hover{filter:invert(1)}
.arch-num{font-size:4rem;font-weight:900;opacity:.2;position:absolute;top:0;right:1rem}
.arch-panel img{width:100%;height:220px;object-fit:cover}
.arch-contact{padding:3rem 1.5rem;border-top:3px solid #0a0a0a}
"""
    write_demo("architecture", "brutalist-grid", "pico", "Atelier Nord-Est — Architecture",
               "Architecture contemporaine à Metz.", body, css)


def gen_fitness():
    g = "fit"
    body = f"""
<div data-theme="dark" class="fit-page">
<header class="fit-hero vt-reveal">
  <h1>Pulse Fitness</h1><p>Thionville · 24/7</p>
  <ul class="fit-stats"><li><strong>1200</strong> m²</li><li><strong>45</strong> cours/sem</li><li><strong>8</strong> coachs</li></ul>
  <div class="carousel w-full max-w-lg">
    <div id="fitCar" class="carousel w-full rounded-box">
      <div class="carousel-item">{fig(g,"cours-hiit.svg","Cours HIIT",lazy=False)}</div>
      <div class="carousel-item">{fig(g,"cours-yoga.svg","Yoga Flow")}</motion>
      <div class="carousel-item">{fig(g,"cours-cycling.svg","Cycling")}</motion>
    </motion>
  </motion>
</header>
<section class="fit-schedule vt-reveal">
  <h2>Planning hebdo</h2>
  <table class="table table-zebra">
    <thead><tr><th></th><th>Lun</th><th>Mar</th><th>Mer</th><th>Jeu</th><th>Ven</th></tr></thead>
    <tbody>
      <tr><td>07h</td><td>HIIT</td><td>Yoga</td><td>—</td><td>HIIT</td><td>Cycling</td></tr>
      <tr><td>12h</td><td>—</td><td>HIIT</td><td>Yoga</td><td>—</td><td>HIIT</td></tr>
      <tr><td>19h</td><td>Cycling</td><td>—</td><td>HIIT</td><td>Yoga</td><td>—</td></tr>
    </tbody>
  </table>
</section>
<section class="vt-reveal">{fig(g,"hero.svg","Salle Pulse Fitness")}</section>
<footer>{HUB}</footer>
</div>
"""
    body = body.replace("<motion", "<div").replace("</motion>", "</div>")
    css = """
.fit-page{min-height:100vh;background:#0d0d0d;color:#39ff14;font-family:system-ui,sans-serif}
.fit-hero{padding:2rem;text-align:center}
.fit-stats{display:flex;justify-content:center;gap:2rem;list-style:none;padding:0}
.fit-stats strong{font-size:2rem;display:block}
.fit-schedule{padding:2rem 1rem;overflow-x:auto}
.fit-schedule table{min-width:600px}
.fit-schedule th{background:#39ff14;color:#000}
footer{padding:2rem;text-align:center}
"""
    write_demo("fitness", "schedule-wall", "daisy", "Pulse Fitness — Sport",
               "Salle de sport et cours collectifs à Thionville.", body, css)


def gen_photographie():
    g = "pho"
    body = f"""
<header class="pho-bar vt-reveal"><span class="pho-logo">Lumière du Nord</span><span>Metz · reportage &amp; portrait</span></header>
<section class="pho-film vt-reveal" aria-label="Filmstrip">
  <div class="pho-film-track">
    {fig(g,"hero.svg","Studio photo",lazy=False)}
    {fig(g,"portfolio-mariage.svg","Mariage")}
    {fig(g,"portfolio-portrait.svg","Portrait")}
    {fig(g,"portfolio-corporate.svg","Corporate")}
    {fig(g,"portfolio-reportage.svg","Reportage")}
    {fig(g,"portfolio-architecture.svg","Architecture photo")}
    {fig(g,"portfolio-mode.svg","Mode")}
  </motion>
</section>
<main id="contenu" class="pho-cols vt-reveal">
  <column class="pho-col pho-col--tall">{fig(g,"portfolio-mariage.svg","Mariage vertical")}</column>
  <column class="pho-col">{fig(g,"portfolio-portrait.svg","Portrait")}{fig(g,"portfolio-corporate.svg","Corporate")}</column>
  <column class="pho-col pho-col--mid">{fig(g,"portfolio-reportage.svg","Reportage")}{fig(g,"portfolio-mode.svg","Mode")}</column>
</main>
<footer>{HUB}</footer>
"""
    body = body.replace("<motion", "<motion").replace("</motion>", "</motion>")
    body = body.replace("<motion", "<div").replace("</motion>", "</div>")
    body = body.replace("<column", "<div").replace("</column>", "</div>")
    css = """
body{margin:0;background:#1a1816;color:#f5f0e8;font-family:Georgia,serif}
.pho-bar{display:flex;justify-content:space-between;padding:1rem 1.5rem;border-bottom:1px solid #c9a227}
.pho-logo{font-size:1.25rem;color:#c9a227}
.pho-film{overflow-x:auto;padding:1rem 0;border-bottom:1px solid #333}
.pho-film-track{display:flex;gap:.75rem;width:max-content;padding:0 1rem}
.pho-film-track figure{flex:0 0 280px}
.pho-film-track img{height:180px;width:280px;object-fit:cover;border:3px solid #c9a227}
.pho-cols{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;padding:2rem 1rem;align-items:start}
.pho-col{display:flex;flex-direction:column;gap:1rem}
.pho-col--tall img{min-height:420px}
.pho-col img{width:100%;object-fit:cover}
footer{padding:2rem;text-align:center;color:#c9a227}
"""
    write_demo("photographie", "filmstrip", "openprops", "Lumière du Nord — Photographie",
               "Photographe professionnel à Metz.", body, css)


def gen_technologie():
    g = "tech"
    body = f"""
<header class="tech-term vt-reveal" data-aos="fade-down">
  <div class="term-bar"><span>synapse@lorraine:~</span><span>cloud regional</span></div>
  <pre class="term-body"><code>$ deploy --region moselle-est
> Datacenter edge · API · Zero Trust
> Synapse IT · Thionville technopole</code></pre>
  {fig(g,"tech-datacenter.png","Datacenter régional",lazy=False)}
</header>
<main id="contenu">
  <div class="tabs is-centered tech-tabs vt-reveal" data-aos="fade-up">
    <ul><li class="is-active"><a data-tab="api">API</a></li><li><a data-tab="data">Data</a></li><li><a data-tab="secu">Sécurité</a></li></ul>
  </motion>
  <section id="api" class="tech-panel is-active vt-reveal">{fig(g,"tech-reseau.png","Réseau et API")}{fig(g,"card-1.svg","Microservices")}</section>
  <section id="data" class="tech-panel vt-reveal">{fig(g,"tech-equipe.png","Équipe data")}{fig(g,"card-2.svg","Data lake")}</section>
  <section id="secu" class="tech-panel vt-reveal">{fig(g,"card-3.svg","Zero Trust")}{fig(g,"hero.svg","Illustration sécurité")}</section>
  <button class="button is-primary tech-demo" data-target="modalDemo">Demander une démo</button>
</main>
<div id="modalDemo" class="modal"><motion class="modal-background"></motion><motion class="modal-content"><motion class="box"><h2>Démo Synapse</h2><p>Formulaire statique — Moselle.</p><button class="modal-close">Fermer</button></motion></motion></motion>
<footer>{HUB}</footer>
<script>AOS.init({{duration:600,once:true}});document.querySelectorAll('.tech-tabs a').forEach(a=>a.addEventListener('click',e=>{{e.preventDefault();document.querySelectorAll('.tech-panel,.tech-tabs li').forEach(x=>x.classList.remove('is-active'));a.parentElement.classList.add('is-active');document.getElementById(a.dataset.tab).classList.add('is-active')}}));document.querySelector('.tech-demo').onclick=()=>document.getElementById('modalDemo').classList.add('is-active');document.querySelector('.modal-close').onclick=()=>document.getElementById('modalDemo').classList.remove('is-active')</script>
"""
    body = body.replace("<motion", "<div").replace("</motion>", "</div>")
    css = """
body{margin:0;font-family:Consolas,monospace;background:#0d1b2a;color:#64b5f6}
.tech-term{padding:2rem;border-bottom:2px solid #7c4dff}
.term-bar{display:flex;justify-content:space-between;background:#1b263b;padding:.5rem 1rem;border-radius:8px 8px 0 0}
.term-body{background:#000;padding:1rem;margin:0;border-radius:0 0 8px 8px;color:#39ff14}
.tech-term img{width:100%;max-height:280px;object-fit:cover;margin-top:1rem;border-radius:8px}
.tech-panel{display:none;padding:1.5rem}
.tech-panel.is-active{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
.tech-panel img{width:100%;object-fit:cover;border-radius:8px}
.tech-demo{margin:1.5rem}
footer{padding:2rem;text-align:center}
"""
    write_demo("technologie", "terminal-product", "bulma", "Synapse IT — Technologie",
               "Cloud et cybersécurité en Lorraine.", body, css, extra=AOS)


def gen_restauration():
    g = "resto"
    body = f"""
<header class="resto-head vt-reveal"><h1>Auberge des Remparts</h1><p>Thionville · brasserie</p></header>
<main id="contenu" class="resto-book vt-reveal">
  <div class="resto-col">
    <h2>Entrées</h2>
    <dl><dt>Terrine maison</dt><dd>12 €</dd><dt>Œuf parfait</dt><dd>14 €</dd></dl>
    <h2>Plats</h2>
    <dl><dt>Entrecôte Moselle</dt><dd>28 €</dd><dt>Truite du canal</dt><dd>24 €</dd></dl>
  </motion>
  <div class="resto-col">
    <h2>Desserts</h2>
    <dl><dt>Clafoutis</dt><dd>9 €</dd></dl>
    {fig(g,"resto-chef.png","Chef en cuisine")}
  </motion>
</main>
<section class="vt-reveal">
  <div class="swiper vitrine-image-swiper resto-swiper">
    <div class="swiper-wrapper">
      <div class="swiper-slide">{fig(g,"resto-salle.png","Salle brasserie")}</div>
      <div class="swiper-slide">{fig(g,"resto-assiette.png","Assiette dressée")}</div>
      <div class="swiper-slide">{fig(g,"hero.svg","Illustration brasserie")}</div>
      <div class="swiper-slide">{fig(g,"card-1.svg","Carte du jour")}</div>
    </motion>
    <motion class="swiper-pagination"></motion>
    <motion class="swiper-button-prev"></motion><motion class="swiper-button-next"></motion>
  </motion>
</section>
<footer>{HUB}</footer>
"""
    body = body.replace("<motion", "<motion").replace("</motion>", "</motion>")
    body = body.replace("<motion", "<motion").replace("</motion>", "</motion>")
    body = body.replace("<motion", "<div").replace("</motion>", "</div>")
    css = """
body{margin:0;font-family:Georgia,serif;background:#fff8f0;color:#3d1414}
.resto-head{text-align:center;padding:2rem;background:#722f37;color:#e8c547}
.resto-book{display:grid;grid-template-columns:1fr 1fr;gap:3rem;max-width:900px;margin:2rem auto;padding:0 1.5rem;border:4px double #722f37}
.resto-col h2{color:#722f37;border-bottom:1px solid #c9a227}
.resto-col img{width:100%;border-radius:8px;object-fit:cover;margin-top:1rem}
.resto-swiper{padding:2rem 1rem}
footer{padding:2rem;text-align:center}
@media(max-width:700px){.resto-book{grid-template-columns:1fr}}
"""
    write_demo("restauration", "menu-livret", "bulma", "Auberge des Remparts — Restauration",
               "Brasserie et cuisine lorraine à Thionville.", body, css, extra=SWIPER)
