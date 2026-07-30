#!/usr/bin/env python3
"""
Genere des articles / tutoriels / guides blog a partir des transcripts UneFilleIA.

Usage:
    python scripts/generate_ia_articles_from_transcripts.py

Sorties:
    - blog/content/articles/ia-*.md (et slugs derives)
    - blog/content/collections/*-serie.json
    - docs/prompt_og_images_articles_ia_pratique.md
    - docs/INSTALL_IMAGES_IA_WEBP.md
"""

from __future__ import annotations

import json
import re
import unicodedata
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SELECTION = ROOT / "scripts" / "_ia_articles_selection.json"
ARTICLES_DIR = ROOT / "blog" / "content" / "articles"
COLLECTIONS_DIR = ROOT / "blog" / "content" / "collections"
DOCS_DIR = ROOT / "docs"

# Contenu a exclure (arnaques, contournement douteux, sujets sensibles)
SKIP_SLUG = re.compile(
    r"darkgpt|non.?censur|renverser|influence.?ia|sora.?2|vpn|"
    r"contourner.?les.?restrictions|psychose|nord.?core",
    re.I,
)
SKIP_TEXT = re.compile(
    r"dark\s*web|renverser le gouvernement|49,90|"
    r"informations bancaires.*site comme",
    re.I,
)

SERIES_META = {
    "prompts": {
        "id": "ia-prompts-serie",
        "title": "Serie IA - Prompts et methodes",
        "description": "Prompts utiles, methodes de prompting et ressources pour mieux parler aux modeles.",
        "slug": "ia-prompts-serie",
        "prefix": "ia-prompts",
        "type": "toolbox",
        "tags": ["IA", "prompts", "ChatGPT", "Claude", "prompt engineering"],
    },
    "chatgpt-astuces": {
        "id": "ia-chatgpt-serie",
        "title": "Serie IA - Astuces ChatGPT",
        "description": "Astuces concretes pour ChatGPT au quotidien, sans jargon inutile.",
        "slug": "ia-chatgpt-serie",
        "prefix": "ia-chatgpt",
        "type": "tutorial",
        "tags": ["IA", "ChatGPT", "productivite", "astuces"],
    },
    "claude": {
        "id": "ia-claude-serie",
        "title": "Serie IA - Claude et Anthropic",
        "description": "Prise en main de Claude, connecteurs, Cowork et ressources Anthropic.",
        "slug": "ia-claude-serie",
        "prefix": "ia-claude",
        "type": "tutorial",
        "tags": ["IA", "Claude", "Anthropic", "productivite"],
    },
    "gemini-google": {
        "id": "ia-gemini-serie",
        "title": "Serie IA - Gemini, NotebookLM et Google",
        "description": "Gemini, NotebookLM, Google AI Studio et formations Google Skills.",
        "slug": "ia-gemini-serie",
        "prefix": "ia-gemini",
        "type": "tutorial",
        "tags": ["IA", "Gemini", "NotebookLM", "Google"],
    },
    "agents-ia": {
        "id": "ia-agents-serie",
        "title": "Serie IA - Agents et automatisation",
        "description": "Agents IA, Agent Kit, Deep Research et automatisations utiles.",
        "slug": "ia-agents-serie",
        "prefix": "ia-agents",
        "type": "guide",
        "tags": ["IA", "agents", "automatisation", "OpenAI"],
    },
    "images-visuels": {
        "id": "ia-images-serie",
        "title": "Serie IA - Images et visuels",
        "description": "Generer des images, logos, infographies et visuels coherents avec l'IA.",
        "slug": "ia-images-serie",
        "prefix": "ia-images",
        "type": "tutorial",
        "tags": ["IA", "images", "design", "visuels"],
    },
    "formations": {
        "id": "ia-formations-serie",
        "title": "Serie IA - Formations et parcours",
        "description": "Certifications, parcours gratuits et projets pour apprendre l'IA.",
        "slug": "ia-formations-serie",
        "prefix": "ia-cours",
        "type": "guide",
        "tags": ["IA", "formation", "apprentissage", "certification"],
    },
    "no-code-apps": {
        "id": "ia-nocode-serie",
        "title": "Serie IA - Apps et sites sans coder",
        "description": "Creer sites et apps avec l'IA, vibe coding et outils no-code.",
        "slug": "ia-nocode-serie",
        "prefix": "ia-nocode",
        "type": "tutorial",
        "tags": ["IA", "no-code", "apps", "sites web"],
    },
    "outils-alternatives": {
        "id": "ia-outils-serie",
        "title": "Serie IA - Outils et alternatives",
        "description": "Comparatifs d'outils IA, alternatives gratuites et stacks pratiques.",
        "slug": "ia-outils-serie",
        "prefix": "ia-outils",
        "type": "comparatif",
        "tags": ["IA", "outils", "alternatives", "comparatif"],
    },
    "metiers-futur": {
        "id": "ia-metiers-serie",
        "title": "Serie IA - Metiers et futur du travail",
        "description": "Impact de l'IA sur les metiers, emploi et competence a developper.",
        "slug": "ia-metiers-serie",
        "prefix": "ia-metiers",
        "type": "article",
        "tags": ["IA", "metiers", "emploi", "futur du travail"],
    },
    "productivite": {
        "id": "ia-productivite-serie",
        "title": "Serie IA - Productivite au quotidien",
        "description": "Gagner du temps avec l'IA sur les taches du quotidien.",
        "slug": "ia-productivite-serie",
        "prefix": "ia-prod",
        "type": "checklist",
        "tags": ["IA", "productivite", "organisation"],
    },
}


