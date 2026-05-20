# -*- coding: utf-8 -*-
"""Contenu détaillé des 23 patterns GoF — ordre popularité (junior-friendly)."""

from __future__ import annotations

# Du plus au moins rencontré en entreprise / tutoriels / frameworks
POPULARITY_SLUGS: list[str] = [
    "design-patterns-singleton",
    "design-patterns-factory-method",
    "design-patterns-observer",
    "design-patterns-strategy",
    "design-patterns-decorator",
    "design-patterns-adapter",
    "design-patterns-facade",
    "design-patterns-command",
    "design-patterns-template-method",
    "design-patterns-builder",
    "design-patterns-iterator",
    "design-patterns-state",
    "design-patterns-proxy",
    "design-patterns-abstract-factory",
    "design-patterns-composite",
    "design-patterns-bridge",
    "design-patterns-prototype",
    "design-patterns-flyweight",
    "design-patterns-chain-of-responsibility",
    "design-patterns-mediator",
    "design-patterns-memento",
    "design-patterns-visitor",
    "design-patterns-interpreter",
]

FAMILY_COLORS = {
    "Créationnel": "#059669",
    "Structurel": "#2563eb",
    "Comportemental": "#d97706",
}


def _p(
    slug: str,
    name: str,
    family: str,
    one_liner: str,
    problem: str,
    idea: str,
    analogy: str,
    roles: list[tuple[str, str]],
    ts: str,
    py: str,
    when_use: list[str],
    when_not: list[str],
    mistakes: list[str],
    related: list[tuple[str, str]],
    real_world: str,
    exercise: str,
    summary: str,
    extra_fig: str | None = None,
    compare: str | None = None,
) -> dict:
    return {
        "slug": slug,
        "name": name,
        "family_fr": family,
        "one_liner": one_liner,
        "problem": problem,
        "idea": idea,
        "analogy": analogy,
        "roles": roles,
        "ts_example": ts.strip(),
        "py_example": py.strip(),
        "when_use": when_use,
        "when_not": when_not,
        "mistakes": mistakes,
        "related": related,
        "real_world": real_world,
        "exercise": exercise,
        "summary": summary,
        "extra_fig": extra_fig,
        "compare": compare,
    }


PATTERNS: dict[str, dict] = {}

# --- Singleton ---
PATTERNS["design-patterns-singleton"] = _p(
    "design-patterns-singleton",
    "Singleton",
    "Créationnel",
    "Le Singleton garantit qu'une classe n'a qu'une seule instance et fournit un point d'accès global contrôlé.",
    """Tu charges la configuration `.env` à plusieurs endroits avec `new Config()`. Résultat : flags incohérents, double connexion, tests impossibles à isoler.

```typescript
// Anti-pattern : plusieurs instances
const a = new AppConfig();
const b = new AppConfig();
// a et b peuvent diverger si le constructeur relit le disque
```""",
    """Cache le constructeur et expose `getInstance()` (lazy) ou exporte un **module unique** (pattern module ES).

| Rôle | Responsabilité |
|------|----------------|
| `Singleton` | Instance unique + accès global |
| Client | Appelle `getInstance()` au lieu de `new` |""",
    "Comme le **maire d'une ville** : une seule personne occupe le poste ; les services administratifs passent par lui, on n'en nomme pas un nouveau par formulaire.",
    [
        ("Singleton", "Stocke l'instance statique, constructeur privé"),
        ("Client", "Utilise getInstance()"),
    ],
    """```typescript
class AppConfig {
  private static instance: AppConfig | null = null;

  private constructor(
    public readonly apiUrl: string,
    public readonly env: 'dev' | 'prod',
  ) {}

  static getInstance(): AppConfig {
    if (!AppConfig.instance) {
      AppConfig.instance = new AppConfig(
        import.meta.env.VITE_API_URL ?? 'http://localhost:3000',
        (import.meta.env.MODE === 'production' ? 'prod' : 'dev') as 'dev' | 'prod',
      );
    }
    return AppConfig.instance;
  }
}

const a = AppConfig.getInstance();
const b = AppConfig.getInstance();
console.log(a === b); // true
```""",
    """```python
class AppConfig:
    _instance: "AppConfig | None" = None

    def __init__(self, api_url: str, env: str) -> None:
        if AppConfig._instance is not None:
            raise RuntimeError("Utilise AppConfig.get()")
        self.api_url = api_url
        self.env = env

    @classmethod
    def get(cls) -> "AppConfig":
        if cls._instance is None:
            cls._instance = cls("https://api.example.com", "prod")
        return cls._instance
```""",
    [
        "Ressource réellement unique (pool de connexions maîtrisé, identifiant machine).",
        "Coût d'initialisation élevé partagé par toute l'application.",
    ],
    [
        "Tests unitaires : l'état global pollue les tests parallèles.",
        "Plusieurs instances légitimes (un panier par utilisateur).",
        "En TypeScript moderne : préfère un module `config.ts` exporté ou l'injection de dépendances.",
    ],
    [
        "Singleton « par défaut » sur toutes les classes.",
        "God Object : tout l'état métier dans l'instance unique.",
        "Oublier le thread-safety en Java/C# (double-checked locking).",
    ],
    [
        ("Factory Method", "Délègue la création sans imposer une instance unique"),
        ("Injection de dépendances", "Passe Config en paramètre — plus testable"),
    ],
    "Node.js : certains drivers utilisent un pool singleton. En front, évite le singleton DOM ; préfère un store (Zustand, Pinia) avec un seul provider.",
    "Remplace ton `Logger.getInstance()` par un logger injecté dans chaque service. Écris 2 tests : avec mock, sans état partagé.",
    "Une instance, un accès — utile pour de vraies ressources uniques ; dangereux comme variable globale déguisée.",
)

