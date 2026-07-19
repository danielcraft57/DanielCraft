#!/usr/bin/env python3
"""Simplifie SEO + GEO : titres, corps accessibles, schemas."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from add_series3_extra_schemas import (  # noqa: E402
    SCHEMAS,
    compare2,
    esc,
    flow_row,
    grid3,
    stack_layers,
    svg_wrap,
)

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "blog" / "content" / "articles"


def write_svg(fname: str, title: str, desc: str, body: str) -> None:
    SCHEMAS.mkdir(parents=True, exist_ok=True)
    (SCHEMAS / fname).write_text(svg_wrap(title, desc, body), encoding="utf-8")


def fig(fname: str, alt: str, caption: str) -> str:
    return f'''<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/{fname}" alt="{esc(alt)}" class="schema-inline" width="640" />
  <figcaption>{esc(caption)}</figcaption>
</figure>'''


def patch_frontmatter(raw: str, title: str, excerpt: str) -> tuple[str, str]:
    end = raw.find("\n---", 3)
    fm, body = raw[: end + 4], raw[end + 4 :]
    fm = re.sub(r'^title:\s*".*?"', f'title: "{title}"', fm, count=1, flags=re.M)
    fm = re.sub(
        r'^excerpt:\s*".*?"',
        f'excerpt: "{excerpt.replace(chr(34), chr(92)+chr(34))}"',
        fm,
        count=1,
        flags=re.M,
    )
    return fm, body


def article(slug: str, title: str, excerpt: str, body_md: str) -> None:
    path = ARTICLES / f"{slug}.md"
    raw = path.read_text(encoding="utf-8")
    fm, _ = patch_frontmatter(raw, title, excerpt)
    path.write_text(fm + "\n\n" + body_md.lstrip() + "\n", encoding="utf-8")
    print(f"[OK] {slug}")


SVGS = [
    ("seo-trois-piliers.svg", "Trois piliers SEO", "Technique, contenu, autorite",
     grid3([
         ("Technique", "Site rapide et lisible"),
         ("Contenu", "Reponses utiles"),
         ("Autorite", "Liens et confiance"),
         ("Crawl", "Google trouve"),
         ("Index", "Google range"),
         ("Classement", "Google trie"),
     ], "Les trois piliers marchent ensemble")),
    ("seo-technique.svg", "SEO technique", "Vitesse, mobile, indexation",
     flow_row(["Crawl", "Index", "Vitesse", "Mobile", "HTTPS"],
              "Un site lent ou casse perd des places facilement")),
    ("seo-contenu.svg", "Contenu SEO", "Intention de recherche",
     flow_row(["Question", "Intention", "Page utile", "Titres clairs", "Liens internes"],
              "Ecrire pour les gens d'abord, Google ensuite")),
    ("seo-local.svg", "SEO local", "Etre trouve pres de chez soi",
     stack_layers([
         ("Fiche Google Business", "Infos a jour"),
         ("Avis clients", "Preuves sociales"),
         ("Pages locales", "Ville / service"),
         ("Citations NAP", "Nom adresse tel coherents"),
     ], "Le local, c'est la confiance de proximite")),
    ("seo-backlinks.svg", "Backlinks", "Liens depuis d'autres sites",
     compare2("Liens utiles", ["Sites de confiance", "Contexte clair", "Naturels"],
              "Liens foireux", ["Ferme de liens", "Hors sujet", "Achat massif"],
              "Un bon lien = une recommandation sincere")),
    ("seo-mesure.svg", "Mesurer le SEO", "Search Console et analytics",
     grid3([
         ("Impressions", "On t'a vu"),
         ("Clics", "On est venu"),
         ("Positions", "Ou tu es"),
         ("Pages", "Quelles URLs"),
         ("Requetes", "Quels mots"),
         ("Conversions", "Objectif metier"),
     ], "Mesure pour apprendre, pas pour se vanter")),
    ("seo-schema-org.svg", "Donnees structurees", "Aider Google a comprendre",
     flow_row(["Page", "Balises", "Schema.org", "Rich result", "Clic"],
              "Des infos claires pour les machines, sans tricher")),
    ("seo-vs-sea.svg", "SEO vs SEA", "Organique vs payant",
     compare2("SEO", ["Gratuit au clic", "Lent a monter", "Dure dans le temps"],
              "SEA", ["Payant au clic", "Rapide", "S'arrete si budget stop"],
              "Souvent les deux : SEA pour demarrer, SEO pour tenir")),
    ("geo-intro.svg", "GEO en bref", "Etre cite par les IA",
     flow_row(["Contenu clair", "Sources", "Mentions", "IA lit", "Citation"],
              "GEO = etre une source que les IA aiment citer")),
    ("geo-vs-seo.svg", "GEO et SEO", "Complementaires",
     compare2("SEO", ["Pages Google", "Clics site", "Classement"],
              "GEO", ["Reponses IA", "Citations", "Autorite"],
              "Meme base : contenu fiable et bien structure")),
    ("geo-outils.svg", "Suivre le GEO", "Audit et citations",
     flow_row(["Chercher", "Citations", "Sources", "Ecarts", "Ameliorer"],
              "Tu ne geres que ce que tu mesures")),
    ("geo-technique.svg", "GEO technique", "HTML lisible par les IA",
     stack_layers([
         ("HTML propre", "Titres et textes"),
         ("Performance", "Pages rapides"),
         ("Indexable", "Pas bloque"),
         ("Structure", "Listes, FAQ, schema"),
     ], "Si une IA ne peut pas lire, elle ne cite pas")),
    ("geo-contenu.svg", "Contenu GEO", "Formats qui aident",
     grid3([
         ("FAQ", "Questions/reponses"),
         ("Listes", "Etapes claires"),
         ("Definitions", "Phrases nettes"),
         ("Preuves", "Chiffres / sources"),
         ("Auteur", "Qui ecrit"),
         ("Maj", "Date a jour"),
     ], "La clarte bat le jargon")),
    ("geo-offsite.svg", "Autorite hors site", "Mentions ailleurs",
     flow_row(["Contenu utile", "Partages", "Mentions", "Liens", "Confiance"],
              "Etre cite ailleurs renforce ta credibilite")),
    ("geo-optimiser-ia.svg", "Optimiser pour les IA", "ChatGPT, Perplexity, SGE",
     stack_layers([
         ("Reponses directes", "En tete de page"),
         ("Sources citees", "Liens fiables"),
         ("Couverture du sujet", "Pas trop mince"),
         ("Cohérence multi-pages", "Serie / hub"),
     ], "Aide l'IA a te resumer correctement")),
]
for item in SVGS:
    write_svg(*item)

# ---- SEO articles ----
article(
    "seo-fondamentaux-referencement-naturel",
    "SEO : etre trouve sur Google (les bases)",
    "Comment Google decouvre, range et classe les pages — et par ou commencer sans jargon.",
    f"""# SEO : etre trouve sur Google (les bases)

