"""
Illustrations cartoon / BD plein cadre pour les cartes Open Graph DanielCraft.
Scènes immersives avec personnages, interactions et texte en surimpression.
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Callable, Sequence

import numpy as np
from PIL import Image, ImageDraw, ImageFont

SKY_TOP = "#e8f6fc"
SKY_BOTTOM = "#f3f4f6"
BLUE_LIGHT = "#7bcde3"
BLUE_MID = "#4da9d6"
BLUE_DARK = "#2f78a6"
INK = "#0f3550"
PALE = "#e8f4fb"
WHITE = "#ffffff"
ACCENT = "#dc2626"
TEXT_ON_SCRIM = "#ffffff"
TEXT_MUTED_SCRIM = "#cce8f5"

OG_W, OG_H = 1200, 630
TWITTER_BOTTOM_RESERVE = 48
FAVICON_PATH = Path(__file__).resolve().parent.parent / "assets" / "icons" / "favicons" / "favicon-96x96.png"
BRAND_DOMAIN = "danielcraft.fr"

CATEGORY_COLORS = {
    "identite": BLUE_DARK,
    "ia": BLUE_MID,
    "technique": "#3d8b72",
    "site-contenu": "#c97b4a",
    "maintenance": "#5b6fd6",
    "web": BLUE_DARK,
    "tools": BLUE_MID,
    "mobile": "#6d5bd6",
    "iot": "#0891b2",
    "specialized": "#a8558f",
    "learning": "#b8860b",
    "desktop": "#475569",
    "vitrine": BLUE_DARK,
    "default": BLUE_MID,
}

ScenePainter = Callable[[ImageDraw.ImageDraw, Image.Image, tuple[int, int, int, int], float, str], None]


def _hex_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def _rgba(h: str, a: float) -> tuple[int, int, int, int]:
    r, g, b = _hex_rgb(h)
    return r, g, b, int(255 * a)


def _font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    paths = [
        Path("C:/Windows/Fonts/segoeuib.ttf") if bold else Path("C:/Windows/Fonts/segoeui.ttf"),
        Path("C:/Windows/Fonts/arialbd.ttf") if bold else Path("C:/Windows/Fonts/arial.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf") if bold else Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ]
    for p in paths:
        if p.is_file():
            try:
                return ImageFont.truetype(str(p), size)
            except OSError:
                continue
    return ImageFont.load_default()


def _sky_gradient(w: int, h: int) -> Image.Image:
    c0 = np.array(_hex_rgb(SKY_TOP), dtype=np.float32)
    c1 = np.array(_hex_rgb(SKY_BOTTOM), dtype=np.float32)
    t = np.linspace(0.0, 1.0, h, dtype=np.float32)[:, np.newaxis]
    rgb = np.zeros((h, w, 3), dtype=np.float32)
    for i in range(3):
        rgb[:, :, i] = c0[i] + (c1[i] - c0[i]) * t
    return Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8))


def _wrap_lines(draw: ImageDraw.ImageDraw, text: str, font, max_width: int, max_lines: int = 2) -> list[str]:
    words = (text or "").split()
    if not words:
        return [""]
    lines: list[str] = []
    current: list[str] = []
    for word in words:
        trial = " ".join(current + [word])
        if draw.textlength(trial, font=font) <= max_width:
            current.append(word)
        else:
            if current:
                lines.append(" ".join(current))
            current = [word]
            if len(lines) >= max_lines:
                break
    if current and len(lines) < max_lines:
        lines.append(" ".join(current))
    if len(lines) == max_lines and len(" ".join(words)) > len(" ".join(lines)):
        last = lines[-1]
        while last and draw.textlength(last + "…", font=font) > max_width:
            last = last[:-1]
        lines[-1] = (last.rstrip(".,; ") + "…") if last else "…"
    return lines or [""]


def _social_hook(text: str, max_len: int = 72) -> str:
    clean = " ".join((text or "").split())
    if len(clean) <= max_len:
        return clean
    cut = clean[: max_len - 1].rsplit(" ", 1)[0]
    return (cut.rstrip(".,; ") + "…") if cut else "…"


def _outline_rounded_rect(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    radius: int,
    fill: str,
    outline: str = INK,
    width: int = 2,
    fill_alpha: float = 1.0,
) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=_rgba(fill, fill_alpha), outline=_rgba(outline, 0.5), width=width)


def _draw_orb(draw: ImageDraw.ImageDraw, cx: int, cy: int, r: int, color: str, alpha: float) -> None:
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=_rgba(color, alpha))


def _draw_character(
    draw: ImageDraw.ImageDraw,
    cx: int,
    cy: int,
    s: float,
    *,
    shirt: str = PALE,
    apron: bool = False,
    point: tuple[int, int] | None = None,
    hair: str | None = None,
) -> None:
    hr = int(46 * s)
    draw.ellipse([cx - hr, cy - hr, cx + hr, cy + hr], fill=_rgba(WHITE, 0.98), outline=_rgba(INK, 0.5), width=max(2, int(3 * s)))
    if hair:
        draw.arc([cx - hr, cy - hr - int(6 * s), cx + hr, cy + int(10 * s)], 195, 345, fill=_rgba(hair, 0.5), width=max(3, int(4 * s)))
    ey = cy - int(5 * s)
    for side in (-1, 1):
        ex = cx + side * int(15 * s)
        draw.ellipse([ex - int(6 * s), ey - int(6 * s), ex + int(6 * s), ey + int(6 * s)], fill=_rgba(INK, 0.9))
        draw.ellipse([ex + int(2 * s), ey - int(4 * s), ex + int(5 * s), ey - int(1 * s)], fill=_rgba(WHITE, 1))
    my = cy + int(16 * s)
    draw.arc([cx - int(18 * s), my - int(12 * s), cx + int(18 * s), my + int(10 * s)], 15, 165, fill=_rgba(INK, 0.55), width=max(2, int(3 * s)))

    sy = cy + int(42 * s)
    bw = int(62 * s)
    bot = cy + int(168 * s)
    draw.rounded_rectangle([cx - bw, sy, cx + bw, bot], radius=int(20 * s), fill=_rgba(shirt, 0.97), outline=_rgba(INK, 0.4), width=2)
    if apron:
        draw.polygon(
            [(cx - int(46 * s), sy + int(10 * s)), (cx + int(46 * s), sy + int(10 * s)), (cx + int(38 * s), bot - int(10 * s)), (cx - int(38 * s), bot - int(10 * s))],
            fill=_rgba("#c97b4a", 0.6),
            outline=_rgba(INK, 0.3),
        )

    ay = sy + int(26 * s)
    if point:
        px, py = point
        draw.line([(cx + int(48 * s), ay), (px, py)], fill=_rgba(INK, 0.45), width=max(4, int(5 * s)))
        draw.ellipse([px - int(10 * s), py - int(10 * s), px + int(10 * s), py + int(10 * s)], fill=_rgba(WHITE, 0.95), outline=_rgba(INK, 0.4), width=2)
    else:
        for side in (-1, 1):
            ax = cx + side * int(58 * s)
            draw.line([(cx + side * int(42 * s), ay), (ax, ay + int(48 * s))], fill=_rgba(INK, 0.4), width=max(3, int(4 * s)))
            draw.ellipse([ax - int(10 * s), ay + int(40 * s), ax + int(10 * s), ay + int(60 * s)], fill=_rgba(WHITE, 0.95), outline=_rgba(INK, 0.35), width=2)

    for side in (-1, 1):
        lx = cx + side * int(30 * s)
        draw.rounded_rectangle([lx - int(16 * s), bot, lx + int(16 * s), bot + int(46 * s)], radius=int(10 * s), fill=_rgba(BLUE_DARK, 0.8), outline=_rgba(INK, 0.35), width=2)


def _draw_speech(draw: ImageDraw.ImageDraw, x: int, y: int, w: int, h: int, text: str, s: float, tail: str = "left") -> None:
    _outline_rounded_rect(draw, (x, y, x + w, y + h), int(16 * s), WHITE, width=2)
    tx = x + int(14 * s) if tail == "left" else x + int(20 * s)
    draw.text((tx, y + int(10 * s)), text[:24], fill=_rgba(INK, 0.9), font=_font(max(13, int(17 * s)), bold=True))
    if tail == "left":
        draw.polygon([(x + int(20 * s), y + h), (x + int(6 * s), y + h + int(16 * s)), (x + int(36 * s), y + h - int(2 * s))], fill=_rgba(WHITE, 0.97))
    else:
        draw.polygon([(x + w - int(20 * s), y + h), (x + w - int(6 * s), y + h + int(16 * s)), (x + w - int(36 * s), y + h - int(2 * s))], fill=_rgba(WHITE, 0.97))


def _draw_browser(draw: ImageDraw.ImageDraw, x: int, y: int, w: int, h: int, *, cta: bool = False) -> None:
    r = max(10, w // 22)
    _outline_rounded_rect(draw, (x, y, x + w, y + h), r, WHITE, width=max(2, w // 200))
    bar = max(16, h // 9)
    draw.rounded_rectangle([x, y, x + w, y + bar + r], radius=r, fill=_rgba(BLUE_MID, 0.35))
    for i, c in enumerate((ACCENT, "#f59e0b", "#22c55e")):
        dr = max(4, bar // 5)
        draw.ellipse([x + 12 + i * (dr * 2 + 8), y + bar // 2 - dr, x + 12 + i * (dr * 2 + 8) + dr * 2, y + bar // 2 + dr], fill=_rgba(c, 0.85))
    lx, ly = x + 14, y + bar + 12
    lw = w - 28
    draw.rounded_rectangle([lx, ly, lx + int(lw * 0.55), ly + 12], radius=6, fill=_rgba(BLUE_MID, 0.55))
    ly += 20
    for frac in (0.9, 0.75, 0.6, 0.5):
        draw.rounded_rectangle([lx, ly, lx + int(lw * frac), ly + 9], radius=4, fill=_rgba(PALE, 0.95))
        ly += 14
    if cta:
        draw.rounded_rectangle([lx, ly + 6, lx + 88, ly + 32], radius=8, fill=_rgba(ACCENT, 0.92))


def _draw_phone(draw: ImageDraw.ImageDraw, x: int, y: int, w: int, h: int) -> None:
    r = max(10, w // 6)
    _outline_rounded_rect(draw, (x, y, x + w, y + h), r, WHITE, width=2)
    ins = max(6, w // 10)
    draw.rounded_rectangle([x + ins, y + ins + 8, x + w - ins, y + h - ins - 10], radius=max(6, r // 2), fill=_rgba(PALE, 0.7), outline=_rgba(BLUE_DARK, 0.3), width=1)
    bx, by = x + ins + 8, y + ins + 18
    bw = w - 2 * ins - 16
    draw.rounded_rectangle([bx, by, bx + bw, by + 10], radius=4, fill=_rgba(BLUE_MID, 0.6))
    for i in range(4):
        draw.rounded_rectangle([bx, by + 16 + i * 11, bx + int(bw * (0.92 - i * 0.08)), by + 22 + i * 11], radius=3, fill=_rgba(WHITE, 0.92))


def _draw_shop_interior(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], s: float) -> None:
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    draw.rectangle([x0, y0 + int(h * 0.58), x1, y1], fill=_rgba("#e8d4bc", 0.65))
    draw.rectangle([x0, y0, x0 + int(w * 0.38), y0 + int(h * 0.65)], fill=_rgba(BLUE_LIGHT, 0.28), outline=_rgba(INK, 0.15), width=2)
    for i in range(5):
        sy = y0 + int(30 * s) + i * int(50 * s)
        draw.rounded_rectangle([x1 - int(140 * s), sy, x1 - int(20 * s), sy + int(36 * s)], radius=6, fill=_rgba(WHITE, 0.55), outline=_rgba(INK, 0.12), width=1)
    draw.rounded_rectangle([x0 + int(50 * s), y0 + int(h * 0.7), x1 - int(50 * s), y1 - int(15 * s)], radius=int(16 * s), fill=_rgba("#d4a574", 0.5), outline=_rgba(INK, 0.25), width=2)


def _draw_office_bg(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], s: float) -> None:
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    draw.rectangle([x0, y0 + int(h * 0.5), x1, y1], fill=_rgba("#dce8f0", 0.5))
    draw.rectangle([x0 + int(w * 0.05), y0 + int(h * 0.08), x0 + int(w * 0.42), y0 + int(h * 0.55)], fill=_rgba(BLUE_LIGHT, 0.25), outline=_rgba(INK, 0.12), width=2)
    draw.ellipse([x1 - int(100 * s), y1 - int(130 * s), x1 - int(30 * s), y1 - int(60 * s)], fill=_rgba("#3d8b72", 0.45), outline=_rgba(INK, 0.2), width=2)


def _draw_bottom_scrim(img: Image.Image, strength: float = 0.78) -> None:
    w, h = img.size
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    top = int(h * 0.48)
    for y in range(top, h):
        t = (y - top) / max(1, h - top)
        a = int(255 * strength * (t**1.3))
        od.line([(0, y), (w, y)], fill=(10, 45, 70, a))
    img.alpha_composite(overlay)


def _draw_brand_watermark(draw: ImageDraw.ImageDraw, img: Image.Image, s: float) -> None:
    pad = int(18 * s)
    bw, bh = int(210 * s), int(48 * s)
    draw.rounded_rectangle([pad, pad, pad + bw, pad + bh], radius=int(14 * s), fill=_rgba(BLUE_DARK, 0.78), outline=_rgba(WHITE, 0.3), width=1)
    ls = int(30 * s)
    if FAVICON_PATH.is_file():
        try:
            logo = Image.open(FAVICON_PATH).convert("RGBA").resize((ls, ls), Image.Resampling.LANCZOS)
            img.paste(logo, (pad + int(8 * s), pad + int(9 * s)), logo)
        except OSError:
            pass
    draw.text((pad + int(44 * s), pad + int(12 * s)), "DanielCraft", fill=WHITE, font=_font(max(13, int(18 * s)), bold=True))


# ── Scènes plein cadre (personnages + interaction) ──────────────────────────


def _scene_hero(draw: ImageDraw.ImageDraw, img: Image.Image, box: tuple[int, int, int, int], s: float, accent: str) -> None:
    x0, y0, x1, y1 = box
    _draw_shop_interior(draw, box, s)
    lap_x, lap_y = x0 + int((x1 - x0) * 0.48), y0 + int((y1 - y0) * 0.52)
    _draw_browser(draw, lap_x, lap_y, int(340 * s), int(220 * s), cta=True)
    _draw_phone(draw, lap_x + int(300 * s), lap_y + int(140 * s), int(56 * s), int(100 * s))
    _draw_character(draw, x0 + int(280 * s), y0 + int(200 * s), s * 1.05, shirt="#dbeafe", apron=True, point=(lap_x + int(80 * s), lap_y + int(60 * s)), hair="#5c4033")
    _draw_character(draw, x0 + int(780 * s), y0 + int(210 * s), s * 1.0, shirt="#fef3c7", hair="#1f2937")
    _draw_speech(draw, x0 + int(620 * s), y0 + int(95 * s), int(200 * s), int(58 * s), "Mon site est en ligne !", s, tail="right")
    _draw_speech(draw, x0 + int(180 * s), y0 + int(85 * s), int(210 * s), int(58 * s), "Visible sur Google", s)
    _draw_sparkles(draw, x1 - int(120 * s), y0 + int(80 * s), s)


def _scene_audit(draw: ImageDraw.ImageDraw, img: Image.Image, box: tuple[int, int, int, int], s: float, accent: str) -> None:
    x0, y0, x1, y1 = box
    _draw_office_bg(draw, box, s)
    scr_x, scr_y = x0 + int(380 * s), y0 + int(90 * s)
    _draw_browser(draw, scr_x, scr_y, int(480 * s), int(300 * s))
    for i, ok in enumerate((True, True, False, True)):
        iy = scr_y + int(70 * s) + i * int(38 * s)
        draw.rounded_rectangle([scr_x + int(24 * s), iy, scr_x + int(44 * s), iy + int(20 * s)], radius=4, outline=_rgba(INK, 0.4), width=2, fill=_rgba(BLUE_LIGHT, 0.5) if ok else _rgba(WHITE, 0.8))
        if ok:
            draw.line([(scr_x + int(28 * s), iy + 10), (scr_x + int(34 * s), iy + 16), (scr_x + int(42 * s), iy + 6)], fill=_rgba(INK, 0.7), width=2)
    _draw_character(draw, x0 + int(220 * s), y0 + int(230 * s), s * 1.0, shirt=PALE, point=(scr_x + int(120 * s), scr_y + int(100 * s)))
    _draw_character(draw, x0 + int(920 * s), y0 + int(240 * s), s * 0.95, shirt="#fef3c7", hair="#374151")
    _draw_speech(draw, x0 + int(130 * s), y0 + int(120 * s), int(230 * s), int(58 * s), "On vérifie tout ça", s)
    _draw_speech(draw, x0 + int(820 * s), y0 + int(110 * s), int(200 * s), int(58 * s), "Et mes clients ?", s, tail="right")
    gr = int(55 * s)
    gx, gy = scr_x + int(380 * s), scr_y + int(40 * s)
    draw.arc([gx, gy, gx + gr * 2, gy + gr * 2], 200, 340, fill=_rgba(ACCENT, 0.85), width=max(5, int(6 * s)))


def _scene_catalog(draw: ImageDraw.ImageDraw, img: Image.Image, box: tuple[int, int, int, int], s: float, accent: str) -> None:
    x0, y0, x1, y1 = box
    _draw_office_bg(draw, box, s)
    positions = ((x0 + int(80 * s), y0 + int(100 * s), 0.85), (x0 + int(280 * s), y0 + int(130 * s), 0.95), (x0 + int(500 * s), y0 + int(90 * s), 1.0))
    for i, (bx, by, sc) in enumerate(positions):
        _draw_browser(draw, bx, by, int(280 * sc * s), int(190 * sc * s), cta=(i == 2))
    _draw_character(draw, x0 + int(200 * s), y0 + int(320 * s), s * 1.0, shirt="#dbeafe", point=(x0 + int(560 * s), y0 + int(180 * s)))
    _draw_character(draw, x0 + int(850 * s), y0 + int(310 * s), s * 0.98, shirt="#e0e7ff", hair="#4b5563")
    _draw_speech(draw, x0 + int(700 * s), y0 + int(95 * s), int(240 * s), int(58 * s), "Quel forfait me va ?", s, tail="right")


def _scene_templates(draw: ImageDraw.ImageDraw, img: Image.Image, box: tuple[int, int, int, int], s: float, accent: str) -> None:
    x0, y0, x1, y1 = box
    w = x1 - x0
    colors = (BLUE_MID, "#c97b4a", "#3d8b72", BLUE_DARK)
    labels = ("Restaurant", "Commerce", "Santé", "Services")
    for i in range(4):
        r, c = divmod(i, 2)
        tx = x0 + int(80 * s) + c * int(280 * s)
        ty = y0 + int(70 * s) + r * int(200 * s)
        tw, th = int(240 * s), int(160 * s)
        _outline_rounded_rect(draw, (tx, ty, tx + tw, ty + th), 12, WHITE, width=2)
        draw.rounded_rectangle([tx + 10, ty + 10, tx + tw - 10, ty + 32], radius=6, fill=_rgba(colors[i], 0.6))
        draw.text((tx + 16, ty + 12), labels[i], fill=WHITE, font=_font(max(11, int(14 * s)), bold=True))
        for j in range(3):
            draw.rounded_rectangle([tx + 14, ty + 42 + j * 16, tx + tw - 14 - j * 10, ty + 50 + j * 16], radius=3, fill=_rgba(PALE, 0.9))
    _draw_character(draw, x0 + int(w * 0.42), y0 + int(400 * s), s * 1.05, shirt="#fef3c7", apron=True, point=(x0 + int(200 * s), y0 + int(150 * s)))
    _draw_speech(draw, x0 + int(520 * s), y0 + int(380 * s), int(260 * s), int(58 * s), "Je choisis mon métier", s, tail="right")


def _scene_process(draw: ImageDraw.ImageDraw, img: Image.Image, box: tuple[int, int, int, int], s: float, accent: str) -> None:
    x0, y0, x1, y1 = box
    w = x1 - x0
    _draw_office_bg(draw, box, s)
    steps = [("1", "Échange"), ("2", "Devis"), ("3", "Création"), ("4", "En ligne")]
    sw = int(140 * s)
    gap = (w - sw * 4) // 5
    cy = y0 + int(180 * s)
    for i, (num, lbl) in enumerate(steps):
        sx = x0 + gap + i * (sw + gap)
        _outline_rounded_rect(draw, (sx, cy, sx + sw, cy + sw), sw // 3, WHITE, width=2)
        draw.text((sx + sw // 2 - int(10 * s), cy + sw // 2 - int(18 * s)), num, fill=_rgba(BLUE_DARK, 1), font=_font(max(20, int(32 * s)), bold=True))
        draw.text((sx + int(8 * s), cy + sw + int(10 * s)), lbl, fill=_rgba(INK, 0.8), font=_font(max(12, int(16 * s)), bold=True))
        if i < 3:
            ax = sx + sw + 6
            draw.line([(ax, cy + sw // 2), (ax + gap - 12, cy + sw // 2)], fill=_rgba(BLUE_MID, 0.8), width=4)
        _draw_character(draw, sx + sw // 2, cy + sw + int(100 * s), s * 0.55, shirt=PALE if i % 2 == 0 else "#dbeafe")
    _draw_character(draw, x0 + int(w * 0.5), y0 + int(420 * s), s * 0.9, shirt="#e0e7ff", point=(x0 + gap + sw // 2, cy + sw // 2))


def _scene_local(draw: ImageDraw.ImageDraw, img: Image.Image, box: tuple[int, int, int, int], s: float, accent: str) -> None:
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    draw.rectangle([x0, y0 + int(h * 0.55), x1, y1], fill=_rgba("#c8d8e4", 0.55))
    bx, by = x0 + int(120 * s), y0 + int(140 * s)
    bw, bh = int(340 * s), int(260 * s)
    draw.polygon([(bx, by + bh), (bx + bw, by + bh), (bx + bw, by + int(bh * 0.35)), (bx + bw // 2, by), (bx, by + int(bh * 0.35))], fill=_rgba(WHITE, 0.95), outline=_rgba(INK, 0.4), width=2)
    draw.rectangle([bx + int(bw * 0.38), by + int(bh * 0.15), bx + int(bw * 0.62), by + bh], fill=_rgba(BLUE_LIGHT, 0.55), outline=_rgba(INK, 0.25), width=2)
    draw.rounded_rectangle([bx + int(20 * s), by + int(bh * 0.55), bx + int(bw * 0.35), by + int(bh * 0.72)], radius=6, fill=_rgba(ACCENT, 0.85))
    draw.text((bx + int(32 * s), by + int(bh * 0.57)), "OUVERT", fill=WHITE, font=_font(max(11, int(14 * s)), bold=True))
    _draw_character(draw, bx + bw // 2, by + bh + int(30 * s), s * 0.95, shirt="#dbeafe", apron=True, hair="#5c4033")
    _draw_speech(draw, bx + int(bw + 20 * s), by + int(40 * s), int(200 * s), int(58 * s), "Artisan à Metz", s, tail="right")
    px, py = x0 + int(w * 0.72), y0 + int(100 * s)
    draw.ellipse([px, py, px + int(50 * s), py + int(50 * s)], fill=_rgba(ACCENT, 0.9), outline=_rgba(INK, 0.3), width=2)
    draw.polygon([(px + int(25 * s), py + int(58 * s)), (px + int(12 * s), py + int(42 * s)), (px + int(38 * s), py + int(42 * s))], fill=_rgba(ACCENT, 0.9))


def _scene_gallery(draw: ImageDraw.ImageDraw, img: Image.Image, box: tuple[int, int, int, int], s: float, accent: str) -> None:
    x0, y0, x1, y1 = box
    _draw_office_bg(draw, box, s)
    gap = int(16 * s)
    fw = int(200 * s)
    fh = int(150 * s)
    tints = (BLUE_LIGHT, "#e8c9a8", "#a8d4c4", BLUE_MID)
    for i in range(4):
        r, c = divmod(i, 2)
        fx = x0 + int(100 * s) + c * (fw + gap)
        fy = y0 + int(80 * s) + r * (fh + gap)
        _outline_rounded_rect(draw, (fx, fy, fx + fw, fy + fh), 10, WHITE, width=2)
        draw.rounded_rectangle([fx + 10, fy + 10, fx + fw - 10, fy + fh - 10], radius=6, fill=_rgba(tints[i], 0.6))
    _draw_character(draw, x0 + int(280 * s), y0 + int(380 * s), s * 1.0, shirt=PALE)
    _draw_character(draw, x0 + int(520 * s), y0 + int(375 * s), s * 1.0, shirt="#fef3c7", hair="#374151")
    hx = x0 + int(400 * s)
    draw.line([(x0 + int(330 * s), y0 + int(340 * s)), (hx, y0 + int(310 * s))], fill=_rgba(INK, 0.35), width=3)
    draw.line([(x0 + int(470 * s), y0 + int(340 * s)), (hx, y0 + int(310 * s))], fill=_rgba(INK, 0.35), width=3)
    _draw_speech(draw, x0 + int(600 * s), y0 + int(360 * s), int(220 * s), int(58 * s), "Beau travail !", s, tail="right")


def _scene_code(draw: ImageDraw.ImageDraw, img: Image.Image, box: tuple[int, int, int, int], s: float, accent: str) -> None:
    x0, y0, x1, y1 = box
    _draw_office_bg(draw, box, s)
    tx, ty = x0 + int(280 * s), y0 + int(100 * s)
    tw, th = int(520 * s), int(320 * s)
    _outline_rounded_rect(draw, (tx, ty, tx + tw, ty + th), 14, INK, width=2, fill_alpha=0.92)
    draw.rounded_rectangle([tx, ty, tx + tw, ty + 32], radius=14, fill=_rgba(BLUE_DARK, 0.95))
    for i, c in enumerate(("#ff5f57", "#febc2e", "#28c840")):
        draw.ellipse([tx + 14 + i * 20, ty + 9, tx + 24 + i * 20, ty + 19], fill=c)
    for i, line in enumerate(("const app = create();", "export { routes };", "// open source ✓")):
        draw.text((tx + 20, ty + 48 + i * 28), line, fill=_rgba(BLUE_LIGHT if i % 2 == 0 else PALE, 1), font=_font(max(12, int(16 * s))))
    _draw_character(draw, x0 + int(180 * s), y0 + int(280 * s), s * 1.05, shirt="#dbeafe", point=(tx + int(80 * s), ty + int(100 * s)), hair="#1e3a5f")
    _draw_speech(draw, x0 + int(820 * s), y0 + int(200 * s), int(200 * s), int(58 * s), "Publié sur GitHub", s, tail="right")


def _scene_stats(draw: ImageDraw.ImageDraw, img: Image.Image, box: tuple[int, int, int, int], s: float, accent: str) -> None:
    x0, y0, x1, y1 = box
    _draw_office_bg(draw, box, s)
    cx, cy = x0 + int(200 * s), y0 + int(120 * s)
    cw, ch = int(520 * s), int(280 * s)
    _outline_rounded_rect(draw, (cx, cy, cx + cw, cy + ch), 14, WHITE, width=2)
    bars = (0.4, 0.58, 0.78, 0.95)
    vals = ("12+", "8", "15 ans", "100%")
    bw = cw // (len(bars) * 2 + 1)
    for i, (frac, val) in enumerate(zip(bars, vals)):
        bx = cx + bw + i * (bw * 2)
        bh = int(ch * frac * 0.7)
        by = cy + ch - bh - 24
        col = (BLUE_LIGHT, BLUE_MID, BLUE_DARK, ACCENT)[i]
        draw.rounded_rectangle([bx, by, bx + bw, cy + ch - 24], radius=6, fill=_rgba(col, 0.8), outline=_rgba(INK, 0.15), width=1)
        draw.text((bx, by - int(22 * s)), val, fill=_rgba(INK, 1), font=_font(max(12, int(16 * s)), bold=True))
    _draw_character(draw, x0 + int(780 * s), y0 + int(300 * s), s * 1.0, shirt="#fef3c7")
    _draw_character(draw, x0 + int(920 * s), y0 + int(295 * s), s * 0.95, shirt=PALE, hair="#374151")
    _draw_speech(draw, x0 + int(720 * s), y0 + int(180 * s), int(240 * s), int(58 * s), "Des résultats concrets", s, tail="right")


def _scene_report(draw: ImageDraw.ImageDraw, img: Image.Image, box: tuple[int, int, int, int], s: float, accent: str) -> None:
    x0, y0, x1, y1 = box
    _draw_office_bg(draw, box, s)
    rx, ry = x0 + int(350 * s), y0 + int(110 * s)
    rw, rh = int(380 * s), int(300 * s)
    _outline_rounded_rect(draw, (rx, ry, rx + rw, ry + rh), 12, WHITE, width=2)
    for i in range(6):
        draw.rounded_rectangle([rx + 18, ry + 20 + i * int(36 * s), rx + rw - 18, ry + 28 + i * int(36 * s)], radius=4, fill=_rgba(BLUE_MID if i == 0 else PALE, 0.45 if i else 0.85))
    _draw_character(draw, x0 + int(200 * s), y0 + int(280 * s), s * 1.0, shirt=PALE, point=(rx + int(60 * s), ry + int(80 * s)))
    _draw_character(draw, x0 + int(820 * s), y0 + int(275 * s), s * 0.98, shirt="#e0e7ff", hair="#4b5563")
    _draw_speech(draw, x0 + int(130 * s), y0 + int(130 * s), int(220 * s), int(58 * s), "Voici votre rapport", s)
    gr = int(50 * s)
    gx, gy = rx + rw - int(40 * s), ry - int(20 * s)
    draw.arc([gx, gy, gx + gr * 2, gy + gr * 2], 200, 340, fill=_rgba(ACCENT, 0.9), width=5)


def _scene_mail(draw: ImageDraw.ImageDraw, img: Image.Image, box: tuple[int, int, int, int], s: float, accent: str) -> None:
    x0, y0, x1, y1 = box
    _draw_office_bg(draw, box, s)
    _draw_character(draw, x0 + int(500 * s), y0 + int(280 * s), s * 1.05, shirt="#dbeafe", point=(x0 + int(700 * s), y0 + int(200 * s)))
    _draw_phone(draw, x0 + int(640 * s), y0 + int(140 * s), int(100 * s), int(180 * s))
    ex, ey = x0 + int(200 * s), y0 + int(150 * s)
    ew, eh = int(280 * s), int(180 * s)
    _outline_rounded_rect(draw, (ex, ey, ex + ew, ey + eh), 12, WHITE, width=2)
    draw.polygon([(ex, ey), (ex + ew, ey), (ex + ew // 2, ey + eh // 2)], fill=_rgba(BLUE_LIGHT, 0.4))
    _draw_speech(draw, x0 + int(720 * s), y0 + int(120 * s), int(240 * s), int(58 * s), "Plus de relances", s, tail="right")


def _scene_legal(draw: ImageDraw.ImageDraw, img: Image.Image, box: tuple[int, int, int, int], s: float, accent: str) -> None:
    x0, y0, x1, y1 = box
    _draw_office_bg(draw, box, s)
    sx, sy = x0 + int(400 * s), y0 + int(100 * s)
    sw, sh = int(320 * s), int(360 * s)
    _outline_rounded_rect(draw, (sx, sy, sx + sw, sy + sh), 8, "#fffef8", width=2)
    for i in range(8):
        draw.rounded_rectangle([sx + 16, sy + 18 + i * int(34 * s), sx + sw - 16, sy + 26 + i * int(34 * s)], radius=3, fill=_rgba(PALE, 0.85))
    _draw_character(draw, x0 + int(250 * s), y0 + int(300 * s), s * 1.0, shirt=PALE)
    _draw_character(draw, x0 + int(780 * s), y0 + int(295 * s), s * 0.95, shirt="#e0e7ff")


def _scene_assistant(draw: ImageDraw.ImageDraw, img: Image.Image, box: tuple[int, int, int, int], s: float, accent: str) -> None:
    x0, y0, x1, y1 = box
    _draw_office_bg(draw, box, s)
    _draw_browser(draw, x0 + int(280 * s), y0 + int(90 * s), int(500 * s), int(280 * s))
    bx, by = x0 + int(520 * s), y0 + int(200 * s)
    _outline_rounded_rect(draw, (bx, by, bx + int(280 * s), by + int(100 * s)), 16, WHITE, width=2)
    draw.ellipse([bx + 14, by + 14, bx + 54, by + 54], fill=_rgba(BLUE_MID, 0.5))
    draw.text((bx + 62, by + 22), "Bonjour ! Je peux aider", fill=_rgba(INK, 0.85), font=_font(max(12, int(15 * s)), bold=True))
    _draw_character(draw, x0 + int(200 * s), y0 + int(300 * s), s * 1.0, shirt="#fef3c7", point=(bx + 30, by + 30))
    _draw_speech(draw, x0 + int(140 * s), y0 + int(150 * s), int(200 * s), int(58 * s), "Une question ?", s)


def _scene_brand(draw: ImageDraw.ImageDraw, img: Image.Image, box: tuple[int, int, int, int], s: float, accent: str) -> None:
    x0, y0, x1, y1 = box
    _draw_office_bg(draw, box, s)
    px, py = x0 + int(420 * s), y0 + int(130 * s)
    draw.ellipse([px, py, px + int(120 * s), py + int(120 * s)], fill=_rgba(BLUE_MID, 0.4), outline=_rgba(INK, 0.35), width=3)
    draw.ellipse([px + int(40 * s), py + int(40 * s), px + int(80 * s), py + int(80 * s)], fill=_rgba(ACCENT, 0.8))
    _draw_character(draw, x0 + int(220 * s), y0 + int(290 * s), s * 1.0, shirt=PALE, point=(px + int(60 * s), py + int(60 * s)))
    _draw_character(draw, x0 + int(780 * s), y0 + int(285 * s), s * 0.98, shirt="#fef3c7", hair="#374151")
    _draw_speech(draw, x0 + int(600 * s), y0 + int(160 * s), int(240 * s), int(58 * s), "Mon identité visuelle", s, tail="right")


def _scene_gear(draw: ImageDraw.ImageDraw, img: Image.Image, box: tuple[int, int, int, int], s: float, accent: str) -> None:
    x0, y0, x1, y1 = box
    _draw_office_bg(draw, box, s)
    _draw_browser(draw, x0 + int(350 * s), y0 + int(100 * s), int(420 * s), int(260 * s))
    cx, cy = x0 + int(200 * s), y0 + int(220 * s)
    r = int(50 * s)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=_rgba(WHITE, 0.95), outline=_rgba(INK, 0.4), width=3)
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        draw.line([(cx + int((r + 10 * s) * math.cos(rad)), cy + int((r + 10 * s) * math.sin(rad))), (cx + int((r + 28 * s) * math.cos(rad)), cy + int((r + 28 * s) * math.sin(rad)))], fill=_rgba(BLUE_DARK, 0.6), width=4)
    _draw_character(draw, x0 + int(780 * s), y0 + int(290 * s), s * 1.0, shirt="#dbeafe", point=(x0 + int(450 * s), y0 + int(180 * s)))


def _scene_visibilite(draw: ImageDraw.ImageDraw, img: Image.Image, box: tuple[int, int, int, int], s: float, accent: str) -> None:
    x0, y0, x1, y1 = box
    _draw_shop_interior(draw, box, s)
    _draw_phone(draw, x0 + int(480 * s), y0 + int(140 * s), int(110 * s), int(200 * s))
    draw.rounded_rectangle([x0 + int(500 * s), y0 + int(170 * s), x0 + int(660 * s), y0 + int(210 * s)], radius=14, fill=_rgba(WHITE, 0.95), outline=_rgba(BLUE_MID, 0.5), width=2)
    draw.ellipse([x0 + int(512 * s), y0 + int(178 * s), x0 + int(536 * s), y0 + int(202 * s)], fill=_rgba(BLUE_MID, 0.5))
    for i, frac in enumerate((0.85, 0.7, 0.55)):
        draw.rounded_rectangle([x0 + int(544 * s), y0 + int(178 + i * 12 * s), x0 + int(544 + 100 * frac * s), y0 + int(186 + i * 12 * s)], radius=3, fill=_rgba(PALE, 0.95))
    _draw_character(draw, x0 + int(300 * s), y0 + int(280 * s), s * 1.05, shirt="#fef3c7", apron=True, point=(x0 + int(540 * s), y0 + int(200 * s)))
    _draw_speech(draw, x0 + int(620 * s), y0 + int(100 * s), int(260 * s), int(58 * s), "Je suis sur Google !", s, tail="right")


def _scene_mobile(draw: ImageDraw.ImageDraw, img: Image.Image, box: tuple[int, int, int, int], s: float, accent: str) -> None:
    x0, y0, x1, y1 = box
    _draw_office_bg(draw, box, s)
    _draw_phone(draw, x0 + int(440 * s), y0 + int(100 * s), int(140 * s), int(260 * s))
    _draw_character(draw, x0 + int(280 * s), y0 + int(290 * s), s * 1.05, shirt="#dbeafe", point=(x0 + int(500 * s), y0 + int(200 * s)))
    _draw_character(draw, x0 + int(780 * s), y0 + int(285 * s), s * 0.95, shirt="#e0e7ff")
    _draw_speech(draw, x0 + int(620 * s), y0 + int(120 * s), int(220 * s), int(58 * s), "Mon app mobile", s, tail="right")


def _scene_browser(draw: ImageDraw.ImageDraw, img: Image.Image, box: tuple[int, int, int, int], s: float, accent: str) -> None:
    x0, y0, x1, y1 = box
    _draw_shop_interior(draw, box, s)
    bx, by = x0 + int(320 * s), y0 + int(120 * s)
    _draw_browser(draw, bx, by, int(480 * s), int(300 * s), cta=True)
    _draw_character(draw, x0 + int(220 * s), y0 + int(300 * s), s * 1.05, shirt=PALE, point=(bx + int(100 * s), by + int(80 * s)))
    _draw_character(draw, x0 + int(850 * s), y0 + int(295 * s), s * 0.95, shirt="#fef3c7")


def _draw_sparkles(draw: ImageDraw.ImageDraw, x: int, y: int, s: float, color: str = BLUE_LIGHT) -> None:
    for dx, dy, r in ((0, 0, 8), (22 * s, -10 * s, 5), (-18 * s, 14 * s, 6)):
        cx, cy = int(x + dx), int(y + dy)
        rr = max(3, int(r * s))
        draw.line([(cx - rr, cy), (cx + rr, cy)], fill=_rgba(color, 0.75), width=3)
        draw.line([(cx, cy - rr), (cx, cy + rr)], fill=_rgba(color, 0.75), width=3)


SCENES: dict[str, ScenePainter] = {
    "hero": _scene_hero,
    "audit": _scene_audit,
    "catalog": _scene_catalog,
    "templates": _scene_templates,
    "process": _scene_process,
    "local": _scene_local,
    "gallery": _scene_gallery,
    "code": _scene_code,
    "stats": _scene_stats,
    "report": _scene_report,
    "mail": _scene_mail,
    "legal": _scene_legal,
    "assistant": _scene_assistant,
    "brand": _scene_brand,
    "gear": _scene_gear,
    "visibilite": _scene_visibilite,
    "mobile": _scene_mobile,
    "browser": _scene_browser,
}

STATIC_SCENES = {
    "home": "hero",
    "audit": "audit",
    "prestations": "catalog",
    "vitrines": "templates",
    "processus": "process",
    "metz": "local",
    "portfolio": "gallery",
    "projets": "code",
    "statistiques": "stats",
    "analyse": "report",
    "desabonnement": "mail",
    "mentions-legales": "legal",
    "cgv": "legal",
    "cgu": "legal",
    "politique-confidentialite": "legal",
}

PRESTATION_SCENES = {
    "identite": "brand",
    "ia": "assistant",
    "technique": "gear",
    "site-contenu": "browser",
    "maintenance": "gear",
}

PROJECT_SCENES = {
    "web": "browser",
    "tools": "gear",
    "mobile": "mobile",
    "iot": "gear",
    "specialized": "code",
    "learning": "catalog",
    "desktop": "code",
}


def _draw_text_overlay(
    draw: ImageDraw.ImageDraw,
    w: int,
    h: int,
    scale: float,
    *,
    title: str,
    badge: str,
    hook: str,
    cta: str,
    color: str,
) -> None:
    """Texte en bandeau bas — lisible sur scène plein cadre."""
    pad = int(44 * scale)
    bottom_safe = h - int(TWITTER_BOTTOM_RESERVE * scale)
    max_w = w - 2 * pad

    font_badge = _font(max(13, int(20 * scale)), bold=True)
    badge_text = badge[:18]
    badge_w = int(draw.textlength(badge_text, font=font_badge) + 24 * scale)
    badge_h = int(36 * scale)
    by = bottom_safe - int(175 * scale)
    draw.rounded_rectangle([pad, by, pad + badge_w, by + badge_h], radius=int(12 * scale), fill=_rgba(color, 0.92), outline=_rgba(WHITE, 0.35), width=1)
    draw.text((pad + int(12 * scale), by + int(7 * scale)), badge_text, fill=WHITE, font=font_badge)

    ty = by + badge_h + int(10 * scale)
    for pt in (int(52 * scale), int(46 * scale), int(40 * scale)):
        font_title = _font(max(26, pt), bold=True)
        lines = _wrap_lines(draw, title.strip(), font_title, max_w, 2)
        if len(lines) <= 2:
            break
    for line in lines:
        draw.text((pad, ty), line, fill=TEXT_ON_SCRIM, font=font_title)
        ty += int(50 * scale)

    if hook:
        font_hook = _font(max(14, int(22 * scale)))
        draw.text((pad, ty + int(4 * scale)), hook[:70], fill=TEXT_MUTED_SCRIM, font=font_hook)
        ty += int(30 * scale)

    if cta:
        font_cta = _font(max(13, int(19 * scale)), bold=True)
        label = cta[:28]
        tw = int(draw.textlength(label, font=font_cta) + 30 * scale)
        th = int(40 * scale)
        cta_y = min(ty + int(8 * scale), bottom_safe - th - int(8 * scale))
        draw.rounded_rectangle([pad, cta_y, pad + tw, cta_y + th], radius=int(20 * scale), fill=_rgba(ACCENT, 0.95), outline=_rgba(WHITE, 0.3), width=1)
        draw.text((pad + int(15 * scale), cta_y + int(9 * scale)), label, fill=WHITE, font=font_cta)

    domain_font = _font(max(11, int(16 * scale)), bold=True)
    draw.text((w - pad - int(draw.textlength(BRAND_DOMAIN, font=domain_font)), bottom_safe - int(28 * scale)), BRAND_DOMAIN, fill=_rgba(BLUE_LIGHT, 0.85), font=domain_font)


def render_og_card(
    *,
    title: str,
    subtitle: str = "",
    badge: str = "DanielCraft",
    color: str = BLUE_MID,
    chips: Sequence[str] | None = None,
    footer: str = "DanielCraft — Metz & Lorraine",
    scene: str = "browser",
    cta: str = "En savoir plus →",
    width: int = OG_W,
    height: int = OG_H,
) -> Image.Image:
    """Carte OG 1200×630 : scène BD plein cadre + texte en surimpression."""
    scale = width / OG_W
    img = _sky_gradient(width, height).convert("RGBA")
    draw = ImageDraw.Draw(img)

    full_box = (0, 0, width, height)
    painter = SCENES.get(scene, _scene_browser)
    painter(draw, img, full_box, scale, color)

    _draw_bottom_scrim(img)
    draw = ImageDraw.Draw(img)
    _draw_brand_watermark(draw, img, scale)
    _draw_text_overlay(
        draw, width, height, scale,
        title=title,
        badge=badge,
        hook=_social_hook(subtitle),
        cta=cta,
        color=color,
    )
    return img.convert("RGB")
