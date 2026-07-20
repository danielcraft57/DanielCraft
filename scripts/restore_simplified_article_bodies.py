#!/usr/bin/env python3
"""Restore long article bodies after over-aggressive simplify scripts.

Keeps current frontmatter (title/excerpt/og/tags/series) and current schema figure
when present. Restores body text from a richer git revision.
"""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ART = ROOT / "blog" / "content" / "articles"
# Last rich baseline before mass "Simplifier" body replacements for classic series
BASE = "fbb4ecc"
# For IA articles created after BASE, restore from parent of first simplify commit that touched them
IA_PARENTS = {
    "162ee3c^": "162ee3c",  # chatgpt/claude/prompts
    "f9ac900^": "f9ac900",  # remaining IA
}


def split_fm(text: str) -> tuple[str, str]:
    m = re.match(r"^(---\n.*?\n---)\n*(.*)$", text, re.S)
    if not m:
        raise ValueError("no frontmatter")
    return m.group(1), m.group(2)


def words(body: str) -> int:
    t = re.sub(r"<[^>]+>", " ", body)
    return len(re.findall(r"\w+", t, flags=re.U))


def extract_title(fm: str) -> str:
    m = re.search(r'^title:\s*"(.*)"\s*$', fm, re.M)
    return m.group(1) if m else ""


def extract_schema_figure(body: str) -> str | None:
    m = re.search(
        r'(<figure class="schema-figure">.*?</figure>)',
        body,
        re.S,
    )
    return m.group(1) if m else None


def strip_figures(body: str) -> str:
    # remove all figures (old schemas/banners) — we re-inject current schema
    body = re.sub(r"<figure\b[^>]*>.*?</figure>\s*", "", body, flags=re.S)
    # remove markdown banner images
    body = re.sub(r"!\[[^\]]*\]\([^)]*banner[^)]*\)\s*", "", body, flags=re.I)
    body = re.sub(r"!\[[^\]]*\]\([^)]*illustrations[^)]*\)\s*", "", body, flags=re.I)
    return body


def replace_h1(body: str, title: str) -> str:
    if not title:
        return body
    if re.search(r"^#\s+.+$", body, re.M):
        return re.sub(r"^#\s+.+$", f"# {title}", body, count=1, flags=re.M)
    return f"# {title}\n\n{body.lstrip()}"


def git_show(rev_path: str) -> str | None:
    try:
        return subprocess.check_output(
            ["git", "show", rev_path],
            text=True,
            encoding="utf-8",
            stderr=subprocess.DEVNULL,
            cwd=ROOT,
        )
    except subprocess.CalledProcessError:
        return None


def pick_source(slug: str, cur_words: int) -> tuple[str, str] | None:
    """Return (rev, text) of richer version if found."""
    candidates: list[tuple[str, str]] = []
    for rev in [BASE, "162ee3c^", "f9ac900^", "5bc3f4e^", "a668bf6^", "9638db2^", "3930f34^"]:
        text = git_show(f"{rev}:blog/content/articles/{slug}.md")
        if text:
            candidates.append((rev, text))
    best = None
    best_w = cur_words
    for rev, text in candidates:
        _, b = split_fm(text)
        w = words(b)
        if w > best_w + 40:
            best = (rev, text)
            best_w = w
    return best


def rebuild(cur_fm: str, cur_body: str, old_text: str) -> str:
    title = extract_title(cur_fm)
    schema = extract_schema_figure(cur_body)
    _, old_body = split_fm(old_text)
    old_body = strip_figures(old_body).strip() + "\n"
    old_body = replace_h1(old_body, title)
    if schema:
        # insert schema after H1
        if re.search(r"^#\s+.+$", old_body, re.M):
            old_body = re.sub(
                r"(^#\s+.+$)\n+",
                rf"\1\n\n{schema}\n\n",
                old_body,
                count=1,
                flags=re.M,
            )
        else:
            old_body = schema + "\n\n" + old_body
    return cur_fm + "\n\n" + old_body.lstrip()


def main() -> None:
    restored = []
    skipped = []
    for path in sorted(ART.glob("*.md")):
        slug = path.stem
        cur = path.read_text(encoding="utf-8")
        fm, body = split_fm(cur)
        cur_w = words(body)
        src = pick_source(slug, cur_w)
        if not src:
            skipped.append({"slug": slug, "words": cur_w, "reason": "no_richer"})
            continue
        rev, old = src
        new_text = rebuild(fm, body, old)
        _, new_body = split_fm(new_text)
        new_w = words(new_body)
        if new_w <= cur_w + 40:
            skipped.append({"slug": slug, "words": cur_w, "reason": "gain_too_small"})
            continue
        path.write_text(new_text, encoding="utf-8")
        restored.append({"slug": slug, "from": rev, "before": cur_w, "after": new_w})
        print(f"[OK] {slug}: {cur_w} -> {new_w} (from {rev})")

    out = {
        "restored": restored,
        "skipped_sample": skipped[:20],
        "restored_count": len(restored),
        "skipped_count": len(skipped),
    }
    (ROOT / "scripts" / "_tmp_restore_report.json").write_text(
        json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"\nrestored={len(restored)} skipped={len(skipped)}")


if __name__ == "__main__":
    main()
