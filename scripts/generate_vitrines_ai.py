#!/usr/bin/env python3
"""Génère les 22 vitrines via contenu IA (scripts/vitrine_ai_batch_*.py)."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from vitrine_gen_multipage import run as run_multipage


def main() -> None:
    print("=== Vitrines IA multi-pages (22 × 4 pages) ===")
    run_multipage()
    print("OK — vitrines générées dans assets/vitrines/demos/")


if __name__ == "__main__":
    main()
