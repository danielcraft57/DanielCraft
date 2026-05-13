#!/usr/bin/env python3
"""
Captures d'écran des vitrines (Playwright), alignées sur les variables
WEBSITE_SCREENSHOT_* (voir README / .env.example).

Correction API Playwright : le viewport se définit sur le **BrowserContext**
(`browser.new_context(viewport=...)`), pas sur `new_page()`.

Prérequis :
  pip install -r showcase/requirements-screenshots.txt
  playwright install chromium
"""

from __future__ import annotations

import argparse
import http.server
import io
import os
import socketserver
import threading
import time
from pathlib import Path
from typing import Callable

PAGES = (
    ("hub", "/index.html"),
    ("technologie", "/technologie/index.html"),
    ("services", "/services/index.html"),
    ("restauration", "/restauration/index.html"),
    ("commerce", "/commerce/index.html"),
    ("education", "/education/index.html"),
    ("etablissement", "/etablissement/index.html"),
    ("beaute", "/beaute/index.html"),
    ("automobile", "/automobile/index.html"),
    ("chocolatier", "/chocolatier/index.html"),
    ("odontologie", "/odontologie/index.html"),
    ("banque", "/banque/index.html"),
    ("industrie", "/industrie/index.html"),
    ("comptable", "/comptable/index.html"),
    ("association", "/association/index.html"),
)

# Sous-chaînes d’URL à bloquer si WEBSITE_SCREENSHOT_BLOCK_TRACKERS (sans bloquer les polices)
_TRACKER_MARKERS = (
    "google-analytics.com",
    "googletagmanager.com",
    "doubleclick.net",
    "facebook.net",
    "hotjar.com",
    "clarity.ms",
    "segment.io",
    "segment.com",
    "sentry.io",
)


def _env_int(key: str, default: int) -> int:
    raw = os.environ.get(key)
    if raw is None or str(raw).strip() == "":
        return default
    try:
        return int(raw)
    except ValueError:
        return default


def _env_bool(key: str, default: bool = False) -> bool:
    raw = os.environ.get(key)
    if raw is None or str(raw).strip() == "":
        return default
    return str(raw).strip().lower() in ("1", "true", "yes", "on")


def _env_str(key: str, default: str) -> str:
    raw = os.environ.get(key)
    if raw is None or str(raw).strip() == "":
        return default
    return str(raw).strip()


def _load_config() -> dict:
    """Valeurs par défaut = copie de la config Celery / site que vous avez fournie."""
    return {
        "wait_ms": _env_int("WEBSITE_SCREENSHOT_WAIT_MS", 700),
        "goto_wait_until": _env_str("WEBSITE_SCREENSHOT_GOTO_WAIT_UNTIL", "domcontentloaded"),
        "goto_timeout_ms": _env_int("WEBSITE_SCREENSHOT_GOTO_TIMEOUT_MS", 28000),
        "webp_quality": _env_int("WEBSITE_SCREENSHOT_WEBP_QUALITY", 78),
        "jpeg_quality": _env_int("WEBSITE_SCREENSHOT_JPEG_QUALITY", 82),
        "device_scale_factor": _env_int("WEBSITE_SCREENSHOT_DEVICE_SCALE_FACTOR", 1),
        "block_trackers": _env_bool("WEBSITE_SCREENSHOT_BLOCK_TRACKERS", True),
        "reduced_motion": _env_bool("WEBSITE_SCREENSHOT_REDUCED_MOTION", True),
        "disable_animations": _env_bool("WEBSITE_SCREENSHOT_DISABLE_ANIMATIONS", True),
        "capture_format": _env_str("WEBSITE_SCREENSHOT_CAPTURE_FORMAT", "jpeg").lower(),
        "viewports": (
            (
                "desktop",
                _env_int("WEBSITE_SCREENSHOT_VIEWPORT_DESKTOP_WIDTH", 1920),
                _env_int("WEBSITE_SCREENSHOT_VIEWPORT_DESKTOP_HEIGHT", 2400),
                _env_int("WEBSITE_SCREENSHOT_MAX_WIDTH_DESKTOP", 1600),
            ),
            (
                "tablet",
                _env_int("WEBSITE_SCREENSHOT_VIEWPORT_TABLET_WIDTH", 1024),
                _env_int("WEBSITE_SCREENSHOT_VIEWPORT_TABLET_HEIGHT", 2500),
                _env_int("WEBSITE_SCREENSHOT_MAX_WIDTH_TABLET", 1200),
            ),
            (
                "mobile",
                _env_int("WEBSITE_SCREENSHOT_VIEWPORT_MOBILE_WIDTH", 430),
                _env_int("WEBSITE_SCREENSHOT_VIEWPORT_MOBILE_HEIGHT", 2500),
                _env_int("WEBSITE_SCREENSHOT_MAX_WIDTH_MOBILE", 800),
            ),
        ),
    }


