#!/usr/bin/env python3
"""
Captures d'écran des vitrines (Playwright), alignées sur les variables
WEBSITE_SCREENSHOT_* (voir README / .env.example).

Usage :
  # Serveur intégré (assets/vitrines/demos) :
  python scripts/screenshot_vitrines.py

  # Site buildé (serve_dev sur :8000) :
  python scripts/screenshot_vitrines.py --base-url http://127.0.0.1:8000/vitrines
"""
from __future__ import annotations

import argparse
import http.server
import io
import json
import os
import shutil
import socketserver
import sys
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Callable, List, Tuple

_REPO = Path(__file__).resolve().parent.parent
_VITRINES_JSON = _REPO / "src" / "data" / "vitrines.json"


def _load_pages_from_catalog() -> Tuple[Tuple[str, str], ...]:
    """(slug, path) depuis vitrines.json + catalogue hub."""
    pages: List[Tuple[str, str]] = [("hub", "/index.html")]
    if _VITRINES_JSON.is_file():
        data = json.loads(_VITRINES_JSON.read_text(encoding="utf-8"))
        for it in data.get("items") or []:
            slug = (it.get("slug") or "").strip()
            if slug:
                pages.append((slug, f"/{slug}/demo/index.html"))
    return tuple(pages)


PAGES = _load_pages_from_catalog()

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


def _env_float(key: str, default: float) -> float:
    raw = os.environ.get(key)
    if raw is None or str(raw).strip() == "":
        return default
    try:
        return float(raw)
    except ValueError:
        return default


def _load_config() -> dict:
    """Valeurs par défaut = copie de la config Celery / site que vous avez fournie."""
    return {
        "wait_ms": _env_int("WEBSITE_SCREENSHOT_WAIT_MS", 700),
        "goto_wait_until": _env_str("WEBSITE_SCREENSHOT_GOTO_WAIT_UNTIL", "domcontentloaded"),
        "goto_timeout_ms": _env_int("WEBSITE_SCREENSHOT_GOTO_TIMEOUT_MS", 28000),
        "webp_quality": _env_int("WEBSITE_SCREENSHOT_WEBP_QUALITY", 72),
        "jpeg_quality": _env_int("WEBSITE_SCREENSHOT_JPEG_QUALITY", 80),
        "device_scale_factor": _env_int("WEBSITE_SCREENSHOT_DEVICE_SCALE_FACTOR", 1),
        "block_trackers": _env_bool("WEBSITE_SCREENSHOT_BLOCK_TRACKERS", True),
        "reduced_motion": _env_bool("WEBSITE_SCREENSHOT_REDUCED_MOTION", True),
        "disable_animations": _env_bool("WEBSITE_SCREENSHOT_DISABLE_ANIMATIONS", True),
        "capture_format": _env_str("WEBSITE_SCREENSHOT_CAPTURE_FORMAT", "webp").lower(),
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
        "brand_enabled": _env_bool("WEBSITE_SCREENSHOT_BRAND_ENABLED", True),
        "brand_pad": _env_int("WEBSITE_SCREENSHOT_BRAND_PAD", 28),
        "brand_bg_rgb": (
            _env_int("WEBSITE_SCREENSHOT_BRAND_BG_R", 238),
            _env_int("WEBSITE_SCREENSHOT_BRAND_BG_G", 243),
            _env_int("WEBSITE_SCREENSHOT_BRAND_BG_B", 248),
        ),
        "brand_blue_mix": _env_float("WEBSITE_SCREENSHOT_BRAND_BLUE_MIX", 0.09),
        "brand_border_width": _env_int("WEBSITE_SCREENSHOT_BRAND_BORDER_WIDTH", 2),
        "brand_border_rgb": (
            _env_int("WEBSITE_SCREENSHOT_BRAND_BORDER_R", 47),
            _env_int("WEBSITE_SCREENSHOT_BRAND_BORDER_G", 120),
            _env_int("WEBSITE_SCREENSHOT_BRAND_BORDER_B", 166),
        ),
    }


def _pick_port(preferred: int) -> int:
    if preferred > 0:
        return preferred
    with socketserver.TCPServer(("127.0.0.1", 0), http.server.SimpleHTTPRequestHandler) as s:
        return s.server_address[1]


