#!/usr/bin/env python3
"""Reecrit les articles LLM + Data Eng dans le ton simple de la serie Agents."""
from __future__ import annotations

from pathlib import Path

ART = Path(__file__).resolve().parent.parent / "blog" / "content" / "articles"

HF_LLM = "https://huggingface.co/learn/llm-course"
ZOOM = "https://github.com/DataTalksClub/data-engineering-zoomcamp"

ARTICLES: dict[str, dict] = {}


def fig(svg: str, alt_svg: str, cap_svg: str, jpg: str, alt_jpg: str, cap_jpg: str) -> str:
    return f"""<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/{svg}" alt="{alt_svg}" class="schema-inline" width="800" />
  <figcaption>{cap_svg}</figcaption>
</figure>

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/{jpg}" alt="{alt_jpg}" class="schema-inline" width="800" loading="lazy" />
  <figcaption>{cap_jpg}</figcaption>
</figure>"""


def pack(
    slug: str,
    title: str,
    date: str,
    excerpt: str,
    tags: list[str],
    series: str,
    order: int,
    og: str,
    body: str,
) -> None:
    tags_s = ", ".join(f'"{t}"' for t in tags)
    md = f"""---
title: "{title}"
date: {date}
excerpt: "{excerpt}"
type: tutorial
tags: [{tags_s}]
series: {series}
series_order: {order}
og_image: {og}
---

# {title}

{body}
"""
    ARTICLES[slug] = md


# ---------------------------------------------------------------------------
# LLM
# ---------------------------------------------------------------------------

pack(
    "llm-nlp-vs-llm-comprendre-les-bases",
    "NLP vs LLM : comprendre la différence sans jargon",
    "2026-10-01",
    "NLP, LLM, Transformers : ce qui change vraiment, explique simplement, avec un exemple concret.",
    ["LLM", "NLP", "Transformers", "Hugging Face", "formation", "débutant"],
    "llm-transformers-serie",
    1,
    "llm-nlp-vs-llm-comprendre-les-bases-1200x630.jpg",
    fig(
        "llm-nlp-vs-llm.svg",
        "Schéma NLP, tâches, Transformers, LLM",
        "Quatre cases : le terrain, les tâches, l'architecture, le gros modèle.",
        "llm-nlp-vs-llm-illustration.jpg",
        "NLP, tâches, Transformers, LLM - en image.",
        "Même idée en image : du terrain NLP au LLM.",
    )
    + f"""

Tu croises NLP, LLM, Transformers partout. Trois mots collés, souvent sans vraiment dire ce qui change. Ici on va doucement. Tu n'as pas besoin d'être ingénieur pour suivre.

Cette série s'inspire du [cours LLM Hugging Face]({HF_LLM}). Le texte est original, en français, clarté d'abord.

## L'idée en une phrase

**NLP** = le terrain (faire comprendre / produire du texte à une machine).  
**Transformer** = une façon de construire le modèle.  
**LLM** = un gros modèle de langage, souvent basé sur cette architecture.

## NLP, c'est quoi ?

Le NLP (traitement du langage), c'est toutes les méthodes pour qu'une machine lise, classe ou écrive du texte.

Exemples concrets :
- avis client positif ou négatif ;
- trouver un nom, une date, une ville dans un mail ;
- traduire ;
- résumer ;
- répondre à une question.

Avant, on faisait souvent **un modèle par tâche**. Un pour le sentiment, un autre pour la traduction. Ça marchait, mais c'était lourd à maintenir.

## LLM, c'est quoi ?

Un **LLM** (gros modèle de langage), c'est un modèle entraîné sur énormément de texte. Il apprend à prédire le **prochain morceau** (on dit token).

Ce n'est pas magique. C'est toujours du NLP - juste à plus grande échelle.

Ce qui change pour toi :
- un même modèle peut faire plusieurs choses via une consigne (le prompt) ;
- tu peux l'adapter à ton métier (fine-tuning) ;
- l'écosystème (Hub, démos) rend les essais plus accessibles.

## Et les Transformers ?

C'est l'architecture derrière beaucoup de modèles modernes (depuis 2017). L'idée clé : l'**attention** - le modèle regarde tout le contexte utile en parallèle, au lieu de lire mot à mot comme avant.

Tu croises des familles :
- **encoder** : comprendre / classer ;
- **decoder** : générer du texte ;
- **les deux** : traduire / résumer.

On détaille ça dans un prochain article.

## Différence qui compte vraiment

| | NLP spécialisé | LLM généraliste |
|---|---|---|
| Sortie | souvent une étiquette claire | texte libre (parfois inventé) |
| Données | beaucoup de labels par tâche | gros pré-entraînement, puis un peu de métier |
| Coût | souvent léger | peut demander GPU / budget |
| Contrôle | prévisible | il faut des garde-fous |

Règle simple : si tu veux juste classer des avis, commence petit. Si tu veux un assistant qui rédige, regarde du côté LLM - avec validation humaine.

## Premier contact (idée)

Avec Hugging Face, tu peux tester une classification en quelques lignes (`pipeline`). On le fait proprement dans l'article suivant. Ici, retiens juste : tu n'as pas besoin de tout comprendre avant d'essayer une petite tâche claire.

## Par où démarrer

1. choisis **une** tâche (classer, résumer, chatter) ;
2. teste un petit modèle via `pipeline` ;
3. lis la fiche du modèle (model card) ;
4. monte ensuite : tokenizers, fine-tuning, démo.

Côté DanielCraft : j'utilise l'IA pour aller plus vite, et je contrôle avant de livrer. Même logique avec un LLM.

## En résumé

NLP = le champ. Transformers = l'architecture dominante. LLM = gros modèles NLP polyvalents.  
Commence simple. Une tâche claire bat un jargon impressionnant.

Prochaine étape : ta première inférence avec `pipeline()`.

---

## Questions fréquentes (FAQ)

**Un LLM, c'est du NLP ?** Oui. C'est une famille de modèles NLP à grande échelle.

**Faut-il un énorme modèle ?** Non. Pour classer des avis, un petit modèle suffit souvent.

**Par où commencer ?** Une tâche claire + `pipeline()` Hugging Face.

**Ça remplace mon métier ?** Non. Ça accélère. Toi tu valides.

---

## Navigation dans la série

- Suivant : [Pipeline Hugging Face : ta première inférence](/blog/articles/llm-transformers-pipeline-premiere-inference.html)
""",
)

