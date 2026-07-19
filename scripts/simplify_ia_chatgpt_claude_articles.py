#!/usr/bin/env python3
"""Simplifie series IA ChatGPT + Claude : titres courts, corps debutant, schemas. Pas de bannieres."""
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
    ("ia-chatgpt-prompt.svg", "Bon prompt ChatGPT", "Contexte, tache, format",
     flow_row(["Role", "Contexte", "Tache", "Format", "Exemple"],
              "Plus tu precises, moins tu corrige")),
    ("ia-chatgpt-memoire.svg", "Memoire ChatGPT", "Voir et nettoyer",
     stack_layers([
         ("Parametres", "Ouvre ton compte"),
         ("Memoire / Personalization", "Ce qu'il retient"),
         ("Lire", "Verifier les faits"),
         ("Effacer", "Garder le controle"),
     ], "Tu restes maitre de ce qui est stocke")),
    ("ia-chatgpt-auto.svg", "Automatiser ChatGPT", "Taches repetees",
     flow_row(["Idee", "Prompt fixe", "Declencheur", "Resultat", "Verifier"],
              "Automatise le repetitif, garde l'humain pour le jugement")),
    ("ia-chatgpt-youtube.svg", "Resume YouTube", "URL + resume",
     flow_row(["Lien video", "Demande claire", "Resume", "Points cles", "Verif"],
              "Utile pour gagner du temps, pas pour tout croire aveuglement")),
    ("ia-chatgpt-photo.svg", "Photo + ChatGPT", "Estimer sans certitude",
     compare2("Utile", ["Idee rapide", "Ordre de grandeur", "Apprendre"],
              "Limites", ["Pas exact medical", "Peut se tromper", "Verifier"],
              "Une photo aide a approximer, pas a diagnostiquer")),
    ("ia-chatgpt-lut.svg", "LUT avec ChatGPT", "Idee puis outil pro",
     flow_row(["Style voulu", "Description", "Export / outil", "Import video"],
              "ChatGPT aide a decrire ; le rendu final passe souvent par un outil image")),
    ("ia-chatgpt-stockage.svg", "Stockage plein", "Liberer ou contourner",
     grid3([
         ("Nettoyer", "Corbeille, doublons"),
         ("Deplacer", "Disque externe"),
         ("Compresser", "Archives"),
         ("Autre compte", "Si autorise"),
         ("Prioriser", "Garder l'essentiel"),
         ("Habitude", "Ranger souvent"),
     ], "Un disque plein, c'est surtout un rangement a faire")),
    ("ia-claude-start.svg", "Demarrer avec Claude", "Ressources gratuites",
     flow_row(["Docs", "Cours", "Essayer", "Skill", "Projet"],
              "Apprendre un peu, tester tout de suite")),
    ("ia-claude-skills.svg", "Skills Claude", "Paquets d'instructions",
     stack_layers([
         ("Skill", "Regles + exemples"),
         ("Choisir", "Selon ta tache"),
         ("Activer", "Dans Claude"),
         ("Iterer", "Ameliore au fil de l'eau"),
     ], "Une skill = un mode d'emploi reutilisable")),
    ("ia-claude-switch.svg", "De ChatGPT a Claude", "Adapter ses habitudes",
     compare2("Garder", ["Bons prompts", "Verifier", "Decouper"],
              "Adapter", ["Ton Claude", "Projects / skills", "Fichiers"],
              "Meme logique : clarite + verification")),
    ("ia-claude-vibe.svg", "Eviter le look IA", "Charte et contraintes",
     flow_row(["Charte", "Exemples", "Contraintes", "Revue humaine"],
              "Sans brief, tout le monde obtient le meme site genérique")),
    ("ia-claude-top.svg", "Choisir une IA", "Selon le besoin",
     grid3([
         ("Ecrire", "Texte, resume"),
         ("Coder", "Aide au code"),
         ("Image", "Visuels"),
         ("Recherche", "Sources"),
         ("Local", "Open source"),
         ("Regle", "Tester 2 outils"),
     ], "Il n'y a pas une IA meilleure pour tout")),
]
for item in SVGS:
    write_svg(*item)

