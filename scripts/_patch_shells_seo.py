#!/usr/bin/env python3
"""Patch _shell_* functions to pass SEO kwargs to wrap_page_*."""
import re
from pathlib import Path

p = Path(__file__).resolve().parent / "build_vitrine_site.py"
text = p.read_text(encoding="utf-8")

# (shell_fn, wrap_fn, slug, brand_var, nav_var)
shells = [
    ("_shell", "wrap_page", "restauration", "BRAND", "NAV"),
    ("_shell_beaute", "wrap_page_spa", "beaute", "B_Brand", "B_NAV"),
    ("_shell_odontologie", "wrap_page_medical", "odontologie", "O_BRAND", "O_NAV"),
    ("_shell_automobile", "wrap_page_garage", "automobile", "A_BRAND_FULL", "A_NAV"),
    ("_shell_commerce", "wrap_page_retail", "commerce", "C_BRAND", "C_NAV"),
    ("_shell_comptable", "wrap_page_cabinet", "comptable", "CP_BRAND", "CP_NAV"),
    ("_shell_industrie", "wrap_page_industrial", "industrie", "I_BRAND", "I_NAV"),
    ("_shell_immobilier", "wrap_page_property", "immobilier", "IM_BRAND", "IM_NAV"),
    ("_shell_juridique", "wrap_page_legal", "juridique", "JU_BRAND", "JU_NAV"),
    ("_shell_architecture", "wrap_page_architecture", "architecture", "AR_BRAND", "AR_NAV"),
    ("_shell_fitness", "wrap_page_fitness", "fitness", "FIT_BRAND", "FIT_NAV"),
    ("_shell_photo", "wrap_page_photo", "photographie", "PH_BRAND", "PH_NAV"),
    ("_shell_association", "wrap_page_association", "association", "ASS_BRAND", "ASS_NAV"),
    ("_shell_education", "wrap_page_education", "education", "EDU_BRAND", "EDU_NAV"),
    ("_shell_services", "wrap_page_facility", "services", "SV_BRAND", "SV_NAV"),
    ("_shell_etablissement", "wrap_page_hotel", "etablissement", "ET_BRAND", "ET_NAV"),
    ("_shell_technologie", "wrap_page_tech", "technologie", "TE_BRAND", "TE_NAV"),
    ("_shell_saas_landing", "wrap_page_saas", "saas-landing", "FM_BRAND", "FM_NAV"),
    ("_shell_saas_onboarding", "wrap_page_saas", "saas-onboarding", "TL_BRAND", "TL_NAV"),
    ("_shell_saas_dashboard", "wrap_page_saas", "saas-dashboard", "MD_BRAND", "MD_NAV"),
    ("_shell_saas_empty", "wrap_page_saas", "saas-empty", "QB_BRAND", "QB_NAV"),
    ("_shell_saas_notifications", "wrap_page_saas", "saas-notifications", "PF_BRAND", "PF_NAV"),
]

for shell_fn, wrap_fn, slug, brand, nav in shells:
    # Match: return wrap_page_*(title, desc, BODY_PART, ...)
    pat = rf"return {wrap_fn}\((title, desc, [^)]+)\)"
    extra = f'slug="{slug}", page=page, site_name={brand}, nav={nav}'
    if wrap_fn == "wrap_page_saas":
        # preserve existing kwargs after body
        pat = rf"return {wrap_fn}\((title, desc, [^,]+), layout=([^)]+)\)"
        def repl_saas(m):
            body_part = m.group(1).split(", ", 2)
            # title, desc, main+...
            prefix = f"return {wrap_fn}(title, desc, {m.group(1).split(', ', 2)[-1] if len(m.group(1).split(', ', 2))==3 else m.group(1)}"
            return None
        # simpler: find lines with return wrap_page_saas
        pass

# Simpler line-by-line approach for return wrap_page*(
lines = text.splitlines()
out = []
i = 0
while i < len(lines):
    line = lines[i]
    matched = False
    for shell_fn, wrap_fn, slug, brand, nav in shells:
        if f"return {wrap_fn}(" in line and "slug=" not in line:
            if wrap_fn == "wrap_page_saas":
                # e.g. return wrap_page_saas(title, desc, nav + main + foot + mobile, layout="saas-landing", brand=FM_BRAND, brand_desc="...")
                m = re.match(
                    rf'\s*return {wrap_fn}\((title, desc, .+?), layout="([^"]+)", brand=(\w+), brand_desc="([^"]*)"\)\s*$',
                    line,
                )
                if m:
                    body_expr = m.group(1).split(", ", 2)[2] if m.group(1).count(", ") >= 2 else m.group(1)
                    # reconstruct from full match
                    full = line.strip()
                    inner = full[len(f"return {wrap_fn}("):-1]
                    parts = []
                    depth = 0
                    cur = []
                    for ch in inner:
                        if ch == "(" :
                            depth += 1
                        elif ch == ")":
                            depth -= 1
                        if ch == "," and depth == 0:
                            parts.append("".join(cur).strip())
                            cur = []
                        else:
                            cur.append(ch)
                    if cur:
                        parts.append("".join(cur).strip())
                    # parts: title, desc, body, layout=..., brand=..., brand_desc=...
                    if len(parts) >= 3:
                        body = parts[2]
                        layout_kw = parts[3] if len(parts) > 3 else 'layout="saas-product"'
                        brand_kw = parts[4] if len(parts) > 4 else f"brand={brand}"
                        desc_kw = parts[5] if len(parts) > 5 else 'brand_desc=""'
                        line = (
                            f"    return {wrap_fn}(title, desc, {body}, {layout_kw}, "
                            f'slug="{slug}", page=page, site_name={brand}, nav={nav}, '
                            f"{brand_kw}, {desc_kw})"
                        )
                        matched = True
                        break
            else:
                m = re.match(rf"(\s*)return {wrap_fn}\((title, desc, .+)\)\s*$", line)
                if m:
                    indent = m.group(1)
                    body_expr = m.group(2).split(", ", 2)[2]
                    line = (
                        f"{indent}return {wrap_fn}(title, desc, {body_expr}, "
                        f'slug="{slug}", page=page, site_name={brand}, nav={nav})'
                    )
                    matched = True
                    break
    out.append(line)
    i += 1

text = "\n".join(out) + "\n"
p.write_text(text, encoding="utf-8")
print("patched build_vitrine_site.py")
