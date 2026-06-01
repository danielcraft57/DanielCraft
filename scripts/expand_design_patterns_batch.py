#!/usr/bin/env python3
"""Réécrit les articles design patterns avec contenu long et exemples réels."""

from __future__ import annotations

from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "blog" / "content" / "articles"

NAV = {
    "design-patterns-singleton": ("design-patterns-introduction-gang-of-four", "design-patterns-factory-method"),
    "design-patterns-factory-method": ("design-patterns-singleton", "design-patterns-abstract-factory"),
    "design-patterns-abstract-factory": ("design-patterns-factory-method", "design-patterns-builder"),
    "design-patterns-builder": ("design-patterns-abstract-factory", "design-patterns-prototype"),
    "design-patterns-prototype": ("design-patterns-builder", "design-patterns-adapter"),
    "design-patterns-adapter": ("design-patterns-prototype", "design-patterns-bridge"),
    "design-patterns-bridge": ("design-patterns-adapter", "design-patterns-composite"),
    "design-patterns-composite": ("design-patterns-bridge", "design-patterns-decorator"),
    "design-patterns-decorator": ("design-patterns-composite", "design-patterns-facade"),
    "design-patterns-facade": ("design-patterns-decorator", "design-patterns-flyweight"),
    "design-patterns-flyweight": ("design-patterns-facade", "design-patterns-proxy"),
    "design-patterns-proxy": ("design-patterns-flyweight", "design-patterns-chain-of-responsibility"),
    "design-patterns-chain-of-responsibility": ("design-patterns-proxy", "design-patterns-command"),
    "design-patterns-command": ("design-patterns-chain-of-responsibility", "design-patterns-iterator"),
    "design-patterns-iterator": ("design-patterns-command", "design-patterns-mediator"),
    "design-patterns-mediator": ("design-patterns-iterator", "design-patterns-memento"),
    "design-patterns-memento": ("design-patterns-mediator", "design-patterns-observer"),
    "design-patterns-observer": ("design-patterns-memento", "design-patterns-state"),
    "design-patterns-state": ("design-patterns-observer", "design-patterns-strategy"),
    "design-patterns-strategy": ("design-patterns-state", "design-patterns-template-method"),
    "design-patterns-template-method": ("design-patterns-strategy", "design-patterns-visitor"),
    "design-patterns-visitor": ("design-patterns-template-method", "design-patterns-interpreter"),
    "design-patterns-interpreter": ("design-patterns-visitor", "design-patterns-interpreter"),
}


def fm(order: int, slug: str, title: str, excerpt: str, name: str, fam: str, date: str) -> str:
    return f"""---
title: "{title}"
date: {date}
excerpt: "{excerpt}"
type: article
tags: [Design Patterns, GoF, {name}, {fam}, TypeScript, Python, junior]
og_image: {slug}-1200x630.jpg
series: design-patterns-serie
series_order: {order}
---

"""


def nav_footer(slug: str) -> str:
    prev_s, next_s = NAV.get(slug, (slug, slug))
    return f"""
---

## Navigation dans la série

- Précédent : [{prev_s.replace('design-patterns-', '').replace('-', ' ').title()}](/blog/articles/{prev_s})
- Suivant : [{next_s.replace('design-patterns-', '').replace('-', ' ').title()}](/blog/articles/{next_s})
"""


def write_article(slug: str, order: int, date: str, name: str, fam: str, excerpt: str, body: str) -> None:
    title = f"{name} : pattern {fam.lower()} expliqué pour juniors"
    svg = "dp-" + slug.replace("design-patterns-", "") + ".svg"
    header = f"""# {name} : comprendre et appliquer le pattern

**Famille :** {fam} · **Série :** Design Patterns GoF · **Article {order}/24**

{excerpt}

<figure>
  <img src="../../assets/images/blog/{svg}" alt="Schéma {name}" class="schema-inline" width="400" />
  <figcaption>Vue simplifiée du pattern {name}.</figcaption>
</figure>

"""
    path = OUT / f"{slug}.md"
    path.write_text(fm(order, slug, title, excerpt, name, fam, date) + header + body + nav_footer(slug), encoding="utf-8")
    print(f"{path.name}: {len(path.read_text(encoding='utf-8').splitlines())} lines")