Le **SEO**, c'est simplement : aider ton site a etre **trouve** quand quelqu'un cherche sur Google. Pas de magie. Des bases solides.

{fig("seo-trois-piliers.svg", "Schema des trois piliers du SEO", "Technique, contenu, autorite — les trois marchent ensemble.")}

## Comment Google travaille (en 3 etapes)

1. **Crawl** : ses robots se promement et decouvrent des pages
2. **Index** : il range ce qu'il a compris
3. **Classement** : pour une question, il trie les pages les plus utiles

Si ta page n'est pas indexee, elle n'apparait pas. Point.

## Les trois piliers

- **Technique** : site rapide, mobile, accessible aux robots
- **Contenu** : reponses claires aux vraies questions
- **Autorite** : d'autres sites (et gens) te font confiance

Commence petit : une page utile, des titres clairs, un site qui charge. Ensuite [technique](/blog/articles/seo-technique-audit-core-web-vitals.html), [contenu](/blog/articles/seo-contenu-mots-cles-intention-redaction.html), [mesure](/blog/articles/seo-mesurer-search-console-analytics-kpis.html).
""",
)

article(
    "seo-technique-audit-core-web-vitals",
    "SEO technique : un site rapide et lisible par Google",
    "Vitesse, mobile, indexation : les bases techniques qui aident (ou freinent) ta visibilite.",
    f"""# SEO technique : un site rapide et lisible par Google