def slugify(text: str, max_len: int = 70) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text[:max_len].rstrip("-")


def clean_title(raw: str) -> str:
    t = raw
    t = re.sub(r"[#＃].*", "", t)
    t = re.sub(r"[‼️⚠️🚨🔥💡✅❌⭐️🎯📌]+", "", t)
    t = t.replace("：", ":").replace("＂", '"').replace("／", "/")
    t = re.sub(r"(?i)^r[eé]ponse\s+[aà]\s+@?[\w.-]+\s*[:：-]?\s*", "", t)
    t = re.sub(r"(?i)^(tutoriel|tuto)\s*[:：]\s*", "", t)
    t = re.sub(r"\s+", " ", t).strip(" :.")
    for cut in (
        " Abonnez",
        " abonnez",
        " Et pour plus",
        " Alors a votre",
        " Alors à votre",
        " #",
    ):
        if cut in t:
            t = t.split(cut)[0]
    t = t.strip()
    if len(t) > 88:
        for sep in (":", " - ", " ?", " !"):
            if sep in t[:88]:
                idx = t.find(sep, 0, 92)
                if idx > 25:
                    t = t[:idx].rstrip(" :-")
                    if sep.strip() in "?!":
                        t = t + sep.strip()
                    break
        else:
            t = t[:85].rsplit(" ", 1)[0] + "…"
    if t:
        t = t[0].upper() + t[1:]
    t = t.replace("'", "'").replace("'", "'").replace("'", "'")
    return t


def clean_body_text(text: str) -> str:
    t = text.replace("\r\n", "\n").replace("\r", "\n")
    t = re.sub(r"\s+", " ", t).strip()
    # Retirer appels a l'abonnement typiques
    t = re.sub(
        r"(?i)\s*(abonnez[- ]vous[^.]*(?:\.|$)|et surtout\.\.\.|le lien (?:est )?dans (?:ma )?bio[^.]*\.?)",
        "",
        t,
    )
    t = t.replace("'", "'").replace("'", "'").replace("'", "'")
    t = t.replace("—", "-").replace("–", "-")
    return t.strip()


def excerpt_from(text: str, title: str) -> str:
    base = clean_body_text(text)
    # Premiere ou deuxieme phrase
    parts = re.split(r"(?<=[.!?])\s+", base)
    bits = []
    for p in parts:
        if len(p) < 20:
            continue
        bits.append(p)
        joined = " ".join(bits)
        if len(joined) >= 120:
            break
    if not bits:
        return f"{title} - guide pratique a partir d'usages reels de l'IA."
    ex = " ".join(bits)
    if len(ex) > 220:
        ex = ex[:217].rsplit(" ", 1)[0] + "…"
    return ex


