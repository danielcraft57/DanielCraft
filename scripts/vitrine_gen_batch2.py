# Batch 2: banque, etablissement, automobile, chocolatier, immobilier, juridique
from vitrine_gen_lib import fig, write_demo

HUB = '<p class="hub-back"><a href="../index.html">← Hub vitrines</a></p>'


def run_batch2():
    gen_banque()
    gen_etablissement()
    gen_automobile()
    gen_chocolatier()
    gen_immobilier()
    gen_juridique()


def gen_banque():
    g = "bnq"
    body = f"""
<header class="bnq-hero vt-reveal">
  <p>Verlaine Banque Régionale · Thionville</p>
  <h1>Votre banque<br>de territoire</h1>
  <ul class="bnq-trust"><li><strong>47</strong> agences Moselle</li><li><strong>4,9</strong> satisfaction</li><li><strong>100%</strong> coopérative</li></ul>
  {fig(g,"hero.png","Agence bancaire Verlaine",lazy=False)}
</header>
<nav class="bnq-tabs vt-reveal" role="tablist">
  <button type="button" class="active" data-tab="courant">Comptes</button>
  <button type="button" data-tab="epargne">Épargne</button>
  <button type="button" data-tab="pro">Pro</button>
</nav>
<main id="contenu">
  <section id="courant" class="bnq-panel vt-reveal active">
    <div class="bnq-cards">
      <article>{fig(g,"conseil.png","Conseiller en rendez-vous")}<h3>Essentiel</h3><p>Carte, appli, virement instantané</p></article>
      <article>{fig(g,"banque-poignee-main.png","Poignée de main client")}<h3>Jeunes</h3><p>0 € jusqu'à 26 ans</p></article>
    </div>
  </section>
  <section id="epargne" class="bnq-panel vt-reveal">
    {fig(g,"banque-infographic.png","Infographie épargne régionale")}
    <p>Livret Territoire +, assurance-vie locale.</p>
  </section>
  <section id="pro" class="bnq-panel vt-reveal">
    <motion class="bnq-cards">
      <article>{fig(g,"agences.png","Réseau d'agences")}<h3>Trésorerie Pro</h3></article>
      <article>{fig(g,"card-1.svg","Illustration crédit")}<h3>Prêt investissement</h3></article>
    </motion>
  </section>
  <section class="bnq-compare vt-reveal">
    <h2>Comparer nos offres</h2>
    <table><thead><tr><th></th><th>Essentiel</th><th>Premium</th></tr></thead>
    <tbody><tr><td>Frais carte</td><td>0 €</td><td>0 €</td></tr><tr><td>Conseiller dédié</td><td>—</td><td>Oui</td></tr></tbody></table>
  </section>
  <footer class="vt-reveal">{HUB}</footer>
</main>
<script>document.querySelectorAll('.bnq-tabs button').forEach(b=>b.addEventListener('click',()=>{{document.querySelectorAll('.bnq-tabs button,.bnq-panel').forEach(e=>e.classList.remove('active'));b.classList.add('active');document.getElementById(b.dataset.tab).classList.add('active')}}))</script>
"""
    body = body.replace("<motion", "<div").replace("</motion>", "</div>")
    css = """
body{margin:0;font-family:system-ui,sans-serif;background:#f8fafc;color:#0f172a}
.bnq-hero{padding:2rem 1.5rem;background:linear-gradient(135deg,#1e3a5f,#0f2744);color:#fff}
.bnq-trust{display:flex;gap:2rem;list-style:none;padding:0;flex-wrap:wrap}
.bnq-trust strong{font-size:1.5rem;color:#c9a227}
.bnq-hero img{width:100%;max-height:360px;object-fit:cover;border-radius:8px;margin-top:1rem}
.bnq-tabs{display:flex;gap:.5rem;padding:1rem 1.5rem;background:#fff;border-bottom:1px solid #e2e8f0;position:sticky;top:0}
.bnq-tabs button{border:0;background:#e2e8f0;padding:.5rem 1rem;border-radius:999px;cursor:pointer}
.bnq-tabs button.active{background:#1e3a5f;color:#fff}
.bnq-panel{display:none;padding:1.5rem}
.bnq-panel.active{display:block}
.bnq-cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1rem}
.bnq-cards img{width:100%;height:180px;object-fit:cover;border-radius:8px}
.bnq-compare{padding:2rem 1.5rem}
.bnq-compare table{width:100%;border-collapse:collapse}
.bnq-compare th,.bnq-compare td{border:1px solid #cbd5e1;padding:.75rem}
"""
    write_demo("banque", "agence-tabs", "tailwind", "Verlaine Banque — Banque",
               "Banque coopérative régionale en Moselle.", body, css)


