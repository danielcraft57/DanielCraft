#!/usr/bin/env python3
"""Illustrations SVG enrichies : photographie, fitness, architecture, juridique, immobilier."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "assets" / "vitrines" / "demos"


def w(rel: str, body: str) -> None:
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body.strip() + "\n", encoding="utf-8")


# ——— Studio Lumière Grise (photographie) ———
w(
    "photographie/images/hero.svg",
    """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 520" role="img" aria-labelledby="t">
  <title id="t">Studio Lumière Grise — lumière naturelle et boîtier</title>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#2a2622"/><stop offset="100%" stop-color="#4a4540"/></linearGradient>
    <radialGradient id="spot" cx="35%" cy="30%" r="55%"><stop offset="0%" stop-color="#fff8ee" stop-opacity=".55"/><stop offset="100%" stop-color="#fff8ee" stop-opacity="0"/></radialGradient>
    <linearGradient id="gold" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#c9a227"/><stop offset="100%" stop-color="#e8d5a0"/></linearGradient>
  </defs>
  <rect width="1200" height="520" fill="url(#bg)"/>
  <rect width="1200" height="520" fill="url(#spot)"/>
  <g opacity=".08" stroke="#fff" stroke-width="1"><path d="M0 130 H1200 M0 260 H1200 M0 390 H1200"/><path d="M200 0 V520 M500 0 V520 M800 0 V520"/></g>
  <g transform="translate(180 70)">
    <rect x="40" y="80" width="760" height="300" rx="6" fill="#1a1816" stroke="#c9a227" stroke-width="2"/>
    <rect x="120" y="120" width="520" height="220" fill="#3d3830"/>
    <circle cx="380" cy="230" r="95" fill="#f5f0e8" opacity=".25"/>
    <rect x="600" y="140" width="160" height="200" rx="4" fill="#f5f0e8" stroke="#1a1a1a" stroke-width="2"/>
    <rect x="620" y="160" width="120" height="90" fill="#2a2622"/>
    <circle cx="680" cy="205" r="28" fill="none" stroke="url(#gold)" stroke-width="4"/>
    <circle cx="680" cy="205" r="14" fill="#e8e0d4"/>
    <rect x="80" y="300" width="200" height="12" rx="3" fill="#c9a227" opacity=".5"/>
    <path d="M100 360 Q380 280 660 360" fill="none" stroke="#c9a227" stroke-width="2" class="vitrine-sketch-stroke" opacity=".6"/>
  </g>
  <g fill="none" stroke="#c9a227" stroke-width="2" opacity=".35" class="vitrine-sketch-stroke">
    <path d="M920 100 Q1000 60 1080 120"/><path d="M60 420 Q200 380 340 420"/>
  </g>
  <text x="600" y="490" text-anchor="middle" font-family="Georgia,serif" font-size="13" fill="#c9a227" opacity=".5">STUDIO LUMIÈRE GRISE · METZ</text>
</svg>""",
)

for name, title, mood in [
    ("portfolio-mariage", "Mariage", ("#f8e8ee", "#c9a227", "♥")),
    ("portfolio-corporate", "Corporate", ("#e8eef5", "#37474f", "◆")),
    ("portfolio-portrait", "Portrait", ("#f5f0e8", "#8b7355", "○")),
]:
    w(
        f"photographie/images/{name}.svg",
        f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" role="img"><title>{title}</title>
  <defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="{mood[0]}"/><stop offset="100%" stop-color="#2a2622"/></linearGradient></defs>
  <rect width="800" height="520" fill="url(#g)"/>
  <rect x="50" y="50" width="700" height="380" fill="#1a1816" stroke="{mood[1]}" stroke-width="2" rx="4"/>
  <ellipse cx="400" cy="240" rx="160" ry="110" fill="{mood[0]}" opacity=".35"/>
  <text x="400" y="255" text-anchor="middle" font-size="48" fill="{mood[1]}" opacity=".4" font-family="Georgia,serif">{mood[2]}</text>
  <rect x="80" y="400" width="120" height="6" fill="{mood[1]}" opacity=".6"/>
  <text x="400" y="470" text-anchor="middle" fill="#c9a227" font-size="16" font-family="Georgia,serif">{title}</text>
</svg>""",
    )