# Corps détaillés — Strategy (exemple de gabarit riche)
STRATEGY_BODY = """
---

## En une phrase

Le pattern **Strategy** encapsule une famille d'algorithmes interchangeables et permet au client de choisir l'implémentation au runtime sans `switch` géant.

---

## Le problème sans ce pattern

Tu calcules le prix de livraison :

```typescript
function shipping(cost: number, mode: string) {
  if (mode === 'express') return cost + 15;
  if (mode === 'standard') return cost + 5;
  if (mode === 'pickup') return 0;
  throw new Error('mode inconnu');
}
```

Chaque nouveau mode (point relais, livraison verte) force à modifier cette fonction — risque de régression sur les modes existants.

---

## L'idée du pattern Strategy

- Définir une interface `ShippingStrategy` avec `compute(cost)`.
- Implémenter `ExpressStrategy`, `StandardStrategy`, etc.
- Le contexte (`Checkout`) reçoit la stratégie par **injection** (constructeur ou setter).

### Analogie

Choisir un **itinéraire GPS** : voiture, vélo, piéton. L'objectif (arriver au point B) est le même ; l'algorithme change.

---

## Exemple TypeScript (checkout e-commerce)

```typescript
interface ShippingStrategy {
  readonly label: string;
  compute(baseCost: number): number;
}

class ExpressShipping implements ShippingStrategy {
  readonly label = 'Express 24h';
  compute(baseCost: number) {
    return baseCost + 15;
  }
}

class StandardShipping implements ShippingStrategy {
  readonly label = 'Standard 3-5j';
  compute(baseCost: number) {
    return baseCost + 5;
  }
}

class PickupShipping implements ShippingStrategy {
  readonly label = 'Retrait magasin';
  compute(baseCost: number) {
    return 0;
  }
}

class Checkout {
  constructor(private strategy: ShippingStrategy) {}

  setStrategy(strategy: ShippingStrategy) {
    this.strategy = strategy;
  }

  total(cart: number) {
    const shipping = this.strategy.compute(cart);
    return { shipping, total: cart + shipping, label: this.strategy.label };
  }
}

const checkout = new Checkout(new StandardShipping());
console.log(checkout.total(100));
checkout.setStrategy(new ExpressShipping());
console.log(checkout.total(100));
```

---

## Exemple Python

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass

class ShippingStrategy(ABC):
    label: str

    @abstractmethod
    def compute(self, base_cost: float) -> float: ...

@dataclass
class ExpressShipping(ShippingStrategy):
    label: str = 'Express'

    def compute(self, base_cost: float) -> float:
        return base_cost + 15

@dataclass
class StandardShipping(ShippingStrategy):
    label: str = 'Standard'

    def compute(self, base_cost: float) -> float:
        return base_cost + 5

class Checkout:
    def __init__(self, strategy: ShippingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: ShippingStrategy) -> None:
        self.strategy = strategy

    def total(self, cart: float) -> dict:
        shipping = self.strategy.compute(cart)
        return {'shipping': shipping, 'total': cart + shipping, 'label': self.strategy.label}
```

---

## Strategy vs State

| | Strategy | State |
|---|----------|-------|
| But | Choisir un **algorithme** | Changer de **comportement** selon l'état interne |
| Qui change | Souvent le client / config | Transitions automatiques |
| Exemple | Mode de livraison | Commande payée → expédiée |

---

## Quand utiliser Strategy

- Variantes d'un même calcul ou traitement.
- Tu veux tester chaque algorithme isolément.
- Configuration utilisateur (thème, tri, export PDF/CSV).

---

## Quand ne pas l'utiliser

- Une seule implémentation, stable depuis 2 ans.
- Deux lignes de logique — une fonction suffit.

---

## Erreurs fréquentes des juniors

- Créer une classe Strategy par `if` existant sans simplifier le client.
- Oublier d'injecter la stratégie (et instancier en dur dans le contexte).
- Confondre avec **Template Method** (squelette fixe en classe de base).

---

## Exercice

Implémente `SortStrategy` : `byPrice`, `byName`, `byRating` sur un tableau de produits. Le composant liste ne doit contenir aucun `switch` sur le critère de tri.

---

## Résumé

Strategy = algorithmes plugables. Tu gagnes en **Open/Closed** et en testabilité. C'est l'un des patterns les plus utiles au quotidien.
"""

DECORATOR_BODY = """
---

## En une phrase

**Decorator** enveloppe un objet pour lui ajouter des comportements dynamiquement, sans sous-classer ni modifier la classe d'origine.

---

## Le problème

Tu as `FileReader` et tu veux : buffer, compression, chiffrement — dans n'importe quel ordre. Hériter `BufferedCompressedEncryptedReader` explose le nombre de classes.

---

## L'idée

Chaque décorateur implémente la même interface que le composant et **délègue** au wrapper interne après avoir ajouté sa couche.

### Analogie

Gâteau : génoise → crème → glaçage. Chaque couche s'ajoute sans refaire la recette de base.

---

## TypeScript : flux de données

```typescript
interface DataSource {
  write(data: string): void;
  read(): string;
}

class FileSource implements DataSource {
  constructor(private path: string, private content = '') {}
  write(data: string) { this.content += data; }
  read() { return this.content; }
}

abstract class DataSourceDecorator implements DataSource {
  constructor(protected wrappee: DataSource) {}
  write(data: string) { this.wrappee.write(data); }
  read() { return this.wrappee.read(); }
}

class EncryptionDecorator extends DataSourceDecorator {
  write(data: string) {
    super.write(btoa(data));
  }
  read() {
    return atob(super.read());
  }
}

class CompressionDecorator extends DataSourceDecorator {
  write(data: string) {
    super.write(data.replace(/(.)\1+/g, '$1')); // démo simpliste
  }
}

let source: DataSource = new FileSource('out.txt');
source = new CompressionDecorator(source);
source = new EncryptionDecorator(source);
source.write('hello');
console.log(source.read());
```

---

## Python

```python
class DataSource(ABC):
    @abstractmethod
    def read(self) -> str: ...
    @abstractmethod
    def write(self, data: str) -> None: ...

class FileSource(DataSource):
    def __init__(self):
        self._buf = ''
    def write(self, data: str) -> None:
        self._buf += data
    def read(self) -> str:
        return self._buf

class EncryptionDecorator(DataSource):
    def __init__(self, wrappee: DataSource):
        self._w = wrappee
    def write(self, data: str) -> None:
        import base64
        self._w.write(base64.b64encode(data.encode()).decode())
    def read(self) -> str:
        import base64
        return base64.b64decode(self._w.read().encode()).decode()
```

---

## Decorator vs Adapter vs Proxy

| Pattern | Rôle |
|---------|------|
| Decorator | Ajoute une **responsabilité** |
| Adapter | Change l'**interface** |
| Proxy | Contrôle l'**accès** (lazy, cache) |

---

## Quand l'utiliser

- Empiler des options (streams Java/Node, middleware).
- UI : HOC React qui « décore » un composant.

---

## Pièges

- Trop de couches = debug difficile — loggue la chaîne.
- Ne pas respecter Liskov : le décorateur doit rester substituable.

---

## Exercice

Enveloppe `Coffee` : `MilkDecorator`, `SugarDecorator`, chacun ajoute un prix. Commande `Espresso` + lait + sucre.

---

## Résumé

Decorator = composition dynamique de comportements. Alternative propre à l'héritage multiple de features.
"""

