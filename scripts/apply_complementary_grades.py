#!/usr/bin/env python3
"""
Applique des déclinaisons de tonalité complémentaires / harmoniques sur les vignettes,
sur le même principe que les variables CSS --portfolio-tint-* (cycle de 6).

Chaque fichier reçoit une variante stable selon l'ordre alphabétique du nom
(même grille que :nth-child(6n+k) sur le site).

Dossiers : assets/images/projets (+ option hero)

Usage :
  python scripts/apply_complementary_grades.py
  # Captures d’UI sombres (recommandé) :
  python scripts/apply_complementary_grades.py --blend dark --strength 0.55 --punch 1.2
  # Effet maximal (toute l’image) :
  python scripts/apply_complementary_grades.py --blend full --strength 0.45 --punch 1.0

Dépend recommandé : numpy (requirements-scripts.txt)

--blend :
  dark   (défaut) — poids fort sur ombres / gris (idéal maquettes sombres)
  wide   — cloche large sur la luminance
  midtone — centre sur gris moyen (peu visible sur fond noir)
  full   — même poids partout (très visible)

--punch — amplifie l’écart des teintes par rapport au gris neutre (0.25..3).
"""
from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path
from typing import List, Tuple

_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from PIL import Image

from _image_tools import ROOT, iter_image_files, save_image

try:
    import numpy as np

    HAS_NP = True
except ImportError:
    HAS_NP = False

# Directions de teinte (autour de 1,1,1). L’intensité perçue vient surtout de --strength, --punch et --blend.
VARIANT_RGB: List[Tuple[str, Tuple[float, float, float]]] = [
    ("warm", (1.12, 1.06, 0.88)),
    ("coral", (1.1, 0.92, 0.9)),
    ("sage", (0.92, 1.12, 1.02)),
    ("gold", (1.14, 1.08, 0.82)),
    ("lilac", (1.05, 0.94, 1.14)),
    ("amber", (1.16, 0.94, 0.78)),
]


def variant_index_for_path(path: Path, n_variants: int = 6) -> int:
    """Index stable : hash MD5 complet modulo n (meilleure répartition que 8 hex)."""
    h = hashlib.md5(path.name.lower().encode("utf-8")).hexdigest()
    return int(h, 16) % n_variants


def _amplify_mult(
    mult: Tuple[float, float, float], punch: float
) -> Tuple[float, float, float]:
    """Écarte (R,G,B) par rapport à 1 selon punch (1 = défaut, 2 = effet ~doublé)."""
    p = max(0.25, min(3.0, punch))
    return tuple(1.0 + (x - 1.0) * p for x in mult)


def _blend_weight(lum: "np.ndarray", blend: str, strength: float) -> "np.ndarray":
    """Poids 0..1 par pixel. Les captures d’UI sombres nécessitent 'dark' ou 'wide'."""
    import numpy as np

    s = float(max(0.0, min(1.0, strength)))
    if blend == "full":
        return np.full_like(lum, s, dtype=np.float32)
    if blend == "dark":
        # Fort sur ombres et gris moyens (la plupart des maquettes sombres)
        w = np.clip((135.0 - lum) / 135.0, 0.0, 1.0)
        w = np.power(w, 0.75)
        return (s * w).astype(np.float32)
    if blend == "wide":
        # Cloche large : plus de pixels touchés qu’en midtone strict
        mid_w = np.clip(1.0 - np.abs(lum - 100.0) / 145.0, 0.0, 1.0)
        mid_w = np.power(mid_w, 0.55)
        return (s * mid_w).astype(np.float32)
    # midtone : ancien comportement (peu visible sur fonds noirs)
    mid_w = np.clip(1.0 - np.abs(lum - 118.0) / 118.0, 0.0, 1.0)
    mid_w = np.power(mid_w, 1.25)
    return (s * mid_w).astype(np.float32)