def _pre_capture_scroll(page, step_px: int = 280, pause_ms: int = 60) -> None:
    """Parcourt la page du haut vers le bas puis revient en haut (lazy-load, état final = haut)."""
    try:
        page.evaluate(
            """([step, pause]) => {
              const delay = (ms) => new Promise((r) => setTimeout(r, ms));
              const doc = document.scrollingElement || document.documentElement;
              const h = doc.scrollHeight;
              return (async () => {
                for (let y = 0; y < h; y += step) {
                  doc.scrollTop = y;
                  await delay(pause);
                }
                doc.scrollTop = Math.max(0, h - window.innerHeight);
                await delay(100);
                doc.scrollTop = 0;
                await delay(80);
              })();
            }""",
            [step_px, pause_ms],
        )
    except Exception:
        pass


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


def _apply_showcase_brand(im, cfg: dict):
    """Marge type carte portfolio + léger voile bleu DanielCraft + bord."""
    if not cfg.get("brand_enabled"):
        return im
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        return im

    pad = max(0, int(cfg.get("brand_pad") or 0))
    bg = cfg.get("brand_bg_rgb") or (238, 243, 248)
    mix = float(cfg.get("brand_blue_mix") or 0.0)
    border_w = max(0, int(cfg.get("brand_border_width") or 0))
    border_rgb = cfg.get("brand_border_rgb") or (47, 120, 166)

    if pad > 0:
        canvas = Image.new("RGB", (im.width + pad * 2, im.height + pad * 2), bg)
        canvas.paste(im, (pad, pad))
        im = canvas

    if mix > 0:
        im_rgba = im.convert("RGBA")
        alpha = int(max(0.0, min(mix, 0.45)) * 255)
        tint = Image.new("RGBA", im_rgba.size, (47, 120, 166, alpha))
        im = Image.alpha_composite(im_rgba, tint).convert("RGB")

    if border_w > 0:
        draw = ImageDraw.Draw(im)
        w, h = im.size
        for i in range(border_w):
            draw.rectangle([i, i, w - 1 - i, h - 1 - i], outline=border_rgb)
    return im


def _save_output(
    png_bytes: bytes,
    dest: Path,
    *,
    capture_format: str,
    max_width: int,
    jpeg_quality: int,
    webp_quality: int,
    brand_cfg: dict | None = None,
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

    if brand_cfg is not None:
        im = _apply_showcase_brand(im, brand_cfg)

    dest.parent.mkdir(parents=True, exist_ok=True)
    if capture_format == "webp":
        im.save(dest, "WEBP", quality=webp_quality, method=6)
    else:
        im.save(dest, "JPEG", quality=jpeg_quality, optimize=True)


def _demo_path_for_mode(path: str, *, embedded_demos: bool) -> str:
    if embedded_demos and path.endswith("/demo/index.html"):
        return path.replace("/demo/index.html", "/index.html")
    return path


def _wait_for_base(base: str, timeout_s: float = 60.0) -> None:
    url = base.rstrip("/") + "/index.html"
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=3) as resp:
                if resp.status < 500:
                    return
        except (urllib.error.URLError, TimeoutError, OSError):
            time.sleep(0.5)
    raise RuntimeError(f"Serveur inaccessible : {base} (timeout {timeout_s}s)")


