#!/usr/bin/env python3
"""Genere schemas SVG + images OG pour les series LLM et Data Engineering."""

from __future__ import annotations

import sys
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = _SCRIPT_DIR.parent
sys.path.insert(0, str(_SCRIPT_DIR))

from _og_cartoon import render_og_card  # noqa: E402

SCHEMA_DIR = ROOT / "assets" / "images" / "blog" / "schemas"
OG_DIR = ROOT / "assets" / "images" / "og"

BG = "#f5f7fb"
INK = "#0f172a"
BLUE = "#2563eb"
BLUE_L = "#60a5fa"
RED = "#dc2626"
WHITE = "#fff"


def flow_schema(
    filename: str,
    title: str,
    boxes: list[str],
    caption: str,
    accent_last: bool = True,
) -> None:
    """Schema horizontal en boites + fleches."""
    n = len(boxes)
    w, h = 800, 420
    gap = 12
    box_w = min(139, (w - 40 - gap * (n - 1)) // n)
    total = n * box_w + (n - 1) * gap
    start_x = (w - total) // 2
    y = 160
    box_h = 70

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',
        f'  <title id="title">{title}</title>',
        f'  <desc id="desc">{caption}</desc>',
        f'  <rect width="{w}" height="{h}" fill="{BG}"/>',
        f'  <text x="{w // 2}" y="36" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="18" font-weight="700" fill="{INK}">{title}</text>',
        '  <defs>',
        '    <marker id="a" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">',
        f'      <path d="M0,0 L6,3 L0,6 Z" fill="{INK}"/>',
        "    </marker>",
        "  </defs>",
    ]

    for i, label in enumerate(boxes):
        x = start_x + i * (box_w + gap)
        stroke = RED if (accent_last and i == n - 1) else (BLUE if i % 2 == 0 else BLUE_L)
        cx = x + box_w / 2
        # wrap label if long
        words = label.split()
        if len(label) > 14 and len(words) > 1:
            mid = len(words) // 2
            line1 = " ".join(words[:mid])
            line2 = " ".join(words[mid:])
            text = (
                f'  <text x="{cx}" y="{y + box_h / 2 - 4}" text-anchor="middle" '
                f'font-family="Segoe UI, Arial, sans-serif" font-size="12" font-weight="600" fill="{INK}">{line1}</text>\n'
                f'  <text x="{cx}" y="{y + box_h / 2 + 14}" text-anchor="middle" '
                f'font-family="Segoe UI, Arial, sans-serif" font-size="12" font-weight="600" fill="{INK}">{line2}</text>'
            )
        else:
            text = (
                f'  <text x="{cx}" y="{y + box_h / 2 + 5}" text-anchor="middle" '
                f'font-family="Segoe UI, Arial, sans-serif" font-size="13" font-weight="600" fill="{INK}">{label}</text>'
            )
        parts.append(
            f'  <rect x="{x}" y="{y}" width="{box_w}" height="{box_h}" rx="8" fill="{WHITE}" stroke="{stroke}" stroke-width="2"/>'
        )
        parts.append(text)
        if i < n - 1:
            ax1 = x + box_w
            ax2 = x + box_w + gap
            mid_y = y + box_h // 2
            parts.append(
                f'  <path d="M{ax1} {mid_y} H{ax2 - 2}" stroke="{INK}" stroke-width="2" fill="none" marker-end="url(#a)"/>'
            )

    parts.append(
        f'  <text x="{w // 2}" y="390" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="{INK}">{caption}</text>'
    )
    parts.append("</svg>")
    SCHEMA_DIR.mkdir(parents=True, exist_ok=True)
    (SCHEMA_DIR / filename).write_text("\n".join(parts) + "\n", encoding="utf-8")
    print(f"[SVG] {filename}")


