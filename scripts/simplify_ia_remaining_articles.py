#!/usr/bin/env python3
"""Simplifie IA images, nocode, cours, metiers, productivite."""
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


for item in [
    ("ia-images-gen.svg", "Generer une image", "Brief clair",
     flow_row(["Idee", "Prompt", "Style", "Generer", "Choisir"], "Un bon brief bat dix essais au hasard")),
    ("ia-images-money.svg", "Monetiser le visuel", "Offre nette",
     grid3([("Offre", "Service clair"), ("Preuve", "Avant/apres"), ("Canal", "Ou vendre"),
            ("Prix", "Simple"), ("Livrable", "Fichiers nets"), ("Limite", "Ethique")],
           "Vendre un resultat, pas juste un outil")),
    ("ia-nocode-flow.svg", "No-code + IA", "Blocs et flux",
     flow_row(["Besoin", "Outil", "Template", "Tester", "Publier"], "Pars d'un besoin reel")),
    ("ia-cours-learn.svg", "Apprendre l'IA", "Cours + pratique",
     stack_layers([("Choisir", "1 parcours"), ("Suivre", "Modules"), ("Pratiquer", "Mini projet"), ("Prouver", "CV / portfolio")],
                  "Finir un parcours > ouvrir dix onglets")),
    ("ia-metiers-work.svg", "IA et metiers", "Adapter ses competences",
     compare2("Peur", ["Remplacement total", "Attendre"], "Action", ["Apprendre", "Tester sur le job"],
              "Ceux qui pratiquent gardent une longueur d'avance")),
    ("ia-prod-daily.svg", "IA au quotidien", "Gagner du temps",
     flow_row(["Tache", "Prompt", "Brouillon", "Verifier", "Livrer"], "L'IA accelere ; toi tu valides")),
]:
    write_svg(*item)