# Extra portfolio (galerie future)
for name, title in [
    ("portfolio-reportage", "Reportage"),
    ("portfolio-architecture", "Architecture"),
    ("portfolio-mode", "Mode"),
]:
    w(
        f"photographie/images/{name}.svg",
        f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 480" role="img"><title>{title}</title>
  <rect width="640" height="480" fill="#2a2622"/>
  <rect x="30" y="40" width="580" height="360" fill="#1a1816" stroke="#c9a227" stroke-width="1"/>
  <rect x="70" y="80" width="500" height="280" fill="#3d3830" opacity=".85"/>
  <path d="M100 360 Q320 300 540 360" fill="none" stroke="#c9a227" stroke-width="2" class="vitrine-sketch-stroke"/>
  <text x="320" y="440" text-anchor="middle" fill="#c9a227" font-size="14" font-family="Georgia,serif">{title}</text>
</svg>""",
    )

# ——— Pulse Fitness Metz ———
w(
    "fitness/images/hero.svg",
    """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 520" role="img" aria-labelledby="t">
  <title id="t">Pulse Fitness Metz — salle et équipement</title>
  <defs>
    <linearGradient id="floor" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0a0a0a"/><stop offset="100%" stop-color="#1a1a1a"/></linearGradient>
    <radialGradient id="neon" cx="50%" cy="35%" r="60%"><stop offset="0%" stop-color="#65a30d" stop-opacity=".45"/><stop offset="100%" stop-color="#39ff14" stop-opacity="0"/></radialGradient>
  </defs>
  <rect width="1200" height="520" fill="url(#floor)"/>
  <ellipse cx="600" cy="180" rx="420" ry="200" fill="url(#neon)"/>
  <g stroke="#39ff14" stroke-width="12" fill="none" stroke-linecap="round">
    <line x1="220" y1="210" x2="480" y2="210"/>
    <rect x="200" y="188" width="40" height="44" rx="6" fill="#39ff14"/>
    <rect x="460" y="188" width="40" height="44" rx="6" fill="#39ff14"/>
  </g>
  <g transform="translate(520 100)">
    <rect x="0" y="60" width="380" height="280" rx="12" fill="#151515" stroke="#65a30d" stroke-width="2"/>
    <ellipse cx="120" cy="200" rx="70" ry="100" fill="#39ff14" opacity=".12"/>
    <path d="M90 80 Q120 40 150 80 L135 260 Q120 300 105 260 Z" fill="#65a30d" opacity=".25"/>
    <circle cx="280" cy="200" r="55" fill="none" stroke="#39ff14" stroke-width="4"/>
    <circle cx="280" cy="200" r="8" fill="#39ff14"/>
    <rect x="320" y="140" width="40" height="120" fill="#39ff14" opacity=".2" rx="4"/>
  </g>
  <g class="vitrine-sketch-stroke" fill="none" stroke="#65a30d" stroke-width="2" opacity=".4">
    <path d="M60 140 L140 200 L60 260"/><path d="M1140 120 L1060 180 L1140 240"/>
  </g>
  <text x="600" y="470" text-anchor="middle" font-family="system-ui,sans-serif" font-size="38" font-weight="800" fill="#39ff14" opacity=".2">PULSE FITNESS</text>
</svg>""",
)

for name, title, accent in [
    ("cours-hiit", "HIIT Burn", "#ff6b35"),
    ("cours-yoga", "Yoga Flow", "#a78bfa"),
    ("cours-cycling", "Cycling", "#39ff14"),
]:
    w(
        f"fitness/images/{name}.svg",
        f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" role="img"><title>{title}</title>
  <rect width="800" height="520" fill="#0d0d0d"/>
  <rect x="40" y="40" width="720" height="400" rx="14" fill="#151515" stroke="{accent}" stroke-width="2"/>
  <ellipse cx="400" cy="240" rx="180" ry="100" fill="{accent}" opacity=".12"/>
  <g transform="translate(400 200)">
    <circle cx="0" cy="0" r="50" fill="none" stroke="{accent}" stroke-width="3" opacity=".6"/>
    <path d="M-30 -20 L30 20 M30 -20 L-30 20" stroke="{accent}" stroke-width="4" stroke-linecap="round"/>
  </g>
  <text x="400" y="420" text-anchor="middle" fill="{accent}" font-size="20" font-family="system-ui,sans-serif" font-weight="700">{title}</text>
</svg>""",
    )

