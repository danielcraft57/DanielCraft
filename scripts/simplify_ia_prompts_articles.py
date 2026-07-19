#!/usr/bin/env python3
"""Simplifie serie IA Prompts : titres courts, corps debutant, schemas."""
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
    ("ia-prompts-base.svg", "Mieux prompter", "Methode simple",
     flow_row(["But", "Contexte", "Contraintes", "Format", "Relance"],
              "Un prompt clair bat dix reformulations vagues")),
    ("ia-prompts-humaniser.svg", "Humaniser un texte", "Moins robot",
     compare2("Robot", ["Trop parfait", "Repetitif", "Sans voix"],
              "Humain", ["Asperites", "Exemples concrets", "Ton clair"],
              "On garde le fond, on assouplit la forme")),
    ("ia-prompts-perso.svg", "Personnage coherent", "Meme look",
     stack_layers([
         ("Fiche perso", "Traits fixes"),
         ("Prompt seed", "Description stable"),
         ("Reference", "Image / notes"),
         ("Serie", "Reutiliser la fiche"),
     ], "La coherence vient d'une fiche, pas du hasard")),
    ("ia-prompts-video.svg", "Meilleure video IA", "Prompt + references",
     flow_row(["Idee", "Prompt detaille", "Reference", "Generer", "Couper"],
              "Le detail et les references font 80% du rendu")),
    ("ia-prompts-logo.svg", "Logo avec l'IA", "Brief puis choix",
     flow_row(["Brief", "Variantes", "Choisir", "Vectoriser", "Charte"],
              "L'IA propose ; toi tu selectionnes et tu peaufines")),
    ("ia-prompts-reseaux.svg", "Contenu reseaux", "Idee a post",
     flow_row(["Sujet", "Angle", "Format", "CTA", "Calendrier"],
              "Un angle clair > dix posts vides")),
    ("ia-prompts-geo.svg", "Apparaitre dans ChatGPT", "Etre cite",
     grid3([
         ("Pages claires", "Reponses utiles"),
         ("Preuves", "Sources / avis"),
         ("Structure", "Titres nets"),
         ("Mentions", "Ailleurs en ligne"),
         ("Maj", "Contenu a jour"),
         ("Mesure", "Tester les prompts"),
     ], "Proche du GEO : etre compréhensible et digne de confiance")),
    ("ia-prompts-ressources.svg", "Ressources prompts", "Apprendre vite",
     grid3([
         ("Exemples", "Prompts modeles"),
         ("Guides", "Methodes"),
         ("Outils", "Aides UI"),
         ("Pratique", "Tes cas reels"),
         ("Partage", "Communautes"),
         ("Critique", "Verifier toujours"),
     ], "Collectionne peu, pratique beaucoup")),
]
for item in SVGS:
    write_svg(*item)

article(
    "ia-prompts-4-ressources-ia-gratuites-pour-vous-former-et-mieux-comprendre-l-inte",
    "4 ressources gratuites pour mieux parler aux IA",
    "Exemples, guides et pratique : un mini kit pour progresser sans se noyer.",
    f"""# 4 ressources gratuites pour mieux parler aux IA

Tu n'as pas besoin de 200 onglets. Quatre types de ressources suffisent.

{fig("ia-prompts-ressources.svg", "Schema ressources prompts", "Exemples, guides, outils, pratique.")}

1. **Exemples** de prompts  
2. **Guides** methodes  
3. **Outils** qui aident a structurer  
4. **Ta pratique** sur un vrai besoin  

Ensuite : [meilleurs prompts](/blog/articles/ia-prompts-comment-creer-de-meilleurs-prompt-sur-chatgpt-site-gratuit.html).
""",
)

article(
    "ia-prompts-comment-creer-un-logo-gratuit-avec-l-ia",
    "Logo gratuit avec l'IA : brief, variantes, choix",
    "Demander des pistes visuelles, selectionner, puis peaufiner (idealement en vectoriel).",
    f"""# Logo gratuit avec l'IA : brief, variantes, choix

L'IA est bonne pour **explorer**. Toi, tu decides.

{fig("ia-prompts-logo.svg", "Schema creation logo IA", "Brief, variantes, choisir, vectoriser, charte.")}

Donne metier, ton, couleurs a eviter, 3 mots cles. Genere des variantes, garde 1-2, vectorise si besoin. Suite charte : [identite visuelle](/blog/articles/communication-identite-visuelle-charte.html).
""",
)