def _pick_port(preferred: int) -> int:
    if preferred > 0:
        return preferred
    with socketserver.TCPServer(("127.0.0.1", 0), http.server.SimpleHTTPRequestHandler) as s:
        return s.server_address[1]


def _make_tracker_route() -> Callable:
    def _route(route) -> None:
        url = route.request.url
        low = url.lower()
        if any(m in low for m in _TRACKER_MARKERS):
            route.abort()
            return
        route.continue_()

    return _route


def _disable_animations_init() -> str:
    return """
(() => {
  const s = document.createElement('style');
  s.setAttribute('data-screenshot-disable-animations', '1');
  s.textContent = '*,' +
    '*::before,' +
    '*::after{' +
    'animation-duration:0s!important;' +
    'animation-delay:0s!important;' +
    'transition-duration:0s!important;' +
    'scroll-behavior:auto!important;' +
    '}';
  document.documentElement.appendChild(s);
})();
"""


def _save_output(
    png_bytes: bytes,
    dest: Path,
    *,
    capture_format: str,
    max_width: int,
    jpeg_quality: int,
    webp_quality: int,
) -> None:
    try:
        from PIL import Image
    except ImportError as e:
        raise RuntimeError(
            "Pillow est requis pour le redimensionnement (MAX_WIDTH) et le format WebP. "
            "Installez : pip install Pillow"
        ) from e

    im = Image.open(io.BytesIO(png_bytes)).convert("RGB")
    if max_width > 0 and im.width > max_width:
        ratio = max_width / im.width
        new_h = max(1, int(im.height * ratio))
        im = im.resize((max_width, new_h), Image.Resampling.LANCZOS)

    dest.parent.mkdir(parents=True, exist_ok=True)
    if capture_format == "webp":
        im.save(dest, "WEBP", quality=webp_quality, method=6)
    else:
        im.save(dest, "JPEG", quality=jpeg_quality, optimize=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Screenshots showcases (Playwright + env WEBSITE_SCREENSHOT_*).")
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

    cfg = _load_config()

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

    ext = ".webp" if cfg["capture_format"] == "webp" else ".jpg"

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=not args.headed)
            for slug, path in PAGES:
                url = f"{base}{path}"
                for label, vw, vh, max_w in cfg["viewports"]:
                    ctx_kwargs: dict = {
                        "viewport": {"width": vw, "height": vh},
                        "device_scale_factor": cfg["device_scale_factor"],
                    }
                    if cfg["reduced_motion"]:
                        ctx_kwargs["reduced_motion"] = "reduce"

                    context = browser.new_context(**ctx_kwargs)

                    if cfg["block_trackers"]:
                        context.route("**/*", _make_tracker_route())

                    if cfg["disable_animations"]:
                        context.add_init_script(_disable_animations_init())

                    page = context.new_page()
                    page.goto(
                        url,
                        wait_until=cfg["goto_wait_until"],
                        timeout=cfg["goto_timeout_ms"],
                    )
                    page.wait_for_timeout(cfg["wait_ms"])

                    png_bytes = page.screenshot(full_page=True, type="png")

                    dest = out_root / slug
                    fname = f"{label}_{vw}x{vh}{ext}"
                    out_path = dest / fname

                    _save_output(
                        png_bytes,
                        out_path,
                        capture_format=cfg["capture_format"],
                        max_width=max_w,
                        jpeg_quality=cfg["jpeg_quality"],
                        webp_quality=cfg["webp_quality"],
                    )

                    page.close()
                    context.close()
                    print(f"OK {slug} {label} -> {out_path}")
            browser.close()
    finally:
        httpd.shutdown()
        httpd.server_close()

    print(f"\nTerminé. Sortie : {out_root}")


if __name__ == "__main__":
    main()
