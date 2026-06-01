# -*- coding: utf-8 -*-
"""Retire « (démo) » en fin de titre dans data-glightbox=\"title: …\"."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
pat = re.compile(r"\(démo\)(?=\")")


def main() -> None:
    for path in (ROOT / "assets" / "vitrines" / "demos").rglob("*.html"):
        text = path.read_text(encoding="utf-8")
        new = pat.sub("", text)
        if new != text:
            path.write_text(new, encoding="utf-8")
            print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