def gen_etablissement():
    g = "etab"
    body = f"""
<main id="contenu" class="etab-snap">
  <section id="chambre" class="etab-chapter vt-reveal">
    <div class="etab-chapter__text"><p>Hôtel Stanislas · Nancy</p><h1>Chambres<br>signature</h1><p>Vue parc, literie hôtel 5* et check-in express.</p></div>
    {fig(g,"etab-chambre.png","Chambre deluxe Stanislas",lazy=False)}
  </section>
  <section id="spa" class="etab-chapter vt-reveal">
    {fig(g,"etab-lobby.png","Lobby spa et bien-être")}
    <div class="etab-chapter__text"><h2>Spa &amp; détente</h2><p>Hammam, piscine et soins Lorraine.</p></motion>
  </section>
  <section id="resto" class="etab-chapter vt-reveal">
    <div class="etab-chapter__text"><h2>Restaurant Terroir</h2><p>Cuisine moselle &amp; carte des vins locaux.</div>
    {fig(g,"etab-seminaire.png","Salle séminaire et restauration")}
  </section>
  <section class="etab-extra vt-reveal">
    {fig(g,"hero.svg","Illustration hôtel")}{fig(g,"card-1.svg","Illustration chambre")}{fig(g,"card-2.svg","Illustration spa")}{fig(g,"card-3.svg","Illustration resto")}
  </section>
  <footer class="etab-foot">{HUB}</footer>
</main>
"""
    body = body.replace("<motion", "<motion").replace("</motion>", "</motion>")
    body = body.replace("<motion", "<div").replace("</motion>", "</div>")
    css = """
html,body{margin:0;height:100%}
.etab-snap{height:100vh;overflow-y:scroll;scroll-snap-type:y mandatory}
.etab-chapter{min-height:100vh;scroll-snap-align:start;display:grid;grid-template-columns:1fr 1fr;align-items:center;background:#1a1410;color:#f5efe6}
.etab-chapter:nth-child(even){background:#2a221c}
.etab-chapter img{width:100%;height:100vh;object-fit:cover}
.etab-chapter__text{padding:clamp(2rem,5vw,4rem)}
.etab-extra{display:grid;grid-template-columns:repeat(4,1fr);gap:.5rem;padding:1rem;scroll-snap-align:start}
.etab-extra img{height:200px;object-fit:cover;width:100%}
.etab-foot{padding:2rem;text-align:center;background:#1a1410;color:#c9a227}
@media(max-width:800px){.etab-chapter{grid-template-columns:1fr}.etab-chapter img{height:50vh}}
"""
    write_demo("etablissement", "hotel-chapters", "pico", "Hôtel Stanislas — Hébergement",
               "Hôtel 4* à Nancy, chambres spa et restauration.", body, css)


