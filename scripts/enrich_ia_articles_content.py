#!/usr/bin/env python3
"""
Enrichit les articles IA : contenu plus long/lisible + figure banniere inline.

Usage:
    python scripts/enrich_ia_articles_content.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "blog" / "content" / "articles"
MANIFEST = ROOT / "scripts" / "_ia_articles_generated.json"
ILLUSTRATIONS = ROOT / "assets" / "images" / "blog" / "illustrations"

TYPE_INTRO = {
    "tutorial": (
        "On avance etape par etape. L'idee c'est que tu puisses le refaire "
        "sans revenir dix fois dans la video d'origine."
    ),
    "guide": (
        "Voici le coeur du sujet, organise pour que tu puisses t'en servir "
        "demain matin sans te perdre."
    ),
    "toolbox": (
        "Des ressources et methodes a garder sous le coude. "
        "Pas besoin de tout faire d'un coup."
    ),
    "comparatif": (
        "Pas un classement absolu. Juste ce qui change vraiment selon ton usage."
    ),
    "checklist": (
        "Tu peux traiter ca comme une liste d'actions a cocher."
    ),
    "article": (
        "On reste concret : ce qu'il faut comprendre, et ce que tu peux faire ensuite."
    ),
}


def _accent(s: str) -> str:
    reps = {
        "etape": "étape",
        "Etape": "Étape",
        "idee": "idée",
        "organise": "organisé",
        "methodes": "méthodes",
        "a garder": "à garder",
        "ca comme": "ça comme",
        "a cocher": "à cocher",
        "coeur": "cœur",
    }
    for a, b in reps.items():
        s = s.replace(a, b)
    return s


def parse_fm(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    raw = text[3:end].strip()
    meta: dict = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip().strip('"')
    body = text[end + 4 :].lstrip("\n")
    return meta, body


def extract_source_bits(body: str) -> list[str]:
    """Recupere les paragraphes utiles deja presents (hors FAQ template)."""
    # Couper avant FAQ / checklist template
    cut = body
    for marker in ("## Mini checklist", "## Questions fréquentes", "## Questions frequentes", "## Pour aller plus loin"):
        if marker in cut:
            cut = cut.split(marker)[0]
    paras = []
    for block in re.split(r"\n{2,}", cut):
        b = re.sub(r"^#+\s*", "", block).strip()
        b = re.sub(r"\s+", " ", b)
        if len(b) < 40:
            continue
        if b.startswith("![" ) or b.startswith("<figure"):
            continue
        if "On va parler" in b or "Petite astuce" in b or "Ce contenu part" in b:
            continue
        if b.startswith("**Famille"):
            continue
        paras.append(b)
    return paras[:12]


def build_rich_body(meta: dict, slug: str, old_body: str) -> str:
    title = meta.get("title", slug)
    art_type = (meta.get("type") or "article").strip()
    tags = meta.get("tags", "")
    series = meta.get("series", "")

    bits = extract_source_bits(old_body)
    # Nettoyage abonnement
    cleaned = []
    for b in bits:
        b = re.sub(r"(?i)\s*si ça vous a plu[^.]*\.?", "", b)
        b = re.sub(r"(?i)\s*n'hésitez pas à vous abonner[^.]*\.?", "", b)
        b = re.sub(r"(?i)\s*abonnez[- ]vous[^.]*\.?", "", b)
        b = b.strip()
        if len(b) > 35:
            cleaned.append(b)
    if not cleaned:
        cleaned = ["Le point de depart, c'est une astuce pratique tiree d'un usage reel de l'IA."]

    resume = cleaned[0]
    if len(resume) > 320:
        resume = resume[:317].rsplit(" ", 1)[0] + "…"

    steps = []
    for i, p in enumerate(cleaned[:6], 1):
        label = f"Étape {i}" if art_type in {"tutorial", "guide", "toolbox"} else f"Point {i}"
        # Titre court
        first = p.split(".")[0].strip()
        if 12 < len(first) < 70 and not first.lower().startswith(("ensuite", "donc", "après", "apres")):
            heading = first[0].upper() + first[1:]
        else:
            heading = label
        steps.append(f"### {heading}\n\n{p}\n")

    # Ajouts pedagogiques pour allonger sans blabla vide
    why = f"""## Pourquoi ca vaut le coup

Tu n'as pas besoin d'etre expert. Tu as juste besoin d'une methode claire, d'un premier essai, et d'un endroit ou noter ce qui marche.

Sur le sujet **{title}**, le plus gros gain vient souvent du premier test serieux : tu vois tout de suite ce qui bloque, et tu ajustes.

Si tu publies ensuite un contenu (article, page, fiche produit), pense structure : un `h1`, des `h2` clairs, une meta description honnete, et des microdonnees (`BlogPosting`, FAQ si tu as des questions/reponses). Ca aide Google et les moteurs IA a te citer.
"""

    how = f"""## Comment l'utiliser demain matin

