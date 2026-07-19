#!/usr/bin/env python3
"""Simplifie series IA Outils + Gemini."""
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
COLLECTIONS = ROOT / "blog" / "content" / "collections"


def write_svg(fname: str, title: str, desc: str, body: str) -> None:
    SCHEMAS.mkdir(parents=True, exist_ok=True)
    (SCHEMAS / fname).write_text(svg_wrap(title, desc, body), encoding="utf-8")


def fig(fname: str, alt: str, caption: str) -> str:
    return f'''<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/{fname}" alt="{esc(alt)}" class="schema-inline" width="640" />
  <figcaption>{esc(caption)}</figcaption>
</figure>'''


def patch_fm(raw: str, title: str, excerpt: str) -> str:
    end = raw.find("\n---", 3)
    fm = raw[: end + 4]
    fm = re.sub(r'^title:\s*".*?"', f'title: "{title}"', fm, count=1, flags=re.M)
    esc_ex = excerpt.replace('"', '\\"')
    fm = re.sub(r'^excerpt:\s*".*?"', f'excerpt: "{esc_ex}"', fm, count=1, flags=re.M)
    return fm


def article(slug: str, title: str, excerpt: str, body: str) -> None:
    path = ARTICLES / f"{slug}.md"
    raw = path.read_text(encoding="utf-8")
    fm = patch_fm(raw, title, excerpt)
    path.write_text(fm + "\n\n" + body.lstrip() + "\n", encoding="utf-8")
    print(f"[OK] {slug}")


SVGS = [
    ("ia-outils-alt.svg", "Alternatives IA", "Gratuit / local / cloud",
     compare2("Cloud payant", ["Souvent plus fort", "Abonnement"],
              "Gratuit / local", ["Moins cher", "Plus de setup"],
              "Choisis selon budget et confidentialite")),
    ("ia-outils-compare.svg", "Comparer les modeles", "Tester sur ton cas",
     flow_row(["Meme tache", "Outil A", "Outil B", "Juger", "Choisir"],
              "Le meilleur outil = celui qui marche sur TON besoin")),
    ("ia-outils-agent.svg", "Agents IA", "Au-dela du chat",
     flow_row(["Objectif", "Outils", "Etapes", "Resultat", "Verifier"],
              "Un agent agit ; toi tu cadres et tu controles")),
    ("ia-outils-open.svg", "Open source", "Tourner chez toi",
     stack_layers([
         ("Modele", "Telecharge / heberge"),
         ("Interface", "Chat local"),
         ("Limites", "Machine + qualite"),
         ("Gain", "Controle des donnees"),
     ], "Utile pour apprendre et pour la confidentialite")),
    ("ia-outils-stack.svg", "Stack pratique", "Base + templates",
     grid3([
         ("Donnees", "Base simple"),
         ("Automation", "n8n / flux"),
         ("IA", "Modele adapte"),
         ("Tutoriels", "Apprendre vite"),
         ("Tester", "Petit cas"),
         ("Iterer", "Ameliorer"),
     ], "Commence petit, branche ensuite")),
    ("ia-gemini-start.svg", "Demarrer Gemini", "Compte et premiers essais",
     flow_row(["Ouvrir", "Prompt clair", "Fichiers", "Relancer", "Sauver"],
              "Meme logique : clarifier avant de generer")),
    ("ia-gemini-notebook.svg", "NotebookLM", "Sources + resume + podcast",
     flow_row(["Sources", "Notebook", "Questions", "Audio", "Verifier"],
              "L'IA s'appuie sur TES documents")),
    ("ia-gemini-learn.svg", "Formations Google", "Skills et certifications",
     stack_layers([
         ("Catalogue", "Choisir un parcours"),
         ("Cours", "Suivre les modules"),
         ("Pratique", "Mini projet"),
         ("CV", "Ajouter la preuve"),
     ], "Apprendre + montrer + appliquer")),
    ("ia-gemini-apps.svg", "Mini-apps Gemini", "Explorer et tester",
     flow_row(["Galerie", "Choisir", "Essayer", "Adapter", "Garder"],
              "Inspire-toi, puis recree pour ton usage")),
    ("ia-gemini-long.svg", "Projets longs", "Memoire et structure",
     compare2("Chat unique", ["Se perd vite", "Contexte flou"],
              "Projet structure", ["Fichiers", "Plan", "Points de reprise"],
              "Pour un memo long : decoupe et documents")),
]
for item in SVGS:
    write_svg(*item)

