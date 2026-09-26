# -*- coding: utf-8 -*-
"""Remplace tirets cadratins / demi-cadratins (regles .cursorrules).

Les apostrophes courbees ne sont remplacees QUE hors fichiers Python :
en .py, une apostrophe droite casse souvent les litteraux '...' .
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROOTS = [
    ROOT / "src",
    ROOT / "assets",
    ROOT / "docs",
    ROOT / "blog",
    ROOT / "api",
    ROOT / "scripts",
    ROOT / "showcase",
    ROOT / "livres-formation",
]

EXTS = {".html", ".json", ".js", ".css", ".md", ".php", ".py", ".txt"}
SKIP_DIRS = {
    "node_modules",
    "dist",
    ".git",
    "__pycache__",
    ".cursor",
    "venv",
    ".venv",
}
SKIP_NAMES = {"package-lock.json"}

DASH_REPL = {
    "\u2014": "-",
    "\u2013": "-",
}
QUOTE_REPL = {
    "\u2019": "'",
    "\u2018": "'",
    "\u201c": '"',
    "\u201d": '"',
}


def should_skip(path: Path) -> bool:
    """Indique si le fichier doit etre ignore."""
    if any(part in SKIP_DIRS for part in path.parts):
        return True
    if path.name in SKIP_NAMES:
        return True
    if path.suffix.lower() not in EXTS:
        return True
    return False


def fix_text(text: str, *, include_quotes: bool) -> tuple[str, int]:
    """Applique les remplacements de ponctuation.

    @param text: Contenu source.
    @param include_quotes: Si True, remplace aussi apostrophes/guillemets courbes.
    @returns: (texte corrige, nombre de remplacements)
    """
    count = 0
    out = text
    mapping = dict(DASH_REPL)
    if include_quotes:
        mapping.update(QUOTE_REPL)
    for src, dst in mapping.items():
        n = out.count(src)
        if n:
            count += n
            out = out.replace(src, dst)
    return out, count


def iter_files():
    """Parcourt les fichiers cibles du depot."""
    for base in ROOTS:
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if path.is_file() and not should_skip(path):
                yield path
    for path in ROOT.iterdir():
        if path.is_file() and path.suffix.lower() in {".md", ".py", ".html", ".json", ".txt"}:
            if path.name not in SKIP_NAMES:
                yield path


def main() -> None:
    """Corrige la ponctuation dans tout le depot pertinent."""
    changed = []
    scanned = 0
    for path in iter_files():
        scanned += 1
        try:
            original = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        include_quotes = path.suffix.lower() != ".py"
        fixed, n = fix_text(original, include_quotes=include_quotes)
        if n:
            try:
                path.write_text(fixed, encoding="utf-8", newline="\n")
            except OSError as exc:
                print(f"[SKIP] {path.relative_to(ROOT).as_posix()}: {exc}")
                continue
            changed.append((path.relative_to(ROOT).as_posix(), n))

    print(f"scanned={scanned}")
    print(f"changed_files={len(changed)}")
    print(f"total_replacements={sum(n for _, n in changed)}")
    for rel, n in sorted(changed, key=lambda x: -x[1])[:40]:
        print(f"{n:5} {rel}")


if __name__ == "__main__":
    main()
