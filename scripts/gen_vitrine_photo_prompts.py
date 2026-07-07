#!/usr/bin/env python3
"""Exporte les prompts photo pour les vitrines.

Sources :
  - scripts/data/vitrine_photos/<slug>.json  (prompts enrichis par vitrine, prioritaire)
  - vitrine_scenarios.image_specs()          (labels agrégés multi-pages, fallback)

Sortie : scripts/data/vitrine_photo_prompts.json (manifeste global pour install_vitrine_photo.py)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from vitrine_scenarios import image_specs

ROOT = Path(__file__).resolve().parents[1]
PHOTOS_DIR = ROOT / "scripts" / "data" / "vitrine_photos"
OUT = ROOT / "scripts" / "data" / "vitrine_photo_prompts.json"

STYLE = {
    "hero": "Professional commercial photography, widescreen 21:9 hero banner, warm natural lighting, photorealistic, shallow depth of field, no text, no watermark, no logos",
    "food": "Gourmet food photography, appetizing, warm ambient light, photorealistic, no text, no watermark",
    "spa": "Luxury spa and beauty photography, soft lighting, serene atmosphere, photorealistic, no text, no watermark",
    "medical": "Modern medical clinic photography, clean bright interior, reassuring atmosphere, photorealistic, no text, no watermark",
    "garage": "Automotive workshop photography, professional garage, natural light, photorealistic, no text, no watermark",
    "retail": "Modern retail store photography, bright aisle, welcoming atmosphere, photorealistic, no text, no watermark",
    "office": "Professional office photography, modern workspace, natural light, photorealistic, no text, no watermark",
    "industrial": "Industrial manufacturing photography, precision machinery, professional, photorealistic, no text, no watermark",
    "property": "Real estate photography, elegant property exterior or interior, golden hour light, photorealistic, no text, no watermark",
    "legal": "Prestigious law firm office photography, wood and leather, professional, photorealistic, no text, no watermark",
    "architecture": "Architectural photography, contemporary building or studio, dramatic light, photorealistic, no text, no watermark",
    "sport": "Fitness gym photography, energetic atmosphere, modern equipment, photorealistic, no text, no watermark",
    "photo": "Fine art photography studio, creative workspace, dramatic lighting, photorealistic, no text, no watermark",
    "team": "Community association photography, volunteers helping, warm authentic moment, photorealistic, no text, no watermark",
    "interior": "Interior design photography, elegant space, natural light, photorealistic, no text, no watermark",
    "saas_ui": "Modern SaaS software UI mockup screenshot, clean dashboard interface, professional product design, dark or light theme, no readable text, no watermark",
    "gallery": "Lifestyle photography, candid authentic moment, natural light, photorealistic, no text, no watermark",
    "card": "Detail shot photography, focused subject, clean composition, photorealistic, no text, no watermark",
    "detail": "Close-up detail photography, professional, photorealistic, no text, no watermark",
    "product": "Product photography, clean background, professional lighting, photorealistic, no text, no watermark",
}


def load_slug_manifests() -> dict[str, dict]:
    manifests: dict[str, dict] = {}
    if not PHOTOS_DIR.is_dir():
        return manifests
    for path in sorted(PHOTOS_DIR.glob("*.json")):
        if path.name.startswith("_"):
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        slug = data.get("slug") or path.stem
        by_file: dict[str, dict] = {}
        for img in data.get("images", []):
            fn = img.get("filename")
            if fn:
                by_file[fn] = img
        manifests[slug] = {
            "meta": data,
            "by_file": by_file,
        }
    return manifests


def build_prompt(label: str, scene: str, style_suffix: str = "") -> str:
    style = STYLE.get(scene, STYLE["interior"])
    if style_suffix:
        return f"{label}. {style_suffix}"
    return f"{label}. {style}"


def build_prompt_for(
    slug: str,
    filename: str,
    label: str,
    scene: str,
    category: str,
    manifests: dict[str, dict],
) -> tuple[str, list]:
    manifest = manifests.get(slug)
    if manifest:
        img = manifest["by_file"].get(filename)
        if img:
            meta = manifest["meta"]
            style_suffix = meta.get("style_suffix") or ""
            subject = img.get("subject") or label
            contexts = img.get("contexts") or []
            ctx_texts = [c.get("text", "") for c in contexts if c.get("text")]
            if style_suffix:
                return f"{subject}. {style_suffix}", ctx_texts
            style = STYLE.get(scene, STYLE["interior"])
            return f"{subject}. {style}", ctx_texts

    ctx_fallback = [p.strip() for p in label.split(". ") if p.strip()]
    return build_prompt(label, scene), ctx_fallback


def main() -> None:
    manifests = load_slug_manifests()
    specs = image_specs()
    items = []
    for slug, filename, label, scene, category in specs:
        manifest = manifests.get(slug)
        img_override = manifest["by_file"].get(filename) if manifest else None
        w = img_override.get("width") if img_override else (1200 if filename == "hero.png" else 800)
        h = img_override.get("height") if img_override else 520
        prompt, contexts = build_prompt_for(slug, filename, label, scene, category, manifests)
        alt = img_override.get("alt") if img_override else (contexts[0] if contexts else label)
        entry = {
            "slug": slug,
            "filename": filename,
            "label": label,
            "alt": alt,
            "scene": img_override.get("scene", scene) if img_override else scene,
            "category": category,
            "width": w,
            "height": h,
            "prompt": prompt,
            "contexts": contexts,
            "dest": f"assets/vitrines/demos/{slug}/images/{filename}",
        }
        if manifest and filename in manifest["by_file"]:
            entry["photo_manifest"] = f"scripts/data/vitrine_photos/{slug}.json"
        items.append(entry)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
    custom = sum(1 for i in items if "photo_manifest" in i)
    print(f"[OK] {len(items)} prompts -> {OUT.relative_to(ROOT)} ({custom} depuis vitrine_photos/)")


if __name__ == "__main__":
    main()
