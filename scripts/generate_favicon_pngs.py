#!/usr/bin/env python3
"""
Génère le pack de favicons PNG + manifest / browserconfig alignés sur la palette bleue.

Utilise uniquement Pillow + NumPy (pas de Cairo). Sortie : assets/icons/favicons/

Usage :
  pip install -r requirements-scripts.txt
  python scripts/generate_favicon_pngs.py
"""
from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "icons" / "favicons"
SVG_PATH = ROOT / "assets" / "icons" / "favicon.svg"

# Stops du dégradé (aligné sur favicon.svg / --metal-blue-gradient)
STOPS = [
    (0.0, (0x9F, 0xD4, 0xEA)),
    (0.28, (0x5F, 0xAE, 0xD8)),
    (0.62, (0x2F, 0x78, 0xA6)),
    (1.0, (0x18, 0x4C, 0x70)),
]

THEME = "#2f78a6"
BG_SPLASH = "#f0f9ff"


def _gradient_rgb(t: "np.ndarray") -> tuple["np.ndarray", "np.ndarray", "np.ndarray"]:
    import numpy as np

    stops_t = np.array([s[0] for s in STOPS], dtype=np.float32)
    r_stops = np.array([s[1][0] for s in STOPS], dtype=np.float32)
    g_stops = np.array([s[1][1] for s in STOPS], dtype=np.float32)
    b_stops = np.array([s[1][2] for s in STOPS], dtype=np.float32)
    tf = np.clip(t.flatten(), 0.0, 1.0)
    r = np.interp(tf, stops_t, r_stops).reshape(t.shape)
    g = np.interp(tf, stops_t, g_stops).reshape(t.shape)
    b = np.interp(tf, stops_t, b_stops).reshape(t.shape)
    return r, g, b


def render_icon(size: int) -> Image.Image:
    """Icône carrée avec coins arrondis (rx ≈ 6/32) et texte DC."""
    s = max(16, size)
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    mask = Image.new("L", (s, s), 0)
    draw_m = ImageDraw.Draw(mask)
    rad = max(2, int(round(s * 6 / 32)))
    draw_m.rounded_rectangle((0, 0, s - 1, s - 1), radius=rad, fill=255)

    import numpy as np

    x = np.linspace(0, 1, s, dtype=np.float32)
    y = np.linspace(0, 1, s, dtype=np.float32)
    xv, yv = np.meshgrid(x, y)
    t = (xv + yv) / 2.0
    r, g, b = _gradient_rgb(t)
    rgb = np.stack([r, g, b], axis=-1).astype(np.uint8)
    base = Image.fromarray(rgb).convert("RGBA")
    base.putalpha(mask)
    img = Image.alpha_composite(Image.new("RGBA", (s, s), (0, 0, 0, 0)), base)

    # Bordure claire (comme le SVG)
    border = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    bd = ImageDraw.Draw(border)
    bd.rounded_rectangle(
        (0, 0, s - 1, s - 1),
        radius=rad,
        outline=(255, 255, 255, 90),
        width=max(1, s // 32),
    )
    img = Image.alpha_composite(img, border)

    # Texte DC
    draw = ImageDraw.Draw(img)
    font_size = max(8, int(s * 13 / 32))
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except OSError:
        try:
            font = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", font_size)
        except OSError:
            font = ImageFont.load_default()

    text = "DC"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = (s - tw) / 2
    ty = (s - th) / 2 - bbox[1]
    draw.text((tx, ty), text, fill=(255, 255, 255, 255), font=font)
    return img


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    sizes = {
        "favicon-16x16.png": 16,
        "favicon-32x32.png": 32,
        "favicon-96x96.png": 96,
        "android-icon-192x192.png": 192,
        "apple-icon-57x57.png": 57,
        "apple-icon-60x60.png": 60,
        "apple-icon-72x72.png": 72,
        "apple-icon-76x76.png": 76,
        "apple-icon-114x114.png": 114,
        "apple-icon-120x120.png": 120,
        "apple-icon-144x144.png": 144,
        "apple-icon-152x152.png": 152,
        "apple-icon-180x180.png": 180,
        "ms-icon-144x144.png": 144,
    }

    for name, dim in sizes.items():
        im = render_icon(dim)
        im.save(OUT_DIR / name, "PNG", optimize=True)
        print(f"[OK] {name}")

    # favicon.ico racine du pack (copie 32x32 en ICO multi-résolution simplifiée : une taille)
    im32 = render_icon(32)
    im32.save(OUT_DIR / "favicon.ico", format="ICO", sizes=[(32, 32)])

    manifest = {
        "name": "DanielCraft",
        "short_name": "DanielCraft",
        "description": "Développeur Full-Stack — sites, identité, SEO",
        "start_url": "/",
        "display": "standalone",
        "background_color": BG_SPLASH,
        "theme_color": THEME,
        "icons": [
            {
                "src": "/assets/icons/favicons/android-icon-192x192.png",
                "sizes": "192x192",
                "type": "image/png",
                "purpose": "any maskable",
            }
        ],
    }
    (OUT_DIR / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print("[OK] manifest.json")

    browserconfig = f"""<?xml version="1.0" encoding="utf-8"?>
<browserconfig>
  <msapplication>
    <tile>
      <square150x150logo src="/assets/icons/favicons/ms-icon-144x144.png"/>
      <TileColor>{THEME}</TileColor>
    </tile>
  </msapplication>
</browserconfig>
"""
    (OUT_DIR / "browserconfig.xml").write_text(browserconfig, encoding="utf-8")
    print("[OK] browserconfig.xml")

    print(f"\n[DONE] Favicons générés dans {OUT_DIR.relative_to(ROOT)}")
    print(f"Source SVG de référence : {SVG_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
