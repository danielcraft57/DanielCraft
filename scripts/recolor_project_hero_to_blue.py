#!/usr/bin/env python3
# Recolorise fortement vers le bleu. Pour atténuer ensuite : reduce_blue_cast.py,
# apply_complementary_grades.py ou portfolio_image_pipeline.py (voir README_IMAGES.md).
from pathlib import Path
from PIL import Image, ImageChops


ROOT = Path(__file__).resolve().parents[1]
TARGET_DIRS = [
    ROOT / "assets" / "images" / "projets",
    ROOT / "assets" / "images" / "hero",
]
EXTS = {".png", ".jpg", ".jpeg", ".webp"}


def recolor_blue_metal(img: Image.Image) -> Image.Image:
    rgba = img.convert("RGBA")
    alpha = rgba.split()[3]
    rgb = rgba.convert("RGB")

    hsv = rgb.convert("HSV")
    h, s, v = hsv.split()

    # Cible les tons rouges/oranges vers un bleu métal.
    warm_hue_mask = h.point(lambda x: 255 if (x <= 32 or x >= 230) else 0, mode="L")
    sat_mask = s.point(lambda x: 255 if x >= 38 else 0, mode="L")
    val_mask = v.point(lambda x: 255 if x >= 28 else 0, mode="L")
    mask = ImageChops.multiply(warm_hue_mask, sat_mask)
    mask = ImageChops.multiply(mask, val_mask)

    target_h = Image.new("L", rgb.size, color=145)  # bleu/cyan
    softened_s = s.point(lambda x: min(255, int(x * 0.82 + 18)), mode="L")
    brightened_v = v.point(lambda x: min(255, int(x * 1.02 + 4)), mode="L")

    new_h = Image.composite(target_h, h, mask)
    new_s = Image.composite(softened_s, s, mask)
    new_v = Image.composite(brightened_v, v, mask)

    recolored_rgb = Image.merge("HSV", (new_h, new_s, new_v)).convert("RGB")

    # Léger refroidissement global pour uniformiser le rendu.
    r, g, b = recolored_rgb.split()
    r = r.point(lambda x: max(0, int(x * 0.95)))
    g = g.point(lambda x: min(255, int(x * 1.01)))
    b = b.point(lambda x: min(255, int(x * 1.08 + 4)))
    cooled = Image.merge("RGB", (r, g, b))

    return Image.merge("RGBA", (*cooled.split(), alpha))


def save_image(path: Path, out: Image.Image) -> None:
    suffix = path.suffix.lower()
    if suffix in {".jpg", ".jpeg"}:
        out.convert("RGB").save(path, quality=92, optimize=True)
    elif suffix == ".webp":
        out.save(path, "WEBP", quality=90, method=6)
    else:
        out.save(path, optimize=True)


def main() -> None:
    changed = []
    for d in TARGET_DIRS:
        if not d.exists():
            continue
        for p in d.iterdir():
            if not p.is_file() or p.suffix.lower() not in EXTS:
                continue
            try:
                with Image.open(p) as img:
                    out = recolor_blue_metal(img)
                    save_image(p, out)
                    changed.append(p.relative_to(ROOT).as_posix())
            except Exception as e:
                print(f"[WARN] Echec {p.name}: {e}")

    print(f"[DONE] Images recolorisees: {len(changed)}")
    for c in changed:
        print(c)


if __name__ == "__main__":
    main()
