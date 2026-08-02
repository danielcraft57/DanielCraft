#!/usr/bin/env python3
"""Cree les bannieres inline (1200x480) pour tous les articles a partir des OG."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OG = ROOT / "assets" / "images" / "og"
OUT = ROOT / "assets" / "images" / "blog" / "illustrations"
MANIFEST = ROOT / "scripts" / "_blog_og_manifest.json"
LEGACY_MANIFEST = ROOT / "scripts" / "_blog_og_legacy_manifest.json"
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
        top = max(0, (h - nh) // 4)
        img = img.crop((0, top, w, top + nh))
    return img.resize((tw, th), Image.Resampling.LANCZOS)


def resolve_og(item: dict) -> Path | None:
    slug = item["slug"]
    og = str(item.get("og") or f"{slug}-1200x630.jpg").strip()
    for name in (og, f"{slug}-1200x630.jpg"):
        path = OG / name
        if path.is_file():
            return path
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--legacy", action="store_true")
    parser.add_argument("only", nargs="*")
    args = parser.parse_args()

    manifest_path = LEGACY_MANIFEST if args.legacy else MANIFEST
    if not manifest_path.exists():
        print("Lance d'abord: python scripts/generate_all_blog_og_prompts.py")
        sys.exit(1)

    items = json.loads(manifest_path.read_text(encoding="utf-8"))
    only = {a.strip() for a in args.only if a.strip()}
    OUT.mkdir(parents=True, exist_ok=True)
    ok = miss = 0
    for item in items:
        slug = item["slug"]
        if only and slug not in only:
            continue
        src = resolve_og(item)
        if src is None:
            miss += 1
            continue
        img = crop_resize(Image.open(src).convert("RGB"), W, H)
        jpg = OUT / f"{slug}-banner.jpg"
        webp = OUT / f"{slug}-banner.webp"
        img.save(jpg, "JPEG", quality=88, optimize=True)
        img.save(webp, "WEBP", quality=82, method=6)
        ok += 1
        print(f"[OK] {webp.relative_to(ROOT)}")
    print(f"\nbanners={ok} missing_og={miss}")


if __name__ == "__main__":
    main()
