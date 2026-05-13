#!/usr/bin/env python3
"""
Génère about-section-hero.png et .webp à partir de la même composition que
`assets/images/about-section-hero.svg` (charte bleu DanielCraft), sans Cairo / Inkscape.

Usage :
  python scripts/rasterize_about_hero.py
  python scripts/rasterize_about_hero.py --size 1600
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "images"


def _hex_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def _gradient_card(w: int, h: int) -> Image.Image:
    c0 = np.array(_hex_rgb("#7bcde3"), dtype=np.float32)
    c1 = np.array(_hex_rgb("#4da9d6"), dtype=np.float32)
    c2 = np.array(_hex_rgb("#2f78a6"), dtype=np.float32)
    y = np.linspace(0.0, 1.0, h, dtype=np.float32)[:, np.newaxis]
    mask_low = y < 0.45
    t1 = np.clip(y / 0.45, 0.0, 1.0)
    t2 = np.clip((y - 0.45) / 0.55, 0.0, 1.0)
    rgb = np.zeros((h, w, 3), dtype=np.float32)
    for i in range(3):
        low = c0[i] + (c1[i] - c0[i]) * t1
        high = c1[i] + (c2[i] - c1[i]) * t2
        rgb[:, :, i] = np.where(mask_low, low, high)
    return Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8))


def _shine_overlay(w: int, h: int, shine_h: int) -> Image.Image:
    """Bande supérieure blanche très transparente (comme le SVG)."""
    sh = min(shine_h, h)
    alpha = np.zeros((h, w), dtype=np.float32)
    if sh > 0:
        grad = np.linspace(0.14, 0.0, sh, dtype=np.float32)[:, np.newaxis]
        alpha[:sh, :] = grad * 255.0
    rgba = np.zeros((h, w, 4), dtype=np.uint8)
    rgba[:, :, 0:3] = 255
    rgba[:, :, 3] = np.clip(alpha, 0, 255).astype(np.uint8)
    return Image.fromarray(rgba, "RGBA")


def rasterize(size: int) -> Image.Image:
    s = size / 800.0
    img = Image.new("RGBA", (size, size), _hex_rgb("#f3f4f6") + (255,))

    x1 = int(round(72 * s))
    y1 = int(round(72 * s))
    x2 = int(round((72 + 656) * s))
    y2 = int(round((72 + 656) * s))
    r = max(2, int(round(52 * s)))
    cw, ch = x2 - x1, y2 - y1

    # Ombre portée (feDropShadow simplifié)
    shadow_layer = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow_layer)
    ox, oy = int(round(4 * s)), int(round(14 * s))
    sd.rounded_rectangle(
        [x1 + ox, y1 + oy, x2 + ox, y2 + oy],
        radius=r,
        fill=(15, 53, 80, 70),
    )
    shadow_layer = shadow_layer.filter(
        ImageFilter.GaussianBlur(radius=max(4, int(round(18 * s))))
    )
    img.alpha_composite(shadow_layer)

    grad = _gradient_card(cw, ch)
    mask = Image.new("L", (cw, ch), 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle([0, 0, cw - 1, ch - 1], radius=r, fill=255)
    card = Image.merge("RGBA", (*grad.convert("RGB").split(), mask))

    shine = _shine_overlay(cw, ch, int(round(320 * s)))
    card = Image.alpha_composite(card.convert("RGBA"), shine)

    img.paste(card, (x1, y1), card)

    dr = ImageDraw.Draw(img)

    # Motifs courbes + points
    lw = max(2, int(round(5 * s)))
    pale = (232, 244, 251, int(255 * 0.35))
    dr.line(
        [(int(140 * s), int(620 * s)), (int(220 * s), int(540 * s)), (int(360 * s), int(640 * s))],
        fill=pale,
        width=lw,
        joint="curve",
    )
    dr.line(
        [(int(620 * s), int(600 * s)), (int(540 * s), int(520 * s)), (int(420 * s), int(630 * s))],
        fill=pale,
        width=lw,
        joint="curve",
    )
    for cx, cy, rad, op in (
        (160, 240, 8, 0.5),
        (640, 280, 6, 0.45),
        (680, 520, 7, 0.4),
    ):
        rr = int(round(rad * s))
        a = int(255 * op)
        bbox = [
            int(round(cx * s)) - rr,
            int(round(cy * s)) - rr,
            int(round(cx * s)) + rr,
            int(round(cy * s)) + rr,
        ]
        dr.ellipse(bbox, fill=(232, 244, 251, a))

    # Accolades
    bw = max(4, int(round(12 * s)))
    white = (255, 255, 255, int(255 * 0.42))
    dr.line(
        [(int(210 * s), int(520 * s)), (int(175 * s), int(400 * s)), (int(210 * s), int(280 * s))],
        fill=white,
        width=bw,
        joint="curve",
    )
    dr.line(
        [(int(590 * s), int(520 * s)), (int(625 * s), int(400 * s)), (int(590 * s), int(280 * s))],
        fill=white,
        width=bw,
        joint="curve",
    )

    cx, cy = int(round(400 * s)), int(round(318 * s))
    head_r = int(round(78 * s))
    dr.ellipse(
        [cx - head_r, cy - head_r, cx + head_r, cy + head_r],
        fill=(240, 249, 255, int(255 * 0.95)),
    )
    dr.ellipse(
        [
            cx - int(round(82 * s)),
            cy - int(round(54 * s)),
            cx + int(round(82 * s)),
            cy + int(round(90 * s)),
        ],
        fill=(240, 249, 255, int(255 * 0.35)),
    )
    # Corps (trapèze arrondi simplifié)
    body = [
        (cx - int(118 * s), cy + int(108 * s)),
        (cx - int(118 * s), cy + int(48 * s)),
        (cx - int(66 * s), cy + int(36 * s)),
        (cx, cy + int(36 * s)),
        (cx + int(66 * s), cy + int(36 * s)),
        (cx + int(118 * s), cy + int(48 * s)),
        (cx + int(118 * s), cy + int(108 * s)),
        (cx + int(118 * s), cy + int(268 * s)),
        (cx + int(92 * s), cy + int(312 * s)),
        (cx + int(52 * s), cy + int(338 * s)),
        (cx - int(52 * s), cy + int(338 * s)),
        (cx - int(92 * s), cy + int(312 * s)),
        (cx - int(118 * s), cy + int(268 * s)),
    ]
    dr.polygon(body, fill=(219, 234, 254, int(255 * 0.92)))

    # Fenêtre code
    rx = int(round(16 * s))
    dr.rounded_rectangle(
        [
            int(248 * s),
            int(468 * s),
            int((248 + 304) * s),
            int((468 + 188) * s),
        ],
        radius=rx,
        fill=(15, 53, 80, int(255 * 0.22)),
    )
    bar_y = [492, 520, 544, 596]
    bar_w = [88, 200, 160, 120]
    bar_op = [0.55, 0.35, 0.28, 0.55]
    last_c = (123, 205, 227)
    for i, (by, bwv, op) in enumerate(zip(bar_y, bar_w, bar_op)):
        hbar = int(round(12 * s)) if i == 0 else int(round(10 * s))
        col = last_c if i == 3 else (240, 249, 255)
        a = int(255 * op)
        fill = col + (a,) if i < 3 else (*last_c, a)
        dr.rounded_rectangle(
            [
                int(268 * s),
                int(by * s),
                int((268 + bwv) * s),
                int(by * s + hbar),
            ],
            radius=int(round(6 * s)),
            fill=fill,
        )

    return img


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--size", type=int, default=1200, help="Côté carré en pixels (défaut 1200)")
    args = ap.parse_args()
    size = max(400, min(4096, args.size))

    im = rasterize(size)
    png_path = OUT_DIR / "about-section-hero.png"
    webp_path = OUT_DIR / "about-section-hero.webp"
    im.convert("RGB").save(png_path, "PNG", optimize=True)
    im.save(webp_path, "WEBP", quality=88, method=6)
    print(f"OK: {png_path.name}, {webp_path.name} ({size}x{size})")


if __name__ == "__main__":
    main()
