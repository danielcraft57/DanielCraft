#!/usr/bin/env python3
"""Fix old dp-* banner paths and accented chars in article image src."""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

ARTICLES = Path(__file__).resolve().parents[1] / "blog" / "content" / "articles"


def main() -> None:
    fixed_dp = 0
    for path in ARTICLES.glob("design-patterns-*.md"):
        text = path.read_text(encoding="utf-8")

        def repl_dp(match: re.Match[str]) -> str:
            quote = match.group(1)
            src = match.group(2)
            src = src.replace("/dp-", "/design-patterns-").replace("illustrations/dp-", "illustrations/design-patterns-")
            return f"src={quote}{src}{quote}"

        new = re.sub(r'src=(["\'])([^"\']*dp-[a-z0-9-]+-banner\.(?:webp|jpg))\1', repl_dp, text)
        if new != text:
            path.write_text(new, encoding="utf-8")
            fixed_dp += 1
            print(f"[dp] {path.name}")

    fixed_acc = 0
    for path in ARTICLES.glob("*.md"):
        text = path.read_text(encoding="utf-8")

        def fold_src(match: re.Match[str]) -> str:
            quote, src = match.group(1), match.group(2)
            folded = unicodedata.normalize("NFD", src)
            folded = "".join(c for c in folded if unicodedata.category(c) != "Mn")
            if folded != src:
                return f"src={quote}{folded}{quote}"
            return match.group(0)

        new = re.sub(r'src=(["\'])([^"\']+)\1', fold_src, text)
        if new != text:
            path.write_text(new, encoding="utf-8")
            fixed_acc += 1
            print(f"[accent] {path.name}")

    print(f"Done: dp={fixed_dp}, accent={fixed_acc}")


if __name__ == "__main__":
    main()
