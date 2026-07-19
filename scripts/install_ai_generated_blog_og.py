#!/usr/bin/env python3
"""Installe les OG generees (Cursor assets) vers assets/images/og/ pour tout le blog."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = Path(
    r"C:/Users/loicDaniel/.cursor/projects/c-Users-loicDaniel-Documents-DanielCraft-DanielCraftFr/assets"
)
DST = ROOT / "assets" / "images" / "og"
MANIFEST = ROOT / "scripts" / "_blog_og_manifest.json"
LEGACY_MANIFEST = ROOT / "scripts" / "_blog_og_legacy_manifest.json"
SIMPLE_MANIFEST = ROOT / "scripts" / "_blog_og_simple_manifest.json"
REMAINING = ROOT / "scripts" / "_blog_og_remaining.json"
EXTRA_OG = ("blog-1200x630.jpg",)


def crop_resize(img: Image.Image) -> Image.Image:
    w, h = img.size
    t = 1200 / 630
    if w / h > t:
        nw = int(h * t)
        left = (w - nw) // 2
        img = img.crop((left, 0, left + nw, h))
    else:
        nh = int(w / t)
        top = (h - nh) // 2
        img = img.crop((0, top, w, top + nh))
    return img.resize((1200, 630), Image.Resampling.LANCZOS)


def og_candidates(item: dict) -> list[str]:
    slug = item["slug"]
    og = str(item.get("og") or f"{slug}-1200x630.jpg").strip()
    names = [og, f"{slug}-1200x630.jpg"]
    seen: set[str] = set()
    out: list[str] = []
    for n in names:
        if n and n not in seen:
            seen.add(n)
            out.append(n)
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--legacy", action="store_true", help="Utilise _blog_og_legacy_manifest.json")
    parser.add_argument("--simple", action="store_true", help="Utilise _blog_og_simple_manifest.json (ton debutant)")
    parser.add_argument("only", nargs="*", help="Slugs optionnels a installer")
    args = parser.parse_args()

    if args.simple:
        manifest_path = SIMPLE_MANIFEST
    elif args.legacy:
        manifest_path = LEGACY_MANIFEST
    else:
        manifest_path = MANIFEST
    if not manifest_path.exists():
        print(f"Manifest manquant: {manifest_path}")
        sys.exit(1)

    items = json.loads(manifest_path.read_text(encoding="utf-8"))
    only = {a.strip() for a in args.only if a.strip()}
    DST.mkdir(parents=True, exist_ok=True)
    installed = 0
    for item in items:
        slug = item["slug"]
        if only and slug not in only:
            continue
        src = None
        src_name = None
        for name in og_candidates(item):
            candidate = SRC / name
            if candidate.exists():
                src = candidate
                src_name = name
                break
        if src is None:
            continue
        dest_name = str(item.get("og") or f"{slug}-1200x630.jpg").strip()
        img = crop_resize(Image.open(src).convert("RGB"))
        out = DST / dest_name
        img.save(out, "JPEG", quality=88, optimize=True)
        img.save(out.with_suffix(".webp"), "WEBP", quality=82, method=6)
        slug_name = f"{slug}-1200x630.jpg"
        if dest_name != slug_name:
            alt = DST / slug_name
            img.save(alt, "JPEG", quality=88, optimize=True)
            img.save(alt.with_suffix(".webp"), "WEBP", quality=82, method=6)
        installed += 1
        print(f"[OK] {src_name} -> {dest_name}")

    if not only and not args.legacy:
        for name in EXTRA_OG:
            src = SRC / name
            if not src.exists():
                continue
            img = crop_resize(Image.open(src).convert("RGB"))
            out = DST / name
            img.save(out, "JPEG", quality=88, optimize=True)
            img.save(out.with_suffix(".webp"), "WEBP", quality=82, method=6)
            installed += 1
            print(f"[OK] {name}")

    need = [
        i for i in items if not any((SRC / n).exists() for n in og_candidates(i))
    ]
    REMAINING.write_text(json.dumps(need, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\ninstalled={installed} remaining={len(need)} total={len(items)}")


if __name__ == "__main__":
    main()