1. Ouvre l'outil concerne et refais le parcours une fois sans viser la perfection.
2. Garde le prompt / la methode dans un fichier texte (ou un GPT / Project dedie).
3. Adapte le resultat a ton cas : ton ton, ton client, ton offre.
4. Verifie les infos sensibles avant de publier ou d'envoyer.
5. Si ca marche, transforme-le en mini process (checklist de 5 lignes max).
"""

    mistakes = """## Erreurs frequentes

- Copier-coller brut sans relire (ca se voit tout de suite).
- Demander trop vague : "fais-moi quelque chose de bien".
- Changer d'outil toutes les 10 minutes au lieu de finir un essai.
- Oublier le contexte (pour qui, pour quel objectif, sous quelle contrainte).
- Croire que "gratuit" veut toujours dire "illimite" : regarde les quotas.
"""

    faq = """## Questions fréquentes

### C'est adapté aux débutants ?

Oui. Tu peux suivre ça même si tu débutes, tant que tu testes au fur et à mesure. Lire sans pratiquer, ça sert à rien ici.

### Combien de temps ça prend ?

Compte entre 20 et 45 minutes pour le premier essai. Après, tu vas plus vite.

### Faut-il un compte payant ?

Pas forcément. Beaucoup d'outils ont un plan gratuit suffisant pour commencer. Si tu bloques, passe à l'outil suivant plutôt que de forcer.

### Comment rendre ca visible (SEO / GEO) ?

Structure tes pages, ecris pour un humain d'abord, ajoute une FAQ utile, et garde une image OG dediee. Les microdonnees du blog (`BlogPosting`, fil d'Ariane) sont deja en place cote template.
"""

    checklist = """## Mini checklist

- [ ] Tu as testé l'astuce une fois de bout en bout
- [ ] Tu as noté le prompt / la méthode quelque part
- [ ] Tu as adapté le résultat à ton cas (pas de copier-coller brut)
- [ ] Tu as vérifié les infos sensibles avant de publier
- [ ] Tu as decide si ca devient un process recurrent
"""

    banner = f"""<figure>
  <img src="../../assets/images/blog/illustrations/{slug}-banner.webp" alt="Illustration : {title}" class="schema-inline" width="720" loading="lazy" />
  <figcaption>Illustration de l'article - repere visuel pour retenir la methode.</figcaption>
</figure>
"""

    type_blurb = _accent(TYPE_INTRO.get(art_type, TYPE_INTRO["article"]))

    body = f"""# {title}

{_accent(type_blurb)}

{banner}
## En clair

{resume}

---

## Deroule

{''.join(steps)}
---

{_accent(why)}

---

{_accent(how)}

---

{_accent(mistakes)}

---

{checklist}

---

{_accent(faq)}

---

## Suite logique

Cette page fait partie de la série associée. Enchaîne avec les autres articles de la série pour construire un vrai parcours, pas juste une astuce isolée.
"""
    body = (
        body.replace("'", "'")
        .replace("'", "'")
        .replace("'", "'")
        .replace("—", "-")
        .replace("–", "-")
    )
    body = _accent(body)
    body = body.replace("microdonnees", "microdonnées").replace("dediee", "dédiée")
    body = body.replace("ecris", "écris").replace("deja", "déjà").replace("isolee", "isolée")
    body = body.replace("decide", "décidé").replace("recurrent", "récurrent")
    body = body.replace("Deroule", "Déroulé")
    return body


def rebuild_frontmatter(meta: dict, slug: str) -> str:
    title = meta.get("title", slug)
    date = meta.get("date", "2026-05-01")
    excerpt = meta.get("excerpt", title)
    # excerpt plus propre si trop "transcript"
    if excerpt.lower().startswith("comment ") and "?" in excerpt:
        excerpt = excerpt.split("?")[0] + "?"
    if len(excerpt) > 200:
        excerpt = excerpt[:197].rsplit(" ", 1)[0] + "…"
    art_type = meta.get("type", "article")
    tags = meta.get("tags", "[IA]")
    if not tags.startswith("["):
        tags = f"[{tags}]"
    og = meta.get("og_image", f"{slug}-1200x630.jpg")
    series = meta.get("series", "")
    order = meta.get("series_order", "1")
    return f"""---
title: "{title.replace('"', '\\"')}"
date: {date}
excerpt: "{excerpt.replace('"', '\\"')}"
type: {art_type}
tags: {tags}
og_image: {og}
series: {series}
series_order: {order}
---

"""


def main() -> None:
    items = json.loads(MANIFEST.read_text(encoding="utf-8"))
    ILLUSTRATIONS.mkdir(parents=True, exist_ok=True)
    n = 0
    for item in items:
        slug = item["slug"]
        path = ARTICLES / f"{slug}.md"
        if not path.exists():
            print(f"[SKIP] missing {slug}")
            continue
        text = path.read_text(encoding="utf-8")
        meta, body = parse_fm(text)
        # sync title from manifest if cleaner
        if item.get("title"):
            meta["title"] = item["title"]
        new_body = build_rich_body(meta, slug, body)
        path.write_text(rebuild_frontmatter(meta, slug) + new_body, encoding="utf-8")
        n += 1
        print(f"[OK] {slug}")
    print(f"\nEnriched {n} articles")


if __name__ == "__main__":
    main()
