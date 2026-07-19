#!/usr/bin/env python3
"""Simplifie Design Patterns GoF : titres, corps accessibles, schemas. Sans bannieres."""
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
    ("dp-intro.svg", "Design Patterns", "Recettes de code reutilisables",
     grid3([
         ("Creationnels", "Comment creer des objets"),
         ("Structurels", "Comment les assembler"),
         ("Comportementaux", "Comment ils discutent"),
         ("Probleme", "Code dur a changer"),
         ("Idee", "Un schema connu"),
         ("Gain", "Plus clair, plus souple"),
     ], "Un pattern = une idee reutilisee, pas une religion")),
    ("dp-singleton.svg", "Singleton", "Une seule instance",
     compare2("Sans", ["Plusieurs copies", "Etats qui divergent", "Tests galere"],
              "Avec", ["Une seule copie", "Acces partage", "Attention aux abus"],
              "Utile rarement : config, cache — pas partout")),
    ("dp-factory-method.svg", "Factory Method", "Creer sans connaitre le detail",
     flow_row(["Demande", "Fabrique", "Produit adapte", "Client content"],
              "Tu demandes un truc, la fabrique choisit comment le creer")),
    ("dp-observer.svg", "Observer", "Previent les abonnes",
     flow_row(["Changement", "Sujet", "A", "B", "C"],
              "Un sujet change : tout le monde abonne est prevenu")),
    ("dp-strategy.svg", "Strategy", "Changer d'algo facilement",
     compare2("Figé", ["If / else geants", "Difficile a etendre"],
              "Strategy", ["Plusieurs methodes", "On change de strategie"],
              "Comme changer de GPS sans changer de voiture")),
    ("dp-decorator.svg", "Decorator", "Couches d'options",
     stack_layers([
         ("Base", "Objet simple"),
         ("Option A", "Ajoute un comportement"),
         ("Option B", "Encore une couche"),
         ("Resultat", "Compose sans tout recoder"),
     ], "Comme des options sur une voiture")),
    ("dp-adapter.svg", "Adapter", "Brancher l'incompatible",
     flow_row(["Ancien format", "Adaptateur", "Nouveau format", "Ca marche"],
              "Comme un chargeur universel")),
    ("dp-facade.svg", "Facade", "Une porte simple",
     compare2("Sans", ["10 appels techniques", "Client perdu"],
              "Avec", ["1 methode claire", "Details caches"],
              "La facade cache la complexite")),
    ("dp-command.svg", "Command", "Action en paquet",
     flow_row(["Bouton", "Commande", "Executer", "Annuler"],
              "Une action devient un objet : on peut la stocker ou l'annuler")),
    ("dp-template-method.svg", "Template Method", "Plan fixe, details libres",
     stack_layers([
         ("Etape 1", "Toujours la meme"),
         ("Etape 2", "A personnaliser"),
         ("Etape 3", "Toujours la meme"),
         ("Resultat", "Meme structure, variantes"),
     ], "Comme une recette avec un ingredient au choix")),
    ("dp-builder.svg", "Builder", "Construire etape par etape",
     flow_row(["Base", "Option", "Option", "Build", "Objet pret"],
              "On assemble clairement, sans constructeur monstrueux")),
    ("dp-iterator.svg", "Iterator", "Parcourir sans tout reveler",
     flow_row(["Collection", "Iterator", "next", "next", "Fin"],
              "Tu avances element par element, sans voir l'interieur")),
    ("dp-state.svg", "State", "Comportement selon l'etat",
     flow_row(["Brouillon", "Publie", "Archive"],
              "Selon l'etat, les actions changent")),
    ("dp-proxy.svg", "Proxy", "Intermediaire controle",
     flow_row(["Client", "Proxy", "Vrai objet"],
              "Le proxy filtre, cache ou protege")),
    ("dp-abstract-factory.svg", "Abstract Factory", "Familles assorties",
     grid3([
         ("Theme clair", "Bouton + champ clairs"),
         ("Theme sombre", "Bouton + champ sombres"),
         ("Regle", "Ne pas melanger"),
         ("Usine A", "Cree la famille A"),
         ("Usine B", "Cree la famille B"),
         ("Client", "Utilise sans savoir"),
     ], "Des objets qui vont bien ensemble")),
    ("dp-composite.svg", "Composite", "Arbre feuille / branche",
     stack_layers([
         ("Dossier", "Contient des enfants"),
         ("Fichier", "Feuille simple"),
         ("Meme API", "totalSize() partout"),
         ("Gain", "Traiter l'arbre uniformement"),
     ], "Comme un dossier et ses fichiers")),
    ("dp-bridge.svg", "Bridge", "Deux axes independants",
     compare2("Axe forme", ["Cercle", "Carre"],
              "Axe rendu", ["Ecran", "Imprimante"],
              "On combine sans explosion de classes")),
    ("dp-prototype.svg", "Prototype", "Copier un modele",
     flow_row(["Modele", "Clone", "Ajuste", "Nouvelle copie"],
              "Plus rapide que tout recreer depuis zero")),
    ("dp-flyweight.svg", "Flyweight", "Partager pour economiser",
     compare2("Lourd", ["Tout duplique", "Memoire gonfle"],
              "Flyweight", ["Partage le commun", "Garde le unique"],
              "Comme une police partagee par plein de lettres")),
    ("dp-chain.svg", "Chain of Responsibility", "Passer au bon maillon",
     flow_row(["Requete", "A?", "B?", "C!", "Traite"],
              "Chaque maillon decide : je gere, ou je passe")),
    ("dp-mediator.svg", "Mediator", "Chef d'orchestre",
     compare2("Spaghetti", ["Chacun parle a tous", "Chaos"],
              "Mediator", ["Tout passe par le centre", "Plus clair"],
              "Comme un air traffic control")),
    ("dp-memento.svg", "Memento", "Sauvegarde et retour",
     flow_row(["Etat", "Save", "Changer", "Restore"],
              "Comme Ctrl+Z : on garde une photo du passe")),
    ("dp-visitor.svg", "Visitor", "Nouvelle operation sans toucher",
     flow_row(["Objets", "Visiteur", "Visite A", "Visite B"],
              "On ajoute un comportement sans modifier chaque classe")),
    ("dp-interpreter.svg", "Interpreter", "Petit langage",
     flow_row(["Texte", "Parse", "Arbre", "Evaluer", "Resultat"],
              "Utile pour regles simples, pas pour tout reinventer")),
]
for item in SVGS:
    write_svg(*item)

