#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Installe les images produit prestations (générées via Cursor) vers assets/ + JSON.

Cherche dans :
- le dossier Cursor assets (exports GenerateImage)
- assets/images/maquettes/prestations/generated/
- arguments fichiers

Cibles :
- assets/images/prestations/cards/<slug>.jpg (+ .webp via build)
- assets/images/prestations/categories/<id>.jpg
Met à jour `image` / `categories[].image` dans src/data/prestations.json
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "src" / "data" / "prestations.json"
CARDS = ROOT / "assets" / "images" / "prestations" / "cards"
CATS = ROOT / "assets" / "images" / "prestations" / "categories"
STAGING = ROOT / "assets" / "images" / "maquettes" / "prestations" / "generated"
CURSOR_ASSETS = Path(
    r"C:/Users/loicDaniel/.cursor/projects/"
    r"c-Users-loicDaniel-Documents-DanielCraft-DanielCraftFr/assets"
)

TARGET_W, TARGET_H = 1200, 675  # 16:9


def crop_resize(img: Image.Image, tw: int, th: int) -> Image.Image:
    w, h = img.size
    target = tw / th
    if w / h > target:
        nw = int(h * target)
        left = (w - nw) // 2
        img = img.crop((left, 0, left + nw, h))
    else:
        nh = int(w / target)
        top = (h - nh) // 2
        img = img.crop((0, top, w, top + nh))
    return img.resize((tw, th), Image.Resampling.LANCZOS)


def save_jpg(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(src) as im:
        im.load()
        out = crop_resize(im.convert("RGB"), TARGET_W, TARGET_H)
        out.save(dst, "JPEG", quality=88, optimize=True)
    # WebP immédiat (le build en refait si absent)
    webp = dst.with_suffix(".webp")
    with Image.open(dst) as im:
        im.convert("RGBA").save(webp, "WEBP", quality=85, method=4)


def find_sources(patterns: list[str]) -> dict[str, Path]:
    """Map key (slug ou cat id) -> fichier source."""
    found: dict[str, Path] = {}
    search_roots: list[Path] = []
    if STAGING.is_dir():
        search_roots.append(STAGING)
    if CURSOR_ASSETS.is_dir():
        search_roots.append(CURSOR_ASSETS)

    files: list[Path] = []
    for d in search_roots:
        # Seulement le dossier (pas rglob profond) — plus rapide
        files.extend(p for p in d.glob("prestation-*.png") if p.is_file())
        files.extend(p for p in d.glob("prestation-*.jpg") if p.is_file())
        if d == STAGING:
            files.extend(p for p in d.rglob("*.png") if p.is_file())

    for p in files:
        name = p.stem.lower()
        for key in patterns:
            k = key.lower()
            aliases = {
                f"prestation-card-{k}",
                f"prestation-cat-{k}",
                f"card-{k}",
                f"cat-{k}",
                k,
            }
            if name in aliases:
                prev = found.get(key)
                if prev is None or p.stat().st_mtime > prev.stat().st_mtime:
                    found[key] = p
    return found


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", nargs="*", help="Slugs / cat ids seulement")
    args = ap.parse_args()

    data = json.loads(DATA.read_text(encoding="utf-8"))
    cats = [c["id"] for c in data.get("categories") or [] if c.get("id")]
    slugs = [
        it["slug"]
        for it in data.get("items") or []
        if isinstance(it, dict) and it.get("has_page") and it.get("slug")
    ]
    keys = cats + slugs
    if args.only:
        only = set(args.only)
        keys = [k for k in keys if k in only]

    sources = find_sources(keys)
    print(f"Sources trouvées : {len(sources)} / {len(keys)}")

    installed = 0
    by_slug = {it["slug"]: it for it in data.get("items") or [] if it.get("slug")}
    by_cat = {c["id"]: c for c in data.get("categories") or [] if c.get("id")}

    for key in keys:
        src = sources.get(key)
        if not src:
            continue
        if key in by_cat:
            dst = CATS / f"{key}.jpg"
            json_path = f"/assets/images/prestations/categories/{key}.jpg"
            if args.dry_run:
                print(f"[dry] cat {key} <- {src.name}")
            else:
                save_jpg(src, dst)
                by_cat[key]["image"] = json_path
                print(f"[OK] cat {key} <- {src.name}")
            installed += 1
        elif key in by_slug:
            dst = CARDS / f"{key}.jpg"
            json_path = f"/assets/images/prestations/cards/{key}.jpg"
            if args.dry_run:
                print(f"[dry] card {key} <- {src.name}")
            else:
                save_jpg(src, dst)
                by_slug[key]["image"] = json_path
                print(f"[OK] card {key} <- {src.name}")
            installed += 1

    if not args.dry_run and installed:
        DATA.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"JSON mis à jour ({installed} image(s))")
    else:
        print(f"Terminé : {installed} (dry={args.dry_run})")
    missing = [k for k in keys if k not in sources]
    if missing:
        print(f"Manquantes ({len(missing)}) : {', '.join(missing[:20])}"
              + ("…" if len(missing) > 20 else ""))
    return 0 if installed or args.dry_run else 1


if __name__ == "__main__":
    sys.exit(main())
