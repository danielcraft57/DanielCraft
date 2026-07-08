#!/usr/bin/env python3
"""One-shot patch: refactor wrap_page_* to use _wrap_vitrine_page."""
import re
from pathlib import Path

p = Path(__file__).resolve().parent / "vitrine_site_blocks.py"
text = p.read_text(encoding="utf-8")

replacements = [
    ("wrap_page_retail", "HEAD_RETAIL", "vt-body vt-body-retail", "commerce", "retail-editorial"),
    ("wrap_page_cabinet", "HEAD_CABINET", "vt-body vt-body-cabinet", "comptable", "cabinet-proof"),
    ("wrap_page_industrial", "HEAD_INDUSTRIAL", "vt-body vt-body-industrial", "industrie", "industrial-spec"),
    ("wrap_page_property", "HEAD_PROPERTY", "vt-body vt-body-property", "immobilier", "property-search"),
    ("wrap_page_legal", "HEAD_LEGAL", "vt-body vt-body-legal", "juridique", "legal-overlay"),
    ("wrap_page_architecture", "HEAD_ARCHITECTURE", "vt-body vt-body-architecture", "architecture", "architecture-editorial"),
    ("wrap_page_hotel", "HEAD_HOTEL", "vt-body vt-body-hotel", "etablissement", "hotel-luxury"),
    ("wrap_page_tech", "HEAD_TECH", "vt-body vt-body-tech", "technologie", "tech-data"),
    ("wrap_page_facility", "HEAD_FACILITY", "vt-body vt-body-facility", "services", "facility-fm"),
    ("wrap_page_education", "HEAD_EDUCATION", "vt-body vt-body-education", "education", "campus-academic"),
    ("wrap_page_association", "HEAD_ASSOCIATION", "vt-body vt-body-association", "association", "ess-impact"),
    ("wrap_page_photo", "HEAD_PHOTO", "vt-body vt-body-photo", "photographie", "photo-masonry"),
    ("wrap_page_fitness", "HEAD_FITNESS", "vt-body vt-body-fitness", "fitness", "fitness-schedule"),
]

for fn, head, body_class, slug, layout in replacements:
    pat = rf"def {fn}\(title: str, description: str, body: str, \*, layout: str = [^)]+\) -> str:\n    return f\"\"\"<!DOCTYPE html>.*?\"\"\"\n"
    new = f'''def {fn}(
    title: str,
    description: str,
    body: str,
    *,
    layout: str = "{layout}",
    slug: str = "{slug}",
    page: str = "index.html",
    site_name: str = "",
    nav: list[dict] | None = None,
    og_image: str = "images/hero.webp",
) -> str:
    return _wrap_vitrine_page(
        title, description, body,
        head_assets={head}, body_class="{body_class}", layout=layout,
        entity_slug=slug, page=page, site_name=site_name, nav=nav, og_image=og_image,
    )


'''
    text, n = re.subn(pat, new, text, count=1, flags=re.S)
    print(f"{fn}: {n}")

pat = r'def wrap_page_saas\(title: str, description: str, body: str, \*, layout: str = [^)]+\) -> str:\n    return f"""<!DOCTYPE html>.*?"""\n'
new = '''def wrap_page_saas(
    title: str,
    description: str,
    body: str,
    *,
    layout: str = "saas-product",
    slug: str = "saas-landing",
    page: str = "index.html",
    site_name: str = "",
    nav: list[dict] | None = None,
    og_image: str = "images/hero.webp",
    brand: str = "FlowMetrics",
    brand_desc: str = "SaaS analytics pour equipes produit",
) -> str:
    return _wrap_vitrine_page(
        title, description, body,
        head_assets=HEAD_SAAS, body_class="vt-body vt-body-saas", layout=layout,
        entity_slug=slug, page=page, site_name=site_name or brand, nav=nav, og_image=og_image,
        entity_overrides={"name": brand, "description": brand_desc},
    )


'''
text, n = re.subn(pat, new, text, count=1, flags=re.S)
print(f"wrap_page_saas: {n}")

p.write_text(text, encoding="utf-8")
print("OK")
