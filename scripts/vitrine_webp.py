#!/usr/bin/env python3
"""Conversion PNG → WebP pour images vitrines demos."""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
DEMOS = ROOT / "assets" / "vitrines" / "demos"
SKIP = {"icon.svg", "apple-touch-icon.png"}


def png_to_webp(png: Path, *, quality: int = 85, delete_png: bool = False) -> Path:
    webp = png.with_suffix(".webp")
    with Image.open(png) as img:
        img.save(webp, "WEBP", quality=quality, method=6)
    if delete_png:
        png.unlink(missing_ok=True)
    return webp


def convert_slug(slug: str, *, quality: int = 85) -> int:
    img_dir = DEMOS / slug / "images"
    if not img_dir.is_dir():
        return 0
    n = 0
    for png in sorted(img_dir.glob("*.png")):
        if png.name in SKIP:
            continue
        webp = png_to_webp(png, quality=quality)
        print(f"[OK] {webp.relative_to(ROOT)}")
        n += 1
    return n


def convert_all(*, quality: int = 85) -> int:
    total = 0
    for d in sorted(DEMOS.iterdir()):
        if d.is_dir() and (d / "images").is_dir():
            total += convert_slug(d.name, quality=quality)
    return total


def main() -> None:
    p = argparse.ArgumentParser(description="Convertit les PNG vitrines en WebP")
    p.add_argument("slug", nargs="?", help="Slug vitrine (tous si omis)")
    p.add_argument("-q", "--quality", type=int, default=85)
    args = p.parse_args()
    if args.slug:
        n = convert_slug(args.slug, quality=args.quality)
    else:
        n = convert_all(quality=args.quality)
    print(f"[OK] {n} WebP générées")


if __name__ == "__main__":
    main()
