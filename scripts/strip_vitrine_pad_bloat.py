#!/usr/bin/env python3
"""Retire FAQ/galerie/contact génériques ajoutés par pad_vitrine_lines.py."""
import re
from pathlib import Path

DEMOS = Path(__file__).resolve().parents[1] / "assets" / "vitrines" / "demos"

SECTION_RE = re.compile(
    r'\n\s*<section class="(?:pad-faq|[^"]*-galerie|pad-contact)[^"]*"[^>]*>.*?</section>',
    re.DOTALL,
)


def clean(html: str) -> str:
    html = SECTION_RE.sub("", html)
    html = html.replace("\\n", "")
    # hub-back mal placé
    html = re.sub(
        r'<p class="hub-back"><a href="\.\./index\.html">← Hub vitrines</a></p></section>',
        "",
        html,
    )
    return html


def main() -> None:
    for slug_dir in sorted(DEMOS.iterdir()):
        if not slug_dir.is_dir():
            continue
        index = slug_dir / "index.html"
        if not index.is_file():
            continue
        raw = index.read_text(encoding="utf-8")
        if "Réponse indicative" not in raw and "-galerie vt-reveal" not in raw:
            continue
        new = clean(raw)
        if new != raw:
            index.write_text(new, encoding="utf-8")
            print(f"cleaned {slug_dir.name}")


if __name__ == "__main__":
    main()