# ---- Articles ----
article(
    "design-patterns-introduction-gang-of-four",
    "Design patterns : des recettes pour un code plus clair",
    "Les 23 idees du Gang of Four, expliquees simplement : a quoi ca sert, quand s'en servir.",
    f"""# Design patterns : des recettes pour un code plus clair

Un **design pattern**, c'est une **recette** : un probleme frequent + une idee de solution deja testee.

{fig("dp-intro.svg", "Schema familles de design patterns", "Creationnels, structurels, comportementaux.")}

## Les 3 familles

1. **Creationnels** : comment creer des objets ([Singleton](/blog/articles/design-patterns-singleton.html), [Factory](/blog/articles/design-patterns-factory-method.html)…)
2. **Structurels** : comment les assembler ([Adapter](/blog/articles/design-patterns-adapter.html), [Decorator](/blog/articles/design-patterns-decorator.html)…)
3. **Comportementaux** : comment ils discutent ([Observer](/blog/articles/design-patterns-observer.html), [Strategy](/blog/articles/design-patterns-strategy.html)…)

## Regle d'or

Ne force pas un pattern. Commence par le probleme. Si la recette colle, utilise-la. Sinon, code simple.
""",
)

article(
    "design-patterns-singleton",
    "Singleton : une seule copie, pas plus",
    "Garantir une seule instance partagee — utile parfois, dangereux si abuse.",
    f"""# Singleton : une seule copie, pas plus

Le **Singleton** dit : il n'existe qu'**une** copie de cet objet pour tout le programme.

{fig("dp-singleton.svg", "Schema Singleton", "Une seule copie partagee versus plusieurs copies qui divergent.")}

## Analogie

Comme le **maire** d'une ville : un seul poste. Tout le monde passe par la meme personne.

## Quand c'est utile

Config globale, un cache partage, un logger. **Rarement** plus.

## Attention

Trop de Singletons = code difficile a tester (tout est lie). Prefere parfois un simple module ou l'[injection](/blog/articles/design-patterns-factory-method.html). Suite de la serie : [Observer](/blog/articles/design-patterns-observer.html).
""",
)