def split_ideas(text: str) -> list[str]:
    """Decoupe le transcript en idees / etapes."""
    t = clean_body_text(text)
    # Numerotations
    chunks = re.split(r"(?=\b(?:\d+|Première|Deuxième|Troisième|Ensuite|Puis|Enfin|Etape|Étape)\b)", t)
    chunks = [c.strip(" ,;") for c in chunks if len(c.strip()) > 40]
    if len(chunks) < 2:
        chunks = re.split(r"(?<=[.!?])\s+", t)
        chunks = [c.strip() for c in chunks if len(c.strip()) > 40]
    return chunks[:8] or [t]


def yaml_escape(s: str) -> str:
    return s.replace('"', '\\"')


def tags_yaml(tags: list[str]) -> str:
    return "[" + ", ".join(tags) + "]"


def _step_label(i: int, idea: str) -> str:
    """Titre de section court et propre (pas un bout de phrase coupe)."""
    labels_num = {
        1: "Premiere etape",
        2: "Deuxieme etape",
        3: "Troisieme etape",
        4: "Quatrieme point",
        5: "Cinquieme point",
    }
    low = idea.lower()
    if re.search(r"\bprompt", low):
        return f"Etape {i} - preparer le prompt"
    if re.search(r"\bexport|png|svg|telecharger", low):
        return f"Etape {i} - exporter le resultat"
    if re.search(r"\bgratuit|ressource|formation|certif", low):
        return f"Point {i} - ressources utiles"
    if re.search(r"\balternative|comparer|vs\b", low):
        return f"Point {i} - alternatives"
    if re.search(r"\battention|danger|eviter|ne (jamais|pas)", low):
        return f"Point {i} - points d'attention"
    return labels_num.get(i, f"Point {i}")


def _humanize_paragraph(text: str) -> str:
    """Legere reecriture pour un ton plus oral, sans inventer de faits."""
    t = clean_body_text(text)
    t = re.sub(r"(?i)\bvous avez juste a\b", "tu as juste a", t)
    t = re.sub(r"(?i)\bvous pouvez\b", "tu peux", t)
    t = re.sub(r"(?i)\bvous voulez\b", "tu veux", t)
    t = re.sub(r"(?i)\bje vous\b", "je te", t)
    t = re.sub(r"(?i)\bn'hesitez pas a vous abonner[^.]*\.?", "", t)
    t = re.sub(r"(?i)\bsi ca vous a plu[^.]*\.?", "", t)
    t = re.sub(r"\s+", " ", t).strip()
    # Accents courants manquants dans certains transcripts
    fixes = {
        " etape ": " étape ",
        " Etape ": " Étape ",
        " premiere ": " première ",
        " deuxieme ": " deuxième ",
        " troisieme ": " troisième ",
        " resultats": " résultats",
        " resultat": " résultat",
        " telecharg": " télécharg",
        " egalement": " également",
        " ca ": " ça ",
        " Ca ": " Ça ",
    }
    for a, b in fixes.items():
        t = t.replace(a, b)
    return t


