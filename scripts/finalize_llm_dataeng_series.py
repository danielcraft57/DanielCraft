#!/usr/bin/env python3
"""Finalise les series LLM + Data Engineering : OG, accents SVG, FAQ/nav articles.

Usage (racine du depot) :
    python scripts/finalize_llm_dataeng_series.py
    python scripts/finalize_llm_dataeng_series.py --skip-og
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = _SCRIPT_DIR.parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from _og_cartoon import render_og_card  # noqa: E402

ARTICLES = ROOT / "blog" / "content" / "articles"
SCHEMAS = ROOT / "assets" / "images" / "blog" / "schemas"
OG_DIR = ROOT / "assets" / "images" / "og"

LLM_ORDER = [
    "llm-nlp-vs-llm-comprendre-les-bases",
    "llm-transformers-pipeline-premiere-inference",
    "llm-architecture-encoder-decoder",
    "llm-huggingface-hub-modeles-datasets",
    "llm-tokenizers-datasets-bases",
    "llm-finetuning-entrainer-modele",
    "llm-gradio-demo-partager-modele",
    "llm-finetuning-avance-lora-reasoning",
]

DE_ORDER = [
    "data-engineering-pipeline-end-to-end-intro",
    "data-engineering-docker-terraform-infra",
    "data-engineering-orchestration-kestra",
    "data-engineering-ingestion-api-incremental",
    "data-engineering-warehouse-bigquery",
    "data-engineering-dbt-analytics-engineering",
    "data-engineering-spark-batch-processing",
    "data-engineering-kafka-streaming",
]

OG_META: dict[str, dict] = {
    "llm-nlp-vs-llm-comprendre-les-bases": {
        "title": "NLP vs LLM : la différence sans jargon",
        "subtitle": "Comprendre le terrain avant les modèles géants",
        "badge": "LLM",
        "scene": "code",
        "chips": ["NLP", "Transformers"],
    },
    "llm-transformers-pipeline-premiere-inference": {
        "title": "Pipeline Transformers : 1re inférence",
        "subtitle": "Classifier et générer en quelques lignes",
        "badge": "LLM",
        "scene": "code",
        "chips": ["pipeline()", "Hugging Face"],
    },
    "llm-architecture-encoder-decoder": {
        "title": "Encoder, decoder, encoder-decoder",
        "subtitle": "Choisir la bonne famille Transformer",
        "badge": "LLM",
        "scene": "gear",
        "chips": ["BERT", "GPT", "T5"],
    },
    "llm-huggingface-hub-modeles-datasets": {
        "title": "Hugging Face Hub : modèles et datasets",
        "subtitle": "Model cards, licences, téléchargement propre",
        "badge": "LLM",
        "scene": "browser",
        "chips": ["Hub", "Datasets"],
    },
    "llm-tokenizers-datasets-bases": {
        "title": "Tokenizers et Datasets",
        "subtitle": "Préparer le texte pour l'entraînement",
        "badge": "LLM",
        "scene": "code",
        "chips": ["BPE", "map()"],
    },
    "llm-finetuning-entrainer-modele": {
        "title": "Fine-tuning avec Trainer",
        "subtitle": "Adapter un modèle à ton métier",
        "badge": "LLM",
        "scene": "stats",
        "chips": ["Trainer", "metrics"],
    },
    "llm-gradio-demo-partager-modele": {
        "title": "Démo Gradio et Spaces",
        "subtitle": "Montrer ton modèle sans friction",
        "badge": "LLM",
        "scene": "browser",
        "chips": ["Gradio", "Spaces"],
    },
    "llm-finetuning-avance-lora-reasoning": {
        "title": "LoRA, PEFT et raisonnement",
        "subtitle": "Fine-tuning avancé sans tout réécrire",
        "badge": "LLM",
        "scene": "gear",
        "chips": ["LoRA", "PEFT"],
    },
    "data-engineering-pipeline-end-to-end-intro": {
        "title": "Pipeline data de bout en bout",
        "subtitle": "Sources, transformation, entrepôt, conso",
        "badge": "Data Eng",
        "scene": "process",
        "chips": ["ETL", "ELT"],
    },
    "data-engineering-docker-terraform-infra": {
        "title": "Docker et Terraform pour la data",
        "subtitle": "Lab local + infra cloud reproductible",
        "badge": "Data Eng",
        "scene": "gear",
        "chips": ["Docker", "IaC"],
    },
    "data-engineering-orchestration-kestra": {
        "title": "Orchestration : DAG et retries",
        "subtitle": "Planifier, surveiller, rejouer les jobs",
        "badge": "Data Eng",
        "scene": "process",
        "chips": ["Kestra", "Airflow"],
    },
    "data-engineering-ingestion-api-incremental": {
        "title": "Ingestion API incrémentale",
        "subtitle": "Full reload vs delta, normalisation",
        "badge": "Data Eng",
        "scene": "code",
        "chips": ["API", "idempotence"],
    },
    "data-engineering-warehouse-bigquery": {
        "title": "Warehouse BigQuery",
        "subtitle": "Partitioning, clustering, couches raw/stg",
        "badge": "Data Eng",
        "scene": "stats",
        "chips": ["BigQuery", "SQL"],
    },
    "data-engineering-dbt-analytics-engineering": {
        "title": "dbt et analytics engineering",
        "subtitle": "Modèles, tests, documentation SQL",
        "badge": "Data Eng",
        "scene": "code",
        "chips": ["dbt", "tests"],
    },
    "data-engineering-spark-batch-processing": {
        "title": "Spark : batch à grande échelle",
        "subtitle": "DataFrames, lazy eval, quand sortir du SQL",
        "badge": "Data Eng",
        "scene": "report",
        "chips": ["Spark", "batch"],
    },
    "data-engineering-kafka-streaming": {
        "title": "Kafka et streaming",
        "subtitle": "Topics, consumers, schémas Avro",
        "badge": "Data Eng",
        "scene": "process",
        "chips": ["Kafka", "Avro"],
    },
}

FAQ: dict[str, list[tuple[str, str]]] = {
    "llm-nlp-vs-llm-comprendre-les-bases": [
        ("Un LLM, c'est quoi en une phrase ?",
         "Un modele de langage de grande taille, entraine a predire des tokens, reutilisable sur plein de taches texte."),
        ("LLM et NLP, c'est la meme chose ?",
         "Non : le NLP est le champ. Un LLM est une famille de modeles NLP a grande echelle."),
        ("Par ou commencer si je debute ?",
         "Une tache claire + `pipeline()` Hugging Face, puis lire la model card avant de monter en GPU."),
    ],
    "llm-transformers-pipeline-premiere-inference": [
        ("C'est quoi `pipeline()` ?",
         "Une API haut niveau qui enchaine tokenizer, modele et post-traitement pour une tache donnee."),
        ("Ca marche en francais ?",
         "Oui si tu choisis un modele FR (ou multilingue) adapte - regarde la model card."),
        ("C'est assez pour la prod ?",
         "Parfait pour prototyper. En prod : versionner le modele, mesurer latence, ajouter garde-fous."),
    ],
    "llm-architecture-encoder-decoder": [
        ("Encoder vs decoder : comment choisir ?",
         "Encoder pour classer / extraire. Decoder pour generer. Encoder-decoder pour traduire / resumer conditionne."),
        ("BERT peut-il chatter ?",
         "Non comme un chat : BERT encode, il ne genere pas du dialogue libre comme un decoder."),
        ("T5 / BART, pour quoi faire ?",
         "Des taches sequence-to-sequence (traduction, resume) ou le design encoder-decoder reste naturel."),
    ],
    "llm-huggingface-hub-modeles-datasets": [
        ("Pourquoi lire la model card ?",
         "Licence, limites, biais, langues, taille : ca evite les mauvaises surprises en prod."),
        ("Ou sont caches les poids ?",
         "Dans le cache Hugging Face local (souvent `~/.cache/huggingface`), pas dans ton repo git."),
        ("Je peux tout reutiliser commercialement ?",
         "Non : chaque modele/dataset a sa licence. Verifie avant de livrer un client."),
    ],
    "llm-tokenizers-datasets-bases": [
        ("Pourquoi le tokenizer doit matcher le modele ?",
         "Le modele a ete entraine sur un vocabulaire precis. Un autre tokenizer casse la representation."),
        ("BPE, WordPiece, c'est quoi ?",
         "Des algos pour decouper le texte en sous-mots (tokens) sans exploser le vocabulaire."),
        ("Datasets sert a quoi ?",
         "Charger, mapper, filtrer et streamer des exemples vers l'entrainement sans reinventer la roue."),
    ],
    "llm-finetuning-entrainer-modele": [
        ("Quand fine-tuner plutot que prompt ?",
         "Quand tu as assez de donnees metier et besoin de stabilite / format de sortie."),
        ("C'est quoi Trainer ?",
         "La boucle d'entrainement Hugging Face : epochs, eval, checkpoints, logs."),
        ("Comment eviter l'overfitting ?",
         "Eval set, early stopping, pas trop d'epochs, et donnees diversifiees."),
    ],
    "llm-gradio-demo-partager-modele": [
        ("Gradio vs Space ?",
         "Gradio = l'UI Python. Space = l'hebergement Hub pour partager la demo."),
        ("Un Space gratuit suffit ?",
         "Pour une demo legere oui. Gros modeles : GPU payant ou inference distante."),
        ("Pourquoi une demo avant la prod ?",
         "Valider le besoin avec de vrais utilisateurs sans deployer toute une API."),
    ],
    "llm-finetuning-avance-lora-reasoning": [
        ("LoRA vs full fine-tune ?",
         "LoRA adapte peu de poids (adapters) : moins de VRAM, plus rapide a iterer."),
        ("Le rang LoRA, ca change quoi ?",
         "Plus le rang est haut, plus l'adapter est expressif (et couteux). Commence petit."),
        ("Raisonnement = plus de parametres ?",
         "Pas seulement : donnees de qualite, chaines de pensee, et evaluation humaine comptent autant."),
    ],
    "data-engineering-pipeline-end-to-end-intro": [
        ("Data engineer vs analyste ?",
         "L'engineer construit les tuyaux fiables. L'analyste consomme l'entrepot pour repondre metier."),
        ("ETL ou ELT ?",
         "ELT domine avec les warehouses cloud : load brut puis transform (dbt). ETL si tu nettoies avant."),
        ("C'est quoi \"production-ready\" ?",
         "Planifiable, observable, rejouable, secrets hors git - pas \"parfait\"."),
    ],
    "data-engineering-docker-terraform-infra": [
        ("Pourquoi Postgres en Docker ?",
         "Meme lab pour tout le monde, sans installer un SGBD sale sur Windows."),
        ("IaC, ca veut dire quoi ?",
         "Infrastructure as Code : bucket, dataset, IAM declares en fichiers versionnes."),
        ("Terraform des le jour 1 ?",
         "Oui pour 2-3 ressources. Non pour tout le cloud d'un coup."),
    ],
    "data-engineering-orchestration-kestra": [
        ("C'est quoi un DAG ?",
         "Un graphe de taches avec dependances : A puis B puis C, parallele quand possible."),
        ("Kestra ou Airflow ?",
         "Pour apprendre, prends l'outil du lab. En boite : competences equipe + managed cloud."),
        ("Retry = doublons ?",
         "Oui si l'ecriture n'est pas idempotente. Corrige le merge / overwrite avant."),
    ],
    "data-engineering-ingestion-api-incremental": [
        ("Full reload vs incremental ?",
         "Full = tout recharger. Incremental = seulement le delta depuis le dernier curseur."),
        ("Schema drift, c'est quoi ?",
         "Quand l'API change de champs sans prevenir. Il faut detecter et versionner."),
        ("Idempotence, pourquoi ?",
         "Relancer le job ne doit pas doubler les lignes dans l'entrepot."),
    ],
    "data-engineering-warehouse-bigquery": [
        ("Partition vs clustering ?",
         "Partition decoupe la table (souvent par date). Clustering ordonne dans la partition."),
        ("Pourquoi pas une base OLTP ?",
         "OLTP sert aux transactions. Le warehouse sert a l'analytique massif (scans, agregats)."),
        ("Couches raw / stg / marts ?",
         "Raw = brut. Staging = nettoye. Marts = pret metier. Ne melange pas."),
    ],
    "data-engineering-dbt-analytics-engineering": [
        ("dbt remplace l'ingestion ?",
         "Non : dbt transforme dans le warehouse. L'ingestion reste un autre job."),
        ("C'est quoi un test dbt ?",
         "Une assertion SQL (unique, not null, relations) executee sur tes modeles."),
        ("Pourquoi documenter les modeles ?",
         "Pour que le metier et les futurs toi comprennent sans archeologie."),
    ],
    "data-engineering-spark-batch-processing": [
        ("Quand sortir de BigQuery pour Spark ?",
         "Volumes / transforms trop lourds, formats complexes, ou cluster deja la."),
        ("Lazy evaluation, ca change quoi ?",
         "Spark planifie : rien ne tourne tant que tu n'appelles pas une action (count, write)."),
        ("DataFrame = table SQL ?",
         "Presque : colonnes nommees + API relationnelle, executee en distribue."),
    ],
    "data-engineering-kafka-streaming": [
        ("Topic, partition, offset ?",
         "Topic = flux. Partition = tranche parallele. Offset = curseur de lecture du consumer."),
        ("Pourquoi Avro + Schema Registry ?",
         "Contracter le format des messages et evoluer sans casser les consumers."),
        ("Batch vs streaming ?",
         "Batch = fenetres planifiees. Streaming = evenements continus. Souvent les deux coexistent."),
    ],
}

CODE_SNIPPETS: dict[str, str] = {
    "data-engineering-docker-terraform-infra": """
