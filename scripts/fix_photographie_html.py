#!/usr/bin/env python3
import re
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "assets" / "vitrines" / "demos" / "photographie" / "index.html"
t = p.read_text(encoding="utf-8")
m = re.search(r"(<article class=\"photo-tile.*?</section>\s*\n\s*<section id=\"prestations\")", t, re.DOTALL)
if not m:
    raise SystemExit("portfolio block not found")
portfolio_inner = m.group(1)
# strip trailing prestations marker from inner
portfolio_inner = portfolio_inner[: portfolio_inner.rfind("\n    <section id=\"prestations\"")]
stats = """    <section class="photo-stats" aria-label="Chiffres clés" style="max-width:var(--size-content-3);margin:0 auto;padding:var(--size-6);display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:var(--size-5);text-align:center;border-block:1px solid var(--sand-4)">
      <div><p style="font-size:var(--font-size-4);font-weight:700;margin:0">240+</p><p style="font-size:var(--font-size-0);color:var(--sand-9)">mariages</p></motion> NO
"""
stats = """    <section class="photo-stats" aria-label="Chiffres clés" style="max-width:var(--size-content-3);margin:0 auto;padding:var(--size-6);display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:var(--size-5);text-align:center;border-block:1px solid var(--sand-4)">
      <div><p style="font-size:var(--font-size-4);font-weight:700;margin:0">240+</p><p style="font-size:var(--font-size-0);color:var(--sand-9)">mariages</p></div>
      <div><p style="font-size:var(--font-size-4);font-weight:700;margin:0">15</p><p style="font-size:var(--font-size-0);color:var(--sand-9)">ans d'expérience</p></div>
      <div><p style="font-size:var(--font-size-4);font-weight:700;margin:0">6</p><p style="font-size:var(--font-size-0);color:var(--sand-9)">univers photo</p></div>
      <div><p style="font-size:var(--font-size-4);font-weight:700;margin:0">48h</p><p style="font-size:var(--font-size-0);color:var(--sand-9)">réponse devis</p></div>
    </section>

        <section id="portfolio" class="photo-masonry" aria-label="Portfolio">
"""
replacement = stats + portfolio_inner + "\n    </section>\n\n"
t = re.sub(
    r'    <section class="photo-stats"[^>]*>.*?(?=\n    <section id="prestations")',
    replacement,
    t,
    count=1,
    flags=re.DOTALL,
)
bo = "<" + "motion" + "> NO"
t = t.replace(bo, "")
p.write_text(t, encoding="utf-8")
print("photo ok")
