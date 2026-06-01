# Batch 4: beaute, odontologie, industrie, association + commerce/comptable refresh
from vitrine_gen_lib import fig, write_demo

HUB = '<p class="hub-back"><a href="../index.html">← Hub vitrines</a></p>'


def run_batch4():
    gen_beaute()
    gen_odontologie()
    gen_industrie()
    gen_association()


def gen_beaute():
    g = "bea"
    body = f"""
<header class="bea-hero vt-reveal"><h1>Écrin Spa</h1><p>Nancy · rituels bien-être</p></header>
<section class="bea-curve bea-curve--1"></section>
<main id="contenu">
  <section class="bea-wall vt-reveal">
    <article>{fig(g,"beaute-soin.png","Soin visage",lazy=False)}<h3>Soin visage</h3></article>
    <article>{fig(g,"beaute-spa.png","Spa et hammam")}<h3>Spa</h3></article>
    <article>{fig(g,"beaute-produits.png","Boutique produits")}<h3>Boutique</h3></article>
    <article>{fig(g,"hero.svg","Illustration institut")}<h3>Rituels</h3></article>
    <article>{fig(g,"card-1.svg","Massage")}<h3>Massage</h3></article>
    <article>{fig(g,"card-2.svg","Manucure")}<h3>Mains</h3></article>
    <article>{fig(g,"card-3.svg","Parfums")}<h3>Parfums</h3></article>
  </section>
</main>
<section class="bea-curve bea-curve--2"></section>
<footer class="vt-reveal">{HUB}</footer>
"""
    css = """
body{margin:0;font-family:system-ui,sans-serif;background:#fdf5f8;color:#5c3d4d}
.bea-hero{padding:4rem 1.5rem;text-align:center;background:linear-gradient(180deg,#f8e8ee,#e8d0dc)}
.bea-curve{height:60px;background:#fdf5f8}
.bea-curve--1{clip-path:ellipse(120% 100% at 50% 100%)}
.bea-curve--2{clip-path:ellipse(120% 100% at 50% 0);margin-top:-1px;background:#8b5a6b}
.bea-wall{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:.75rem;padding:2rem 1rem;max-width:1100px;margin:0 auto}
.bea-wall article{border-radius:16px;overflow:hidden;background:#fff}
.bea-wall img{width:100%;height:200px;object-fit:cover}
.bea-wall h3{margin:.5rem 1rem 1rem;font-size:1rem}
footer{padding:2rem;text-align:center;background:#8b5a6b;color:#fff}
"""
    write_demo("beaute", "spa-ritual", "bulma", "Écrin Spa — Beauté",
               "Institut spa et soins à Nancy.", body, css)


def gen_odontologie():
    g = "odo"
    body = f"""
<header class="odo-calm vt-reveal"><h1>Cabinet Mosäique</h1><p>Thionville · prévention &amp; soins</p></header>
<main id="contenu" class="odo-path">
  <article class="odo-step vt-reveal"><span class="odo-step-num">1</span><div class="message is-info"><div class="message-body"><strong>Accueil</strong> — bilan et pano numérique.</div></div>{fig(g,"hero.png","Accueil cabinet",lazy=False)}</article>
  <article class="odo-step vt-reveal"><span class="odo-step-num">2</span>{fig(g,"salle.png","Salle de soins")}<div class="message is-light"><motion class="message-body">Soins conservateurs, implants, orthodontie.</motion></div></article>
  <article class="odo-step vt-reveal"><span class="odo-step-num">3</span><div class="message is-success"><div class="message-body">Prévention — détartrage &amp; fluoration.</motion></div>{fig(g,"odo-illus-brossage.png","Illustration brossage")}{fig(g,"odo-salle-soins-vide.png","Salle équipée")}</article>
  <article class="odo-step vt-reveal"><span class="odo-step-num">4</span>{fig(g,"equipe-soins.png","Équipe pluridisciplinaire")}{fig(g,"card-1.svg","Illustration équipe")}{fig(g,"card-2.svg","Illustration prévention")}{fig(g,"card-3.svg","Illustration implants")}</article>
</main>
<footer>{HUB}</footer>
"""
    body = body.replace("<motion", "<div").replace("</motion>", "</div>")
    css = """
body{margin:0;font-family:system-ui,sans-serif;background:#e8f4fc;color:#0d7ea8}
.odo-calm{padding:2.5rem 1.5rem;text-align:center;background:#fff}
.odo-path{max-width:640px;margin:0 auto;padding:2rem 1rem}
.odo-step{position:relative;padding-left:3rem;margin-bottom:2.5rem;border-left:3px solid #b8e0f0}
.odo-step-num{position:absolute;left:-1.1rem;top:0;width:2rem;height:2rem;background:#0d7ea8;color:#fff;border-radius:50%;display:grid;place-items:center;font-weight:700}
.odo-step img{width:100%;border-radius:8px;object-fit:cover;margin:.75rem 0}
footer{padding:2rem;text-align:center}
"""
    write_demo("odontologie", "patient-path", "bulma", "Mosäique — Odontologie",
               "Cabinet dentaire à Thionville.", body, css)


