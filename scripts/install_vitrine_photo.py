#!/usr/bin/env python3
"""Redimensionne et installe une image générée dans le dossier vitrine cible."""
from __future__ import annotations

import argparse
import io
import json
import os
import time
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "scripts" / "data" / "vitrine_photo_prompts.json"


def _save_png(img: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    buf = io.BytesIO()
    img.save(buf, format="PNG", optimize=True)
    data = buf.getvalue()
    tmp = path.with_name(f".{path.stem}.tmp.png")
    last_err: OSError | None = None
    for attempt in range(8):
        try:
            tmp.write_bytes(data)
            os.replace(tmp, path)
            return
        except OSError as err:
            last_err = err
            time.sleep(0.2 * (attempt + 1))
        finally:
            if tmp.exists():
                try:
                    tmp.unlink()
                except OSError:
                    pass
    if last_err:
        raise last_err


def _save_webp(img: Image.Image, path: Path, *, quality: int = 85) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, "WEBP", quality=quality, method=6)


def install(src: Path, slug: str, filename: str) -> Path:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    entry = next((e for e in manifest if e["slug"] == slug and e["filename"] == filename), None)
    if not entry:
        raise SystemExit(f"Entree introuvable : {slug}/{filename}")
    dest = ROOT / entry["dest"]
    w, h = entry["width"], entry["height"]
    with Image.open(src) as img:
        img = img.convert("RGB")
        img = img.resize((w, h), Image.Resampling.LANCZOS)
        _save_png(img, dest)
        _save_webp(img, dest.with_suffix(".webp"))
    print(f"[OK] {dest.relative_to(ROOT)} ({w}x{h}) + webp")
    return dest


def main() -> None:
    p = argparse.ArgumentParser(description="Installe une photo vitrine redimensionnée")
    p.add_argument("src", type=Path, help="Image source générée")
    p.add_argument("slug", help="Slug vitrine (ex. restauration)")
    p.add_argument("filename", help="Nom fichier cible (ex. hero.png)")
    args = p.parse_args()
    if not args.src.is_file():
        raise SystemExit(f"Fichier introuvable : {args.src}")
    install(args.src, args.slug, args.filename)


if __name__ == "__main__":
    main()