def mk_body(
    one: str,
    problem: str,
    idea: str,
    analogy: str,
    ts: str,
    py: str,
    use: str,
    not_use: str,
    mistakes: str,
    related: str,
    exercise: str,
    summary: str,
) -> str:
    return f"""
---

## En une phrase

{one}

---

## Le problème sans ce pattern

{problem}

---

## L'idée du pattern

{idea}

### Analogie du quotidien

{analogy}

---

## Exemple en TypeScript

{ts}

---

## Exemple en Python

{py}

---

## Quand l'utiliser

{use}

---

## Quand ne pas l'utiliser

{not_use}

---

## Erreurs fréquentes des juniors

{mistakes}

---

## Patterns proches

{related}

---

## Pas à pas : comment l'implémenter

1. **Nomme le problème** — est-ce vraiment ce pattern ou un simple refactor ?
2. **Définis les interfaces** — ce que le client voit vs les implémentations.
3. **Écris un test** — comportement attendu avant la structure « pattern ».
4. **Implémente une variante** — une seule suffit pour valider.
5. **Documente en équipe** — « ici on utilise X parce que… ».

---

## Cas réel en entreprise

Tu retrouveras ce pattern dans des frameworks que tu utilises déjà : middleware web, composants UI, ORM, pipelines CI. En entretien, explique le **problème** avant le nom du pattern — c'est ce qui marque les juniors matures.

---

## Checklist code review

- [ ] Le client ne dépend pas de classes concrètes inutiles
- [ ] Pas de sur-abstraction sur un cas unique
- [ ] Tests unitaires sur chaque variante / handler / état
- [ ] Nommage métier clair (pas seulement `AbstractFactoryImpl`)

---

## Exercice pratique (20–30 min)

{exercise}

---

## Résumé

{summary}
"""


def ts_block(code: str) -> str:
    return "```typescript\n" + code.strip() + "\n```"


def py_block(code: str) -> str:
    return "```python\n" + code.strip() + "\n```"


# (slug, order, date, name, family, excerpt, body via mk_body)
_META = [
    ("design-patterns-singleton", 2, "2026-04-02", "Singleton", "Créationnel",
     "Une seule instance partagée avec point d'accès contrôlé — utile pour config et logger, dangereux comme variable globale déguisée."),
    ("design-patterns-factory-method", 3, "2026-04-03", "Factory Method", "Créationnel",
     "Délègue la création d'objets aux sous-classes pour supprimer les if/else de type partout dans le client."),
    ("design-patterns-abstract-factory", 4, "2026-04-04", "Abstract Factory", "Créationnel",
     "Crée des familles d'objets cohérents (UI Mac/Windows) sans mélanger les kits dans le code client."),
    ("design-patterns-builder", 5, "2026-04-05", "Builder", "Créationnel",
     "Construit des objets complexes étape par étape (SQL, burgers, configs) sans constructeurs à 15 paramètres."),
    ("design-patterns-prototype", 6, "2026-04-06", "Prototype", "Créationnel",
     "Clone des objets existants au lieu de recréer depuis zéro — pratique pour templates et configs lourdes."),
    ("design-patterns-adapter", 7, "2026-04-07", "Adapter", "Structurel",
     "Fait collaborer une API existante avec ton interface attendue — le pont entre legacy et code moderne."),
    ("design-patterns-bridge", 8, "2026-04-08", "Bridge", "Structurel",
     "Sépare abstraction et implémentation pour qu'elles évoluent sans explosion combinatoire de classes."),
    ("design-patterns-composite", 9, "2026-04-09", "Composite", "Structurel",
     "Traite feuilles et conteneurs uniformément — menus, dossiers, scènes de jeu."),
    ("design-patterns-facade", 11, "2026-04-11", "Facade", "Structurel",
     "Interface simple au-dessus d'un sous-système complexe — démarrage app, SDK paiement."),
    ("design-patterns-flyweight", 12, "2026-04-12", "Flyweight", "Structurel",
     "Partage l'état intrinsèque pour des milliers d'objets similaires — jeux, éditeurs de texte."),
    ("design-patterns-proxy", 13, "2026-04-13", "Proxy", "Structurel",
     "Substitut contrôlant l'accès : lazy load, cache, permissions, logging."),
    ("design-patterns-chain-of-responsibility", 14, "2026-04-14", "Chain of Responsibility", "Comportemental",
     "Chaîne de handlers qui traitent ou transmettent une requête — middleware HTTP."),
    ("design-patterns-command", 15, "2026-04-15", "Command", "Comportemental",
     "Encapsule une action en objet pour undo, redo, files d'attente et macros."),
    ("design-patterns-iterator", 16, "2026-04-16", "Iterator", "Comportemental",
     "Parcourt une collection sans exposer sa structure interne."),
    ("design-patterns-mediator", 17, "2026-04-17", "Mediator", "Comportemental",
     "Centralise les échanges entre composants pour éviter le maillage N×N."),
    ("design-patterns-memento", 18, "2026-04-18", "Memento", "Comportemental",
     "Sauvegarde et restaure l'état sans casser l'encapsulation — undo, checkpoints."),
    ("design-patterns-state", 20, "2026-04-20", "State", "Comportemental",
     "Comportement qui change avec l'état interne — workflow commande, machine à états."),
    ("design-patterns-template-method", 22, "2026-04-22", "Template Method", "Comportemental",
     "Squelette d'algorithme fixe, étapes variables en sous-classes — pipelines ETL."),
    ("design-patterns-visitor", 23, "2026-04-23", "Visitor", "Comportemental",
     "Ajoute des opérations sur une structure sans modifier chaque classe de nœud."),
    ("design-patterns-interpreter", 24, "2026-04-24", "Interpreter", "Comportemental",
     "Grammaire + arbre d'interprétation pour des langages mini (règles, expressions)."),
]


