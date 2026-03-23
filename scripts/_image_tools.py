"""
Utilitaires partagés par les scripts de traitement d'images (portfolio, hero).
"""
from __future__ import annotations

from pathlib import Path
from typing import Iterable, List

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
EXTS = {".png", ".jpg", ".jpeg", ".webp"}

DEFAULT_TARGET_DIRS = [
    ROOT / "assets" / "images" / "projets",
    ROOT / "assets" / "images" / "hero",
]


def save_image(path: Path, img: Image.Image) -> None:
    suf = path.suffix.lower()
    if suf in {".jpg", ".jpeg"}:
        img.convert("RGB").save(path, quality=92, optimize=True)
    elif suf == ".webp":
        img.save(path, "WEBP", quality=90, method=6)
    else:
        img.save(path, optimize=True)


def iter_image_files(
    dirs: Iterable[Path],
    exts: set[str] | None = None,
) -> List[Path]:
    ex = exts or EXTS
    out: List[Path] = []
    for d in dirs:
        if not d.is_dir():
            continue
        for p in d.iterdir():
            if p.is_file() and p.suffix.lower() in ex:
                out.append(p)
    return sorted(out, key=lambda x: x.name.lower())