## Mini exemple Compose + Terraform

```yaml
# docker-compose.yml (extrait)
services:
  postgres:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: lab
      POSTGRES_DB: taxi
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
volumes:
  pgdata:
```

```hcl
# main.tf (extrait conceptuel)
resource "google_storage_bucket" "raw" {
  name     = "mon-lab-raw-2026"
  location = "EU"
}

resource "google_bigquery_dataset" "raw" {
  dataset_id = "raw_taxi"
  location   = "EU"
}
```

Pin les versions, isole le lab, et ne commit jamais de credentials.
""",
    "data-engineering-orchestration-kestra": """
## Mini flow (esprit Kestra / YAML)

```yaml
id: nightly_orders
namespace: company.lab
tasks:
  - id: extract
    type: io.kestra.plugin.scripts.python.Script
    script: |
      print("extract orders for {{ inputs.date }}")
  - id: load_bq
    type: io.kestra.plugin.gcp.bigquery.Load
    # ... config dataset / table
triggers:
  - id: schedule
    type: io.kestra.plugin.core.trigger.Schedule
    cron: "0 3 * * *"
```

L'important : une date logique en entree, des taches chainees, un cron unique.
""",
    "data-engineering-ingestion-api-incremental": """
## Mini extract Python (curseur)

```python
import requests
from datetime import datetime, timezone

def fetch_since(cursor: str, api_url: str, token: str) -> list[dict]:
    \"\"\"Recupere les evenements plus recents que le curseur ISO.\"\"\"
    r = requests.get(
        api_url,
        headers={"Authorization": f"Bearer {token}"},
        params={"updated_after": cursor, "limit": 500},
        timeout=30,
    )
    r.raise_for_status()
    return r.json().get("items", [])

def next_cursor(rows: list[dict], fallback: str) -> str:
    if not rows:
        return fallback
    return max(row["updated_at"] for row in rows)

# Persiste le curseur (table state / fichier versionne) apres un load reussi.
```
""",
    "data-engineering-warehouse-bigquery": """
