#!/usr/bin/env python3
"""Met à jour le hub vitrines (grille + KPI) après évolution du catalogue."""
import re
from pathlib import Path

HUB = Path(__file__).resolve().parents[1] / "assets" / "vitrines" / "demos" / "index.html"
D = "div"

GRID = f"""
        <{D} class="grid hub-grid">
          <a class="card" href="technologie/index.html"><span class="badge">Bulma · Tech</span><h3><i class="fa-solid fa-microchip fa-fw" aria-hidden="true"></i> Technologie</h3><p>Synapse Lorraine — SaaS &amp; cloud.</p></a>
          <a class="card" href="restauration/index.html"><span class="badge">Bulma · HCR</span><h3><i class="fa-solid fa-utensils fa-fw" aria-hidden="true"></i> Restauration</h3><p>Brasserie Saint-Jacques.</p></a>
          <a class="card" href="beaute/index.html"><span class="badge">Bulma · Bien-être</span><h3><i class="fa-solid fa-spa fa-fw" aria-hidden="true"></i> Beauté</h3><p>Spa Thalie.</p></a>
          <a class="card" href="odontologie/index.html"><span class="badge">Bulma · Santé</span><h3><i class="fa-solid fa-tooth fa-fw" aria-hidden="true"></i> Odontologie</h3><p>Centre dentaire Mosaïque.</p></a>
          <a class="card" href="industrie/index.html"><span class="badge">Bulma · Industrie</span><h3><i class="fa-solid fa-gears fa-fw" aria-hidden="true"></i> Industrie</h3><p>Précisite Usinage.</p></a>
          <a class="card" href="association/index.html"><span class="badge">Bulma · ESS</span><h3><i class="fa-solid fa-hand-holding-heart fa-fw" aria-hidden="true"></i> Association</h3><p>Solidarités Metz Métropole.</p></a>
          <a class="card" href="commerce/index.html"><span class="badge">Bootstrap · Retail</span><h3><i class="fa-solid fa-store fa-fw" aria-hidden="true"></i> Commerce</h3><p>Halles Thionville.</p></a>
          <a class="card" href="comptable/index.html"><span class="badge">Bootstrap · Conseil</span><h3><i class="fa-solid fa-calculator fa-fw" aria-hidden="true"></i> Comptable</h3><p>Verlaine &amp; Associés.</p></a>
          <a class="card" href="education/index.html"><span class="badge">Tailwind · Formation</span><h3><i class="fa-solid fa-graduation-cap fa-fw" aria-hidden="true"></i> Éducation</h3><p>Institut Mercure.</p></a>
          <a class="card" href="services/index.html"><span class="badge">Tailwind · Services</span><h3><i class="fa-solid fa-building fa-fw" aria-hidden="true"></i> Services</h3><p>Proprio Facility.</p></a>
          <a class="card" href="banque/index.html"><span class="badge">Tailwind · Finance</span><h3><i class="fa-solid fa-landmark fa-fw" aria-hidden="true"></i> Banque</h3><p>Verlaine Banque Régionale.</p></a>
          <a class="card" href="etablissement/index.html"><span class="badge">Pico CSS · Hôtel</span><h3><i class="fa-solid fa-hotel fa-fw" aria-hidden="true"></i> Établissement</h3><p>Hôtel Stanislas Collection.</p></a>
          <a class="card" href="automobile/index.html"><span class="badge">DaisyUI · Garage</span><h3><i class="fa-solid fa-car fa-fw" aria-hidden="true"></i> Automobile</h3><p>Garage Central Plappeville.</p></a>
          <a class="card" href="chocolatier/index.html"><span class="badge">Open Props · Artisan</span><h3><i class="fa-solid fa-cookie-bite fa-fw" aria-hidden="true"></i> Chocolatier</h3><p>Chocolaterie Vialson.</p></a>
          <a class="card" href="immobilier/index.html"><span class="badge">Bootstrap</span><h3><i class="fa-solid fa-house-chimney fa-fw" aria-hidden="true"></i> Immobilier</h3><p>Patrimoine Lorraine.</p></a>
          <a class="card" href="juridique/index.html"><span class="badge">Tailwind</span><h3><i class="fa-solid fa-scale-balanced fa-fw" aria-hidden="true"></i> Juridique</h3><p>Rivière &amp; Partenaires.</p></a>
          <a class="card" href="architecture/index.html"><span class="badge">Pico CSS</span><h3><i class="fa-solid fa-drafting-compass fa-fw" aria-hidden="true"></i> Architecture</h3><p>Atelier Nord-Est.</p></a>
          <a class="card" href="fitness/index.html"><span class="badge">DaisyUI</span><h3><i class="fa-solid fa-dumbbell fa-fw" aria-hidden="true"></i> Fitness</h3><p>Pulse Fitness Metz.</p></a>
          <a class="card" href="photographie/index.html"><span class="badge">Open Props</span><h3><i class="fa-solid fa-camera fa-fw" aria-hidden="true"></i> Photographie</h3><p>Studio Lumière Grise.</p></a>
        </{D}>
"""

KPI = f"""
        <{D} class="hub-kpi" aria-label="Indicateurs vitrines">
          <{D}><strong>19</strong><span>vitrines</span></{D}>
          <{D}><strong>6</strong><span>Bulma</span></{D}>
          <{D}><strong>13</strong><span>autres frameworks</span></{D}>
          <{D}><strong>3</strong><span>formats capture</span></{D}>
        </{D}>
"""

t = HUB.read_text(encoding="utf-8")
pat = rf'<div class="grid hub-grid">.*?</div>\s*</div>\s*(?=\n    </section>\n\n    <section id="guide")'
t, n1 = re.subn(pat, GRID.strip() + f"\n      </{D}>\n", t, count=1, flags=re.DOTALL)
if not n1:
    raise SystemExit("grid replace failed")

t, n2 = re.subn(
    rf'<div class="hub-kpi"[^>]*>.*?</{D}>\s*(?=\n      </{D}>\n    </section>\n\n    <section id="contact")',
    KPI.strip(),
    t,
    count=1,
    flags=re.DOTALL,
)
if not n2:
    raise SystemExit("kpi replace failed")

HUB.write_text(t, encoding="utf-8")
print("hub updated", n1, n2)
