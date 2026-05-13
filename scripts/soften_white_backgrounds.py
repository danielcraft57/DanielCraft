#!/usr/bin/env python3
"""
Adoucit les fonds blancs / gris très clairs des visuels pour les fondre
dans la palette du site (bleus pastel #e8f2fc, #ecf6ff) au lieu d'un blanc pur.

Traite : assets/images/projets/*.jpg, about-section-hero.png/.webp (raster depuis `rasterize_about_hero.py`) si présents,
         et assets/images/hero/* si présent (hors gitignore local).

Usage :
  python scripts/soften_white_backgrounds.py
  python scripts/soften_white_backgrounds.py --max-side 1920   # défaut : rapide
  python scripts/soften_white_backgrounds.py --max-side 0      # pleine résolution (lent)
  python scripts/soften_white_backgrounds.py --skip-hero       # ignore hero (souvent très lourd)

Suite possible : reduce_blue_cast.py + apply_complementary_grades.py
ou portfolio_image_pipeline.py — voir scripts/README_IMAGES.md
"""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image
from PIL import ImageFile

ROOT = Path(__file__).resolve().parents[1]

# PNG incomplets (copie tronquée) : charger le maximum de données
ImageFile.LOAD_TRUNCATED_IMAGES = True

# Proche du hero / cartes (évite le contraste « boîte blanche »)
TARGET_R, TARGET_G, TARGET_B = 232, 242, 252


def _soften_numpy_core(rgba: Image.Image) -> Image.Image:
    """Traite une image déjà à la taille de travail (éviter float32 inutile)."""
    import numpy as np

    arr = np.asarray(rgba, dtype=np.uint8)
    r, g, b, a = arr[..., 0], arr[..., 1], arr[..., 2], arr[..., 3]
    mx = np.maximum(np.maximum(r, g), b)
    mn = np.minimum(np.minimum(r, g), b)
    spread = mx.astype(np.int16) - mn.astype(np.int16)

    near_white = (mx >= 218) & (spread <= 42) & (mn >= 185)
    t = np.clip((mx.astype(np.float32) - 218.0) / 37.0, 0.0, 1.0)
    t = np.where(near_white, t, 0.0)
    t = t[..., np.newaxis]

    rgb = arr[..., :3].astype(np.float32)
    trg = np.array([TARGET_R, TARGET_G, TARGET_B], dtype=np.float32)
    out_rgb = rgb * (1.0 - t) + trg * t
    out = np.empty_like(arr)
    out[..., 0] = np.clip(out_rgb[..., 0], 0, 255).astype(np.uint8)
    out[..., 1] = np.clip(out_rgb[..., 1], 0, 255).astype(np.uint8)
    out[..., 2] = np.clip(out_rgb[..., 2], 0, 255).astype(np.uint8)
    out[..., 3] = a
    # Pillow 13+ : éviter l’argument positionnel "mode" déprécié
    return Image.fromarray(out)


def soften_rgba(img: Image.Image, max_working_side: int = 1920) -> Image.Image:
    """
    Remplace les pixels très clairs et peu saturés par un bleu pastel.

    max_working_side : si le plus grand côté dépasse cette valeur, le filtre est
    appliqué sur une copie redimensionnée puis réétalée (beaucoup plus rapide, rendu
    suffisant pour des fonds plats). 0 = toujours pleine résolution.
    """
    rgba = img.convert("RGBA")
    w, h = rgba.size
    side = max(w, h)

    try:
        import numpy as np  # noqa: F401
    except ImportError:
        return _soften_pillow_only(rgba)

    if max_working_side > 0 and side > max_working_side:
        scale = max_working_side / float(side)
        nw = max(1, int(round(w * scale)))
        nh = max(1, int(round(h * scale)))
        small = rgba.resize((nw, nh), Image.Resampling.LANCZOS)
        out_small = _soften_numpy_core(small)
        return out_small.resize((w, h), Image.Resampling.LANCZOS)

    return _soften_numpy_core(rgba)


def _soften_pillow_only(rgba: Image.Image) -> Image.Image:
    """Sans NumPy : lent ; à éviter sur grosses images."""
    out_px = []
    append = out_px.append
    flat = (
        rgba.get_flattened_data()
        if hasattr(rgba, "get_flattened_data")
        else rgba.getdata()
    )
    for pr, pg, pb, pa in flat:
        mx = pr if pr >= pg and pr >= pb else (pg if pg >= pb else pb)
        mn = pr if pr <= pg and pr <= pb else (pg if pg <= pb else pb)
        spread = mx - mn
        if mx >= 218 and spread <= 42 and mn >= 185:
            strength = min(1.0, max(0.0, (mx - 218) / 37.0))
            pr = int(pr * (1 - strength) + TARGET_R * strength)
            pg = int(pg * (1 - strength) + TARGET_G * strength)
            pb = int(pb * (1 - strength) + TARGET_B * strength)
        append((pr, pg, pb, pa))
    rgba.putdata(out_px)
    return rgba


def save_image(path: Path, img: Image.Image) -> None:
    suf = path.suffix.lower()
    if suf in {".jpg", ".jpeg"}:
        img.convert("RGB").save(path, quality=92, optimize=True)
    elif suf == ".webp":
        img.save(path, "WEBP", quality=90, method=6)
    else:
        img.save(path, optimize=True)


def main() -> None:
    ap = argparse.ArgumentParser(description="Adoucit les fonds blancs des visuels.")
    ap.add_argument(
        "--max-side",
        type=int,
        default=1920,
        help="Côté max pour le calcul (0 = pleine résolution, très lent sur hero). Défaut 1920.",
    )
    ap.add_argument(
        "--skip-hero",
        action="store_true",
        help="Ne pas traiter assets/images/hero/",
    )
    args = ap.parse_args()

    targets: list[Path] = []

    projets = ROOT / "assets" / "images" / "projets"
    if projets.is_dir():
        targets.extend(
            p for p in projets.iterdir() if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}
        )

    for name in ("about-section-hero.png", "about-section-hero.webp"):
        p = ROOT / "assets" / "images" / name
        if p.is_file():
            targets.append(p)

    if not args.skip_hero:
        hero_dir = ROOT / "assets" / "images" / "hero"
        if hero_dir.is_dir():
            targets.extend(
                p
                for p in hero_dir.iterdir()
                if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}
            )

    max_side = args.max_side if args.max_side > 0 else 0
    done = []
    for path in sorted(set(targets)):
        try:
            with Image.open(path) as im:
                im.load()
                w, h = im.size
                print(f"  … {path.name} ({w}×{h})", flush=True)
                out = soften_rgba(im, max_working_side=max_side)
                save_image(path, out)
                done.append(path.relative_to(ROOT).as_posix())
        except Exception as e:
            print(f"[WARN] {path.name}: {e}")

    print(f"[OK] Fonds adoucis: {len(done)} fichier(s)")
    for d in done:
        print(f"  - {d}")


if __name__ == "__main__":
    main()