article(
    "ia-prompts-comment-generer-un-personnage-coherent-avec-chatgpt-si-vou",
    "Personnage IA coherent : une fiche avant les images",
    "Fixer age, style, details, puis reutiliser la meme description a chaque generation.",
    f"""# Personnage IA coherent : une fiche avant les images

Sans fiche, chaque image est un cousin eloigne.

{fig("ia-prompts-perso.svg", "Schema personnage coherent", "Fiche, seed, reference, serie.")}

Ecris une **fiche** (look, vetements, ambiance). Recolle-la a chaque prompt. Garde une image de reference. Voir aussi [meme perso en video](/blog/articles/ia-prompts-comment-garder-le-meme-personnage-dans-des-videos-ia-pour.html).
""",
)

article(
    "ia-prompts-comment-humaniser-un-texte-redige-par-l-intelligence-artif",
    "Humaniser un texte IA : garder le fond, assouplir la forme",
    "Couper le trop parfait, ajouter exemples et ton — sans perdre le message.",
    f"""# Humaniser un texte IA : garder le fond, assouplir la forme

Un texte "trop IA" sonne lisse et vide. On le **rend vivant**.

{fig("ia-prompts-humaniser.svg", "Schema humaniser texte IA", "Moins robot, plus humain.")}

Demande : phrases plus courtes, un exemple concret, moins d'adverbes. Relis a voix haute. Base prompts : [methode](/blog/articles/ia-prompts-comment-creer-de-meilleurs-prompt-sur-chatgpt-site-gratuit.html).
""",
)

article(
    "ia-prompts-comment-generer-des-videos-ia-de-meilleure-qualite-en-utilisant-un-pr",
    "Videos IA plus nettes : detaille ton prompt",
    "Sujet, plan, lumiere, mouvement, style : plus tu precises, moins c'est flou.",
    f"""# Videos IA plus nettes : detaille ton prompt

Une video floue vient souvent d'un prompt **vague**.

{fig("ia-prompts-video.svg", "Schema prompt video IA", "Idee, prompt, reference, generer, couper.")}

Precise le plan (gros plan / large), la lumiere, le mouvement, ce qu'il ne faut **pas**. Puis coupe les essais ratés. Perso stable : [personnage coherent](/blog/articles/ia-prompts-comment-generer-un-personnage-coherent-avec-chatgpt-si-vou.html).
""",
)

article(
    "ia-prompts-comment-creer-de-meilleurs-prompt-sur-chatgpt-site-gratuit",
    "Meilleurs prompts : methode + quelques aides gratuites",
    "Role, contexte, objectif, format — puis des sites d'exemples si tu bloques.",
    f"""# Meilleurs prompts : methode + quelques aides gratuites

Avant les sites d'exemples : une **methode**.

{fig("ia-prompts-base.svg", "Schema methode prompt", "But, contexte, contraintes, format, relance.")}

1. But  
2. Contexte  
3. Contraintes  
4. Format de sortie  
5. Relance ("ameliore X")  

Les bibliotheques de prompts aident a demarrer, pas a penser a ta place. Cousin ChatGPT : [modele de prompt](/blog/articles/ia-chatgpt-comment-utiliser-chatgpt-5-template-a-suivre-pour-creer-de-meilleur.html).
""",
)

article(
    "ia-prompts-comment-creer-du-contenu-sur-les-reseau",
    "Contenu reseaux avec l'IA : un angle, pas du remplissage",
    "Idee, angle, format, appel a l'action — l'IA aide a rediger, toi tu choisis le sujet.",
    f"""# Contenu reseaux avec l'IA : un angle, pas du remplissage

L'IA ecrit vite. Sans angle, ca fait du bruit.

{fig("ia-prompts-reseaux.svg", "Schema contenu reseaux", "Sujet, angle, format, CTA, calendrier.")}

Donne ton public et **une** promesse par post. Demande 3 variantes, garde la plus claire. Voir [marketing reseaux](/blog/articles/marketing-reseaux-sociaux-strategie.html).
""",
)

