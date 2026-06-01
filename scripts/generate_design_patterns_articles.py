#!/usr/bin/env python3
"""Génère les 24 articles Markdown de la série Design Patterns."""

from __future__ import annotations

from pathlib import Path
from textwrap import dedent

BASE = Path(__file__).resolve().parent.parent
OUT = BASE / "blog" / "content" / "articles"
SERIES = "design-patterns-serie"
DATE_START = "2026-04-01"


def fm(
    title: str,
    excerpt: str,
    order: int,
    slug: str,
    tags: list[str],
    date: str,
) -> str:
    og = f"{slug}-1200x630.jpg"
    tag_line = ", ".join(tags)
    return f"""---
title: "{title}"
date: {date}
excerpt: "{excerpt}"
type: article
tags: [{tag_line}]
og_image: {og}
series: {SERIES}
series_order: {order}
---

"""


def block(*parts: str) -> str:
    return "\n\n".join(dedent(p).strip() for p in parts) + "\n"


INTRO = block(
    """
    # Introduction aux Design Patterns : guide pour développeurs juniors

    Tu as déjà copié-collé du code d'un collègue sans comprendre pourquoi c'était structuré comme ça ? Ou tu t'es retrouvé avec une classe de 800 lignes que personne n'ose toucher ? Les **design patterns** (patrons de conception) existent pour t'aider à nommer des solutions qui marchent, à communiquer avec ton équipe, et à éviter de réinventer la roue à chaque feature.

    Ce premier article de la série pose les bases. Les suivants détaillent **chaque pattern du Gang of Four (GoF)**, classé par famille : créationnels, structurels, comportementaux.

    ---

    ## Qu'est-ce qu'un design pattern ?

    Un design pattern est une **solution réutilisable** à un problème récurrent de conception logicielle. Ce n'est pas une librairie à installer : c'est une **façon d'organiser tes classes, modules et objets** pour garder le code lisible, testable et évolutif.

    ### Ce qu'un pattern n'est pas

    - Ce n'est **pas** une règle absolue : « il faut toujours utiliser Singleton » est faux.
    - Ce n'est **pas** du code copiable tel quel : tu l'adaptes à ton langage et ton contexte.
    - Ce n'est **pas** une excuse pour sur-architecturer un CRUD de 3 écrans.

    ### Ce qu'un pattern est

    - Un **vocabulaire partagé** : « on met un Observer ici » = tout le monde visualise la même chose.
    - Une **réponse éprouvée** à un problème précis (création d'objets, couplage, algorithmes interchangeables…).
    - Un **outil de réflexion** avant d'écrire la dixième variante `if/else`.

    <figure>
      <img src="../../assets/images/blog/design-patterns-families.svg" alt="Les trois familles de design patterns GoF" class="schema-inline" width="520" />
      <figcaption>Les 23 patterns GoF se répartissent en trois familles : 5 créationnels, 7 structurels, 11 comportementaux.</figcaption>
    </figure>

    ---

    ## D'où viennent les patterns GoF ?

    En 1994, quatre auteurs (Gamma, Helm, Johnson, Vlissides — d'où « Gang of Four ») publient *Design Patterns: Elements of Reusable Object-Oriented Software*. Ils cataloguent **23 patterns** observés sur des projets réels en C++ et Smalltalk.

    Aujourd'hui, les langages ont changé (TypeScript, Python, Rust…), mais **les problèmes restent les mêmes** : qui crée l'objet ? comment découpler l'interface de l'implémentation ? comment notifier plusieurs composants sans spaghetti ?

    ---

    ## Les trois familles

    | Famille | Question centrale | Exemples |
    |---------|-------------------|----------|
    | **Créationnels** | Comment instancier proprement ? | Singleton, Factory, Builder |
    | **Structurels** | Comment composer classes et objets ? | Adapter, Decorator, Facade |
    | **Comportementaux** | Comment répartir responsabilités et algorithmes ? | Strategy, Observer, Command |

    Dans cette série, **un article = un pattern**, dans l'ordre des familles. Tu peux lire linéairement ou sauter vers celui qui résout ton problème du moment.

    ---

    ## Principes à connaître avant les patterns

    Les patterns s'appuient sur des principes SOLID (résumé junior-friendly) :

    1. **S**ingle Responsibility — une classe, une raison de changer.
    2. **O**pen/Closed — ouvert à l'extension, fermé à la modification sauvage.
    3. **L**iskov Substitution — les sous-types doivent pouvoir remplacer le type parent.
    4. **I**nterface Segregation — petites interfaces plutôt qu'un monstre `IManager`.
    5. **D**ependency Inversion — dépendre d'abstractions, pas de détails concrets.

    Tu n'as pas besoin de maîtriser SOLID par cœur avant de lire la série. Reviens-y quand un pattern te parle d'« inversion de dépendances » ou de « fermer à la modification ».

    ---

    ## Comment lire la série efficacement

    Pour chaque article :

    1. Lis **« En une phrase »** et **« Le problème »** — si ça ne te parle pas, passe (pour l'instant).
    2. Regarde le **schéma** et l'**exemple TypeScript** (langage principal de la série).
    3. Parcours l'**exemple Python** si tu bosses plutôt côté backend.
    4. Note **« Quand ne pas l'utiliser »** — souvent plus utile que la théorie.
    5. Fais l'**exercice** en 20 minutes sur un mini-projet perso.

    ---

    ## Patterns modernes hors GoF (aperçu)

    Le catalogue GoF n'épuise pas tout :

    - **Repository / Service** — couche d'accès aux données (souvent avec DI).
    - **Dependency Injection** — fournir les dépendances de l'extérieur (frameworks, conteneurs IoC).
    - **CQRS / Event Sourcing** — architectures avancées pour gros domaines.

    On les croise parfois avec Factory, Strategy ou Observer. Cette série reste focalisée sur les **23 GoF** pour une base solide.

    ---

    ## Erreurs classiques des juniors avec les patterns

    | Erreur | Conséquence | Meilleure attitude |
    |--------|-------------|-------------------|
    | Appliquer un pattern « parce que c'est cool » | Code verbeux, difficile à lire | Commence simple ; refactorise quand la douleur apparaît |
    | Tout mélanger dans une même classe | God Object | Extrais une responsabilité à la fois |
    | Confondre noms proches | Factory vs Abstract Factory vs Builder | Lis les articles dans l'ordre créationnel |
    | Oublier les tests | Patterns non refactorables | Écris un test avant d'introduire le pattern |

    ---

    ## Plan de la série

    **Créationnels (articles 2 à 6)** : Singleton, Factory Method, Abstract Factory, Builder, Prototype.

    **Structurels (7 à 13)** : Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy.

    **Comportementaux (14 à 24)** : Chain of Responsibility, Command, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor, Interpreter.

    ---

    ## Exercice : cartographier ton projet

    Ouvre un projet perso ou pro (même petit). Pour chaque module, note :

    - Où la **création** d'objets est compliquée (→ famille créationnelle).
    - Où tu as des **adaptateurs** vers des APIs tierces (→ structurel).
    - Où tu as des **gros switch** sur le comportement (→ comportemental).

    Tu n'as pas besoin de tout refactoriser. L'objectif est d'**entraîner ton œil**.

    ---

    ## Résumé

    - Un design pattern = solution nommée à un problème de conception récurrent.
    - 23 patterns GoF en 3 familles ; cette série = 1 article par pattern + cette intro.
    - Utilise les patterns pour **communiquer** et **simplifier**, pas pour impressionner.
    - Article suivant : **Singleton** — quand une seule instance a du sens (et quand c'en est une mauvaise idée).
    """,
)