pack(
    "llm-transformers-pipeline-premiere-inference",
    "Pipeline Hugging Face : ta première inférence",
    "2026-10-02",
    "Lancer une classification ou une génération en quelques lignes, sans usine à gaz.",
    ["LLM", "Transformers", "pipeline", "Hugging Face", "formation", "débutant"],
    "llm-transformers-serie",
    2,
    "llm-transformers-pipeline-premiere-inference-1200x630.jpg",
    fig(
        "llm-pipeline.svg",
        "Schéma pipeline Hugging Face",
        "Texte → pipeline → modèle → résultat.",
        "llm-pipeline-illustration.jpg",
        "De ta phrase au résultat via pipeline().",
        "Une ligne qui prépare le modèle et te rend un résultat.",
    )
    + f"""

Tu veux un résultat tout de suite, pas un cours de trois heures. `pipeline()` chez Hugging Face sert exactement à ça : tu donnes une tâche + un texte, tu récupères une sortie.

Inspiration : [cours LLM Hugging Face]({HF_LLM}). Texte original, français simple.

## L'idée en une phrase

**pipeline** = un raccourci qui charge le modèle, le tokenizer, et lance le calcul pour toi.

## Installer le minimum

```bash
pip install transformers
```

Selon le modèle, tu pourras aussi avoir besoin de `torch` (ou d'un backend compatible). Lis toujours la fiche du modèle.

## Classification en 4 lignes

```python
from transformers import pipeline

clf = pipeline("sentiment-analysis")
print(clf("Ce magasin est super, j'y retourne."))
```

Tu obtiens en gros un label (positif / négatif) et un score. C'est déjà utile pour trier des avis.

## Génération (idée)

```python
gen = pipeline("text-generation", model="gpt2")
print(gen("Aujourd'hui à Metz,", max_new_tokens=40))
```

Attention : un petit modèle de démo invente facilement. Pour un vrai usage métier, choisis un modèle adapté et **relis** la sortie.

## Ce qui se passe sous le capot

1. ton texte arrive ;
2. le tokenizer le découpe en tokens ;
3. le modèle calcule ;
4. la sortie est retransformée en label ou en texte.

`pipeline` cache ces étapes. Plus tard, tu les verras une par une.

## Pièges fréquents

- lancer un modèle trop gros sur une machine trop petite ;
- ignorer la langue du modèle (anglais vs français) ;
- croire que le score = vérité absolue ;
- coller la sortie telle quelle sur un site client sans relecture.

## En résumé

`pipeline` = le plus court chemin pour tester. Une tâche, un texte, un résultat. Ensuite tu peaufines.

---

## Questions fréquentes (FAQ)

**Ça marche hors ligne ?** Après le premier téléchargement du modèle, souvent oui (selon ta config).

**Quel modèle choisir ?** Commence petit, lis la model card, teste sur tes vrais textes.

**Faut-il un GPU ?** Pas pour démarrer sur des petits modèles.

---

## Navigation dans la série

- Précédent : [NLP vs LLM](/blog/articles/llm-nlp-vs-llm-comprendre-les-bases.html)
- Suivant : [Encoder, decoder : quelle architecture ?](/blog/articles/llm-architecture-encoder-decoder.html)
""",
)

