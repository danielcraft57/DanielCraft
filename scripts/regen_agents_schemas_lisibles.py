#!/usr/bin/env python3
"""Regenere des schemas Agents tres lisibles (francais simple, gros titres)."""
from __future__ import annotations

from pathlib import Path

SCH = Path(__file__).resolve().parent.parent / "assets" / "images" / "blog" / "schemas"
DIST = Path(__file__).resolve().parent.parent / "dist" / "assets" / "images" / "blog" / "schemas"


def card(x, y, w, h, stroke, lines, num=None):
    parts = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#fff" stroke="{stroke}" stroke-width="3"/>'
    ]
    if num is not None:
        parts.append(
            f'<circle cx="{x + 22}" cy="{y + 22}" r="14" fill="{stroke}"/>'
            f'<text x="{x + 22}" y="{y + 27}" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" '
            f'font-size="14" font-weight="700" fill="#fff">{num}</text>'
        )
        ty = y + 58
    else:
        ty = y + 40
    for i, line in enumerate(lines):
        size = 16 if i == 0 else 13
        weight = 700 if i == 0 else 500
        fill = "#0f172a" if i == 0 else "#475569"
        parts.append(
            f'<text x="{x + w/2}" y="{ty + i * 22}" text-anchor="middle" '
            f'font-family="Segoe UI, Arial, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{line}</text>'
        )
    return "\n  ".join(parts)


def arrow(x1, y, x2):
    return (
        f'<defs><marker id="arr" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto">'
        f'<path d="M0,0 L8,3 L0,6 Z" fill="#0f172a"/></marker></defs>'
        f'<path d="M{x1} {y} H{x2}" stroke="#0f172a" stroke-width="3" fill="none" marker-end="url(#arr)"/>'
    )


def make(name: str, title: str, subtitle: str, boxes: list[tuple[str, list[str]]], colors=None):
    colors = colors or ["#2563eb", "#0284c7", "#0ea5e9", "#dc2626"]
    n = len(boxes)
    gap = 18
    w = min(170, (740 - gap * (n - 1)) // n)
    h = 110
    total = n * w + (n - 1) * gap
    start = (800 - total) // 2
    y = 150
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" role="img">',
        f'  <title>{title}</title>',
        f'  <desc>{subtitle}</desc>',
        '  <rect width="800" height="420" fill="#f5f7fb"/>',
        f'  <text x="400" y="48" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="26" font-weight="800" fill="#0f172a">{title}</text>',
        f'  <text x="400" y="82" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="15" fill="#475569">{subtitle}</text>',
    ]
    # one marker def for all
    parts.append(
        '  <defs><marker id="arr" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto">'
        '<path d="M0,0 L8,3 L0,6 Z" fill="#0f172a"/></marker></defs>'
    )
    for i, (label_lines) in enumerate(boxes):
        # boxes is list of list of lines
        lines = boxes[i]
        x = start + i * (w + gap)
        stroke = colors[i % len(colors)]
        parts.append("  " + card(x, y, w, h, stroke, lines, num=i + 1).replace("\n  ", "\n  "))
        if i < n - 1:
            parts.append(
                f'  <path d="M{x + w + 2} {y + h/2} H{x + w + gap - 8}" stroke="#0f172a" stroke-width="3" fill="none" marker-end="url(#arr)"/>'
            )
    parts.append(
        f'  <text x="400" y="390" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="14" fill="#334155">{subtitle}</text>'
    )
    parts.append("</svg>\n")
    text = "\n".join(parts)
    # fix card() - it returns multi-line with wrong structure. Rebuild simpler.
    return name, title, subtitle, boxes, colors


def write_svg(name: str, title: str, subtitle: str, boxes: list[list[str]], colors=None) -> None:
    colors = colors or ["#2563eb", "#0284c7", "#0ea5e9", "#dc2626"]
    n = len(boxes)
    gap = 18
    w = min(170, (740 - gap * (n - 1)) // n)
    h = 120
    total = n * w + (n - 1) * gap
    start = (800 - total) // 2
    y = 145
    lines_out = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" role="img">',
        f"  <title>{title}</title>",
        f"  <desc>{subtitle}</desc>",
        '  <rect width="800" height="420" fill="#f5f7fb"/>',
        f'  <text x="400" y="48" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="24" font-weight="800" fill="#0f172a">{title}</text>',
        f'  <text x="400" y="78" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="14" fill="#475569">{subtitle}</text>',
        '  <defs><marker id="arr" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#0f172a"/></marker></defs>',
    ]
    for i, box_lines in enumerate(boxes):
        x = start + i * (w + gap)
        stroke = colors[min(i, len(colors) - 1)]
        lines_out.append(
            f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#ffffff" stroke="{stroke}" stroke-width="3"/>'
        )
        lines_out.append(
            f'  <circle cx="{x + 22}" cy="{y + 22}" r="14" fill="{stroke}"/>'
        )
        lines_out.append(
            f'  <text x="{x + 22}" y="{y + 27}" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="14" font-weight="700" fill="#ffffff">{i + 1}</text>'
        )
        for j, t in enumerate(box_lines[:3]):
            size = 15 if j == 0 else 12
            weight = 700 if j == 0 else 500
            fill = "#0f172a" if j == 0 else "#475569"
            lines_out.append(
                f'  <text x="{x + w/2}" y="{y + 58 + j * 20}" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{t}</text>'
            )
        if i < n - 1:
            lines_out.append(
                f'  <path d="M{x + w + 2} {y + h/2} H{x + w + gap - 10}" stroke="#0f172a" stroke-width="3" fill="none" marker-end="url(#arr)"/>'
            )
    lines_out.append(
        f'  <rect x="80" y="300" width="640" height="70" rx="10" fill="#e2e8f0"/>'
    )
    lines_out.append(
        f'  <text x="400" y="342" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="15" font-weight="600" fill="#0f172a">{subtitle}</text>'
    )
    lines_out.append("</svg>\n")
    SCH.mkdir(parents=True, exist_ok=True)
    DIST.mkdir(parents=True, exist_ok=True)
    content = "\n".join(lines_out)
    (SCH / name).write_text(content, encoding="utf-8")
    (DIST / name).write_text(content, encoding="utf-8")
    print("schema", name)