## Mini SQL BigQuery

```sql
CREATE TABLE IF NOT EXISTS raw.orders (
  order_id STRING,
  customer_id STRING,
  amount NUMERIC,
  ordered_at TIMESTAMP
)
PARTITION BY DATE(ordered_at)
CLUSTER BY customer_id;

-- Couche staging : types et nulls nettoyes
CREATE OR REPLACE TABLE stg.orders AS
SELECT
  order_id,
  customer_id,
  amount,
  ordered_at
FROM raw.orders
WHERE order_id IS NOT NULL;
```
""",
    "data-engineering-dbt-analytics-engineering": """
## Mini modele dbt

```sql
-- models/staging/stg_orders.sql
with source as (
  select * from {{ source('raw', 'orders') }}
)
select
  order_id,
  customer_id,
  amount::numeric as amount,
  ordered_at::timestamp as ordered_at
from source
```

```yaml
# models/staging/schema.yml (extrait)
models:
  - name: stg_orders
    columns:
      - name: order_id
        tests: [unique, not_null]
      - name: amount
        tests: [not_null]
```
""",
    "data-engineering-kafka-streaming": """
## Mini producer / consumer (esprit)

```python
# Producer (pseudo)
from confluent_kafka import SerializingProducer

producer.produce(
    topic="orders.events",
    key=order_id,
    value={"order_id": order_id, "amount": 42.5, "ts": ts},
)
producer.flush()

# Consumer : commit l'offset apres ecriture idempotente vers le warehouse
```