pack(
    "llm-architecture-encoder-decoder",
    "Encoder, decoder : quelle architecture choisir ?",
    "2026-10-03",
    "Comprendre encoder, decoder et encoder-decoder sans slide illisible - pour choisir selon ton besoin.",
    ["LLM", "Transformers", "architecture", "encoder", "decoder", "formation"],
    "llm-transformers-serie",
    3,
    "llm-architecture-encoder-decoder-1200x630.jpg",
    fig(
        "llm-architecture.svg",
        "Schéma encoder decoder encoder-decoder",
        "Trois familles, un choix selon le besoin.",
        "llm-architecture-illustration.jpg",
        "Encoder, decoder, ou les deux.",
        "Même idée en image : choisir la bonne famille.",
    )
    + f"""

Tu n'as pas besoin de redessiner le papier Attention Is All You Need. Tu as besoin de savoir **quoi choisir** pour ton cas.

Inspiration : [cours LLM HF]({HF_LLM}).

## L'idée en une phrase

- **Encoder** : comprendre / classer / extraire.  
- **Decoder** : générer la suite.  
- **Les deux** : lire d'un côté, écrire de l'autre (traduire, résumer).

## Encoder (comprendre)

Tu donnes un texte, tu veux une **étiquette** ou une info structurée.

Exemples : sentiment, spam ou pas, type de demande client.

Famille connue : modèles type BERT / DistilBERT.

## Decoder (générer)

Tu veux du **texte qui continue** : réponse, brouillon, reformulation.

Famille connue : modèles type GPT.

Point de vigilance : il peut inventer. Garde une relecture.

## Encoder-decoder (les deux)

Tu as une **entrée** et une **sortie** liées : traduction, résumé conditionné, reformulation cadrée.

Famille connue : T5, BART.

## Comment choisir (boutique)

- « Classe mes avis 1 à 5 » → encoder.  
- « Propose un mail de réponse » → decoder (avec validation).  
- « Résume cette fiche produit en 3 lignes » → souvent encoder-decoder ou un bon modèle instructionné.

## En résumé

L'architecture suit le besoin, pas la mode. Classe → encoder. Génère → decoder. Transforme A en B → souvent les deux.

---

## Questions fréquentes (FAQ)

**Je peux tout faire avec un gros decoder ?** Souvent oui en démo, pas toujours optimal en coût / contrôle.

**BERT est mort ?** Non. Pour classer, ça reste très solide.

---

## Navigation dans la série

- Précédent : [Pipeline](/blog/articles/llm-transformers-pipeline-premiere-inference.html)
- Suivant : [Le Hub Hugging Face](/blog/articles/llm-huggingface-hub-modeles-datasets.html)
""",
)

pack(
    "llm-huggingface-hub-modeles-datasets",
    "Le Hub Hugging Face : modèles et datasets",
    "2026-10-04",
    "Chercher un modèle, lire sa fiche, télécharger un dataset - le réflexe avant de coder.",
    ["Hugging Face", "Hub", "modèles", "datasets", "LLM", "formation"],
    "llm-transformers-serie",
    4,
    "llm-huggingface-hub-modeles-datasets-1200x630.jpg",
    fig(
        "llm-hub.svg",
        "Schéma Hub Hugging Face",
        "Chercher, lire, télécharger, réutiliser.",
        "llm-hub-illustration.jpg",
        "Chercher, lire la model card, télécharger.",
        "Le Hub comme un catalogue clair.",
    )
    + f"""

Le Hub, c'est le catalogue : modèles, datasets, démos. Avant de coder trois heures, tu regardes ce qui existe déjà.

## L'idée en une phrase

**Cherche → lis la fiche → teste petit → intègre.**

## Model card : lis avant de télécharger

Sur la page d'un modèle, regarde :
- la tâche (classification, génération…) ;
- la langue ;
- la licence ;
- les limites / biais signalés ;
- la taille (ça tient sur ta machine ?).

Si la fiche est vide ou confuse, méfiance.

## Datasets

Même logique : d'où viennent les données, licence, colonnes, qualité. Un beau nom ne garantit rien.

## Bon réflexe DanielCraft

Je ne colle pas un modèle inconnu en prod. Je teste sur **tes** textes (avis, mails, FAQ). Si ça se trompe trop, on change - ou on fine-tune plus tard.

## En résumé

Le Hub accélère. La model card te protège. Lis avant de télécharger.

---

## Questions fréquentes (FAQ)

**Tout est gratuit ?** Beaucoup est ouvert. Lis licence et conditions d'usage.

**Je peux publier mon modèle ?** Oui, quand tu es prêt - avec une vraie fiche.

---

## Navigation dans la série

- Précédent : [Architectures](/blog/articles/llm-architecture-encoder-decoder.html)
- Suivant : [Tokenizers et datasets](/blog/articles/llm-tokenizers-datasets-bases.html)
""",
)

