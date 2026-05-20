#!/usr/bin/env python3
"""Generate hero and card SVG illustrations for vitrine demos."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "assets" / "vitrines" / "demos"


def w(rel: str, body: str) -> None:
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body.strip() + "\n", encoding="utf-8")


# --- Technologie ---
w(
    "technologie/images/hero.svg",
    """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 520" role="img" aria-labelledby="t">
  <title id="t">Datacenter et réseau — illustration tech</title>
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0d1b2a"/><stop offset="100%" stop-color="#1b263b"/></linearGradient>
    <linearGradient id="rack" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#1e3a5f"/><stop offset="100%" stop-color="#0f2744"/></linearGradient>
    <linearGradient id="glow" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#64b5f6"/><stop offset="100%" stop-color="#7c4dff"/></linearGradient>
  </defs>
  <rect width="1200" height="520" fill="url(#sky)"/>
  <g opacity=".15" stroke="#64b5f6" stroke-width="1" fill="none">
    <path d="M0 80 H1200 M0 160 H1200 M0 240 H1200 M0 320 H1200 M0 400 H1200"/>
    <path d="M150 0 V520 M350 0 V520 M550 0 V520 M750 0 V520 M950 0 V520"/>
  </g>
  <g transform="translate(200 90)">
    <rect x="0" y="40" width="120" height="280" rx="6" fill="url(#rack)" stroke="#64b5f6" stroke-width="2"/>
    <rect x="140" y="40" width="120" height="280" rx="6" fill="url(#rack)" stroke="#64b5f6" stroke-width="2"/>
    <rect x="280" y="40" width="120" height="280" rx="6" fill="url(#rack)" stroke="#7c4dff" stroke-width="2"/>
    <rect x="420" y="40" width="120" height="280" rx="6" fill="url(#rack)" stroke="#64b5f6" stroke-width="2"/>
    <g fill="#39ff14" opacity=".85">
      <circle cx="30" cy="80" r="4"/><circle cx="60" cy="80" r="4"/><circle cx="90" cy="80" r="4"/>
      <circle cx="30" cy="120" r="4"/><circle cx="60" cy="120" r="4"/>
      <circle cx="170" cy="100" r="4"/><circle cx="200" cy="100" r="4"/><circle cx="230" cy="100" r="4"/>
      <circle cx="310" cy="90" r="4"/><circle cx="340" cy="130" r="4"/><circle cx="450" cy="110" r="4"/>
    </g>
    <rect x="560" y="120" width="200" height="8" rx="4" fill="url(#glow)" opacity=".7"/>
    <path d="M560 128 Q680 200 760 128" fill="none" stroke="#7c4dff" stroke-width="3" class="vitrine-sketch-stroke" opacity=".6"/>
  </g>
  <g class="vitrine-sketch-stroke" fill="none" stroke="#64b5f6" stroke-width="2" opacity=".5">
    <path d="M80 420 Q200 360 320 420 T560 400"/>
    <ellipse cx="1000" cy="380" rx="90" ry="50" stroke="#7c4dff"/>
    <path d="M950 350 L1050 350 L1020 420 L980 420 Z"/>
  </g>
  <text x="600" y="490" text-anchor="middle" font-family="system-ui,sans-serif" font-size="14" fill="#64b5f6" opacity=".4">SYNAPSE · CLOUD RÉGIONAL</text>
</svg>""",
)

for i, (title, accent) in enumerate(
    [
        ("API & microservices", "#64b5f6"),
        ("Data lakehouse", "#7c4dff"),
        ("Sécurité Zero Trust", "#4fc3f7"),
    ],
    1,
):
    w(
        f"technologie/images/card-{i}.svg",
        f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" role="img"><title>{title}</title>
  <defs><linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#1b263b"/><stop offset="100%" stop-color="#0d1b2a"/></linearGradient></defs>
  <rect width="800" height="520" fill="url(#bg)"/>
  <rect x="80" y="100" width="640" height="280" rx="12" fill="#1e3a5f" stroke="{accent}" stroke-width="2"/>
  <circle cx="200" cy="220" r="50" fill="none" stroke="{accent}" stroke-width="3"/>
  <path d="M320 180 L480 180 L480 320 L320 320 Z" fill="{accent}" opacity=".25" stroke="{accent}" stroke-width="2"/>
  <g class="vitrine-sketch-stroke" fill="none" stroke="{accent}" stroke-width="2" opacity=".5"><path d="M100 80 Q400 40 700 100"/></g>
</svg>""",
    )

