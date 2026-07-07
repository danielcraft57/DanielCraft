#!/usr/bin/env python3
"""Génère visuels sectoriels (PIL) + icônes pour vitrines multi-pages."""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import random
import shutil
import sys
import time
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
from vitrine_scenarios import image_specs

ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = ROOT / "src" / "data" / "vitrines.json"
DEMOS = ROOT / "assets" / "vitrines" / "demos"
ORPHAN_SLUGS = frozenset({"banque", "chocolatier"})

PALETTES = {
    "saas": [(99, 102, 241), (15, 23, 42)],
    "tech": [(56, 189, 248), (13, 27, 42)],
    "hcr": [(183, 28, 28), (62, 39, 35)],
    "beaute": [(236, 72, 153), (253, 242, 248)],
    "sante": [(14, 165, 233), (224, 242, 254)],
    "industrie": [(255, 179, 0), (10, 22, 40)],
    "ess": [(34, 197, 94), (20, 83, 45)],
    "retail": [(27, 94, 32), (232, 245, 233)],
    "conseil": [(13, 71, 161), (227, 242, 253)],
    "formation": [(37, 99, 235), (239, 246, 255)],
    "services": [(15, 118, 110), (204, 251, 241)],
    "hotel": [(120, 81, 45), (255, 248, 225)],
    "mobilite": [(198, 40, 40), (26, 26, 26)],
    "immobilier": [(26, 60, 52), (212, 232, 223)],
    "juridique": [(201, 162, 39), (15, 23, 42)],
    "architecture": [(17, 17, 17), (245, 245, 245)],
    "sport": [(101, 163, 13), (20, 83, 45)],
    "creatif": [(55, 71, 79), (236, 239, 241)],
}

ICON_PATHS = {
    "saas": "M12 20h40v28H12z M20 12h24v8H20z",
    "tech": "M16 16h32v32H16z M24 24h16v16H24z",
    "hcr": "M32 8v48 M8 32h48",
    "beaute": "M32 8c-8 12-12 20-12 28a12 12 0 1024 0c0-8-4-16-12-28z",
    "sante": "M32 10v44 M18 24h28",
    "industrie": "M8 48h48 M14 48V28l10-8 8 6 12-10v32",
    "ess": "M32 12l6 12h14l-11 8 4 14-13-9-13 9 4-14-11-8h14z",
    "retail": "M12 24l4-12h32l4 12v24H12z",
    "conseil": "M16 44V20l16-10 16 10v24",
    "formation": "M10 22l22-12 22 12-22 12z",
    "services": "M32 8l20 12v24L32 56 12 44V20z",
    "hotel": "M8 44h48V28L32 16 8 28z",
    "mobilite": "M12 40h40l-4-16H16z M18 40a6 6 0 1112 0",
    "immobilier": "M32 10L8 32h8v22h32V32h8z",
    "juridique": "M32 8l-4 16h-12l10 8-4 16 10-12 10 12-4-16 10-8H36z",
    "architecture": "M8 48h48 M12 48V32l20-16 20 16v16",
    "sport": "M32 10a14 14 0 110 28 14 14 0 010-28z",
    "creatif": "M12 48l8-32h24l8 32z",
}