article(
    "design-patterns-factory-method",
    "Factory Method : laisser creer sans se prendre la tete",
    "Demander un objet a une fabrique au lieu de tout construire a la main.",
    f"""# Factory Method : laisser creer sans se prendre la tete

La **fabrique** cree l'objet pour toi. Toi, tu demandes juste "un paiement" ou "un bouton".

{fig("dp-factory-method.svg", "Schema Factory Method", "Demande, fabrique, produit adapte.")}

## Analogie

Tu commandes un cafe. Le barista choisit la machine et la recette. Tu ne rentres pas en cuisine.

## Pourquoi c'est cool

Tu peux changer le type cree **sans** casser le code qui utilise le produit. Voir aussi [Abstract Factory](/blog/articles/design-patterns-abstract-factory.html) et [Builder](/blog/articles/design-patterns-builder.html).
""",
)

article(
    "design-patterns-observer",
    "Observer : prevenir plein de gens d'un coup",
    "Quand quelque chose change, tous les abonnes sont prevenus automatiquement.",
    f"""# Observer : prevenir plein de gens d'un coup

Le **sujet** change. Les **abonnes** (observers) sont prevenus. Personne n'a besoin de tout hardcoder.

{fig("dp-observer.svg", "Schema Observer", "Un sujet notifie A, B et C.")}

## Analogie

Tu t'abonnes a une chaine : quand une video sort, tu es notifie. La chaine ne te connait pas personnellement.

## Ou on le voit

UI qui se met a jour, notifications, events. Cousin utile : [Mediator](/blog/articles/design-patterns-mediator.html) si trop d'abonnes se parlent entre eux.
""",
)

article(
    "design-patterns-strategy",
    "Strategy : changer de methode sans tout casser",
    "Plusieurs facons de faire la meme chose, interchangeables.",
    f"""# Strategy : changer de methode sans tout casser

Une **strategie** = une maniere de faire. Tu peux en changer sans reecrire tout le programme.

{fig("dp-strategy.svg", "Schema Strategy", "If/else geants versus strategies interchangeables.")}

## Analogie

Meme trajet, GPS different (voiture, velo, pied). La voiture reste la voiture.

## Exemple

Trier, payer, calculer frais de port… plusieurs algos, meme interface. Complement : [State](/blog/articles/design-patterns-state.html) (le comportement depend d'un etat).
""",
)

article(
    "design-patterns-decorator",
    "Decorator : ajouter des options comme des couches",
    "Enrichir un objet sans modifier sa classe de base.",
    f"""# Decorator : ajouter des options comme des couches

Le **Decorator** enveloppe un objet et ajoute un comportement. On peut empiler les couches.

{fig("dp-decorator.svg", "Schema Decorator", "Base puis options empilees.")}

## Analogie

Cafe + lait + chantilly. Chaque option enveloppe la precedente.

## Différence avec heritage

Heritage fixe. Decorator compose a la volee. Voir aussi [Proxy](/blog/articles/design-patterns-proxy.html) (controle d'acces) et [Adapter](/blog/articles/design-patterns-adapter.html) (compatibilite).
""",
)

article(
    "design-patterns-adapter",
    "Adapter : faire marcher deux pieces incompatibles",
    "Traduire une interface pour brancher l'ancien sur le nouveau.",
    f"""# Adapter : faire marcher deux pieces incompatibles

L'**Adapter** traduit. D'un cote un format, de l'autre un autre. Au milieu : l'adaptateur.

{fig("dp-adapter.svg", "Schema Adapter", "Ancien format, adaptateur, nouveau format.")}

## Analogie

Un **prise / chargeur universel** : la prise murale et ton appareil ne sont pas les memes.

## Quand

API legacy, lib tierce, formats differents. Ne confonds pas avec [Facade](/blog/articles/design-patterns-facade.html) (simplifie) ni [Bridge](/blog/articles/design-patterns-bridge.html) (separe deux axes).
""",
)

