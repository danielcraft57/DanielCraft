#!/usr/bin/env python3
"""Inject slug/entity into block_site_nav and block_site_footer in all _shell_*."""
import re
from pathlib import Path

p = Path(__file__).resolve().parent / "build_vitrine_site.py"
text = p.read_text(encoding="utf-8")

shells = [
    ("_shell", "restauration"),
    ("_shell_beaute", "beaute"),
    ("_shell_odontologie", "odontologie"),
    ("_shell_automobile", "automobile"),
    ("_shell_commerce", "commerce"),
    ("_shell_comptable", "comptable"),
    ("_shell_industrie", "industrie"),
    ("_shell_immobilier", "immobilier"),
    ("_shell_juridique", "juridique"),
    ("_shell_architecture", "architecture"),
    ("_shell_fitness", "fitness"),
    ("_shell_photo", "photographie"),
    ("_shell_association", "association"),
    ("_shell_education", "education"),
    ("_shell_services", "services"),
    ("_shell_etablissement", "etablissement"),
    ("_shell_technologie", "technologie"),
    ("_shell_saas_landing", "saas-landing"),
    ("_shell_saas_onboarding", "saas-onboarding"),
    ("_shell_saas_dashboard", "saas-dashboard"),
    ("_shell_saas_empty", "saas-empty"),
    ("_shell_saas_notifications", "saas-notifications"),
]

import_line = "from vitrine_seo import get_entity\n"
helpers = '''

def _chrome_nav(slug: str, brand: str, nav: list, page: str, *, cta_label: str, cta_href: str) -> str:
    return block_site_nav(brand, nav, page, cta_label=cta_label, cta_href=cta_href, slug=slug)


def _chrome_foot(slug: str, brand: str, **kwargs) -> str:
    return block_site_footer(brand, entity=get_entity(slug), slug=slug, **kwargs)

'''

if "def _chrome_nav" not in text:
    anchor = "sys.path.insert(0, str(Path(__file__).resolve().parent))\n\n"
    text = text.replace(anchor, anchor + import_line + helpers)

for shell_fn, slug in shells:
    pat = rf"(def {shell_fn}\([^)]*\) -> str:.*?)(?=\ndef |\Z)"
    m = re.search(pat, text, re.DOTALL)
    if not m:
        print(f"SKIP {shell_fn}")
        continue
    block = m.group(1)
    new_block = block.replace("block_site_nav(", f'_chrome_nav("{slug}", ')
    new_block = new_block.replace("block_site_footer(", f'_chrome_foot("{slug}", ')
    if new_block == block:
        print(f"NO CHANGE {shell_fn}")
    else:
        text = text[: m.start(1)] + new_block + text[m.end(1) :]
        print(f"OK {shell_fn}")

p.write_text(text, encoding="utf-8")
print("Done.")