pack(
    "llm-tokenizers-datasets-bases",
    "Tokenizers et datasets : préparer le texte",
    "2026-10-05",
    "Découper le texte en tokens et ranger tes exemples : la base avant tout entraînement.",
    ["tokenizers", "datasets", "LLM", "Hugging Face", "formation", "débutant"],
    "llm-transformers-serie",
    5,
    "llm-tokenizers-datasets-bases-1200x630.jpg",
    fig(
        "llm-tokenizers.svg",
        "Schéma tokenizers et datasets",
        "Texte → tokens → dataset → entraînement.",
        "llm-tokenizers-illustration.jpg",
        "Texte, tokens, dataset, entraînement.",
        "Préparer proprement avant d'apprendre.",
    )
    + """

Le modèle ne lit pas des phrases comme toi. Il lit des **tokens** (morceaux). Et pour apprendre, il a besoin d'exemples bien rangés.

## L'idée en une phrase

**Tokenizer** = découpe le texte. **Dataset** = tes exemples prêts.

## Pourquoi ça compte

Mauvais tokenizer / mauvais découpage → résultats bizarres.  
Dataset sale (doublons, labels faux) → modèle qui apprend n'importe quoi.

## Ce que tu fais concrètement

1. tu as des textes + labels (ou paires entrée/sortie) ;
2. tu tokenizes comme le modèle s'y attend ;
3. tu ranges ça dans un dataset (souvent via la lib `datasets`) ;
4. tu lances l'entraînement ou l'évaluation.

## Conseil terrain

Pour un commerce : 200 avis bien labellisés valent mieux que 10 000 lignes douteuses. Qualité > volume bruité.

## En résumé

Tokens = langage machine. Dataset = ta matière première. Propre avant rapide.

---

## Questions fréquentes (FAQ)

**Je dois écrire mon tokenizer ?** Rarement. Tu réutilises celui du modèle.

**Combien d'exemples ?** Ça dépend. Commence petit, mesure, puis enrichis.

---

## Navigation dans la série

- Précédent : [Hub](/blog/articles/llm-huggingface-hub-modeles-datasets.html)
- Suivant : [Fine-tuning](/blog/articles/llm-finetuning-entrainer-modele.html)
""",
)

pack(
    "llm-finetuning-entrainer-modele",
    "Fine-tuning : adapter un modèle à ton métier",
    "2026-10-06",
    "Partir d'un modèle déjà entraîné et l'adapter avec tes exemples - sans tout réinventer.",
    ["fine-tuning", "LLM", "Trainer", "Hugging Face", "formation"],
    "llm-transformers-serie",
    6,
    "llm-finetuning-entrainer-modele-1200x630.jpg",
    fig(
        "llm-finetuning.svg",
        "Schéma fine-tuning",
        "Modèle de base + tes données → modèle adapté.",
        "llm-finetuning-illustration.jpg",
        "Adapter un modèle avec tes données.",
        "Le métier entre dans le modèle, pas l'inverse.",
    )
    + """

Fine-tuning = tu prends un modèle qui sait déjà lire/écrire, et tu lui montres **tes** exemples pour qu'il s'aligne sur ton cas.

## L'idée en une phrase

**Pas tout reconstruire : adapter.**

## Quand c'est utile

- tes libellés métier ne sont pas dans le modèle général ;
- le prompt seul ne suffit pas ;
- tu as un minimum d'exemples propres.

## Quand ce n'est pas la première option

- tu n'as presque aucune donnée ;
- un petit classifieur dédié suffit ;
- tu peux résoudre le besoin avec des règles + un outil (souvent pour les agents).

## Déroulé simple

1. modèle de base choisi ;
2. dataset propre ;
3. entraînement (Trainer ou équivalent) ;
4. évaluation sur des cas réels ;
5. checkpoint sauvegardé.

## En résumé

Fine-tuning = spécialisation contrôlée. Données propres d'abord, GPU ensuite.

---

## Questions fréquentes (FAQ)

**Ça écrase le modèle de base ?** Tu produis une version adaptée (checkpoint). Garde une trace de la base.

**Combien de temps ?** De minutes à heures selon taille et machine.

---

## Navigation dans la série

- Précédent : [Tokenizers](/blog/articles/llm-tokenizers-datasets-bases.html)
- Suivant : [Démo Gradio](/blog/articles/llm-gradio-demo-partager-modele.html)
""",
)

