#!/usr/bin/env python3
"""Installe les heroes Movento regeneres pour les flagships redesignes."""
from __future__ import annotations

import io
import os
import time
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SRC = Path(
    r"C:\Users\loicDaniel\.cursor\projects\c-Users-loicDaniel-Documents-DanielCraft-DanielCraftFr\assets"
)
DEMOS = ROOT / "assets" / "vitrines" / "demos"

JOBS = [
    ("odontologie", "odontologie-hero-mv"),
    ("restauration", "restauration-hero-mv"),
    ("artisan", "artisan-hero-mv"),
    ("automobile", "automobile-hero-mv"),
    ("beaute", "beaute-hero-mv"),
    ("commerce", "commerce-hero-mv"),
    ("immobilier", "immobilier-hero-mv"),
    ("juridique", "juridique-hero-mv"),
    ("industrie", "industrie-hero-mv"),
    ("etablissement", "etablissement-hero-mv"),
    ("fitness", "fitness-hero-mv"),
    ("gites", "gites-hero-mv"),
    ("technologie", "technologie-hero-mv"),
    ("banque", "banque-hero-mv"),
    ("services", "services-hero-mv"),
    ("education", "education-hero-mv"),
]


def _save(img: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    buf = io.BytesIO()
    img.save(buf, format="PNG", optimize=True)
    data = buf.getvalue()
    tmp = path.with_name(f".{path.stem}.tmp.png")
    for attempt in range(8):
        try:
            tmp.write_bytes(data)
            os.replace(tmp, path)
            break
        except OSError:
            time.sleep(0.2 * (attempt + 1))
    img.save(path.with_suffix(".webp"), "WEBP", quality=85, method=6)


def main() -> int:
    ok = 0
    for slug, stem in JOBS:
        src = SRC / f"{stem}.png"
        if not src.is_file():
            alt = ROOT / "assets" / f"{stem}.png"
            src = alt if alt.is_file() else src
        if not src.is_file():
            print(f"[SKIP] {stem}")
            continue
        dest = DEMOS / slug / "images" / "hero.png"
        with Image.open(src) as im:
            im = im.convert("RGB").resize((1200, 520), Image.Resampling.LANCZOS)
            _save(im, dest)
        print(f"[OK] {dest.relative_to(ROOT)}")
        ok += 1
    print(f"Done {ok}/{len(JOBS)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
