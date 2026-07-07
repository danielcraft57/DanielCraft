#!/usr/bin/env python3
"""Corrige le double encodage UTF-8 dans src/data/vitrines.json."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VITRINES_JSON = ROOT / "src" / "data" / "vitrines.json"


def fix_text(s: str) -> str:
    s = s.replace("\u20ac\u201d", "\u2014")
    s = s.replace("\u20ac\u201c", "\u2014")
    s = s.replace("â€\u201d", "\u2014").replace("â€\u201c", "\u2014")
    s = s.replace("â€\"", "\u2014").replace("â€”", "\u2014")
    s = s.replace("Â«", "\u00ab").replace("Â»", "\u00bb")
    s = s.replace("Å\u201c", "\u0153").replace("Å“", "\u0153")
    for _ in range(5):
        if not re.search(r"[\u00c0-\u00ff]|Ã|â|Å", s):
            break
        try:
            t = s.encode("latin-1").decode("utf-8")
        except (UnicodeEncodeError, UnicodeDecodeError):
            break
        if t == s:
            break
        s = t
    return s


def walk(obj):
    if isinstance(obj, dict):
        return {k: walk(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [walk(x) for x in obj]
    if isinstance(obj, str):
        return fix_text(obj)
    return obj


def main() -> None:
    data = json.loads(VITRINES_JSON.read_text(encoding="utf-8"))
    fixed = walk(data)
    bad = []
    for it in fixed.get("items", []):
        ex = it.get("excerpt", "")
        if re.search(r"Ã|â€|Å|Â", ex):
            bad.append(it.get("slug", "?"))
    VITRINES_JSON.write_text(
        json.dumps(fixed, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    if bad:
        print(f"[WARN] Encodage suspect : {', '.join(bad)}")
    else:
        print(f"[OK] {VITRINES_JSON} — extraits corrigés")


if __name__ == "__main__":
    main()
