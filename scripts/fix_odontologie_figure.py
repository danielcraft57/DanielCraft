#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "assets" / "vitrines" / "demos" / "odontologie" / "index.html"
t = p.read_text(encoding="utf-8")
bo = "<" + "motion" + "> NO"
mc = "vitrine-figure--" + "motion"
block = f"""            <div class="column is-6 vitrine-img-reveal animate__animated animate__fadeInRight animate__delay-1s" style="--animate-duration: 0.95s;">
              <figure class="vitrine-figure vitrine-hero-visual vitrine-figure--ken {mc} mb-0">
                <a href="images/hero.svg" class="glightbox" data-gallery="odo-visuels" data-glightbox="title: Cabinet Mosaïque — illustration">
                  <img src="images/hero.png" width="1200" height="675" alt="Salle d'attente lumineuse du cabinet dentaire" decoding="async" fetchpriority="high">
                </a>
              </figure>
            </div>
"""
if bo in t:
    t = t.replace(f"            {bo}\n", block, 1)
while bo in t:
    t = t.replace(bo, "")
stats = """
    <section class="section odo-stats-band py-5" aria-label="Chiffres clés">
      <div class="container">
        <div class="columns has-text-centered mb-0">
          <div class="column"><p class="title is-2 odo-brand mb-1">6</p><p class="subtitle is-6">praticiens</p></div>
          <div class="column"><p class="title is-2 odo-brand mb-1">4,9</p><p class="subtitle is-6">note patients</p></div>
          <div class="column"><p class="title is-2 odo-brand mb-1">J+0</p><p class="subtitle is-6">urgences du jour</p></div>
          <div class="column"><p class="title is-2 odo-brand mb-1">100 %</p><p class="subtitle is-6">devis détaillés</p></div>
        </div>
      </div>
    </section>
"""
if "odo-stats-band" not in t:
    t = t.replace(
        '    </section>\n\n    <section class="section vitrine-cta-banner odo-cta-banner',
        "    </section>" + stats + '\n    <section class="section vitrine-cta-banner odo-cta-banner',
        1,
    )
if "glightbox.min.js" not in t:
    t = t.replace(
        "</body>",
        '  <script src="https://cdn.jsdelivr.net/npm/glightbox@3.2.0/dist/js/glightbox.min.js" crossorigin="anonymous"></script>\n'
        '  <script src="../shared/vitrine-images.js"></script>\n</body>',
    )
p.write_text(t, encoding="utf-8")
print("odo ok", bo in p.read_text(encoding="utf-8"))
