#!/usr/bin/env python3
"""Simplifie Marketing + Communication : titres, corps, schemas. Sans bannieres."""
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
    ("mkt-strategie.svg", "Strategie marketing", "Objectifs, cibles, canaux",
     flow_row(["Objectif", "Cible", "Message", "Canaux", "Mesure"],
              "Sans objectif clair, chaque canal est du bruit")),
    ("mkt-reseaux.svg", "Reseaux sociaux", "Etre utile, pas partout",
     grid3([
         ("Choisir 1-2", "Pas tous les reseaux"),
         ("Rythme", "Regulier et tenable"),
         ("Valeur", "Aider avant de vendre"),
         ("Ecouter", "Commentaires / DM"),
         ("Preuves", "Avis, cas clients"),
         ("Mesurer", "Clics utiles"),
     ], "Mieux vaut un reseau bien tenu que cinq abandonnes")),
    ("mkt-email.svg", "Email marketing", "Nurturing simple",
     flow_row(["Contact", "Serie utile", "Confiance", "Offre", "Suivi"],
              "Un bon email aide. Un mauvais email fatigue")),
    ("mkt-inbound.svg", "Inbound", "Attirer plutot que pousser",
     compare2("Pousser", ["Pub intrusive", "Spam", "Message froid"],
              "Attirer", ["Contenu utile", "SEO / GEO", "Confiance"],
              "On vient vers toi parce que tu aides")),
    ("mkt-analytics.svg", "Analytics", "Piloter avec 5 chiffres",
     grid3([
         ("Trafic", "D'ou viennent-ils ?"),
         ("Pages", "Quelles pages ?"),
         ("Leads", "Contacts ?"),
         ("Ventes", "Conversions ?"),
         ("Cout", "Combien ca coute ?"),
         ("Apprendre", "Que changer ?"),
     ], "Peu de chiffres, mais les bons")),
    ("mkt-cro.svg", "Conversion", "Enlever les freins",
     flow_row(["Arrivee", "Comprendre", "Confiance", "Action", "Merci"],
              "Chaque etape perdue = des clients qui partent")),
    ("mkt-automation.svg", "Automation", "Workflows simples",
     flow_row(["Declencheur", "Message", "Attente", "Relance", "Stop"],
              "Automatiser le repetitif, garder l'humain pour l'important")),
    ("mkt-budget.svg", "Budget et ROI", "Prioriser les canaux",
     compare2("Cher et flou", ["Tout tester", "Aucun suivi", "Budget eclate"],
              "Simple et mesure", ["1-2 canaux", "Objectif clair", "Arreter ce qui ne marche pas"],
              "Le ROI, c'est : est-ce que ca rapporte assez ?")),
    ("com-strategie.svg", "Strategie com", "Objectifs et canaux",
     flow_row(["Qui ?", "Quoi ?", "Ou ?", "Quand ?", "Mesurer"],
              "Une phrase claire bat un plan de 40 pages")),
    ("com-classique-digital.svg", "Classique vs digital", "Complementaires",
     compare2("Classique", ["Print, salon, presse", "Contact humain", "Ancrage local"],
              "Digital", ["Site, reseaux, email", "Mesurable", "Rapide a ajuster"],
              "Le bon mix depend de ton public")),
    ("com-rp.svg", "Relations presse", "Parler aux medias",
     flow_row(["Angle", "Communique", "Contact", "Relance", "Suite"],
              "Un angle utile > un communique ego")),
    ("com-event.svg", "Evenementiel", "Avant, pendant, apres",
     flow_row(["Avant", "Pendant", "Apres", "Contacts", "Suivi"],
              "L'evenement ne finit pas a la fermeture des portes")),
    ("com-print.svg", "Print et affichage", "Support tangible",
     stack_layers([
         ("Message court", "Une idee"),
         ("Visuel clair", "Lisible de loin"),
         ("Coordonnees", "Faciles a retenir"),
         ("Lien digital", "QR / URL simple"),
     ], "Le print doit mener quelque part")),
    ("com-identite.svg", "Identite visuelle", "Reconnaissance",
     flow_row(["Logo", "Couleurs", "Typo", "Regles", "Exemples"],
              "Si on te reconnait en 2 secondes, c'est gagne")),
    ("com-oral.svg", "Prise de parole", "Structure simple",
     flow_row(["Accroche", "Message", "Preuve", "Appel", "Fin"],
              "Une idee, bien dite, vaut mieux que dix slides")),
    ("com-interne.svg", "Com interne", "Informer et federer",
     grid3([
         ("Clarte", "Qui dit quoi"),
         ("Rythme", "Points reguliers"),
         ("Canaux", "Mail / chat / reunion"),
         ("Ecoute", "Questions OK"),
         ("Decisions", "Tracees"),
         ("Ton", "Respectueux"),
     ], "Une equipe mal informee invente des rumeurs")),
    ("com-digitale.svg", "Presence digitale", "Coherence",
     stack_layers([
         ("Site", "Base de confiance"),
         ("Profils", "Memes infos"),
         ("Contenu", "Utile et regulier"),
         ("Contact", "Facile a trouver"),
     ], "Partout la meme histoire")),
    ("com-community.svg", "Community management", "Animer sans s'epuiser",
     flow_row(["Ecouter", "Publier", "Repondre", "Moderer", "Apprendre"],
              "Repondre vaut souvent plus que publier")),
    ("com-crise.svg", "Crise en ligne", "Reagir proprement",
     flow_row(["Detecter", "Verifier", "Repondre", "Corriger", "Debrief"],
              "Silence + panique = pire cocktail")),
    ("com-influence.svg", "Influence", "Partenariats sinceres",
     compare2("Faux", ["Achat opaque", "Hors sujet", "Zero authenticite"],
              "Sain", ["Affinite reelle", "Transparence", "Valeur partagee"],
              "Un partenaire credible > dix posts achetes")),
    ("com-story.svg", "Storytelling", "Raconter pour marquer",
     flow_row(["Situation", "Probleme", "Action", "Resultat", "Lecon"],
              "Les gens retiennent les histoires, pas les slogans")),
    ("com-ereputation.svg", "E-reputation", "Ecouter et proteger",
     flow_row(["Veille", "Signal", "Reponse", "Preuve", "Ameliorer"],
              "Ta reputation se construit aussi hors de ton site")),
    ("com-b2b-b2c.svg", "B2B vs B2C", "Adapter le message",
     compare2("B2B", ["Plusieurs decideurs", "Preuves / ROI", "Cycle long"],
              "B2C", ["Emotion + clarte", "Decision plus rapide", "Simplicite"],
              "Meme marque, pas le meme discours")),
]
for item in SVGS:
    write_svg(*item)