pack(
    "llm-gradio-demo-partager-modele",
    "Gradio : montrer ton modèle facilement",
    "2026-10-07",
    "Une petite interface web pour tester et partager ton modèle, sans refaire tout un site.",
    ["Gradio", "Spaces", "Hugging Face", "démo", "LLM", "formation"],
    "llm-transformers-serie",
    7,
    "llm-gradio-demo-partager-modele-1200x630.jpg",
    fig(
        "llm-gradio.svg",
        "Schéma Gradio Spaces",
        "Modèle → interface → partage → feedback.",
        "llm-gradio-illustration.jpg",
        "Montrer le modèle avec une interface simple.",
        "Une démo claire pour faire tester.",
    )
    + """

Tu as un modèle qui marche en script. Cool. Pour le faire tester à un client ou un collègue, une petite interface aide beaucoup. Gradio sert à ça.

## L'idée en une phrase

**Entrée texte → bouton → sortie visible.** Sans refaire un site complet.

## Pourquoi c'est utile

- tu vois les cas limites tout de suite ;
- quelqu'un d'autre peut cliquer sans installer Python ;
- tu récoltes du feedback avant d'intégrer en prod.

## Spaces

Sur Hugging Face, tu peux héberger une démo (Space). Pratique pour un proto. Pour un vrai produit client, tu branches ensuite dans ton site / ton process.

## En résumé

Gradio = vitrine de test. Pas un CMS. Ça accélère la validation humaine.

---

## Questions fréquentes (FAQ)

**Ça remplace mon site ?** Non. C'est une démo.

**C'est sécurisé ?** Une démo publique expose ce que tu y mets. Pas de secrets dedans.

---

## Navigation dans la série

- Précédent : [Fine-tuning](/blog/articles/llm-finetuning-entrainer-modele.html)
- Suivant : [LoRA et raisonnement](/blog/articles/llm-finetuning-avance-lora-reasoning.html)
""",
)

pack(
    "llm-finetuning-avance-lora-reasoning",
    "LoRA et raisonnement : adapter sans tout réécrire",
    "2026-10-08",
    "LoRA pour fine-tuner léger, et pourquoi bien briefer compte autant que la taille du modèle.",
    ["LoRA", "PEFT", "fine-tuning", "LLM", "raisonnement", "formation"],
    "llm-transformers-serie",
    8,
    "llm-finetuning-avance-lora-reasoning-1200x630.jpg",
    fig(
        "llm-lora-reasoning.svg",
        "Schéma LoRA PEFT",
        "Base gelée + petits adapters = moins de coût.",
        "llm-lora-illustration.jpg",
        "LoRA : adapter sans tout réécrire.",
        "Des petits modules, un gros gain de confort.",
    )
    + f"""

Fine-tuner **tout** un gros modèle coûte cher. LoRA (et la famille PEFT) ajoute de **petits adapters** : tu adaptes sans tout réécrire.

## L'idée en une phrase

**Base fixe + petites pièces apprises = spécialisation moins chère.**

## Pourquoi tu t'en fiches (en vrai)

- moins de mémoire ;
- entraînements plus courts ;
- tu peux stocker plusieurs adapters pour plusieurs métiers.

## Raisonnement / briefing

Un modèle « qui raisonne mieux », ce n'est pas seulement plus de paramètres. C'est aussi :
- une consigne claire ;
- des exemples ;
- des outils (voir la [série Agents](/blog/series/hf-agents-serie.html)) ;
- une relecture humaine sur ce qui compte.

## En résumé

LoRA = fine-tuning malin. Le briefing + la validation restent ton métier.

Inspiration pédagogique : [cours LLM HF]({HF_LLM}). Suite logique : les agents.

---

## Questions fréquentes (FAQ)

**LoRA remplace le fine-tuning classique ?** Souvent un excellent défaut. Pas toujours obligatoire.

**Et après cette série ?** Les [agents IA](/blog/series/hf-agents-serie.html) : outils + boucle.

---

## Navigation dans la série

- Précédent : [Gradio](/blog/articles/llm-gradio-demo-partager-modele.html)
- Série Agents : [C'est quoi un agent ?](/blog/articles/agents-hf-quest-ce-qu-un-agent.html)
""",
)

# ---------------------------------------------------------------------------
# Data Engineering
# ---------------------------------------------------------------------------

