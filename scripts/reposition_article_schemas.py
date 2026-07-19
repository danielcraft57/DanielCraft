#!/usr/bin/env python3
"""Repositionne schemas / bannieres dans les articles blog.

Regles (voir docs/GUIDE_ARTICLES_CAPTIVANTS.md) :
- Retire les bannieres inline (le hero OG suffit en tete d'article)
- Retire les illustrations decoratives empilees sous le H1 (webp/jpg hors schemas)
- Place les schemas SVG encore sous l'intro apres 1-2 paragraphes du 1er H2
- Ne deplace PAS les schemas deja dans une section
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "blog" / "content" / "articles"

FIGURE_RE = re.compile(
    r"<figure(?:\s[^>]*)?>\s*<img[^>]+>\s*(?:<figcaption>.*?</figcaption>\s*)?</figure>\s*",
    re.IGNORECASE | re.DOTALL,
)


def is_banner(fig: str) -> bool:
    return "illustrations/" in fig and "-banner." in fig


def is_schema(fig: str) -> bool:
    src = re.search(r'src=["\']([^"\']+)["\']', fig, re.I)
    if not src:
        return False
    path = src.group(1).lower()
    if path.endswith(".svg"):
        return True
    if "/schemas/" in path:
        return True
    return False


def is_decorative_head(fig: str) -> bool:
    """Illustration non pedagogique empilee en tete (hero suffit)."""
    if is_banner(fig) or is_schema(fig):
        return False
    src = re.search(r'src=["\']([^"\']+)["\']', fig, re.I)
    if not src:
        return False
    path = src.group(1).lower()
    return any(path.endswith(ext) for ext in (".webp", ".jpg", ".jpeg", ".png"))


def classify_figure(fig: str) -> str:
    if is_banner(fig):
        return "drop"
    if is_decorative_head(fig):
        return "drop"
    if is_schema(fig):
        return "schema"
    return "keep"


def with_schema_class(fig: str) -> str:
    fig = fig.strip()
    if "schema-figure" in fig:
        return fig
    if fig.startswith("<figure>"):
        return fig.replace("<figure>", '<figure class="schema-figure">', 1)
    if re.match(r"<figure\s", fig, re.I):
        return re.sub(r"<figure\b", '<figure class="schema-figure"', fig, count=1, flags=re.I)
    return fig


def insert_after_first_h2(body: str, block: str) -> str:
    m = re.search(r"\n## [^\n]+\n", body)
    if not m:
        h1 = re.search(r"^# .+\n+", body, re.MULTILINE)
        insert_at = h1.end() if h1 else 0
        rest = body[insert_at:]
        paras = re.split(r"\n\n+", rest, maxsplit=2)
        if len(paras) >= 3:
            insert_at = insert_at + len(paras[0]) + 2 + len(paras[1]) + 2
        return body[:insert_at] + "\n\n" + block + body[insert_at:]

    section_start = m.end()
    rest = body[section_start:]
    parts = re.split(r"(\n\n+)", rest)
    para_count = 0
    idx = 0
    while idx < len(parts) and para_count < 2:
        chunk = parts[idx]
        if chunk.strip() and not chunk.startswith("##") and not chunk.startswith("<") and not chunk.startswith("---"):
            para_count += 1
            idx += 1
            if idx < len(parts) and re.match(r"\n\n+", parts[idx] or ""):
                idx += 1
            continue
        if re.match(r"\n\n+", chunk or ""):
            idx += 1
            continue
        if chunk.startswith("##") or chunk.startswith("---"):
            break
        idx += 1

    insert_rel = sum(len(parts[i]) for i in range(idx))
    insert_abs = section_start + insert_rel
    return body[:insert_abs] + block + body[insert_abs:]


def reposition(text: str) -> str:
    first_h2 = re.search(r"\n## ", text)
    h2_pos = first_h2.start() if first_h2 else len(text)

    to_move: list[str] = []
    keep_map: list[tuple[int, int, str]] = []  # start, end, replacement or ""

    for m in FIGURE_RE.finditer(text):
        block = m.group(0)
        kind = classify_figure(block)
        before_h2 = m.start() < h2_pos

        if kind == "drop":
            keep_map.append((m.start(), m.end(), ""))
            continue

        if kind == "schema":
            styled = with_schema_class(block) + "\n\n"
            if before_h2:
                keep_map.append((m.start(), m.end(), ""))
                to_move.append(styled)
            else:
                # deja dans une section : juste ajouter la classe
                keep_map.append((m.start(), m.end(), styled if styled.strip() != block.strip() else block))
            continue

        # keep other figures as-is
        keep_map.append((m.start(), m.end(), block))

    if not keep_map and not to_move:
        return text

    # Rebuild from end to start
    body = text
    for start, end, repl in reversed(keep_map):
        body = body[:start] + repl + body[end:]

    body = re.sub(r"\n{3,}", "\n\n", body)

    if to_move:
        body = insert_after_first_h2(body, "".join(to_move))
        body = re.sub(r"\n{3,}", "\n\n", body)

    return body


def process_file(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---"):
        return False
    end = raw.find("\n---", 3)
    if end < 0:
        return False
    fm = raw[: end + 4]
    body = raw[end + 4 :]
    new_body = reposition(body)
    if new_body == body:
        return False
    path.write_text(fm + new_body, encoding="utf-8")
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--glob",
        default="design-patterns-*.md",
        help="Glob sous blog/content/articles (defaut: design-patterns-*.md)",
    )
    args = parser.parse_args()
    paths = sorted(ARTICLES.glob(args.glob))
    changed = 0
    for path in paths:
        if process_file(path):
            changed += 1
            print(f"[OK] {path.name}")
    print(f"updated={changed}/{len(paths)}")


if __name__ == "__main__":
    main()
