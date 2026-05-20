#!/usr/bin/env python3
"""
Serveur HTTP local pour dist/ avec URLs blog sans extension.

Résout /blog/articles/mon-slug -> dist/blog/articles/mon-slug.html
"""

from __future__ import annotations

import argparse
import http.server
import os
from pathlib import Path
from urllib.parse import unquote, urlparse


EXTENSIONLESS_PREFIXES = (
    "/blog/articles/",
    "/blog/series/",
    "/blog/types/",
)


class BlogFriendlyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Ajoute .html pour les chemins blog connus si le fichier existe."""

    def __init__(self, *args, directory: str | None = None, **kwargs):
        super().__init__(*args, directory=directory, **kwargs)

    def _resolve_path(self, raw_path: str) -> str:
        path = unquote(urlparse(raw_path).path)
        query = ("?" + raw_path.split("?", 1)[1]) if "?" in raw_path else ""

        if path in ("/blog", "/blog/"):
            return "/blog/index.html" + query

        if path.endswith("/") and path.startswith("/blog/"):
            index = path.rstrip("/") + "/index.html"
            local = Path(self.directory) / index.lstrip("/").replace("/", os.sep)
            if local.is_file():
                return index + query

        _, ext = os.path.splitext(path)
        if not ext:
            if any(path.startswith(p) for p in EXTENSIONLESS_PREFIXES):
                candidate = path + ".html"
                local = Path(self.directory) / candidate.lstrip("/").replace("/", os.sep)
                if local.is_file():
                    return candidate + query
            # Pages statiques à la racine : /audit -> audit.html, /analyse -> analyse.html, etc.
            if path not in ("", "/"):
                candidate = path.rstrip("/") + ".html"
                local = Path(self.directory) / candidate.lstrip("/").replace("/", os.sep)
                if local.is_file():
                    return candidate + query

        return raw_path

    def do_GET(self) -> None:
        self.path = self._resolve_path(self.path)
        return super().do_GET()


def main() -> None:
    parser = argparse.ArgumentParser(description="Serveur local DanielCraft (blog URLs propres)")
    parser.add_argument("port", nargs="?", type=int, default=8000)
    parser.add_argument(
        "--directory",
        default="dist",
        help="Racine HTTP (défaut: dist)",
    )
    args = parser.parse_args()
    root = Path(args.directory).resolve()
    if not root.is_dir():
        raise SystemExit(f"Dossier introuvable: {root}")

    handler = lambda *h_args, **h_kwargs: BlogFriendlyHTTPRequestHandler(  # noqa: E731
        *h_args, directory=str(root), **h_kwargs
    )
    server_class = getattr(http.server, "ThreadingHTTPServer", http.server.HTTPServer)
    with server_class(("", args.port), handler) as httpd:
        print(f"Serving HTTP on port {args.port} (blog sans .html OK) — {root}")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