ARTICLES_DATA = [
    # images
    ("ia-images-tutoriel-kling-ai-motion-control-comment-utiliser-l-ia-pour-se-trans",
     "Kling Motion Control : animer un personnage simplement",
     "Controller un mouvement video avec l'IA : brief, reference, essais.",
     "ia-images-gen.svg", "Schema motion control", "Idee, prompt, style, generer.",
     "Precise le mouvement voulu. Fais 2-3 essais. Coupe le meilleur. Voir aussi [personnage coherent](/blog/articles/ia-prompts-comment-generer-un-personnage-coherent-avec-chatgpt-si-vou.html)."),
    ("ia-images-3-facons-de-gagner-de-l-argent-grace-a-l-ia-avec-ces-methodes-je-gagn",
     "Gagner de l'argent avec l'image IA : 3 pistes realistes",
     "Services, templates, formation : moneter un savoir-faire, pas magie.",
     "ia-images-money.svg", "Schema monetisation image", "Offre, preuve, canal.",
     "Choisis **une** offre (ex. miniatures YouTube). Montre avant/apres. Prix clair."),
    ("ia-images-comment-creer-un-clone-dans-une-video-grace-a-l-ia-chinois",
     "Clone video avec l'IA : possible, a utiliser avec ethique",
     "Dupliquer une personne a l'ecran : technique fun, responsabilite importante.",
     "ia-images-gen.svg", "Schema clone video", "Reference et generation.",
     "Demande toujours le consentement. Ne trompe pas. Usage pro : charte claire."),
    ("ia-images-comment-creer-le-mock-up-d-une-application-ou-d-un-site-we",
     "Mock-up app/site avec l'IA : visualiser vite",
     "Decrire ecrans et style pour obtenir une maquette a discuter.",
     "ia-images-gen.svg", "Schema mock-up IA", "Brief ecran puis variantes.",
     "Donne device, pages, couleurs. Garde 2 variantes. Peaufine ensuite."),
    ("ia-images-deepseek-ocr-c-est-une-nouvelle-methode-qui-permet-de-compresser-du",
     "OCR et compression : lire du texte dans les images",
     "Extraire du texte d'une image / PDF scanne pour le reutiliser.",
     "ia-images-gen.svg", "Schema OCR", "Image vers texte.",
     "Utile pour archives. Verifie les erreurs de lecture. Suite outils : [alternatives](/blog/articles/ia-outils-une-ia-comme-chatgpt-mais-gratuite-huggingchat-d.html)."),
    ("ia-images-nouvelle-ia-pour-creer-des-graphiques-animes-et-animations-visuelles",
     "Graphiques animes avec l'IA : pour expliquer plus vite",
     "Transformer une idee ou des chiffres en animation simple et claire.",
     "ia-images-gen.svg", "Schema graphiques animes", "Donnees vers visuel.",
     "Donne les chiffres + message. Evite le trop charge. Export et relis."),
    ("ia-images-comment-acceder-aux-5-ia-secretes-de-whatsapp-merci-jolan-ai-d-avoi",
     "IA dans WhatsApp : acces et limites",
     "Certaines IA s'utilisent via messagerie : pratique, mais regarde confidentialite.",
     "ia-images-gen.svg", "Schema IA messagerie", "Acces rapide, prudence donnees.",
     "Ne colle pas de secrets. Prefere un compte dedie. Compare a [Gemini](/blog/articles/ia-gemini-comment-utiliser-gemini-l-intelligence-artificielle-de-goo.html)."),
    ("ia-images-dites-moi-si-vous-voulez-que-je-fasse-un-tut",
     "Tutoriel image IA : par ou commencer",
     "Un parcours simple pour ton premier rendu propre.",
     "ia-images-gen.svg", "Schema premier tutoriel image", "Etapes debutant.",
     "1 sujet, 1 style, 1 outil. Documente ton prompt gagnant. [Meilleurs prompts](/blog/articles/ia-prompts-comment-creer-de-meilleurs-prompt-sur-chatgpt-site-gratuit.html)."),
    ("ia-images-comment-utiliser-nano-banana-pro-la-meilleure-plateforme-la-nouvell",
     "Plateforme image IA : comment la juger vite",
     "Teste qualite, prix, controle du style — sur TON type d'image.",
     "ia-images-gen.svg", "Schema comparer plateformes image", "Meme brief, deux outils.",
     "Lance le meme prompt partout. Garde celui qui respecte le mieux le brief."),
    ("ia-images-la-chine-continue-de-nous-impressionner-pendant-que-les-etats-unis-re",
     "Outils image Chine vs USA : comparer sans hype",
     "Regarde rendu, prix, conditions d'usage — pas seulement les annonces.",
     "ia-images-money.svg", "Schema comparaison outils", "Juger sur le rendu.",
     "Teste 2 outils. Lis confidentialite. Choisis selon ton usage pro."),
    ("ia-images-une-ia-francaise-avec-toutes-les-fonctionnalites",
     "IA image francaise : pourquoi ca peut compter",
     "Hebergement, langue, support : des criteres utiles selon ton contexte.",
     "ia-images-gen.svg", "Schema choix outil FR", "Critères locaux.",
     "Si donnees sensibles : regarde ou ca tourne. Sinon, juge surtout la qualite."),
    ("ia-images-cette-ia-gratuite-remplace-photoshop-googleai-studio-avec-gemini-2",
     "Retouche image gratuite (style Studio) : ce que ca remplace vraiment",
     "Utile pour retouches simples ; Photoshop reste pour le travail pro complexe.",
     "ia-images-gen.svg", "Schema retouche IA", "Simple vs pro.",
     "Essaye detourage, fond, texte. Pour print pro : verifie resolution."),
    # nocode
    ("ia-nocode-test-de-thoreo-une-ia-qui-resume-les-videos",
     "Resumer des videos avec l'IA : gagner du temps",
     "Outil de resume video : utile en veille, a verifier sur le fond.",
     "ia-nocode-flow.svg", "Schema resume video", "Video vers points cles.",
     "Demande resume + actions. Verifie les faits. Cousin : [YouTube ChatGPT](/blog/articles/ia-chatgpt-astuce-pour-que-chatgpt-resume-des-videos-youtube-en-utilisant-l-url.html)."),
    ("ia-nocode-comment-installer-n8n-gratuitement-pour-creer-vos-automati",
     "Installer n8n gratuitement : premier flux",
     "Automation visuelle : installer, importer un template, tester un cas simple.",
     "ia-nocode-flow.svg", "Schema n8n", "Besoin, template, tester.",
     "Vise un flux utile (email, formulaire). Puis ajoute l'IA. [Stack base+n8n](/blog/articles/ia-outils-base-de-donnees-gratuite-avec-des-templates-n8n-et-des-tutoriels-pour.html)."),
    ("ia-nocode-templates-n8n-gratuites-pour-creer-des-agents-ia-comment-y-acceder",
     "Templates n8n pour agents : ou les trouver",
     "Partir d'un modele existant accelere — adapte-le a ton cas.",
     "ia-nocode-flow.svg", "Schema templates agents", "Choisir et adapter.",
     "Importe, lis chaque noeud, teste. Agents : [debutant](/blog/articles/ia-agents-tutoriel-debutant-comment-creer-un-agent-ia-en-quelques-minutes.html)."),
    ("ia-nocode-comment-passer-un-appel-video-chat",
     "Appel video avec une IA : a quoi ca sert",
     "Discuter en live avec un assistant : pratique pour oral / coaching, a cadrer.",
     "ia-nocode-flow.svg", "Schema appel video IA", "Conversation guidee.",
     "Prepare un objectif. Note les actions. Ne partage pas d'infos sensibles."),
    ("ia-nocode-comment-apparaitre-dans-les-resultats-de-chatgpt-tutoriel-avec-2-me",
     "Apparaitre dans ChatGPT : 2 methodes simples",
     "Contenu clair + mentions ailleurs : bases pour etre cite.",
     "ia-nocode-flow.svg", "Schema etre cite", "Clarte et preuves.",
     "Aligne avec le [GEO](/blog/articles/geo-nouveau-seo-ia-guide-complet.html) et [prompts GEO](/blog/articles/ia-prompts-comment-apparaitre-dans-les-reponses-de-chatgpt-tutoriel-rapide-pou.html)."),
    ("ia-nocode-comment-creer-un-avatar-hyper-realiste-et-poster-des-video",
     "Avatar realiste + videos : pipeline simple",
     "Creer un visage coherent puis publier des videos courtes — avec ethique.",
     "ia-images-gen.svg", "Schema avatar video", "Visage, video, publier.",
     "Fiche personnage stable. Consentement si c'est une vraie personne. [Perso coherent](/blog/articles/ia-prompts-comment-generer-un-personnage-coherent-avec-chatgpt-si-vou.html)."),
    ("ia-nocode-comment-payer-moins-cher-les-abonnements-a-des-outils-d-intelligence",
     "Payer moins cher les abonnements IA : pistes",
     "Essais, partages d'equipe, open source : reduire la facture sans se perdre.",
     "ia-nocode-flow.svg", "Schema budget outils IA", "Comparer et couper.",
     "Liste tes outils. Coupe les doublons. Teste [alternatives gratuites](/blog/articles/ia-outils-une-ia-comme-chatgpt-mais-gratuite-huggingchat-d.html)."),
    ("ia-nocode-2-facons-de-gagner-de-l-argent-grace-a-l-intellige",
     "2 facons de moneter l'IA (sans mirage)",
     "Service a un client, ou produit repete (template / formation).",
     "ia-images-money.svg", "Schema monetisation IA", "Service ou produit.",
     "Choisis un probleme precis. Livre un resultat. Evite les promesses miracles."),
    ("ia-nocode-gamma-ai-meilleure-ia-gratuite-pour-creer-des-presentations-powerpo",
     "Gamma : presentations IA rapides",
     "Generer une trame de slides, puis simplifier le message.",
     "ia-nocode-flow.svg", "Schema Gamma slides", "Plan puis design.",
     "Demande un plan court. Enleve le superflu. Cousin : [agent slides](/blog/articles/ia-agents-agent-ia-pour-creer-des-presentations-style-powerpoint-en-utilisant-d.html)."),
    ("ia-nocode-templates-100-gratuites-pour-creer-des-automatisations-et-agents-ia",
     "100 templates d'automation : comment choisir",
     "Ne telecharge pas tout : prends 1 template proche de ton besoin.",
     "ia-nocode-flow.svg", "Schema choisir template", "Filtrer puis adapter.",
     "Cherche ton cas (CRM, email, contenu). Adapte. Documente."),
]