def _font(size: int):
    for name in ("arial.ttf", "segoeui.ttf", "calibri.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def _seed(slug: str, suffix: str) -> int:
    return int(hashlib.md5(f"{slug}:{suffix}".encode()).hexdigest()[:8], 16)


def _save_png(img: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    data = buf.getvalue()
    tmp = path.with_name(f".{path.stem}.tmp.png")
    last_err: OSError | None = None
    for attempt in range(6):
        try:
            tmp.write_bytes(data)
            os.replace(tmp, path)
            return
        except OSError as err:
            last_err = err
            time.sleep(0.15 * (attempt + 1))
        finally:
            if tmp.exists():
                try:
                    tmp.unlink()
                except OSError:
                    pass
    if last_err:
        raise last_err


def _gradient(w: int, h: int, c1: tuple, c2: tuple) -> Image.Image:
    img = Image.new("RGB", (w, h))
    draw = ImageDraw.Draw(img)
    for y in range(h):
        t = y / max(h - 1, 1)
        r = int(c1[0] + (c2[0] - c1[0]) * t)
        g = int(c1[1] + (c2[1] - c1[1]) * t)
        b = int(c1[2] + (c2[2] - c1[2]) * t)
        draw.line([(0, y), (w, y)], fill=(r, g, b))
    return img


def _radial_glow(img: Image.Image, cx: int, cy: int, radius: int, color: tuple, strength: float = 0.35) -> Image.Image:
    overlay = Image.new("RGB", img.size, (0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    for r in range(radius, 0, -8):
        alpha = int(255 * strength * (1 - r / radius))
        c = tuple(min(255, int(color[i] * alpha / 255)) for i in range(3))
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c)
    return Image.blend(img, overlay, 0.55)


def _noise(img: Image.Image, rng: random.Random, amount: int = 12) -> Image.Image:
    px = img.load()
    w, h = img.size
    for _ in range((w * h) // 800):
        x, y = rng.randint(0, w - 1), rng.randint(0, h - 1)
        r, g, b = px[x, y]
        d = rng.randint(-amount, amount)
        px[x, y] = tuple(max(0, min(255, c + d)) for c in (r, g, b))
    return img.filter(ImageFilter.GaussianBlur(radius=0.6))


def _draw_food_scene(draw: ImageDraw.ImageDraw, w: int, h: int, accent: tuple, rng: random.Random, variant: str) -> None:
    """Brasserie / restauration — compositions chaleureuses sans texte."""
    warm = (210, 140, 60)
    cream = (248, 236, 210)
    wood = (90, 55, 35)
    burgundy = accent

    if variant == "hero":
        draw.rectangle([0, 0, w, h], fill=(35, 22, 18))
        for i in range(6):
            draw.rectangle([40 + i * 55, 40, 85 + i * 55, h - 80], fill=(55, 38, 28))
        for i in range(4):
            tx = 120 + i * 220
            draw.ellipse([tx, h - 200, tx + 140, h - 60], fill=wood)
            draw.ellipse([tx + 20, h - 230, tx + 120, h - 150], fill=burgundy)
        draw.rectangle([w - 280, 30, w - 40, h - 40], fill=(25, 18, 14))
        for row in range(8):
            for col in range(3):
                draw.rectangle(
                    [w - 260 + col * 70, 50 + row * 55, w - 200 + col * 70, 95 + row * 55],
                    fill=(80, 30, 40) if (row + col) % 2 else (60, 25, 35),
                )
        draw.polygon([(w // 2 - 40, 20), (w // 2, 5), (w // 2 + 40, 20), (w // 2 + 30, 80), (w // 2 - 30, 80)], fill=warm)
    elif variant == "scene-1":
        draw.rectangle([0, 0, w, h], fill=(28, 18, 14))
        for i in range(5):
            draw.ellipse([80 + i * 130, 180, 180 + i * 130, 380], outline=warm, width=4)
            draw.ellipse([100 + i * 130, 200, 160 + i * 130, 320], fill=(255, 120, 30))
        draw.rectangle([0, h - 120, w, h], fill=(50, 32, 22))
    elif variant == "scene-2":
        draw.rectangle([0, 0, w, h], fill=(18, 12, 10))
        for row in range(6):
            for col in range(5):
                bx = 60 + col * 140
                by = 60 + row * 70
                draw.rectangle([bx, by, bx + 35, by + 55], fill=(55, 20, 28))
                draw.ellipse([bx + 5, by - 8, bx + 30, by + 8], fill=(40, 15, 20))
    elif variant == "scene-3":
        draw.rectangle([0, 0, w, h // 2], fill=(120, 175, 220))
        draw.rectangle([0, h // 2, w, h], fill=cream)
        draw.polygon([(w // 2 - 120, h // 2 - 20), (w // 2, h // 2 - 180), (w // 2 + 120, h // 2 - 20)], fill=(180, 175, 165))
        for i in range(5):
            draw.ellipse([80 + i * 140, h - 180, 200 + i * 140, h - 60], fill=wood)
            draw.rectangle([110 + i * 140, h - 220, 170 + i * 140, h - 180], fill=burgundy)
    elif variant == "card-1":
        draw.rectangle([0, 0, w, h], fill=cream)
        draw.ellipse([w // 2 - 160, h // 2 - 100, w // 2 + 160, h // 2 + 100], fill=(255, 255, 250))
        draw.ellipse([w // 2 - 120, h // 2 - 60, w // 2 + 120, h // 2 + 60], fill=(180, 100, 50))
        draw.ellipse([w // 2 - 40, h // 2 - 30, w // 2 + 40, h // 2 + 30], fill=(90, 140, 60))
    elif variant == "card-2":
        draw.rectangle([0, 0, w, h], fill=(255, 248, 235))
        draw.rounded_rectangle([w // 4, h // 4, 3 * w // 4, 3 * h // 4], radius=24, fill=(240, 200, 120))
        draw.ellipse([w // 2 - 80, h // 2 - 50, w // 2 + 80, h // 2 + 70], fill=(200, 80, 100))
    elif variant == "card-3":
        draw.rectangle([0, 0, w, h], fill=(45, 32, 28))
        draw.rounded_rectangle([60, 80, w - 60, h - 80], radius=16, outline=warm, width=3)
        for i in range(4):
            draw.ellipse([100 + i * 150, h // 2 - 40, 200 + i * 150, h // 2 + 60], fill=wood)
    elif variant.startswith("gallery"):
        draw.rectangle([0, 0, w, h], fill=(40, 28, 22))
        n = 3 if "1" in variant else 2
        for i in range(n):
            gw = (w - 80) // n - 20
            gx = 40 + i * (gw + 20)
            draw.rectangle([gx, 60, gx + gw, h - 60], fill=(65, 45, 35))
            draw.ellipse([gx + gw // 4, 100, gx + 3 * gw // 4, h - 120], fill=warm)
    else:
        draw.rectangle([0, 0, w, h], fill=cream)
        draw.ellipse([w // 2 - 100, h // 2 - 80, w // 2 + 100, h // 2 + 80], fill=burgundy)


def _draw_scene(draw: ImageDraw.ImageDraw, w: int, h: int, scene: str, accent: tuple, rng: random.Random, filename: str, slug: str) -> None:
    if slug == "restauration" or scene == "food":
        _draw_food_scene(draw, w, h, accent, rng, filename.removesuffix(".png"))
        return

    light = tuple(min(255, c + 50) for c in accent)
    mid = tuple(max(0, c - 30) for c in accent)
    if scene in ("hero", "interior"):
        draw.rounded_rectangle([40, 80, w - 40, h - 60], radius=20, outline=light, width=3)
        for i in range(5):
            draw.rectangle([60 + i * 90, 100, 130 + i * 90, h - 120], fill=mid if i % 2 else light)
    elif scene == "food":
        draw.ellipse([w // 2 - 120, h // 2 - 80, w // 2 + 120, h // 2 + 80], outline=light, width=4)
        draw.line([(w // 2 - 80, h // 2), (w // 2 + 80, h // 2)], fill=light, width=2)
    elif scene == "spa":
        for i in range(8):
            x, y = rng.randint(80, w - 80), rng.randint(80, h - 80)
            draw.ellipse([x - 25, y - 25, x + 25, y + 25], outline=light, width=2)
    elif scene == "medical":
        draw.rounded_rectangle([w // 2 - 60, 100, w // 2 + 60, h - 100], radius=12, fill=mid)
        draw.line([(w // 2, 130), (w // 2, h - 130)], fill=light, width=6)
        draw.line([(w // 2 - 40, h // 2), (w // 2 + 40, h // 2)], fill=light, width=6)
    elif scene == "garage":
        draw.polygon([(40, h - 80), (w // 2, 100), (w - 40, h - 80)], outline=light, width=3)
        draw.ellipse([100, h - 160, 180, h - 80], outline=light, width=3)
        draw.ellipse([w - 180, h - 160, w - 100, h - 80], outline=light, width=3)
    elif scene == "retail":
        for i in range(4):
            draw.rectangle([50 + i * 140, 120, 170 + i * 140, h - 100], outline=light, width=2)
    elif scene == "office":
        draw.rectangle([80, 100, w - 80, h - 100], outline=light, width=2)
        for row in range(4):
            draw.line([(100, 140 + row * 50), (w - 100, 140 + row * 50)], fill=light, width=2)
    elif scene == "industrial":
        for i in range(3):
            draw.rectangle([60 + i * 200, h - 220, 220 + i * 200, h - 80], outline=light, width=3)
    elif scene == "property":
        draw.polygon([(w // 2, 80), (80, h - 80), (w - 80, h - 80)], outline=light, width=4)
        draw.rectangle([w // 2 - 40, h - 160, w // 2 + 40, h - 80], fill=mid)
    elif scene == "legal":
        draw.rectangle([w // 2 - 8, 90, w // 2 + 8, h - 90], fill=light)
        draw.ellipse([w // 2 - 50, 70, w // 2 + 50, 120], outline=light, width=3)
    elif scene == "architecture":
        draw.line([(60, h - 80), (w // 2, 90), (w - 60, h - 80)], fill=light, width=4)
        draw.line([(w // 2, 90), (w // 2, h - 80)], fill=light, width=2)
    elif scene == "sport":
        draw.ellipse([w // 2 - 100, h // 2 - 100, w // 2 + 100, h // 2 + 100], outline=light, width=4)
    elif scene == "photo":
        draw.rectangle([w // 2 - 100, h // 2 - 70, w // 2 + 100, h // 2 + 70], outline=light, width=3)
        draw.ellipse([w // 2 - 30, h // 2 - 30, w // 2 + 30, h // 2 + 30], outline=light, width=2)
    elif scene == "team":
        for i in range(5):
            cx = 80 + i * ((w - 160) // 4)
            draw.ellipse([cx - 35, 140, cx + 35, 210], fill=mid)
            draw.rectangle([cx - 45, 210, cx + 45, h - 100], fill=light)
    elif scene == "saas_ui":
        draw.rounded_rectangle([50, 50, w - 50, h - 50], radius=16, outline=light, width=2)
        draw.rectangle([50, 50, w - 50, 110], fill=mid)
        for row in range(5):
            draw.line([(70, 140 + row * 45), (w - 70, 140 + row * 45)], fill=light, width=2)
    elif scene == "gallery":
        for i in range(3):
            draw.rectangle([40 + i * (w // 3), 100, 30 + (i + 1) * (w // 3), h - 80], outline=light, width=2)
    elif scene == "card":
        draw.rounded_rectangle([60, 100, w - 60, h - 80], radius=14, outline=light, width=2)
        draw.rectangle([60, 100, w - 60, 180], fill=mid)
    elif scene == "detail":
        draw.ellipse([w // 2 - 80, h // 2 - 80, w // 2 + 80, h // 2 + 80], outline=light, width=3)
    elif scene == "product":
        draw.rounded_rectangle([w // 3, h // 3, 2 * w // 3, 2 * h // 3], radius=20, outline=light, width=4)
    else:
        for i in range(4):
            bw = rng.randint(80, 160)
            draw.rounded_rectangle([60 + i * 140, h - 180 - rng.randint(0, 40), 60 + i * 140 + bw, h - 80], radius=8, outline=light, width=2)


def gen_image(path: Path, slug: str, label: str, category: str, scene: str, w: int, h: int) -> None:
    pal = PALETTES.get(category, [(71, 85, 105), (241, 245, 249)])
    rng = random.Random(_seed(slug, path.name))
    c1 = tuple(max(0, min(255, c + rng.randint(-15, 15))) for c in pal[0])
    c2 = pal[1]
    img = _gradient(w, h, c1, c2)
    draw = ImageDraw.Draw(img)
    _draw_scene(draw, w, h, scene, pal[0], rng, path.name, slug)
    if path.name == "hero.png" and slug == "restauration":
        img = _radial_glow(img, w // 3, h // 3, min(w, h) // 2, (255, 200, 120))
    img = _noise(img, rng)
    _save_png(img, path)


def gen_icon_svg(path: Path, category: str, accent: tuple) -> None:
    d = ICON_PATHS.get(category, ICON_PATHS.get("retail", "M8 8h48v48H8z"))
    r, g, b = accent
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="rgb({r},{g},{b})"/><path d="{d}" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/></svg>'
    path.write_text(svg, encoding="utf-8")


def gen_apple_touch(path: Path, accent: tuple, letter: str) -> None:
    size = 180
    img = Image.new("RGB", (size, size), accent)
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([8, 8, size - 8, size - 8], radius=28, outline=(255, 255, 255), width=3)
    f = _font(72)
    bbox = draw.textbbox((0, 0), letter, font=f)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((size - tw) // 2, (size - th) // 2 - 8), letter, fill=(255, 255, 255), font=f)
    _save_png(img, path)


def clean_demo_images(slug: str, keep: set[str]) -> int:
    img_dir = DEMOS / slug / "images"
    if not img_dir.is_dir():
        return 0
    n = 0
    for f in img_dir.iterdir():
        if f.is_file() and f.name not in keep and f.suffix.lower() in {".png", ".svg", ".jpg", ".webp"}:
            if f.name != "icon.svg":
                f.unlink()
                n += 1
    return n


def remove_orphan_demos() -> None:
    for slug in ORPHAN_SLUGS:
        d = DEMOS / slug
        if d.is_dir():
            shutil.rmtree(d)


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Génère les visuels des vitrines démo")
    p.add_argument("--slug", help="Limiter à une vitrine (ex. restauration)")
    p.add_argument("--force", action="store_true", help="Régénérer même si le fichier existe")
    p.add_argument("--limit", type=int, default=0, help="Nombre max d'images (0 = toutes)")
    p.add_argument("--skip-icons", action="store_true", help="Ne pas régénérer favicon / apple-touch-icon")
    return p.parse_args()


def main() -> None:
    args = _parse_args()
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    titles = {it["slug"]: it.get("title") or it["slug"] for it in data["items"]}
    print("=== Génération visuels PIL ===")
    remove_orphan_demos()

    by_slug: dict[str, set[str]] = {}
    specs = image_specs()
    if args.slug:
        specs = [s for s in specs if s[0] == args.slug]
        if not specs:
            raise SystemExit(f"Vitrine inconnue : {args.slug}")

    total_cleaned = 0
    total_written = 0
    total_skipped = 0

    for slug, filename, label, scene, category in specs:
        if args.limit and total_written >= args.limit:
            break
        by_slug.setdefault(slug, set()).add(filename)
        img_dir = DEMOS / slug / "images"
        out = img_dir / filename
        w, h = (1200, 520) if filename == "hero.png" else (800, 520)
        if filename.startswith("gallery"):
            scene = "gallery"
        elif filename.startswith("card"):
            scene = "card"

        if out.is_file() and not args.force:
            total_skipped += 1
            continue

        print(f"  {slug}/{filename}")
        gen_image(out, slug, label, category, scene, w, h)
        total_written += 1

    if not args.skip_icons:
        for slug, keep in by_slug.items():
            keep |= {"icon.svg", "apple-touch-icon.png"}
            total_cleaned += clean_demo_images(slug, keep)
            pal = PALETTES.get(
                next((c for s, _, _, _, c in specs if s == slug), "retail"),
                [(71, 85, 105), (241, 245, 249)],
            )
            title = titles.get(slug, slug)
            letter = title[0].upper()
            cat = next((c for s, _, _, _, c in specs if s == slug), "retail")
            img_dir = DEMOS / slug / "images"
            gen_icon_svg(img_dir / "icon.svg", cat, pal[0])
            gen_apple_touch(img_dir / "apple-touch-icon.png", pal[0], letter)

    print(
        f"\n[OK] {total_written} images générées · {total_skipped} ignorées (déjà présentes)"
        f" · {total_cleaned} anciens fichiers supprimés · {len(by_slug)} vitrines"
    )


if __name__ == "__main__":
    main()
