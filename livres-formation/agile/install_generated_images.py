#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Copie couvertures, scenes et felicitations generees vers chaque livre agile."""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]
ASSETS_CANDIDATES = [
    REPO / "assets",
    Path.home() / ".cursor" / "projects" / "c-Users-loicDaniel-Documents-DanielCraft-DanielCraftFr" / "assets",
]

INSTALL = {
    "gestion-projet": [
        "agile-couverture.png",
        "agile-scene-livrable.png",
        "agile-scene-backlog.png",
        "agile-scene-retro.png",
        "agile-felicitations.png",
    ],
    "methodologie-scrum": [
        "scrum-couverture.png",
        "scrum-scene-roles.png",
        "scrum-scene-daily.png",
        "scrum-scene-board.png",
        "scrum-felicitations.png",
    ],
    "scrum-master": [
        "sm-couverture.png",
        "sm-scene-facilitation.png",
        "sm-scene-freins.png",
        "sm-scene-coaching.png",
        "sm-felicitations.png",
    ],
    "product-owner": [
        "po-couverture.png",
        "po-scene-vision.png",
        "po-scene-priorisation.png",
        "po-scene-backlog.png",
        "po-felicitations.png",
    ],
}


def find_src(name: str) -> Path | None:
    for base in ASSETS_CANDIDATES:
        p = base / name
        if p.is_file():
            return p
    return None


def main() -> int:
    ok = 0
    miss = 0
    for book, names in INSTALL.items():
        dest_dir = ROOT / book / "images"
        dest_dir.mkdir(parents=True, exist_ok=True)
        for name in names:
            src = find_src(name)
            if src is None:
                print(f"[MISS] {name}")
                miss += 1
                continue
            shutil.copy2(src, dest_dir / name)
            print(f"[OK] {book}/{name} <- {src}")
            ok += 1
    print(f"Done: {ok} copied, {miss} missing")
    return 1 if miss else 0


if __name__ == "__main__":
    raise SystemExit(main())