Le SEO technique, c'est l'**etat du magasin** : portes ouvertes, rayons lisibles, lumiere allumee. Sinon personne ne reste.

{fig("seo-technique.svg", "Schema SEO technique", "Crawl, index, vitesse, mobile, HTTPS.")}

## A verifier en premier

- Pages **indexables** (pas bloquees par erreur)
- **HTTPS**
- Affichage **mobile** correct
- **Vitesse** raisonnable (Core Web Vitals = signes de confort)
- Titres et balises presentes

Tu n'as pas besoin d'etre parfait. Tu as besoin d'enlever les gros cailloux. Puis travaille le [contenu](/blog/articles/seo-contenu-mots-cles-intention-redaction.html).
""",
)

article(
    "seo-contenu-mots-cles-intention-redaction",
    "SEO contenu : repondre a ce que les gens cherchent vraiment",
    "Mots-cles, intention de recherche et pages utiles — ecrire pour les humains d'abord.",
    f"""# SEO contenu : repondre a ce que les gens cherchent vraiment

Un bon contenu SEO, ce n'est pas bourrer des mots-cles. C'est **repondre** a une question claire.

{fig("seo-contenu.svg", "Schema contenu SEO et intention", "Question, intention, page utile, titres, liens internes.")}

## Intention : le vrai sujet

Les gens cherchent pour :
- **apprendre** (guides)
- **comparer** (vs, avis)
- **acheter** / contacter

Aligne ta page sur l'intention. Ajoute des [liens internes](/blog/articles/seo-fondamentaux-referencement-naturel.html) vers tes autres pages utiles.
""",
)

article(
    "seo-local-google-business-avis",
    "SEO local : etre trouve pres de chez tes clients",
    "Fiche Google, avis et pages locales : la visibilite de proximite expliquee simplement.",
    f"""# SEO local : etre trouve pres de chez tes clients

Le **SEO local**, c'est apparaitre quand quelqu'un cherche un service **pres de lui**.

{fig("seo-local.svg", "Schema SEO local", "Fiche Google, avis, pages locales, infos coherentes.")}

## Les bases

- Fiche **Google Business** a jour
- **Avis** clients (et reponses polies)
- Nom / adresse / telephone **identiques** partout
- Une page claire par ville / service si besoin

C'est de la confiance de voisinage, pas du jargon.
""",
)

article(
    "seo-backlinks-netlinking-strategie",
    "Backlinks : les recommandations d'autres sites",
    "Les liens entrants utiles (et ceux a eviter) pour renforcer ta credibilite.",
    f"""# Backlinks : les recommandations d'autres sites

Un **backlink**, c'est un autre site qui pointe vers toi. Comme une recommandation.

{fig("seo-backlinks.svg", "Schema backlinks utiles vs foireux", "Liens de confiance contre fermes de liens.")}

## Qualite > quantite

Un lien depuis un site serieux dans ton sujet vaut mieux que 100 liens douteux. Evite l'achat massif. Mieux : contenu utile, partenariats, mentions. Voir aussi le [GEO hors site](/blog/articles/geo-off-site-mentions-autorite.html).
""",
)

article(
    "seo-mesurer-search-console-analytics-kpis",
    "Mesurer le SEO : savoir ce qui marche vraiment",
    "Search Console et analytics : impressions, clics, positions — sans vanity metrics.",
    f"""# Mesurer le SEO : savoir ce qui marche vraiment

