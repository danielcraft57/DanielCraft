#!/usr/bin/env python3
"""Génère la série Design Patterns : articles longs, SVG, images OG, collection."""

from __future__ import annotations

import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from textwrap import dedent

BASE = Path(__file__).resolve().parent.parent
OUT_ARTICLES = BASE / "blog" / "content" / "articles"
OUT_COLLECTION = BASE / "blog" / "content" / "collections"
OUT_SVG = BASE / "assets" / "images" / "blog"
OUT_OG = BASE / "assets" / "images" / "og"
SERIES = "design-patterns-serie"
DATE_START = "2026-04-01"

sys.path.insert(0, str(Path(__file__).parent))
from design_patterns_data import (  # noqa: E402
    FAMILY_COLORS,
    PATTERNS,
    POPULARITY_SLUGS,
    patterns_in_popularity_order,
)
from design_patterns_enriched import apply_enriched  # noqa: E402

apply_enriched()

ILLUSTRATIONS_DIR = OUT_SVG / "illustrations"


def fm(title: str, excerpt: str, order: int, slug: str, tags: list[str], date: str) -> str:
    tag_line = ", ".join(tags)
    og = f"{slug}-1200x630.jpg"
    return f"""---
title: "{title}"
date: {date}
excerpt: "{excerpt.replace('"', "'")[:220]}"
type: article
tags: [{tag_line}]
og_image: {og}
series: {SERIES}
series_order: {order}
---

"""


def svg_key(slug: str) -> str:
    return slug.replace("design-patterns-", "")


def roles_table(roles: list[tuple[str, str]]) -> str:
    lines = ["| Rôle | Responsabilité |", "|------|----------------|"]
    for role, desc in roles:
        lines.append(f"| **{role}** | {desc} |")
    return "\n".join(lines)


def bullet_list(items: list[str]) -> str:
    return "\n".join(f"- {x}" for x in items)


def link(slug: str, label: str) -> str:
    return f"[{label}](/blog/articles/{slug}.html)"