# --- Factory Method ---
PATTERNS["design-patterns-factory-method"] = _p(
    "design-patterns-factory-method",
    "Factory Method",
    "Créationnel",
    "La Factory Method délègue la création d'objets aux sous-classes sans que le client connaisse la classe concrète.",
    """Chaque export PDF/CSV/JSON ajoute un `if` dans le service :

```typescript
function exportData(type: string, rows: Row[]) {
  if (type === 'pdf') { /* 40 lignes */ }
  else if (type === 'csv') { /* ... */ }
  // chaque format = modifier cette fonction
}
```""",
    """Une classe abstraite (ou interface) déclare `createExporter()` ; chaque sous-classe retourne le bon produit. Le client appelle `run()` sur le service, pas `new PdfExporter()` partout.""",
    "Tu commandes le **plat du jour** au restaurant : la salle ne cuisine pas — la cuisine (sous-classe) choisit le plat selon les stocks.",
    [
        ("Creator", "Déclare la factory method + logique qui l'utilise"),
        ("ConcreteCreator", "Implémente createProduct()"),
        ("Product", "Interface commune des objets créés"),
    ],
    """```typescript
interface Exporter {
  export(rows: Record<string, unknown>[]): string;
}

abstract class ExportService {
  protected abstract createExporter(): Exporter;

  run(rows: Record<string, unknown>[]) {
    return this.createExporter().export(rows);
  }
}

class CsvExportService extends ExportService {
  protected createExporter(): Exporter {
    return {
      export: (rows) =>
        [Object.keys(rows[0] ?? {}).join(','), ...rows.map((r) => Object.values(r).join(','))].join('\\n'),
    };
  }
}

class JsonExportService extends ExportService {
  protected createExporter(): Exporter {
    return { export: (rows) => JSON.stringify(rows, null, 2) };
  }
}

function download(userChoice: 'csv' | 'json', rows: Record<string, unknown>[]) {
  const service =
    userChoice === 'csv' ? new CsvExportService() : new JsonExportService();
  return service.run(rows);
}
```""",
    """```python
from abc import ABC, abstractmethod

class Exporter(ABC):
    @abstractmethod
    def export(self, rows: list[dict]) -> str: ...

class ExportService(ABC):
    @abstractmethod
    def create_exporter(self) -> Exporter: ...

    def run(self, rows: list[dict]) -> str:
        return self.create_exporter().export(rows)

class CsvExportService(ExportService):
    def create_exporter(self) -> Exporter:
        class _Csv(Exporter):
            def export(self, rows: list[dict]) -> str:
                if not rows:
                    return ""
                keys = rows[0].keys()
                lines = [",".join(keys)]
                lines += [",".join(str(r[k]) for k in keys) for r in rows]
                return "\\n".join(lines)
        return _Csv()
```""",
    ["Le type de produit dépend du contexte (config, tenant, environnement).", "Tu veux ajouter des variantes sans toucher au code client (Open/Closed)."],
    ["Une seule implémentation stable.", "Création triviale (`return new Date()`)."],
    ["Confondre avec Abstract Factory (famille entière d'objets).", "Hiérarchie inutile pour 2 produits figés."],
    [("Abstract Factory", "Crée des familles d'objets liés"), ("Simple Factory", "Fonction unique non GoF mais courante")],
    "Django : `Model.objects` est une factory. Les frameworks UI créent des composants via des registres de factory.",
    "Ajoute un format `xlsx` via une nouvelle sous-classe `XlsxExportService` sans modifier `download()`.",
    "Factory Method = création polymorphe par sous-classes — idéal quand le « quel produit » varie selon le contexte.",
)