article(
    "design-patterns-facade",
    "Facade : une porte simple vers un systeme complexe",
    "Cacher 10 appels techniques derriere une methode claire.",
    f"""# Facade : une porte simple vers un systeme complexe

La **Facade** offre une entree simple. Derriere, plein de pieces techniques restent cachees.

{fig("dp-facade.svg", "Schema Facade", "Une methode claire versus dix appels techniques.")}

## Analogie

La **reception** d'un hotel : tu demandes une chambre, tu ne geres pas le menage, la cle, la facture.

## Gain

Le client (ton code UI) reste simple. Les details restent au service. Cousin : [Mediator](/blog/articles/design-patterns-mediator.html) pour coordonner des egaux.
""",
)

article(
    "design-patterns-command",
    "Command : une action en paquet (qu'on peut annuler)",
    "Transformer une action en objet : executer, stocker, annuler, rejouer.",
    f"""# Command : une action en paquet (qu'on peut annuler)

Une **Command** = "fais ca" emballe dans un objet. On peut la mettre en file, l'annuler, la rejouer.

{fig("dp-command.svg", "Schema Command", "Bouton, commande, executer, annuler.")}

## Analogie

Une **telecommande** : chaque bouton envoie une commande. Tu peux meme avoir "annuler".

## Ou c'est top

Undo/redo, files de taches, macros. Voir [Memento](/blog/articles/design-patterns-memento.html) pour restaurer un etat complet.
""",
)

article(
    "design-patterns-template-method",
    "Template Method : meme plan, details au choix",
    "Une recette fixe avec quelques etapes a personnaliser.",
    f"""# Template Method : meme plan, details au choix

Le **Template Method** fixe l'ordre des etapes. Les sous-classes remplissent les trous.

{fig("dp-template-method.svg", "Schema Template Method", "Etapes fixes et etape a personnaliser.")}

## Analogie

Recette de gateau : melanger, cuire, decorer. La decoration change ; le plan reste.

## Astuce

Garde le squelette dans la classe mere, mets le variable ailleurs. Proche de [Strategy](/blog/articles/design-patterns-strategy.html), mais ici l'ordre est impose.
""",
)

article(
    "design-patterns-builder",
    "Builder : construire etape par etape",
    "Assembler un objet complexe clairement, sans constructeur monstrueux.",
    f"""# Builder : construire etape par etape

Le **Builder** te laisse ajouter des options une par une, puis `build()`.

{fig("dp-builder.svg", "Schema Builder", "Base, options, build, objet pret.")}

## Analogie

Commander un sandwich : pain, sauce, garnitures, puis "c'est pret".

## Pourquoi

Evite les constructeurs a 12 parametres. Complement : [Factory Method](/blog/articles/design-patterns-factory-method.html) pour creer, Builder pour configurer.
""",
)

article(
    "design-patterns-iterator",
    "Iterator : parcourir sans tout reveler",
    "Avancer element par element sans exposer la structure interne.",
    f"""# Iterator : parcourir sans tout reveler

L'**Iterator** dit : "suivant ?" jusqu'a la fin. Toi, tu ne vois pas si c'est une liste, un arbre, un fichier.

{fig("dp-iterator.svg", "Schema Iterator", "Collection, iterator, next, next, fin.")}

## Analogie

Une **playlist** : tu passes a la suivante sans ouvrir le tiroir des fichiers.

## Bonus

Tu peux avoir plusieurs parcours (avant, arriere) sans casser la collection. Souvent couple a [Composite](/blog/articles/design-patterns-composite.html).
""",
)

article(
    "design-patterns-state",
    "State : le comportement change selon l'etat",
    "Selon ou tu en es (brouillon, publie…), les actions autorisees changent.",
    f"""# State : le comportement change selon l'etat

Avec **State**, l'objet se comporte differemment selon son etat actuel.

{fig("dp-state.svg", "Schema State", "Brouillon, publie, archive.")}

## Analogie

Une **commande en ligne** : panier, paye, expedie. Tu ne peux pas "expedier" depuis le panier.

## Vs Strategy

Strategy : tu choisis l'algo. State : l'etat decide (et peut changer tout seul). Voir [Strategy](/blog/articles/design-patterns-strategy.html).
""",
)

