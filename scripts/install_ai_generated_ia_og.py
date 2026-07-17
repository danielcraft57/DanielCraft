#!/usr/bin/env python3
"""Installe les OG IA generees (Cursor assets) vers assets/images/og/ en 1200x630 JPG+WebP."""
from __future__ import annotations

import json
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = Path(r"C:/Users/loicDaniel/.cursor/projects/c-Users-loicDaniel-Documents-DanielCraft-DanielCraftFr/assets")
DST = ROOT / "assets" / "images" / "og"
MANIFEST = ROOT / "scripts" / "_ia_articles_generated.json"
REMAINING = ROOT / "scripts" / "_ia_og_remaining.json"


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


def main() -> None:
    items = json.loads(MANIFEST.read_text(encoding="utf-8"))
    wanted = {f"{i['slug']}-1200x630.jpg": i for i in items}
    DST.mkdir(parents=True, exist_ok=True)
    installed = 0
    for name, item in wanted.items():
        src = SRC / name
        if not src.exists():
            continue
        img = crop_resize(Image.open(src).convert("RGB"))
        out = DST / name
        img.save(out, "JPEG", quality=88, optimize=True)
        img.save(out.with_suffix(".webp"), "WEBP", quality=82, method=6)
        installed += 1
        print(f"[OK] {name}")

    have_ai = {p.name for p in SRC.glob("ia-*-1200x630.jpg")}
    need = [i for i in items if f"{i['slug']}-1200x630.jpg" not in have_ai]
    REMAINING.write_text(json.dumps(need, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\ninstalled_this_run={installed} remaining={len(need)} total={len(items)}")


if __name__ == "__main__":
    main()
