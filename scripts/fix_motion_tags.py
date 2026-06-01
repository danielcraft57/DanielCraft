#!/usr/bin/env python3
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1] / "assets" / "vitrines" / "demos"
for p in root.rglob("index.html"):
    t = p.read_text(encoding="utf-8")
    new = re.sub(r"</?motion\b", lambda m: m.group(0).replace("motion", "div"), t)
    if new != t:
        p.write_text(new, encoding="utf-8")
        print("fixed", p)
