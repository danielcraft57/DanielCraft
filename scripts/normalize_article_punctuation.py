#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
m = json.loads((ROOT / "scripts" / "_blog_og_series3_manifest.json").read_text(encoding="utf-8"))
fixed = 0
for it in m:
    p = ROOT / "blog" / "content" / "articles" / f"{it['slug']}.md"
    t = p.read_text(encoding="utf-8")
    n = (
        t.replace("\u2019", "'")
        .replace("\u2018", "'")
        .replace("\u201c", '"')
        .replace("\u201d", '"')
        .replace("\u2014", "-")
        .replace("\u2013", "-")
    )
    if n != t:
        p.write_text(n, encoding="utf-8")
        fixed += 1
print(f"normalized {fixed} files")
bad = 0
for it in m:
    t = (ROOT / "blog" / "content" / "articles" / f"{it['slug']}.md").read_text(encoding="utf-8")
    if any(c in t for c in "\u2019\u2018\u2014\u2013"):
        bad += 1
        print("still bad", it["slug"])
print("remaining_bad", bad)
print("schemas", len(list((ROOT / "assets" / "images" / "blog" / "schemas").glob("*.svg"))))