pack(
    "data-engineering-pipeline-end-to-end-intro",
    "Data engineering : un pipeline de bout en bout",
    "2026-10-01",
    "C'est quoi un data engineer, et comment relier sources, transform, entrepôt et dashboards sans jargon.",
    ["data engineering", "pipeline", "ETL", "formation", "débutant"],
    "data-engineering-serie",
    1,
    "data-engineering-pipeline-end-to-end-intro-1200x630.jpg",
    fig(
        "data-eng-pipeline.svg",
        "Schéma pipeline data",
        "Sources → transform → entrepôt → consommation.",
        "data-eng-pipeline-illustration.jpg",
        "Sources, transform, entrepôt, consommation.",
        "Les tuyaux, pas seulement le graphique final.",
    )
    + f"""

« Data engineer », tu entends le mot. Concrètement : la personne qui construit les **tuyaux**. Pas le dashboard. Pas le modèle ML. Les tuyaux qui amènent des données propres.

Cette série s'inspire du [Data Engineering Zoomcamp]({ZOOM}). Texte original, français simple.

## L'idée en une phrase

**Faire arriver les données au bon endroit, propres, à l'heure - pour que les autres puissent les utiliser.**

## Les 4 zones

1. **Sources** : API, fichiers, base métier.  
2. **Transform** : nettoyer, joindre, agréger.  
3. **Entrepôt** : là où c'est stocké pour analyser (ex. BigQuery).  
4. **Conso** : dashboards, SQL métier, parfois ML.

Un pipeline de bout en bout relie les quatre, sans que quelqu'un exporte un Excel chaque lundi.

## Exemple boutique

Tu veux le panier moyen par jour. Les commandes sont dans Postgres, les campagnes dans une API.

Sans pipeline : export manuel, fusion hasardeuse, chiffre douteux.  
Avec pipeline : chaque nuit, extract → load → modèles propres → dashboard à jour.

## ETL vs ELT (version courte)

- **ETL** : tu transformes avant de charger.  
- **ELT** : tu charges le brut, tu transformes dans l'entrepôt (souvent avec dbt).

Retiens surtout : **sépare le brut du prêt à analyser**.

## Production-ready, sans blabla

Ça veut dire : planifiable, observable, rejouable. Tu sais quand ça a tourné, ce qui a cassé, comment relancer sans doubler les lignes.

## Parcours de la série

Docker/Terraform → orchestration → ingestion → BigQuery → dbt → Spark → Kafka.  
On avance brique par brique.

## En résumé

Data eng = fiabilité du flux. Le dashboard n'est que la vitrine.

---

## Questions fréquentes (FAQ)

**C'est la même chose que data analyst ?** Non. L'analyste consomme. L'engineer livre des tuyaux fiables.

**Je commence où ?** Une source, une table propre, un schedule simple.

---

## Navigation dans la série

- Suivant : [Docker et Terraform](/blog/articles/data-engineering-docker-terraform-infra.html)
""",
)

pack(
    "data-engineering-docker-terraform-infra",
    "Docker et Terraform : lab local + infra cloud",
    "2026-10-02",
    "Postgres en local avec Docker, infra cloud rejouable avec Terraform - le socle avant les jobs.",
    ["Docker", "Terraform", "data engineering", "infra", "formation"],
    "data-engineering-serie",
    2,
    "data-engineering-docker-terraform-infra-1200x630.jpg",
    fig(
        "data-eng-docker-terraform.svg",
        "Schéma Docker Terraform",
        "Lab local, puis infra cloud rejouable.",
        "data-eng-docker-illustration.jpg",
        "Lab local Docker, infra cloud Terraform.",
        "Même esprit : reproductible chez toi et dans le cloud.",
    )
    + """

Avant l'orchestration fancy, tu as besoin d'un **lab** et d'une infra que tu peux recréer.

## L'idée en une phrase

**Docker** = environnement local isolé. **Terraform** = décrire le cloud en code.

## Docker (chez toi)

Tu lances Postgres (ou autre) sans polluer ta machine. Tout le monde du projet a la même base de départ.

## Terraform (dans le cloud)

Bucket, dataset BigQuery, droits… décrits dans des fichiers. Tu détruis / recrées sans cliquer 40 fois dans une console.

## En résumé

Reproductible > « ça marche sur mon PC ». Socle d'abord, jobs ensuite.

---

## Questions fréquentes (FAQ)

**Obligatoire dès le jour 1 ?** Docker oui pour apprendre tranquille. Terraform dès que tu touches le cloud pour de vrai.

---

## Navigation dans la série

- Précédent : [Pipeline intro](/blog/articles/data-engineering-pipeline-end-to-end-intro.html)
- Suivant : [Orchestration](/blog/articles/data-engineering-orchestration-kestra.html)
""",
)

pack(
    "data-engineering-orchestration-kestra",
    "Orchestration : planifier et surveiller les jobs",
    "2026-10-03",
    "Enchaîner les étapes, retenter si ça casse, être alerté - l'esprit Kestra / Airflow sans usine obscure.",
    ["orchestration", "Kestra", "Airflow", "DAG", "data engineering", "formation"],
    "data-engineering-serie",
    3,
    "data-engineering-orchestration-kestra-1200x630.jpg",
    fig(
        "data-eng-orchestration.svg",
        "Schéma orchestration",
        "DAG, schedule, retries, alertes.",
        "data-eng-orchestration-illustration.jpg",
        "Planifier, retenter, alerter.",
        "Le chef d'orchestre des jobs data.",
    )
    + """

Un script lancé à la main, ça va… jusqu'au jour où tu oublies. L'orchestration enchaîne les étapes et te dit quand ça rate.

## L'idée en une phrase

**Planifier → enchaîner → retenter → alerter.**

## Ce que tu gagnes

- un calendrier (chaque nuit, chaque heure…) ;
- un ordre clair (extract avant transform) ;
- des retries si l'API tousse ;
- une alerte au lieu d'un silence gênant.

## DAG, en français

C'est le plan des étapes et de leurs dépendances. Pas besoin du jargon pour retenir : **qui doit finir avant qui**.

## En résumé

L'orchestrateur ne remplace pas tes scripts. Il les rend fiables dans le temps.

---

## Questions fréquentes (FAQ)

**Kestra ou Airflow ?** L'esprit est le même. Choisis selon ton équipe / ton hébergement.

---

## Navigation dans la série

- Précédent : [Docker Terraform](/blog/articles/data-engineering-docker-terraform-infra.html)
- Suivant : [Ingestion](/blog/articles/data-engineering-ingestion-api-incremental.html)
""",
)