# helper to emit short body
def emit(slug, title, excerpt, svg, alt, cap, more):
    article(slug, title, excerpt, f"""# {title}

{more.split('.')[0]}.

{fig(svg, alt, cap)}

{more}
""")


for row in ARTICLES_DATA:
    emit(*row)

# --- cours / metiers / prod via compact table ---
COURS = [
    ("ia-cours-meilleurs-cours-pour-apprendre-l-ia-gratuit-voici-les-meilleurs-cou",
     "Meilleurs cours IA gratuits : comment choisir",
     "Comparer parcours selon ton niveau et ton objectif, puis en finir un."),
    ("ia-cours-le-futur-du-travail-avec-l-intelligence-artificielle-plus-d-opportu",
     "Futur du travail et IA : opportunites concretes",
     "Ce qui change deja : competences a renforcer, pas seulement peur."),
    ("ia-cours-comment-cloner-le-cerveau-de-n-importe-quel-createur-en-5-minutes-et",
     "Cloner le style d'un createur : methode rapide",
     "Extraire ton, structure et exemples pour reproduire un style (ethiquement)."),
    ("ia-cours-guide-gratuit-par-microsoft-pour-apprendre-a-creer-des-agents-ia-pour",
     "Guide Microsoft agents IA : par ou commencer",
     "Parcours gratuit pour comprendre agents et automatisations."),
    ("ia-cours-5-predictions-sur-le-futur-de-l-ia-et-de-l-humanite-selon-sam-altman",
     "Predictions IA : lire sans tout croire",
     "Des visions utiles pour reflechir — pas des garanties."),
    ("ia-cours-3-facons-d-utiliser-l-ia-notebook-lm-de-g",
     "3 facons d'utiliser NotebookLM",
     "Sources, questions, audio : tirer parti de tes documents."),
    ("ia-cours-nouveaute-avec-la-meilleure-ia-gratuite-pour-apprendre-plus-vite-et-m",
     "Apprendre plus vite avec une IA gratuite",
     "Quiz, resumes, reformulations : un rituel simple de revision."),
    ("ia-cours-comment-utiliser-chatgpt-pour-les-debutants-en-4-etapes-si",
     "ChatGPT debutant : 4 etapes",
     "Compte, prompt clair, exemple, verification."),
    ("ia-cours-alternative-gratuite-5-requetes-par-jour-si-vous-voulez-tester-l-ag",
     "Tester un agent gratuit (quota limite)",
     "5 requetes par jour : assez pour juger si ca vaut le coup."),
    ("ia-cours-plein-de-formations-gratuites-a-l-intelligence-artificielle-sur-le-si",
     "Plein de formations IA gratuites : ne pas se noyer",
     "Filtrer 2 parcours max, calendariser, pratiquer."),
    ("ia-cours-formation-ia-gratuite-pour-apprendre-a-coder-la-formation-dure-17h",
     "Formation coder avec l'IA (parcours long)",
     "17h : decouper en sessions, projets mini, notes."),
]
for slug, title, excerpt in COURS:
    article(slug, title, excerpt, f"""# {title}

{excerpt}

{fig("ia-cours-learn.svg", "Schema apprentissage IA", "Choisir, suivre, pratiquer, prouver.")}

Pratique sur un mini projet cette semaine. Suite Google : [Skills](/blog/articles/ia-gemini-alerte-formations-ia-gratuites-par-google-avec-google-skills-il-y-a-p.html).
""")