def build_article(
    order: int,
    total: int,
    p: dict,
    prev_slug: str,
    next_slug: str,
    date: str,
) -> str:
    name = p["name"]
    slug = p["slug"]
    fam = p["family_fr"]
    sk = svg_key(slug)
    tags = ["Design Patterns", "GoF", name, fam, "TypeScript", "Python", "junior"]
    title = f"{name} : pattern {fam.lower()} expliqué pour juniors"
    figs = f"""
<figure>
  <img src="../../assets/images/blog/dp-{sk}.svg" alt="Schéma du pattern {name}" class="schema-inline" width="480" />
  <figcaption>Structure simplifiée du pattern {name} — les flèches montrent qui dépend de qui.</figcaption>
</figure>
"""
    banner = f"illustrations/dp-{sk}-banner.webp"
    figs += f"""
<figure>
  <img src="../../assets/images/blog/{banner}" alt="Illustration {name}" class="schema-inline" width="720" />
  <figcaption>Vue d'ensemble visuelle du pattern {name} ({fam}).</figcaption>
</figure>
"""
    if p.get("extra_fig"):
        figs += p["extra_fig"]

    compare_block = ""
    if p.get("compare"):
        compare_block = f"""
---

## Comparaisons utiles

{p['compare']}
"""

    prev_label = PATTERNS.get(prev_slug, {}).get("name", "Introduction")
    next_label = PATTERNS.get(next_slug, {}).get("name", "Fin de série")

    related_lines = "\n".join(f"- **{n}** : {d}" for n, d in p["related"])
    body = dedent(
        f"""
# {name} : guide complet pour développeurs juniors

**Famille :** {fam} · **Série :** Design Patterns GoF · **Article {order}/{total}** · **Popularité :** #{order - 1} sur 23

{p['one_liner']}

{figs}

---

## En une phrase

{p['one_liner']}

---

## Le problème sans ce pattern

{p['problem']}

### Symptômes dans ton code

- Fichiers qui grossissent à chaque nouvelle variante.
- Tests difficiles : trop de mocks ou d'effets de bord cachés.
- Tu as peur de toucher une classe car « tout dépend de tout ».

---

## L'idée du pattern {name}

{p['idea']}

{roles_table(p['roles'])}

### Analogie du quotidien

{p['analogy']}

---

## Exemple complet en TypeScript

{p['ts_example']}

### Ce qu'il faut retenir du code

- Le **client** dépend d'abstractions, pas de détails partout.
- Chaque nouvelle variante = **nouvelle classe** (ou module), pas un `if` de plus.
- Nomme tes types pour le **métier** (noms métier explicites, pas `Strategy1`).

---

## Exemple en Python

{p['py_example']}

---

## Quand utiliser {name}

{bullet_list(p['when_use'])}

---

## Quand ne pas utiliser {name}

{bullet_list(p['when_not'])}

---

## Erreurs fréquentes des juniors

{bullet_list(p['mistakes'])}

---

## Patterns proches

{related_lines}
{compare_block}
---

## Dans le monde réel

{p['real_world']}

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Non — on teste surtout ta capacité à reconnaître le problème. Le nom {name} aide à communiquer en équipe.

**Ça remplace les frameworks ?** Non — React, Express ou Spring implémentent souvent ces idées pour toi. Comprendre {name} te permet de les utiliser correctement.

**Je dois tout refactoriser ?** Non — applique le pattern quand la douleur est réelle (nouveaux bugs à chaque feature).

---

## Mini test unitaire (idée)

```typescript
// Exemple de test : mocke les collaborateurs, vérifie le comportement public
describe('{name}', () => {{
  it('fonctionne avec une variante', () => {{
    // Arrange → Act → Assert
  }});
}});
```

Adapte ce squelette à ton framework (Jest, Vitest, pytest).

---

## Pas à pas : implémenter en 5 étapes

1. **Nomme le problème** — est-ce vraiment {name} ?
2. **Dessine les rôles** sur papier (client, abstraction, implémentations).
3. **Écris un test** qui décrit le comportement attendu.
4. **Implémente une variante** — valide avant d'en ajouter d'autres.
5. **Documente en équipe** — « ici on utilise {name} parce que… ».

---

## Checklist code review

- [ ] Le client ne dépend pas de classes concrètes inutiles
- [ ] Pas de sur-abstraction sur un cas unique
- [ ] Tests sur chaque variante / handler / état
- [ ] Nommage métier clair

---

## Exercice pratique (25–35 min)

{p['exercise']}

---

## Résumé

{p['summary']}

---

## Navigation dans la série

- Précédent : {link(prev_slug, prev_label)}
- Suivant : {link(next_slug, next_label)}
"""
    ).strip()

    return fm(title, p["one_liner"], order, slug, tags, date) + body + "\n"