# ---- Marketing ----
article(
    "marketing-digital-strategie-visibilite",
    "Marketing digital : se faire trouver en ligne (sans se perdre)",
    "Objectifs, cibles et canaux : une strategie simple pour PME et freelances.",
    f"""# Marketing digital : se faire trouver en ligne (sans se perdre)

Le **marketing digital**, c'est simplement : etre visible la ou tes clients cherchent, avec un message clair.

{fig("mkt-strategie.svg", "Schema strategie marketing simple", "Objectif, cible, message, canaux, mesure.")}

## Par ou commencer

1. **Objectif** : notoriete, contacts, ou ventes ?
2. **Cible** : qui exactement ?
3. **Message** : une phrase qu'ils comprennent
4. **Canaux** : 1 ou 2 au debut ([SEO](/blog/articles/seo-fondamentaux-referencement-naturel.html), reseaux, email…)
5. **Mesure** : un chiffre utile

Mieux vaut bien faire peu de choses que tout faire mal. Suite : [reseaux](/blog/articles/marketing-reseaux-sociaux-strategie.html), [email](/blog/articles/marketing-email-nurturing-conversion.html), [budget](/blog/articles/marketing-budget-roi-priorisation.html).
""",
)

article(
    "marketing-reseaux-sociaux-strategie",
    "Reseaux sociaux : etre utile, pas partout",
    "Choisir 1-2 reseaux, un rythme tenable, et mesurer ce qui compte vraiment.",
    f"""# Reseaux sociaux : etre utile, pas partout

Tu n'as pas besoin d'etre sur **tous** les reseaux. Tu as besoin d'etre **utile** la ou ton public est.

{fig("mkt-reseaux.svg", "Schema strategie reseaux sociaux", "Choisir, rythme, valeur, ecoute, preuves, mesure.")}

Publie pour aider. Reponds. Montre des preuves. Mesure les clics utiles, pas seulement les likes. Relie ca a ta [strategie](/blog/articles/marketing-digital-strategie-visibilite.html).
""",
)

