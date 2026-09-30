#!/usr/bin/env python3
"""Installe les PNG gen-IA des 3 secteurs Movento (btp, communication, transport)."""
from __future__ import annotations

import io
import os
import sys
import time
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = Path(
    r"C:\Users\loicDaniel\.cursor\projects\c-Users-loicDaniel-Documents-DanielCraft-DanielCraftFr\assets"
)
DEMOS = ROOT / "assets" / "vitrines" / "demos"

# (slug, filename, source stem, w, h)
JOBS = [
    ("btp", "hero.png", "btp-hero", 1200, 520),
    ("btp", "card-1.png", "btp-card-1", 800, 520),
    ("btp", "card-2.png", "btp-card-2", 800, 520),
    ("btp", "card-3.png", "btp-card-3", 800, 520),
    ("btp", "gallery-1.png", "btp-gallery-1", 800, 520),
    ("btp", "gallery-2.png", "btp-gallery-2", 800, 520),
    ("btp", "scene-1.png", "btp-scene-1", 800, 520),
    ("btp", "scene-2.png", "btp-scene-2", 800, 520),
    ("btp", "scene-3.png", "btp-scene-3", 800, 520),
    ("communication", "hero.png", "communication-hero", 1200, 520),
    ("communication", "card-1.png", "communication-card-1", 800, 520),
    ("communication", "card-2.png", "communication-card-2", 800, 520),
    ("communication", "card-3.png", "communication-card-3", 800, 520),
    ("communication", "scene-1.png", "communication-scene-1", 800, 520),
    ("communication", "scene-2.png", "communication-scene-2", 800, 520),
    ("communication", "scene-3.png", "communication-scene-3", 800, 520),
    ("transport", "hero.png", "transport-hero", 1200, 520),
    ("transport", "card-1.png", "transport-card-1", 800, 520),
    ("transport", "card-2.png", "transport-card-2", 800, 520),
    ("transport", "card-3.png", "transport-card-3", 800, 520),
    ("transport", "scene-1.png", "transport-scene-1", 800, 520),
    ("transport", "scene-2.png", "transport-scene-2", 800, 520),
    ("transport", "scene-3.png", "transport-scene-3", 800, 520),
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


def _find_src(stem: str) -> Path | None:
    for candidate in (SRC_DIR / f"{stem}.png", ROOT / "assets" / f"{stem}.png"):
        if candidate.is_file():
            return candidate
    return None


def _icon_svg(slug: str, color: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="{slug}">
  <rect width="64" height="64" rx="14" fill="{color}"/>
  <circle cx="32" cy="32" r="14" fill="#fff" opacity=".9"/>
</svg>
"""


def main() -> int:
    ok = 0
    for slug, filename, stem, w, h in JOBS:
        src = _find_src(stem)
        if not src:
            print(f"[SKIP] {stem}.png introuvable", file=sys.stderr)
            continue
        dest = DEMOS / slug / "images" / filename
        with Image.open(src) as im:
            im = im.convert("RGB").resize((w, h), Image.Resampling.LANCZOS)
            _save(im, dest)
        print(f"[OK] {dest.relative_to(ROOT)}")
        ok += 1

    # icons + copy gallery placeholders for com/transport missing gallery
    icons = {
        "btp": "#c45c26",
        "communication": "#0f766e",
        "transport": "#38bdf8",
    }
    for slug, color in icons.items():
        img_dir = DEMOS / slug / "images"
        img_dir.mkdir(parents=True, exist_ok=True)
        (img_dir / "icon.svg").write_text(_icon_svg(slug, color), encoding="utf-8")
        # apple-touch: reuse hero if present
        hero = img_dir / "hero.png"
        if hero.is_file():
            with Image.open(hero) as im:
                im = im.convert("RGB").resize((180, 180), Image.Resampling.LANCZOS)
                im.save(img_dir / "apple-touch-icon.png", "PNG", optimize=True)
        # gallery fallbacks for com/transport: copy card-1/2
        for i, src_name in enumerate(("card-1.png", "card-2.png"), 1):
            g = img_dir / f"gallery-{i}.png"
            s = img_dir / src_name
            if not g.is_file() and s.is_file():
                with Image.open(s) as im:
                    im = im.convert("RGB").resize((800, 520), Image.Resampling.LANCZOS)
                    _save(im, g)
                print(f"[OK] {g.relative_to(ROOT)} (copie)")

    print(f"Installees: {ok}/{len(JOBS)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
