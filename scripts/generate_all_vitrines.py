#!/usr/bin/env python3
"""Generate all unique vitrine demos. Run from repo root: python scripts/generate_all_vitrines.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from vitrine_gen_lib import fig, write_demo  # noqa: E402
from vitrine_gen_batch2 import run_batch2  # noqa: E402
from vitrine_gen_batch3 import run_batch3  # noqa: E402
from vitrine_gen_batch4 import run_batch4  # noqa: E402

HUB = '<p class="hub-back"><a href="../index.html">← Hub vitrines</a></p>'


def gen_education():
    g = "edu"
    body = f"""
<a class="skip" href="#contenu">Aller au contenu</a>
<header class="edu-bar vt-reveal">
  <span class="edu-logo">Institut Mercure</span>
  <nav><a href="#parcours">Parcours</a><a href="#modules">Modules</a><button type="button" class="edu-btn" onclick="document.getElementById('dlgIns').showModal()">S'inscrire</button></nav>
</header>
<main id="contenu">
  <section class="edu-intro vt-reveal">
    <p class="edu-tag">Nancy · formations pro</p>
    <h1>Apprendre en <em>Moselle-Est</em></h1>
    <p>Parcours métiers, alternance et VAE — campus digital et salles à Saint-Nicolas.</p>
  </section>
  <section id="parcours" class="edu-snap vt-reveal" aria-label="Parcours">
    <h2>Parcours (scroll horizontal)</h2>
    <motion class="edu-snap-track">
      <article>{fig(g,"edu-gen-parcours.png","Parcours métiers digital",lazy=False)}<h3>Digital &amp; data</h3></article>
      <article>{fig(g,"edu-groupe.png","Groupe en formation")}<h3>Management</h3></article>
      <article>{fig(g,"edu-formateur.png","Formateur en atelier")}<h3>Soft skills</h3></article>
      <article>{fig(g,"edu-salle.png","Salle de cours équipée")}<h3>Langues</h3></article>
      <article>{fig(g,"card-1.svg","Illustration parcours")}<h3>Industrie 4.0</h3></article>
    </motion>
  </section>
  <section id="modules" class="edu-bento vt-reveal">
    <h2>Modules bento</h2>
    <motion class="edu-bento-grid">
      <motion class="cell wide">{fig(g,"edu-gen-modules.png","Modules e-learning")}<span>Blended learning</span></motion>
      <motion class="cell">{fig(g,"edu-gen-mosaic.png","Mosaïque campus")}</motion>
      <motion class="cell tall">{fig(g,"card-2.svg","Module alternance")}</motion>
      <motion class="cell">{fig(g,"card-3.svg","Module VAE")}</motion>
    </motion>
  </section>
  <footer class="edu-foot vt-reveal">{HUB}</footer>
</main>
<dialog id="dlgIns" class="edu-dialog"><form method="dialog">
  <h2>Inscription (démo)</h2><label>Nom <input name="n"></label><label>Parcours <select><option>Digital</option></select></label>
  <button value="cancel">Fermer</button><button value="ok">Envoyer</button>
</form></dialog>
"""
    body = body.replace("<motion", "<div").replace("</motion>", "</div>")
    css = """