# --- Observer (contenu enrichi) ---
PATTERNS["design-patterns-observer"] = _p(
    "design-patterns-observer",
    "Observer",
    "Comportemental",
    "Le Observer notifie automatiquement tous les abonnés quand l'état d'un sujet change.",
    """```typescript
class Product {
  setStock(n: number) {
    this.stock = n;
    new EmailService().sendLowStockAlert(this);
    new Dashboard().refresh(this);
    new SlackNotifier().post(this.stock);
  }
}
```
Chaque nouveau canal modifie `Product`. Une erreur Slack peut casser la mise à jour du stock.""",
    """Sépare **Subject** (état + abonnés) et **Observer** (réactions). Le sujet appelle `notify()` sans connaître les détails.""",
    "Newsletter : tu t'abonnes, l'éditeur publie, tous les abonnés reçoivent le mail.",
    [
        ("Subject", "attach / detach / notify"),
        ("Observer", "update(event)"),
        ("ConcreteSubject", "État métier (stock, panier…)"),
    ],
    """```typescript
interface Observer<T> {
  update(data: T): void;
}

class StockSubject {
  private observers = new Set<Observer<number>>();
  private stock = 0;

  subscribe(obs: Observer<number>): () => void {
    this.observers.add(obs);
    return () => this.observers.delete(obs);
  }

  setStock(value: number): void {
    if (value < 0) throw new Error('Stock invalide');
    this.stock = value;
    for (const obs of this.observers) obs.update(this.stock);
  }
}

class LowStockAlert implements Observer<number> {
  constructor(private threshold: number) {}
  update(stock: number): void {
    if (stock <= this.threshold) console.log(`ALERTE stock bas: ${stock}`);
  }
}
```""",
    """```python
from typing import Callable

class StockSubject:
    def __init__(self) -> None:
        self._stock = 0
        self._observers: list[Callable[[int], None]] = []

    def subscribe(self, fn: Callable[[int], None]) -> Callable[[], None]:
        self._observers.append(fn)
        def unsub() -> None:
            self._observers.remove(fn)
        return unsub

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, value: int) -> None:
        self._stock = value
        for obs in list(self._observers):
            obs(value)
```""",
    ["Plusieurs réactions au même changement d'état.", "Ajouter des réactions sans modifier la source.", "UI réactive (modèle → vues)."],
    ["Une seule réaction → simple callback.", "Microservices distribués → bus de messages (Kafka), pas Observer in-process.", "Oublier le désabonnement → fuite mémoire."],
    ["Pas de `unsubscribe` en SPA.", "Notifier pendant une mutation partielle.", "Observer qui modifie le sujet dans `update` → boucles.", "EventBus global non typé."],
    [("Mediator", "Coordonne des collègues, ne diffuse pas un état"), ("Pub/Sub", "Bus intermédiaire optionnel")],
    "React : hooks + state. Vue : réactivité. Node : `EventEmitter`. Domain-Driven Design : événements de domaine.",
    "Crée `CartSubject` + observers badge panier et analytics. Ajoute un 3e observer sans toucher `CartSubject`. Teste le désabonnement.",
    "Subject notifie, Observer réagit — découplage fort ; pense toujours au cycle de vie des abonnements.",
    compare="""| Approche | Usage |
|----------|-------|
| Observer GoF | Domaine métier clair |
| EventEmitter | Modules techniques Node |
| RxJS | Flux complexes avec opérateurs |
| Store React/Zustand | UI : le sujet est le store |""",
)