# ---- Outils ----
article(
    "ia-outils-base-de-donnees-gratuite-avec-des-templates-n8n-et-des-tutoriels-pour",
    "Base + n8n : une stack gratuite pour demarrer",
    "Associer une base simple, des templates d'automation et des tutos — sans tout complexifier.",
    f"""# Base + n8n : une stack gratuite pour demarrer

Tu n'as pas besoin d'une usine. Une **base**, des **templates**, un peu d'IA.

{fig("ia-outils-stack.svg", "Schema stack IA pratique", "Donnees, automation, IA, tester.")}

Prends un cas reel (relance email, fiche client). Branche ensuite. Suite agents : [creer un agent](/blog/articles/ia-agents-tutoriel-debutant-comment-creer-un-agent-ia-en-quelques-minutes.html).
""",
)

article(
    "ia-outils-comment-installer-une-alternative-gratuite-a-chatgpt-pour-l-ut",
    "Alternative gratuite a ChatGPT : installer en local",
    "Faire tourner un chat IA sur ta machine : gratuit, plus de controle, un peu plus de setup.",
    f"""# Alternative gratuite a ChatGPT : installer en local

Une IA **locale** marche sans abonnement cloud — si ta machine suit.

{fig("ia-outils-open.svg", "Schema IA open source locale", "Modele, interface, limites, gain.")}

Installe une interface (type Ollama / LM Studio), choisis un modele leger, teste. Voir aussi [HuggingChat](/blog/articles/ia-outils-une-ia-comme-chatgpt-mais-gratuite-huggingchat-d.html).
""",
)

article(
    "ia-outils-une-ia-comme-chatgpt-mais-gratuite-huggingchat-d",
    "HuggingChat : une IA gratuite dans le navigateur",
    "Discuter sans payer d'abonnement — utile pour tester, avec des limites selon le trafic.",
    f"""# HuggingChat : une IA gratuite dans le navigateur

Pas de carte bleue obligatoire pour **essayer**.

{fig("ia-outils-alt.svg", "Schema alternatives IA", "Cloud payant versus gratuit.")}

Ouvre, teste la meme tache que sur ChatGPT, compare. Pour du local : [installer une alternative](/blog/articles/ia-outils-comment-installer-une-alternative-gratuite-a-chatgpt-pour-l-ut.html).
""",
)

article(
    "ia-outils-un-studio-de-jeu-video-japonais-a-trouve-une-solution-contre-l-utilis",
    "Portfolios et IA : comment les studios filtrent",
    "Quand l'IA gonfle un book : tests pratiques et preuves de travail reel.",
    f"""# Portfolios et IA : comment les studios filtrent

L'IA peut embellir un portfolio. Les recruteurs cherchent des **preuves** en conditions reelles.

{fig("ia-outils-compare.svg", "Schema evaluation talent", "Tester sur un vrai exercice.")}

Si tu postules : montre ton process, pas seulement le rendu. Si tu recrutes : fais faire un petit exercice supervise.
""",
)

article(
    "ia-outils-l-intelligence-artificielle-va-t-elle-mener-a-la-fin-du-capitalisme",
    "IA et economie : des idees, pas des certitudes",
    "Debats sur productivite et travail : lire, relativiser, garder l'esprit critique.",
    f"""# IA et economie : des idees, pas des certitudes

Les essays "l'IA va tout changer" sont stimulants — pas des **preuves**.

{fig("ia-outils-compare.svg", "Schema esprit critique", "Lire, comparer, juger.")}

Lis plusieurs points de vue. Regarde ce qui change **deja** dans ton metier. Suite : [metiers](/blog/articles/ia-metiers-voici-la-liste-des-metiers-avec-la-croissance-la-plus-rapide-en-2026.html).
""",
)