article(
    "marketing-email-nurturing-conversion",
    "Email : accompagner sans spammer",
    "Nurturing simple : une serie utile qui construit la confiance avant l'offre.",
    f"""# Email : accompagner sans spammer

Un bon email **aide**. Un mauvais email fatigue.

{fig("mkt-email.svg", "Schema nurturing email", "Contact, serie utile, confiance, offre, suivi.")}

Commence petit : 3 a 5 messages utiles, puis une offre claire. Toujours un moyen de se desinscrire. Ensuite : [conversion](/blog/articles/marketing-conversion-optimisation.html).
""",
)

article(
    "marketing-contenu-inbound",
    "Contenu inbound : attirer plutot que pousser",
    "Creer du contenu utile pour que les bons gens viennent vers toi.",
    f"""# Contenu inbound : attirer plutot que pousser

**Inbound** = tu attires. Les gens viennent parce que tu reponds a leurs questions ([SEO](/blog/articles/seo-contenu-mots-cles-intention-redaction.html), guides, exemples).

{fig("mkt-inbound.svg", "Schema inbound versus pousser", "Attirer avec du contenu utile plutot que forcer.")}

Une page utile par mois bat dix posts vides. Pense aussi au [GEO](/blog/articles/geo-nouveau-seo-ia-guide-complet.html) : etre cite par les IA.
""",
)

article(
    "marketing-analytics-pilotage",
    "Analytics : piloter avec peu de chiffres (mais les bons)",
    "Trafic, leads, ventes, cout : un mini tableau de bord pour decideur.",
    f"""# Analytics : piloter avec peu de chiffres (mais les bons)

Trop de chiffres = brouillard. Cinq questions suffisent.

{fig("mkt-analytics.svg", "Schema analytics marketing", "Trafic, pages, leads, ventes, cout, apprendre.")}

Regarde une fois par semaine. Change **une** chose. Re-mesure. Voir aussi [mesure SEO](/blog/articles/seo-mesurer-search-console-analytics-kpis.html).
""",
)

article(
    "marketing-conversion-optimisation",
    "Conversion : enlever ce qui freine l'action",
    "CRO simple : clarifier le parcours jusqu'au clic ou au formulaire.",
    f"""# Conversion : enlever ce qui freine l'action

La **conversion**, c'est le moment ou quelqu'un passe a l'action (appel, devis, achat).

{fig("mkt-cro.svg", "Schema parcours de conversion", "Arrivee, comprendre, confiance, action, merci.")}

Titre clair, preuve, bouton visible, formulaire court. Teste une chose a la fois ([A/B](/blog/articles/mesurer-ux-kpis-analytics-ab-testing.html)).
""",
)

article(
    "marketing-automatisation-outils",
    "Marketing automation : automatiser sans perdre l'humain",
    "Workflows simples : declencheurs, messages, relances — et quand s'arreter.",
    f"""# Marketing automation : automatiser sans perdre l'humain

L'**automation** sert a ne pas refaire 50 fois la meme tache. Pas a devenir un robot froid.

{fig("mkt-automation.svg", "Schema workflow automation simple", "Declencheur, message, attente, relance, stop.")}

Automatise l'accueil et les rappels. Garde l'humain pour les cas importants. Branche ca a ton [email](/blog/articles/marketing-email-nurturing-conversion.html).
""",
)

article(
    "marketing-budget-roi-priorisation",
    "Budget marketing : ou mettre l'argent (et ou arreter)",
    "Prioriser 1-2 canaux, mesurer le retour, couper ce qui ne marche pas.",
    f"""# Budget marketing : ou mettre l'argent (et ou arreter)

Le **ROI**, en clair : est-ce que ca rapporte assez par rapport a ce que ca coute ?

{fig("mkt-budget.svg", "Schema priorisation budget marketing", "Simple et mesure versus cher et flou.")}

Choisis peu de canaux. Donne-leur une chance mesuree. Arrete le reste. Reviens a ta [strategie](/blog/articles/marketing-digital-strategie-visibilite.html).
""",
)

# ---- Communication ----
article(
    "communication-strategie-objectifs-canaux",
    "Communication : une strategie en 5 questions",
    "Qui, quoi, ou, quand, comment mesurer — sans plan de 40 pages.",
    f"""# Communication : une strategie en 5 questions

Une bonne com tient souvent en **une phrase** claire, repetee au bon endroit.

{fig("com-strategie.svg", "Schema strategie communication", "Qui, quoi, ou, quand, mesurer.")}

Ecris tes reponses sur une page. Puis aligne [print](/blog/articles/communication-print-affichage.html), [digital](/blog/articles/communication-digitale-presence-en-ligne.html) et [oral](/blog/articles/communication-prise-parole-discours.html).
""",
)