def pattern_article(
    order: int,
    slug: str,
    name: str,
    family: str,
    family_fr: str,
    date: str,
    one_liner: str,
    problem: str,
    idea: str,
    analogy: str,
    ts_example: str,
    py_example: str,
    when_use: str,
    when_not: str,
    mistakes: str,
    related: str,
    exercise: str,
    summary: str,
    prev_link: str,
    next_link: str,
) -> str:
    svg = f"dp-{slug.replace('design-patterns-', '')}.svg"
    tags = ["Design Patterns", "GoF", name, family_fr, "TypeScript", "Python", "junior"]
    excerpt = one_liner[:200].replace('"', "'")
    title = f"{name} : pattern {family_fr.lower()} expliqué pour juniors"
    body = block(
        f"""
        # {name} : comprendre et appliquer le pattern

        **Famille :** {family_fr} · **Série :** Design Patterns GoF · **Article {order}/24**

        {one_liner}

        ---

        ## En une phrase

        {one_liner}

        ---

        ## Le problème sans ce pattern

        {problem}

        ---

        ## L'idée du pattern {name}

        {idea}

        ### Analogie du quotidien

        {analogy}

        <figure>
          <img src="../../assets/images/blog/{svg}" alt="Schéma simplifié du pattern {name}" class="schema-inline" width="400" />
          <figcaption>Vue simplifiée : le client délègue au rôle défini par le pattern {name}.</figcaption>
        </figure>

        ---

        ## Exemple en TypeScript

        {ts_example}

        ---

        ## Exemple en Python

        {py_example}

        ---

        ## Quand utiliser {name}

        {when_use}

        ---

        ## Quand ne pas utiliser {name}

        {when_not}

        ---

        ## Erreurs fréquentes des juniors

        {mistakes}

        ---

        ## Patterns proches

        {related}

        ---

        ## Exercice pratique (20–30 min)

        {exercise}

        ---

        ## Résumé

        {summary}

        ---

        ## Navigation dans la série

        - Précédent : {prev_link}
        - Suivant : {next_link}
        """,
    )
    return fm(title, excerpt, order, slug, tags, date) + body


