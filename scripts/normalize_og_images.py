#!/usr/bin/env python3
"""
Normalise les images Open Graph pour Meta (Facebook, Messenger, Instagram).

Exigences Meta :
- Ratio ~1,91:1 (recommandé 1200×630 px)
- JPEG ou PNG, < 8 Mo
- Dimensions réelles = og:image:width / og:image:height

Les visuels IA arrivent souvent en 1536×1024 PNG renommés .jpg : ce script recadre,
redimensionne et ré-encode en JPEG 1200×630.
"""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
OG_DIR = ROOT / "assets" / "images" / "og"
TARGET_W, TARGET_H = 1200, 630
TARGET_RATIO = TARGET_W / TARGET_H
JPEG_QUALITY = 88
MAX_BYTES = 7_500_000  # marge sous la limite Meta 8 Mo


def _crop_to_ratio(im: Image.Image, ratio: float) -> Image.Image:
    w, h = im.size
    current = w / h
    if abs(current - ratio) < 0.01:
        return im
    if current > ratio:
        # trop large → rogner les côtés
        new_w = int(h * ratio)
        left = (w - new_w) // 2
        return im.crop((left, 0, left + new_w, h))
    # trop haut → rogner haut/bas
    new_h = int(w / ratio)
    top = (h - new_h) // 2
    return im.crop((0, top, w, top + new_h))


def _needs_normalize(path: Path) -> bool:
    try:
        with Image.open(path) as im:
            if im.size != (TARGET_W, TARGET_H):
                return True
            if (im.format or "").upper() not in ("JPEG", "JPG"):
                return True
            if path.stat().st_size > MAX_BYTES:
                return True
    except OSError:
        return True
    return False


def normalize_file(path: Path, *, force: bool = False) -> bool:
    if not force and not _needs_normalize(path):
        return False

    with Image.open(path) as im:
        rgb = ImageOps.exif_transpose(im).convert("RGB")
        cropped = _crop_to_ratio(rgb, TARGET_RATIO)
        out = cropped.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)

    tmp = path.with_suffix(path.suffix + ".tmp")
    quality = JPEG_QUALITY
    out.save(tmp, format="JPEG", quality=quality, optimize=True)
    while tmp.stat().st_size > MAX_BYTES and quality > 60:
        quality -= 5
        out.save(tmp, format="JPEG", quality=quality, optimize=True)

    tmp.replace(path)
    return True


def main() -> int:
    force = "--force" in sys.argv
    if not OG_DIR.is_dir():
        print(f"[WARN] Dossier absent : {OG_DIR}")
        return 1

    changed = 0
    scanned = 0
    for path in sorted(OG_DIR.rglob("*.jpg")):
        scanned += 1
        try:
            if normalize_file(path, force=force):
                changed += 1
                print(f"  [OK] {path.relative_to(ROOT)}")
        except Exception as exc:
            print(f"  [ERR] {path.relative_to(ROOT)} : {exc}", file=sys.stderr)

    print(f"[OK] {changed}/{scanned} image(s) OG normalisees -> {TARGET_W}x{TARGET_H} JPEG")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