# ---- ChatGPT ----
article(
    "ia-chatgpt-comment-utiliser-chatgpt-5-template-a-suivre-pour-creer-de-meilleur",
    "ChatGPT : un modele de prompt qui marche vraiment",
    "Role, contexte, tache, format, exemple : un canevas simple pour de meilleures reponses.",
    f"""# ChatGPT : un modele de prompt qui marche vraiment

Un bon prompt, ce n'est pas magique. C'est **clair**.

{fig("ia-chatgpt-prompt.svg", "Schema d'un bon prompt", "Role, contexte, tache, format, exemple.")}

## Canevas

1. **Role** : "Tu es…"
2. **Contexte** : pour qui, quel projet
3. **Tache** : ce que tu veux exactement
4. **Format** : liste, tableau, texte court…
5. **Exemple** (optionnel) : un mini modele

Ensuite : [automatiser](/blog/articles/ia-chatgpt-nouveaute-sur-chatgpt-plus-on-peut-maintenant-automatiser-des-taches.html) ce qui se repete.
""",
)

article(
    "ia-chatgpt-comment-creer-un-lut-avec-chatgpt-pour-l-importer-dans-un",
    "LUT video : se faire aider par ChatGPT (puis finir dans un outil)",
    "Decrire un style couleur avec ChatGPT, puis appliquer le rendu dans ton logiciel video.",
    f"""# LUT video : se faire aider par ChatGPT (puis finir dans un outil)

Une **LUT**, c'est une "recette de couleurs" pour une video. ChatGPT peut t'aider a **decrire** le style.

{fig("ia-chatgpt-lut.svg", "Schema creation LUT assistee", "Style, description, outil, import.")}

Demande un style (cinema, chaud, froid…), des valeurs, des etapes. Puis importe dans ton logiciel (DaVinci, Premiere…). Verifie toujours a l'oeil. Suite astuces : [resume YouTube](/blog/articles/ia-chatgpt-astuce-pour-que-chatgpt-resume-des-videos-youtube-en-utilisant-l-url.html).
""",
)

article(
    "ia-chatgpt-astuce-pour-que-chatgpt-resume-des-videos-youtube-en-utilisant-l-url",
    "Resume YouTube : donner le lien a ChatGPT",
    "Gagner du temps sur une video longue : resume + points cles, puis verifier.",
    f"""# Resume YouTube : donner le lien a ChatGPT

Colle l'**URL**, demande un resume court + 5 points cles + pour qui c'est utile.

{fig("ia-chatgpt-youtube.svg", "Schema resume video YouTube", "Lien, demande, resume, points cles, verif.")}

## Astuce

Precise la langue et la longueur. Si la video est critique (sante, argent, droit), **revérifie** les faits. Voir aussi [memoire ChatGPT](/blog/articles/ia-chatgpt-comment-savoir-tout-ce-que-chatgpt-sait-sur-vous-en-accedant-a-sa-mem.html).
""",
)

article(
    "ia-chatgpt-astuce-si-votre-espace-de-stockage-google-est-plein-comment-acceder",
    "Google Drive plein : liberer de la place (sans paniquer)",
    "Nettoyer, deplacer, compresser : un plan simple quand le stockage bloque.",
    f"""# Google Drive plein : liberer de la place (sans paniquer)

Quand c'est plein, Google freine. Le fix, c'est surtout du **rangement**.

{fig("ia-chatgpt-stockage.svg", "Schema liberer stockage", "Nettoyer, deplacer, compresser, prioriser.")}

Vide la corbeille, cherche les gros fichiers, deplace ce qui dort. ChatGPT peut t'aider a faire une checklist — mais c'est toi qui cliques. Reviens aux [prompts utiles](/blog/articles/ia-chatgpt-comment-utiliser-chatgpt-5-template-a-suivre-pour-creer-de-meilleur.html).
""",
)

article(
    "ia-chatgpt-nouveaute-sur-chatgpt-plus-on-peut-maintenant-automatiser-des-taches",
    "ChatGPT : automatiser les taches qui se repetent",
    "Quand c'est toujours la meme demande, industrialise le prompt (et garde un oeil humain).",
    f"""# ChatGPT : automatiser les taches qui se repetent

L'automatisation sert a ne pas retaper 20 fois la meme chose.

{fig("ia-chatgpt-auto.svg", "Schema automatisation ChatGPT", "Idee, prompt fixe, declencheur, resultat, verifier.")}

Garde un **prompt modele**, un declencheur clair, et une verification. Ne automatise pas ce qui demande du jugement delicate. Base : [modele de prompt](/blog/articles/ia-chatgpt-comment-utiliser-chatgpt-5-template-a-suivre-pour-creer-de-meilleur.html).
""",
)