# Données condensées mais complètes par pattern
PATTERNS_DATA = [
    {
        "slug": "design-patterns-singleton",
        "name": "Singleton",
        "family_fr": "Créationnel",
        "one_liner": "Le Singleton garantit qu'une classe n'a qu'une seule instance et fournit un point d'accès global à celle-ci.",
        "problem": "Tu as besoin d'un objet unique partagé (connexion config, logger, pool) mais `new MaClasse()` partout crée des doublons, des états incohérents et des bugs difficiles à tracer.",
        "idea": "Tu **cache le constructeur** (privé ou protégé) et tu exposes une méthode statique `getInstance()` qui crée l'instance au premier appel (lazy) ou au chargement du module.",
        "analogy": "Comme le **maire d'une ville** : il n'y en a qu'un à la fois. Tu ne « crées » pas un nouveau maire à chaque question administrative — tu passes par l'instance officielle.",
        "ts_example": '''
        ```typescript
        class AppConfig {
          private static instance: AppConfig | null = null;
          private constructor(public readonly apiUrl: string) {}

          static getInstance(): AppConfig {
            if (!AppConfig.instance) {
              AppConfig.instance = new AppConfig(import.meta.env.VITE_API_URL);
            }
            return AppConfig.instance;
          }
        }

        const a = AppConfig.getInstance();
        const b = AppConfig.getInstance();
        console.log(a === b); // true
        ```
        ''',
        "py_example": '''
        ```python
        class AppConfig:
            _instance = None

            def __new__(cls, api_url: str):
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.api_url = api_url
                return cls._instance
        ```
        ''',
        "when_use": "- Ressource réellement unique (config lecture seule, identifiant d'app).\n- Coût de création élevé et partage légitime.\n- Besoin d'un état global **maîtrisé**.",
        "when_not": "- Testabilité importante (Singleton = état global = tests flaky).\n- Multi-instances naturelles (panier utilisateur ≠ singleton).\n- En frontend moderne : préfère modules ES / context React / injection.",
        "mistakes": "- Singleton « par défaut » partout.\n- Oublier le thread-safety en environnement concurrent.\n- Stocker trop de logique métier dans l'instance unique (God Object).",
        "related": "- **Factory** : crée des objets sans exposer `new` partout.\n- **Monostate** (variante) : état statique partagé sans vrai singleton d'instance.",
        "exercise": "Implémente un `Logger` singleton puis réécris-le sans singleton : passe le logger en paramètre. Compare la facilité de tests unitaires.",
        "summary": "Singleton = une instance, un accès. Utile pour de vraies ressources uniques ; dangereux comme raccourci global. En 2026, questionne d'abord l'injection de dépendances.",
    },
    {
        "slug": "design-patterns-factory-method",
        "name": "Factory Method",
        "family_fr": "Créationnel",
        "one_liner": "La Factory Method délègue la création d'objets aux sous-classes, sans que le client connaisse la classe concrète instanciée.",
        "problem": "Ton code client contient `if (type === 'pdf') ... else if (type === 'csv')` à chaque fois que tu dois créer un exporteur. Ajouter un format = modifier 12 fichiers.",
        "idea": "Une classe de base (ou interface) déclare une méthode `createX()` ; chaque sous-classe retourne le produit adapté. Le client appelle la factory, pas `new Concrete()`.",
        "analogy": "Un **restaurant** : tu commandes « un plat du jour ». La cuisine (sous-classe) décide si c'est poisson ou viande ; toi tu ne vas pas en cuisine choisir la poêle.",
        "ts_example": '''
        ```typescript
        interface Exporter { export(data: unknown): string; }

        abstract class ExportService {
          protected abstract createExporter(): Exporter;
          run(data: unknown) {
            return this.createExporter().export(data);
          }
        }

        class PdfExportService extends ExportService {
          protected createExporter() { return { export: (d) => `PDF:${JSON.stringify(d)}` }; }
        }
        ```
        ''',
        "py_example": '''
        ```python
        class ExportService(ABC):
            @abstractmethod
            def create_exporter(self) -> Exporter: ...

            def run(self, data):
                return self.create_exporter().export(data)
        ```
        ''',
        "when_use": "- Le type exact du produit dépend du contexte (environnement, config, utilisateur).\n- Tu veux respecter Open/Closed : nouveau produit = nouvelle sous-classe.",
        "when_not": "- Une seule implémentation et pas d'évolution prévue.\n- La création est triviale (`return new Date()`).",
        "mistakes": "- Confondre avec Abstract Factory (une factory = une famille entière).\n- Hiérarchies trop profondes pour 2 produits.",
        "related": "- **Abstract Factory** : familles d'objets liés.\n- **Simple Factory** (non GoF) : fonction unique `create(type)`.",
        "exercise": "Crée `NotificationFactory` avec Email / SMS / Push. Ajoute Slack sans toucher au code client `sendAlert()`.",
        "summary": "Factory Method = création polymorphe via sous-classes. Idéal quand le « quel produit » varie selon le contexte métier.",
    },
]


