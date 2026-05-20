#!/usr/bin/env python3
"""Régénère images OG et SVG — délègue au générateur principal de la série."""

from __future__ import annotations

import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).parent))

from generate_design_patterns_serie import write_og_images, write_svgs  # noqa: E402


def main() -> None:
    write_svgs()
    write_og_images()
    print("Assets Design Patterns OK (style unifié)")


if __name__ == "__main__":
    main()
