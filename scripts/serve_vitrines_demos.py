#!/usr/bin/env python3
"""
Serveur HTTP local pour assets/vitrines/demos/ (hub + secteurs).

Usage (à la racine du repo) :
  python scripts/serve_vitrines_demos.py
  python scripts/serve_vitrines_demos.py --port 9000 --no-browser
"""

from __future__ import annotations

import argparse
import threading
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Sert assets/vitrines/demos et ouvre le navigateur.")
    parser.add_argument("--host", default="127.0.0.1", help="Adresse d'écoute (défaut: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8765, help="Port TCP (défaut: 8765)")
    parser.add_argument(
        "--no-browser",
        action="store_true",
        help="Ne pas ouvrir le navigateur automatiquement.",
    )
    parser.add_argument(
        "--path",
        type=Path,
        default=None,
        help="Répertoire à servir (défaut: assets/vitrines/demos).",
    )
    args = parser.parse_args()

    repo = Path(__file__).resolve().parent.parent
    root: Path = (args.path or (repo / "assets" / "vitrines" / "demos")).resolve()

    class VitrinesDemosHandler(SimpleHTTPRequestHandler):
        def __init__(self, *handler_args, **handler_kwargs):
            super().__init__(*handler_args, directory=str(root), **handler_kwargs)

        def log_message(self, fmt: str, *log_args) -> None:
            super().log_message(fmt, *log_args)

    url = f"http://{args.host}:{args.port}/"

    server = ThreadingHTTPServer((args.host, args.port), VitrinesDemosHandler)

    if not args.no_browser:

        def _open() -> None:
            webbrowser.open(url)

        threading.Timer(0.35, _open).start()

    print(f"Vitrines démos : {root}")
    print(f"URL           : {url}")
    print("Ctrl+C pour arrêter.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nArrêt.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