def all_patterns() -> list[dict]:
    """Retourne la liste complète des 23 patterns (hors intro)."""
    # Les deux premiers sont détaillés ci-dessus ; le reste est généré avec le même gabarit
    extra = [
        ("design-patterns-abstract-factory", "Abstract Factory", "Créationnel",
         "Fournit une interface pour créer des familles d'objets liés sans les nommer concrètement.",
         "Tu dois créer des UI Windows ET Mac cohérentes (bouton + checkbox du même style) sans mélanger les kits.",
         "Une factory abstraite expose `createButton()` et `createCheckbox()` ; `MacFactory` et `WinFactory` garantissent la cohérence.",
         "Un **kit de meuble** IKEA vs artisan : tu ne mélanges pas les vis du kit A avec les plateaux du kit B."),
        ("design-patterns-builder", "Builder", "Créationnel",
         "Construit un objet complexe étape par étape, en séparant la construction de sa représentation.",
         "Un objet a 15 paramètres optionnels ; les constructeurs deviennent illisibles.",
         "Un `QueryBuilder` avec `select().from().where()` — chaque méthode retourne `this`, l'objet final est immuable.",
         "Assembler un **burger** : pain, steak, sauce — tu choisis l'ordre sans tout passer au caissier d'un coup."),
        ("design-patterns-prototype", "Prototype", "Créationnel",
         "Crée de nouveaux objets en copiant un prototype existant plutôt qu'en appelant `new` sur une sous-classe.",
         "Cloner une config ou un document template coûte moins que de tout recharger depuis la DB.",
         "Implémente `clone()` / `copy()` ; le client demande une copie du prototype enregistré.",
         "Photocopieuse : tu dupliques une feuille modèle au lieu de retaper le document."),
        ("design-patterns-adapter", "Adapter", "Structurel",
         "Convertit l'interface d'une classe existante en une autre interface attendue par le client.",
         "Une API tierce renvoie du XML ; ton app attend du JSON.",
         "Une classe `XmlToJsonAdapter` implémente ton interface `DataPort` et wrap l'API legacy.",
         "Adaptateur prise **EU → US** : l'appareil ne change pas, la prise s'adapte."),
        ("design-patterns-bridge", "Bridge", "Structurel",
         "Sépare une abstraction de son implémentation pour qu'elles évoluent indépendamment.",
         "Tu as des formes (cercle, carré) ET des moteurs de rendu (SVG, Canvas) — évite l'explosion de classes.",
         "Abstraction `Shape` contient une référence vers `Renderer` injectée.",
         "Télécommande (abstraction) et téléviseur (implémentation) : change l'un sans refabriquer l'autre."),
        ("design-patterns-composite", "Composite", "Structurel",
         "Compose des objets en arborescences pour traiter individus et groupes uniformément.",
         "Menu avec sous-menus : `render()` doit marcher sur une feuille et sur un dossier.",
         "Interface `Component` avec `add()`, `remove()`, `operation()` ; `Leaf` et `Composite`.",
         "Dossier système : un fichier et un répertoire peuvent tous deux être « parcourus »."),
        ("design-patterns-decorator", "Decorator", "Structurel",
         "Ajoute dynamiquement des responsabilités à un objet sans modifier sa classe.",
         "Stream : compression puis chiffrement puis buffer autour d'un fichier.",
         "Wrappers qui implémentent la même interface et délèguent au composant interne.",
         "Gâteau : tu ajoutes glaçage et sprinkles sans changer la recette de base."),
        ("design-patterns-facade", "Facade", "Structurel",
         "Expose une interface simple à un sous-système complexe.",
         "Démarrer l'app nécessite 8 services initialisés dans le bon ordre.",
         "`AppFacade.start()` cache config, DB, cache, queue derrière une méthode.",
         "Réception d'hôtel : une clé, pas besoin de connaître chaque service interne."),
        ("design-patterns-flyweight", "Flyweight", "Structurel",
         "Partage l'état intrinsèque entre many objets pour économiser la mémoire.",
         "10 000 arbres dans un jeu : position unique, texture partagée.",
         "Factory de flyweights + état extrinsèque passé à l'exécution.",
         "Bibliothèque : un exemplaire du livre, plusieurs lecteurs avec leur page courante."),
        ("design-patterns-proxy", "Proxy", "Structurel",
         "Surrogate contrôlant l'accès à un objet (lazy load, cache, sécurité).",
         "Image lourde chargée seulement quand elle entre dans le viewport.",
         "Même interface que le réel ; le proxy décide quand déléguer.",
         "Secrétaire qui filtre les appels avant le directeur."),
        ("design-patterns-chain-of-responsibility", "Chain of Responsibility", "Comportemental",
         "Passe une requête le long d'une chaîne de handlers jusqu'à ce que l'un la traite.",
         "Middleware HTTP : auth, log, rate limit, handler métier.",
         "Chaque maillon implémente `handle(req)` et appelle `next` ou stop.",
         "Support technique : niveau 1 → 2 → expert."),
        ("design-patterns-command", "Command", "Comportemental",
         "Encapsule une action en objet : undo, queue, macro.",
         "Éditeur avec Ctrl+Z : chaque action est un objet `Command` avec `execute` / `undo`.",
         "Invocateur ne connaît que l'interface Command, pas les détails.",
         "Commande au restaurant : le serveur note, la cuisine exécute plus tard."),
        ("design-patterns-iterator", "Iterator", "Comportemental",
         "Parcourt une collection sans exposer sa structure interne.",
         "Liste chaînée, arbre, tableau : le client utilise `for (const x of iterable)`.",
         "Interface `Iterator` avec `next()` / `hasNext()` ou protocole natif du langage.",
         "Télécommande chaînes : suivant/précédent sans voir la liste interne."),
        ("design-patterns-mediator", "Mediator", "Comportemental",
         "Centralise les communications chaotiques entre objets dans un médiateur.",
         "Formulaire : 10 champs qui se désactivent mutuellement — évite N×N liens.",
         "Les composants parlent au `FormMediator`, pas entre eux directement.",
         "Tour de contrôle aérien : les avions ne se coordonnent pas tous à tous."),
        ("design-patterns-memento", "Memento", "Comportemental",
         "Sauvegarde et restaure l'état interne d'un objet sans violer l'encapsulation.",
         "Checkpoint dans un jeu ou brouillon d'éditeur.",
         "`Originator` crée un `Memento` ; `Caretaker` stocke l'historique.",
         "Ctrl+S : snapshot invisible de l'état du document."),
        ("design-patterns-observer", "Observer", "Comportemental",
         "Notification automatique des dépendants quand l'état d'un sujet change.",
         "Stock qui baisse → alerte email + push + dashboard.",
         "`Subject.subscribe(observer)` ; `notify()` sur changement.",
         "Newsletter : tu t'abonnes, tu reçois les nouveautés."),
        ("design-patterns-state", "State", "Comportemental",
         "Change le comportement d'un objet selon son état interne.",
         "Commande : brouillon → payée → expédiée ; chaque état a ses actions autorisées.",
         "Classes `DraftState`, `PaidState` au lieu d'un switch géant.",
         "Distributeur : pas de soda si pas payé — l'état décide."),
        ("design-patterns-strategy", "Strategy", "Comportemental",
         "Famille d'algorithmes interchangeables injectés au runtime.",
         "Calcul de livraison : express, standard, point relais.",
         "Interface `ShippingStrategy` ; le contexte reçoit la stratégie.",
         "GPS : mode voiture / vélo / piéton change l'itinéraire."),
        ("design-patterns-template-method", "Template Method", "Comportemental",
         "Squelette d'algorithme dans une classe de base ; étapes précises aux sous-classes.",
         "Pipeline ETL : extract et load communs, transform spécifique.",
         "Méthode `process()` appelle des hooks `step1()`, `step2()` overridables.",
         "Recette de cuisine : étapes fixes, épices variables."),
        ("design-patterns-visitor", "Visitor", "Comportemental",
         "Sépare les opérations sur une structure d'objets de la structure elle-même.",
         "Exporter AST en HTML, PDF, lint — sans modifier chaque nœud.",
         "Double dispatch : `node.accept(visitor)`.",
         "Inspecteur bâtiment : même visite, rapports différents par expert."),
        ("design-patterns-interpreter", "Interpreter", "Comportemental",
         "Définit une grammaire et interprète des phrases du langage.",
         "Règles métier simples type « SI age > 18 ET pays = FR ».",
         "Arbre d'expressions avec `interpret(context)`.",
         "Calculatrice avec + et * : chaque symbole est une classe."),
    ]
    items = list(PATTERNS_DATA)
    for slug, name, fam, one, problem, idea, analogy in extra:
        items.append({
            "slug": slug,
            "name": name,
            "family_fr": fam,
            "one_liner": one,
            "problem": problem,
            "idea": idea,
            "analogy": analogy,
            "ts_example": f"```typescript\n// {name} — adapte ce squelette à ton domaine\ninterface {name.replace(' ', '')}Role {{\n  execute(): void;\n}}\n```",
            "py_example": f"```python\n# {name} — même logique côté Python\nclass {name.replace(' ', '')}Role(ABC):\n    @abstractmethod\n    def execute(self) -> None: ...\n```",
            "when_use": f"- Le problème décrit dans « Le problème » correspond à ton cas.\n- Tu anticipes plusieurs variantes sans `if` géants.",
            "when_not": "- Sur-ingénierie sur un script de 50 lignes.\n- Une librairie standard fait déjà le travail (ex. `itertools`, middleware framework).",
            "mistakes": "- Copier le pattern sans comprendre le problème.\n- Mélanger responsabilités (ex. Observer qui fait aussi persistance DB).",
            "related": "- Voir les articles de la même famille dans la série.\n- Compare avec les patterns listés en intro.",
            "exercise": f"Identifie dans un projet open source un usage probable de {name}. Note le fichier et explique en 5 lignes pourquoi c'est ce pattern.",
            "summary": f"{name} : {one}",
        })
    return items