article(
    "communication-classique-vs-digitale",
    "Com classique et digitale : mieux ensemble",
    "Print, salons, presse d'un cote ; site et reseaux de l'autre — comment les combiner.",
    f"""# Com classique et digitale : mieux ensemble

Ce n'est pas "l'un ou l'autre". C'est **le bon mix** pour ton public.

{fig("com-classique-digital.svg", "Schema classique versus digital", "Deux mondes complementaires.")}

Un salon sans suivi digital perd des contacts. Un site sans ancrage local perd de la confiance. Voir [evenementiel](/blog/articles/communication-evenementiel.html) et [presence digitale](/blog/articles/communication-digitale-presence-en-ligne.html).
""",
)

article(
    "communication-relations-presse",
    "Relations presse : proposer un angle utile",
    "Communique, contacts medias et relances — sans ego, avec un vrai sujet.",
    f"""# Relations presse : proposer un angle utile

Les medias n'ont pas besoin de ton ego. Ils ont besoin d'un **angle** utile a leurs lecteurs.

{fig("com-rp.svg", "Schema relations presse", "Angle, communique, contact, relance, suite.")}

Court, clair, facts. Puis une relance polie. Complement : [e-reputation](/blog/articles/communication-ereputation-veille.html).
""",
)

article(
    "communication-evenementiel",
    "Evenementiel : avant, pendant, apres",
    "Salons et conferences : preparer, rencontrer, puis surtout suivre.",
    f"""# Evenementiel : avant, pendant, apres

L'evenement ne se joue pas seulement le jour J.

{fig("com-event.svg", "Schema evenementiel avant pendant apres", "Avant, pendant, apres, contacts, suivi.")}

Avant : objectif et outils de capture. Pendant : ecoute. Apres : emails et rendez-vous. Sinon tu as paye pour des cartes de visite qui dorment.
""",
)

article(
    "communication-print-affichage",
    "Print et affichage : une idee, bien visible",
    "Brochure, flyer, affiche : message court, visuel clair, lien vers le digital.",
    f"""# Print et affichage : une idee, bien visible

Le print doit se lire **vite**. Une idee. Un visuel. Des coordonnees.

{fig("com-print.svg", "Schema communication print", "Message, visuel, coordonnees, lien digital.")}

Ajoute un QR ou une URL simple vers une page dediee. Aligne avec ton [identite visuelle](/blog/articles/communication-identite-visuelle-charte.html).
""",
)

article(
    "communication-identite-visuelle-charte",
    "Identite visuelle : qu'on te reconnaisse en 2 secondes",
    "Logo, couleurs, typo et regles simples pour une marque coherente.",
    f"""# Identite visuelle : qu'on te reconnaisse en 2 secondes

Ton **identite visuelle**, c'est ta tenue. Si elle change tous les jours, on ne te reconnait plus.

{fig("com-identite.svg", "Schema identite visuelle", "Logo, couleurs, typo, regles, exemples.")}

Une petite charte suffit : couleurs, polices, exemples oui/non. Utile aussi pour le [design system](/blog/articles/design-system-composants-tokens.html) digital.
""",
)

article(
    "communication-prise-parole-discours",
    "Prise de parole : une idee, bien dite",
    "Accroche, message, preuve, appel : structure simple pour parler sans paniquer.",
    f"""# Prise de parole : une idee, bien dite

A l'oral, moins c'est mieux. Une idee. Des preuves. Un appel clair.

{fig("com-oral.svg", "Schema prise de parole", "Accroche, message, preuve, appel, fin.")}

Entraine-toi a voix haute. Chronometre. Coupe le jargon. Lien avec le [storytelling](/blog/articles/communication-content-storytelling.html).
""",
)

article(
    "communication-interne-entreprise",
    "Communication interne : informer pour federer",
    "Qui dit quoi, sur quel canal, a quel rythme — pour eviter les rumeurs.",
    f"""# Communication interne : informer pour federer

Une equipe mal informee **invente**. Une equipe bien informee avance.

{fig("com-interne.svg", "Schema communication interne", "Clarte, rythme, canaux, ecoute, decisions, ton.")}

Points courts, decisions tracees, questions bienvenues. C'est de la com, pas du controle.
""",
)

article(
    "communication-digitale-presence-en-ligne",
    "Presence en ligne : la meme histoire partout",
    "Site, profils et contenus alignes pour inspirer confiance.",
    f"""# Presence en ligne : la meme histoire partout

Si ton site dit A et ton profil LinkedIn dit B, on doute.

{fig("com-digitale.svg", "Schema presence digitale coherente", "Site, profils, contenu, contact.")}

Base = site clair. Puis les memes infos partout. Relie au [marketing digital](/blog/articles/marketing-digital-strategie-visibilite.html).
""",
)