def gen_automobile():
    g = "auto"
    body = f"""
<div data-theme="dark" class="auto-page">
<header class="auto-head vt-reveal"><h1>Garage Central</h1><p>Plappeville · Moselle</p></header>
<section class="auto-stats vt-reveal">
  <div class="radial-progress" style="--value:88" role="progressbar">88% satisfaction</motion>
  <div class="radial-progress" style="--value:72" role="progressbar">72% atelier occupé</motion>
  <motion class="countdown" id="promo"><span data-days>00</span>j <span data-h>00</span>h promo pneus</motion>
</section>
<section class="vt-reveal carousel w-full">
  <div id="autoCar" class="carousel w-full">
    <div class="carousel-item">{fig(g,"auto-mecanique.png","Mécanicien en atelier",lazy=False)}</div>
    <motion class="carousel-item">{fig(g,"auto-pont.png","Pont élévateur garage")}</motion>
    <motion class="carousel-item">{fig(g,"auto-pneus.png","Montage pneus hiver")}</motion>
  </motion>
</section>
<section class="auto-grid vt-reveal">
  {fig(g,"hero.svg","Illustration garage")}{fig(g,"card-1.svg","Entretien")}{fig(g,"card-2.svg","Carrosserie")}{fig(g,"card-3.svg","Contrôle")}
</section>
<footer class="auto-foot">{HUB}</footer>
</div>
<script>
(function(){{var e=new Date();e.setDate(e.getDate()+((5+7-e.getDay())%7||7));function t(){{var n=e-new Date();document.querySelectorAll('#promo [data-days]').forEach(function(el){{el.textContent=String(Math.floor(n/864e5)).padStart(2,'0')}});document.querySelectorAll('#promo [data-h]').forEach(function(el){{el.textContent=String(Math.floor((n%864e5)/36e5)).padStart(2,'0')}})}};t();setInterval(t,36e5)}})();
</script>
"""
    body = body.replace("<motion", "<motion").replace("</motion>", "</motion>")
    body = body.replace("<motion", "<motion").replace("</motion>", "</motion>")
    body = body.replace("<motion", "<div").replace("</motion>", "</motion>")
    body = body.replace("</motion>", "</motion>")
    body = body.replace("</motion>", "</div>")
    css = """
.auto-page{min-height:100vh;background:#111;color:#e5e5e5;font-family:system-ui,sans-serif}
.auto-head{padding:2rem;text-align:center}
.auto-stats{display:flex;gap:2rem;justify-content:center;flex-wrap:wrap;padding:1rem}
.radial-progress{width:8rem;height:8rem;border-radius:50%;display:grid;place-items:center;background:conic-gradient(#f97316 calc(var(--value)*1%),#333 0)}
.countdown{font-size:1.25rem;color:#f97316}
.auto-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:.5rem;padding:1rem}
.auto-grid img{width:100%;height:160px;object-fit:cover}
.auto-foot{padding:2rem;text-align:center}
"""
    write_demo("automobile", "pit-dashboard", "daisy", "Garage Central — Automobile",
               "Garage multimarques à Plappeville, Moselle.", body, css)


