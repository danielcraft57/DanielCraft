#!/usr/bin/env python3
"""
Génère les illustrations de la page d'accueil (charte bleu DanielCraft).

Usage :
  python scripts/generate_home_images.py
  python scripts/generate_home_images.py --only hero audit
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "images" / "home"

SKY_TOP = "#e8f6fc"
SKY_BOTTOM = "#f3f4f6"
BLUE_LIGHT = "#7bcde3"
BLUE_MID = "#4da9d6"
BLUE_DARK = "#2f78a6"
INK = "#0f3550"
PALE = "#e8f4fb"
WHITE = "#ffffff"
ACCENT = "#dc2626"

SCENES: dict[str, tuple[int, int]] = {
    "home-hero": (800, 600),
    "home-offer-vitrine": (640, 400),
    "home-offer-visibilite": (640, 400),
    "home-offer-assistant": (640, 400),
    "home-offer-audit": (640, 400),
}


def _hex_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def _rgba(h: str, a: float) -> tuple[int, int, int, int]:
    r, g, b = _hex_rgb(h)
    return r, g, b, int(255 * a)


def _sky_gradient(w: int, h: int) -> Image.Image:
    c0 = np.array(_hex_rgb(SKY_TOP), dtype=np.float32)
    c1 = np.array(_hex_rgb(SKY_BOTTOM), dtype=np.float32)
    t = np.linspace(0.0, 1.0, h, dtype=np.float32)[:, np.newaxis]
    rgb = np.zeros((h, w, 3), dtype=np.float32)
    for i in range(3):
        rgb[:, :, i] = c0[i] + (c1[i] - c0[i]) * t
    return Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8))


def _scale(size: tuple[int, int]) -> float:
    return min(size) / 640.0


def _draw_orb(draw: ImageDraw.ImageDraw, cx: int, cy: int, r: int, color: str, alpha: float) -> None:
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=_rgba(color, alpha))


def _draw_person(draw: ImageDraw.ImageDraw, cx: int, cy: int, s: float) -> None:
    hr = int(42 * s)
    draw.ellipse([cx - hr, cy - hr, cx + hr, cy + hr], fill=_rgba(WHITE, 0.95))
    body = [
        (cx - int(62 * s), cy + int(56 * s)),
        (cx - int(62 * s), cy + int(24 * s)),
        (cx - int(34 * s), cy + int(16 * s)),
        (cx, cy + int(16 * s)),
        (cx + int(34 * s), cy + int(16 * s)),
        (cx + int(62 * s), cy + int(24 * s)),
        (cx + int(62 * s), cy + int(56 * s)),
        (cx + int(62 * s), cy + int(140 * s)),
        (cx + int(48 * s), cy + int(168 * s)),
        (cx + int(28 * s), cy + int(182 * s)),
        (cx - int(28 * s), cy + int(182 * s)),
        (cx - int(48 * s), cy + int(168 * s)),
        (cx - int(62 * s), cy + int(140 * s)),
    ]
    draw.polygon(body, fill=_rgba(PALE, 0.92))


def _draw_browser(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    w: int,
    h: int,
    *,
    accent_bar: bool = True,
    cta: bool = False,
) -> None:
    r = max(8, w // 28)
    draw.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=_rgba(WHITE, 0.96), outline=_rgba(BLUE_MID, 0.35), width=2)
    bar_h = max(18, h // 9)
    draw.rounded_rectangle([x, y, x + w, y + bar_h + r], radius=r, fill=_rgba(BLUE_MID, 0.18))
    for i, dot in enumerate((ACCENT, "#f59e0b", "#22c55e")):
        dr = max(4, bar_h // 5)
        draw.ellipse([x + 14 + i * (dr * 2 + 8), y + bar_h // 2 - dr, x + 14 + i * (dr * 2 + 8) + dr * 2, y + bar_h // 2 + dr], fill=_rgba(dot, 0.75))
    lx, ly = x + 18, y + bar_h + 16
    lw = w - 36
    if accent_bar:
        draw.rounded_rectangle([lx, ly, lx + int(lw * 0.42), ly + 12], radius=6, fill=_rgba(BLUE_MID, 0.55))
        ly += 22
    for frac in (0.78, 0.62, 0.48):
        draw.rounded_rectangle([lx, ly, lx + int(lw * frac), ly + 8], radius=4, fill=_rgba(PALE, 0.95))
        ly += 16
    if cta:
        draw.rounded_rectangle([lx, ly + 8, lx + 96, ly + 34], radius=8, fill=_rgba(ACCENT, 0.88))


def _draw_phone(draw: ImageDraw.ImageDraw, x: int, y: int, w: int, h: int) -> None:
    r = max(10, w // 6)
    draw.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=_rgba(INK, 0.12), outline=_rgba(BLUE_DARK, 0.35), width=2)
    inset = max(6, w // 10)
    draw.rounded_rectangle([x + inset, y + inset + 8, x + w - inset, y + h - inset - 10], radius=max(6, r // 2), fill=_rgba(WHITE, 0.96))
    bx = x + inset + 8
    by = y + inset + 18
    bw = w - 2 * inset - 16
    draw.rounded_rectangle([bx, by, bx + bw, by + 10], radius=4, fill=_rgba(BLUE_MID, 0.5))
    for i in range(3):
        draw.rounded_rectangle([bx, by + 18 + i * 12, bx + int(bw * (0.9 - i * 0.12)), by + 24 + i * 12], radius=3, fill=_rgba(PALE, 0.95))


def render_home_hero(w: int, h: int) -> Image.Image:
    s = _scale((w, h))
    img = _sky_gradient(w, h).convert("RGBA")
    draw = ImageDraw.Draw(img)
    _draw_orb(draw, int(w * 0.12), int(h * 0.18), int(70 * s), BLUE_LIGHT, 0.22)
    _draw_orb(draw, int(w * 0.88), int(h * 0.22), int(52 * s), BLUE_MID, 0.16)
    _draw_orb(draw, int(w * 0.78), int(h * 0.82), int(44 * s), BLUE_LIGHT, 0.14)
    _draw_person(draw, int(w * 0.24), int(h * 0.34), s * 1.05)
    bx, by = int(w * 0.38), int(h * 0.16)
    bw, bh = int(w * 0.52), int(h * 0.62)
    _draw_browser(draw, bx, by, bw, bh, accent_bar=True, cta=True)
    _draw_phone(draw, bx + bw - int(58 * s), by + bh - int(118 * s), int(46 * s), int(88 * s))
    return img


def render_offer_vitrine(w: int, h: int) -> Image.Image:
    s = _scale((w, h))
    img = _sky_gradient(w, h).convert("RGBA")
    draw = ImageDraw.Draw(img)
    _draw_orb(draw, int(w * 0.15), int(h * 0.75), int(36 * s), BLUE_LIGHT, 0.18)
    bx, by = int(w * 0.08), int(h * 0.12)
    bw, bh = int(w * 0.62), int(h * 0.76)
    _draw_browser(draw, bx, by, bw, bh, accent_bar=True, cta=False)
    px, py = bx + bw - int(24 * s), by + int(36 * s)
    _draw_phone(draw, px, py, int(110 * s), int(190 * s))
    shop_x, shop_y = bx + int(28 * s), by + int(bh * 0.34)
    draw.rounded_rectangle([shop_x, shop_y, shop_x + int(bw * 0.38), shop_y + int(bh * 0.28)], radius=10, fill=_rgba(BLUE_LIGHT, 0.35))
    draw.rounded_rectangle([shop_x + int(bw * 0.44), shop_y, bx + bw - int(24 * s), shop_y + int(bh * 0.28)], radius=10, fill=_rgba(PALE, 0.9))
    return img


def render_offer_visibilite(w: int, h: int) -> Image.Image:
    s = _scale((w, h))
    img = _sky_gradient(w, h).convert("RGBA")
    draw = ImageDraw.Draw(img)
    card_x, card_y = int(w * 0.08), int(h * 0.14)
    card_w, card_h = int(w * 0.84), int(h * 0.72)
    draw.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + card_h], radius=18, fill=_rgba(WHITE, 0.94), outline=_rgba(BLUE_MID, 0.28), width=2)
    sb_y = card_y + int(24 * s)
    draw.rounded_rectangle([card_x + 24, sb_y, card_x + card_w - 24, sb_y + int(44 * s)], radius=22, fill=_rgba(WHITE, 1), outline=_rgba(BLUE_MID, 0.35), width=2)
    draw.ellipse([card_x + 36, sb_y + 10, card_x + 56, sb_y + 30], fill=_rgba(BLUE_MID, 0.45))
    draw.rounded_rectangle([card_x + 66, sb_y + 14, card_x + card_w - 110, sb_y + 26], radius=5, fill=_rgba(PALE, 0.95))
    lens = card_x + card_w - 72
    draw.ellipse([lens, sb_y + 6, lens + 32, sb_y + 38], fill=_rgba(BLUE_MID, 0.25), outline=_rgba(BLUE_DARK, 0.45), width=2)
    draw.line([(lens + 26, sb_y + 32), (lens + 42, sb_y + 48)], fill=_rgba(BLUE_DARK, 0.55), width=3)
    row_y = sb_y + int(58 * s)
    for i in range(3):
        ry = row_y + i * int(52 * s)
        draw.rounded_rectangle([card_x + 24, ry, card_x + card_w - 24, ry + int(40 * s)], radius=10, fill=_rgba(PALE, 0.55 if i else 0.75))
        draw.rounded_rectangle([card_x + 36, ry + 10, card_x + int(card_w * 0.45), ry + 18], radius=4, fill=_rgba(BLUE_MID, 0.45 if i == 0 else 0.25))
        for star in range(5):
            sx = card_x + int(card_w * 0.52) + star * 14
            draw.ellipse([sx, ry + 12, sx + 8, ry + 20], fill=_rgba(BLUE_MID, 0.35 if star < 4 else 0.15))
    pin_x, pin_y = card_x + card_w - int(78 * s), card_y + card_h - int(58 * s)
    draw.ellipse([pin_x, pin_y, pin_x + 28, pin_y + 28], fill=_rgba(ACCENT, 0.85))
    draw.polygon([(pin_x + 14, pin_y + 34), (pin_x + 6, pin_y + 24), (pin_x + 22, pin_y + 24)], fill=_rgba(ACCENT, 0.85))
    return img


def render_offer_assistant(w: int, h: int) -> Image.Image:
    s = _scale((w, h))
    img = _sky_gradient(w, h).convert("RGBA")
    draw = ImageDraw.Draw(img)
    bx, by = int(w * 0.1), int(h * 0.1)
    bw, bh = int(w * 0.8), int(h * 0.8)
    _draw_browser(draw, bx, by, bw, bh, accent_bar=False, cta=False)
    bubble_w = int(bw * 0.52)
    user_y = by + int(bh * 0.28)
    draw.rounded_rectangle([bx + 24, user_y, bx + 24 + bubble_w, user_y + 46], radius=14, fill=_rgba(BLUE_MID, 0.22))
    draw.rounded_rectangle([bx + 36, user_y + 12, bx + bubble_w, user_y + 22], radius=4, fill=_rgba(BLUE_DARK, 0.35))
    bot_y = user_y + 58
    draw.rounded_rectangle([bx + bw - bubble_w - 24, bot_y, bx + bw - 24, bot_y + 72], radius=14, fill=_rgba(WHITE, 0.98), outline=_rgba(BLUE_MID, 0.35), width=2)
    draw.ellipse([bx + bw - bubble_w - 6, bot_y + 8, bx + bw - bubble_w + 26, bot_y + 40], fill=_rgba(BLUE_MID, 0.35))
    ty = bot_y + 14
    for frac in (0.72, 0.58):
        draw.rounded_rectangle([bx + bw - bubble_w + 34, ty, bx + bw - 38, ty + 8], radius=4, fill=_rgba(PALE, 0.95))
        ty += 14
    draw.rounded_rectangle([bx + bw - bubble_w + 34, ty + 4, bx + bw - 98, ty + 24], radius=8, fill=_rgba(BLUE_MID, 0.45))
    return img


def render_offer_audit(w: int, h: int) -> Image.Image:
    s = _scale((w, h))
    img = _sky_gradient(w, h).convert("RGBA")
    draw = ImageDraw.Draw(img)
    clip_x, clip_y = int(w * 0.08), int(h * 0.12)
    clip_w, clip_h = int(w * 0.42), int(h * 0.76)
    draw.rounded_rectangle([clip_x, clip_y, clip_x + clip_w, clip_y + clip_h], radius=16, fill=_rgba(WHITE, 0.96), outline=_rgba(BLUE_MID, 0.3), width=2)
    draw.rounded_rectangle([clip_x + 18, clip_y + 16, clip_x + clip_w - 18, clip_y + 38], radius=6, fill=_rgba(BLUE_MID, 0.35))
    for i, checked in enumerate((True, True, False)):
        iy = clip_y + 52 + i * int(46 * s)
        box = [clip_x + 22, iy, clip_x + 42, iy + 20]
        draw.rounded_rectangle(box, radius=4, outline=_rgba(BLUE_DARK, 0.35), width=2, fill=_rgba(BLUE_LIGHT, 0.35) if checked else _rgba(WHITE, 0.9))
        if checked:
            draw.line([(clip_x + 26, iy + 10), (clip_x + 32, iy + 16), (clip_x + 40, iy + 6)], fill=_rgba(INK, 0.7), width=2)
        draw.rounded_rectangle([clip_x + 50, iy + 4, clip_x + clip_w - 22, iy + 12], radius=4, fill=_rgba(PALE, 0.95))
    chart_x = int(w * 0.54)
    chart_y = int(h * 0.22)
    chart_w = int(w * 0.36)
    chart_h = int(h * 0.56)
    draw.rounded_rectangle([chart_x, chart_y, chart_x + chart_w, chart_y + chart_h], radius=14, fill=_rgba(WHITE, 0.92), outline=_rgba(BLUE_MID, 0.25), width=2)
    bars = (0.35, 0.52, 0.68, 0.88)
    gap = chart_w // (len(bars) * 2 + 1)
    for i, frac in enumerate(bars):
        bx = chart_x + gap + i * (gap * 2)
        bh = int(chart_h * frac) - gap
        by = chart_y + chart_h - bh - gap
        color = BLUE_LIGHT if i < 2 else BLUE_MID if i == 2 else BLUE_DARK
        draw.rounded_rectangle([bx, by, bx + gap, chart_y + chart_h - gap], radius=6, fill=_rgba(color, 0.75))
    draw.line([(chart_x + 12, chart_y + 18), (chart_x + chart_w - 12, chart_y + 18)], fill=_rgba(BLUE_MID, 0.45), width=3)
    badge_x, badge_y = chart_x + int(chart_w * 0.18), chart_y - int(18 * s)
    draw.rounded_rectangle([badge_x, badge_y, badge_x + int(88 * s), badge_y + int(30 * s)], radius=10, fill=_rgba(ACCENT, 0.9))
    return img


RENDERERS = {
    "home-hero": render_home_hero,
    "home-offer-vitrine": render_offer_vitrine,
    "home-offer-visibilite": render_offer_visibilite,
    "home-offer-assistant": render_offer_assistant,
    "home-offer-audit": render_offer_audit,
}


def _save_pair(name: str, im: Image.Image, expected: tuple[int, int]) -> None:
    if im.size != expected:
        raise ValueError(f"{name}: taille {im.size} != attendue {expected}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    png_path = OUT_DIR / f"{name}.png"
    webp_path = OUT_DIR / f"{name}.webp"
    im.convert("RGB").save(png_path, "PNG", optimize=True)
    im.save(webp_path, "WEBP", quality=88, method=6)
    print(f"OK: {png_path.relative_to(ROOT)}, {webp_path.name}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", metavar="SLUG", help="home-hero, vitrine, visibilite, assistant, audit")
    args = ap.parse_args()
    alias = {
        "hero": "home-hero",
        "vitrine": "home-offer-vitrine",
        "visibilite": "home-offer-visibilite",
        "assistant": "home-offer-assistant",
        "audit": "home-offer-audit",
    }
    selected = set(args.only or SCENES.keys())
    for key, full in alias.items():
        if key in selected:
            selected.discard(key)
            selected.add(full)
    for name in SCENES:
        if name not in selected:
            continue
        w, h = SCENES[name]
        im = RENDERERS[name](w, h)
        _save_pair(name, im, (w, h))


if __name__ == "__main__":
    main()