def build_article(
    *,
    slug: str,
    title: str,
    excerpt: str,
    art_type: str,
    tags: list[str],
    series_id: str,
    order: int,
    pub_date: date,
    source_text: str,
    category: str,
) -> str:
    ideas = [_humanize_paragraph(x) for x in split_ideas(source_text)]
    ideas = [x for x in ideas if len(x) > 35][:6]
    if not ideas:
        ideas = [_humanize_paragraph(source_text)]
    og = f"{slug}-1200x630.jpg"

    intro_hooks = {
        "prompts": "On va parler prompts, sans se prendre la tête. L'idée c'est d'avoir quelque chose que tu peux tester ce soir.",
        "chatgpt-astuces": "Petite astuce ChatGPT, du genre que tu gardes dans un coin et que tu réutilises souvent.",
        "claude": "Si tu tournes autour de Claude en ce moment, voilà ce qui vaut vraiment le coup de tester.",
        "gemini-google": "Du côté Google, Gemini et NotebookLM bougent vite. Voici ce qui m'a paru utile.",
        "agents-ia": "Les agents IA, c'est un peu le buzzword du moment. On va rester concret.",
        "images-visuels": "Pour les images, le résultat dépend surtout de comment tu demandes. On regarde ça.",
        "formations": "Si tu veux te former à l'IA sans y passer des mois, voici un parcours clair.",
        "no-code-apps": "Créer un site ou une petite app avec l'IA, c'est possible. Encore faut-il savoir par où commencer.",
        "outils-alternatives": "Pas besoin de tout payer. On passe en revue des options qui tiennent la route.",
        "metiers-futur": "L'IA change le taf, oui. Mais pas toujours comme les titres le laissent croire.",
        "productivite": "Quelques gestes simples pour gagner du temps, sans transformer ta vie en dashboard.",
    }
    hook = intro_hooks.get(category, "Voici ce qu'il faut retenir, en vrai, sans blabla.")

    # Resume en clair
    resume = ideas[0] if ideas else excerpt
    if len(resume) > 280:
        resume = resume[:277].rsplit(" ", 1)[0] + "…"

    steps_md = []
    for i, idea in enumerate(ideas, 1):
        heading = _step_label(i, idea)
        # Accents sur labels
        heading = (
            heading.replace("Etape", "Étape")
            .replace("Premiere", "Première")
            .replace("Deuxieme", "Deuxième")
            .replace("Troisieme", "Troisième")
            .replace("Quatrieme", "Quatrième")
            .replace("Cinquieme", "Cinquième")
            .replace("preparer", "préparer")
            .replace("resultat", "résultat")
        )
        steps_md.append(f"### {heading}\n\n{idea}\n")

    steps_block = "\n".join(steps_md)

    faq = """## Questions fréquentes

### C'est adapté aux débutants ?

Oui. Tu peux suivre ça même si tu débutes, tant que tu testes au fur et à mesure. Lire sans pratiquer, ça sert à rien ici.

### Combien de temps ça prend ?

Compte entre 15 et 45 minutes pour le premier essai. Après, tu vas plus vite.

### Faut-il un compte payant ?

Pas forcément. Beaucoup d'outils ont un plan gratuit suffisant pour commencer. Si tu bloques, passe à l'outil suivant plutôt que de forcer.

### Et le SEO / la visibilité ?

Si tu publies ce que tu produis (articles, pages, fiches), structure bien tes titres, mets une meta description claire, et pense aux microdonnées (Article, HowTo, FAQ). Ça aide Google et les moteurs IA à te citer.
"""

    checklist = """## Mini checklist

- [ ] Tu as testé l'astuce une fois de bout en bout
- [ ] Tu as noté le prompt / la méthode quelque part
- [ ] Tu as adapté le résultat à ton cas (pas de copier-coller brut)
- [ ] Tu as vérifié les infos sensibles avant de publier
"""

    type_blurb = {
        "tutorial": "## Déroule pas à pas\n\nOn avance étape par étape. Prends le temps de faire chaque point avant de passer au suivant.\n",
        "guide": "## Le guide en pratique\n\nVoici le coeur du sujet, organisé pour que tu puisses t'en servir demain matin.\n",
        "toolbox": "## Dans la boîte à outils\n\nDes ressources et méthodes à garder sous le coude.\n",
        "comparatif": "## Comparaison utile\n\nPas un classement absolu. Juste ce qui change vraiment selon ton usage.\n",
        "checklist": "## À cocher\n\nTu peux traiter ça comme une liste d'actions.\n",
        "article": "## Ce qu'il faut comprendre\n\n",
    }.get(art_type, "## Contenu\n\n")

    body = f"""# {title}

{hook}

## En clair

{resume}

---

{type_blurb}

{steps_block}
---

## Ce que j'en retiens

Le truc important, c'est pas d'avoir le "meilleur" outil. C'est d'avoir une méthode claire, de tester vite, et de garder ce qui marche pour toi. L'IA avance vite, mais les bases (bon prompt, bon contexte, vérification) restent les mêmes.

Si tu appliques seulement une idée de cet article aujourd'hui, c'est déjà gagnant.

---

{checklist}

---

{faq}

---

## Pour aller plus loin (SEO & structure)

Quand tu transformes ce genre d'astuce en page web :

1. Un seul `h1`, des `h2`/`h3` clairs
2. Une meta description qui dit vraiment le sujet (comme l'excerpt ci-dessus)
3. Des microdonnées `BlogPosting` (deja gerees par le template du blog) + FAQ si tu as des questions/reponses
4. Une image OG 1200x630 (voir le fichier prompts images de la serie)

---

## Suite logique

Cette page fait partie d'une série sur l'IA pratique. Enchaîne avec les autres articles de la série pour construire un vrai parcours, pas juste une astuce isolée.
"""

    body = body.replace("'", "'").replace("'", "'").replace("—", "-").replace("–", "-")
    body = body.replace("deja gerees", "déjà gérées")
    body = body.replace("questions/reponses", "questions/réponses")

    fm = f"""---
title: "{yaml_escape(title)}"
date: {pub_date.isoformat()}
excerpt: "{yaml_escape(excerpt)}"
type: {art_type}
tags: {tags_yaml(tags)}
og_image: {og}
series: {series_id}
series_order: {order}
---

"""
    return fm + body


