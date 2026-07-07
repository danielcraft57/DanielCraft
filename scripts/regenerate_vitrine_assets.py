#!/usr/bin/env python3

"""Regénère démos, visuels uniques et typo — pipeline complet vitrines."""

from __future__ import annotations



import subprocess

import sys

from pathlib import Path



ROOT = Path(__file__).resolve().parents[1]

PY = sys.executable

SCRIPTS = [

    "generate_vitrines_ai.py",

    "gen_vitrine_assets.py",

]





def main() -> None:

    asset_args = [

        a for a in sys.argv[1:]

        if a in ("--force", "--skip-icons") or a.startswith("--slug") or a.startswith("--limit")

    ]

    for name in SCRIPTS:

        print(f"\n=== {name} ===")

        cmd = [PY, str(ROOT / "scripts" / name)]

        if name == "gen_vitrine_assets.py":

            cmd.extend(asset_args)

        subprocess.run(cmd, cwd=str(ROOT), check=True)

    print("\n[OK] Pipeline vitrines terminé — lancez : python build.py")





if __name__ == "__main__":

    main()

