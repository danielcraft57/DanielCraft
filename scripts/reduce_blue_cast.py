#!/usr/bin/env python3
"""
Réduit une dominante bleue / cyan trop uniforme (ex. après recolor_project_hero_to_blue.py).

Approche : sur les pixels nettement « bleus » (canal B dominant, saturation HSV),
on rapproche légèrement les canaux R/V/B et on baisse un peu le bleu pour rétablir
du naturel, sans retomber sur du rouge.

Dossiers : assets/images/projets, assets/images/hero (comme recolor_project_hero_to_blue.py)

Usage :
  python scripts/reduce_blue_cast.py
  python scripts/reduce_blue_cast.py --strength 0.55
  python scripts/reduce_blue_cast.py --dry-run

Dépend recommandé : pip install -r requirements-scripts.txt (numpy)
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from PIL import Image

from _image_tools import DEFAULT_TARGET_DIRS, ROOT, iter_image_files, save_image

try:
    import numpy as np

    HAS_NP = True
except ImportError:
    HAS_NP = False


def reduce_blue_rgba(img: Image.Image, strength: float) -> Image.Image:
    """
    strength: 0 = rien, 1 = correction max raisonnable sur les pixels bleu-dominants.
    """
    rgba = img.convert("RGBA")
    s = max(0.0, min(1.0, strength))

    if not HAS_NP:
        return _reduce_blue_pillow(rgba, s)

    arr = np.asarray(rgba.convert("RGBA"), dtype=np.uint8)
    if arr.ndim == 2:
        arr = np.stack(
            [arr, arr, arr, np.full(arr.shape, 255, dtype=np.uint8)], axis=2
        )
    if arr.ndim != 3 or arr.shape[2] not in (3, 4):
        raise ValueError(
            f"Forme numpy inattendue {arr.shape!r} (attendu H×W×3 ou H×W×4)"
        )
    if arr.shape[2] == 3:
        a255 = np.full(arr.shape[:2] + (1,), 255, dtype=np.uint8)
        arr = np.concatenate([arr, a255], axis=2)

    h, w, _ = arr.shape
    r = arr[:, :, 0].astype(np.float32)
    g = arr[:, :, 1].astype(np.float32)
    b = arr[:, :, 2].astype(np.float32)
    a = arr[:, :, 3].astype(np.float32)

    b_dom = (b >= r + 12) & (b >= g + 8) & (b >= 55)
    lum = 0.299 * r + 0.587 * g + 0.114 * b
    valid = b_dom & (lum > 35) & (lum < 248)
    mx = np.maximum(np.maximum(r, g), b)
    mn = np.minimum(np.minimum(r, g), b)
    sat = np.where(mx < 1e-3, 0, (mx - mn) / (mx + 1e-3))
    valid = valid & (sat > 0.12)

    t = s * 0.6 * valid.astype(np.float32)
    lift_r = t * 10.0
    lift_g = t * 7.0
    drop_b = t * 16.0
    nr = np.clip(r + lift_r, 0, 255)
    ng = np.clip(g + lift_g, 0, 255)
    nb = np.clip(b - drop_b, 0, 255)

    out = np.empty((h, w, 4), dtype=np.uint8)
    out[:, :, 0] = nr.astype(np.uint8)
    out[:, :, 1] = ng.astype(np.uint8)
    out[:, :, 2] = nb.astype(np.uint8)
    out[:, :, 3] = np.clip(a, 0, 255).astype(np.uint8)
    return Image.fromarray(out)


def _reduce_blue_pillow(rgba: Image.Image, strength: float) -> Image.Image:
    px = rgba.load()
    w, h = rgba.size
    for y in range(h):
        for x in range(w):
            pr, pg, pb, pa = px[x, y]
            if pb < pr + 12 or pb < pg + 8 or pb < 55:
                continue
            lum = 0.299 * pr + 0.587 * pg + 0.114 * pb
            if lum <= 35 or lum >= 248:
                continue
            mx = max(pr, pg, pb)
            mn = min(pr, pg, pb)
            sat = (mx - mn) / (mx + 1e-3) if mx > 0 else 0
            if sat <= 0.12:
                continue
            t = strength * 0.6
            pr = int(max(0, min(255, pr + t * 10)))
            pg = int(max(0, min(255, pg + t * 7)))
            pb = int(max(0, min(255, pb - t * 16)))
            px[x, y] = (pr, pg, pb, pa)
    return rgba


def main() -> None:
    ap = argparse.ArgumentParser(description="Réduit la dominante bleue des vignettes.")
    ap.add_argument(
        "--strength",
        type=float,
        default=0.5,
        help="Intensité 0..1 (défaut 0.5)",
    )
    ap.add_argument("--dry-run", action="store_true", help="Ne pas écrire les fichiers")
    ap.add_argument(
        "--dirs",
        nargs="*",
        type=Path,
        help="Dossiers d'images (défaut : projets + hero)",
    )
    args = ap.parse_args()

    dirs = [Path(p).resolve() for p in args.dirs] if args.dirs else DEFAULT_TARGET_DIRS
    files = iter_image_files(dirs)
    if not files:
        print("[WARN] Aucune image trouvée.")
        return

    if not HAS_NP:
        print("[INFO] NumPy absent : traitement pixel par pixel (lent). pip install numpy recommandé.")

    done = []
    for path in files:
        try:
            with Image.open(path) as im:
                out = reduce_blue_rgba(im, args.strength)
            if args.dry_run:
                print(f"[DRY] {path.relative_to(ROOT)}")
            else:
                save_image(path, out)
                done.append(path.relative_to(ROOT).as_posix())
        except Exception as e:
            print(f"[WARN] {path.name}: {e}")

    print(f"[OK] reduce_blue_cast : {len(done)} fichier(s)" + (" (dry-run)" if args.dry_run else ""))
    for d in done:
        print(f"  - {d}")


if __name__ == "__main__":
    main()
