"""Publie un slug vitrine vers dist/echantillons/<slug>/demo/."""
from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def rewrite(text: str) -> str:
    return re.sub(r"(?:\.\./)+(?=shared/)", "../../", text)


def publish(slug: str) -> None:
    src = ROOT / "assets" / "vitrines" / "demos" / slug
    dst = ROOT / "dist" / "echantillons" / slug / "demo"
    if not src.is_dir():
        raise SystemExit(f"source absente : {src}")
    if dst.exists():
        shutil.rmtree(dst)
    for path in src.rglob("*"):
        rel = path.relative_to(src)
        dest = dst / rel
        if path.is_dir():
            dest.mkdir(parents=True, exist_ok=True)
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        ext = path.suffix.lower()
        if ext in {".html", ".css", ".js", ".svg"}:
            try:
                txt = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                shutil.copy2(path, dest)
                continue
            txt = rewrite(txt)
            if ext == ".html":
                txt = txt.replace("/vitrines/", "/echantillons/")
            dest.write_text(txt, encoding="utf-8")
        else:
            shutil.copy2(path, dest)
    shared_src = ROOT / "assets" / "vitrines" / "demos" / "shared"
    shared_dst = ROOT / "dist" / "echantillons" / "shared"
    if shared_src.is_dir():
        if shared_dst.exists():
            shutil.rmtree(shared_dst)
        shutil.copytree(shared_src, shared_dst)
    print(f"[OK] dist/echantillons/{slug}/demo")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("usage: publish_echantillon_slug.py <slug>")
    publish(sys.argv[1])