INTRO_BODY = dedent(
    """
# Introduction aux Design Patterns : guide Gang of Four pour juniors

Tu as déjà copié-collé du code sans comprendre sa structure ? Ou une classe de 800 lignes que personne n'ose toucher ? Les **design patterns** t'aident à **nommer** des solutions qui marchent, à **communiquer** avec ton équipe, et à **éviter** de réinventer la roue.

Cette série couvre les **23 patterns du Gang of Four (1994)**. Contrairement à beaucoup de catalogues, nous les classons ici du **plus populaire au moins rencontré** en entreprise — pour que tu apprennes d'abord ce que tu verras le plus souvent en code review et en entretien.

<figure>
  <img src="../../assets/images/blog/design-patterns-intro-illustration.webp" alt="Illustration des trois familles de design patterns" class="schema-inline" width="720" />
  <figcaption>Vue d'ensemble : création, structure et comportement — les trois familles du catalogue GoF.</figcaption>
</figure>

---

## Qu'est-ce qu'un design pattern ?

Un design pattern est une **solution réutilisable** à un problème récurrent de conception. Ce n'est pas une librairie : c'est une **organisation** de classes, modules et objets pour garder le code lisible, testable et évolutif.

### Ce qu'un pattern n'est pas

- Une règle absolue (« toujours Singleton » → faux).
- Du code à copier-coller sans réfléchir.
- Une excuse pour sur-architecturer un petit script.

### Ce qu'un pattern est

- Un **vocabulaire partagé** : « Observer ici » = tout le monde visualise la même chose.
- Une **réponse éprouvée** à un problème précis.
- Un **outil de réflexion** avant le dixième `if/else`.

<figure>
  <img src="../../assets/images/blog/design-patterns-families.svg" alt="Les trois familles GoF" class="schema-inline" width="520" />
  <figcaption>5 créationnels, 7 structurels, 11 comportementaux — 23 patterns au total.</figcaption>
</figure>

<figure>
  <img src="../../assets/images/blog/design-patterns-popularity.svg" alt="Ordre de popularité de la série" class="schema-inline" width="520" />
  <figcaption>Cette série suit l'ordre de popularité (du plus au moins utilisé), pas l'ordre du livre GoF.</figcaption>
</figure>

---

## Les trois familles (rappel)

| Famille | Question | Exemples populaires |
|---------|----------|---------------------|
| **Créationnels** | Comment instancier ? | Singleton, Factory, Builder |
| **Structurels** | Comment composer ? | Adapter, Decorator, Facade |
| **Comportementaux** | Comment répartir les comportements ? | Observer, Strategy, Command |

---

## Ordre de la série (popularité décroissante)

1. Singleton · 2. Factory Method · 3. Observer · 4. Strategy · 5. Decorator · 6. Adapter · 7. Facade · 8. Command · 9. Template Method · 10. Builder · 11. Iterator · 12. State · 13. Proxy · 14. Abstract Factory · 15. Composite · 16. Bridge · 17. Prototype · 18. Flyweight · 19. Chain of Responsibility · 20. Mediator · 21. Memento · 22. Visitor · 23. Interpreter

Tu peux lire linéairement ou sauter vers le pattern qui correspond à ta douleur du moment.

---

## SOLID en version junior

1. **S**ingle Responsibility — une raison de changer par classe.
2. **O**pen/Closed — étendre sans tout casser.
3. **L**iskov — les sous-types restent substituables.
4. **I**nterface Segregation — petites interfaces.
5. **D**ependency Inversion — dépendre d'abstractions.

---

## Comment lire chaque article

1. **En une phrase** + **Le problème** — si ça ne parle pas, passe.
2. **Schéma** + **TypeScript** — cœur de la série.
3. **Python** si tu es plutôt backend.
4. **Quand ne pas l'utiliser** — souvent le plus utile.
5. **Exercice** 25–35 min sur un mini-projet.

---

## Erreurs classiques des juniors

| Erreur | Conséquence | Attitude saine |
|--------|-------------|----------------|
| Pattern « pour faire joli » | Code verbeux | Commence simple ; refactorise quand ça fait mal |
| God Object | Tout dans une classe | Une responsabilité à la fois |
| Confondre Factory / Abstract Factory / Builder | Mauvais choix | Lis les 3 articles créationnels |
| Pas de tests | Pattern rigide | Test avant structure |

---

## Exercice : cartographier ton projet

Sur un repo perso, note : création compliquée → créationnel ; API tierce → structurel ; gros `switch` comportement → comportemental. Pas besoin de tout refactoriser : entraîne ton **œil**.

---

## Résumé

- 23 patterns GoF, expliqués pour juniors, avec schémas et exemples TS/Python.
- Ordre **popularité** (pas livre) pour un apprentissage pragmatique.
- Article suivant : **Singleton**.

---

## Navigation

- Suivant : [Singleton](/blog/articles/design-patterns-singleton.html)
"""
).strip()


def write_intro(date: str) -> None:
    path = OUT_ARTICLES / "design-patterns-introduction-gang-of-four.md"
    content = fm(
        "Introduction aux Design Patterns : guide Gang of Four pour juniors",
        "Comprendre les design patterns, les 3 familles GoF, l'ordre par popularité et comment lire la série avant chaque pattern en détail.",
        1,
        "design-patterns-introduction-gang-of-four",
        ["Design Patterns", "GoF", "junior", "SOLID", "architecture"],
        date,
    ) + INTRO_BODY + "\n"
    path.write_text(content, encoding="utf-8")
    print("Wrote", path.name)


def write_articles() -> list[str]:
    slugs = ["design-patterns-introduction-gang-of-four", *POPULARITY_SLUGS]
    total = len(slugs)
    start = datetime.strptime(DATE_START, "%Y-%m-%d")
    write_intro(start.strftime("%Y-%m-%d"))

    for i, p in enumerate(patterns_in_popularity_order(), start=2):
        date = (start + timedelta(days=i - 1)).strftime("%Y-%m-%d")
        prev_slug = slugs[i - 2]
        next_slug = slugs[i] if i < len(slugs) else slugs[-1]
        content = build_article(i, total, p, prev_slug, next_slug, date)
        path = OUT_ARTICLES / f"{p['slug']}.md"
        path.write_text(content, encoding="utf-8")
        print("Wrote", path.name)
    return slugs