pack(
    "data-engineering-ingestion-api-incremental",
    "Ingestion : charger sans tout rejouer",
    "2026-10-04",
    "Incrémental, idempotent, normalisé : charger le nouveau sans casser l'historique.",
    ["ingestion", "API", "ETL", "data engineering", "formation"],
    "data-engineering-serie",
    4,
    "data-engineering-ingestion-api-incremental-1200x630.jpg",
    fig(
        "data-eng-ingestion.svg",
        "Schéma ingestion incrémentale",
        "Sources → incrémental → normaliser → load.",
        "data-eng-ingestion-illustration.jpg",
        "Charger le nouveau sans tout rejouer.",
        "Le delta, pas le grand reset quotidien.",
    )
    + """

Tout recharger depuis 2019 chaque nuit, ça marche… jusqu'à ce que ça coûte cher et que ça dure trois heures.

## L'idée en une phrase

**Ne prendre que le nouveau (ou le modifié), proprement.**

## Trois mots utiles

- **Incrémental** : depuis le dernier curseur / la dernière date.  
- **Idempotent** : relancer ne double pas les lignes.  
- **Normaliser** : types, fuseaux, noms de colonnes stables.

## Exemple

L'API renvoie les commandes du jour. Tu charges, tu dédupliques sur l'id commande, tu écris dans le brut. Demain, tu reprends où tu t'es arrêté.

## En résumé

Ingestion propre = moins de surprises plus bas dans le tuyau.

---

## Questions fréquentes (FAQ)

**Et si l'API n'a pas de filtre date ?** Tu gères un cache / un hash / un full + merge - mais documente le contrat.

---

## Navigation dans la série

- Précédent : [Orchestration](/blog/articles/data-engineering-orchestration-kestra.html)
- Suivant : [BigQuery](/blog/articles/data-engineering-warehouse-bigquery.html)
""",
)

pack(
    "data-engineering-warehouse-bigquery",
    "BigQuery : l'entrepôt pour analyser",
    "2026-10-05",
    "Raw, staging, marts : ranger les données pour que le métier puisse interroger sans se perdre.",
    ["BigQuery", "warehouse", "data engineering", "SQL", "formation"],
    "data-engineering-serie",
    5,
    "data-engineering-warehouse-bigquery-1200x630.jpg",
    fig(
        "data-eng-bigquery.svg",
        "Schéma BigQuery couches",
        "Raw → staging → marts, avec partition.",
        "data-eng-bigquery-illustration.jpg",
        "Raw, staging, marts - couche par couche.",
        "Du brut au prêt métier.",
    )
    + """

L'entrepôt, c'est le lieu où les données vivent pour être **analysées**. BigQuery est un exemple cloud courant.

## L'idée en une phrase

**Couches claires : brut, nettoyé, prêt métier.**

## Les 3 couches (à retenir)

1. **Raw** : tel quel (ou presque).  
2. **Staging** : types propres, jointures de base.  
3. **Marts** : tables que le métier comprend (panier moyen, etc.).

## Coût / vitesse

Partitionne et filtre intelligemment. Interroger tout l'historique « parce que » coûte cher.

## En résumé

Un entrepôt sans couches, c'est un grenier. Avec couches, c'est une boutique rangée.

---

## Questions fréquentes (FAQ)

**Obligé BigQuery ?** Non. L'esprit couches reste valable ailleurs.

---

## Navigation dans la série

- Précédent : [Ingestion](/blog/articles/data-engineering-ingestion-api-incremental.html)
- Suivant : [dbt](/blog/articles/data-engineering-dbt-analytics-engineering.html)
""",
)