# ——— Atelier Nord-Est (architecture) ———
w(
    "architecture/images/hero.svg",
    """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 520" role="img" aria-labelledby="t">
  <title id="t">Atelier Nord-Est — façade et volumes</title>
  <rect width="1200" height="520" fill="#f5f3ef"/>
  <g transform="translate(140 40)">
    <polygon points="460,0 920,100 0,100" fill="#0a0a0a"/>
    <rect x="60" y="100" width="800" height="340" fill="#fff" stroke="#0a0a0a" stroke-width="3"/>
    <rect x="100" y="140" width="130" height="260" fill="#e8e4dc" stroke="#0a0a0a" stroke-width="2"/>
    <rect x="260" y="140" width="130" height="260" fill="#e8e4dc" stroke="#0a0a0a" stroke-width="2"/>
    <rect x="420" y="140" width="130" height="260" fill="#e0dcd4" stroke="#0a0a0a" stroke-width="2"/>
    <rect x="580" y="140" width="240" height="200" fill="#c45c26" opacity=".3" stroke="#0a0a0a" stroke-width="2"/>
    <line x1="60" y1="440" x2="860" y2="440" stroke="#0a0a0a" stroke-width="5"/>
    <rect x="700" y="200" width="80" height="120" fill="#87ceeb" opacity=".35" stroke="#0a0a0a" stroke-width="1"/>
  </g>
  <g class="vitrine-sketch-stroke" fill="none" stroke="#c45c26" stroke-width="2" opacity=".55">
    <path d="M80 180 Q320 80 560 160"/><circle cx="1000" cy="380" r="60" stroke="#0a0a0a" opacity=".3"/>
  </g>
  <text x="600" y="500" text-anchor="middle" font-family="monospace" font-size="12" fill="#0a0a0a" opacity=".4">ATELIER NORD-EST · METZ</text>
</svg>""",
)

