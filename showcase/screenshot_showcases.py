#!/usr/bin/env python3
"""
Captures d'écran des vitrines à plusieurs viewports (desktop, tablette, mobile).

Prérequis :
  pip install -r showcase/requirements-screenshots.txt
  playwright install chromium

Lance un serveur HTTP local sur le dossier showcase/, puis ouvre Chromium en tête
non visible et enregistre des PNG pleine page par page et par format.
"""

from __future__ import annotations

import argparse
import http.server
import socketserver
import threading
import time
from pathlib import Path

VIEWPORTS = (
    ("desktop", 1440, 900),
    ("tablet", 834, 1112),
    ("mobile", 390, 844),
)

PAGES = (
    ("hub", "/index.html"),
    ("chocolatier", "/chocolatier/index.html"),
    ("odontologie", "/odontologie/index.html"),
    ("banque", "/banque/index.html"),
    ("industrie", "/industrie/index.html"),
    ("comptable", "/comptable/index.html"),
    ("association", "/association/index.html"),
)


def _pick_port(preferred: int) -> int:
    if preferred > 0:
        return preferred
    with socketserver.TCPServer(("127.0.0.1", 0), http.server.SimpleHTTPRequestHandler) as s:
        return s.server_address[1]


def main() -> None:
    parser = argparse.ArgumentParser(description="Screenshots showcases multi-viewports.")
    parser.add_argument("--host", default="127.0.0.1", help="Hôte du serveur statique")
    parser.add_argument("--port", type=int, default=0, help="Port (0 = automatique)")
    parser.add_argument(
        "--showcase-dir",
        type=Path,
        default=None,
        help="Dossier showcase/ à servir (défaut : parent de ce script).",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Dossier de sortie (défaut : showcase/screenshots).",
    )
    parser.add_argument("--headed", action="store_true", help="Afficher le navigateur (debug).")
    args = parser.parse_args()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print(
            "Playwright manquant. Installez :\n"
            "  pip install -r showcase/requirements-screenshots.txt\n"
            "  playwright install chromium"
        )
        raise SystemExit(1) from None

    showcase_root = (args.showcase_dir or Path(__file__).resolve().parent).resolve()
    out_root = (args.out or (showcase_root / "screenshots")).resolve()
    out_root.mkdir(parents=True, exist_ok=True)

    port = _pick_port(args.port)
    root = str(showcase_root)

    socketserver.TCPServer.allow_reuse_address = True

    class ShowcaseHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *handler_args, **handler_kwargs):
            super().__init__(*handler_args, directory=root, **handler_kwargs)

    httpd = socketserver.TCPServer((args.host, port), ShowcaseHandler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    base = f"http://{args.host}:{port}"

    time.sleep(0.2)

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=not args.headed)
            context = browser.new_context(device_scale_factor=1)
            for slug, path in PAGES:
                url = f"{base}{path}"
                for label, width, height in VIEWPORTS:
                    page = context.new_page(viewport={"width": width, "height": height})
                    page.goto(url, wait_until="domcontentloaded", timeout=90_000)
                    page.wait_for_timeout(800)
                    dest = out_root / slug
                    dest.mkdir(parents=True, exist_ok=True)
                    fname = f"{label}_{width}x{height}.png"
                    page.screenshot(path=dest / fname, full_page=True)
                    page.close()
                    print(f"OK {slug} {label} -> {dest / fname}")
            browser.close()
    finally:
        httpd.shutdown()
        httpd.server_close()

    print(f"\nTerminé. Sortie : {out_root}")


if __name__ == "__main__":
    main()