article(
    "ia-outils-chatgpt-agent-vient-de-sortir-les-agents-ia-feront-bientot-partie-d",
    "ChatGPT Agent : quand le chat commence a agir",
    "Au-dela des reponses : des etapes, des outils, et surtout une verification humaine.",
    f"""# ChatGPT Agent : quand le chat commence a agir

Un **agent** ne se contente pas de repondre : il enchaine des actions.

{fig("ia-outils-agent.svg", "Schema agent IA", "Objectif, outils, etapes, verifier.")}

Donne un perimetre clair. Verifie le resultat. Serie agents : [tutoriel debutant](/blog/articles/ia-agents-tutoriel-debutant-comment-creer-un-agent-ia-en-quelques-minutes.html).
""",
)

article(
    "ia-outils-comment-utiliser-chatgpt-with-canvas-nouveau-chatgpt",
    "ChatGPT Canvas : ecrire et iterer cote a cote",
    "Une zone de travail pour corriger un texte ou un code sans tout recommencer dans le chat.",
    f"""# ChatGPT Canvas : ecrire et iterer cote a cote

Canvas sert a **travailler sur un document** avec l'IA a cote.

{fig("ia-gemini-start.svg", "Schema collaboration IA", "Ouvrir, ecrire, relancer, sauver.")}

Colle un brouillon, demande des passes ciblees ("raccourcis", "clarifie"). Base prompts : [methode](/blog/articles/ia-prompts-comment-creer-de-meilleurs-prompt-sur-chatgpt-site-gratuit.html).
""",
)

article(
    "ia-outils-deepseek-l-ia-chinoise-gratuite-et-open-source-a-t-elle-copie-openai",
    "DeepSeek vs OpenAI : comprendre la polemique (simplement)",
    "Accusations de copie, open source, prix : ce qu'il faut retenir pour choisir un outil.",
    f"""# DeepSeek vs OpenAI : comprendre la polemique (simplement)

Les annonces vont vite. Pour toi : **qualite**, **prix**, **confidentialite**.

{fig("ia-outils-alt.svg", "Schema choix d'IA", "Comparer sans se perdre dans le bruit.")}

Teste sur ton usage. Ne mets pas de donnees sensibles n'importe ou. Voir [DeepSeek pratique](/blog/articles/ia-claude-comment-utiliser-l-ia-chinoise-gratuite-et-open-source-deepseek-en-ve.html).
""",
)

article(
    "ia-outils-test-des-differentes-versions-de-chatgpt-dont-le-nouveau-chatgpt-4-5",
    "Versions de ChatGPT : comment choisir sans se perdre",
    "Pas la meilleure version absolue : celle qui repond a ta tache et a ton budget.",
    f"""# Versions de ChatGPT : comment choisir sans se perdre

Les noms changent. Ta methode non.

{fig("ia-outils-compare.svg", "Schema comparer versions ChatGPT", "Meme tache, deux modeles, juger.")}

Prends **une** tache type, lance deux modeles, compare cout / qualite / vitesse. Template : [bon prompt](/blog/articles/ia-chatgpt-comment-utiliser-chatgpt-5-template-a-suivre-pour-creer-de-meilleur.html).
""",
)

article(
    "ia-outils-google-vient-de-sortir-la-meilleure-ia-open-source-gemma-4-pour-l-u",
    "Gemma (Google) : une IA open a tester chez toi",
    "Modele open de Google : interessant pour local / experimentation, a calibrer selon ta machine.",
    f"""# Gemma (Google) : une IA open a tester chez toi

Gemma vise l'usage **open** / local, pas seulement le cloud.

{fig("ia-outils-open.svg", "Schema modele open Google", "Telecharge, interface, limites.")}

Choisis une taille adaptee a ta RAM, teste, compare a [HuggingChat](/blog/articles/ia-outils-une-ia-comme-chatgpt-mais-gratuite-huggingchat-d.html).
""",
)

