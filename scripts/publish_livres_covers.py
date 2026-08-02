#!/usr/bin/env python3
"""Associe chaque livre a sa couverture et publie des vignettes web legeres."""
from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIVRES_JSON = ROOT / "src" / "data" / "livres.json"
BOOKS_ROOT = ROOT / "livres-formation"
OUT_DIR = ROOT / "assets" / "images" / "livres" / "covers"
WEB_PREFIX = "/assets/images/livres/covers"

MAX_W = 420
JPEG_Q = 78


def find_cover_file(source_dir: str) -> Path | None:
    if not source_dir:
        return None
    img_dir = BOOKS_ROOT / source_dir / "images"
    if not img_dir.is_dir():
        return None
    candidates = []
    for p in img_dir.iterdir():
        if not p.is_file() or p.suffix.lower() not in {".png", ".jpg", ".jpeg", ".webp"}:
            continue
        name = p.name.lower()
        if "couvert" in name or name.endswith("-cover.png") or name.endswith("_cover.png") or "-cover." in name:
            if name.startswith("_src"):
                continue
            candidates.append(p)
    if not candidates:
        return None
    # Prefer *couverture* then *cover*
    candidates.sort(
        key=lambda p: (
            0 if "couverture" in p.name.lower() else 1,
            len(p.name),
        )
    )
    return candidates[0]


def export_cover(src: Path, dest: Path) -> bool:
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        from PIL import Image

        im = Image.open(src)
        if im.mode in ("RGBA", "P"):
            bg = Image.new("RGB", im.size, (255, 255, 255))
            rgba = im.convert("RGBA")
            bg.paste(rgba, mask=rgba.split()[-1])
            im = bg
        else:
            im = im.convert("RGB")
        w, h = im.size
        if w > MAX_W:
            nh = int(h * (MAX_W / w))
            im = im.resize((MAX_W, max(1, nh)), Image.Resampling.LANCZOS)
        im.save(dest, "JPEG", quality=JPEG_Q, optimize=True)
        return True
    except Exception:
        # Fallback: copy as-is renamed jpg only if already jpeg-ish
        try:
            shutil.copy2(src, dest.with_suffix(src.suffix))
            return False
        except OSError:
            return False


def main() -> None:
    data = json.loads(LIVRES_JSON.read_text(encoding="utf-8"))
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ok = 0
    miss = 0
    for it in data.get("items", []):
        if it.get("kind") == "pack":
            # Pack cover = first book cover (filled later after livres have covers)
            continue
        slug = (it.get("slug") or "").strip()
        source = (it.get("source_dir") or "").strip()
        src = find_cover_file(source)
        if not src or not slug:
            it.pop("cover", None)
            miss += 1
            print(f"[MISS] {slug or '?'} ({source})")
            continue
        dest = OUT_DIR / f"{slug}.jpg"
        export_cover(src, dest)
        it["cover"] = f"{WEB_PREFIX}/{slug}.jpg"
        ok += 1

    by_slug = {it.get("slug"): it for it in data.get("items", [])}
    for it in data.get("items", []):
        if it.get("kind") != "pack":
            continue
        covers = []
        for bs in it.get("book_slugs") or []:
            cov = (by_slug.get(bs) or {}).get("cover")
            if cov:
                covers.append(cov)
        if covers:
            it["cover"] = covers[0]
            it["cover_stack"] = covers[:5]
        else:
            it.pop("cover", None)
            it.pop("cover_stack", None)

    LIVRES_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"[OK] covers livres={ok} miss={miss} -> {OUT_DIR}")


if __name__ == "__main__":
    main()