def prompt_for_image(slug: str, title: str, category: str) -> str:
    themes = {
        "prompts": "workspace technique avec prompt engineering, console, blocs de contexte et panneau de sortie",
        "chatgpt-astuces": "interface conversationnelle avancee, panneau de taches, notes et checklists produit",
        "claude": "assistant de travail, documents longs, connecteurs et panneaux d'analyse",
        "gemini-google": "AI Studio, notebooks, sources reliees, cartes de traitement Google",
        "agents-ia": "workflow d'automatisation, noeuds relies, orchestration, etapes d'execution",
        "images-visuels": "pipeline image, outils de retouche, calques, generation visuelle technique",
        "formations": "parcours d'apprentissage, modules, ressources, docs et tableaux de progression",
        "no-code-apps": "maquettes d'apps, editeur visuel, composants UI, navigateur et schema de flux",
        "outils-alternatives": "comparatif d'outils, cartes produit, interfaces cote a cote, mesures",
        "metiers-futur": "visualisation de metiers, tendances, data, postes de travail modernes",
        "productivite": "tableau de bord, calendrier, automatisations, taches et suivi",
    }
    theme = themes.get(category, "interface IA moderne")
    short = title[:48]
    return f"""Scene : visuel Open Graph technique et premium pour un article informatique, {theme}. Composition complexe mais lisible, avec plusieurs panneaux UI, elements logiciels, flux de donnees ou modules techniques selon le sujet. Palette claire premium : fond #f5f7fb vers #e9eef6, bleus #2563eb et #60a5fa, encre #0f172a, accent rouge #dc2626. Bandeau bas sombre avec titre en francais "{short}" et marque "DanielCraft". Style plus technique, plus logiciel, plus architecture web, moins cartoon, moins simplifie, pas de mascotte naive, pas de flat design vide. Si un humain apparait, il reste secondaire et sobre. Ratio 1.91:1, 1200x630. Export JPG puis convertir en WebP.
"""