article(
    "ia-chatgpt-comment-savoir-tout-ce-que-chatgpt-sait-sur-vous-en-accedant-a-sa-mem",
    "Memoire ChatGPT : voir (et effacer) ce qu'il retient",
    "Ouvrir les reglages memoire, controler les infos, nettoyer ce qui ne doit plus rester.",
    f"""# Memoire ChatGPT : voir (et effacer) ce qu'il retient

ChatGPT peut **retenir** des infos pour personnaliser. Toi, tu peux les lire et les supprimer.

{fig("ia-chatgpt-memoire.svg", "Schema memoire ChatGPT", "Parametres, lire, verifier, effacer.")}

## En pratique

Parametres → memoire / personalization → parcours les items → supprime le superflu. Moins de donnees sensibles = mieux. Suite : [automatiser sans tout exposer](/blog/articles/ia-chatgpt-nouveaute-sur-chatgpt-plus-on-peut-maintenant-automatiser-des-taches.html).
""",
)

article(
    "ia-chatgpt-astuce-chatgpt-pour-tous-les-gomuscu-et-autres-sportifs-qui-veulent-c",
    "Photo de repas + ChatGPT : une estimation, pas une science exacte",
    "Envoyer une photo pour approximer calories / macros — utile en ordre de grandeur, a verifier.",
    f"""# Photo de repas + ChatGPT : une estimation, pas une science exacte

Tu envoies une **photo** de ton assiette. ChatGPT propose un ordre de grandeur (calories, macros).

{fig("ia-chatgpt-photo.svg", "Schema photo repas ChatGPT", "Utile pour approximer, pas pour certifier.")}

## Important

Ce n'est **pas** un diagnostic ni un plan competition. Pour un suivi precis, pese et utilise une app dediee. Pour mieux formuler tes demandes : [modele de prompt](/blog/articles/ia-chatgpt-comment-utiliser-chatgpt-5-template-a-suivre-pour-creer-de-meilleur.html).
""",
)

# ---- Claude ----
article(
    "ia-claude-ressources-gratuite-pour-apprendre-a-utiliser-claude-code-cours-offic",
    "Claude Code : ressources gratuites pour demarrer",
    "Cours et docs pour apprendre Claude Code sans payer une formation opaque.",
    f"""# Claude Code : ressources gratuites pour demarrer

Tu peux apprendre **Claude Code** avec des ressources officielles / gratuites, puis pratiquer tout de suite.

{fig("ia-claude-start.svg", "Schema demarrage Claude", "Docs, cours, essayer, skill, projet.")}

Lis un peu, ouvre un petit projet, demande de l'aide sur **une** tache claire. Suite : [formation Claude Code](/blog/articles/ia-claude-formation-100-gratuite-pour-apprendre-a-utiliser-claude-code-anthrop.html).
""",
)

article(
    "ia-claude-formation-100-gratuite-pour-apprendre-a-utiliser-claude-code-anthrop",
    "Formation Claude Code gratuite : par ou commencer",
    "Un parcours simple : bases, pratique, puis skills pour aller plus vite.",
    f"""# Formation Claude Code gratuite : par ou commencer

Objectif : etre capable de faire une tache reelle en Claude Code sans te perdre.

{fig("ia-claude-start.svg", "Schema parcours Claude Code", "Docs, cours, essayer, skill, projet.")}

1. Bases de l'outil  
2. Un mini projet perso  
3. Une [skill](/blog/articles/ia-claude-si-vous-utilisez-claude-utilisez-ca-une-skill-c-est-un-ensemble-d-i.html) utile  

Videos : [Anthropic](/blog/articles/ia-claude-ou-trouver-les-videos-officielles-et-gratuites-d-anthropic-pour-appre.html).
""",
)

article(
    "ia-claude-ou-trouver-les-videos-officielles-et-gratuites-d-anthropic-pour-appre",
    "Videos Anthropic gratuites : ou les trouver",
    "Apprendre Claude avec les contenus officiels, sans se perdre dans 40 tutos hasardeux.",
    f"""# Videos Anthropic gratuites : ou les trouver

Commence par les **sources officielles** Anthropic (chaine / docs / cours), puis complete si besoin.

{fig("ia-claude-start.svg", "Schema apprentissage Claude", "Docs et videos, puis pratique.")}

Regarde une video, reproduis immédiatement. Ensuite : [3 ressources](/blog/articles/ia-claude-3-ressources-gratuites-pour-apprendre-a-utiliser-claude-1-anthropic.html).
""",
)

