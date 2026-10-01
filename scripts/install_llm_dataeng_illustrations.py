#!/usr/bin/env python3
"""Installe illustrations LLM/DataEng et les injecte dans les articles markdown."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = Path(
    r"C:\Users\loicDaniel\.cursor\projects\c-Users-loicDaniel-Documents-DanielCraft-DanielCraftFr\assets"
)
SCH = ROOT / "assets" / "images" / "blog" / "schemas"
DIST_SCH = ROOT / "dist" / "assets" / "images" / "blog" / "schemas"
ART = ROOT / "blog" / "content" / "articles"

# article slug -> (schema svg already in article, illustration filename, caption)
MAP = [
    (
        "llm-nlp-vs-llm-comprendre-les-bases",
        "llm-nlp-vs-llm.svg",
        "llm-nlp-vs-llm-illustration.jpg",
        "NLP, taches, Transformers, LLM - en image.",
    ),
    (
        "llm-transformers-pipeline-premiere-inference",
        "llm-pipeline.svg",
        "llm-pipeline-illustration.jpg",
        "De ta phrase au resultat via pipeline().",
    ),
    (
        "llm-architecture-encoder-decoder",
        "llm-architecture.svg",
        "llm-architecture-illustration.jpg",
        "Encoder, decoder, ou les deux - selon le besoin.",
    ),
    (
        "llm-huggingface-hub-modeles-datasets",
        "llm-hub.svg",
        "llm-hub-illustration.jpg",
        "Chercher, lire la model card, telecharger.",
    ),
    (
        "llm-tokenizers-datasets-bases",
        "llm-tokenizers.svg",
        "llm-tokenizers-illustration.jpg",
        "Texte, tokens, dataset, entrainement.",
    ),
    (
        "llm-finetuning-entrainer-modele",
        "llm-finetuning.svg",
        "llm-finetuning-illustration.jpg",
        "Adapter un modele avec tes donnees.",
    ),
    (
        "llm-gradio-demo-partager-modele",
        "llm-gradio.svg",
        "llm-gradio-illustration.jpg",
        "Montrer le modele avec une interface simple.",
    ),
    (
        "llm-finetuning-avance-lora-reasoning",
        "llm-lora-reasoning.svg",
        "llm-lora-illustration.jpg",
        "LoRA : adapter sans tout reecrire.",
    ),
    (
        "data-engineering-pipeline-end-to-end-intro",
        "data-eng-pipeline.svg",
        "data-eng-pipeline-illustration.jpg",
        "Sources, transform, entrepot, consommation.",
    ),
    (
        "data-engineering-docker-terraform-infra",
        "data-eng-docker-terraform.svg",
        "data-eng-docker-illustration.jpg",
        "Lab local Docker, infra cloud Terraform.",
    ),
    (
        "data-engineering-orchestration-kestra",
        "data-eng-orchestration.svg",
        "data-eng-orchestration-illustration.jpg",
        "Planifier, retenter, alerter.",
    ),
    (
        "data-engineering-ingestion-api-incremental",
        "data-eng-ingestion.svg",
        "data-eng-ingestion-illustration.jpg",
        "Charger le nouveau sans tout rejouer.",
    ),
    (
        "data-engineering-warehouse-bigquery",
        "data-eng-bigquery.svg",
        "data-eng-bigquery-illustration.jpg",
        "Raw, staging, marts - couche par couche.",
    ),
    (
        "data-engineering-dbt-analytics-engineering",
        "data-eng-dbt.svg",
        "data-eng-dbt-illustration.jpg",
        "SQL versionne, tests, docs.",
    ),
    (
        "data-engineering-spark-batch-processing",
        "data-eng-spark.svg",
        "data-eng-spark-illustration.jpg",
        "Gros volumes en batch avec Spark.",
    ),
    (
        "data-engineering-kafka-streaming",
        "data-eng-kafka.svg",
        "data-eng-kafka-illustration.jpg",
        "Evenements en continu avec Kafka.",
    ),
]


def accent_caption(s: str) -> str:
    reps = [
        ("taches", "tâches"),
        ("resultat", "résultat"),
        ("telecharger", "télécharger"),
        ("entrainement", "entraînement"),
        ("modele", "modèle"),
        ("donnees", "données"),
        ("reecrire", "réécrire"),
        ("entrepot", "entrepôt"),
        ("versionne", "versionné"),
        ("Evenements", "Événements"),
    ]
    for a, b in reps:
        s = s.replace(a, b)
    return s


def install_images() -> None:
    SCH.mkdir(parents=True, exist_ok=True)
    DIST_SCH.mkdir(parents=True, exist_ok=True)
    for _, _, illus, _ in MAP:
        src = SRC / illus
        if not src.exists():
            print("MISSING", illus)
            continue
        im = Image.open(src).convert("RGB")
        im.save(SCH / illus, "JPEG", quality=88, optimize=True)
        shutil.copy2(SCH / illus, DIST_SCH / illus)
        print("img", illus)


def inject() -> None:
    for slug, schema, illus, caption in MAP:
        path = ART / f"{slug}.md"
        if not path.exists():
            print("no article", slug)
            continue
        text = path.read_text(encoding="utf-8")
        if illus in text:
            print("skip", slug)
            continue
        # find first schema figure block and append illustration after it
        pattern = rf'(<figure class="schema-figure">\s*<img src="/assets/images/blog/schemas/{re.escape(schema)}"[\s\S]*?</figure>)'
        m = re.search(pattern, text)
        if not m:
            # softer: any first schema-figure
            m = re.search(r'(<figure class="schema-figure">[\s\S]*?</figure>)', text)
        if not m:
            print("no figure", slug)
            continue
        block = m.group(1)
        extra = (
            f'\n\n<figure class="schema-figure">\n'
            f'  <img src="/assets/images/blog/schemas/{illus}" alt="{accent_caption(caption)}" '
            f'class="schema-inline" width="800" loading="lazy" />\n'
            f'  <figcaption>{accent_caption(caption)}</figcaption>\n'
            f'</figure>'
        )
        text = text.replace(block, block + extra, 1)
        # widen first schema width if 640
        text = text.replace(
            f'src="/assets/images/blog/schemas/{schema}"',
            f'src="/assets/images/blog/schemas/{schema}"',
            1,
        )
        text = re.sub(
            rf'(src="/assets/images/blog/schemas/{re.escape(schema)}"[^>]*width=")640(")',
            r'\g<1>800\2',
            text,
            count=1,
        )
        path.write_text(text, encoding="utf-8")
        print("inject", slug)


def main() -> None:
    install_images()
    inject()
    print("OK")


if __name__ == "__main__":
    main()