pack(
    "data-engineering-dbt-analytics-engineering",
    "dbt : transformer en SQL testé",
    "2026-10-06",
    "Modèles SQL versionnés, tests, docs : l'analytics engineering sans magie noire.",
    ["dbt", "SQL", "analytics engineering", "data engineering", "formation"],
    "data-engineering-serie",
    6,
    "data-engineering-dbt-analytics-engineering-1200x630.jpg",
    fig(
        "data-eng-dbt.svg",
        "Schéma dbt",
        "Sources → modèles → tests → docs.",
        "data-eng-dbt-illustration.jpg",
        "SQL versionné, tests, docs.",
        "La transformation devient un produit d'équipe.",
    )
    + """

dbt, c'est (surtout) du **SQL versionné** avec des tests et de la doc. Tu transformes dans l'entrepôt, en équipe.

## L'idée en une phrase

**Chaque modèle = un fichier SQL clair, testable, documenté.**

## Ce que tu gagnes

- historique Git ;
- tests (unicité, pas de null surprises) ;
- doc générée pour l'équipe ;
- moins de « la requête de Kevin dans un pad ».

## En résumé

dbt ne remplace pas l'ingestion. Il range la transformation analytique.

---

## Questions fréquentes (FAQ)

**Faut-il être expert SQL ?** Tu progresses. Les modèles simples suffisent pour démarrer.

---

## Navigation dans la série

- Précédent : [BigQuery](/blog/articles/data-engineering-warehouse-bigquery.html)
- Suivant : [Spark](/blog/articles/data-engineering-spark-batch-processing.html)
""",
)

pack(
    "data-engineering-spark-batch-processing",
    "Spark : gros volumes en batch",
    "2026-10-07",
    "Quand le volume explose, Spark (ou équivalent) découpe le travail - sans paniquer.",
    ["Spark", "batch", "data engineering", "DataFrame", "formation"],
    "data-engineering-serie",
    7,
    "data-engineering-spark-batch-processing-1200x630.jpg",
    fig(
        "data-eng-spark.svg",
        "Schéma Spark batch",
        "Fichiers → DataFrame → actions → sortie.",
        "data-eng-spark-illustration.jpg",
        "Gros volumes en batch avec Spark.",
        "Distribuer le calcul quand une machine ne suffit plus.",
    )
    + """

Une seule machine suffit… jusqu'au jour où non. Spark sert à traiter de **gros volumes** en batch (fichiers, historiques).

## L'idée en une phrase

**Découper le calcul sur plusieurs workers, puis écrire le résultat.**

## Quand tu en as besoin

- historiques lourds ;
- transforms trop lents en SQL simple ;
- formats fichiers massifs (parquet, etc.).

## Quand tu n'en as pas besoin

- 50 000 lignes bien indexées dans BigQuery ;
- un cron + pandas qui finit en 2 minutes.

## En résumé

Spark = outil de volume. Pas un badge de prestige. Utilise-le quand le besoin est réel.

---

## Questions fréquentes (FAQ)

**Spark remplace dbt ?** Non. Souvent complémentaires selon la couche.

---

## Navigation dans la série

- Précédent : [dbt](/blog/articles/data-engineering-dbt-analytics-engineering.html)
- Suivant : [Kafka](/blog/articles/data-engineering-kafka-streaming.html)
""",
)

pack(
    "data-engineering-kafka-streaming",
    "Kafka : événements en continu",
    "2026-10-08",
    "Producers, topics, consumers : comprendre le streaming sans se noyer dans le cluster.",
    ["Kafka", "streaming", "events", "data engineering", "formation"],
    "data-engineering-serie",
    8,
    "data-engineering-kafka-streaming-1200x630.jpg",
    fig(
        "data-eng-kafka.svg",
        "Schéma Kafka",
        "Producers → topics → consumers.",
        "data-eng-kafka-illustration.jpg",
        "Événements en continu avec Kafka.",
        "Une file d'attente robuste pour les events.",
    )
    + f"""

Le batch tourne chaque nuit. Le streaming réagit aux **événements** au fil de l'eau (clic, commande, capteur…).

## L'idée en une phrase

**Quelqu'un publie → ça attend dans un topic → quelqu'un consomme.**

## Les 3 rôles

1. **Producer** : envoie l'événement.  
2. **Topic** : la file / le canal.  
3. **Consumer** : lit et agit (enrichir, alerter, écrire en base).

## Schémas (Avro etc.)

Mettez-vous d'accord sur le format. Sinon le consumer casse le jour où un champ change de type.

## Quand s'en passer

Si un import horaire suffit au métier, ne force pas Kafka pour le CV.

## En résumé

Kafka = tuyau temps (quasi) réel. Puissant, mais seulement si le besoin est temps réel.

Inspiration : [Zoomcamp DataTalks]({ZOOM}). Tu as maintenant la carte mentale bout en bout.

---

## Questions fréquentes (FAQ)

**Kafka = base de données ?** Non. C'est un journal / bus d'événements.

**Je commence par le streaming ?** Non. Maîtrise d'abord un pipeline batch simple.

---

## Navigation dans la série

- Précédent : [Spark](/blog/articles/data-engineering-spark-batch-processing.html)
- Série LLM : [NLP vs LLM](/blog/articles/llm-nlp-vs-llm-comprendre-les-bases.html)
""",
)


def main() -> None:
    ART.mkdir(parents=True, exist_ok=True)
    for slug, content in ARTICLES.items():
        path = ART / f"{slug}.md"
        path.write_text(content, encoding="utf-8")
        print("wrote", path.name)
    print("OK", len(ARTICLES))


if __name__ == "__main__":
    main()
