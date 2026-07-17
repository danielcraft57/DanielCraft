#!/usr/bin/env python3
"""
Cree les bannieres inline des articles IA a partir des OG IA deja generees.

Sortie : assets/images/blog/illustrations/<slug>-banner.webp (+ .jpg)
Format banniere article : 1200x480 (ratio 2.5:1), adapte au corps d'article.
"""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OG = ROOT / "assets" / "images" / "og"
OUT = ROOT / "assets" / "images" / "blog" / "illustrations"
MANIFEST = ROOT / "scripts" / "_ia_articles_generated.json"
W, H = 1200, 480


def crop_resize(img: Image.Image, tw: int, th: int) -> Image.Image:
    w, h = img.size
    target = tw / th
    if w / h > target:
        nw = int(h * target)
        left = (w - nw) // 2
        img = img.crop((left, 0, left + nw, h))
    else:
        nh = int(w / target)
        # privilegier le haut de l'illustration (scene) plutot que le bandeau texte
        top = max(0, (h - nh) // 4)
        img = img.crop((0, top, w, top + nh))
    return img.resize((tw, th), Image.Resampling.LANCZOS)


def main() -> None:
    items = json.loads(MANIFEST.read_text(encoding="utf-8"))
    OUT.mkdir(parents=True, exist_ok=True)
    ok = miss = 0
    for item in items:
        slug = item["slug"]
        src = OG / f"{slug}-1200x630.jpg"
        if not src.exists():
            print(f"[MISS] {src.name}")
            miss += 1
            continue
        img = crop_resize(Image.open(src).convert("RGB"), W, H)
        jpg = OUT / f"{slug}-banner.jpg"
        webp = OUT / f"{slug}-banner.webp"
        img.save(jpg, "JPEG", quality=88, optimize=True)
        img.save(webp, "WEBP", quality=82, method=6)
        ok += 1
        print(f"[OK] {webp.relative_to(ROOT)}")
    print(f"\nbanners={ok} missing={miss}")


if __name__ == "__main__":
    main()