article(
    "ia-claude-si-vous-utilisez-claude-utilisez-ca-une-skill-c-est-un-ensemble-d-i",
    "Skills Claude : des modes d'emploi reutilisables",
    "Une skill = instructions + exemples pour que Claude travaille comme tu veux.",
    f"""# Skills Claude : des modes d'emploi reutilisables

Une **skill**, c'est un paquet de regles : comment Claude doit repondre sur un sujet.

{fig("ia-claude-skills.svg", "Schema skill Claude", "Skill, choisir, activer, iterer.")}

Cree-en une pour ton style d'ecriture, ton code, ou ta checklist. Choisir : [quelle skill](/blog/articles/ia-claude-comment-savoir-quelle-skill-choisir-dans-claude-le-site-c-est-skills.html).
""",
)

article(
    "ia-claude-3-ressources-gratuites-pour-apprendre-a-utiliser-claude-1-anthropic",
    "3 ressources gratuites pour apprendre Claude",
    "Docs, videos, pratique : le trio minimum pour demarrer sans se noyer.",
    f"""# 3 ressources gratuites pour apprendre Claude

1. **Docs** Anthropic  
2. **Videos** officielles  
3. **Pratique** : un vrai petit besoin

{fig("ia-claude-start.svg", "Schema 3 ressources Claude", "Docs, videos, pratique.")}

Sans pratique, tu accumules des onglets. Avec pratique, ca colle. Voir [skills](/blog/articles/ia-claude-si-vous-utilisez-claude-utilisez-ca-une-skill-c-est-un-ensemble-d-i.html).
""",
)

article(
    "ia-claude-comment-savoir-quelle-skill-choisir-dans-claude-le-site-c-est-skills",
    "Choisir une skill Claude : selon ta tache",
    "Ne collectionne pas 50 skills : prends celle qui match ton besoin du jour.",
    f"""# Choisir une skill Claude : selon ta tache

Regarde le **besoin** (ecrire, coder, resume…), pas la mode.

{fig("ia-claude-skills.svg", "Schema choix de skill", "Skill adaptee a la tache.")}

Teste 1 skill, mesure si ca gagne du temps, sinon change. Intro skills : [c'est quoi](/blog/articles/ia-claude-si-vous-utilisez-claude-utilisez-ca-une-skill-c-est-un-ensemble-d-i.html).
""",
)

article(
    "ia-claude-3-astuces-si-vous-venez-de-passer-de-chatgpt-a-claude-et-que-vous-en",
    "Passer de ChatGPT a Claude : 3 reflexes utiles",
    "Garde tes bons reflexes de prompt, adapte le reste a Claude.",
    f"""# Passer de ChatGPT a Claude : 3 reflexes utiles

1. Garde des prompts **clairs**  
2. Decoupe les grosses taches  
3. Verifie toujours le resultat

{fig("ia-claude-switch.svg", "Schema transition ChatGPT vers Claude", "Garder le bon, adapter le reste.")}

Explore projects / skills. Si tu codes avec IA : [eviter le look generique](/blog/articles/ia-claude-astuce-pour-eviter-qu-un-site-vibe-code-ressemble-a-tous-les-autres.html).
""",
)

article(
    "ia-claude-mon-top-des-meilleures-3-ia",
    "Choisir une IA : 3 questions (pas un classement absolu)",
    "Ecrire, coder, chercher : choisis selon le job, pas selon le hype.",
    f"""# Choisir une IA : 3 questions (pas un classement absolu)

Il n'existe pas **une** meilleure IA pour tout.

{fig("ia-claude-top.svg", "Schema choix d'IA selon besoin", "Ecrire, coder, image, recherche…")}

Demande-toi : quel job ? quel budget ? ai-je besoin de sources ? Teste deux outils sur **la meme** tache. Comparer aussi [DeepSeek](/blog/articles/ia-claude-comment-utiliser-l-ia-chinoise-gratuite-et-open-source-deepseek-en-ve.html).
""",
)

article(
    "ia-claude-nouveaux-plugins-claude-pour-la-finance-les-plugins-prennent-5-min",
    "Plugins Claude finance : utiles, mais a verifier",
    "Des extensions pour aller plus vite sur des taches finance — sans remplacer un pro.",
    f"""# Plugins Claude finance : utiles, mais a verifier

Un plugin peut gagner du temps. Il ne remplace pas un **conseil pro** (comptable, banquier).

{fig("ia-claude-skills.svg", "Schema plugin / skill", "Activer, tester, verifier.")}

Installe, teste sur un cas simple, controle les chiffres. Pour le choix d'outil : [quelle IA](/blog/articles/ia-claude-mon-top-des-meilleures-3-ia.html).
""",
)