def _bodies() -> dict[str, str]:
    """Contenu détaillé par slug."""
    S = ts_block
    P = py_block
    return {
        "design-patterns-singleton": mk_body(
            "Le Singleton garantit une unique instance et un accès global contrôlé.",
            "Plusieurs `new Config()` chargent le fichier .env plusieurs fois ; les flags divergent entre modules.",
            "Constructeur privé + `getInstance()` lazy. En TS moderne, parfois remplacé par un module ES unique.",
            "Un seul maire par ville : on ne crée pas un nouveau maire pour chaque formulaire.",
            S("""class AppConfig {
  private static inst: AppConfig | null = null;
  private constructor(public apiUrl: string) {}
  static getInstance(): AppConfig {
    if (!this.inst) this.inst = new AppConfig(process.env.API_URL!);
    return this.inst;
  }
}
const a = AppConfig.getInstance();
const b = AppConfig.getInstance();
console.log(a === b);"""),
            P("""class AppConfig:
    _inst = None
    def __init__(self, api_url: str):
        self.api_url = api_url
    @classmethod
    def get(cls):
        if cls._inst is None:
            cls._inst = cls('https://api.example.com')
        return cls._inst"""),
            "- Vraie ressource unique (pool, identifiant machine).\n- Coût d'init élevé partagé.",
            "- Tests unitaires (état global).\n- Plusieurs instances légitimes (panier par user).",
            "- Singleton par défaut partout.\n- Stocker toute l'app dedans (God Object).",
            "- **Factory** pour création.\n- Injection de dépendances.",
            "Remplace ton Singleton par injection de `Config` en paramètre ; compare les tests.",
            "Une instance, un accès — à utiliser avec parcimonie.",
        ),
        "design-patterns-factory-method": mk_body(
            "La Factory Method délègue la création aux sous-classes.",
            "Des `if (type==='pdf')` partout pour instancier des exporteurs.",
            "Classe créatrice abstraite avec `createExporter()` ; sous-classes retournent le bon produit.",
            "Restaurant : tu commandes le plat, la cuisine choisit la recette du jour.",
            S("""abstract class ExportService {
  protected abstract createExporter(): { export(d: unknown): string };
  run(data: unknown) { return this.createExporter().export(data); }
}
class PdfService extends ExportService {
  protected createExporter() {
    return { export: (d) => 'PDF:' + JSON.stringify(d) };
  }
}"""),
            P("""class ExportService(ABC):
    @abstractmethod
    def create_exporter(self): ...
    def run(self, data):
        return self.create_exporter().export(data)"""),
            "- Type de produit dépend du contexte.\n- Extension par nouvelle sous-classe.",
            "- Un seul produit pour toujours.",
            "- Confondre avec Abstract Factory.\n- Hiérarchie trop profonde pour 2 cas.",
            "- **Abstract Factory**, **Simple Factory**.",
            "Notifications Email/SMS/Push : ajoute Slack sans modifier `sendAlert()`.",
            "Création polymorphe via sous-classes — Open/Closed.",
        ),
        "design-patterns-abstract-factory": mk_body(
            "L'Abstract Factory produit des familles d'objets cohérents.",
            "Tu mélanges `MacButton` avec `WinCheckbox` par erreur.",
            "`UIFactory` expose `createButton()` + `createCheckbox()` ; `MacFactory` et `WinFactory` restent cohérents.",
            "Kit meuble : toutes les vis et planches du même carton.",
            S("""interface Button { render(): string }
interface Checkbox { render(): string }
interface UIFactory {
  createButton(): Button;
  createCheckbox(): Checkbox;
}
class MacFactory implements UIFactory {
  createButton() { return { render: () => 'MacBtn' }; }
  createCheckbox() { return { render: () => 'MacChk' }; }
}
function renderForm(f: UIFactory) {
  console.log(f.createButton().render(), f.createCheckbox().render());
}"""),
            P("""class MacFactory:
    def create_button(self): return 'MacBtn'
    def create_checkbox(self): return 'MacChk'"""),
            "- Familles d'objets liés (UI, DB drivers).\n- Cohérence obligatoire.",
            "- Un seul produit isolé → Factory Method.",
            "- Une factory géante pour tout l'app.",
            "- **Factory Method** (un produit).\n- **Builder** (étapes).",
            "Deux thèmes complets dark/light pour une app fictive.",
            "Familles cohérentes, pas des pièces mélangées.",
        ),
        "design-patterns-builder": mk_body(
            "Le Builder construit un objet complexe par étapes fluides.",
            "Constructeur `User(a,b,c,d,e,f)` illisible ; paramètres optionnels chaos.",
            "`QueryBuilder.select().from().where()` retourne `this` jusqu'à `build()`.",
            "Composer un burger garniture par garniture.",
            S("""class QueryBuilder {
  private parts: string[] = [];
  select(cols: string) { this.parts.push('SELECT ' + cols); return this; }
  from(table: string) { this.parts.push('FROM ' + table); return this; }
  where(cond: string) { this.parts.push('WHERE ' + cond); return this; }
  build() { return this.parts.join(' '); }
}
const sql = new QueryBuilder().select('*').from('users').where('active=1').build();"""),
            P("""class QueryBuilder:
    def __init__(self):
        self.parts = []
    def select(self, cols):
        self.parts.append(f'SELECT {cols}'); return self
    def build(self):
        return ' '.join(self.parts)"""),
            "- Nombreux paramètres optionnels.\n- Ordre de construction libre.",
            "- Objet simple 2-3 champs.",
            "- Oublier `build()` immuable.\n- Builder avec logique métier lourde.",
            "- **Abstract Factory**.\n- Records/dataclasses.",
            "Builder pour `Email` : to, cc, subject, body, attachments.",
            "Construction lisible, objet final cohérent.",
        ),
        "design-patterns-prototype": mk_body(
            "Le Prototype clone un exemplaire au lieu d'appeler `new` coûteux.",
            "Recharger un template 10 Mo depuis la DB à chaque copie utilisateur.",
            "`clone()` copie l'état ; registre de prototypes par clé.",
            "Photocopieuse : dupliquer la feuille modèle.",
            S("""interface Prototype { clone(): Prototype }
class DocumentTemplate implements Prototype {
  constructor(public title: string, public blocks: string[]) {}
  clone() { return new DocumentTemplate(this.title, [...this.blocks]); }
}
const registry = new Map<string, Prototype>();
registry.set('invoice', new DocumentTemplate('Facture', ['header','lines']));
const copy = registry.get('invoice')!.clone();"""),
            P("""import copy
class DocumentTemplate:
    def __init__(self, title, blocks):
        self.title, self.blocks = title, blocks
    def clone(self):
        return copy.deepcopy(self)"""),
            "- Coût de création élevé.\n- Beaucoup d'objets similaires.",
            "- Clone plus cher que `new` simple.",
            "- Clone superficiel vs profond confondu.",
            "- **Factory Method**.\n- Serialization.",
            "Registre de 3 modèles de contrat clonables.",
            "Copier intelligemment, pas reconstruire.",
        ),
        "design-patterns-adapter": mk_body(
            "L'Adapter convertit une interface incompatible.",
            "API legacy XML ; ton code attend du JSON typé.",
            "Wrapper implémente ton port et traduit vers le service legacy.",
            "Adaptateur de prise EU vers US.",
            S("""interface PaymentPort { pay(euros: number): boolean }
class StripeApi { charge(cents: number) { return cents > 0; } }
class StripeAdapter implements PaymentPort {
  constructor(private stripe: StripeApi) {}
  pay(euros: number) { return this.stripe.charge(Math.round(euros * 100)); }
}"""),
            P("""class StripeAdapter:
    def __init__(self, stripe):
        self.stripe = stripe
    def pay(self, euros):
        return self.stripe.charge(int(euros * 100))"""),
            "- Intégration tierce.\n- Migration progressive.",
            "- Tu contrôles déjà l'API → change l'API.",
            "- Adapter qui devient God Object.",
            "- **Facade** (simplifier).\n- **Bridge**.",
            "Adapter une fausse API météo vers ton interface `WeatherService`.",
            "Traduction d'interface, pas de logique métier.",
        ),
        "design-patterns-bridge": mk_body(
            "Le Bridge découple abstraction et implémentation.",
            "Formes × Renderers = 6 classes (CircleSvg, CircleCanvas…).",
            "`Shape` contient un `Renderer` injecté.",
            "Télécommande et TV : changer l'un sans refabriquer l'autre.",
            S("""interface Renderer { drawCircle(): void }
class SvgRenderer implements Renderer { drawCircle() { console.log('svg'); } }
abstract class Shape {
  constructor(protected renderer: Renderer) {}
  abstract draw(): void;
}
class Circle extends Shape {
  draw() { this.renderer.drawCircle(); }
}"""),
            P("""class Shape:
    def __init__(self, renderer):
        self.renderer = renderer"""),
            "- Deux axes de variation indépendants.\n- Évolution séparée.",
            "- Une seule implémentation stable.",
            "- Confondre avec Adapter.",
            "- **Strategy** (algorithme).\n- **Adapter**.",
            "Shapes + 2 renderers ; ajoute Square sans doubler les renderers.",
            "Composition > multiplication de classes.",
        ),
        "design-patterns-composite": mk_body(
            "Le Composite compose objets en arbres traités uniformément.",
            "Menu avec sous-menus : `render()` doit marcher partout.",
            "Interface `Component` ; `Leaf` et `Composite` avec `operation()`.",
            "Dossier fichiers : fichier et dossier ont `getSize()`.",
            S("""interface Component { getPrice(): number }
class Product implements Component {
  constructor(private price: number) {}
  getPrice() { return this.price; }
}
class Box implements Component {
  private children: Component[] = [];
  add(c: Component) { this.children.push(c); }
  getPrice() { return this.children.reduce((s, c) => s + c.getPrice(), 0); }
}"""),
            P("""class Box:
    def __init__(self):
        self.children = []
    def add(self, c):
        self.children.append(c)
    def price(self):
        return sum(c.price() for c in self.children)"""),
            "- Structures arborescentes.\n- Opération commune feuille/nœud.",
            "- Liste plate suffit.",
            "- Enfants modifiés sans contrôle.",
            "- **Decorator** (empiler features).\n- **Iterator**.",
            "Menu restaurant 2 niveaux avec prix total.",
            "Un traitement pour tout l'arbre.",
        ),
        "design-patterns-facade": mk_body(
            "La Facade expose une API simple à un sous-système.",
            "`startApp()` doit init config, DB, cache, queue dans le bon ordre.",
            "`AppFacade.start()` cache la complexité.",
            "Réception d'hôtel : une clé pour tout.",
            S("""class Config { load() {} }
class Database { connect() {} }
class AppFacade {
  start() {
    new Config().load();
    new Database().connect();
    console.log('App ready');
  }
}"""),
            P("""class AppFacade:
    def start(self):
        Config().load()
        Database().connect()"""),
            "- Sous-système complexe.\n- Point d'entrée unique pour juniors.",
            "- Ajouter une couche sans valeur.",
            "- Facade qui contient toute la logique métier.",
            "- **Adapter**.\n- Modules ES.",
            "Facade `Checkout` : stock, paiement, email.",
            "Simplifier l'usage, pas cacher un mauvais design partout.",
        ),
        "design-patterns-flyweight": mk_body(
            "Le Flyweight partage l'état intrinsèque entre instances.",
            "10 000 arbres : même texture, positions différentes.",
            "Factory de flyweights ; état extrinsèque passé aux méthodes.",
            "Une partition de piano partagée, notes différentes par pianiste.",
            S("""class TreeType { constructor(public name: string, public color: string) {} }
class TreeFactory {
  private cache = new Map<string, TreeType>();
  get(name: string, color: string) {
    const key = name + color;
    if (!this.cache.has(key)) this.cache.set(key, new TreeType(name, color));
    return this.cache.get(key)!;
  }
}
class Tree {
  constructor(public type: TreeType, public x: number, public y: number) {}
}"""),
            P("""class TreeFactory:
    _cache = {}
    def get(self, name, color):
        key = (name, color)
        return self._cache.setdefault(key, (name, color))"""),
            "- Très nombreux objets similaires.\n- Mémoire critique.",
            "- Peu d'instances.\n- Extrinsèque mal séparé.",
            "- Tout mettre dans le flyweight.",
            "- **Singleton** (une instance).\n- Cache simple.",
            "1000 icônes « star » partagent la même définition SVG.",
            "Mémoire : partager ce qui ne change pas.",
        ),
        "design-patterns-proxy": mk_body(
            "Le Proxy contrôle l'accès à un objet réel.",
            "Image 4 Mo : charger seulement si visible.",
            "Même interface ; proxy décide quand déléguer.",
            "Secrétaire filtre les appels au directeur.",
            S("""interface Image { display(): void }
class RealImage implements Image {
  constructor(private src: string) { console.log('load', src); }
  display() { console.log('show'); }
}
class LazyImageProxy implements Image {
  private real: RealImage | null = null;
  constructor(private src: string) {}
  display() {
    if (!this.real) this.real = new RealImage(this.src);
    this.real.display();
  }
}"""),
            P("""class LazyImageProxy:
    def __init__(self, src):
        self.src, self.real = src, None
    def display(self):
        if self.real is None:
            self.real = RealImage(self.src)
        self.real.display()"""),
            "- Lazy load, cache, droits, logging.",
            "- Pas de contrôle d'accès nécessaire.",
            "- Proxy ≠ Decorator (intention différente).",
            "- **Decorator**.\n- **Facade**.",
            "Proxy cache sur `fetchUser` (TTL 5 min).",
            "Surrogate avec même interface.",
        ),
        "design-patterns-chain-of-responsibility": mk_body(
            "La chaîne passe une requête de handler en handler.",
            "Middleware : auth, rate limit, log, puis route.",
            "Chaque maillon appelle `next()` ou stop.",
            "Support niveau 1 → 2 → expert.",
            S("""type Context = { user?: string; body: string };
type Handler = (ctx: Context, next: () => void) => void;
function chain(...handlers: Handler[]) {
  let i = 0;
  const next = () => { if (i < handlers.length) handlers[i++](ctx, next); };
  const ctx: Context = { body: '' };
  next();
}"""),
            P("""def auth(ctx, n):
    if not ctx.get('user'): raise Error('401')
    n()"""),
            "- Ordre de traitement flexible.\n- Plusieurs traitements optionnels.",
            "- Chaîne fixe simple → liste de fonctions.",
            "- Oublier d'appeler `next`.",
            "- **Decorator** (empilement).\n- **Command**.",
            "3 middlewares sur faux serveur HTTP.",
            "Premier qui peut (ou tous) traitent.",
        ),
        "design-patterns-command": mk_body(
            "Command encapsule une action en objet.",
            "Undo Ctrl+Z dans un éditeur.",
            "`execute()` / `undo()` ; historique de commandes.",
            "Commande au restaurant notée pour la cuisine.",
            S("""interface Command { execute(): void; undo(): void }
class AddTextCommand implements Command {
  constructor(private doc: { text: string }, private chunk: string) {}
  execute() { this.doc.text += this.chunk; }
  undo() { this.doc.text = this.doc.text.slice(0, -this.chunk.length); }
}
class History {
  private stack: Command[] = [];
  run(cmd: Command) { cmd.execute(); this.stack.push(cmd); }
  undo() { this.stack.pop()?.undo(); }
}"""),
            P("""class History:
    def __init__(self):
        self.stack = []
    def run(self, cmd):
        cmd.execute(); self.stack.append(cmd)"""),
            "- Undo/redo, queue, macros, audit log.",
            "- Action triviale sans historique.",
            "- Commandes non idempotentes mal gérées.",
            "- **Strategy**.\n- **Memento**.",
            "Éditeur texte mini avec undo.",
            "Action = objet first-class.",
        ),
        "design-patterns-iterator": mk_body(
            "Iterator parcourt sans exposer la structure.",
            "Liste chaînée, arbre : le client veut `for..of`.",
            "Interface `next()` / `hasNext()` ou protocole natif.",
            "Télécommande chaîne suivant/précédent.",
            S("""class NumberCollection {
  constructor(private items: number[]) {}
  *[Symbol.iterator]() {
    for (const x of this.items) yield x;
  }
}
for (const n of new NumberCollection([1, 2, 3])) console.log(n);"""),
            P("""class NumberCollection:
    def __init__(self, items):
        self.items = items
    def __iter__(self):
        return iter(self.items)"""),
            "- Structures variées.\n- Parcours uniforme.",
            "- Tableau natif suffit.",
            "- Modifier la collection pendant l'itération.",
            "- **Composite** (parcours arbre).\n- Generators.",
            "Iterator custom sur liste chaînée.",
            "Parcours découplé de l'implémentation.",
        ),
        "design-patterns-mediator": mk_body(
            "Mediator centralise les communications.",
            "Formulaire : 10 champs qui se désactivent mutuellement.",
            "Composants parlent au `FormMediator`.",
            "Tour de contrôle aérienne.",
            S("""class FormMediator {
  private fields = new Map<string, HTMLInputElement>();
  register(name: string, el: HTMLInputElement) { this.fields.set(name, el); }
  changed(name: string) {
    if (name === 'country' && this.fields.get('country')!.value !== 'FR') {
      this.fields.get('siret')!.disabled = true;
    }
  }
}"""),
            P("""class FormMediator:
    def __init__(self):
        self.fields = {}
    def changed(self, name):
        pass"""),
            "- N×N interactions.\n- UI formulaires complexes.",
            "- 2 composants seulement → Observer.",
            "- Mediator God Object.",
            "- **Observer**.\n- **Facade**.",
            "Chat room : users envoient via mediator.",
            "Réduire le maillage, pas la logique métier partout.",
        ),
        "design-patterns-memento": mk_body(
            "Memento sauvegarde l'état pour restauration.",
            "Undo sans exposer les champs privés.",
            "Originator crée Memento ; Caretaker stocke l'historique.",
            "Ctrl+S snapshot.",
            S("""class Editor {
  constructor(public text: string) {}
  save() { return this.text; }
  restore(m: string) { this.text = m; }
}
class History {
  private states: string[] = [];
  push(editor: Editor) { this.states.push(editor.save()); }
  undo(editor: Editor) { editor.restore(this.states.pop()!); }
}"""),
            P("""class History:
    def __init__(self):
        self.states = []
    def push(self, state):
        self.states.append(state)"""),
            "- Undo, checkpoints jeu, brouillons.",
            "- État énorme sérialisé sans limite.",
            "- Caretaker qui modifie le memento.",
            "- **Command** (undo via commandes).\n- Snapshots DB.",
            "Éditeur avec pile undo 10 niveaux.",
            "Sauver l'état proprement.",
        ),
        "design-patterns-state": mk_body(
            "State change le comportement selon l'état interne.",
            "Commande : brouillon → payée → expédiée ; actions autorisées différentes.",
            "Classes d'état au lieu d'un switch géant.",
            "Distributeur : pas de soda si pas payé.",
            S("""interface OrderState { pay(o: Order): void; ship(o: Order): void }
class Draft implements OrderState {
  pay(o: Order) { o.setState(new Paid()); }
  ship() { throw new Error('impossible'); }
}
class Paid implements OrderState {
  pay() { throw new Error('deja paye'); }
  ship(o: Order) { o.setState(new Shipped()); }
}
class Order {
  constructor(private state: OrderState = new Draft()) {}
  setState(s: OrderState) { this.state = s; }
  pay() { this.state.pay(this); }
  ship() { this.state.ship(this); }
}"""),
            P("""class Order:
    def __init__(self):
        self.state = 'draft'"""),
            "- Transitions complexes.\n- Règles par état.",
            "- 2-3 états stables → enum suffit.",
            "- Table de transitions incomplète.",
            "- **Strategy**.\n- Machine à états framework.",
            "Machine à états pour ticket support.",
            "Comportement = f(état), pas if géant.",
        ),
        "design-patterns-template-method": mk_body(
            "Template Method : squelette fixe, hooks variables.",
            "ETL : extract/load communs, transform spécifique.",
            "`process()` appelle des étapes overridables.",
            "Recette : étapes fixes, épices variables.",
            S("""abstract class DataImporter {
  import(path: string) {
    const raw = this.read(path);
    const data = this.transform(raw);
    this.save(data);
  }
  protected abstract read(path: string): string;
  protected abstract transform(raw: string): unknown;
  protected save(data: unknown) { console.log('saved', data); }
}"""),
            P("""class DataImporter(ABC):
    def import_file(self, path):
        raw = self.read(path)
        data = self.transform(raw)
        self.save(data)"""),
            "- Algorithme stable, étapes variables.\n- Frameworks (hooks).",
            "- Tout l'algorithme change → Strategy.",
            "- Hooks trop granulaires illisibles.",
            "- **Strategy** (tout l'algo).\n- **Builder**.",
            "Importer CSV vs JSON avec même squelette.",
            "Hollywood : don't call us, we'll call you.",
        ),
        "design-patterns-visitor": mk_body(
            "Visitor sépare opérations et structure d'objets.",
            "Exporter un AST en HTML, PDF, lint sans modifier chaque nœud.",
            "Double dispatch : `node.accept(visitor)`.",
            "Inspecteurs experts sur même bâtiment.",
            S("""interface Node { accept(v: Visitor): void }
interface Visitor { visitParagraph(p: Paragraph): void; visitImage(i: ImageNode): void }
class Paragraph implements Node {
  constructor(public text: string) {}
  accept(v: Visitor) { v.visitParagraph(this); }
}
class HtmlExport implements Visitor {
  visitParagraph(p: Paragraph) { console.log('<p>', p.text); }
  visitImage(i: ImageNode) { console.log('<img>'); }
}"""),
            P("""class HtmlExport:
    def visit_paragraph(self, p):
        print('<p>', p.text)"""),
            "- Nouvelles opérations fréquentes sur structure stable.\n- AST, DOM.",
            "- Structure change souvent.\n- Peu de types.",
            "- Visitor qui casse l'encapsulation.",
            "- **Interpreter**.\n- Pattern matching moderne.",
            "2 visitors sur arbre expression (eval, print).",
            "Opérations externes à la hiérarchie.",
        ),
        "design-patterns-interpreter": mk_body(
            "Interpreter définit une grammaire et interprète des phrases.",
            "Règles « SI age > 18 ET pays = FR ».",
            "Arbre d'expressions avec `interpret(context)`.",
            "Calculatrice + et *.",
            S("""interface Expr { interpret(ctx: Record<string, number>): number }
class NumberLit implements Expr {
  constructor(private n: number) {}
  interpret() { return this.n; }
}
class Plus implements Expr {
  constructor(private l: Expr, private r: Expr) {}
  interpret(ctx: Record<string, number>) { return this.l.interpret(ctx) + this.r.interpret(ctx); }
}"""),
            P("""class Plus:
    def __init__(self, left, right):
        self.left, self.right = left, right
    def interpret(self, ctx):
        return self.left.interpret(ctx) + self.right.interpret(ctx)"""),
            "- Grammaire simple stable.\n- DSL métier petit.",
            "- Langage complexe → parser generator.",
            "- Arbre non typé fragile.",
            "- **Composite** (arbre).\n- **Visitor**.",
            "Parser « 1 + 2 * 3 » mini (priorités).",
            "Langage mini = classes + interpret.",
        ),
    }


ARTICLES_EXTRA = {
    "design-patterns-strategy": (21, "2026-04-21", "Strategy", "Comportemental",
        "Strategy encapsule des algorithmes interchangeables (livraison, tri, export) pour éviter les switch et respecter Open/Closed.",
        STRATEGY_BODY),
    "design-patterns-decorator": (10, "2026-04-10", "Decorator", "Structurel",
        "Decorator ajoute des responsabilités à un objet par composition (buffer, crypto, logs) sans explosion de sous-classes.",
        DECORATOR_BODY),
}


def main() -> None:
    bodies = _bodies()
    for slug, order, date, name, fam, excerpt in _META:
        body = bodies[slug]
        write_article(slug, order, date, name, fam, excerpt, body)
    for slug, (order, date, name, fam, excerpt, body) in ARTICLES_EXTRA.items():
        write_article(slug, order, date, name, fam, excerpt, body)
    print("skip intro & observer (hand-written)")


if __name__ == "__main__":
    main()