# ---- Gemini ----
article(
    "ia-gemini-alerte-formations-ia-gratuites-par-google-avec-google-skills-il-y-a-p",
    "Google Skills : formations IA gratuites a explorer",
    "Parcours Google pour apprendre l'IA : choisir un module, pratiquer, garder une preuve.",
    f"""# Google Skills : formations IA gratuites a explorer

Google publie des parcours. L'astuce : en finir **un**, pas en ouvrir vingt.

{fig("ia-gemini-learn.svg", "Schema formations Google Skills", "Catalogue, cours, pratique, CV.")}

Choisis un theme utile a ton job. Suite certifs : [3 certifications](/blog/articles/ia-gemini-3-certifications-ia-gratuites-a-ajouter-sur-votre-cv-pour-les-debutan.html).
""",
)

article(
    "ia-gemini-comment-creer-un-assistant-ia-gratuit-avec-gemini-l-ia-de",
    "Assistant Gemini gratuit : creer le tien",
    "Configurer un assistant avec consignes claires pour un usage precis (etudiant, job, hobby).",
    f"""# Assistant Gemini gratuit : creer le tien

Un assistant = des **instructions** + un usage repete.

{fig("ia-gemini-start.svg", "Schema assistant Gemini", "Ouvrir, consignes, tester.")}

Ecris son role, ton, limites. Teste 3 questions types. Voir [utiliser Gemini](/blog/articles/ia-gemini-comment-utiliser-gemini-l-intelligence-artificielle-de-goo.html).
""",
)

article(
    "ia-gemini-un-homme-vient-de-creer-un-conseil-des-ia-avec-un-tutoriel-pour-fair",
    "Conseil d'IA : faire debattre plusieurs modeles",
    "Comparer plusieurs reponses sur le meme sujet pour enrichir ta decision — sans tout croire.",
    f"""# Conseil d'IA : faire debattre plusieurs modeles

Une idee simple : poser **la meme question** a plusieurs IA, puis trancher.

{fig("ia-outils-compare.svg", "Schema conseil multi-IA", "Meme question, plusieurs avis, juger.")}

Utile pour brainstorm. Dangereux pour les faits sensibles : verifie toujours.
""",
)

article(
    "ia-gemini-3-certifications-ia-gratuites-a-ajouter-sur-votre-cv-pour-les-debutan",
    "3 certifications IA gratuites (utiles sur un CV)",
    "Choisir des preuves concretes : cours termines + mini projet, pas juste des badges.",
    f"""# 3 certifications IA gratuites (utiles sur un CV)

Un badge sans pratique convainc peu. Vise **cours + projet**.

{fig("ia-gemini-learn.svg", "Schema certifications IA", "Cours, pratique, preuve.")}

Liste 3 parcours (Google / Microsoft / autre), termine-en un cette semaine. Formations : [Google Skills](/blog/articles/ia-gemini-alerte-formations-ia-gratuites-par-google-avec-google-skills-il-y-a-p.html).
""",
)

article(
    "ia-gemini-comment-utiliser-gemini-l-intelligence-artificielle-de-goo",
    "Gemini : demarrer en 5 minutes",
    "Ouvrir Gemini, poser une demande claire, ajouter un fichier si besoin, iterer.",
    f"""# Gemini : demarrer en 5 minutes

Meme base que ChatGPT : **clarte**.

{fig("ia-gemini-start.svg", "Schema demarrage Gemini", "Ouvrir, prompt, fichiers, relancer.")}

1. Compte Google  
2. Prompt avec but + format  
3. Joins un PDF si utile  

Astuce etudiants : [Gemini etudes](/blog/articles/ia-gemini-vous-connaissez-cette-astuce-sur-gemini-parfait-pour-les-etudiants.html).
""",
)