article(
    "design-patterns-proxy",
    "Proxy : un intermediaire qui controle l'acces",
    "Un objet devant un autre : cache, securite, ou chargement lazy.",
    f"""# Proxy : un intermediaire qui controle l'acces

Le **Proxy** se place devant le vrai objet. Le client parle au proxy.

{fig("dp-proxy.svg", "Schema Proxy", "Client, proxy, vrai objet.")}

## Analogie

Un **gardien** a l'entree : il verifie, puis te laisse entrer (ou non).

## Usages

Lazy loading, cache, droits d'acces, logs. Differe du [Decorator](/blog/articles/design-patterns-decorator.html) (ajoute une feature) et de la [Facade](/blog/articles/design-patterns-facade.html) (simplifie un sous-systeme).
""",
)

article(
    "design-patterns-abstract-factory",
    "Abstract Factory : des familles d'objets qui vont ensemble",
    "Creer des lots coherents (theme clair / sombre) sans melanger les pieces.",
    f"""# Abstract Factory : des familles d'objets qui vont ensemble

L'**Abstract Factory** cree des **familles** assorties : bouton + champ + fenetre du meme style.

{fig("dp-abstract-factory.svg", "Schema Abstract Factory", "Familles assorties, ne pas melanger.")}

## Analogie

Un **pack salon** : canape + fauteuil + table du meme style. Pas un canape baroque avec une table IKEA au hasard.

## Lien

Plus "macro" que [Factory Method](/blog/articles/design-patterns-factory-method.html). Utile UI multi-themes, multi-plateformes.
""",
)

article(
    "design-patterns-composite",
    "Composite : traiter un arbre comme une seule piece",
    "Dossiers et fichiers : meme API pour une feuille ou une branche.",
    f"""# Composite : traiter un arbre comme une seule piece

Le **Composite** permet de manipuler un element **seul** ou un **groupe** de la meme facon.

{fig("dp-composite.svg", "Schema Composite", "Dossier, fichier, meme API.")}

## Analogie

Un **dossier** : `taille totale` marche pour un fichier et pour un dossier entier.

## Ou

Menus, arbres de scene, org charts. Souvent avec [Iterator](/blog/articles/design-patterns-iterator.html) pour parcourir.
""",
)

article(
    "design-patterns-bridge",
    "Bridge : deux axes independants (sans explosion de classes)",
    "Separer forme et rendu (ou appareil et protocole) pour les combiner librement.",
    f"""# Bridge : deux axes independants (sans explosion de classes)

Le **Bridge** separe deux dimensions qui évoluent chacune de leur cote.

{fig("dp-bridge.svg", "Schema Bridge", "Axe forme et axe rendu combines.")}

## Analogie

**Forme** (cercle / carre) × **rendu** (ecran / imprimante). Sans Bridge, tu exploses en CercleEcran, CarreImprimante…

## Vs Adapter

Adapter repare un mauvais fit. Bridge est prevu des le debut pour evoluer. Voir [Adapter](/blog/articles/design-patterns-adapter.html).
""",
)

article(
    "design-patterns-prototype",
    "Prototype : copier un modele plutot que tout recreer",
    "Cloner un objet existant puis ajuster — plus simple parfois que construire a neuf.",
    f"""# Prototype : copier un modele plutot que tout recreer

Le **Prototype** part d'un modele, le **clone**, puis tu ajustes.

{fig("dp-prototype.svg", "Schema Prototype", "Modele, clone, ajuste, nouvelle copie.")}

## Analogie

Un **tampon** ou un modele Word : tu dupliques, tu changes 2 champs.

## Quand

Objets couteux a creer, ou beaucoup de variantes proches. Voir aussi [Builder](/blog/articles/design-patterns-builder.html).
""",
)

article(
    "design-patterns-flyweight",
    "Flyweight : partager pour economiser la memoire",
    "Factoriser ce qui est commun, garder a part ce qui est unique.",
    f"""# Flyweight : partager pour economiser la memoire

Le **Flyweight** partage les donnees **communes** entre plein d'objets semblables.

{fig("dp-flyweight.svg", "Schema Flyweight", "Tout duplique versus partage du commun.")}

## Analogie

Dans un livre, la **police** est partagee. Chaque lettre n'emporte pas sa propre copie de la police.

## Attention

Utile si tu as **beaucoup** d'instances. Sinon, complexite inutile. Cousin memoire : parfois [Proxy](/blog/articles/design-patterns-proxy.html) pour le lazy.
""",
)