SPECS = [
    ("agents-hf-quest.svg", "Un agent IA, c'est simple", "Cerveau + outils + boucle = vraie réponse", [
        ["Le cerveau", "lit ta question"],
        ["Les outils", "horaires, stock..."],
        ["La boucle", "agit, puis regarde"],
        ["La réponse", "avec de vrais faits"],
    ]),
    ("agents-hf-tools.svg", "Les outils, mode d'emploi", "Le modèle demande, ton site exécute", [
        ["Ta question", "ex. ouvert samedi ?"],
        ["Choix d'outil", "horaires / stock"],
        ["Exécution", "vrai code / vraie API"],
        ["Résultat", "le modèle répond"],
    ]),
    ("agents-hf-react.svg", "La boucle en 3 temps", "Penser → Agir → Regarder le résultat", [
        ["Penser", "de quoi ai-je besoin ?"],
        ["Agir", "appeler un outil"],
        ["Observer", "lire le résultat"],
        ["Répondre", "ou recommencer"],
    ]),
    ("agents-hf-smolagents.svg", "Ton premier agent", "smolagents : on branche et on lance", [
        ["Préparer", "Python + lib"],
        ["Un outil", "ex. moyenne / horaires"],
        ["L'agent", "modèle + outil"],
        ["On lance", "et on lit la trace"],
    ]),
    ("agents-hf-code-vs-json.svg", "Deux façons d'agir", "Code libre ou appel d'outil contrôlé", [
        ["Code agent", "écrit du Python"],
        ["Plus souple", "calculs, enchaînements"],
        ["Appel JSON", "outil précis seulement"],
        ["Plus sûr", "liste d'outils fermée"],
    ]),
    ("agents-hf-frameworks.svg", "Trois boîtes à outils", "Choisis selon ton besoin", [
        ["smolagents", "démarrer vite"],
        ["LlamaIndex", "tes documents"],
        ["LangGraph", "parcours contrôlé"],
        ["Le critère", "ton cas métier"],
    ]),
    ("agents-hf-rag.svg", "Chercher puis répondre", "L'agent va chercher dans ta doc", [
        ["Question", "du client"],
        ["Recherche", "dans ta FAQ"],
        ["Vérification", "autres outils si besoin"],
        ["Réponse", "avec sources"],
    ]),
    ("agents-hf-observability.svg", "Voir ce qui se passe", "Sans traces, tu voles à l'aveugle", [
        ["Traces", "chaque action"],
        ["Mesures", "temps, erreurs"],
        ["Tests", "vrais cas clients"],
        ["Améliorer", "corriger les tools"],
    ]),
    ("agents-hf-finetune-fc.svg", "Mieux appeler les outils", "Quand le modèle se trompe trop souvent", [
        ["Exemples", "bons appels d'outils"],
        ["Entraînement", "adapter le modèle"],
        ["Contrôle", "jeux de tests"],
        ["Agent", "plus fiable"],
    ]),
    ("agents-hf-langgraph.svg", "Un parcours en étapes", "Comme un plan : A puis B, ou C", [
        ["État", "ce qu'on sait"],
        ["Étapes", "actions claires"],
        ["Choix", "si / sinon"],
        ["Fin", "réponse ou humain"],
    ]),
    ("agents-hf-llamaindex.svg", "Agent + tes documents", "Il répond avec ta FAQ, pas d'invention", [
        ["Tes docs", "FAQ, fiches"],
        ["Index", "rangés pour chercher"],
        ["L'agent", "va chercher"],
        ["Réponse", "citée / sourcée"],
    ]),
    ("agents-hf-multi.svg", "Plusieurs spécialistes", "Un chef d'orchestre, des rôles clairs", [
        ["Le chef", "répartit le travail"],
        ["Recherche", "doc / web limité"],
        ["Vision", "lit une image"],
        ["Synthèse", "réponse finale"],
    ]),
]


def main() -> None:
    for name, title, sub, boxes in SPECS:
        write_svg(name, title, sub, boxes)
    print("OK", len(SPECS))


if __name__ == "__main__":
    main()
