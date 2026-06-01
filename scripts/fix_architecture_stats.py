#!/usr/bin/env python3
import re
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "assets" / "vitrines" / "demos" / "architecture" / "index.html"
t = p.read_text(encoding="utf-8")
bo = "<" + "motion" + "> NO"
stats = (
    '    <section class="arch-stats container" aria-label="Chiffres clés" style="padding:2.5rem 0;border-bottom:2px solid #0a0a0a">\n'
    '      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:1.5rem;text-align:center">\n'
    '        <div><p style="font-size:2.25rem;font-weight:700;margin:0">48</p><p class="arch-mono arch-accent">projets livrés</p></div>\n'
    '        <div><p style="font-size:2.25rem;font-weight:700;margin:0">8</p><p class="arch-mono arch-accent">architectes DPLG</p></div>\n'
    '        <div><p style="font-size:2.25rem;font-weight:700;margin:0">12</p><p class="arch-mono arch-accent">prix &amp; labels</p></div>\n'
    '        <div><p style="font-size:2.25rem;font-weight:700;margin:0">3</p><p class="arch-mono arch-accent">pays d\'intervention</p></div>\n'
    "      </div>\n"
    "    </section>\n\n"
    '        <section id="projets" class="container" style="padding:4rem 0">\n'
    '      <h2 class="arch-mono" style="margin-bottom:2rem">Sélection 2024–2026</h2>\n'
    '      <div class="arch-grid-projects">\n'
)
t, n = re.subn(
    r'    <section class="arch-stats[^>]*>.*?(?=<motion> NO\n      <div class="arch-grid-projects">|<motion> NO\n      <div class="arch-grid-projects">|<div class="arch-grid-projects">)',
    stats,
    t,
    count=1,
    flags=re.DOTALL,
)
if n == 0:
    t, n = re.subn(
        r'    <section class="arch-stats[^>]*>.*?(?=<div class="arch-grid-projects">)',
        stats,
        t,
        count=1,
        flags=re.DOTALL,
    )
while bo in t:
    t = t.replace(bo, "")
p.write_text(t, encoding="utf-8")
print("n=", n, "bad=", bo in t)
