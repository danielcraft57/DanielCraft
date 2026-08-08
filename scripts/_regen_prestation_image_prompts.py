# -*- coding: utf-8 -*-
"""Regenerate PROMPTS-IMAGES.md for all categories + prestations (product-shot styles)."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "src/data/prestations.json").read_text(encoding="utf-8"))
OUT = ROOT / "assets/images/maquettes/prestations/PROMPTS-IMAGES.md"

PALETTE = (
    "Palette DanielCraft only: navy #0f3550, sky #4da9d6, mint #7dd4a8, soft ice #e8f6fc, white. "
    "No purple, no cream-terracotta, no neon glow. No readable brand logos "
    "(Google/WhatsApp as generic shapes only). No text logos."
)

# Rotating visual styles — product-first, still on-brand
STYLES = [
    "Photorealistic e-commerce product hero on a clean white seamless, soft studio light, subtle navy rim light, catalog quality",
    "Soft isometric 3D product diorama on a mint-to-ice gradient podium, clean soft shadows, marketplace packshot",
    "UI device mockup product shot (phone + laptop), Framer-like studio, UI blocks without readable text",
    "Editorial flat vector product poster, subtle paper grain, generous negative space, navy/sky/mint shapes",
    "Macro still-life product props on a pale desk (matte plastic + soft metal accents), tactile, soft daylight",
    "Floating product composition over blurred French shop facade, shallow DOF, premium agency look",
]

SUBJECTS = {
    "pack-presence-telephone": "bundle packshot: phone with home-screen app icon, map pin, call button tokens tied with mint ribbon",
    "pack-reputation-locale": "bundle packshot: listing card, star ratings, map pin, mint ribbon",
    "pack-whatsapp-commerce": "bundle packshot: phone with generic chat bubbles, shop counter prop, mint ribbon",
    "pack-etre-trouve": "bundle packshot: magnifying glass over map of shops, analytics card, mint ribbon",
    "pack-demarrer-commerce": "bundle packshot: mini open shop, laptop website mock, map pin, call buttons",
    "site-vitrine-essentiel": "product: smartphone + small laptop showing a simple 3-page local business site",
    "site-vitrine": "product: desktop monitor, tablet and phone showing the same clean commerce website",
    "identite-harmonieuse": "product: matching business card, shop signage sample and phone screen with same navy/sky colors",
    "visibilite-complete": "product: map pin object + phone local listing card with stars (generic, no brand)",
    "referencement-google": "product: clean search-results mock card beside a small shop photo print",
    "visible-assistants-ia": "product: soft AI orb figurine answering FAQ cards next to a storefront model",
    "repondeur-intelligent": "product: night-desk phone with soft chat bubbles beside a closed shop sign",
    "aide-emails-clients": "product: laptop with tidy email draft panels, soft desk props",
    "ia-contenus": "product: text-block tiles assembling into a website page layout board",
    "ia-redaction": "product: pen, flyer drafts and printed page proofs on a clean desk",
    "ia-analyse": "product: soft KPI cards and chart tiles stacked like physical product samples",
    "ia-boutique": "product: ecommerce grid mock on tablet with a small advisor orb prop",
    "ia-automatisation": "product: connected workflow nodes linking calendar, mail and form tiles",
    "ia-maint-mensuelle": "product: assistant orb with tiny wrench and update-dot badges",
    "ia-evolution": "product: assistant gaining a new feature tile, soft upgrade accent in mint",
    "ia-audit": "product: clipboard checklist over AI tool icons as physical tokens",
    "whatsapp-assistant-ia": "product: phone with generic chat assistant UI, no brand logo, shop blur",
    "geo-citations-ia": "product: AI citation cards naming a local shop, subtle map hint",
    "ia-avis-google": "product: review stars + QR stand after visit, storefront soft focus",
    "prise-rdv-ia": "product: calendar slot cards filling with filtered appointment tokens",
    "pwa-vitrine": "product: phone home screen with installable web-app icon as hero object",
    "whatsapp-business-setup": "product: business profile setup cards on phone, generic chat UI",
    "fiche-google-mobile": "product: local maps pin object + clean business profile card (generic)",
    "conversion-mobile": "product: oversized call and message buttons as physical UI props on phone",
    "app-mobile-metier": "product: client-space app UI on phone, soft mint header, no readable text",
    "conseil-projet": "product: architecture flowchart board and blueprint roll on a planning table",
    "connexion-crm": "product: website screen linked by a clean cable to a CRM panel box",
    "transfert-donnees": "product: data folder blocks moving between two soft server units",
    "liaison-outils": "product: two app panels joined by a plug/connector motif",
    "rapport-vitesse": "product: speed gauge and lightweight loading-bar slabs as desk objects",
    "page-supplementaire": "product: extra website page panel sliding into a site sitemap board",
    "formulaire-sur-mesure": "product: clean contact form UI on tablet as catalog product",
    "nouveau-look": "product: before/after website skins with paintbrush accent",
    "maj-contenus": "product: content cards being refreshed on a CMS-like board",
    "entretien-mensuel": "product: calendar checkmarks and shield over a calm laptop",
    "hebergement-domaine": "product: domain name plaque next to a soft cloud server unit",
    "sauvegardes-securite": "product: shield and backup disks above a laptop",
    "https-site": "product: padlock and certificate ribbon on a browser chrome mock",
    "support-mensuel": "product: support headset icon and calm ticket cards",
    "depannage-2h": "product: urgent wrench fixing a soft error badge, still calm palette",
    "accompagnement-heure": "product: hourglass and coaching session desk kit",
    "support-prioritaire": "product: priority flag on a support ticket stack",
    "audit-eco-numerique": "product: leaf over weight/perf meters of a heavy website slab",
    "alleger-medias": "product: compressed photo and video icons becoming lighter tiles",
    "site-allege": "product: slim website dashboard with green efficiency arcs",
    "site-vitrine-eco": "product: eco storefront website mock, light pages, leaf accents",
    "page-engagement-numerique": "product: commitment page mock with leaf and impact icons",
    "suivi-eco-mensuel": "product: monthly eco score chart card, soft mint grid",
    "atelier-eco-web": "product: workshop table teaching image compression, laptop open",
}

CAT_SUBJECTS = {
    "packs": "product: three soft offer cards (store, map pin, chat) tied with mint ribbon on a white desk",
    "identite": "product: storefront window reflecting a modern website mockup, French street daylight",
    "ia": "product: soft assistant orb above smartphone and laptop, calm automation arrows",
    "mobile": "product: smartphone with home-screen web app icon and generic message bubbles",
    "technique": "product: two software panels linked by a clean cable/plug motif",
    "site-contenu": "product: designer desk with laptop page layout, paintbrush and text blocks",
    "maintenance": "product: shield and cloud backup icons above a calm laptop",
    "eco": "product: leaf motif over a fast-loading website dashboard",
}


def prompt(style: str, subject: str, ratio: str = "16:9") -> str:
    return (
        f"{style}. {subject}. Shot as a digital product / catalog image for a service card. "
        f"{PALETTE} Aspect {ratio}."
    )


cats = DATA.get("categories") or []
items = [it for it in DATA.get("items") or [] if it.get("has_page") and it.get("slug")]
by_cat: dict[str, list] = {c["id"]: [] for c in cats if c.get("id")}
for it in items:
    cid = (it.get("category") or "").strip()
    if cid in by_cat:
        by_cat[cid].append(it)
    else:
        by_cat.setdefault(cid or "other", []).append(it)

lines: list[str] = []
lines.append("# Prompts images — catalogue prestations & packs")
lines.append("")
lines.append("A generer (JPG/WebP **produit** : 1200x630 cartes, 800x800 ou 4:3 fiche hero).")
lines.append("Palette site : navy `#0f3550`, ciel `#4da9d6`, mint `#7dd4a8`, fond clair `#e8f6fc` / blanc.")
lines.append("Pas de violet, pas de creme terracotta, pas de glow violet.")
lines.append(
    "Priorite : **images produit** (packshot / mockup / diorama), styles varies "
    "mais toujours la meme palette."
)
lines.append("")
lines.append("Export cible :")
lines.append("- Cadres categories : `assets/images/prestations/categories/<id>.jpg`")
lines.append("- Cartes / fiches : `assets/images/prestations/cards/<slug>.jpg`")
lines.append("")
lines.append(
    f"Couverture : **{len(cats)} categories** + **{len(items)} offres** "
    f"(dont {sum(1 for i in items if i.get('kind')=='pack')} packs)."
)
lines.append("")
lines.append("## Cadres categories (hub /nos-offres)")
lines.append("")

for i, cat in enumerate(cats):
    cid = cat["id"]
    style = STYLES[i % len(STYLES)]
    subject = CAT_SUBJECTS.get(cid, f"product icon for category {cid}")
    lines.append(f"### {cid}")
    lines.append(prompt(style, subject, "16:9"))
    lines.append("")

lines.append("## Cartes & fiches produit (toutes les offres)")
lines.append("")

idx = 0
for cat in cats:
    cid = cat["id"]
    title = cat.get("title") or cid
    lines.append(f"### Categorie : {title} (`{cid}`)")
    lines.append("")
    for it in by_cat.get(cid) or []:
        slug = it["slug"]
        style = STYLES[idx % len(STYLES)]
        idx += 1
        if it.get("kind") == "pack":
            style = STYLES[1]  # isometric podium for packs feel, then rotate
            style = STYLES[idx % len(STYLES)]
            subject = SUBJECTS.get(slug, f"pack bundle packshot for {slug}")
            prefix = "Pack "
        else:
            subject = SUBJECTS.get(slug, f"service product packshot for {slug}")
            prefix = ""
        lines.append(f"#### {slug}")
        lines.append(prompt(style, prefix + subject if prefix and not subject.startswith("bundle") else subject))
        lines.append("")

# orphans
known = {c["id"] for c in cats}
for cid, group in by_cat.items():
    if cid in known:
        continue
    lines.append(f"### Categorie : {cid}")
    lines.append("")
    for it in group:
        slug = it["slug"]
        style = STYLES[idx % len(STYLES)]
        idx += 1
        subject = SUBJECTS.get(slug, f"service product packshot for {slug}")
        lines.append(f"#### {slug}")
        lines.append(prompt(style, subject))
        lines.append("")

lines.append("## Offre de la semaine (bandeau)")
lines.append("")
lines.append("### prestations-deal-week-visual")
lines.append(
    prompt(
        STYLES[1],
        "stacked soft product cards with pack icons (store, map pin, chat), "
        "navy-to-sky gradient backdrop, mint ribbon space empty for overlay text",
        "1:1",
    )
)
lines.append("")
lines.append("## Notes generation")
lines.append("- Eviter logos de marques protegees (WhatsApp, Google) — formes generiques.")
lines.append("- Preferer UI sans texte lisible.")
lines.append("- Une fois generes : pointer `image` dans `prestations.json` vers le JPG (pas SVG) pour activer le hero fiche.")
lines.append("- Pour les cadres hub : optionnellement `categories[].image` dans prestations.json.")
lines.append("- Varier le style entre voisins de catalogue (le fichier alterne deja 6 styles produit).")
lines.append("")

missing = [it["slug"] for it in items if it["slug"] not in SUBJECTS]
if missing:
    lines.append("## Manuels a enrichir (sujet generique pour l'instant)")
    lines.append("")
    for s in missing:
        lines.append(f"- `{s}`")
    lines.append("")

OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"Wrote {OUT}")
print(f"cats={len(cats)} items={len(items)} missing_subjects={len(missing)}")

# coverage check vs md headings
md = OUT.read_text(encoding="utf-8")
for it in items:
    assert f"#### {it['slug']}" in md, it["slug"]
for cat in cats:
    assert f"### {cat['id']}" in md, cat["id"]
print("coverage OK")