def link(slug: str, label: str) -> str:
    return f"[{label}](/blog/articles/{slug})"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    slugs_order = [
        "design-patterns-introduction-gang-of-four",
        *[p["slug"] for p in all_patterns()],
    ]
    # Intro
    intro_path = OUT / "design-patterns-introduction-gang-of-four.md"
    intro_path.write_text(
        fm(
            "Introduction aux Design Patterns : guide Gang of Four pour juniors",
            "Comprendre ce qu'est un design pattern, les 3 familles GoF, comment lire la série et éviter les pièges classiques avant d'attaquer chaque pattern en détail.",
            1,
            "design-patterns-introduction-gang-of-four",
            ["Design Patterns", "GoF", "junior", "SOLID", "architecture"],
            DATE_START,
        )
        + INTRO,
        encoding="utf-8",
    )
    print(intro_path.name)

    patterns = all_patterns()
    for i, p in enumerate(patterns, start=2):
        from datetime import datetime, timedelta

        d = (datetime.strptime(DATE_START, "%Y-%m-%d") + timedelta(days=i - 1)).strftime(
            "%Y-%m-%d"
        )
        prev_slug = slugs_order[i - 2] if i > 1 else slugs_order[0]
        next_slug = slugs_order[i] if i < len(slugs_order) else slugs_order[-1]
        prev = link(prev_slug, "article précédent")
        next_ = link(next_slug, "article suivant")
        content = pattern_article(
            order=i,
            slug=p["slug"],
            name=p["name"],
            family=p["family_fr"],
            family_fr=p["family_fr"],
            date=d,
            one_liner=p["one_liner"],
            problem=p["problem"],
            idea=p["idea"],
            analogy=p["analogy"],
            ts_example=p["ts_example"],
            py_example=p["py_example"],
            when_use=p["when_use"],
            when_not=p["when_not"],
            mistakes=p["mistakes"],
            related=p["related"],
            exercise=p["exercise"],
            summary=p["summary"],
            prev_link=prev,
            next_link=next_,
        )
        path = OUT / f"{p['slug']}.md"
        path.write_text(content, encoding="utf-8")
        print(path.name)


if __name__ == "__main__":
    main()