def grade_rgba(
    img: Image.Image,
    rgb_mult: Tuple[float, float, float],
    strength: float,
    blend: str = "dark",
    punch: float = 1.0,
) -> Image.Image:
    """Applique un grade coloré ; voir --blend et --punch."""
    rgba = img.convert("RGBA")
    mr, mg, mb = _amplify_mult(rgb_mult, punch)

    if not HAS_NP:
        return _grade_pillow(rgba, mr, mg, mb, strength, blend)

    # uint8 puis canaux explicites : évite le piège 2D où d[...,k] = colonnes k (broadcast 1024³)
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

    lum = 0.299 * r + 0.587 * g + 0.114 * b
    t = _blend_weight(lum, blend, strength)
    # Poids 2D uniquement (évite erreurs broadcast numpy 2.x entre r,g,b 2D et t 3D)

    tr = r * mr
    tg = g * mg
    tb = b * mb
    nr = np.clip(r * (1.0 - t) + tr * t, 0, 255)
    ng = np.clip(g * (1.0 - t) + tg * t, 0, 255)
    nb = np.clip(b * (1.0 - t) + tb * t, 0, 255)

    out = np.empty((h, w, 4), dtype=np.uint8)
    out[:, :, 0] = nr.astype(np.uint8)
    out[:, :, 1] = ng.astype(np.uint8)
    out[:, :, 2] = nb.astype(np.uint8)
    out[:, :, 3] = np.clip(a, 0, 255).astype(np.uint8)
    return Image.fromarray(out)


def _lum_blend_weight(lum: float, blend: str, strength: float) -> float:
    s = max(0.0, min(1.0, strength))
    if blend == "full":
        return s
    if blend == "dark":
        w = max(0.0, min(1.0, (135.0 - lum) / 135.0))
        return s * (w**0.75)
    if blend == "wide":
        mid_w = max(0.0, min(1.0, 1.0 - abs(lum - 100.0) / 145.0))
        return s * (mid_w**0.55)
    mid_w = max(0.0, min(1.0, 1.0 - abs(lum - 118.0) / 118.0))
    return s * (mid_w**1.25)


def _grade_pillow(
    rgba: Image.Image,
    mr: float,
    mg: float,
    mb: float,
    strength: float,
    blend: str,
) -> Image.Image:
    px = rgba.load()
    w, h = rgba.size
    for y in range(h):
        for x in range(w):
            pr, pg, pb, pa = px[x, y]
            lum = 0.299 * pr + 0.587 * pg + 0.114 * pb
            t = _lum_blend_weight(lum, blend, strength)
            tr, tg, tb = pr * mr, pg * mg, pb * mb
            pr = int(max(0, min(255, pr * (1 - t) + tr * t)))
            pg = int(max(0, min(255, pg * (1 - t) + tg * t)))
            pb = int(max(0, min(255, pb * (1 - t) + tb * t)))
            px[x, y] = (pr, pg, pb, pa)
    return rgba


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Cycle de grades complémentaires sur les images portfolio."
    )
    ap.add_argument(
        "--strength",
        type=float,
        default=0.5,
        help="Intensité 0..1 (défaut 0.5). Combiner avec --blend dark pour les UI sombres.",
    )
    ap.add_argument(
        "--blend",
        choices=("dark", "wide", "midtone", "full"),
        default="dark",
        help="Où appliquer la teinte : dark=recommandé pour vignettes sombres (défaut).",
    )
    ap.add_argument(
        "--punch",
        type=float,
        default=1.15,
        help="Amplification des couleurs 0.25..3 (défaut 1.15). >1 = complémentaires plus marqués.",
    )
    ap.add_argument(
        "--include-hero",
        action="store_true",
        help="Inclure assets/images/hero (défaut : projets seulement)",
    )
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    dirs = [ROOT / "assets" / "images" / "projets"]
    if args.include_hero:
        dirs.append(ROOT / "assets" / "images" / "hero")

    files = iter_image_files(dirs)
    if not files:
        print("[WARN] Aucune image.")
        return

    if not HAS_NP:
        print("[INFO] NumPy absent : traitement lent. pip install numpy recommandé.")

    done = []
    for path in files:
        idx = variant_index_for_path(path)
        name, mult = VARIANT_RGB[idx]
        try:
            with Image.open(path) as im:
                out = grade_rgba(
                    im,
                    mult,
                    args.strength,
                    blend=args.blend,
                    punch=args.punch,
                )
            if args.dry_run:
                print(f"[DRY] {path.name} -> {name} {mult}")
            else:
                save_image(path, out)
                done.append((path.relative_to(ROOT).as_posix(), name))
        except Exception as e:
            print(f"[WARN] {path.name}: {e}")

    print(
        f"[OK] apply_complementary_grades : {len(done)} fichier(s)"
        + (" (dry-run)" if args.dry_run else "")
    )
    for path_s, vname in done:
        print(f"  - {path_s}  ({vname})")


if __name__ == "__main__":
    main()
