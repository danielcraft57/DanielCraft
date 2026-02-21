#!/usr/bin/env python3
"""
Telecharge le README de chaque depot GitHub liste dans src/data/projects.json
et les enregistre dans src/data/readmes/<slug>.md.

Usage:
    python scripts/fetch_readmes.py

Optionnel : GITHUB_TOKEN pour plus de requetes/heure (sinon 60/h).
"""
import base64
import json
import os
import sys
import time
from pathlib import Path
from typing import Optional

try:
    import urllib.request
    import urllib.error
except ImportError:
    pass

BASE_DIR = Path(__file__).parent.parent
PROJECTS_JSON = BASE_DIR / 'src' / 'data' / 'projects.json'
READMES_DIR = BASE_DIR / 'src' / 'data' / 'readmes'


def fetch_readme(owner: str, repo: str, token: Optional[str] = None) -> Optional[str]:
    """Recupere le contenu brut du README (Markdown) via l'API GitHub. Retourne None si absent ou erreur."""
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    req = urllib.request.Request(url)
    req.add_header('Accept', 'application/vnd.github.raw')
    if token:
        req.add_header('Authorization', f'Bearer {token}')
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.read().decode('utf-8', errors='replace')
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        if e.code == 403 and 'rate limit' in (e.read().decode() or '').lower():
            raise SystemExit("Rate limit GitHub depasse. Attendez 1h ou definissez GITHUB_TOKEN.")
        return None
    except Exception:
        return None


def main():
    if not PROJECTS_JSON.exists():
        print("[ERREUR] src/data/projects.json introuvable. Lancez d'abord scripts/build_projects_data.py")
        sys.exit(1)

    with open(PROJECTS_JSON, 'r', encoding='utf-8') as f:
        projects = json.load(f)

    token = os.environ.get('GITHUB_TOKEN', '').strip()
    readmes_dir = READMES_DIR
    readmes_dir.mkdir(parents=True, exist_ok=True)

    ok = 0
    skip = 0
    err = 0
    for p in projects:
        slug = p.get('slug') or p.get('id', '')
        repo = (p.get('repo') or '').strip()
        if not repo or '/' not in repo:
            skip += 1
            continue
        owner, name = repo.split('/', 1)
        path = readmes_dir / f"{slug}.md"
        if path.exists() and '--force' not in sys.argv:
            skip += 1
            continue
        try:
            content = fetch_readme(owner, name, token or None)
            if content:
                path.write_text(content, encoding='utf-8')
                ok += 1
                print(f"  [OK] {slug} <- {repo}")
            else:
                err += 1
        except SystemExit:
            raise
        except Exception as e:
            err += 1
            print(f"  [ERREUR] {slug}: {e}")
        time.sleep(0.5 if not token else 0.1)  # eviter rate limit

    print(f"\n[OK] {ok} README telecharges, {skip} deja en cache ou sans repo, {err} erreurs/absents.")
    print(f"     Fichiers dans {readmes_dir}")


if __name__ == '__main__':
    main()