# --- Restauration ---
w(
    "restauration/images/hero.svg",
    """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 520" role="img" aria-labelledby="t">
  <title id="t">Brasserie — salle et dressage</title>
  <defs>
    <linearGradient id="amb" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#3d1414"/><stop offset="100%" stop-color="#722f37"/></linearGradient>
    <linearGradient id="gold" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#e8c547"/><stop offset="100%" stop-color="#c9a227"/></linearGradient>
  </defs>
  <rect width="1200" height="520" fill="url(#amb)"/>
  <ellipse cx="600" cy="480" rx="500" ry="60" fill="#2a1010" opacity=".5"/>
  <g transform="translate(180 80)">
    <rect x="0" y="120" width="840" height="200" rx="8" fill="#4a2020" stroke="#e8c547" stroke-width="2"/>
    <circle cx="120" cy="220" r="35" fill="url(#gold)" opacity=".9"/>
    <circle cx="280" cy="200" r="28" fill="#f5e6d3" stroke="#e8c547" stroke-width="2"/>
    <circle cx="420" cy="230" r="32" fill="#8b4513" opacity=".8"/>
    <rect x="520" y="160" width="180" height="100" rx="6" fill="#5c2a2a" stroke="#e8c547" stroke-width="1"/>
    <path d="M60 80 Q200 40 360 90 Q520 130 700 70" fill="none" stroke="#e8c547" stroke-width="3" class="vitrine-sketch-stroke"/>
  </g>
  <g fill="#e8c547" opacity=".3"><ellipse cx="150" cy="100" rx="8" ry="12"/><ellipse cx="200" cy="90" rx="6" ry="10"/></g>
</svg>""",
)

for i, label in enumerate(["Carte du jour", "Terrasse ombragée", "Cave à vins"], 1):
    w(
        f"restauration/images/card-{i}.svg",
        f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" role="img"><title>{label}</title>
  <rect width="800" height="520" fill="#fff8f0"/>
  <rect x="60" y="80" width="680" height="320" rx="10" fill="#722f37" opacity=".15" stroke="#722f37" stroke-width="2"/>
  <ellipse cx="400" cy="260" rx="120" ry="80" fill="#e8c547" opacity=".4"/>
  <path d="M200 200 Q400 120 600 200" fill="none" stroke="#722f37" stroke-width="3" class="vitrine-sketch-stroke"/>
</svg>""",
    )

# --- Beauté ---
w(
    "beaute/images/hero.svg",
    """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 520" role="img" aria-labelledby="t">
  <title id="t">Institut spa — cabine bien-être</title>
  <defs>
    <linearGradient id="rose" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f8e8ee"/><stop offset="100%" stop-color="#e8d0dc"/></linearGradient>
    <linearGradient id="mauve" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#8b5a6b"/><stop offset="100%" stop-color="#5c3d4d"/></linearGradient>
  </defs>
  <rect width="1200" height="520" fill="url(#rose)"/>
  <g transform="translate(220 60)">
    <rect x="0" y="80" width="760" height="280" rx="16" fill="#fff" stroke="#8b5a6b" stroke-width="2"/>
    <ellipse cx="380" cy="220" rx="200" ry="90" fill="#f0d8e4" stroke="#8b5a6b" stroke-width="2"/>
    <circle cx="200" cy="180" r="40" fill="url(#mauve)" opacity=".3"/>
    <path d="M100 360 Q380 300 660 360" fill="none" stroke="#8b5a6b" stroke-width="3" class="vitrine-sketch-stroke"/>
    <g fill="#c9a0b0" opacity=".6"><ellipse cx="600" cy="140" rx="30" ry="50"/><ellipse cx="650" cy="160" rx="25" ry="40"/></g>
  </g>
</svg>""",
)

for i, t in enumerate(["Soin visage", "Massage relaxant", "Boutique produits"], 1):
    w(
        f"beaute/images/card-{i}.svg",
        f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" role="img"><title>{t}</title>
  <rect width="800" height="520" fill="#fdf5f8"/>
  <rect x="100" y="100" width="600" height="300" rx="12" fill="#e8d0dc" stroke="#8b5a6b" stroke-width="2"/>
  <circle cx="400" cy="250" r="70" fill="#8b5a6b" opacity=".2"/>
  <path d="M150 400 Q400 320 650 400" fill="none" stroke="#5c3d4d" stroke-width="2" class="vitrine-sketch-stroke"/>
</svg>""",
    )