METIERS = [
    ("ia-metiers-l-ia-pourra-t-elle-remplacer-les-acteurs-demo-de-dream-actor-m1-ge",
     "IA et acteurs : remplacement ou outil",
     "La tech avance ; le casting et l'ethique restent humains."),
    ("ia-metiers-voici-la-liste-des-metiers-avec-la-croissance-la-plus-rapide-en-2026",
     "Metiers en croissance 2026 : lire une liste utilement",
     "Une tendance n'est pas une promesse d'emploi — croise avec ton territoire."),
    ("ia-metiers-etude-secrete-sur-reddit-par-l-universite-de-zurich-l-intelligence",
     "Etudes IA sur les reseaux : garder l'esprit critique",
     "Methodes, biais, titres choc : lire au-dela du buzz."),
    ("ia-metiers-singularite-technologique-bientot-sam-altman-et-l-hypothese-de-la",
     "Singularite : hypothese, pas calendrier",
     "Debats sur le futur lointain — utile pour reflechir, pas pour paniquer."),
    ("ia-metiers-l-intelligence-artificielle-est-elle-vraim",
     "L'IA est-elle intelligente : ce que ca veut dire",
     "Fort sur motifs ; fragile sur le jugement et le monde reel."),
    ("ia-metiers-chatgpt-est-deja-meilleur-que-certains-medecins-lorsqu-il-s-agit-de-f",
     "IA et medecine : aide, pas remplacement",
     "Peut aider a formuler ; un pro valide le diagnostic et le soin."),
    ("ia-metiers-ils-ont-pourri-le-cerveau-des-ia-le-papier-de-recherche-llm-can-ge",
     "Quand on pollue les modeles : pourquoi ca compte",
     "Donnees de mauvaise qualite = reponses plus foireuses."),
    ("ia-metiers-skild-brain-le-robot-qui-ne-s-arrete-jamais-cree-par-l-entreprise-s",
     "Robots au travail : ce qui change vraiment",
     "Automatiser des gestes repetes ; l'humain garde exceptions et sens."),
    ("ia-metiers-genie-3-l-ia-de-google-capable-de-creer-des-mondes-3d-interactifs-e",
     "Mondes 3D generes : promesse et limites",
     "Impressionnant en demo ; le pipeline prod reste exigeant."),
    ("ia-metiers-on-va-bientot-pouvoir-passer-des-appels-video-avec-chatgpt-je-su",
     "Appels video avec ChatGPT : nouveau canal",
     "Oral + IA : pratique pour brainstorm, a cadrer pour le sensible."),
]
for slug, title, excerpt in METIERS:
    article(slug, title, excerpt, f"""# {title}

{excerpt}

{fig("ia-metiers-work.svg", "Schema IA et metiers", "Peur versus action.")}

Adapte une tache de ton job cette semaine avec l'IA. Formations : [cours gratuits](/blog/articles/ia-cours-meilleurs-cours-pour-apprendre-l-ia-gratuit-voici-les-meilleurs-cou.html).
""")

