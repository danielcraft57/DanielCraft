#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "assets" / "vitrines" / "demos" / "technologie" / "index.html"
t = p.read_text(encoding="utf-8")
bo = "<" + "motion" + "> NO"
bc = "</" + "motion" + "> NO"

t = t.replace(f"              {bo}\n", '              <div class="buttons mt-5">\n')

fig = (
    "            </div>\n"
    '            <div class="column is-6 vitrine-img-reveal">\n'
    '              <figure class="vitrine-figure vitrine-hero-visual vitrine-figure--ken vitrine-figure--motion mb-0">\n'
    '                <a href="images/hero.svg" class="glightbox" data-gallery="tech-visuels" data-glightbox="title: Datacenter — illustration">\n'
    '                  <img src="images/tech-datacenter.png" width="1200" height="675" alt="Salle serveurs et infrastructure cloud" decoding="async" fetchpriority="high">\n'
    "                </a>\n"
    "              </figure>\n"
    "            </div>\n"
    "          </div>\n"
)
t = t.replace(f"            {bc}\n        </div>", fig + "        </div>")

stats = (
    '\n    <section class="section tech-stats-band py-5" aria-label="Chiffres clés">\n'
    '      <div class="container">\n'
    '        <div class="columns has-text-centered mb-0">\n'
    '          <div class="column"><p class="title is-2 has-text-white mb-1">120+</p>'
    '<p class="subtitle is-6 has-text-white-ter">clients actifs</p></div>\n'
    '          <div class="column"><p class="title is-2 has-text-white mb-1">99,9 %</p>'
    '<p class="subtitle is-6 has-text-white-ter">SLA plateforme</p></div>\n'
    '          <div class="column"><p class="title is-2 has-text-white mb-1">48 h</p>'
    '<p class="subtitle is-6 has-text-white-ter">délai audit</p></div>\n'
    '          <div class="column"><p class="title is-2 has-text-white mb-1">UE</p>'
    '<p class="subtitle is-6 has-text-white-ter">données hébergées</p></div>\n'
    "        </div>\n      </div>\n    </section>\n"
)

if "tech-stats-band" not in t:
    t = t.replace(
        '    </section>\n    <section class="section vitrine-cta-banner vitrine-cta-shimmer has-background-link',
        "    </section>" + stats + '    <section class="section vitrine-cta-banner vitrine-cta-shimmer has-background-link',
        1,
    )

while bo in t:
    t = t.replace(bo, "")
while bc in t:
    t = t.replace(bc, "</div>")

p.write_text(t, encoding="utf-8")
print("fixed", p.name, "bad tags left:", bo in p.read_text(encoding="utf-8"))