# --- Odontologie ---
w(
    "odontologie/images/hero.svg",
    """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 520" role="img" aria-labelledby="t">
  <title id="t">Cabinet dentaire — salle de soins</title>
  <defs>
    <linearGradient id="clin" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e8f4fc"/><stop offset="100%" stop-color="#d0e8f5"/></linearGradient>
  </defs>
  <rect width="1200" height="520" fill="url(#clin)"/>
  <g transform="translate(200 70)">
    <rect x="0" y="100" width="800" height="260" rx="12" fill="#fff" stroke="#0d7ea8" stroke-width="2"/>
    <rect x="80" y="180" width="200" height="120" rx="8" fill="#b8e0f0" stroke="#0d7ea8" stroke-width="2"/>
    <circle cx="500" cy="220" r="60" fill="#0d7ea8" opacity=".15"/>
    <path d="M300 160 L380 160 L360 280 L320 280 Z" fill="#0d7ea8" opacity=".25"/>
    <ellipse cx="650" cy="200" rx="80" ry="40" fill="#fff" stroke="#0d7ea8" stroke-width="2"/>
    <path d="M40 380 Q400 340 760 380" fill="none" stroke="#0d7ea8" stroke-width="3" class="vitrine-sketch-stroke" opacity=".5"/>
  </g>
  <text x="600" y="480" text-anchor="middle" font-size="13" fill="#0d7ea8" opacity=".5">MOSAÏQUE · SOINS &amp; PRÉVENTION</text>
</svg>""",
)

for i, t in enumerate(["Salle de soins", "Équipe pluridisciplinaire", "Prévention"], 1):
    w(
        f"odontologie/images/card-{i}.svg",
        f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" role="img"><title>{t}</title>
  <rect width="800" height="520" fill="#e8f4fc"/>
  <rect x="80" y="90" width="640" height="300" rx="10" fill="#fff" stroke="#0d7ea8" stroke-width="2"/>
  <circle cx="400" cy="240" r="55" fill="#0d7ea8" opacity=".12"/>
  <path d="M120 420 Q400 360 680 420" fill="none" stroke="#0d7ea8" stroke-width="2" class="vitrine-sketch-stroke"/>
</svg>""",
    )

# --- Industrie ---
w(
    "industrie/images/hero.svg",
    """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 520" role="img" aria-labelledby="t">
  <title id="t">Usine — ligne d'usinage</title>
  <defs>
    <linearGradient id="dark" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#1a1a1a"/><stop offset="100%" stop-color="#2d2d2d"/></linearGradient>
  </defs>
  <rect width="1200" height="520" fill="url(#dark)"/>
  <g transform="translate(150 80)">
    <rect x="0" y="140" width="900" height="180" fill="#333" stroke="#ffb300" stroke-width="2"/>
    <rect x="80" y="80" width="160" height="100" fill="#444" stroke="#ffb300" stroke-width="2"/>
    <circle cx="400" cy="230" r="50" fill="none" stroke="#ffb300" stroke-width="4"/>
    <rect x="520" y="160" width="280" height="100" fill="#3a3a3a" stroke="#ff8f00" stroke-width="2"/>
    <path d="M0 360 H900" stroke="#ffb300" stroke-width="4" class="vitrine-sketch-stroke"/>
    <g fill="#ffb300" opacity=".7"><rect x="200" y="200" width="40" height="60"/><rect x="600" y="190" width="30" height="70"/></g>
  </g>
  <g fill="none" stroke="#ff8f00" stroke-width="2" opacity=".4" class="vitrine-sketch-stroke"><path d="M100 100 L300 60 L500 120"/></g>
</svg>""",
)

for i, t in enumerate(["Ligne production", "Contrôle qualité", "Plan usine"], 1):
    w(
        f"industrie/images/card-{i}.svg",
        f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" role="img"><title>{t}</title>
  <rect width="800" height="520" fill="#1a1a1a"/>
  <rect x="60" y="100" width="680" height="300" rx="8" fill="#2d2d2d" stroke="#ffb300" stroke-width="2"/>
  <rect x="200" y="180" width="400" height="80" fill="#ffb300" opacity=".2"/>
  <circle cx="400" cy="250" r="40" fill="none" stroke="#ff8f00" stroke-width="3"/>
</svg>""",
    )