def two_row_schema(
    filename: str,
    title: str,
    top: list[str],
    bottom: list[str],
    caption: str,
) -> None:
    w, h = 800, 420
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',
        f'  <title id="title">{title}</title>',
        f'  <desc id="desc">{caption}</desc>',
        f'  <rect width="{w}" height="{h}" fill="{BG}"/>',
        f'  <text x="400" y="36" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="18" font-weight="700" fill="{INK}">{title}</text>',
        '  <defs><marker id="a" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#0f172a"/></marker></defs>',
    ]

    def row(boxes: list[str], y: int) -> None:
        n = len(boxes)
        box_w = min(160, (760 - 12 * (n - 1)) // n)
        total = n * box_w + (n - 1) * 12
        sx = (800 - total) // 2
        for i, label in enumerate(boxes):
            x = sx + i * (box_w + 12)
            stroke = BLUE if i % 2 == 0 else BLUE_L
            parts.append(
                f'  <rect x="{x}" y="{y}" width="{box_w}" height="64" rx="8" fill="{WHITE}" stroke="{stroke}" stroke-width="2"/>'
            )
            parts.append(
                f'  <text x="{x + box_w / 2}" y="{y + 38}" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="13" font-weight="600" fill="{INK}">{label}</text>'
            )
            if i < n - 1:
                parts.append(
                    f'  <path d="M{x + box_w} {y + 32} H{x + box_w + 10}" stroke="{INK}" stroke-width="2" fill="none" marker-end="url(#a)"/>'
                )

    row(top, 100)
    parts.append(
        f'  <path d="M400 175 V210" stroke="{INK}" stroke-width="2" fill="none" marker-end="url(#a)"/>'
    )
    row(bottom, 220)
    parts.append(
        f'  <text x="400" y="390" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="{INK}">{caption}</text>'
    )
    parts.append("</svg>")
    SCHEMA_DIR.mkdir(parents=True, exist_ok=True)
    (SCHEMA_DIR / filename).write_text("\n".join(parts) + "\n", encoding="utf-8")
    print(f"[SVG] {filename}")


SCHEMAS = [
    ("llm-nlp-vs-llm.svg", "NLP vs LLM", ["NLP (champ)", "Taches classiques", "Transformers", "LLM"], "Le LLM est une famille de modeles NLP a grande echelle."),
    ("llm-pipeline.svg", "pipeline() Hugging Face", ["Texte", "Tokenizer", "Modele", "Post-traitement", "Resultat"], "Une ligne de code pour une premiere inference."),
    ("llm-architecture.svg", "Architectures Transformer", ["Encoder (BERT)", "Decoder (GPT)", "Encoder-Decoder (T5)"], "Choisir selon la tache : comprendre, generer, ou les deux."),
    ("llm-hub.svg", "Hugging Face Hub", ["Modeles", "Datasets", "Spaces", "Model cards"], "Trouver, telecharger, documenter et partager."),
    ("llm-tokenizers.svg", "Tokenizers & Datasets", ["Texte brut", "Tokens", "IDs", "Tenseurs"], "Le tokenizer est le pont entre le langage et le modele."),
    ("llm-finetuning.svg", "Fine-tuning", ["Dataset", "Trainer", "Eval", "Checkpoint Hub"], "Adapter un modele pre-entraine a ton cas d'usage."),
    ("llm-gradio.svg", "Demo Gradio", ["Modele", "Interface Gradio", "Space Hub", "Utilisateurs"], "Montrer le modele sans installer Python chez le lecteur."),
    ("llm-lora-reasoning.svg", "LoRA & raisonnement", ["Base LLM", "LoRA/PEFT", "Data qualite", "Reasoning"], "Fine-tuner legerement, soigner les donnees, viser le raisonnement."),
    ("data-eng-pipeline.svg", "Pipeline data end-to-end", ["Sources", "Ingestion", "Warehouse", "dbt / BI"], "Sources, transformation, entrepot, consommation."),
    ("data-eng-docker-terraform.svg", "Infra Docker & Terraform", ["Docker", "Postgres", "Terraform", "GCP"], "Reproductible en local, declaratif dans le cloud."),
    ("data-eng-orchestration.svg", "Orchestration", ["Trigger", "Extract", "Transform", "Load", "Alertes"], "Planifier, enchainer, reessayer et observer."),
    ("data-eng-ingestion.svg", "Ingestion incremental", ["API", "Normalisation", "State / curseur", "Lake / WH"], "Charger seulement le nouveau, sans casser le schema."),
    ("data-eng-bigquery.svg", "BigQuery warehouse", ["Tables brutes", "Partition", "Clustering", "SQL analytique"], "Cout et perf : partitionner et clusteriser."),
    ("data-eng-dbt.svg", "Analytics engineering (dbt)", ["Staging", "Intermediate", "Marts", "Tests / docs"], "Du SQL versionne au modele metier teste."),
    ("data-eng-spark.svg", "Batch Spark", ["Fichiers / tables", "DataFrame", "Transform", "Sortie"], "Traiter de gros volumes hors ligne."),
    ("data-eng-kafka.svg", "Streaming Kafka", ["Producteurs", "Topics", "Consumers", "Schemas Avro"], "Evenements en continu, contrats de schema."),
]


OG_ITEMS = [
    # LLM
    ("llm-nlp-vs-llm-comprendre-les-bases-1200x630.jpg", "NLP vs LLM : la difference sans jargon", "Bases Transformers & Hugging Face", "LLM", "assistant"),
    ("llm-transformers-pipeline-premiere-inference-1200x630.jpg", "Premiere inference avec pipeline()", "Classification, generation, en une ligne", "LLM", "code"),
    ("llm-architecture-encoder-decoder-1200x630.jpg", "Encoder, decoder, encoder-decoder", "Choisir l'architecture Transformer", "LLM", "gear"),
    ("llm-huggingface-hub-modeles-datasets-1200x630.jpg", "Hub Hugging Face : modeles & datasets", "Trouver, telecharger, partager", "LLM", "catalog"),
    ("llm-tokenizers-datasets-bases-1200x630.jpg", "Tokenizers et Datasets", "Du texte aux tenseurs", "LLM", "code"),
    ("llm-finetuning-entrainer-modele-1200x630.jpg", "Fine-tuning : entrainer ton modele", "Trainer, eval, checkpoint", "LLM", "process"),
    ("llm-gradio-demo-partager-modele-1200x630.jpg", "Demo Gradio et Spaces", "Partager ton modele en public", "LLM", "browser"),
    ("llm-finetuning-avance-lora-reasoning-1200x630.jpg", "LoRA, PEFT et raisonnement", "Fine-tuning leger et data qualite", "LLM", "assistant"),
    # Data eng
    ("data-engineering-pipeline-end-to-end-intro-1200x630.jpg", "Pipeline data de bout en bout", "Le metier du data engineer", "Data Eng", "process"),
    ("data-engineering-docker-terraform-infra-1200x630.jpg", "Docker, Postgres & Terraform", "Socle infra pour les donnees", "Data Eng", "gear"),
    ("data-engineering-orchestration-kestra-1200x630.jpg", "Orchestration de workflows", "Kestra, DAG, scheduling", "Data Eng", "process"),
    ("data-engineering-ingestion-api-incremental-1200x630.jpg", "Ingestion API incrementale", "Normaliser et charger sans tout relire", "Data Eng", "code"),
    ("data-engineering-warehouse-bigquery-1200x630.jpg", "BigQuery : warehouse cloud", "Partition, clustering, SQL", "Data Eng", "stats"),
    ("data-engineering-dbt-analytics-engineering-1200x630.jpg", "dbt et analytics engineering", "Modeles, tests, documentation", "Data Eng", "report"),
    ("data-engineering-spark-batch-processing-1200x630.jpg", "Spark : traitement batch", "DataFrames et gros volumes", "Data Eng", "code"),
    ("data-engineering-kafka-streaming-1200x630.jpg", "Kafka et streaming", "Topics, consumers, Avro", "Data Eng", "visibilite"),
]


def main() -> None:
    for name, title, boxes, caption in SCHEMAS:
        flow_schema(name, title, boxes, caption)

    OG_DIR.mkdir(parents=True, exist_ok=True)
    for filename, title, subtitle, badge, scene in OG_ITEMS:
        img = render_og_card(
            title=title,
            subtitle=subtitle,
            badge=badge,
            chips=["Cours", "Tutorial", "DanielCraft"],
            scene=scene,
            cta="Lire le tuto →",
            footer="DanielCraft - blog",
        )
        out = OG_DIR / filename
        img.save(out, "JPEG", quality=88, optimize=True)
        print(f"[OG] {filename}")

    print(f"Done: {len(SCHEMAS)} SVG, {len(OG_ITEMS)} OG")


if __name__ == "__main__":
    main()
