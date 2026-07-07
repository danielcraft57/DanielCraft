#!/usr/bin/env python3
"""Injecte vitrine-prose.css dans toutes les démos HTML."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "assets" / "vitrines" / "demos"
LINK = '<link rel="stylesheet" href="../shared/vitrine-prose.css">'


def main() -> None:
    n = 0
    for html in ROOT.rglob("index.html"):
        if "shared" in html.parts:
            continue
        text = html.read_text(encoding="utf-8")
        if "vitrine-prose.css" in text:
            continue
        if 'href="styles.css"' in text:
            text = text.replace('href="styles.css"', 'href="../shared/vitrine-prose.css">\n  <link rel="stylesheet" href="styles.css"', 1)
        elif "<head>" in text:
            text = text.replace("<head>", f"<head>\n  {LINK}", 1)
        else:
            continue
        html.write_text(text, encoding="utf-8")
        n += 1
        print("patched", html.parent.name)
    print(f"[OK] {n} démos patchées")


if __name__ == "__main__":
    main()