def gen_chocolatier():
    g = "ch"
    body = f"""
<nav class="ch-nav"><a href="#timeline">Histoire</a><a href="#boutique">Boutique</a></nav>
<main id="contenu">
  <section id="timeline" class="ch-timeline vt-reveal">
    <h1 class="ch-title">Vialson · bean-to-bar</h1>
    <article class="ch-step"><div class="ch-step__txt"><h2>Grain</h2><p>Fèves Équateur &amp; Pérou — torréfaction Nancy.</p></div>{fig(g,"cacao-origines.png","Fèves de cacao",lazy=False)}</article>
    <article class="ch-step ch-step--flip"><motion class="ch-step__txt"><h2>Tablette</h2><p>Tempérage et moulage atelier Saint-Pierre.</p></motion>{fig(g,"atelier.png","Atelier de fabrication")}</article>
    <article class="ch-step">{fig(g,"produit-1.png","Tablette noir 72%")}<div class="ch-step__txt"><h2>Boutique</h2><p>Ganaches et coffrets entreprise.</p></div></article>
    <article class="ch-step ch-step--flip">{fig(g,"choco-degustation-plateau.png","Plateau dégustation")}{fig(g,"hero.png","Vitrine chocolaterie")}</article>
  </section>
  <section id="boutique" class="ch-masonry vt-reveal">
    <motion class="tile wide">{fig(g,"choco-aquarelle-coffrets.png","Coffrets cadeaux")}</motion>
    <motion class="tile">{fig(g,"produit-2.png","Tablette lait")}</motion>
    <motion class="tile">{fig(g,"produit-3.png","Pralinés")}</motion>
    <motion class="tile">{fig(g,"card-1.svg","Illustration ganaches")}</motion>
    <motion class="tile wide">{fig(g,"hero.svg","Illustration boutique")}</motion>
  </section>
  <footer>{HUB}</footer>
</main>
"""
    body = body.replace("<motion", "<div").replace("</motion>", "</div>")
    css = """
body{margin:0;background:#1a0f0a;color:#ffccbc;font-family:Georgia,serif}
.ch-nav{display:flex;gap:1.5rem;padding:1rem 1.5rem;position:sticky;top:0;background:#1a0f0a;z-index:5}
.ch-nav a{color:#ffab91}
.ch-timeline{max-width:900px;margin:0 auto;padding:2rem 1rem}
.ch-title{font-size:2.5rem;color:#ffab91}
.ch-step{display:grid;grid-template-columns:1fr 1fr;gap:2rem;align-items:center;margin:3rem 0;padding:1rem 0;border-top:1px solid #5d4037}
.ch-step--flip .ch-step__txt{order:2}
.ch-step img{width:100%;border-radius:4px;object-fit:cover;min-height:200px}
.ch-masonry{columns:2;gap:1rem;padding:1.5rem}
.ch-masonry .tile{break-inside:avoid;margin-bottom:1rem}
.ch-masonry .wide{column-span:all}
.ch-masonry img{width:100%;object-fit:cover}
footer{padding:2rem;text-align:center}
"""
    write_demo("chocolatier", "bean-timeline", "openprops", "Chocolaterie Vialson",
               "Chocolaterie artisanale bean-to-bar à Nancy.", body, css)


def gen_immobilier():
    g = "imm"
    body = f"""
<header class="imm-bar vt-reveal sticky-top">
  <span>Agence Sablon · Thionville</span>
  <form class="imm-search" role="search"><input placeholder="Ville, budget…"><button type="button">Rechercher</button></form>
</header>
<main id="contenu">
  <section class="imm-hero vt-reveal"><h1>Biens d'exception<br>en Moselle</h1></section>
  <section class="imm-stack vt-reveal">
    <article class="imm-card imm-card--1">{fig(g,"bien-thionville.svg","Appartement Thionville centre")}<h3>Thionville · 89 m²</h3></article>
    <article class="imm-card imm-card--2">{fig(g,"bien-yutz.svg","Maison Yutz jardin")}<h3>Yutz · 120 m²</h3></article>
    <article class="imm-card imm-card--3">{fig(g,"bien-sablon.svg","Loft Sablon")}<h3>Sablon · loft</h3></article>
  </section>
  <section class="imm-map vt-reveal" aria-label="Carte"><div class="imm-map-ph">Carte interactive — Moselle-Est (démo)</div></section>
  <section class="vt-reveal">{fig(g,"hero.svg","Illustration agence")}{fig(g,"equipe-agence.svg","Équipe agence immobilière")}</section>
  <footer>{HUB}</footer>
</main>
"""
    css = """
body{margin:0;font-family:system-ui,sans-serif;background:#faf8f4}
.imm-bar{display:flex;flex-wrap:wrap;gap:1rem;align-items:center;justify-content:space-between;padding:1rem 1.5rem;background:#1b4332;color:#fff;top:0;z-index:100}
.imm-search{display:flex;gap:.5rem}
.imm-search input{padding:.5rem 1rem;border-radius:6px;border:0}
.imm-hero{padding:4rem 1.5rem;background:#2d6a4f;color:#fff}
.imm-stack{position:relative;padding:4rem 1.5rem 6rem;max-width:1000px;margin:0 auto}
.imm-card{position:relative;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 12px 40px rgba(0,0,0,.12);max-width:420px}
.imm-card--2{margin-top:-3rem;margin-left:auto}
.imm-card--3{margin-top:-2rem}
.imm-card img{width:100%;height:240px;object-fit:cover}
.imm-map{padding:2rem 1.5rem}
.imm-map-ph{height:280px;background:repeating-linear-gradient(45deg,#d8e8d8,#d8e8d8 10px,#c5dcc5 10px,#c5dcc5 20px);display:grid;place-items:center;border-radius:12px;color:#1b4332}
footer{padding:2rem;text-align:center}
"""
    write_demo("immobilier", "magazine-overlap", "bootstrap", "Agence Sablon — Immobilier",
               "Immobilier prestige en Moselle.", body, css)