# --- Strategy ---
PATTERNS["design-patterns-strategy"] = _p(
    "design-patterns-strategy",
    "Strategy",
    "Comportemental",
    "Strategy encapsule des algorithmes interchangeables injectés au runtime.",
    """```typescript
function shipping(cost: number, mode: string) {
  if (mode === 'express') return cost + 15;
  if (mode === 'standard') return cost + 5;
  if (mode === 'pickup') return 0;
  throw new Error('mode inconnu');
}
```""",
    "Interface `ShippingStrategy` + implémentations ; le `Checkout` reçoit la stratégie par injection.",
    "GPS : mode voiture / vélo / piéton — même destination, algorithme différent.",
    [("Context", "Utilise une Strategy"), ("Strategy", "Interface compute()"), ("ConcreteStrategy", "Express, Standard…")],
    """```typescript
interface ShippingStrategy {
  readonly label: string;
  compute(baseCost: number): number;
}

class ExpressShipping implements ShippingStrategy {
  readonly label = 'Express 24h';
  compute(baseCost: number) { return baseCost + 15; }
}

class Checkout {
  constructor(private shipping: ShippingStrategy) {}
  total(items: number) {
    return this.shipping.compute(items);
  }
  setShipping(s: ShippingStrategy) { this.shipping = s; }
}
```""",
    """```python
from abc import ABC, abstractmethod

class ShippingStrategy(ABC):
    @abstractmethod
    def compute(self, base: float) -> float: ...

class ExpressShipping(ShippingStrategy):
    def compute(self, base: float) -> float:
        return base + 15.0

class Checkout:
    def __init__(self, shipping: ShippingStrategy) -> None:
        self._shipping = shipping
    def total(self, items: float) -> float:
        return self._shipping.compute(items)
```""",
    ["Plusieurs variantes d'un même calcul.", "Changer d'algorithme à l'exécution (config utilisateur)."],
    ["Un seul algorithme stable.", "Quelques `if` lisibles suffisent."],
    ["Une stratégie par ligne de `if` sans interface commune.", "Stratégies avec effets de bord cachés."],
    [("State", "Change le comportement selon l'état interne"), ("Template Method", "Squelette fixe, étapes en sous-classes")],
    "Paiement Stripe (cartes, wallets). Tri : `Array.sort(compareFn)` en JS est Strategy.",
    "Implémente `DiscountStrategy` (étudiant, membre, aucun) pour un panier e-commerce.",
    "Strategy = algorithmes plugables — évite les switch qui grossissent à chaque release.",
)

# --- Decorator ---
PATTERNS["design-patterns-decorator"] = _p(
    "design-patterns-decorator",
    "Decorator",
    "Structurel",
    "Decorator ajoute des responsabilités à un objet par composition, sans modifier sa classe.",
    "Tu veux buffer + compression + chiffrement sur un flux : `BufferedCompressedEncryptedReader` multiplie les sous-classes.",
    "Chaque décorateur implémente la même interface et délègue au composant interne après sa couche.",
    "Gâteau : génoise → crème → glaçage, couche par couche.",
    [("Component", "Interface commune"), ("ConcreteComponent", "Objet de base"), ("Decorator", "Wrap + délègue")],
    """```typescript
interface DataSource {
  write(data: string): void;
  read(): string;
}

class FileSource implements DataSource {
  private content = '';
  write(data: string) { this.content += data; }
  read() { return this.content; }
}

abstract class DataSourceDecorator implements DataSource {
  constructor(protected wrappee: DataSource) {}
  write(data: string) { this.wrappee.write(data); }
  read() { return this.wrappee.read(); }
}

class EncryptionDecorator extends DataSourceDecorator {
  write(data: string) { super.write(btoa(data)); }
  read() { return atob(super.read()); }
}

let source: DataSource = new FileSource();
source = new EncryptionDecorator(source);
source.write('secret');
```""",
    """```python
class DataSource(ABC):
    @abstractmethod
    def read(self) -> str: ...
    @abstractmethod
    def write(self, data: str) -> None: ...

class EncryptionDecorator(DataSource):
    def __init__(self, wrappee: DataSource) -> None:
        self._w = wrappee
    def write(self, data: str) -> None:
        import base64
        self._w.write(base64.b64encode(data.encode()).decode())
    def read(self) -> str:
        import base64
        return base64.b64decode(self._w.read().encode()).decode()
```""",
    ["Empiler des options (streams, middleware HTTP).", "HOC React qui enrichit un composant."],
    ["Peu de combinaisons possibles.", "Ordre des couches critique et non documenté."],
    ["Trop de couches = debug difficile.", "Décorateur non substituable (viole Liskov)."],
    [("Adapter", "Change l'interface"), ("Proxy", "Contrôle l'accès")],
    "Express middleware : `app.use(logger)`, `app.use(auth)` — chaîne de décorateurs autour du handler.",
    "`Coffee` + `MilkDecorator` + `SugarDecorator` qui ajoutent au prix.",
    "Decorator = composition dynamique de comportements.",
    compare="""| Pattern | Rôle |
|---------|------|
| Decorator | Ajoute une responsabilité |
| Adapter | Change l'interface |
| Proxy | Contrôle l'accès |""",
)

# Les patterns suivants sont enrichis dans design_patterns_enriched.py (apply au build)


def patterns_in_popularity_order() -> list[dict]:
    return [PATTERNS[s] for s in POPULARITY_SLUGS]