def main() -> None:
    parser = argparse.ArgumentParser(description="Screenshots vitrines (Playwright + env WEBSITE_SCREENSHOT_*).")
    parser.add_argument("--host", default="127.0.0.1", help="Hôte du serveur statique intégré")
    parser.add_argument("--port", type=int, default=0, help="Port serveur intégré (0 = automatique)")
    parser.add_argument(
        "--base-url",
        default="",
        help="URL de base dist (ex. http://127.0.0.1:8000/vitrines) — pas de serveur intégré",
    )
    parser.add_argument(
        "--demos-dir",
        type=Path,
        default=None,
        help="Dossier assets/vitrines/demos (défaut : à la racine du repo).",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Dossier de sortie (défaut : assets/vitrines/screenshots).",
    )
    parser.add_argument("--headed", action="store_true", help="Afficher le navigateur (debug).")
    parser.add_argument(
        "--slugs",
        default="",
        help="Slugs à capturer (virgules). Défaut : tout le catalogue.",
    )
    parser.add_argument(
        "--install-dist",
        action="store_true",
        help="Copier screenshots + démos vers dist/vitrines/ après capture.",
    )
    args = parser.parse_args()

    cfg = _load_config()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print(
            "Playwright manquant. Installez :\n"
            "  pip install -r scripts/requirements-vitrines-screenshots.txt\n"
            "  playwright install chromium"
        )
        raise SystemExit(1) from None

    _repo = Path(__file__).resolve().parent.parent
    _default_demos = _repo / "assets" / "vitrines" / "demos"
    _default_out = _repo / "assets" / "vitrines" / "screenshots"
    demos_root = (args.demos_dir or _default_demos).resolve()
    out_root = (args.out or _default_out).resolve()
    out_root.mkdir(parents=True, exist_ok=True)

    pages = _load_pages_from_catalog()
    if (args.slugs or "").strip():
        wanted = {s.strip() for s in args.slugs.split(",") if s.strip()}
        pages = tuple(p for p in pages if p[0] in wanted)
        if not pages:
            raise SystemExit(f"Aucun slug trouvé dans le catalogue : {', '.join(sorted(wanted))}")
    use_external = bool((args.base_url or "").strip())
    httpd = None
    thread = None

    if use_external:
        base = args.base_url.strip().rstrip("/")
        print(f"Mode dist — base : {base}")
        _wait_for_base(base)
        embedded = False
    else:
        port = _pick_port(args.port)
        root = str(demos_root)
        socketserver.TCPServer.allow_reuse_address = True

        class ShowcaseHandler(http.server.SimpleHTTPRequestHandler):
            def __init__(self, *handler_args, **handler_kwargs):
                super().__init__(*handler_args, directory=root, **handler_kwargs)

        httpd = socketserver.TCPServer((args.host, port), ShowcaseHandler)
        thread = threading.Thread(target=httpd.serve_forever, daemon=True)
        thread.start()
        base = f"http://{args.host}:{port}"
        embedded = True
        time.sleep(0.2)
        print(f"Mode demos — {base}")

    ext = ".webp" if cfg["capture_format"] == "webp" else ".jpg"

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=not args.headed)
            for slug, path in pages:
                rel = _demo_path_for_mode(path, embedded_demos=embedded)
                url = f"{base}{rel}"
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
                    _pre_capture_scroll(page)

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
                        brand_cfg=cfg,
                    )

                    page.close()
                    context.close()
                    print(f"OK {slug} {label} -> {out_path}")
            browser.close()
    finally:
        if httpd is not None:
            httpd.shutdown()
            httpd.server_close()

    print(f"\nTerminé. Sortie : {out_root}")
    if args.install_dist:
        _install_to_dist(pages, out_root, demos_root)


def _install_to_dist(pages: tuple[tuple[str, str], ...], shots_root: Path, demos_root: Path) -> None:
    """Copie screenshots + démos BS5 vers dist/vitrines/ puis régénère le catalogue."""
    repo = Path(__file__).resolve().parents[1]
    dist_root = repo / "dist" / "vitrines"
    slugs = sorted({slug for slug, _ in pages if slug != "hub"})
    for slug in slugs:
        src_shots = shots_root / slug
        dst_shots = dist_root / slug / "screenshots"
        if src_shots.is_dir():
            if dst_shots.exists():
                shutil.rmtree(dst_shots)
            shutil.copytree(src_shots, dst_shots)
            print(f"[dist] screenshots/{slug}")
        src_demo = demos_root / slug
        dst_demo = dist_root / slug / "demo"
        if src_demo.is_dir():
            if dst_demo.exists():
                shutil.rmtree(dst_demo)
            shutil.copytree(src_demo, dst_demo)
            print(f"[dist] demo/{slug}")
    print(f"[OK] dist/vitrines/ synchronisé ({len(slugs)} slugs)")
    try:
        sys.path.insert(0, str(repo))
        from build import OUTPUT_DIR, build_vitrines_catalog_embed, publish_vitrines_to_dist

        OUTPUT_DIR = repo / "dist"
        publish_vitrines_to_dist(OUTPUT_DIR)
        build_vitrines_catalog_embed()
        print("[OK] Catalogue vitrines régénéré (build.py)")
    except Exception as err:
        print(f"[WARN] Catalogue non régénéré : {err}")
        print("       Lancez : python build.py --no-webp")


if __name__ == "__main__":
    main()
