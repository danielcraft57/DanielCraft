#!/usr/bin/env python3
"""Convertit les OG JPG de la serie IA en WebP (1200x630)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("pip install pillow")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
OG = ROOT / "assets" / "images" / "og"
PROMPT_DOC = ROOT / "docs" / "prompt_og_images_articles_ia_pratique.md"


def listed_stems() -> set[str]:
    if not PROMPT_DOC.exists():
        return set()
    text = PROMPT_DOC.read_text(encoding="utf-8")
    return set(re.findall(r"^##\s+([\w.-]+-1200x630)\.jpg", text, flags=re.M))


def center_crop(img: Image.Image, ratio: float) -> Image.Image:
    w, h = img.size
    cur = w / h if h else 1.0
    if cur > ratio:
        nw = int(h * ratio)
        left = (w - nw) // 2
        return img.crop((left, 0, left + nw, h))
    nh = int(w / ratio)
    top = (h - nh) // 2
    return img.crop((0, top, w, top + nh))


def main() -> None:
    OG.mkdir(parents=True, exist_ok=True)
    stems = listed_stems()
    files = sorted(OG.glob("ia-*-1200x630.jpg"))
    if stems:
        extra = [OG / f"{s}.jpg" for s in stems if (OG / f"{s}.jpg").exists()]
        files = sorted(set(files) | set(extra))
    if not files:
        print(f"[WARN] Aucun JPG ia-*-1200x630.jpg dans {OG}")
        print("Genere d'abord les images via docs/prompt_og_images_articles_ia_pratique.md")
        return
    for jpg in files:
        img = Image.open(jpg).convert("RGB")
        img = center_crop(img, 1200 / 630)
        img = img.resize((1200, 630), Image.Resampling.LANCZOS)
        webp = jpg.with_suffix(".webp")
        img.save(webp, "WEBP", quality=82, method=6)
        # Reecrit aussi un JPG optimise
        img.save(jpg, "JPEG", quality=85, optimize=True)
        print(f"[OK] {webp.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