def write_collection(slugs: list[str]) -> None:
    data = {
        "id": SERIES,
        "title": "Série Design Patterns — du plus populaire au moins (GoF pour juniors)",
        "description": "Les 23 design patterns du Gang of Four expliqués clairement pour développeurs juniors : ordre par popularité, schémas, exemples TypeScript et Python, exercices et pièges à éviter.",
        "slug": SERIES,
        "articles": slugs,
    }
    path = OUT_COLLECTION / f"{SERIES}.json"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Wrote", path.name)


MARKER = (
    '<defs><marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">'
    '<path d="M0,0 L8,4 L0,8 z" fill="{color}"/></marker></defs>'
)


def box(x: int, y: int, w: int, h: int, title: str, sub: str, stroke: str, fill: str) -> str:
    return f"""
  <rect fill="{fill}" stroke="{stroke}" stroke-width="2" x="{x}" y="{y}" width="{w}" height="{h}" rx="8"/>
  <text x="{x + w // 2}" y="{y + 28}" text-anchor="middle" font-size="12" font-weight="bold" fill="#374151">{title}</text>
  <text x="{x + w // 2}" y="{y + 46}" text-anchor="middle" font-size="10" fill="#6b7280">{sub}</text>
"""


def line(x1: int, y1: int, x2: int, y2: int, color: str) -> str:
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="2" marker-end="url(#arr)"/>'


def write_svgs() -> None:
    OUT_SVG.mkdir(parents=True, exist_ok=True)
    layouts: dict[str, str] = {}

    for slug in POPULARITY_SLUGS:
        p = PATTERNS[slug]
        name = p["name"]
        color = FAMILY_COLORS[p["family_fr"]]
        sk = svg_key(slug)
        # Layouts spécifiques
        if slug == "design-patterns-observer":
            inner = (
                box(150, 10, 100, 50, "Subject", "notify()", color, "#fff7ed")
                + box(20, 70, 90, 40, "Obs A", "update", color, "#f8f9fa")
                + box(130, 70, 90, 40, "Obs B", "update", color, "#f8f9fa")
                + box(240, 70, 90, 40, "Obs C", "update", color, "#f8f9fa")
                + line(200, 60, 65, 70, color)
                + line(200, 60, 175, 70, color)
                + line(200, 60, 285, 70, color)
            )
            vb, w = "0 0 360 120", 360
        elif slug == "design-patterns-decorator":
            inner = (
                box(20, 35, 80, 50, "Core", "Component", color, "#eff6ff")
                + box(110, 25, 90, 50, "Deco A", "wrap", color, "#eff6ff")
                + box(210, 15, 90, 50, "Deco B", "wrap", color, "#eff6ff")
                + line(100, 60, 110, 50, color)
                + line(200, 50, 210, 40, color)
            )
            vb, w = "0 0 320 100", 320
        elif slug == "design-patterns-strategy":
            inner = (
                box(20, 30, 100, 50, "Context", "setStrategy()", color, "#fff7ed")
                + box(150, 10, 110, 40, "Strategy", "interface", color, "#fef2f2")
                + box(150, 60, 50, 35, "A", "impl", color, "#f8f9fa")
                + box(210, 60, 50, 35, "B", "impl", color, "#f8f9fa")
                + line(120, 55, 150, 30, color)
                + line(175, 50, 175, 60, color)
                + line(205, 50, 235, 60, color)
            )
            vb, w = "0 0 280 110", 280
        elif slug == "design-patterns-singleton":
            inner = (
                box(30, 30, 90, 50, "Client", "getInstance()", color, "#ecfdf5")
                + box(160, 20, 120, 70, "Singleton", "une instance", color, "#ecfdf5")
                + line(120, 55, 160, 55, color)
            )
            vb, w = "0 0 300 100", 300
        else:
            inner = (
                box(20, 25, 110, 55, "Client", "utilise", color, "#f8f9fa")
                + line(130, 52, 170, 52, color)
                + box(170, 25, 120, 55, name[:14], "rôle central", color, "#fef2f2")
            )
            vb, w = "0 0 310 100", 310

        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}">
{MARKER.format(color=color)}
{inner}
</svg>"""
        layouts[sk] = svg

    # Familles + popularité
    pop_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 200">
  <rect fill="#f8f9fa" width="520" height="200" rx="8"/>
  <text x="260" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#374151">Popularité (cette série)</text>
"""
    y = 40
    for i, slug in enumerate(POPULARITY_SLUGS[:12], 1):
        name = PATTERNS[slug]["name"]
        pop_svg += f'  <text x="20" y="{y}" font-size="10" fill="#374151">{i}. {name}</text>\n'
        y += 13
    for i, slug in enumerate(POPULARITY_SLUGS[12:], 13):
        name = PATTERNS[slug]["name"]
        pop_svg += f'  <text x="270" y="{40 + (i - 13) * 13}" font-size="10" fill="#374151">{i}. {name}</text>\n'
    pop_svg += "</svg>"

    for sk, svg in layouts.items():
        (OUT_SVG / f"dp-{sk}.svg").write_text(svg, encoding="utf-8")
    (OUT_SVG / "design-patterns-popularity.svg").write_text(pop_svg, encoding="utf-8")
    print(f"Wrote {len(layouts)} pattern SVGs + popularity chart")


