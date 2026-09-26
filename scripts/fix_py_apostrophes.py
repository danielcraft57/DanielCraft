# -*- coding: utf-8 -*-
"""Repare les chaines Python cassees par le remplacement ' courbe -> droite.

Strategie : pour chaque fichier .py, tenter py_compile ; si echec, convertir
les litteraux problematiques (apostrophe dans une chaine simple quotes) en
chaines double quotes quand c'est sur une seule ligne.
"""
from __future__ import annotations

import py_compile
import re
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Lignes du type: ...('...d'indexation...')  ->  ...("...d'indexation...")
SINGLE_LINE_STR = re.compile(
    r"(?P<prefix>^[^#'\"]*)(?P<q>')(?P<body>(?:\\'|[^'])*)(?P=q)(?P<suffix>.*)$"
)


def try_compile(path: Path) -> str | None:
    """Compile le fichier ; retourne le message d'erreur ou None."""
    try:
        py_compile.compile(str(path), doraise=True)
        return None
    except py_compile.PyCompileError as exc:
        return str(exc)


def fix_file(path: Path) -> int:
    """Tente de reparer un fichier Python casse par des apostrophes.

    @returns: nombre de lignes modifiees
    """
    err = try_compile(path)
    if not err:
        return 0

    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    changed = 0
    # Plusieurs passes : a chaque passe on convertit les '...' contenant ' en "..."
    for _ in range(20):
        err = try_compile(path)
        if not err:
            break
        # Extraire le numero de ligne si possible
        m = re.search(r"line (\d+)", err)
        if not m:
            print(f"[FAIL] {path}: {err}")
            break
        lineno = int(m.group(1)) - 1
        if lineno < 0 or lineno >= len(lines):
            print(f"[FAIL] bad line {path}: {err}")
            break
        line = lines[lineno]
        # Remplace le premier litteral '...' qui contient une apostrophe non echappee
        new_line = re.sub(
            r"'((?:\\'|[^'\\]|\\.)*?'(?:\\'|[^'\\]|\\.)*)'",
            lambda mo: '"' + mo.group(1).replace('\\"', '"').replace("\\'", "'") + '"',
            line,
            count=1,
        )
        # Approche plus simple : si la ligne a des ' imbriqués, passer toute la
        # chaine append/commentaire en double quotes pour les appels connus
        if new_line == line:
            # Heuristique : premiere ' -> ", derniere ' avant ) ou fin -> "
            # Trouver paires de quotes simples autour d'un contenu avec apostrophe
            def flip(match: re.Match[str]) -> str:
                body = match.group(1)
                if "'" in body.replace("\\'", ""):
                    return '"' + body + '"'
                return match.group(0)

            new_line = re.sub(r"'([^'\\]*(?:\\.[^'\\]*)*)'", flip, line)

        if new_line == line:
            # Dernier recours : echapper les apostrophes internes apres la premiere
            parts = line.split("'")
            if len(parts) >= 4:
                # reconstruct: before ' first ' middle with escaped ' last ' after
                # Too fragile - print and skip
                print(f"[MANUAL] {path.relative_to(ROOT)}:{lineno + 1}: {line.rstrip()}")
                break
        lines[lineno] = new_line
        path.write_text("".join(lines), encoding="utf-8", newline="\n")
        changed += 1
        # Recharger apres ecriture
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)

    err = try_compile(path)
    if err:
        print(f"[STILL BROKEN] {path.relative_to(ROOT)}: {err}")
    else:
        print(f"[OK] {path.relative_to(ROOT)} ({changed} fix(es))")
    return changed


def main() -> None:
    """Repare build.py et les scripts Python du depot."""
    targets = [ROOT / "build.py"]
    targets.extend(sorted((ROOT / "scripts").rglob("*.py")))
    for path in targets:
        if not path.is_file():
            continue
        if path.name.startswith("fix_"):
            continue
        err = try_compile(path)
        if err:
            print(f"repairing {path.relative_to(ROOT)}")
            fix_file(path)


if __name__ == "__main__":
    main()