def main() -> None:
    raw = json.loads(SELECTION.read_text(encoding="utf-8"))
    # Filtrer
    items = []
    for e in raw:
        slug_test = e.get("slug", "") + " " + e.get("title", "")
        text = e.get("text", "")
        if SKIP_SLUG.search(slug_test) or SKIP_TEXT.search(text):
            continue
        if len(clean_body_text(text)) < 150:
            continue
        items.append(e)

    by_cat: dict[str, list] = defaultdict(list)
    for e in items:
        by_cat[e["category"]].append(e)

    start = date(2026, 5, 1)
    generated = []
    prompt_blocks = []
    collections: dict[str, list[str]] = defaultdict(list)

    ARTICLES_DIR.mkdir(parents=True, exist_ok=True)
    COLLECTIONS_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    global_idx = 0
    for cat, meta in SERIES_META.items():
        group = by_cat.get(cat, [])
        # Limiter un peu pour qualite / volume raisonnable par serie
        group = sorted(group, key=lambda x: (x.get("edu", 0), x.get("len", 0)), reverse=True)[:12]
        for order, e in enumerate(group, 1):
            global_idx += 1
            title = clean_title(e["title"])
            # Prefixe slug stable
            base_slug = slugify(title)
            if not base_slug.startswith(meta["prefix"]):
                slug = f"{meta['prefix']}-{base_slug}"[:80].rstrip("-")
            else:
                slug = base_slug[:80]
            # Eviter collision avec articles existants non-ia
            path = ARTICLES_DIR / f"{slug}.md"
            if path.exists() and "series: ia-" not in path.read_text(encoding="utf-8")[:500]:
                slug = f"{slug}-pratique"
                path = ARTICLES_DIR / f"{slug}.md"

            excerpt = excerpt_from(e["text"], title)
            pub = start + timedelta(days=global_idx)
            content = build_article(
                slug=slug,
                title=title,
                excerpt=excerpt,
                art_type=meta["type"],
                tags=meta["tags"],
                series_id=meta["id"],
                order=order,
                pub_date=pub,
                source_text=e["text"],
                category=cat,
            )
            path.write_text(content, encoding="utf-8")
            collections[meta["id"]].append(slug)
            generated.append({"slug": slug, "series": meta["id"], "title": title, "og": f"{slug}-1200x630.jpg"})
            prompt_blocks.append(
                f"## {slug}-1200x630.jpg\n\nArticle : {title}\n\n```\n{prompt_for_image(slug, title, cat).strip()}\n```\n"
            )
            print(f"[OK] {path.relative_to(ROOT)}")

    # Collections JSON
    for meta in SERIES_META.values():
        art_slugs = collections.get(meta["id"], [])
        if not art_slugs:
            continue
        col = {
            "id": meta["id"],
            "title": meta["title"].replace("Serie", "Série").replace("methodes", "méthodes"),
            "description": meta["description"]
            .replace("methodes", "méthodes")
            .replace("concret", "concret")
            .replace("Prise en main", "Prise en main"),
            "slug": meta["slug"],
            "articles": art_slugs,
        }
        # Accents corrects pour titres collections
        col["title"] = (
            meta["title"]
            .replace("Serie", "Série")
            .replace("methodes", "méthodes")
            .replace("Metiers", "Métiers")
            .replace("Productivite", "Productivité")
        )
        col["description"] = (
            meta["description"]
            .replace("methodes", "méthodes")
            .replace("metiers", "métiers")
            .replace("competence", "compétence")
            .replace("Creer", "Créer")
            .replace("Comparatifs", "Comparatifs")
            .replace("Gagner", "Gagner")
        )
        out = COLLECTIONS_DIR / f"{meta['slug']}.json"
        out.write_text(json.dumps(col, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"[COL] {out.relative_to(ROOT)} ({len(art_slugs)} articles)")

    # Prompt file
    prompt_doc = f"""# Prompts OG / WebP - Serie IA pratique (transcripts)

Images Open Graph pour les articles generes depuis les transcripts UneFilleIA.

**Format :** 1200x630 px (ratio 1.91:1), JPG puis WebP.
**Dossier cible :** `assets/images/og/`
**Style :** fond clair, accent rouge #dc2626, flat design, textes en francais, pas de visage.
**Charte :** coherent avec `docs/prompt_og_images_articles_geo.md` et `.cursor/rules/danielcraft-visual-bd.mdc`.

## Installation rapide

1. Genere chaque image avec le prompt ci-dessous (Midjourney, Flux, ChatGPT Images, Recraft…).
2. Nomme le fichier exactement comme indique (`*-1200x630.jpg`).
3. Place le JPG dans `assets/images/og/`.
4. Convertis en WebP (meme nom, extension `.webp`) :

```bash
python scripts/install_ia_og_webp.py
```

Ou manuellement avec Pillow / magick :

```bash
# Exemple ImageMagick
magick convert assets/images/og/SLUG-1200x630.jpg -quality 82 assets/images/og/SLUG-1200x630.webp
```

5. Relance le build : `python build.py` (ou `python blog/build_blog.py`).

## Liste des images ({len(prompt_blocks)} fichiers)

"""
    # Fix accents in header without breaking ASCII file unnecessarily - use proper French
    prompt_doc = """# Prompts OG / WebP - Serie IA pratique (transcripts)

Images Open Graph pour les articles generes depuis les transcripts UneFilleIA.

**Format :** 1200x630 px (ratio 1.91:1), JPG puis WebP.
**Dossier cible :** `assets/images/og/`
**Style :** fond clair, accent rouge #dc2626, flat design, textes en francais, pas de visage.
**Charte :** coherent avec `docs/prompt_og_images_articles_geo.md`.

## Installation rapide

1. Genere chaque image avec le prompt ci-dessous (Flux, ChatGPT Images, Recraft, Midjourney…).
2. Nomme le fichier exactement comme indique (`*-1200x630.jpg`).
3. Place le JPG dans `assets/images/og/`.
4. Lance le script d'install WebP :

```bash
python scripts/install_ia_og_webp.py
```

5. Rebuild : `python build.py`

---

""" + "\n---\n\n".join(prompt_blocks)

    prompt_path = DOCS_DIR / "prompt_og_images_articles_ia_pratique.md"
    prompt_path.write_text(prompt_doc, encoding="utf-8")
    print(f"[DOC] {prompt_path.relative_to(ROOT)}")

    install_doc = """# Installer les images OG WebP (serie IA pratique)

## Prerequis

- Les JPG `*-1200x630.jpg` generes via `docs/prompt_og_images_articles_ia_pratique.md`
- Python 3 + Pillow : `pip install pillow`

## Etapes

1. Copie tous les JPG dans `assets/images/og/`.
2. Execute :

```bash
python scripts/install_ia_og_webp.py
```

Le script :
- trouve les JPG listes dans le fichier prompts (ou tous les `ia-*-1200x630.jpg`)
- cree le `.webp` a cote (qualite 82)
- optionnellement recentre au ratio 1200/630

3. Verifie qu'un article pointe bien `og_image: slug-1200x630.jpg` dans le frontmatter.
4. `python build.py`

## Depannage

- Si le WebP manque, le site peut retomber sur le JPG selon le loader.
- Les fichiers sous `assets/images/og/` sont souvent gitignores : regenerer avant deploy.
"""
    (DOCS_DIR / "INSTALL_IMAGES_IA_WEBP.md").write_text(install_doc, encoding="utf-8")

    # Script install webp
    install_py = ROOT / "scripts" / "install_ia_og_webp.py"
    install_py.write_text(
        '''#!/usr/bin/env python3
"""Convertit les OG JPG de la serie IA en WebP (1200x630)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("pip install pillow")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
OG = ROOT / "assets" / "images" / "og"
PROMPT_DOC = ROOT / "docs" / "prompt_og_images_articles_ia_pratique.md"


def listed_stems() -> set[str]:
    if not PROMPT_DOC.exists():
        return set()
    text = PROMPT_DOC.read_text(encoding="utf-8")
    return set(re.findall(r"^##\\s+([\\w.-]+-1200x630)\\.jpg", text, flags=re.M))


def center_crop(img: Image.Image, ratio: float) -> Image.Image:
    w, h = img.size
    cur = w / h if h else 1.0
    if cur > ratio:
        nw = int(h * ratio)
        left = (w - nw) // 2
        return img.crop((left, 0, left + nw, h))
    nh = int(w / ratio)
    top = (h - nh) // 2
    return img.crop((0, top, w, top + nh))


def main() -> None:
    OG.mkdir(parents=True, exist_ok=True)
    stems = listed_stems()
    files = sorted(OG.glob("ia-*-1200x630.jpg"))
    if stems:
        extra = [OG / f"{s}.jpg" for s in stems if (OG / f"{s}.jpg").exists()]
        files = sorted(set(files) | set(extra))
    if not files:
        print(f"[WARN] Aucun JPG ia-*-1200x630.jpg dans {OG}")
        print("Genere d'abord les images via docs/prompt_og_images_articles_ia_pratique.md")
        return
    for jpg in files:
        img = Image.open(jpg).convert("RGB")
        img = center_crop(img, 1200 / 630)
        img = img.resize((1200, 630), Image.Resampling.LANCZOS)
        webp = jpg.with_suffix(".webp")
        img.save(webp, "WEBP", quality=82, method=6)
        # Reecrit aussi un JPG optimise
        img.save(jpg, "JPEG", quality=85, optimize=True)
        print(f"[OK] {webp.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
''',
        encoding="utf-8",
    )
    print(f"[SCR] {install_py.relative_to(ROOT)}")

    manifest = ROOT / "scripts" / "_ia_articles_generated.json"
    manifest.write_text(json.dumps(generated, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nDone: {len(generated)} articles, {len(collections)} series")


if __name__ == "__main__":
    main()