# --- Association ---
w(
    "association/images/hero.svg",
    """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 520" role="img" aria-labelledby="t">
  <title id="t">Solidarité — bénévoles et quartier</title>
  <defs>
    <linearGradient id="green" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#d4edda"/><stop offset="100%" stop-color="#a8d5b5"/></linearGradient>
  </defs>
  <rect width="1200" height="520" fill="url(#green)"/>
  <g transform="translate(180 100)">
    <circle cx="200" cy="120" r="50" fill="#48c774" opacity=".4" stroke="#2e7d4e" stroke-width="2"/>
    <circle cx="400" cy="100" r="45" fill="#48c774" opacity=".35" stroke="#2e7d4e" stroke-width="2"/>
    <circle cx="600" cy="130" r="48" fill="#48c774" opacity=".4" stroke="#2e7d4e" stroke-width="2"/>
    <path d="M120 280 Q400 220 680 280 L640 360 L160 360 Z" fill="#fff" stroke="#2e7d4e" stroke-width="2"/>
    <rect x="300" y="200" width="200" height="80" rx="8" fill="#ffdd57" opacity=".6" stroke="#2e7d4e" stroke-width="2"/>
    <path d="M0 380 Q400 320 840 380" fill="none" stroke="#2e7d4e" stroke-width="3" class="vitrine-sketch-stroke"/>
  </g>
</svg>""",
)

