#!/usr/bin/env python3
"""
Enchaîne les traitements d'images portfolio / hero dans un ordre conseillé.

Ordre par défaut :
  1. soften_white_backgrounds.py
  2. reduce_blue_cast.py
  3. apply_complementary_grades.py

Usage :
  python scripts/portfolio_image_pipeline.py
  python scripts/portfolio_image_pipeline.py --grade-blend dark --grade-punch 1.3 --grade-strength 0.55
  python scripts/portfolio_image_pipeline.py --skip-soften
  python scripts/portfolio_image_pipeline.py --include-hero-grades --dry-run
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY = sys.executable


def run_step(args_list: list[str]) -> int:
    cmd = [PY, *args_list]
    print(f"\n>>> {' '.join(cmd)}\n")
    r = subprocess.run(cmd, cwd=str(ROOT))
    return r.returncode


def main() -> int:
    ap = argparse.ArgumentParser(description="Pipeline images portfolio / hero")
    ap.add_argument("--skip-soften", action="store_true")
    ap.add_argument("--skip-reduce-blue", action="store_true")
    ap.add_argument("--skip-grades", action="store_true")
    ap.add_argument("--include-hero-grades", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--reduce-strength", type=float, default=0.5)
    ap.add_argument("--grade-strength", type=float, default=0.5)
    ap.add_argument(
        "--grade-blend",
        choices=("dark", "wide", "midtone", "full"),
        default="dark",
        help="Mode apply_complementary_grades (défaut dark = UI sombres).",
    )
    ap.add_argument(
        "--grade-punch",
        type=float,
        default=1.15,
        help="Amplification des teintes complémentaires (défaut 1.15).",
    )
    ap.add_argument(
        "--soften-max-side",
        type=int,
        default=1920,
        help="Passé à soften_white_backgrounds (0 = pleine résolution, lent). Défaut 1920.",
    )
    ap.add_argument(
        "--soften-skip-hero",
        action="store_true",
        help="Ne pas lancer soften sur assets/images/hero/",
    )
    args = ap.parse_args()

    scripts = ROOT / "scripts"

    if not args.skip_soften:
        soften_cmd = [str(scripts / "soften_white_backgrounds.py"), "--max-side", str(args.soften_max_side)]
        if args.soften_skip_hero:
            soften_cmd.append("--skip-hero")
        if run_step(soften_cmd) != 0:
            return 1

    if not args.skip_reduce_blue:
        step = [
            str(scripts / "reduce_blue_cast.py"),
            "--strength",
            str(args.reduce_strength),
        ]
        if args.dry_run:
            step.append("--dry-run")
        if run_step(step) != 0:
            return 1

    if not args.skip_grades:
        step = [
            str(scripts / "apply_complementary_grades.py"),
            "--strength",
            str(args.grade_strength),
            "--blend",
            args.grade_blend,
            "--punch",
            str(args.grade_punch),
        ]
        if args.include_hero_grades:
            step.append("--include-hero")
        if args.dry_run:
            step.append("--dry-run")
        if run_step(step) != 0:
            return 1

    print("\n[DONE] portfolio_image_pipeline")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