article(
    "ia-gemini-vous-connaissez-cette-astuce-sur-gemini-parfait-pour-les-etudiants",
    "Astuce Gemini etudiants : apprendre plus vite",
    "Resumes, quiz, reformulations : transformer un cours en questions pour retenir.",
    f"""# Astuce Gemini etudiants : apprendre plus vite

Colle un cours, demande : resume + **10 questions** + corrections.

{fig("ia-gemini-start.svg", "Schema revision avec Gemini", "Cours, questions, verifier.")}

Fais les questions **sans** regarder. Corrige ensuite. NotebookLM : [podcast FR](/blog/articles/ia-gemini-comment-avoir-le-podcast-notebooklm-en-francais-precision.html).
""",
)

article(
    "ia-gemini-comment-avoir-un-assistant-gratuit-sur-votre-ordinateur-pour-a",
    "Assistant IA sur l'ordi : gratuit et sous la main",
    "Raccourci navigateur, app, ou modele local : choisis selon confidentialite et confort.",
    f"""# Assistant IA sur l'ordi : gratuit et sous la main

L'objectif : y acceder en **un clic**, pas en 10 onglets.

{fig("ia-outils-open.svg", "Schema assistant sur ordinateur", "Acces rapide, local ou cloud.")}

Epingles Gemini / ChatGPT, ou installe du local. Creer un assistant : [Gemini](/blog/articles/ia-gemini-comment-creer-un-assistant-ia-gratuit-avec-gemini-l-ia-de.html).
""",
)

article(
    "ia-gemini-comment-avoir-le-podcast-notebooklm-en-francais-precision",
    "Podcast NotebookLM en francais : reglage simple",
    "Importer tes sources, generer l'audio, verifier la langue et le contenu.",
    f"""# Podcast NotebookLM en francais : reglage simple

NotebookLM part de **tes documents** pour resumer / discuter / audio.

{fig("ia-gemini-notebook.svg", "Schema NotebookLM", "Sources, questions, audio, verifier.")}

Ajoute tes PDFs, precise la langue si besoin, ecoute, corrige les erreurs. Base Gemini : [demarrer](/blog/articles/ia-gemini-comment-utiliser-gemini-l-intelligence-artificielle-de-goo.html).
""",
)

article(
    "ia-gemini-quelle-ia-choisir-pour-des-projets-longs-comme-la-redaction-d-un-memo",
    "Projet long (memo, livre) : quelle IA et quelle methode",
    "Decouper, garder des fichiers sources, reprendre le fil — plus important que le logo de l'outil.",
    f"""# Projet long (memo, livre) : quelle IA et quelle methode

Sur un long projet, le chat unique **oublie**. Structure.

{fig("ia-gemini-long.svg", "Schema projet long avec IA", "Plan, fichiers, points de reprise.")}

Plan en chapitres, un fichier par partie, resume de suivi. NotebookLM aide avec les sources. Voir [NotebookLM](/blog/articles/ia-gemini-comment-avoir-le-podcast-notebooklm-en-francais-precision.html).
""",
)

article(
    "ia-gemini-comment-acceder-a-des-milliers-de-mini-applications-creees-par-les-ut",
    "Mini-apps Gemini : explorer la galerie",
    "Trouver des petites apps faites par la communaute, tester, puis adapter a ton besoin.",
    f"""# Mini-apps Gemini : explorer la galerie

Des utilisateurs partagent des **mini-apps**. Inspire-toi, ne copie pas aveuglement.

{fig("ia-gemini-apps.svg", "Schema galerie mini-apps", "Choisir, essayer, adapter.")}

Teste 2 apps utiles, note ce qui marche, recree une version simple pour toi.
""",
)

for name, title, desc in (
    (
        "ia-outils-serie.json",
        "Serie IA — Outils et alternatives (simples)",
        "Comparer, installer, tester : ChatGPT, open source, agents et stacks pratiques.",
    ),
    (
        "ia-gemini-serie.json",
        "Serie IA — Gemini et Google (demarrer clairement)",
        "Gemini, NotebookLM, Skills et certifications expliques simplement.",
    ),
):
    path = COLLECTIONS / name
    col = json.loads(path.read_text(encoding="utf-8"))
    col["title"] = title
    col["description"] = desc
    path.write_text(json.dumps(col, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"[OK] {name}")

print("done")