for name, title, accent in [
    ("projet-metz", "24 logements passifs", "#2d5a4e"),
    ("projet-lux", "Siège social", "#1e3a5f"),
    ("projet-verdun", "Réhabilitation caserne", "#8b4513"),
]:
    w(
        f"architecture/images/{name}.svg",
        f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" role="img"><title>{title}</title>
  <rect width="800" height="520" fill="#f0ede8"/>
  <rect x="40" y="50" width="720" height="380" fill="#fff" stroke="#0a0a0a" stroke-width="2"/>
  <polygon points="400,50 720,120 80,120" fill="#0a0a0a"/>
  <rect x="80" y="140" width="100" height="260" fill="#e0dcd4" stroke="#0a0a0a" stroke-width="1"/>
  <rect x="200" y="140" width="100" height="260" fill="#e0dcd4" stroke="#0a0a0a" stroke-width="1"/>
  <rect x="320" y="140" width="380" height="180" fill="{accent}" opacity=".25" stroke="#0a0a0a" stroke-width="1"/>
  <text x="400" y="470" text-anchor="middle" font-family="monospace" font-size="13" fill="#0a0a0a" opacity=".6">{title}</text>
</svg>""",
    )

# ——— Rivière & Partenaires (juridique) ———
w(
    "juridique/images/hero.svg",
    """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 520" role="img" aria-labelledby="t">
  <title id="t">Rivière &amp; Partenaires — cabinet Metz</title>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#0f172a"/><stop offset="100%" stop-color="#1e293b"/></linearGradient>
  </defs>
  <rect width="1200" height="520" fill="url(#bg)"/>
  <g fill="#1e293b" stroke="#334155" stroke-width="2">
    <rect x="160" y="100" width="36" height="360"/><rect x="1004" y="100" width="36" height="360"/>
    <rect x="196" y="100" width="808" height="24" fill="#0f172a" stroke="none"/>
  </g>
  <g transform="translate(600 180)">
    <line x1="0" y1="0" x2="0" y2="220" stroke="#c9a227" stroke-width="7"/>
    <line x1="-200" y1="50" x2="200" y2="50" stroke="#c9a227" stroke-width="5"/>
    <path d="M-200 50 L-250 150 L-150 150 Z" fill="none" stroke="#94a3b8" stroke-width="3"/>
    <path d="M200 50 L150 150 L250 150 Z" fill="none" stroke="#94a3b8" stroke-width="3"/>
    <circle cx="0" cy="0" r="26" fill="#c9a227"/>
  </g>
  <rect x="280" y="320" width="640" height="80" rx="4" fill="#1e293b" stroke="#c9a227" stroke-width="1" opacity=".6"/>
  <g class="vitrine-sketch-stroke" fill="none" stroke="#c9a227" stroke-width="2" opacity=".45">
    <path d="M80 80 Q280 40 480 90"/><path d="M720 85 Q920 45 1120 95"/>
  </g>
  <text x="600" y="480" text-anchor="middle" font-family="Georgia,serif" font-size="13" fill="#c9a227" opacity=".5">RIVIÈRE &amp; PARTENAIRES · BARREAU DE METZ</text>
</svg>""",
)

for name, title, icon in [
    ("expertise-societes", "Droit des sociétés", "§"),
    ("expertise-social", "Droit social", "RH"),
    ("expertise-contentieux", "Contentieux", "⚖"),
]:
    w(
        f"juridique/images/{name}.svg",
        f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" role="img"><title>{title}</title>
  <defs><linearGradient id="b" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0f172a"/><stop offset="100%" stop-color="#334155"/></linearGradient></defs>
  <rect width="800" height="520" fill="url(#b)"/>
  <rect x="50" y="50" width="700" height="380" fill="#1e293b" stroke="#c9a227" stroke-width="2" rx="4"/>
  <text x="400" y="260" text-anchor="middle" font-size="72" fill="#c9a227" opacity=".25" font-family="Georgia,serif">{icon}</text>
  <rect x="100" y="380" width="200" height="4" fill="#c9a227" opacity=".7"/>
  <text x="400" y="430" text-anchor="middle" fill="#e2e8f0" font-size="16" font-family="system-ui,sans-serif">{title}</text>
</svg>""",
    )

