#!/usr/bin/env python3
"""Schemas lisibles LLM + Data Eng (meme style que Agents)."""
from __future__ import annotations

from pathlib import Path

SCH = Path(__file__).resolve().parent.parent / "assets" / "images" / "blog" / "schemas"
DIST = Path(__file__).resolve().parent.parent / "dist" / "assets" / "images" / "blog" / "schemas"


def write_svg(name: str, title: str, subtitle: str, boxes: list[list[str]]) -> None:
    colors = ["#2563eb", "#0284c7", "#0ea5e9", "#dc2626"]
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
        lines_out.append(f'  <circle cx="{x + 22}" cy="{y + 22}" r="14" fill="{stroke}"/>')
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
    lines_out.append('  <rect x="80" y="300" width="640" height="70" rx="10" fill="#e2e8f0"/>')
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
    ("llm-nlp-vs-llm.svg", "NLP et LLM, la difference", "Le terrain, puis les gros modeles", [
        ["NLP", "comprendre le texte"],
        ["Taches", "classer, traduire..."],
        ["Transformers", "architecture cle"],
        ["LLM", "gros modele polyvalent"],
    ]),
    ("llm-pipeline.svg", "Ta premiere inference", "Une ligne, un resultat", [
        ["Texte", "ta phrase"],
        ["pipeline()", "prepare tout"],
        ["Modele", "calcule"],
        ["Resultat", "label ou texte"],
    ]),
    ("llm-architecture.svg", "Trois familles", "Encoder, decoder, les deux", [
        ["Encoder", "comprendre / classer"],
        ["Decoder", "generer du texte"],
        ["Les deux", "traduire / resumer"],
        ["Choix", "selon ton besoin"],
    ]),
    ("llm-hub.svg", "Le Hub Hugging Face", "Modeles et datasets ranges", [
        ["Chercher", "modele / dataset"],
        ["Model card", "lire avant"],
        ["Telecharger", "en local"],
        ["Reutiliser", "dans ton code"],
    ]),
    ("llm-tokenizers.svg", "Tokenizers et datasets", "Couper le texte, preparer les exemples", [
        ["Texte", "phrase brute"],
        ["Tokenizer", "morceaux (tokens)"],
        ["Dataset", "exemples ranges"],
        ["Entrainement", "pret a apprendre"],
    ]),
    ("llm-finetuning.svg", "Fine-tuning", "Adapter un modele a ton metier", [
        ["Modele de base", "deja entraine"],
        ["Tes donnees", "exemples metier"],
        ["Trainer", "apprend encore"],
        ["Checkpoint", "modele adapte"],
    ]),
    ("llm-gradio.svg", "Demo Gradio", "Montrer ton modele facilement", [
        ["Modele", "pret"],
        ["Interface", "Gradio"],
        ["Space", "partage web"],
        ["Feedback", "vrais users"],
    ]),
    ("llm-lora-reasoning.svg", "LoRA et raisonnement", "Adapter sans tout reecrire", [
        ["Modele gele", "base fixe"],
        ["LoRA", "petits adapters"],
        ["Moins de cout", "VRAM / temps"],
        ["Raisonnement", "mieux briefer"],
    ]),
    ("data-eng-pipeline.svg", "Pipeline data", "De la source au dashboard", [
        ["Sources", "API, fichiers, BDD"],
        ["Transform", "nettoyer / joindre"],
        ["Entrepot", "BigQuery..."],
        ["Conso", "dashboards / metier"],
    ]),
    ("data-eng-docker-terraform.svg", "Docker + Terraform", "Lab local + infra cloud", [
        ["Docker", "Postgres local"],
        ["Scripts", "extract test"],
        ["Terraform", "bucket / dataset"],
        ["Cloud", "rejouable"],
    ]),
    ("data-eng-orchestration.svg", "Orchestration", "Planifier et surveiller les jobs", [
        ["DAG", "etapes chainees"],
        ["Schedule", "chaque nuit"],
        ["Retries", "si ca casse"],
        ["Alertes", "tu vois le souci"],
    ]),
    ("data-eng-ingestion.svg", "Ingestion", "Charger sans tout rejouer", [
        ["API / fichiers", "sources"],
        ["Incremental", "seulement le nouveau"],
        ["Normaliser", "types propres"],
        ["Load", "vers l'entrepot"],
    ]),
    ("data-eng-bigquery.svg", "BigQuery", "Entrepot cloud pour analyser", [
        ["Raw", "brut"],
        ["Staging", "nettoye"],
        ["Marts", "pret metier"],
        ["Partition", "cout / vitesse"],
    ]),
    ("data-eng-dbt.svg", "dbt", "Transformer en SQL teste", [
        ["Sources", "tables brutes"],
        ["Modeles", "SQL versionne"],
        ["Tests", "unique / not null"],
        ["Docs", "equipe alignee"],
    ]),
    ("data-eng-spark.svg", "Spark batch", "Gros volumes, calcul distribue", [
        ["Fichiers", "gros historique"],
        ["DataFrame", "transfos"],
        ["Actions", "ecrire / compter"],
        ["Sortie", "tables / parquet"],
    ]),
    ("data-eng-kafka.svg", "Kafka streaming", "Evenements en continu", [
        ["Producers", "envoient"],
        ["Topics", "files d'attente"],
        ["Consumers", "lisent"],
        ["Schemas", "contrat Avro"],
    ]),
]

# Accents corrects pour affichage SVG
ACC = {
    "difference": "différence",
    "modeles": "modèles",
    "Modele": "Modèle",
    "modele": "modèle",
    "Taches": "Tâches",
    "cle": "clé",
    "premiere": "première",
    "inference": "inférence",
    "resultat": "résultat",
    "Resultat": "Résultat",
    "prepare": "prépare",
    "generer": "générer",
    "resumer": "résumer",
    "Telecharger": "Télécharger",
    "Reutiliser": "Réutiliser",
    "ranges": "rangés",
    "Entrainement": "Entraînement",
    "pret a": "prêt à",
    "deja entraine": "déjà entraîné",
    "donnees": "données",
    "metier": "métier",
    "adapte": "adapté",
    "Demo": "Démo",
    "pret": "prêt",
    "gele": "gelé",
    "reecrire": "réécrire",
    "cout": "coût",
    "Entrepot": "Entrepôt",
    "entrepot": "entrepôt",
    "etapes": "étapes",
    "chainees": "chaînées",
    "ca casse": "ça casse",
    "Incremental": "Incrémental",
    "nettoye": "nettoyé",
    "Modeles": "Modèles",
    "versionne": "versionné",
    "equipe": "équipe",
    "alignee": "alignée",
    "distribue": "distribué",
    "ecrire": "écrire",
    "Evenements": "Événements",
    "teste": "testé",
}


def accent(s: str) -> str:
    for a, b in ACC.items():
        s = s.replace(a, b)
    return s


def main() -> None:
    for name, title, sub, boxes in SPECS:
        boxes2 = [[accent(x) for x in box] for box in boxes]
        write_svg(name, accent(title), accent(sub), boxes2)
    print("OK", len(SPECS))


if __name__ == "__main__":
    main()
