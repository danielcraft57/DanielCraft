#!/usr/bin/env python3
"""Génère hero + 3 cartes PNG uniques par vitrine (évite vignettes dupliquées)."""
from __future__ import annotations

import hashlib
import io
import json
import math
import os
import random
import time
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = ROOT / "src" / "data" / "vitrines.json"
DEMOS = ROOT / "assets" / "vitrines" / "demos"

PALETTES = {
    "saas": [(99, 102, 241), (15, 23, 42)],
    "tech": [(100, 181, 246), (13, 27, 42)],
    "hcr": [(183, 28, 28), (62, 39, 35)],
    "beaute": [(236, 72, 153), (253, 242, 248)],
    "sante": [(14, 165, 233), (224, 242, 254)],
    "industrie": [(255, 179, 0), (10, 22, 40)],
    "ess": [(34, 197, 94), (20, 83, 45)],
    "retail": [(27, 94, 32), (232, 245, 233)],
    "conseil": [(13, 71, 161), (227, 242, 253)],
    "formation": [(37, 99, 235), (239, 246, 255)],
    "services": [(15, 118, 110), (204, 251, 241)],
    "hotel": [(78, 52, 46), (255, 248, 225)],
    "mobilite": [(198, 40, 40), (26, 26, 26)],
    "immobilier": [(26, 60, 52), (212, 232, 223)],
    "juridique": [(201, 162, 39), (15, 23, 42)],
    "architecture": [(17, 17, 17), (245, 245, 245)],
    "sport": [(101, 163, 13), (20, 83, 45)],
    "creatif": [(55, 71, 79), (236, 239, 241)],
}


def _font(size: int):
    for name in ("arial.ttf", "segoeui.ttf", "calibri.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def _seed(slug: str, suffix: str) -> int:
    h = hashlib.md5(f"{slug}:{suffix}".encode()).hexdigest()
    return int(h[:8], 16)


def _gradient(w: int, h: int, c1: tuple, c2: tuple) -> Image.Image:
    img = Image.new("RGB", (w, h))
    draw = ImageDraw.Draw(img)
    for y in range(h):
        t = y / max(h - 1, 1)
        r = int(c1[0] + (c2[0] - c1[0]) * t)
        g = int(c1[1] + (c2[1] - c1[1]) * t)
        b = int(c1[2] + (c2[2] - c1[2]) * t)
        draw.line([(0, y), (w, y)], fill=(r, g, b))
    return img


def _draw_mock_ui(draw: ImageDraw.ImageDraw, w: int, h: int, rng: random.Random, accent: tuple) -> None:
    draw.rounded_rectangle([40, 40, w - 40, h - 40], radius=16, outline=accent, width=2)
    for i in range(4):
        bw = rng.randint(60, 140)
        bh = rng.randint(80, min(200, h // 3))
        x = 60 + i * ((w - 120) // 4)
        y = h - 60 - bh
        draw.rounded_rectangle([x, y, x + bw, y + bh], radius=8, fill=(*accent, 40) if len(accent) == 3 else accent)


def _save_png(img: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    data = buf.getvalue()
    tmp = path.with_name(f".{path.stem}.tmp.png")
    last_err: OSError | None = None
    for attempt in range(6):
        try:
            tmp.write_bytes(data)
            os.replace(tmp, path)
            return
        except OSError as err:
            last_err = err
            time.sleep(0.15 * (attempt + 1))
        finally:
            if tmp.exists():
                try:
                    tmp.unlink()
                except OSError:
                    pass
    if last_err:
        raise last_err


def gen_image(path: Path, slug: str, title: str, tagline: str, category: str, variant: str, w: int, h: int) -> None:
    pal = PALETTES.get(category, [(71, 85, 105), (241, 245, 249)])
    if isinstance(pal[0], list):
        pal = pal[0]
    rng = random.Random(_seed(slug, variant))
    c1, c2 = pal[0], pal[1]
    if variant != "hero":
        c1 = tuple(max(0, min(255, c + rng.randint(-20, 20))) for c in c1)
    img = _gradient(w, h, c1, c2)
    draw = ImageDraw.Draw(img)
    accent = pal[0]
    _draw_mock_ui(draw, w, h, rng, accent)
    f_title = _font(28 if w >= 1000 else 22)
    f_sub = _font(16)
    label = title[:42]
    draw.text((48, 48), label, fill=(255, 255, 255) if sum(c1) < 400 else (20, 20, 20), font=f_title)
    draw.text((48, 90), tagline[:60], fill=(230, 230, 230) if sum(c1) < 400 else (60, 60, 60), font=f_sub)
    draw.text((48, h - 36), f"DanielCraft · {slug} · {variant}", fill=(180, 180, 180), font=_font(12))
    _save_png(img, path)


def main() -> None:
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    for it in data["items"]:
        slug = it["slug"]
        title = it.get("title") or slug
        tagline = it.get("tagline") or ""
        cat = it.get("category") or "tech"
        img_dir = DEMOS / slug / "images"
        gen_image(img_dir / "hero.png", slug, title, tagline, cat, "hero", 1200, 520)
        for i in range(1, 4):
            gen_image(img_dir / f"card-{i}.png", slug, title, f"Offre {i}", cat, f"card{i}", 800, 520)
        print(f"OK images {slug}")


if __name__ == "__main__":
    main()