PROD = [
    ("ia-prod-une-etude-montre-que-les-publicites-creees-entierement-par-l-ia-augme",
     "Pubs 100% IA : ce que dit une etude (avec prudence)",
     "Des gains possibles ; marque, preuve et conformite restent a toi."),
    ("ia-prod-il-y-a-un-probleme-avec-cette-video-ce-time-lapse-d-un-dessin-est-f",
     "Spotter une video IA foireuse : indices simples",
     "Incoherences, mains, texte : apprendre a douter utilement."),
    ("ia-prod-la-premiere-intelligence-artificielle-capable-de-reproduire-le-monde",
     "Reproduire le monde en IA : demos vs realite",
     "Les annonces impressionnent ; le quotidien produit est plus terre-a-terre."),
    ("ia-prod-les-experts-en-ia-vs-les-personnes-qui-s",
     "Experts IA vs pratiquants : qui avance vraiment",
     "La pratique reguliere bat souvent le titre d'expert sur LinkedIn."),
    ("ia-prod-demo-kling-motion-control-et-encore-j-ai-pas-pris-le-temps-de-chan",
     "Demo Kling : tester sans tout abandonner",
     "Bloque 30 minutes, un essai, une note — puis decide."),
]
for slug, title, excerpt in PROD:
    article(slug, title, excerpt, f"""# {title}

{excerpt}

{fig("ia-prod-daily.svg", "Schema productivite IA", "Tache, brouillon, verifier.")}

Garde une checklist. Verifie toujours avant de publier.
""")

for name, title, desc in (
    ("ia-images-serie.json", "Serie IA — Images et visuels (simples)", "Generer, retoucher et moneter des images avec l'IA, sans jargon."),
    ("ia-nocode-serie.json", "Serie IA — No-code et apps (pratiques)", "n8n, templates, presentations et moneter sans usine a gaz."),
    ("ia-formations-serie.json", "Serie IA — Formations (parcours clairs)", "Cours gratuits, NotebookLM, agents : apprendre en pratiquant."),
    ("ia-metiers-serie.json", "Serie IA — Metiers et futur (avec nuance)", "Impact sur le travail : lire, relativiser, agir."),
    ("ia-productivite-serie.json", "Serie IA — Productivite (quotidien)", "Gagner du temps avec l'IA sans perdre le sens critique."),
):
    path = COLLECTIONS / name
    col = json.loads(path.read_text(encoding="utf-8"))
    col["title"] = title
    col["description"] = desc
    path.write_text(json.dumps(col, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"[OK] {name}")

print("done")
