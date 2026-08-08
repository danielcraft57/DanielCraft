# -*- coding: utf-8 -*-
"""Génère PROMPTS-IMAGES.md pour toutes les prestations + catégories."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
d = json.loads((ROOT / "src/data/prestations.json").read_text(encoding="utf-8"))
items = [i for i in d["items"] if i.get("has_page")]
cats = d.get("categories") or []

PALETTE = (
    "Palette DanielCraft only: navy #0f3550, sky #4da9d6, mint #7dd4a8, soft blue-gray backgrounds. "
    "No purple, no cream-terracotta, no neon. No readable brand logos (Google/WhatsApp as generic shapes)."
)

STYLES = {
    "photo": "Photorealistic commercial photography, soft daylight, shallow depth of field, premium web-agency look.",
    "iso": "Soft isometric 3D illustration, clean soft shadows, marketplace product feel, not childish cartoon.",
    "flat": "Modern flat vector illustration with subtle grain, editorial poster vibe, generous negative space.",
    "mock": "UI product mockup on devices (phone/laptop), studio soft light, Framer/Webflow aesthetic, UI without readable text.",
    "macro": "Close-up abstract product still-life (icons as objects on desk), tactile materials, soft studio lighting.",
}

CAT_STYLE_CYCLE = {
    "packs": ["iso", "iso", "flat", "iso", "mock"],
    "identite": ["photo", "mock", "photo", "flat", "photo", "iso"],
    "ia": ["iso", "mock", "flat", "photo", "iso", "mock", "flat", "photo", "iso", "mock", "flat", "iso", "mock"],
    "mobile": ["mock", "photo", "iso", "flat", "mock"],
    "technique": ["flat", "iso", "mock", "photo", "macro"],
    "site-contenu": ["photo", "mock", "flat", "macro"],
    "maintenance": ["iso", "flat", "macro", "photo", "iso", "mock", "flat"],
    "eco": ["flat", "photo", "iso", "mock", "flat", "photo", "macro"],
}

SCENE = {
    "pack-presence-telephone": "smartphone home-screen web app icon, storefront, call buttons",
    "pack-reputation-locale": "star ratings floating above a local storefront listing card",
    "pack-whatsapp-commerce": "phone with generic green chat bubbles, shop counter",
    "pack-etre-trouve": "magnifying glass over a map of small shops, analytics laptop",
    "pack-demarrer-commerce": "mini open shop, laptop website, map pin, call buttons bundle",
    "site-vitrine-essentiel": "simple 3-page website on phone and small laptop, bakery facade blur",
    "site-vitrine": "responsive site on desktop tablet phone, artisan workshop blur",
    "identite-harmonieuse": "same brand colors across shop window, business cards, phone screen",
    "visibilite-complete": "map pin over French town street, phone local listing stars",
    "referencement-google": "clean search results page mock without logos, local shop photo",
    "visible-assistants-ia": "soft AI orb answering a local business FAQ near a storefront",
    "repondeur-intelligent": "chat bubbles answering at night beside a closed shop",
    "aide-emails-clients": "inbox drafts being organized on a laptop, calm desk",
    "entretien-mensuel": "calendar checkmarks and shield over a calm laptop",
    "ia-contenus": "text blocks assembling into a website page layout",
    "ia-redaction": "pen and commercial flyer drafts on a clean desk",
    "ia-analyse": "simple charts and KPI cards on a soft dashboard",
    "ia-boutique": "online shop product grid with a helpful advisor orb",
    "ia-automatisation": "connected workflow nodes linking calendar mail and forms",
    "ia-maint-mensuelle": "assistant orb with maintenance wrench and update dots",
    "ia-evolution": "assistant gaining a new feature tile, soft upgrade glow",
    "ia-audit": "checklist clipboard over AI tools icons, audit mood",
    "conseil-projet": "blueprint and architecture flowchart on a table, planning session",
    "connexion-crm": "website screen linked by cable to a CRM panel",
    "transfert-donnees": "data folders moving between two soft servers",
    "liaison-outils": "two apps shaking hands via a plug connector motif",
    "rapport-vitesse": "speed gauge and lightweight page loading bars",
    "page-supplementaire": "extra website page sliding into a site sitemap",
    "formulaire-sur-mesure": "clean contact form UI on tablet, soft shadows",
    "nouveau-look": "before/after website skins with paintbrush accent",
    "maj-contenus": "content cards being refreshed on a CMS-like board",
    "hebergement-domaine": "domain name plaque next to a soft cloud server",
    "sauvegardes-securite": "shield and backup disks above a laptop",
    "https-site": "padlock and certificate ribbon on a browser mock",
    "support-mensuel": "support headset icon and calm email tickets",
    "depannage-2h": "urgent wrench fixing a glowing error badge, still calm colors",
    "accompagnement-heure": "hourglass and coaching session at a desk",
    "support-prioritaire": "priority flag on a support ticket stack",
    "audit-eco-numerique": "leaf over weight/perf meters of a heavy website",
    "alleger-medias": "compressed photo and video icons becoming lighter",
    "site-allege": "slim website dashboard with green efficiency arcs",
    "site-vitrine-eco": "eco storefront website, light pages, leaf accents",
    "page-engagement-numerique": "commitment page mock with leaf and impact icons",
    "suivi-eco-mensuel": "monthly eco score chart, soft mint grid",
    "atelier-eco-web": "workshop table teaching image compression, laptop open",
    "whatsapp-assistant-ia": "generic chat assistant on phone, shop blur, no brand logo",
    "geo-citations-ia": "AI citation cards mentioning a local shop, map hint",
    "ia-avis-google": "review stars and QR after visit, storefront soft focus",
    "prise-rdv-ia": "calendar slots filling with filtered appointment cards",
    "pwa-vitrine": "installable site icon on phone home screen",
    "whatsapp-business-setup": "business profile setup cards on phone, generic chat UI",
    "fiche-google-mobile": "local maps pin and clean business profile card, generic",
    "conversion-mobile": "big call and message buttons on a mobile website",
    "app-mobile-metier": "client space app UI on phone, soft mint header",
}

CAT_PROMPTS = {
    "packs": ("iso", "Isometric bundle of three soft product cards (store, map pin, chat) tied with a mint ribbon, clean white desk, marketplace pack feel"),
    "identite": ("photo", "Clean storefront window with a glowing modern website mockup reflected in the glass, French town street daylight"),
    "ia": ("iso", "Friendly soft-isometric assistant orb above smartphone and laptop, calm automation arrows"),
    "mobile": ("mock", "Smartphone with home-screen web app icon next to generic message bubbles, shop counter blur"),
    "technique": ("flat", "Two connected software panels linked by a clean cable/plug motif, organized tools talking"),
    "site-contenu": ("photo", "Designer desk with laptop showing a simple page layout, paintbrush and text blocks"),
    "maintenance": ("iso", "Shield and cloud backup icons above a calm laptop, serene support uptime feel"),
    "eco": ("flat", "Lightweight leaf motif over a fast-loading website dashboard, performance sobriety mood"),
}


def main() -> None:
    packs_n = sum(1 for i in items if i.get("kind") == "pack")
    lines: list[str] = [
        "# Prompts images — catalogue prestations & packs",
        "",
        "A generer (JPG/WebP 1200x630 cartes, 800x800 ou 4:3 pour fiche hero).",
        "Palette site : navy `#0f3550`, ciel `#4da9d6`, mint `#7dd4a8`, fond clair `#e8f6fc` / blanc.",
        "Pas de violet, pas de creme terracotta, pas de glow violet.",
        "Styles varies : photo realiste, isometric soft, flat vector editorial, mockup UI, macro still-life — toujours la meme palette.",
        "",
        "Export cible :",
        "- Cadres categories : `assets/images/prestations/categories/<id>.jpg`",
        "- Cartes / fiches : `assets/images/prestations/cards/<slug>.jpg`",
        "",
        f"Couverture : **{len(cats)} categories** + **{len(items)} offres** (dont {packs_n} packs).",
        "",
        "## Cadres categories (hub /nos-offres)",
        "",
    ]

    for c in cats:
        cid = c["id"]
        style_key, scene = CAT_PROMPTS.get(cid, ("iso", c.get("title", cid)))
        lines.append(f"### {cid}")
        lines.append(f"{STYLES[style_key]} {scene}. {PALETTE} 16:9.")
        lines.append("")

    by_cat: dict[str, list] = {}
    for it in items:
        by_cat.setdefault(it.get("category") or "autre", []).append(it)

    lines.append("## Cartes & fiches produit (toutes les offres)")
    lines.append("")
    cat_idx = {cid: 0 for cid in CAT_STYLE_CYCLE}
    order = [c["id"] for c in cats] + [k for k in by_cat if k not in {c["id"] for c in cats}]

    for cid in order:
        group = by_cat.get(cid) or []
        if not group:
            continue
        title = next((c.get("title") for c in cats if c["id"] == cid), cid)
        lines.append(f"### Categorie : {title} (`{cid}`)")
        lines.append("")
        cycle = CAT_STYLE_CYCLE.get(cid, ["photo", "iso", "flat", "mock", "macro"])
        for it in group:
            slug = it["slug"]
            i = cat_idx.get(cid, 0)
            style_key = cycle[i % len(cycle)]
            cat_idx[cid] = i + 1
            scene = SCENE.get(slug) or (
                f'visual metaphor for "{it.get("title", "")}" — local commerce / artisan context'
            )
            kind = "Pack bundle composition. " if it.get("kind") == "pack" else ""
            lines.append(f"#### {slug}")
            lines.append(
                f"{kind}{STYLES[style_key]} Subject: {scene}. {PALETTE} 16:9 for cards; also useful as fiche hero."
            )
            lines.append("")

    lines.extend(
        [
            "## Offre de la semaine (bandeau)",
            "",
            "### prestations-deal-week-visual",
            f"{STYLES['iso']} Stacked soft cards with pack icons (store, map pin, chat), "
            f"navy-to-teal gradient backdrop matching site deal banner, mint ribbon space empty for overlay text. {PALETTE} 1:1.",
            "",
            "## Notes generation",
            "- Eviter logos de marques protegees (WhatsApp, Google) — formes generiques.",
            "- Preferer UI sans texte lisible.",
            "- Une fois generes : pointer `image` dans `prestations.json` vers le JPG (pas SVG) pour activer le hero fiche.",
            "- Pour les cadres hub : optionnellement `categories[].image` dans prestations.json.",
            "- Varier le style entre voisins de catalogue pour eviter un mur d'images identiques.",
            "",
        ]
    )

    out = ROOT / "assets/images/maquettes/prestations/PROMPTS-IMAGES.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    text = out.read_text(encoding="utf-8")
    miss = [i["slug"] for i in items if f"#### {i['slug']}" not in text]
    print(f"OK {out} — {len(items)} offres, {len(cats)} cats, missing={miss}")


if __name__ == "__main__":
    main()
