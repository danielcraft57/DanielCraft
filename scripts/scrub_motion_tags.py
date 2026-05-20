#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "assets" / "vitrines" / "demos"
SLUGS = [
    "technologie",
    "restauration",
    "beaute",
    "odontologie",
    "industrie",
    "association",
    "fitness",
    "architecture",
    "photographie",
]
bo = "<" + "motion" + "> NO"
bc = "</" + "motion" + "> NO"

for slug in SLUGS:
    p = ROOT / slug / "index.html"
    if not p.exists():
        continue
    t = p.read_text(encoding="utf-8")
    t = t.replace(bo, "").replace(bc, "")
    p.write_text(t, encoding="utf-8")
    print(slug, bo in t)

# photographie stats completion
p = ROOT / "photographie" / "index.html"
t = p.read_text(encoding="utf-8")
if "photo-stats" in t and "corporate" not in t.split("photo-stats")[1][:400]:
    block = """    <section class="photo-stats" aria-label="Chiffres clés" style="max-width:var(--size-content-3);margin:0 auto;padding:var(--size-6);display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:var(--size-5);text-align:center;border-block:1px solid var(--sand-4)">
      <div><p style="font-size:var(--font-size-4);font-weight:700;margin:0">240+</p><p style="font-size:var(--font-size-0);color:var(--sand-9)">mariages</p></div>
      <div><p style="font-size:var(--font-size-4);font-weight:700;margin:0">15</p><p style="font-size:var(--font-size-0);color:var(--sand-9)">ans d'expérience</p></div>
      <div><p style="font-size:var(--font-size-4);font-weight:700;margin:0">6</p><p style="font-size:var(--font-size-0);color:var(--sand-9)">univers photo</p></div>
      <div><p style="font-size:var(--font-size-4);font-weight:700;margin:0">48h</p><p style="font-size:var(--font-size-0);color:var(--sand-9)">réponse devis</p></div>
    </section>

"""
    t = re.sub(r'    <section class="photo-stats"[^>]*>.*?(?=    <section id="portfolio")', block, t, count=1, flags=re.DOTALL)
    p.write_text(t, encoding="utf-8")

# architecture duplicate grid
p = ROOT / "architecture" / "index.html"
t = p.read_text(encoding="utf-8")
t = t.replace(
    '      <div class="arch-grid-projects">\n\n      <div class="arch-grid-projects">',
    '      <div class="arch-grid-projects">',
)
p.write_text(t, encoding="utf-8")
print("scrub done")