article(
    "communication-reseaux-sociaux-community-management",
    "Community management : animer sans s'epuiser",
    "Ecouter, publier, repondre, moderer — un rythme humain et utile.",
    f"""# Community management : animer sans s'epuiser

Publier sans repondre, c'est parler dans le vide.

{fig("com-community.svg", "Schema community management", "Ecouter, publier, repondre, moderer, apprendre.")}

Repondre compte souvent plus que le volume de posts. Voir aussi [marketing reseaux](/blog/articles/marketing-reseaux-sociaux-strategie.html).
""",
)

article(
    "communication-crise-en-ligne",
    "Crise en ligne : reagir sans aggraver",
    "Detecter, verifier, repondre, corriger, debrief — une fiche simple sous stress.",
    f"""# Crise en ligne : reagir sans aggraver

Le pire : paniquer **ou** disparaitre.

{fig("com-crise.svg", "Schema communication de crise", "Detecter, verifier, repondre, corriger, debrief.")}

Verifie les faits. Reponds avec calme et preuves. Puis un debrief pour ne pas recommencer. Lien [e-reputation](/blog/articles/communication-ereputation-veille.html).
""",
)

article(
    "communication-influence-partenariats",
    "Influence : des partenariats qui ont du sens",
    "Affinite, transparence et valeur partagee — loin des achats opaques.",
    f"""# Influence : des partenariats qui ont du sens

Un bon partenaire, c'est quelqu'un que ton public **croit deja**.

{fig("com-influence.svg", "Schema partenariats influence", "Sain versus faux.")}

Affinite > audience. Transparence obligatoire. Mesure un resultat concret.
""",
)

article(
    "communication-content-storytelling",
    "Storytelling : raconter pour qu'on s'en souvienne",
    "Situation, probleme, action, resultat : une histoire simple qui marque.",
    f"""# Storytelling : raconter pour qu'on s'en souvienne

Les gens oublient les slogans. Ils retiennent les **histoires**.

{fig("com-story.svg", "Schema storytelling", "Situation, probleme, action, resultat, lecon.")}

Une histoire vraie et courte bat dix arguments abstraits. Utile en [prise de parole](/blog/articles/communication-prise-parole-discours.html) et en contenu web.
""",
)

article(
    "communication-ereputation-veille",
    "E-reputation : ecouter ce qu'on dit de toi",
    "Veille, signaux, reponses et preuves pour proteger ton image en ligne.",
    f"""# E-reputation : ecouter ce qu'on dit de toi

Ta reputation se joue aussi **hors** de ton site : avis, forums, reseaux, IA.

{fig("com-ereputation.svg", "Schema e-reputation et veille", "Veille, signal, reponse, preuve, ameliorer.")}

Mets une alerte simple. Reponds aux vrais problemes. Ameliore le produit. Voir [crise](/blog/articles/communication-crise-en-ligne.html) et [GEO](/blog/articles/geo-off-site-mentions-autorite.html).
""",
)

article(
    "communication-b2b-b2c",
    "B2B ou B2C : adapter le message (pas la marque)",
    "Decideurs multiples vs emotion claire : deux facons de parler, une meme promesse.",
    f"""# B2B ou B2C : adapter le message (pas la marque)

Meme entreprise, pas le meme discours selon que tu parles a une **entreprise** ou a un **particulier**.

{fig("com-b2b-b2c.svg", "Schema communication B2B versus B2C", "Preuves et cycle long vs clarte et emotion.")}

B2B : preuves, ROI, plusieurs decideurs. B2C : simplicite et benefice immédiat. Ta [strategie](/blog/articles/communication-strategie-objectifs-canaux.html) doit le dire clairement.
""",
)

for path, title, desc in [
    (
        ROOT / "blog/content/collections/marketing-digital-serie.json",
        "Série Marketing digital : se faire trouver et convertir",
        "Strategie, reseaux, email, contenu, analytics et budget — expliques simplement.",
    ),
    (
        ROOT / "blog/content/collections/communication-serie.json",
        "Série Communication : se faire comprendre (partout)",
        "Strategie, print, digital, presse, crise et storytelling — sans jargon inutile.",
    ),
]:
    data = json.loads(path.read_text(encoding="utf-8"))
    data["title"] = title
    data["description"] = desc
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"[OK] {path.name}")

print("done")