for i, t in enumerate(["Maraude", "Cuisine solidaire", "Fête de quartier"], 1):
    w(
        f"association/images/card-{i}.svg",
        f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" role="img"><title>{t}</title>
  <rect width="800" height="520" fill="#e8f5e9"/>
  <rect x="80" y="100" width="640" height="300" rx="12" fill="#fff" stroke="#48c774" stroke-width="2"/>
  <circle cx="400" cy="250" r="80" fill="#48c774" opacity=".2"/>
  <path d="M150 400 Q400 320 650 400" fill="none" stroke="#2e7d4e" stroke-width="2" class="vitrine-sketch-stroke"/>
</svg>""",
    )

# --- Fitness ---
w(
    "fitness/images/hero.svg",
    """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 520" role="img" aria-labelledby="t">
  <title id="t">Salle Pulse Fitness — musculation et cours</title>
  <defs>
    <linearGradient id="floor" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0d0d0d"/><stop offset="100%" stop-color="#1a1a1a"/></linearGradient>
    <radialGradient id="neon" cx="50%" cy="40%" r="50%"><stop offset="0%" stop-color="#39ff14" stop-opacity=".35"/><stop offset="100%" stop-color="#39ff14" stop-opacity="0"/></radialGradient>
  </defs>
  <rect width="1200" height="520" fill="url(#floor)"/>
  <ellipse cx="600" cy="200" rx="350" ry="180" fill="url(#neon)"/>
  <g stroke="#39ff14" stroke-width="10" fill="none" stroke-linecap="round">
    <line x1="280" y1="200" x2="520" y2="200"/>
    <rect x="260" y="180" width="36" height="40" fill="#39ff14" rx="4"/>
    <rect x="504" y="180" width="36" height="40" fill="#39ff14" rx="4"/>
  </g>
  <g transform="translate(620 120)">
    <ellipse cx="80" cy="140" rx="55" ry="90" fill="#39ff14" opacity=".12"/>
    <path d="M50 60 Q80 20 110 60 L95 200 Q80 250 65 200 Z" fill="#39ff14" opacity=".22"/>
    <rect x="140" y="100" width="200" height="120" rx="8" fill="#222" stroke="#39ff14" stroke-width="2"/>
    <circle cx="240" cy="160" r="35" fill="none" stroke="#39ff14" stroke-width="3"/>
  </g>
  <g class="vitrine-sketch-stroke" fill="none" stroke="#39ff14" stroke-width="2" opacity=".45">
    <path d="M80 120 L180 170 L80 220"/><path d="M1120 100 L1020 150 L1120 200"/>
  </g>
  <text x="600" y="470" text-anchor="middle" font-family="system-ui,sans-serif" font-size="42" font-weight="800" fill="#39ff14" opacity=".25">PULSE</text>
</svg>""",
)

for name, title in [
    ("cours-hiit", "HIIT Burn"),
    ("cours-yoga", "Yoga Flow"),
    ("cours-cycling", "Cycling"),
]:
    w(
        f"fitness/images/{name}.svg",
        f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 400" role="img"><title>{title}</title>
  <rect width="640" height="400" fill="#111"/>
  <rect x="40" y="50" width="560" height="280" rx="10" fill="#1a1a1a" stroke="#39ff14" stroke-width="2"/>
  <ellipse cx="320" cy="190" rx="100" ry="60" fill="#39ff14" opacity=".15"/>
  <path d="M120 320 Q320 260 520 320" fill="none" stroke="#39ff14" stroke-width="3" class="vitrine-sketch-stroke"/>
  <text x="320" y="360" text-anchor="middle" fill="#39ff14" font-size="18" font-family="system-ui" opacity=".6">{title}</text>
</svg>""",
    )

# --- Architecture ---
w(
    "architecture/images/hero.svg",
    """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 520" role="img" aria-labelledby="t">
  <title id="t">Façade contemporaine — atelier d'architecture</title>
  <rect width="1200" height="520" fill="#f5f3ef"/>
  <g transform="translate(200 60)">
    <rect x="0" y="80" width="800" height="320" fill="#fff" stroke="#0a0a0a" stroke-width="3"/>
    <rect x="60" y="120" width="120" height="200" fill="#e8e4dc" stroke="#0a0a0a" stroke-width="2"/>
    <rect x="220" y="120" width="120" height="200" fill="#e8e4dc" stroke="#0a0a0a" stroke-width="2"/>
    <rect x="380" y="120" width="120" height="200" fill="#e8e4dc" stroke="#0a0a0a" stroke-width="2"/>
    <rect x="540" y="120" width="120" height="200" fill="#c45c26" opacity=".35" stroke="#0a0a0a" stroke-width="2"/>
    <polygon points="400,0 800,80 0,80" fill="#0a0a0a"/>
    <line x1="0" y1="400" x2="800" y2="400" stroke="#0a0a0a" stroke-width="4"/>
  </g>
  <g class="vitrine-sketch-stroke" fill="none" stroke="#c45c26" stroke-width="2" opacity=".5"><path d="M80 200 Q300 100 520 180"/></g>
</svg>""",
)