article(
    "design-patterns-chain-of-responsibility",
    "Chain of Responsibility : passer la demande au bon maillon",
    "Chaque etape decide : je traite, ou je passe au suivant.",
    f"""# Chain of Responsibility : passer la demande au bon maillon

Une **chaine** : A regarde, sinon B, sinon C… jusqu'a ce que quelqu'un traite.

{fig("dp-chain.svg", "Schema Chain of Responsibility", "Requete passee de maillon en maillon.")}

## Analogie

Support client : niveau 1, puis 2, puis expert. Ou une file de validateurs.

## Gain

Tu ajoutes un maillon sans toucher les autres. Voir [Command](/blog/articles/design-patterns-command.html) pour emballer la requete.
""",
)

article(
    "design-patterns-mediator",
    "Mediator : un chef d'orchestre entre les objets",
    "Les objets ne se parlent plus tous entre eux : ils passent par un centre.",
    f"""# Mediator : un chef d'orchestre entre les objets

Le **Mediator** centralise les echanges. Fini le spaghetti "tout le monde appelle tout le monde".

{fig("dp-mediator.svg", "Schema Mediator", "Spaghetti versus centre de coordination.")}

## Analogie

La **tour de controle** d'un aeroport : les avions ne negocient pas entre eux.

## Vs Observer

Observer diffuse un evenement. Mediator **coordonne** des interactions precises. Voir [Observer](/blog/articles/design-patterns-observer.html).
""",
)

article(
    "design-patterns-memento",
    "Memento : sauvegarder pour pouvoir revenir en arriere",
    "Prendre une photo de l'etat, la ranger, la restaurer plus tard (Ctrl+Z).",
    f"""# Memento : sauvegarder pour pouvoir revenir en arriere

Le **Memento** garde une **photo** de l'etat. Plus tard, on restaure.

{fig("dp-memento.svg", "Schema Memento", "Etat, save, changer, restore.")}

## Analogie

**Ctrl+Z** ou une sauvegarde de jeu.

## Tip

Ne laisse pas tout le monde fouiller dans la sauvegarde : un gardien (caretaker) la range. Couple bien avec [Command](/blog/articles/design-patterns-command.html) pour l'historique.
""",
)

article(
    "design-patterns-visitor",
    "Visitor : ajouter une operation sans toucher les classes",
    "Une nouvelle action qui visite chaque type d'objet, sans modifier leur code.",
    f"""# Visitor : ajouter une operation sans toucher les classes

Le **Visitor** apporte une nouvelle operation. Les objets acceptent la visite.

{fig("dp-visitor.svg", "Schema Visitor", "Objets visites par un visiteur.")}

## Analogie

Un **controleur des impots** qui visite chaque type de dossier avec des regles differentes.

## Quand

Beaucoup de types stables, beaucoup d'operations qui changent (export, stats…). Sinon, ca peut etre lourd. Intro : [patterns](/blog/articles/design-patterns-introduction-gang-of-four.html).
""",
)

article(
    "design-patterns-interpreter",
    "Interpreter : comprendre un petit langage",
    "Lire une expression simple (regles, formules) et l'evaluer.",
    f"""# Interpreter : comprendre un petit langage

L'**Interpreter** lit une petite grammaire (regles, filtres) et calcule un resultat.

{fig("dp-interpreter.svg", "Schema Interpreter", "Texte, parse, arbre, evaluer, resultat.")}

## Analogie

Une **calculatrice** ou un filtre "prix > 10 ET stock".

## Attention

Pour un vrai langage complexe, utilise un vrai parseur. Ici : regles metier simples. Retour a l'[intro](/blog/articles/design-patterns-introduction-gang-of-four.html).
""",
)

# Collection
col_path = COLLECTIONS / "design-patterns-serie.json"
col = json.loads(col_path.read_text(encoding="utf-8"))
col["title"] = "Serie Design Patterns — recettes de code (GoF, version simple)"
col["description"] = (
    "Les 23 design patterns du Gang of Four expliques simplement : analogies du quotidien, "
    "schemas, et liens entre articles — sans jargon inutile."
)
col_path.write_text(json.dumps(col, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"[OK] {col_path.name}")
print("done")