article(
    "ia-prompts-astuce-prompt-chatgpt-gratuit-pour-clarifie",
    "Astuce : demander a ChatGPT de clarifier (avant d'agir)",
    "Fais reformuler ton besoin en 5 puces — tu gagnes du temps sur la suite.",
    f"""# Astuce : demander a ChatGPT de clarifier (avant d'agir)

Avant une longue reponse : "Reformule mon besoin en 5 puces et pose 3 questions."

{fig("ia-prompts-base.svg", "Schema clarification prompt", "Clarifier avant de generer.")}

Tu corriges les malentendus **tot**. Puis tu lances la vraie tache. Methode complete : [meilleurs prompts](/blog/articles/ia-prompts-comment-creer-de-meilleurs-prompt-sur-chatgpt-site-gratuit.html).
""",
)

article(
    "ia-prompts-cette-etudiante-a-cree-une-extension-qui-detecte-en-direct-les-menson",
    "Detecter les erreurs d'une IA : garder l'esprit critique",
    "Outils et reflexes pour repérer approximations et inventions — surtout sur les sujets sensibles.",
    f"""# Detecter les erreurs d'une IA : garder l'esprit critique

Les IA peuvent **inventer**. Un outil d'aide, ca n'enleve pas ta verification.

{fig("ia-prompts-humaniser.svg", "Schema esprit critique IA", "Lire, verifier, garder le doute utile.")}

Sur sante, argent, droit : croise les sources. Demande des citations, puis controle. GEO / confiance : [apparaitre dans ChatGPT](/blog/articles/ia-prompts-comment-apparaitre-dans-les-reponses-de-chatgpt-tutoriel-rapide-pou.html).
""",
)

article(
    "ia-prompts-comment-garder-le-meme-personnage-dans-des-videos-ia-pour",
    "Meme personnage en video IA : fiche + references",
    "Reutiliser description et images de reference pour limiter les mutations de visage.",
    f"""# Meme personnage en video IA : fiche + references

La video IA "change de tete" si tu ne verrouilles rien.

{fig("ia-prompts-perso.svg", "Schema personnage video coherent", "Fiche et references stables.")}

Meme fiche textuelle, memes references image, meme style. Accepte quelques essais. Base : [personnage coherent](/blog/articles/ia-prompts-comment-generer-un-personnage-coherent-avec-chatgpt-si-vou.html).
""",
)

article(
    "ia-prompts-comment-apparaitre-dans-les-reponses-de-chatgpt-tutoriel-rapide-pou",
    "Apparaitre dans les reponses ChatGPT : etre clair et digne de confiance",
    "Pages utiles, preuves, mentions ailleurs : les bases pour etre cite par une IA.",
    f"""# Apparaitre dans les reponses ChatGPT : etre clair et digne de confiance

Les IA citent ce qu'elles comprennent et jugent fiable.

{fig("ia-prompts-geo.svg", "Schema etre cite par une IA", "Clarte, preuves, structure, mentions.")}

Ecris des reponses nettes, montre des preuves, sois mentionne ailleurs. C'est le coeur du [GEO](/blog/articles/geo-nouveau-seo-ia-guide-complet.html).
""",
)

article(
    "ia-prompts-comment-acceder-et-utiliser-reve",
    "Reve (outil IA) : acceder et tester sans se perdre",
    "Trouver l'acces, faire un premier essai simple, puis voir si ca colle a ton usage.",
    f"""# Reve (outil IA) : acceder et tester sans se perdre

Un nouvel outil IA se teste en **petit** : une tache, un critere de succes.

{fig("ia-prompts-ressources.svg", "Schema tester un outil IA", "Acceder, essayer, juger.")}

Cree un compte / acces, lance un cas simple, compare a ce que tu as deja ([ChatGPT](/blog/articles/ia-chatgpt-comment-utiliser-chatgpt-5-template-a-suivre-pour-creer-de-meilleur.html), [Claude](/blog/articles/ia-claude-ressources-gratuite-pour-apprendre-a-utiliser-claude-code-cours-offic.html)).
""",
)

path = COLLECTIONS / "ia-prompts-serie.json"
col = json.loads(path.read_text(encoding="utf-8"))
col["title"] = "Serie IA — Prompts (parler clairement aux modeles)"
col["description"] = (
    "Methodes de prompting, humaniser un texte, personnages coherents et contenu reseaux — en langage simple."
)
path.write_text(json.dumps(col, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("[OK] ia-prompts-serie.json")
print("done")