body{margin:0;font-family:system-ui,sans-serif;background:#0f2744;color:#fff}
.edu-bar{display:flex;justify-content:space-between;align-items:center;padding:1rem 1.5rem;background:#1a3a5f;position:sticky;top:0;z-index:10}
.edu-logo{font-weight:800;color:#e8c547}
.edu-bar nav{display:flex;gap:1rem;align-items:center}
.edu-bar a{color:#cde}
.edu-btn{background:#e8c547;border:0;padding:.5rem 1rem;border-radius:6px;cursor:pointer}
.edu-intro{padding:3rem 1.5rem;max-width:40rem}
.edu-intro h1{font-size:clamp(2rem,5vw,3rem)}
.edu-intro em{color:#e8c547;font-style:normal}
.edu-snap{padding:1.5rem}
.edu-snap-track{display:flex;gap:1rem;overflow-x:auto;scroll-snap-type:x mandatory;padding-bottom:1rem}
.edu-snap-track article{flex:0 0 min(85vw,380px);scroll-snap-align:start;background:#1a3a5f;border-radius:12px;overflow:hidden}
.edu-snap-track img{width:100%;height:200px;object-fit:cover}
.edu-bento{padding:2rem 1.5rem}
.edu-bento-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:.75rem}
.edu-bento .cell{background:#1a3a5f;border-radius:10px;overflow:hidden;min-height:140px}
.edu-bento .wide{grid-column:span 2}
.edu-bento .tall{grid-row:span 2}
.edu-bento img{width:100%;height:100%;min-height:140px;object-fit:cover}
.edu-dialog{border:0;border-radius:12px;padding:1.5rem;max-width:24rem}
.edu-foot{padding:2rem;text-align:center;opacity:.8}
@media(max-width:700px){.edu-bento-grid{grid-template-columns:1fr 1fr}}
"""
    write_demo("education", "campus-snap", "tailwind", "Institut Mercure — Éducation",
               "Formations professionnelles à Nancy et en Moselle.", body, css)


def gen_services():
    g = "svc"
    body = f"""
<a class="skip" href="#contenu">Aller au contenu</a>
<nav class="svc-stick" aria-label="Sections"><a href="#band1">Accueil</a><a href="#band2">Nettoyage</a><a href="#band3">Facility</a><a href="#contact">Contact</a></nav>
<main id="contenu">
  <section id="band1" class="svc-zig svc-zig--left vt-reveal">
    <motion class="svc-zig-copy"><p>Metz · Grand Est</p><h1>Proprio Facility</h1><p>Accueil, sécurité et image de marque pour sites tertiaires lorrain.</p></motion>
    <motion class="svc-zig-media">{fig(g,"services-accueil.png","Hôtesse d'accueil en entreprise",lazy=False)}</motion>
  </section>
  <section id="band2" class="svc-zig svc-zig--right vt-reveal">
    <motion class="svc-zig-media">{fig(g,"services-nettoyage.png","Équipe nettoyage tertiaire")}</motion>
    <motion class="svc-zig-copy"><h2>Propreté &amp; hygiène</h2><p>Plans QHSE, audits ISO et équipes de nuit sur technopoles messines.</p></motion>
  </section>
  <section id="band3" class="svc-zig svc-zig--left vt-reveal">
    <motion class="svc-zig-copy"><h2>Facility management</h2><p>Gestion multi-sites, maintenance et reporting carbone.</p></motion>
    <motion class="svc-zig-media">{fig(g,"services-facility.png","Gestionnaire facility sur site")}</motion>
  </section>
  <section class="svc-gallery vt-reveal">
    {fig(g,"card-1.svg","Illustration accueil")}{fig(g,"card-2.svg","Illustration sécurité")}{fig(g,"card-3.svg","Illustration maintenance")}
  </section>
  <section id="contact" class="svc-foot vt-reveal"><h2>Devis sous 48 h</h2><p>03 87 00 00 00 · Metz</p>{HUB}</section>
</main>
"""
    body = body.replace("<motion", "<motion").replace("</motion>", "</motion>")
    body = body.replace("<motion", "<div").replace("</motion>", "</div>")
    css = """
body{margin:0;font-family:system-ui,sans-serif}
.svc-stick{position:sticky;top:0;z-index:20;display:flex;gap:1.5rem;justify-content:center;padding:.75rem;background:#111;color:#fff}
.svc-stick a{color:#7dd3fc;text-decoration:none}
.svc-zig{min-height:100vh;display:grid;grid-template-columns:1fr 1fr;align-items:center}
.svc-zig--right .svc-zig-media{order:-1}
.svc-zig-copy{padding:clamp(2rem,6vw,4rem)}
.svc-zig-media{overflow:hidden}
.svc-zig-media img{width:100%;min-height:100vh;object-fit:cover}
.svc-gallery{display:grid;grid-template-columns:repeat(3,1fr);gap:.5rem;padding:1rem}
.svc-gallery img{width:100%;height:220px;object-fit:cover}
.svc-foot{padding:3rem 1.5rem;text-align:center;background:#0ea5e9;color:#fff}
@media(max-width:800px){.svc-zig{grid-template-columns:1fr}.svc-zig-media img{min-height:50vh}}
"""
    write_demo("services", "zigzag-ops", "tailwind", "Proprio Facility — Services",
               "Facility management et services aux entreprises en Lorraine.", body, css)


def fix_all_motion():
    import re
    root = Path(__file__).resolve().parents[1] / "assets" / "vitrines" / "demos"
    for p in root.rglob("index.html"):
        t = p.read_text(encoding="utf-8")
        new = re.sub(r"</?motion\b", lambda m: m.group(0).replace("motion", "motion").replace("motion", "div"), t)
        new = re.sub(r"</?motion\b", lambda m: m.group(0).replace("motion", "div"), t)
        if new != t:
            p.write_text(new, encoding="utf-8")


if __name__ == "__main__":
    gen_education()
    gen_services()
    run_batch2()
    run_batch3()
    run_batch4()
    fix_all_motion()
    print("Generated 17 demos (+ commerce/comptable manual). Run fix_motion_tags if needed.")
