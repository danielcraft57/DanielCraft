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


def _font(size: int):
    try:
        return ImageFont.truetype("arial.ttf", size)
    except OSError:
        return ImageFont.load_default()


def gen_photo_png(path: Path, w: int = 1200, h: int = 520) -> None:
    img = Image.new("RGB", (w, h))
    draw = ImageDraw.Draw(img)
    _gradient_bg(draw, w, h, (42, 38, 34), (74, 69, 64))
    draw.ellipse([80, 40, 420, 380], fill=(90, 82, 74))
    draw.rectangle([w // 2 - 80, h // 2 - 60, w // 2 + 200, h // 2 + 100], fill=(26, 24, 22), outline=(201, 162, 39), width=3)
    draw.ellipse([w // 2 + 20, h // 2 - 10, w // 2 + 120, h // 2 + 70], outline=(201, 162, 39), width=4)
    draw.text((40, h - 36), "Studio Lumière Grise — démo", fill=(201, 162, 39), font=_font(18))
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, optimize=True)


def gen_fitness_png(path: Path, w: int = 1200, h: int = 520) -> None:
    img = Image.new("RGB", (w, h), (10, 10, 10))
    draw = ImageDraw.Draw(img)
    draw.ellipse([w // 2 - 350, 30, w // 2 + 350, 280], fill=(30, 50, 20))
    draw.line([(220, 220), (480, 220)], fill=(57, 255, 20), width=14)
    draw.rectangle([200, 198, 240, 242], fill=(57, 255, 20))
    draw.rectangle([460, 198, 500, 242], fill=(57, 255, 20))
    draw.text((w // 2 - 80, h - 40), "PULSE FITNESS METZ", fill=(57, 255, 20), font=_font(22))
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, optimize=True)


def gen_arch_png(path: Path, w: int = 1200, h: int = 520) -> None:
    img = Image.new("RGB", (w, h), (245, 243, 239))
    draw = ImageDraw.Draw(img)
    draw.polygon([(w // 2, 60), (w - 120, 160), (120, 160)], fill=(10, 10, 10))
    draw.rectangle([180, 160, w - 180, h - 80], fill=(255, 255, 255), outline=(10, 10, 10), width=3)
    for i, x in enumerate([220, 360, 500]):
        draw.rectangle([x, 200, x + 100, h - 120], fill=(224, 220, 212), outline=(10, 10, 10))
    draw.rectangle([620, 200, 900, 340], fill=(210, 160, 120), outline=(10, 10, 10))
    draw.text((w // 2 - 70, h - 36), "Atelier Nord-Est", fill=(10, 10, 10), font=_font(16))
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, optimize=True)


def gen_jur_png(path: Path, w: int = 1200, h: int = 520) -> None:
    img = Image.new("RGB", (w, h))
    draw = ImageDraw.Draw(img)
    _gradient_bg(draw, w, h, (15, 23, 42), (30, 41, 59))
    draw.rectangle([160, 100, 196, 460], fill=(30, 41, 59), outline=(51, 65, 85))
    draw.rectangle([w - 196, 100, w - 160, 460], fill=(30, 41, 59), outline=(51, 65, 85))
    cx, cy = w // 2, 240
    draw.line([(cx, cy - 80), (cx, cy + 140)], fill=(201, 162, 39), width=7)
    draw.line([(cx - 200, cy), (cx + 200, cy)], fill=(201, 162, 39), width=5)
    draw.ellipse([cx - 26, cy - 26, cx + 26, cy + 26], fill=(201, 162, 39))
    draw.text((w // 2 - 120, h - 36), "Rivière & Partenaires", fill=(201, 162, 39), font=_font(18))
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, optimize=True)


def gen_immo_png(path: Path, w: int = 1200, h: int = 520) -> None:
    img = Image.new("RGB", (w, h))
    draw = ImageDraw.Draw(img)
    _gradient_bg(draw, w, h, (143, 181, 168), (212, 232, 223))
    draw.polygon([(w // 2, 100), (w - 200, 260), (200, 260)], fill=(26, 60, 52))
    draw.rectangle([260, 260, w - 260, h - 100], fill=(244, 239, 230), outline=(26, 60, 52), width=3)
    draw.rectangle([w // 2 - 50, 320, w // 2 + 50, h - 100], fill=(26, 60, 52))
    for x in (w // 2 + 80, w // 2 + 180):
        draw.rectangle([x, 300, x + 60, 360], fill=(184, 149, 74))
    draw.text((w // 2 - 90, h - 36), "Patrimoine Lorraine", fill=(26, 60, 52), font=_font(18))
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, optimize=True)


def main() -> None:
    edu = ROOT / "assets" / "vitrines" / "demos" / "education" / "images"
    assoc = ROOT / "assets" / "vitrines" / "demos" / "association" / "images"
    gen_edu_mosaic(edu / "edu-gen-mosaic.png")
    gen_edu_modules(edu / "edu-gen-modules.png")
    gen_edu_parcours(edu / "edu-gen-parcours.png")
    gen_assoc_mains(assoc / "assoc-gen-mains.png")
    gen_assoc_quartier(assoc / "assoc-gen-quartier.png")
    gen_assoc_volontaires(assoc / "assoc-gen-volontaires.png")
    print("OK:", edu, assoc, "PNG pédagogiques")


if __name__ == "__main__":
    main()
