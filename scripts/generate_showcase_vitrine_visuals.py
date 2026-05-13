#!/usr/bin/env python3
"""
Génère des visuels PNG abstraits (style affiche / mosaïque) pour les vitrines portfolio.
Usage (à la racine du dépôt) : python scripts/generate_showcase_vitrine_visuals.py

Dépendance : Pillow (déjà utilisée ailleurs dans le repo).
"""
from __future__ import annotations

import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]


def _gradient_bg(draw: ImageDraw.ImageDraw, w: int, h: int, top: tuple, bottom: tuple) -> None:
    for y in range(h):
        t = y / max(h - 1, 1)
        r = int(top[0] + (bottom[0] - top[0]) * t)
        g = int(top[1] + (bottom[1] - top[1]) * t)
        b = int(top[2] + (bottom[2] - top[2]) * t)
        draw.line([(0, y), (w, y)], fill=(r, g, b))


def gen_edu_mosaic(path: Path, w: int = 800, h: int = 450, seed: int = 42) -> None:
    rng = random.Random(seed)
    img = Image.new("RGB", (w, h))
    draw = ImageDraw.Draw(img)
    _gradient_bg(draw, w, h, (18, 42, 88), (30, 72, 130))
    for _ in range(140):
        x, y = rng.randint(0, w), rng.randint(0, h)
        s = rng.randint(4, 28)
        c = (rng.randint(180, 255), rng.randint(160, 230), rng.randint(60, 120), 40)
        draw.ellipse([x - s, y - s, x + s, y + s], fill=c[:3])
    for i in range(12):
        x0 = (i * 73) % (w + 80) - 40
        draw.rectangle([x0, i * 31, x0 + 24, h], outline=(255, 214, 120), width=2)
    draw.rectangle([w // 2 - 120, h // 2 - 40, w // 2 + 120, h // 2 + 40], outline=(255, 214, 120), width=3)
    try:
        font = ImageFont.truetype("arial.ttf", 22)
    except OSError:
        font = ImageFont.load_default()
    draw.text((24, h - 52), "Campus — visuel démo", fill=(255, 240, 200), font=font)
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, optimize=True)


def gen_edu_modules(path: Path, w: int = 800, h: int = 450, seed: int = 43) -> None:
    rng = random.Random(seed)
    img = Image.new("RGB", (w, h), (245, 247, 252))
    draw = ImageDraw.Draw(img)
    cols = 5
    cw = w // cols
    palette = [(30, 58, 95), (41, 98, 168), (255, 193, 7), (52, 152, 120), (200, 210, 225)]
    for c in range(cols):
        ph = rng.randint(int(h * 0.25), int(h * 0.85))
        y0 = h - ph
        draw.rectangle([c * cw + 4, y0, (c + 1) * cw - 4, h - 8], fill=palette[c % len(palette)])
    for _ in range(25):
        draw.line(
            [(rng.randint(0, w), rng.randint(0, h)), (rng.randint(0, w), rng.randint(0, h))],
            fill=(220, 225, 235),
            width=1,
        )
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except OSError:
        font = ImageFont.load_default()
    draw.text((20, 16), "Modules — maquette", fill=(25, 45, 80), font=font)
    img.save(path, optimize=True)


def gen_edu_parcours(path: Path, w: int = 800, h: int = 450) -> None:
    img = Image.new("RGB", (w, h), (15, 28, 48))
    draw = ImageDraw.Draw(img)
    pts = []
    for i in range(8):
        x = 60 + i * (w - 120) // 7
        y = int(h * 0.35 + 90 * math.sin(i * 0.9))
        pts.append((x, y))
    draw.line(pts, fill=(255, 209, 102), width=6, joint="curve")
    for (x, y) in pts:
        draw.ellipse([x - 10, y - 10, x + 10, y + 10], fill=(72, 199, 142))
    draw.ellipse([pts[0][0] - 14, pts[0][1] - 14, pts[0][0] + 14, pts[0][1] + 14], outline=(255, 255, 255), width=3)
    try:
        font = ImageFont.truetype("arial.ttf", 18)
    except OSError:
        font = ImageFont.load_default()
    draw.text((24, h - 44), "Parcours apprenant (fictif)", fill=(200, 220, 255), font=font)
    img.save(path, optimize=True)


def gen_assoc_mains(path: Path, w: int = 800, h: int = 450) -> None:
    img = Image.new("RGB", (w, h), (12, 62, 40))
    draw = ImageDraw.Draw(img)
    _gradient_bg(draw, w, h, (18, 90, 55), (8, 48, 32))
    cx, cy = w // 2, h // 2 + 20
    for i, scale in enumerate([1.0, 0.72, 0.48]):
        r = int(80 * scale)
        ox = int((i - 1) * 55)
        draw.ellipse(
            [cx - r + ox, cy - r, cx + r + ox, cy + r],
            outline=(255, 230, 180),
            width=4,
        )
    draw.polygon(
        [(cx, cy - 95), (cx + 28, cy - 40), (cx - 28, cy - 40)],
        fill=(255, 107, 107),
    )
    try:
        font = ImageFont.truetype("arial.ttf", 19)
    except OSError:
        font = ImageFont.load_default()
    draw.text((20, h - 46), "Solidarité — visuel démo", fill=(230, 255, 240), font=font)
    img.save(path, optimize=True)


def gen_assoc_quartier(path: Path, w: int = 800, h: int = 450) -> None:
    img = Image.new("RGB", (w, h), (230, 245, 238))
    draw = ImageDraw.Draw(img)
    base_y = h - 80
    colors = [(46, 125, 50), (56, 142, 60), (76, 175, 80), (129, 199, 132)]
    for i in range(9):
        bw = 50 + (i % 3) * 18
        x = 30 + i * 78
        bh = 60 + (i * 17) % 90
        draw.rectangle([x, base_y - bh, x + bw, base_y], fill=colors[i % len(colors)])
        draw.polygon(
            [(x, base_y - bh), (x + bw // 2, base_y - bh - 35), (x + bw, base_y - bh)],
            fill=(139, 195, 74),
        )
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except OSError:
        font = ImageFont.load_default()
    draw.text((20, 18), "Quartier imaginaire", fill=(27, 94, 32), font=font)
    img.save(path, optimize=True)


def gen_assoc_volontaires(path: Path, w: int = 800, h: int = 450, seed: int = 7) -> None:
    rng = random.Random(seed)
    img = Image.new("RGB", (w, h), (250, 252, 248))
    draw = ImageDraw.Draw(img)
    for i in range(18):
        x = 40 + (i % 6) * 120 + rng.randint(-8, 8)
        y = 60 + (i // 6) * 110 + rng.randint(-6, 6)
        draw.ellipse([x - 22, y - 22, x + 22, y + 22], fill=(rng.randint(80, 160), rng.randint(120, 200), rng.randint(90, 180)))
        draw.line([x, y + 22, x, y + 70], fill=(60, 60, 70), width=4)
    try:
        font = ImageFont.truetype("arial.ttf", 18)
    except OSError:
        font = ImageFont.load_default()
    draw.text((w - 240, h - 40), "Bénévoles — fiction graphique", fill=(50, 70, 55), font=font)
    img.save(path, optimize=True)


def main() -> None:
    edu = ROOT / "showcase" / "education" / "images"
    assoc = ROOT / "showcase" / "association" / "images"
    gen_edu_mosaic(edu / "edu-gen-mosaic.png")
    gen_edu_modules(edu / "edu-gen-modules.png")
    gen_edu_parcours(edu / "edu-gen-parcours.png")
    gen_assoc_mains(assoc / "assoc-gen-mains.png")
    gen_assoc_quartier(assoc / "assoc-gen-quartier.png")
    gen_assoc_volontaires(assoc / "assoc-gen-volontaires.png")
    print("OK:", edu, assoc)


if __name__ == "__main__":
    main()
