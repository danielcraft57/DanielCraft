#!/usr/bin/env python3
"""
Pipeline images Open Graph (assets/images/og) : teinte bleu métal + filtres.

Enchaîne (comme README_IMAGES.md pour le portfolio, adapté aux cartes 1200×630) :
  1. Recolorisation rouge/orange → bleu métal (même logique que recolor_project_hero_to_blue.py)
  2. Atténuation de la dominante bleue (reduce_blue_cast)
  3. Grades complémentaires cyclés par fichier (apply_complementary_grades) — blend « wide » par défaut (visuels clairs)
  4. Optionnel : recadrage / compression 1200×630 + WebP (optimize_images)

Usage (depuis la racine du dépôt) :
  python scripts/og_image_pipeline.py
  python scripts/og_image_pipeline.py --dry-run
  python scripts/og_image_pipeline.py --skip-recolor --reduce-strength 0.4
  python scripts/og_image_pipeline.py --no-optimize

Les fichiers sont ignorés par git (.gitignore assets/images/og/*) : le script s’applique
aux JPEG/PNG/WebP présents localement dans ce dossier.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from PIL import Image

from _image_tools import ROOT, iter_image_files, save_image
from apply_complementary_grades import VARIANT_RGB, grade_rgba, variant_index_for_path
from optimize_images import generate_webp_for_path, optimize_image
from recolor_project_hero_to_blue import recolor_blue_metal
from reduce_blue_cast import reduce_blue_rgba

OG_DIR = ROOT / "assets" / "images" / "og"
RATIO_OG = 1200 / 630
OG_SOURCE_EXTS = {".jpg", ".jpeg", ".png"}


def collect_og_images() -> list[Path]:
    """JPEG/PNG uniquement : les WebP sont régénérés après optimisation."""
    return [
        p
        for p in iter_image_files([OG_DIR])
        if p.suffix.lower() in OG_SOURCE_EXTS
    ]


def main() -> int:
    ap = argparse.ArgumentParser(description="Pipeline bleu + filtres pour les images Open Graph")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--skip-recolor", action="store_true", help="Ne pas appliquer le bleu métal")
    ap.add_argument(
        "--reduce-strength",
        type=float,
        default=0.45,
        help="reduce_blue_cast 0..1 (défaut 0.45)",
    )
    ap.add_argument(
        "--grade-strength",
        type=float,
        default=0.34,
        help="Intensité des grades complémentaires (défaut 0.34, visuels clairs)",
    )
    ap.add_argument(
        "--grade-blend",
        choices=("dark", "wide", "midtone", "full"),
        default="wide",
        help="Zone d’application du grade (défaut wide pour cartes OG claires)",
    )
    ap.add_argument(
        "--grade-punch",
        type=float,
        default=1.08,
        help="Amplification des teintes (défaut 1.08)",
    )
    ap.add_argument(
        "--no-optimize",
        action="store_true",
        help="Ne pas recadrer/compresser en 1200×630 ni régénérer le WebP",
    )
    args = ap.parse_args()

    if not OG_DIR.is_dir():
        print(f"[ERREUR] Dossier introuvable : {OG_DIR}")
        return 1

    files = collect_og_images()
    if not files:
        print(
            f"[WARN] Aucune image dans {OG_DIR} "
            "(extensions .jpg .jpeg .png .webp). "
            "Les fichiers OG sont souvent locaux (gitignore)."
        )
        return 0

    print(f"[INFO] {len(files)} fichier(s) à traiter dans og/")
    done: list[str] = []

    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        try:
            with Image.open(path) as im:
                out = im
                if not args.skip_recolor:
                    out = recolor_blue_metal(out)
                out = reduce_blue_rgba(out, args.reduce_strength)
                idx = variant_index_for_path(path)
                _name, mult = VARIANT_RGB[idx]
                out = grade_rgba(
                    out,
                    mult,
                    args.grade_strength,
                    blend=args.grade_blend,
                    punch=args.grade_punch,
                )

            if args.dry_run:
                print(f"[DRY] {rel} -> grade #{idx} {_name}")
                continue

            save_image(path, out)

            if not args.no_optimize:
                ext = path.suffix.lower()
                if ext in {".jpg", ".jpeg", ".png"}:
                    optimize_image(
                        path,
                        target_ratio=RATIO_OG,
                        exact_size=(1200, 630),
                        quality=82,
                    )
                    wp = path.with_suffix(".webp")
                    if wp.is_file():
                        wp.unlink()
                    generate_webp_for_path(path, quality=82)
            done.append(rel)
        except Exception as e:
            print(f"[WARN] {path.name}: {e}")

    print(f"[OK] og_image_pipeline : {len(done)} fichier(s)" + (" (dry-run)" if args.dry_run else ""))
    for d in done:
        print(f"  - {d}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