En vrai lab : Schema Registry + Avro (ou Protobuf), pas du JSON libre sans contrat.
""",
}

TITLE_FIXES: dict[str, dict[str, str]] = {
    "llm-nlp-vs-llm-comprendre-les-bases": {
        "title": "NLP vs LLM : comprendre la difference sans jargon",
        "title_accent": "NLP vs LLM : comprendre la difference sans jargon",
        "h1": "NLP vs LLM : comprendre la difference sans jargon",
        "excerpt": "NLP, LLM, Transformers : ce qui change vraiment, et par ou commencer pour pratiquer.",
        "excerpt_fix": "NLP, LLM, Transformers : ce qui change vraiment, et par ou commencer pour pratiquer.",
    },
}

# Accents corrects (apostrophe droite)
ACCENT_TITLE = {
    "llm-nlp-vs-llm-comprendre-les-bases": {
        "old_title": 'title: "NLP vs LLM : comprendre la difference sans jargon"',
        "new_title": 'title: "NLP vs LLM : comprendre la difference sans jargon"',
        # will fix difference -> différence below via generic replace
    },
}


def _nav_block(order: list[str], slug: str) -> str:
    idx = order.index(slug)
    lines = ["\n---\n\n## Navigation dans la serie\n"]
    if idx > 0:
        prev = order[idx - 1]
        prev_title = _read_title(prev)
        lines.append(f"- Precedent : [{prev_title}](/blog/articles/{prev}.html)")
    if idx < len(order) - 1:
        nxt = order[idx + 1]
        nxt_title = _read_title(nxt)
        lines.append(f"- Suivant : [{nxt_title}](/blog/articles/{nxt}.html)")
    else:
        lines.append("- Fin de la serie - tu peux relire l'intro ou croiser avec l'autre parcours (LLM / data).")
    return "\n".join(lines) + "\n"


def _read_title(slug: str) -> str:
    path = ARTICLES / f"{slug}.md"
    text = path.read_text(encoding="utf-8")
    m = re.search(r'^title:\s*"(.*)"\s*$', text, re.M)
    return m.group(1) if m else slug


def _faq_block(slug: str) -> str:
    items = FAQ.get(slug, [])
    if not items:
        return ""
    lines = ["\n---\n\n## Questions frequentes (FAQ)\n"]
    for q, a in items:
        lines.append(f"**{q}** {a}\n")
    return "\n".join(lines)


def _apply_text_fixes(text: str, slug: str) -> str:
    replacements = [
        ("comprendre la difference", "comprendre la difference"),  # placeholder
        ("comprendre la difference", "comprendre la différence"),
        ("par ou commencer", "par où commencer"),
        ("alt=\"Schema ", "alt=\"Schéma "),
        ("alt=\"Schema", "alt=\"Schéma"),
        ("a grande echelle", "à grande échelle"),
        ("modeles NLP", "modèles NLP"),
        ("famille de modeles", "famille de modèles"),
        ("moins de linker oubliés", "moins de liens oubliés"),
        ("je parte souvent", "je pars souvent"),
        ("tu casse ", "tu casses "),
        ("schemas Avro", "schémas Avro"),
        ("Schema pipeline", "Schéma pipeline"),
        ("Schema ingestion", "Schéma ingestion"),
        ("Schema Spark", "Schéma Spark"),
        ("Schema Kafka", "Schéma Kafka"),
        ("Schema BigQuery", "Schéma BigQuery"),
        ("Schema dbt", "Schéma dbt"),
        ("Schema infra", "Schéma infra"),
        ("Schema orchestration", "Schéma orchestration"),
        ("entrepot", "entrepôt"),
        ("Entrepot", "Entrepôt"),
        ("Questions frequentes", "Questions fréquentes"),
        ("Navigation dans la serie", "Navigation dans la série"),
        ("Precedent :", "Précédent :"),
        ("Fin de la serie", "Fin de la série"),
        ("# Schema typique apres", "# Schéma typique après"),
        ("# depend du modele", "# dépend du modèle"),
        ("est arrive direct", "est arrivé direct"),
        ("meme_repo_que_le_modele", "meme_repo_que_le_modele"),
    ]
    # Fix double-application of entrepôt in URLs? Avoid replacing in code carefully.
    for old, new in replacements:
        if old != new:
            text = text.replace(old, new)
    # Undo entrepôt inside english tech if any - rare
    return text


def polish_article(slug: str, order: list[str]) -> None:
    path = ARTICLES / f"{slug}.md"
    text = path.read_text(encoding="utf-8")
    text = _apply_text_fixes(text, slug)

    # Specific H1/title for NLP article
    if slug == "llm-nlp-vs-llm-comprendre-les-bases":
        text = text.replace(
            'title: "NLP vs LLM : comprendre la difference sans jargon"',
            'title: "NLP vs LLM : comprendre la différence sans jargon"',
        )
        text = text.replace(
            "# NLP vs LLM : comprendre la difference sans jargon",
            "# NLP vs LLM : comprendre la différence sans jargon",
        )
        text = text.replace(
            'excerpt: "NLP, LLM, Transformers : ce qui change vraiment, et par ou commencer pour pratiquer."',
            'excerpt: "NLP, LLM, Transformers : ce qui change vraiment, et par où commencer pour pratiquer."',
        )

    if slug == "data-engineering-kafka-streaming":
        text = text.replace("schemas Avro", "schémas Avro")
        text = text.replace("Schemas Avro", "Schémas Avro")

    # Insert code snippets before "## En résumé" or "## Lien avec" or end
    snippet = CODE_SNIPPETS.get(slug)
    if snippet and snippet.strip() not in text and "Mini exemple" not in text and "Mini flow" not in text and "Mini extract" not in text and "Mini SQL" not in text and "Mini modele" not in text and "Mini producer" not in text:
        markers = [
            "\n## En résumé\n",
            "\n## En resume\n",
            "\n## Lien avec la suite",
            "\n## Pour la suite",
            "\n## Ce que tu emportes",
            "\n## Prochaine étape",
        ]
        inserted = False
        for marker in markers:
            if marker in text:
                text = text.replace(marker, "\n" + snippet.strip() + "\n" + marker, 1)
                inserted = True
                break
        if not inserted:
            text = text.rstrip() + "\n\n" + snippet.strip() + "\n"

    # FAQ + nav once
    if "## Questions fréquentes (FAQ)" not in text and "## Questions frequentes (FAQ)" not in text:
        faq = _faq_block(slug).replace("Questions frequentes", "Questions fréquentes")
        text = text.rstrip() + "\n" + faq

    if "## Navigation dans la série" not in text and "## Navigation dans la serie" not in text:
        idx = order.index(slug)
        lines = ["\n---\n\n## Navigation dans la série\n"]
        if idx > 0:
            prev = order[idx - 1]
            lines.append(f"- Précédent : [{_read_title(prev)}](/blog/articles/{prev}.html)")
        if idx < len(order) - 1:
            nxt = order[idx + 1]
            lines.append(f"- Suivant : [{_read_title(nxt)}](/blog/articles/{nxt}.html)")
        else:
            lines.append(
                "- Fin de la série - tu peux relire l'intro ou croiser avec l'autre parcours (LLM / data)."
            )
        text = text.rstrip() + "\n" + "\n".join(lines) + "\n"

    # Final accent pass on FAQ answers written without accents in FAQ dict - fix common words
    faq_accents = [
        ("modele", "modèle"),
        ("modeles", "modèles"),
        ("entraine", "entraîné"),
        ("predire", "prédire"),
        ("reutilisable", "réutilisable"),
        ("taches", "tâches"),
        ("meme chose", "même chose"),
        ("echelle", "échelle"),
        ("Par ou", "Par où"),
        ("debute", "débutes"),
        ("Ca marche", "Ça marche"),
        ("francais", "français"),
        ("adapte", "adapté"),
        ("generer", "générer"),
        ("resumer", "résumer"),
        ("conditionne", "conditionné"),
        ("telechargement", "téléchargement"),
        ("Ou sont", "Où sont"),
        ("caches", "cachés"),
        ("decouper", "découper"),
        ("sous-mots", "sous-mots"),
        ("entrainement", "entraînement"),
        ("plutot", "plutôt"),
        ("donnees", "données"),
        ("metier", "métier"),
        ("hebergement", "hébergement"),
        ("legere", "légère"),
        ("parametres", "paramètres"),
        ("pensee", "pensée"),
        ("evaluation", "évaluation"),
        ("entrepot", "entrepôt"),
        ("repondre", "répondre"),
        ("rejouable", "rejouable"),
        ("declarees", "déclarées"),
        ("versionnes", "versionnés"),
        ("dependances", "dépendances"),
        ("parallele", "parallèle"),
        ("ecriture", "écriture"),
        ("evenements", "événements"),
        ("recents", "récents"),
        ("Persiste", "Persiste"),
        ("decoupe", "découpe"),
        ("agregats", "agrégats"),
        ("nettoye", "nettoyé"),
        ("archeologie", "archéologie"),
        ("deja", "déjà"),
        ("nommees", "nommées"),
        ("executee", "exécutée"),
        ("distribue", "distribué"),
        ("evoluer", "évoluer"),
        ("evenements continus", "événements continus"),
        ("fenetres", "fenêtres"),
        ("planifiees", "planifiées"),
    ]
    # Only accent-fix the FAQ section to avoid breaking code identifiers
    if "## Questions fréquentes (FAQ)" in text:
        pre, post = text.split("## Questions fréquentes (FAQ)", 1)
        if "## Navigation dans la série" in post:
            faq_part, nav_part = post.split("## Navigation dans la série", 1)
            for old, new in faq_accents:
                faq_part = faq_part.replace(old, new)
            text = pre + "## Questions fréquentes (FAQ)" + faq_part + "## Navigation dans la série" + nav_part
        else:
            for old, new in faq_accents:
                post = post.replace(old, new)
            text = pre + "## Questions fréquentes (FAQ)" + post

    path.write_text(text, encoding="utf-8")
    print(f"  polish {slug}")


def fix_schemas() -> None:
    replacements = [
        ("modeles", "modèles"),
        ("a grande echelle", "à grande échelle"),
        ("Taches", "Tâches"),
        ("entrepot", "entrepôt"),
        ("Entrepot", "Entrepôt"),
        ("Schema ", "Schéma "),
        ("incremental", "incrémental"),
        ("Incremental", "Incrémental"),
    ]
    for path in SCHEMAS.glob("llm-*.svg"):
        t = path.read_text(encoding="utf-8")
        orig = t
        for old, new in replacements:
            t = t.replace(old, new)
        if t != orig:
            path.write_text(t, encoding="utf-8")
            print(f"  schema {path.name}")
    for path in SCHEMAS.glob("data-eng-*.svg"):
        t = path.read_text(encoding="utf-8")
        orig = t
        for old, new in replacements:
            # Keep Schema Registry as English if present as full phrase
            t = t.replace(old, new)
        t = t.replace("Schéma Registry", "Schema Registry")
        if t != orig:
            path.write_text(t, encoding="utf-8")
            print(f"  schema {path.name}")


def generate_og() -> None:
    OG_DIR.mkdir(parents=True, exist_ok=True)
    # Prefer scenes that exist
    available_scenes = None
    try:
        from _og_cartoon import SCENES

        available_scenes = set(SCENES.keys())
    except Exception:
        available_scenes = set()

    for slug, meta in OG_META.items():
        scene = meta.get("scene", "browser")
        if available_scenes and scene not in available_scenes:
            scene = "browser" if "browser" in available_scenes else next(iter(available_scenes), "browser")
        img = render_og_card(
            title=meta["title"],
            subtitle=meta.get("subtitle", ""),
            badge=meta.get("badge", "DanielCraft"),
            chips=meta.get("chips"),
            scene=scene,
            cta="Lire l'article →",
            color="#4da9d6",
        )
        out = OG_DIR / f"{slug}-1200x630.jpg"
        img.save(out, "JPEG", quality=88, optimize=True)
        print(f"  og {out.name} ({out.stat().st_size // 1024} Ko)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-og", action="store_true")
    ap.add_argument("--skip-polish", action="store_true")
    args = ap.parse_args()

    print("== schemas ==")
    fix_schemas()

    if not args.skip_polish:
        print("== articles LLM ==")
        for slug in LLM_ORDER:
            polish_article(slug, LLM_ORDER)
        print("== articles Data Eng ==")
        for slug in DE_ORDER:
            polish_article(slug, DE_ORDER)

    if not args.skip_og:
        print("== OG images ==")
        generate_og()

    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