for name, title in [
    ("projet-metz", "24 logements passifs"),
    ("projet-lux", "Siège social"),
    ("projet-verdun", "Réhabilitation caserne"),
]:
    w(
        f"architecture/images/{name}.svg",
        f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 480" role="img"><title>{title}</title>
  <rect width="720" height="480" fill="#f0ede8"/>
  <rect x="40" y="60" width="640" height="340" fill="#fff" stroke="#0a0a0a" stroke-width="2"/>
  <rect x="80" y="100" width="100" height="260" fill="#e0dcd4" stroke="#0a0a0a" stroke-width="1"/>
  <rect x="220" y="100" width="100" height="260" fill="#e0dcd4" stroke="#0a0a0a" stroke-width="1"/>
  <rect x="360" y="100" width="260" height="180" fill="#c45c26" opacity=".25" stroke="#0a0a0a" stroke-width="1"/>
  <text x="360" y="430" text-anchor="middle" font-family="monospace" font-size="12" fill="#0a0a0a" opacity=".5">{title}</text>
</svg>""",
    )

# --- Photographie ---
w(
    "photographie/images/hero.svg",
    """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 520" role="img" aria-labelledby="t">
  <title id="t">Studio photo — lumière naturelle</title>
  <defs>
    <linearGradient id="sand" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#f5f0e8"/><stop offset="100%" stop-color="#e8dfd0"/></linearGradient>
  </defs>
  <rect width="1200" height="520" fill="url(#sand)"/>
  <g transform="translate(250 80)">
    <rect x="0" y="60" width="700" height="320" fill="#2a2a2a" stroke="#1a1a1a" stroke-width="2" rx="4"/>
    <circle cx="350" cy="220" r="100" fill="#fff" opacity=".9" stroke="#c9a227" stroke-width="3"/>
    <circle cx="350" cy="220" r="60" fill="#e8e0d4"/>
    <rect x="520" y="120" width="140" height="200" fill="#f5f0e8" stroke="#1a1a1a" stroke-width="2"/>
    <path d="M80 380 Q350 300 620 380" fill="none" stroke="#8b7355" stroke-width="3" class="vitrine-sketch-stroke"/>
  </g>
  <ellipse cx="150" cy="150" rx="80" ry="120" fill="#fff" opacity=".15"/>
</svg>""",
)

for name, title in [
    ("portfolio-mariage", "Mariage"),
    ("portfolio-portrait", "Portrait"),
    ("portfolio-corporate", "Corporate"),
    ("portfolio-reportage", "Reportage"),
    ("portfolio-architecture", "Architecture"),
    ("portfolio-mode", "Mode"),
]:
    w(
        f"photographie/images/{name}.svg",
        f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 480" role="img"><title>{title}</title>
  <rect width="640" height="480" fill="#2a2622"/>
  <rect x="30" y="40" width="580" height="380" fill="#1a1816" stroke="#c9a227" stroke-width="1"/>
  <rect x="80" y="90" width="480" height="280" fill="#3d3830" opacity=".8"/>
  <circle cx="320" cy="230" r="70" fill="#f5f0e8" opacity=".15"/>
  <text x="320" y="450" text-anchor="middle" fill="#c9a227" font-size="14" font-family="Georgia,serif">{title}</text>
</svg>""",
    )

# --- Commerce ---
w(
    "commerce/images/hero.svg",
    """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 520" role="img"><title>Halles couvertes Thionville</title>
  <rect width="1200" height="520" fill="#1b5e3a"/>
  <rect x="80" y="120" width="1040" height="280" fill="#faf6ef" opacity=".15" stroke="#c9a227" stroke-width="3"/>
  <circle cx="300" cy="260" r="80" fill="#c9a227" opacity=".4"/>
  <path d="M200 400 Q600 320 1000 400" fill="none" stroke="#c9a227" stroke-width="4" class="vitrine-sketch-stroke"/>
  <text x="600" y="480" text-anchor="middle" fill="#c9a227" font-size="16">HALLES THIONVILLE</text>
</svg>""",
)

# --- Comptable, Banque, Education, Services (card sets) ---
for slug, colors in [
    ("comptable", ("#0c2340", "#c9a227")),
    ("banque", ("#1e3a5f", "#c9a227")),
    ("education", ("#0f2744", "#e8c547")),
    ("services", ("#0ea5e9", "#111")),
]:
    for i, title in enumerate(["Offre A", "Offre B", "Offre C"], 1):
        w(
            f"{slug}/images/card-{i}.svg",
            f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" role="img"><title>{title}</title>
  <rect width="800" height="520" fill="{colors[0]}"/>
  <rect x="60" y="80" width="680" height="320" rx="12" fill="#fff" opacity=".12" stroke="{colors[1]}" stroke-width="2"/>
  <text x="400" y="280" text-anchor="middle" fill="{colors[1]}" font-size="22">{title}</text>
</svg>""",
        )

print("SVG vitrines générés.")