Sans mesure, tu avances a l'aveugle. Avec trop de chiffres, tu te noies.

{fig("seo-mesure.svg", "Schema mesures SEO utiles", "Impressions, clics, positions, pages, requetes, conversions.")}

## Le tableau de bord minimal

- Quelles **requetes** amènent des clics ?
- Quelles **pages** montent ou baissent ?
- Est-ce que ca mene a un **objectif** (contact, achat) ?

Search Console + analytics suffisent pour demarrer. Relie ca a ta [strategie contenu](/blog/articles/seo-contenu-mots-cles-intention-redaction.html).
""",
)

article(
    "seo-schema-org-donnees-structurees",
    "Donnees structurees : aider Google a comprendre ta page",
    "Schema.org et rich results : des infos claires pour les machines, sans tricher.",
    f"""# Donnees structurees : aider Google a comprendre ta page

Les **donnees structurees**, c'est etiqueter clairement : "ceci est un article", "ceci est une FAQ", "ceci est une entreprise".

{fig("seo-schema-org.svg", "Schema donnees structurees Schema.org", "Page, balises, Schema.org, rich result, clic.")}

## A quoi ca sert

Google (et d'autres) comprennent mieux. Parfois tu gagnes un affichage enrichi. Ce n'est **pas** un passe-droit de classement. C'est de la clarte. Utile aussi pour le [GEO](/blog/articles/geo-nouveau-seo-ia-guide-complet.html).
""",
)

article(
    "seo-vs-sea-quand-choisir",
    "SEO ou pubs Google (SEA) : quoi choisir",
    "Organique vs payant : quand miser sur le SEO, le SEA, ou les deux.",
    f"""# SEO ou pubs Google (SEA) : quoi choisir

Le **SEO** gagne des clics "gratuits" (mais demande du temps). Le **SEA**, tu paies pour apparaitre tout de suite.

{fig("seo-vs-sea.svg", "Schema SEO versus SEA", "SEO durable vs SEA rapide et payant.")}

## En pratique

- Besoin **rapide** : SEA
- Visibilite **durable** : SEO
- Souvent : les **deux** (SEA le temps que le SEO monte)

Pas de guerre de religion. Un budget et un objectif clairs.
""",
)

# ---- GEO ----
article(
    "geo-nouveau-seo-ia-guide-complet",
    "GEO : etre cite par les IA (ChatGPT et cie)",
    "Le referencement pour les moteurs generatifs : comment devenir une source que les IA citent.",
    f"""# GEO : etre cite par les IA (ChatGPT et cie)

Le **GEO** (Generative Engine Optimization), c'est aider les IA a te **trouver** et te **citer** quand elles repondent.

{fig("geo-intro.svg", "Schema GEO en bref", "Contenu clair, sources, mentions, citation par l'IA.")}

## L'idee simple

Les IA aiment les contenus :
- clairs
- fiables
- bien structures
- cites ailleurs

Ce n'est pas "anti-SEO". C'est un cousin du [SEO](/blog/articles/seo-fondamentaux-referencement-naturel.html). Voir [GEO vs SEO](/blog/articles/geo-vs-seo-differences-complementarite.html).
""",
)

article(
    "geo-vs-seo-differences-complementarite",
    "GEO et SEO : differents, mais amis",
    "Pages Google vs reponses IA : ce qui change, et ce qui reste la meme base.",
    f"""# GEO et SEO : differents, mais amis

Le **SEO** vise les pages bleues de Google. Le **GEO** vise les reponses des IA. La base reste : contenu utile et digne de confiance.

{fig("geo-vs-seo.svg", "Schema GEO et SEO complementaires", "SEO pour les clics, GEO pour les citations.")}

Travaille les deux sans les opposer. Technique + contenu + autorite restent les fondations.
""",
)

article(
    "outils-geo-audit-suivi-citations",
    "Suivre le GEO : voir si les IA te citent",
    "Comment auditer tes mentions et citations dans les reponses generatives.",
    f"""# Suivre le GEO : voir si les IA te citent

Tu ameliorest seulement ce que tu **observes**. Pour le GEO : cherche si tu es cite, par qui, sur quels sujets.

{fig("geo-outils.svg", "Schema suivi citations GEO", "Chercher, citations, sources, ecarts, ameliorer.")}

Note les ecarts, renforce les pages faibles, gagne des [mentions](/blog/articles/geo-off-site-mentions-autorite.html).
""",
)

article(
    "geo-technique-indexabilite-html-performance",
    "GEO technique : un HTML que les IA peuvent lire",
    "Pages rapides, textes visibles, structure claire : la base technique du GEO.",
    f"""# GEO technique : un HTML que les IA peuvent lire

Si le texte est cache, casse ou trop lent, l'IA lit mal — ou pas du tout.

{fig("geo-technique.svg", "Schema GEO technique", "HTML propre, performance, indexable, structure.")}

Meme esprit que le [SEO technique](/blog/articles/seo-technique-audit-core-web-vitals.html) : accessibilite machine + confort humain.
""",
)

article(
    "geo-contenu-structure-formats-checklist",
    "Contenu GEO : formats clairs que les IA aiment resumer",
    "FAQ, listes, definitions et preuves : une checklist simple.",
    f"""# Contenu GEO : formats clairs que les IA aiment resumer

Aide l'IA a te citer : reponses **directes**, listes, FAQ, sources.

{fig("geo-contenu.svg", "Schema formats contenu GEO", "FAQ, listes, definitions, preuves, auteur, mise a jour.")}

Ecris comme tu expliques a un ami presse. Puis lie tes pages entre elles ([SEO contenu](/blog/articles/seo-contenu-mots-cles-intention-redaction.html)).
""",
)

article(
    "geo-off-site-mentions-autorite",
    "Autorite hors site : etre mentionne ailleurs",
    "Mentions, partages et liens : renforcer ta credibilite au-dela de ton site.",
    f"""# Autorite hors site : etre mentionne ailleurs

Si personne ne parle de toi ailleurs, les IA (et Google) te font moins confiance.

{fig("geo-offsite.svg", "Schema autorite hors site GEO", "Contenu utile, partages, mentions, liens, confiance.")}

Meme logique que les [backlinks SEO](/blog/articles/seo-backlinks-netlinking-strategie.html) : la qualite compte.
""",
)

article(
    "geo-optimiser-chatgpt-perplexity-sge",
    "Optimiser pour ChatGPT, Perplexity et cie",
    "Des gestes concrets pour etre mieux resume et cite par les assistants IA.",
    f"""# Optimiser pour ChatGPT, Perplexity et cie

Tu ne "hackes" pas ChatGPT. Tu lui facilites le travail : reponse nette en haut, preuves, pages coherentes.

{fig("geo-optimiser-ia.svg", "Schema optimisation pour assistants IA", "Reponses directes, sources, couverture, coherence.")}

Reviens au [guide GEO](/blog/articles/geo-nouveau-seo-ia-guide-complet.html) et mesure tes [citations](/blog/articles/outils-geo-audit-suivi-citations.html).
""",
)

for path, title, desc in [
    (
        ROOT / "blog/content/collections/seo-serie.json",
        "Serie SEO : etre trouve sur Google",
        "Bases, technique, contenu, local, liens et mesure — le referencement explique simplement.",
    ),
    (
        ROOT / "blog/content/collections/geo-serie.json",
        "Serie GEO : etre cite par les IA",
        "Optimiser pour ChatGPT, Perplexity et les moteurs generatifs — complementaire au SEO.",
    ),
]:
    data = json.loads(path.read_text(encoding="utf-8"))
    data["title"] = title.replace("Serie", "Série")
    data["description"] = desc
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"[OK] {path.name}")

print("done")