def _pillow_fonts() -> tuple:
    from PIL import ImageFont

    try:
        return (
            ImageFont.truetype("arial.ttf", 52),
            ImageFont.truetype("arial.ttf", 28),
            ImageFont.truetype("arial.ttf", 22),
        )
    except OSError:
        d = ImageFont.load_default()
        return d, d, d


def _wrap_title(draw, text: str, font, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    line: list[str] = []
    for w in words:
        test = " ".join(line + [w])
        if draw.textlength(test, font=font) > max_width:
            if line:
                lines.append(" ".join(line))
            line = [w]
        else:
            line.append(w)
    if line:
        lines.append(" ".join(line))
    return lines[:2]


def _render_design_pattern_card(
    width: int,
    height: int,
    *,
    title: str,
    subtitle: str,
    badge: str,
    color: str,
    boxes: list[tuple[str, str]],
    footer: str = "DanielCraft — Design Patterns",
):
    """Carte visuelle unifiée (fond clair, badge, titre, 3 blocs reliés)."""
    from PIL import Image, ImageDraw

    scale = width / 1200
    pad = int(48 * scale)
    font_title, font_sub, font_small = _pillow_fonts()
    if scale < 1:
        from PIL import ImageFont

        try:
            font_title = ImageFont.truetype("arial.ttf", max(22, int(52 * scale)))
            font_sub = ImageFont.truetype("arial.ttf", max(14, int(28 * scale)))
            font_small = ImageFont.truetype("arial.ttf", max(12, int(22 * scale)))
        except OSError:
            pass

    img = Image.new("RGB", (width, height), "#eef2f7")
    draw = ImageDraw.Draw(img)
    bar_h = max(8, int(10 * scale))
    draw.rectangle([0, 0, width, bar_h], fill=color)
    draw.rounded_rectangle(
        [pad, pad, width - pad, height - pad],
        radius=max(12, int(20 * scale)),
        fill="#ffffff",
        outline="#dbeafe",
        width=max(1, int(2 * scale)),
    )

    bx1, by1 = pad + int(24 * scale), pad + int(24 * scale)
    bx2, by2 = bx1 + int(200 * scale), by1 + int(52 * scale)
    draw.rounded_rectangle([bx1, by1, bx2, by2], radius=max(8, int(12 * scale)), fill=color)
    draw.text((bx1 + int(16 * scale), by1 + int(12 * scale)), badge[:18], fill="#ffffff", font=font_small)

    tx = pad + int(24 * scale)
    ty = by2 + int(20 * scale)
    for ln in _wrap_title(draw, title, font_title, width - 2 * pad - int(48 * scale)):
        draw.text((tx, ty), ln, fill="#111827", font=font_title)
        ty += int(58 * scale)
    draw.text((tx, ty + int(4 * scale)), subtitle[:80], fill="#6b7280", font=font_sub)

    box_w = int(280 * scale)
    gap = int(36 * scale)
    box_h = int(96 * scale)
    total_w = len(boxes) * box_w + (len(boxes) - 1) * gap
    start_x = (width - total_w) // 2
    y_box = height - pad - int(130 * scale)
    for i, (label, sub) in enumerate(boxes):
        x = start_x + i * (box_w + gap)
        draw.rounded_rectangle(
            [x, y_box, x + box_w, y_box + box_h],
            radius=max(8, int(10 * scale)),
            outline=color,
            width=max(1, int(2 * scale)),
            fill="#f8fafc",
        )
        draw.text((x + int(16 * scale), y_box + int(18 * scale)), label[:16], fill="#111827", font=font_small)
        if sub:
            draw.text((x + int(16 * scale), y_box + int(44 * scale)), sub[:22], fill="#6b7280", font=font_small)
        if i < len(boxes) - 1:
            y_mid = y_box + box_h // 2
            draw.line([x + box_w, y_mid, x + box_w + gap, y_mid], fill=color, width=max(1, int(2 * scale)))

    draw.text(
        (tx, height - pad - int(28 * scale)),
        footer,
        fill="#9ca3af",
        font=font_small,
    )
    return img


def write_pattern_illustrations() -> None:
    try:
        from PIL import Image
    except ImportError:
        print("[WARN] Pillow manquant pour les illustrations")
        return

    ILLUSTRATIONS_DIR.mkdir(parents=True, exist_ok=True)

    for slug in POPULARITY_SLUGS:
        p = PATTERNS[slug]
        name = p["name"]
        fam = p["family_fr"]
        color = FAMILY_COLORS[fam]
        sk = svg_key(slug)
        img = _render_design_pattern_card(
            960,
            400,
            title=name,
            subtitle=f"Pattern {fam}",
            badge=fam,
            color=color,
            boxes=[("Client", "utilise"), (name[:14], "rôle central"), ("Collab.", "optionnel")],
        )
        out = ILLUSTRATIONS_DIR / f"dp-{sk}-banner.webp"
        img.save(out, "WEBP", quality=86, method=6)
    print(f"Wrote {len(POPULARITY_SLUGS)} pattern illustrations")

    intro = _render_design_pattern_card(
        720,
        377,
        title="Design Patterns",
        subtitle="Guide Gang of Four pour juniors",
        badge="Introduction",
        color="#dc2626",
        boxes=[
            ("Créationnels", "5 patterns"),
            ("Structurels", "7 patterns"),
            ("Comportementaux", "11 patterns"),
        ],
    )
    intro.save(OUT_SVG / "design-patterns-intro-illustration.webp", "WEBP", quality=86, method=6)
    intro.save(OUT_SVG / "design-patterns-intro-illustration.png", "PNG", optimize=True)
    print("Wrote design-patterns-intro-illustration.webp/png")


def write_og_images() -> None:
    try:
        from PIL import Image
    except ImportError:
        print("[WARN] Pillow manquant — pip install Pillow pour les images OG")
        return

    OUT_OG.mkdir(parents=True, exist_ok=True)

    intro_img = _render_design_pattern_card(
        1200,
        630,
        title="Design Patterns",
        subtitle="Guide Gang of Four pour juniors",
        badge="Introduction",
        color="#dc2626",
        boxes=[
            ("Créationnels", "5 patterns"),
            ("Structurels", "7 patterns"),
            ("Comportementaux", "11 patterns"),
        ],
        footer="DanielCraft — Série Design Patterns",
    )
    intro_out = OUT_OG / "design-patterns-introduction-gang-of-four-1200x630.jpg"
    intro_img.save(intro_out, "JPEG", quality=88)
    print("Wrote OG", intro_out.name)

    for slug in POPULARITY_SLUGS:
        p = PATTERNS[slug]
        name = p["name"]
        fam = p["family_fr"]
        color = FAMILY_COLORS[fam]
        img = _render_design_pattern_card(
            1200,
            630,
            title=name,
            subtitle=f"Pattern {fam}",
            badge=fam,
            color=color,
            boxes=[("Client", "utilise"), (name[:14], "rôle central"), ("Collab.", "optionnel")],
            footer="DanielCraft — Série Design Patterns",
        )
        out = OUT_OG / f"{slug}-1200x630.jpg"
        img.save(out, "JPEG", quality=88)
        print("Wrote OG", out.name)


def main() -> None:
    slugs = write_articles()
    write_collection(slugs)
    write_svgs()
    write_pattern_illustrations()
    write_og_images()
    print("Done — série Design Patterns régénérée.")


if __name__ == "__main__":
    main()