article(
    "ia-claude-comment-utiliser-l-ia-chinoise-gratuite-et-open-source-deepseek-en-ve",
    "DeepSeek : une IA gratuite / open a tester",
    "Alternative interessante pour coder ou ecrire — avec les memes regles de verification.",
    f"""# DeepSeek : une IA gratuite / open a tester

DeepSeek est une option **gratuite / open** a comparer a ChatGPT ou Claude.

{fig("ia-claude-top.svg", "Schema alternatives IA", "Tester selon le besoin.")}

Teste sur ton usage reel (code, texte). Regarde confidentialite et limites. Retour serie Claude : [demarrer](/blog/articles/ia-claude-ressources-gratuite-pour-apprendre-a-utiliser-claude-code-cours-offic.html).
""",
)

article(
    "ia-claude-clawdbot-ou-moltbot-l-ia-autonome-surpuissante-depuis-quelques-jour",
    "Agents autonomes (type bot) : puissants, a encadrer",
    "Un agent qui enchaine des actions : utile, mais fixe des limites et verifie.",
    f"""# Agents autonomes (type bot) : puissants, a encadrer

Un agent "autonome" peut enchainer des etapes. C'est pratique — et risqué si tu ne cadres rien.

{fig("ia-claude-auto.svg" if False else "ia-chatgpt-auto.svg", "Schema agent autonome", "Idee, etapes, resultat, verifier.")}

Donne un perimetre, des droits limites, et une revue humaine. Proche : [automatiser ChatGPT](/blog/articles/ia-chatgpt-nouveaute-sur-chatgpt-plus-on-peut-maintenant-automatiser-des-taches.html).
""",
)

article(
    "ia-claude-astuce-pour-eviter-qu-un-site-vibe-code-ressemble-a-tous-les-autres",
    "Vibe coding : eviter le site qui ressemble a tous les autres",
    "Charte, exemples, contraintes : sans brief, l'IA sort le meme design generique.",
    f"""# Vibe coding : eviter le site qui ressemble a tous les autres

Sans brief, l'IA recycle les memes idees (couleurs, layout, texte).

{fig("ia-claude-vibe.svg", "Schema anti-generique", "Charte, exemples, contraintes, revue.")}

Donne une **charte**, 2-3 references, des interdits ("pas de violet", "pas de hero carte"). Puis relis en humain. Transition outils : [ChatGPT → Claude](/blog/articles/ia-claude-3-astuces-si-vous-venez-de-passer-de-chatgpt-a-claude-et-que-vous-en.html).
""",
)

# Fix the hacky fig for clawdbot - rewrite that article cleanly
article(
    "ia-claude-clawdbot-ou-moltbot-l-ia-autonome-surpuissante-depuis-quelques-jour",
    "Agents autonomes (type bot) : puissants, a encadrer",
    "Un agent qui enchaine des actions : utile, mais fixe des limites et verifie.",
    f"""# Agents autonomes (type bot) : puissants, a encadrer

Un agent "autonome" peut enchainer des etapes. C'est pratique — et risque si tu ne cadres rien.

{fig("ia-chatgpt-auto.svg", "Schema agent autonome", "Idee, etapes, resultat, verifier.")}

Donne un perimetre, des droits limites, et une revue humaine. Proche : [automatiser ChatGPT](/blog/articles/ia-chatgpt-nouveaute-sur-chatgpt-plus-on-peut-maintenant-automatiser-des-taches.html).
""",
)

for name, title, desc in (
    (
        "ia-chatgpt-serie.json",
        "Serie IA — ChatGPT (astuces simples)",
        "Prompts, memoire, resumes et automatisations ChatGPT expliques clairement.",
    ),
    (
        "ia-claude-serie.json",
        "Serie IA — Claude (demarrer sans se perdre)",
        "Claude, skills, ressources Anthropic et bons reflexes, en langage simple.",
    ),
):
    path = COLLECTIONS / name
    col = json.loads(path.read_text(encoding="utf-8"))
    col["title"] = title
    col["description"] = desc
    path.write_text(json.dumps(col, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"[OK] {name}")

print("done")