def gen_juridique():
    g = "jur"
    body = f"""
<header class="jur-mast vt-reveal">
  <p class="jur-kicker">Metz · Barreau de Metz</p>
  <h1>Lex &amp; Territoire</h1>
  <p class="jur-deck">Cabinet d'avocats — droit des affaires et social en Lorraine.</p>
</header>
<main id="contenu" class="jur-gazette vt-reveal">
  <article class="jur-col">
    <h2>Contentieux</h2>
    <p>Accompagnement des PME messines devant le TJ et les juridictions commerciales.</p>
    <blockquote class="jur-pull">« La prévention coûte moins qu'un procès mal préparé. »</blockquote>
    {fig(g,"expertise-contentieux.svg","Expertise contentieux")}
  </article>
  <article class="jur-col jur-col--feat">
    {fig(g,"hero.svg","Illustration cabinet",lazy=False)}
    <h2>Sociétés</h2>
    <p>Création, pactes d'associés, levées de fonds régionales.</p>
    {fig(g,"expertise-societes.svg","Expertise sociétés")}
  </article>
  <article class="jur-col">
    <h2>Social</h2>
    <p>Conseil RH, licenciement, CSE — prud'hommes de Metz.</p>
    {fig(g,"expertise-social.svg","Expertise droit social")}
    <blockquote class="jur-pull">« Un accord signé vaut mieux qu'un contentieux long. »</blockquote>
  </article>
</main>
<footer class="jur-foot vt-reveal">{HUB}</footer>
"""
    css = """
body{margin:0;font-family:Georgia,serif;background:#f4f1ea;color:#1a1a2e}
.jur-mast{padding:3rem 1.5rem;border-bottom:4px solid #c9a227;max-width:48rem}
.jur-kicker{text-transform:uppercase;letter-spacing:.2em;font-size:.75rem;color:#8b7355}
.jur-deck{font-size:1.15rem;max-width:36ch}
.jur-gazette{display:grid;grid-template-columns:repeat(3,1fr);gap:2rem;padding:2rem 1.5rem;max-width:1200px;margin:0 auto}
.jur-col{border-top:2px solid #c9a227;padding-top:1rem}
.jur-col--feat{border:3px double #c9a227;padding:1rem}
.jur-pull{border-left:4px solid #c9a227;margin:1.5rem 0;padding-left:1rem;font-style:italic;color:#4a4a6a}
.jur-gazette img{width:100%;object-fit:cover;border-radius:4px;margin:1rem 0}
.jur-foot{padding:2rem;text-align:center;border-top:1px solid #c9a227}
@media(max-width:900px){.jur-gazette{grid-template-columns:1fr}}
"""
    write_demo("juridique", "gazette-columns", "tailwind", "Lex & Territoire — Juridique",
               "Avocats droit des affaires et social à Metz.", body, css)