def gen_industrie():
    g = "ind"
    body = f"""
<header class="ind-head vt-reveal"><h1>Forja Lorraine</h1><p>Usinage · Yutz</p></header>
<main id="contenu">
  <div class="tabs is-boxed ind-tabs vt-reveal">
    <ul><li class="is-active"><a data-tab="ligne">Ligne</a></li><li><a data-tab="qual">Qualité</a></li><li><a data-tab="plan">Plan</a></li></ul>
  </motion>
  <section id="ligne" class="ind-panel is-active vt-reveal">
  {fig(g,"ligne-production.png","Ligne d'usinage",lazy=False)}{fig(g,"industrie-soudure.png","Poste soudure")}
  <table class="table is-striped"><thead><tr><th>Machine</th><th>Précision</th><th>Cadence</th></tr></thead>
  <tbody><tr><td>CNC-01</td><td>±0.01 mm</td><td>240 p/h</td></tr><tr><td>Robot soude</td><td>ISO 5817-B</td><td>—</td></tr></tbody></table>
  </section>
  <section id="qual" class="ind-panel vt-reveal">{fig(g,"controle.png","Contrôle qualité")}{fig(g,"card-1.svg","Métrologie")}</section>
  <section id="plan" class="ind-panel vt-reveal">{fig(g,"industrie-plan-usine.png","Plan usine")}{fig(g,"hero.png","Vue usine")}{fig(g,"card-2.svg","Logistique")}{fig(g,"card-3.svg","Maintenance")}</section>
</main>
<footer>{HUB}</footer>
<script>document.querySelectorAll('.ind-tabs a').forEach(a=>a.addEventListener('click',e=>{{e.preventDefault();document.querySelectorAll('.ind-panel,.ind-tabs li').forEach(x=>x.classList.remove('is-active'));a.parentElement.classList.add('is-active');document.getElementById(a.dataset.tab).classList.add('is-active')}}))</script>
"""
    body = body.replace("<motion", "<div").replace("</motion>", "</div>")
    css = """
body{margin:0;font-family:Consolas,monospace;background:#0a1628;color:#7dd3fc;
background-image:linear-gradient(rgba(56,189,248,.08) 1px,transparent 1px),linear-gradient(90deg,rgba(56,189,248,.08) 1px,transparent 1px);background-size:24px 24px}
.ind-head{padding:2rem;border-bottom:2px solid #ffb300;color:#ffb300}
.ind-panel{display:none;padding:1.5rem}
.ind-panel.is-active{display:block}
.ind-panel img{width:100%;max-height:320px;object-fit:cover;border:1px solid #ffb300;margin-bottom:1rem}
.table{background:#111;color:#e5e5e5}
footer{padding:2rem;text-align:center;color:#ffb300}
"""
    write_demo("industrie", "blueprint-spec", "bulma", "Forja Lorraine — Industrie",
               "Usinage et métallurgie à Yutz.", body, css)


def gen_association():
    g = "ass"
    body = f"""
<header class="ass-head vt-reveal"><h1>Les Mains du Quartier</h1><p>Metz · solidarité</p>
<div class="ass-thermo" role="progressbar" aria-valuenow="72" aria-valuemin="0" aria-valuemax="100"><div class="ass-thermo-fill" style="width:72%"></div><span>72 % objectif dons 2026 — 18 400 € / 25 500 €</span></div>
</header>
<main id="contenu" class="ass-mosaic vt-reveal">
  <article class="tile t1">{fig(g,"hero.png","Bénévoles quartier",lazy=False)}</article>
  <article class="tile t2 wide">{fig(g,"mission-benevoles.png","Mission bénévoles")}</article>
  <article class="tile t3">{fig(g,"cuisine.png","Cuisine solidaire")}</article>
  <article class="tile t4 tall">{fig(g,"assoc-fete-quartier.png","Fête de quartier")}</article>
  <article class="tile t5">{fig(g,"assoc-gen-quartier.png","Quartier Metz")}</article>
  <article class="tile t6 wide">{fig(g,"assoc-gen-mains.png","Mains solidaires")}</article>
  <article class="tile t7">{fig(g,"assoc-gen-volontaires.png","Volontaires")}</article>
  <article class="tile t8">{fig(g,"assoc-poster-illu.png","Affiche événement")}</article>
  <article class="tile t9">{fig(g,"card-1.svg","Maraude")}{fig(g,"card-2.svg","Cuisine")}{fig(g,"card-3.svg","Fête")}</article>
</main>
<footer>{HUB}</footer>
"""
    css = """
body{margin:0;font-family:system-ui,sans-serif;background:#e8f5e9;color:#2e7d4e}
.ass-head{padding:2rem 1.5rem;background:#fff}
.ass-thermo{height:28px;background:#c8e6c9;border-radius:999px;overflow:hidden;margin-top:1rem;position:relative}
.ass-thermo-fill{height:100%;background:linear-gradient(90deg,#48c774,#2e7d4e)}
.ass-thermo span{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:.75rem;font-weight:600}
.ass-mosaic{display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:140px;gap:.5rem;padding:1rem;max-width:1100px;margin:0 auto}
.ass-mosaic .tile{overflow:hidden;border-radius:10px;background:#fff}
.ass-mosaic .wide{grid-column:span 2}
.ass-mosaic .tall{grid-row:span 2}
.ass-mosaic img{width:100%;height:100%;object-fit:cover}
footer{padding:2rem;text-align:center}
@media(max-width:700px){.ass-mosaic{grid-template-columns:1fr 1fr}}
"""
    write_demo("association", "impact-mosaic", "bulma", "Les Mains du Quartier — Association",
               "Association solidaire à Metz.", body, css)