# ——— Patrimoine Lorraine (immobilier) ———
w(
    "immobilier/images/hero.svg",
    """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 520" role="img" aria-labelledby="t">
  <title id="t">Patrimoine Lorraine — maison de maître et jardin</title>
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#8fb5a8"/><stop offset="100%" stop-color="#d4e8df"/></linearGradient>
    <linearGradient id="facade" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#f4efe6"/><stop offset="100%" stop-color="#e0d4c4"/></linearGradient>
    <linearGradient id="roof" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#1a3c34"/><stop offset="100%" stop-color="#2d5a4e"/></linearGradient>
  </defs>
  <rect width="1200" height="520" fill="url(#sky)"/>
  <ellipse cx="600" cy="490" rx="540" ry="70" fill="#b8d4c8" opacity=".5"/>
  <g transform="translate(260 90)">
    <polygon points="340,0 660,200 20,200" fill="url(#roof)"/>
    <rect x="60" y="200" width="560" height="240" fill="url(#facade)" stroke="#1a3c34" stroke-width="3"/>
    <rect x="220" y="280" width="100" height="160" fill="#1a3c34" opacity=".9"/>
    <rect x="360" y="260" width="75" height="60" fill="#b8954a" opacity=".95"/>
    <rect x="460" y="260" width="75" height="60" fill="#b8954a" opacity=".95"/>
    <rect x="360" y="335" width="75" height="60" fill="#b8954a" opacity=".75"/>
    <rect x="460" y="335" width="75" height="60" fill="#b8954a" opacity=".75"/>
    <path d="M0 440 Q140 400 280 440 T560 440" fill="none" stroke="#2d5a4e" stroke-width="4" class="vitrine-sketch-stroke"/>
  </g>
  <g fill="#2d5a4e" opacity=".45">
    <ellipse cx="140" cy="430" rx="55" ry="75"/><ellipse cx="1060" cy="410" rx="70" ry="90"/>
  </g>
  <g class="vitrine-sketch-stroke" fill="none" stroke="#b8954a" stroke-width="2" opacity=".55">
    <path d="M40 180 Q200 100 360 180"/><path d="M840 160 Q1000 80 1160 170"/>
  </g>
  <text x="600" y="505" text-anchor="middle" font-family="Georgia,serif" font-size="12" fill="#1a3c34" opacity=".5">PATRIMOINE LORRAINE · THIONVILLE</text>
</svg>""",
)

for name, title, rooms in [
    ("bien-thionville", "Thionville centre · 89 m²", "3 pièces"),
    ("bien-yutz", "Maison Yutz · 120 m²", "Jardin"),
    ("bien-sablon", "Loft Sablon", "Duplex"),
]:
    w(
        f"immobilier/images/{name}.svg",
        f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" role="img"><title>{title}</title>
  <defs><linearGradient id="s" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#d4e8df"/><stop offset="100%" stop-color="#8fb5a8"/></linearGradient></defs>
  <rect width="800" height="520" fill="url(#s)"/>
  <rect x="60" y="80" width="680" height="340" fill="#f4efe6" stroke="#1a3c34" stroke-width="2" rx="6"/>
  <polygon points="400,80 700,180 100,180" fill="#1a3c34"/>
  <rect x="140" y="200" width="90" height="180" fill="#1a3c34" opacity=".7"/>
  <rect x="280" y="220" width="60" height="50" fill="#b8954a"/><rect x="360" y="220" width="60" height="50" fill="#b8954a"/>
  <rect x="480" y="200" width="200" height="120" fill="#2d5a4e" opacity=".15" stroke="#1a3c34" stroke-width="1"/>
  <text x="400" y="450" text-anchor="middle" font-size="15" fill="#1a3c34" font-family="system-ui,sans-serif">{title}</text>
  <text x="400" y="475" text-anchor="middle" font-size="12" fill="#2d5a4e" opacity=".7">{rooms}</text>
</svg>""",
    )

w(
    "immobilier/images/equipe-agence.svg",
    """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" role="img"><title>Équipe agence Patrimoine Lorraine</title>
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#1a3c34"/><stop offset="100%" stop-color="#2d5a4e"/></linearGradient></defs>
  <rect width="800" height="520" fill="url(#bg)"/>
  <g transform="translate(120 100)">
    <circle cx="100" cy="80" r="45" fill="#f4efe6" opacity=".9"/><circle cx="280" cy="70" r="42" fill="#f4efe6" opacity=".85"/><circle cx="460" cy="85" r="48" fill="#f4efe6" opacity=".9"/>
    <rect x="50" y="150" width="100" height="180" rx="8" fill="#b8954a" opacity=".4"/><rect x="230" y="145" width="100" height="185" rx="8" fill="#b8954a" opacity=".35"/><rect x="410" y="155" width="100" height="175" rx="8" fill="#b8954a" opacity=".4"/>
  </g>
  <text x="400" y="470" text-anchor="middle" fill="#f4efe6" font-size="14" font-family="system-ui,sans-serif" opacity=".8">Votre équipe locale</text>
</svg>""",
)

print("OK — SVG premium : photographie, fitness, architecture, juridique, immobilier")
