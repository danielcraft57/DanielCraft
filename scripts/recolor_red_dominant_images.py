#!/usr/bin/env python3
# Rouge dominant → bleu. Voir aussi README_IMAGES.md (pipeline complémentaires).
from pathlib import Path
from PIL import Image, ImageChops


ROOT = Path(__file__).resolve().parents[1]
IMAGES_DIR = ROOT / "assets" / "images"
EXTS = {".png", ".jpg", ".jpeg", ".webp"}


def is_red_dominant(rgb_img: Image.Image) -> bool:
    hsv = rgb_img.convert("HSV")
    h, s, v = hsv.split()

    # Rouge / orange chaud en HSV Pillow (0..255)
    red_hue_mask = h.point(lambda x: 255 if (x <= 24 or x >= 235) else 0, mode="L")
    sat_mask = s.point(lambda x: 255 if x >= 70 else 0, mode="L")
    val_mask = v.point(lambda x: 255 if x >= 45 else 0, mode="L")

    mask = ImageChops.multiply(red_hue_mask, sat_mask)
    mask = ImageChops.multiply(mask, val_mask)

    hot_pixels = sum(mask.histogram()[1:])
    total_pixels = rgb_img.size[0] * rgb_img.size[1]
    if total_pixels == 0:
        return False
    ratio = hot_pixels / total_pixels
    return ratio >= 0.06


def recolor_to_blue_metal(rgba_img: Image.Image) -> Image.Image:
    rgb = rgba_img.convert("RGB")
    alpha = rgba_img.split()[3]

    hsv = rgb.convert("HSV")
    h, s, v = hsv.split()

    red_hue_mask = h.point(lambda x: 255 if (x <= 28 or x >= 232) else 0, mode="L")
    sat_mask = s.point(lambda x: 255 if x >= 60 else 0, mode="L")
    val_mask = v.point(lambda x: 255 if x >= 40 else 0, mode="L")

    mask = ImageChops.multiply(red_hue_mask, sat_mask)
    mask = ImageChops.multiply(mask, val_mask)

    # Hue cible bleu métal (en HSV Pillow)
    target_h = Image.new("L", rgb.size, color=145)
    # Saturation légèrement adoucie pour rester pastel
    softened_s = s.point(lambda x: min(255, int(x * 0.78 + 22)), mode="L")

    new_h = Image.composite(target_h, h, mask)
    new_s = Image.composite(softened_s, s, mask)

    recolored_rgb = Image.merge("HSV", (new_h, new_s, v)).convert("RGB")
    return Image.merge("RGBA", (*recolored_rgb.split(), alpha))


def process_image(path: Path) -> bool:
    try:
        with Image.open(path) as img:
            rgba = img.convert("RGBA")
            rgb = rgba.convert("RGB")
            if not is_red_dominant(rgb):
                return False

            out = recolor_to_blue_metal(rgba)
            suffix = path.suffix.lower()
            if suffix in {".jpg", ".jpeg"}:
                out.convert("RGB").save(path, quality=92, optimize=True)
            elif suffix == ".webp":
                out.save(path, "WEBP", quality=90, method=6)
            else:
                out.save(path, optimize=True)
            return True
    except Exception:
        return False


def main() -> None:
    changed = []
    for p in IMAGES_DIR.rglob("*"):
        if p.is_file() and p.suffix.lower() in EXTS:
            if process_image(p):
                changed.append(p.relative_to(ROOT))

    print(f"[DONE] Images recolorisees: {len(changed)}")
    for c in changed:
        print(c.as_posix())


if __name__ == "__main__":
    main()
