# -*- coding: utf-8 -*-
"""Contenu enrichi pour les patterns (articles longs + illustrations)."""

from __future__ import annotations

from design_patterns_data import PATTERNS, _p

# Met à jour les patterns déjà définis avec sections supplémentaires
for key in ("design-patterns-singleton", "design-patterns-factory-method", "design-patterns-observer",
            "design-patterns-strategy", "design-patterns-decorator"):
    if key in PATTERNS:
        PATTERNS[key]["steps"] = [
            "Identifie la variation (création, structure, comportement).",
            "Isole l'abstraction que le client doit voir.",
            "Implémente une seule variante concrète et teste.",
            "Ajoute les variantes sans modifier le client.",
            "Revoyez en code review : pas de sur-abstraction.",
        ]


def _anti(code: str) -> str:
    return f"```typescript\n{code.strip()}\n```"


ENRICHED: dict[str, dict] = {}

ENRICHED["design-patterns-adapter"] = _p(
    "design-patterns-adapter", "Adapter", "Structurel",
    "Adapter convertit l'interface d'une classe existante en celle attendue par le client, sans modifier le code legacy.",
    f"""Tu intègres une API de paiement legacy qui expose `sendPayment(amountUsd)` alors que ton domaine parle en euros via `pay(euros)`.

{_anti('''
// Partout dans l'app : conversion manuelle + appel direct
function checkout(amountEur: number) {
  const legacy = new LegacyPayPal();
  const usd = amountEur * 1.08;
  const r = legacy.sendPayment(usd);
  if (!r.success) throw new Error('Paiement refusé');
}
''')}

Chaque nouveau fournisseur = nouveau bricolage dans les controllers.""",
    """L'**Adapter** implémente **ton** port (`PaymentPort`) et encapsule l'adaptee (SDK legacy). Le client ne voit que l'interface propre.

| Rôle | Responsabilité |
|------|----------------|
| **Client** | Appelle `PaymentPort` |
| **Target** | Interface attendue (`pay`) |
| **Adapter** | Traduit appels et formats |
| **Adaptee** | API existante non modifiable |""",
    "Adaptateur **prise EU → US** : l'appareil (client) reste identique ; l'adaptateur convertit le courant.",
    [("Client", "Checkout, service métier"), ("PaymentPort", "Interface cible"), ("PayPalAdapter", "Traduction EUR→USD"), ("LegacyPayPal", "SDK tiers")],
    """```typescript
interface PaymentPort {
  pay(euros: number): Promise<{ ok: boolean; ref?: string }>;
}

class LegacyPayPal {
  sendPayment(amountUsd: number) {
    return { success: amountUsd > 0, transactionId: `PP-${amountUsd}` };
  }
}

class PayPalAdapter implements PaymentPort {
  constructor(
    private readonly legacy: LegacyPayPal,
    private readonly eurToUsd: number,
  ) {}

  async pay(euros: number) {
    const usd = Math.round(euros * this.eurToUsd * 100) / 100;
    const result = this.legacy.sendPayment(usd);
    return { ok: result.success, ref: result.transactionId };
  }
}

async function checkout(port: PaymentPort, amount: number) {
  const r = await port.pay(amount);
  if (!r.ok) throw new Error('Paiement échoué');
  return r.ref;
}
```""",
    """```python
from abc import ABC, abstractmethod

class PaymentPort(ABC):
    @abstractmethod
    async def pay(self, euros: float) -> dict: ...

class LegacyPayPal:
    def send_payment(self, amount_usd: float) -> dict:
        return {"success": amount_usd > 0, "transaction_id": f"PP-{amount_usd}"}

class PayPalAdapter(PaymentPort):
    def __init__(self, legacy: LegacyPayPal, eur_to_usd: float) -> None:
        self._legacy = legacy
        self._rate = eur_to_usd

    async def pay(self, euros: float) -> dict:
        usd = round(euros * self._rate, 2)
        r = self._legacy.send_payment(usd)
        return {"ok": r["success"], "ref": r["transaction_id"]}
```""",
    ["Intégration SDK/API que tu ne peux pas modifier.", "Formats de données différents (XML, SOAP, binaire).", "Plusieurs clients doivent partager la même traduction."],
    ["Tu contrôles le code legacy et peux le refactoriser directement.", "Un simple mapper fonction suffit (pas besoin d'objet Adapter)."],
    ["Adapter qui fait de la logique métier (doit seulement traduire).", "Oublier les erreurs du adaptee (timeouts, codes).", "Créer un adapter par appel au lieu d'un par service."],
    [("Facade", "Simplifie un sous-système entier"), ("Decorator", "Ajoute un comportement, ne change pas l'interface cible")],
    "Stripe SDK derrière ton port interne. Axios + transform pour API REST legacy. Lecteurs de fichiers Node (`fs` streams).",
    "Branche `StripeAdapter` et `PayPalAdapter` sur le même `PaymentPort`. Teste le checkout avec un mock sans appeler l'API réelle.",
    "Adapter = traduire une interface incompatible — le client reste propre.",
    compare="""| Pattern | Quand |
|---------|-------|
| Adapter | Interface incompatible |
| Facade | Sous-système complexe, même techno |
| Decorator | Même interface, couche en plus |""",
)

ENRICHED["design-patterns-facade"] = _p(
    "design-patterns-facade", "Facade", "Structurel",
    "Facade offre une interface simple qui orchestre un sous-système complexe.",
    f"""Démarrer l'application oblige chaque module à connaître l'ordre d'initialisation :

{_anti('''
await loadConfig();
const db = await connectDb(process.env.DB_URL);
await migrate(db);
const cache = await connectRedis();
await warmCache(cache, db);
queue.start();
http.listen(3000);
''')}

Un oubli ou un mauvais ordre = crash au boot.""",
    "`AppFacade.start()` encapsule les étapes. Les modules internes restent découplés ; seul la facade connaît l'orchestration.",
    "Réception d'**hôtel** : une clé, pas besoin de gérer ménage, cuisine et spa séparément.",
    [("Client", "main.ts, CLI"), ("Facade", "start(), stop()"), ("Subsystem", "DB, cache, queue…")],
    """```typescript
class Database {
  async connect(url: string) { console.log('DB', url); return this; }
}
class Cache {
  async warm() { console.log('cache warm'); }
}
class JobQueue {
  start() { console.log('workers'); }
}

class AppFacade {
  private db = new Database();
  private cache = new Cache();
  private queue = new JobQueue();

  async start() {
    await this.db.connect(process.env.DB_URL!);
    await this.cache.warm();
    this.queue.start();
    console.log('App ready');
  }

  async stop() {
    console.log('Graceful shutdown');
  }
}
```""",
    """```python
class AppFacade:
    def __init__(self) -> None:
        self._db = Database()
        self._cache = Cache()

    async def start(self) -> None:
        await self._db.connect(os.environ["DB_URL"])
        await self._cache.warm()
        print("App ready")

    async def stop(self) -> None:
        await self._db.close()
```""",
    ["Sous-système avec 5+ composants à initialiser.", "Tu veux une API stable pour des clients externes.", "Onboarding : un seul point d'entrée documenté."],
    ["Le sous-système tient en 2 appels — pas besoin de facade.", "La facade devient un God Object qui connaît tout le métier."],
    ["Mettre la logique métier dans la facade.", "Exposer tous les subsystèmes au client (perd l'intérêt)."],
    [("Adapter", "Une classe legacy"), ("Mediator", "Coordonne des collègues égaux")],
    "Frameworks `NestFactory.create()`, `SpringApplication.run()`. Scripts `docker compose up` qui masquent réseau + volumes.",
    "Écris `DeployFacade.deploy(env)` qui enchaîne build, tests, push image, rollout K8s — une commande pour l'équipe.",
    "Facade = point d'entrée simple vers la complexité.",
)

ENRICHED["design-patterns-command"] = _p(
    "design-patterns-command", "Command", "Comportemental",
    "Command encapsule une requête en objet : exécution, annulation, file d'attente, historique.",
    f"""Éditeur de texte sans Command :

{_anti('''
function onKey(type: string) {
  if (type === 'bold') document.execCommand('bold');
  // impossible de stocker l'historique proprement pour undo
}
''')}

Undo/redo devient un cauchemar de flags.""",
    "Chaque action est un objet `execute()` / `undo()`. L'**Invoker** empile l'historique sans connaître les détails.",
    "Commande au **restaurant** : le serveur note, la cuisine exécute plus tard — la commande est l'objet.",
    [("Command", "execute / undo"), ("Invoker", "Historique"), ("Receiver", "Document modifié"), ("Client", "UI")],
    """```typescript
interface Command {
  execute(): void;
  undo(): void;
}

class AddTextCommand implements Command {
  constructor(private doc: string[], private text: string) {}
  execute() { this.doc.push(this.text); }
  undo() { this.doc.pop(); }
}

class EditorInvoker {
  private history: Command[] = [];
  private pointer = -1;

  run(cmd: Command) {
    cmd.execute();
    this.history = this.history.slice(0, this.pointer + 1);
    this.history.push(cmd);
    this.pointer++;
  }

  undo() {
    if (this.pointer < 0) return;
    this.history[this.pointer--].undo();
  }
}

const doc: string[] = [];
const invoker = new EditorInvoker();
invoker.run(new AddTextCommand(doc, 'Hello'));
invoker.undo();
```""",
    """```python
class Command(ABC):
    @abstractmethod
    def execute(self) -> None: ...
    @abstractmethod
    def undo(self) -> None: ...

class AddTextCommand(Command):
    def __init__(self, doc: list[str], text: str) -> None:
        self._doc = doc
        self._text = text
    def execute(self) -> None:
        self._doc.append(self._text)
    def undo(self) -> None:
        self._doc.pop()
```""",
    ["Undo/redo.", "File d'attente de tâches (jobs).", "Macros rejouant plusieurs commandes.", "CQRS côté écriture."],
    ["Action unique sans historique.", "Overhead inutile pour un bouton."],
    ["undo() qui ne restaure pas l'état exact.", "Commandes non idempotentes mal documentées."],
    [("Strategy", "Choisit un algorithme, pas une action réversible"), ("Memento", "Snapshot d'état sans objet commande")],
    "Photoshop history. Redis queues. Git commit comme snapshot (proche, pas identique).",
    "Implémente `MoveItemCommand` pour un panier (ajout/retrait avec undo).",
    "Command = action comme objet, parfaite pour undo et files d'attente.",
)

# Suite des patterns enrichis (builder, state, proxy, etc.)
def _bulk() -> None:
    specs = [
        ("design-patterns-builder", "Builder", "Créationnel",
         "Builder construit pas à pas un objet complexe avec une API fluide.",
         "Un `User` a 12 champs optionnels : `new User(a,b,c,...)` illisible.",
         "Étapes nommées qui retournent `this`, `build()` valide et retourne l'objet immuable.",
         "Composer un burger : pain, steak, sauce — étape par étape.",
         """```typescript
class HttpRequest {
  constructor(
    public method: string,
    public url: string,
    public headers: Record<string, string> = {},
    public body?: string,
  ) {}
}

class RequestBuilder {
  private method = 'GET';
  private url = '/';
  private headers: Record<string, string> = {};
  private body?: string;

  setMethod(m: string) { this.method = m; return this; }
  setUrl(u: string) { this.url = u; return this; }
  addHeader(k: string, v: string) { this.headers[k] = v; return this; }
  setBody(b: string) { this.body = b; return this; }

  build() {
    if (!this.url.startsWith('/')) throw new Error('URL invalide');
    return new HttpRequest(this.method, this.url, this.headers, this.body);
  }
}

const req = new RequestBuilder()
  .setMethod('POST')
  .setUrl('/api/users')
  .addHeader('Content-Type', 'application/json')
  .setBody('{"name":"Loic"}')
  .build();
```""",
         "Prisma query builder, `StringBuilder`, Docker Compose multi-services."),
        ("design-patterns-state", "State", "Comportemental",
         "State délègue le comportement à des objets d'état selon le contexte.",
         "Un `switch(status)` de 80 lignes pour une commande e-commerce.",
         "Chaque état (`Draft`, `Paid`, `Shipped`) implémente les transitions autorisées.",
         "Distributeur : pas de soda tant que pas payé.",
         """```typescript
interface OrderState {
  pay(ctx: OrderContext): void;
  ship(ctx: OrderContext): void;
  cancel(ctx: OrderContext): void;
}

class DraftState implements OrderState {
  pay(ctx) { ctx.transition(new PaidState()); }
  ship() { throw new Error('Impossible : non payé'); }
  cancel(ctx) { ctx.transition(new CancelledState()); }
}

class OrderContext {
  constructor(private state: OrderState = new DraftState()) {}
  transition(s: OrderState) { this.state = s; }
  pay() { this.state.pay(this); }
  ship() { this.state.ship(this); }
}
```""",
         "Workflow Jira, formulaires multi-étapes, jeux (menu / play / pause)."),
        ("design-patterns-proxy", "Proxy", "Structurel",
         "Proxy contrôle l'accès à un objet coûteux ou distant (lazy, cache, sécurité).",
         "Charger une image 4K à chaque rendu même hors écran.",
         "Même interface que le sujet ; chargement réel au premier `render()`.",
         "Secrétaire qui filtre les appels avant le directeur.",
         """```typescript
interface Image {
  render(): string;
}

class HeavyImage implements Image {
  constructor(private url: string) {
    console.log('Chargement lourd', url);
  }
  render() { return `<img src="${this.url}"/>`; }
}

class ImageProxy implements Image {
  private real: HeavyImage | null = null;
  constructor(private url: string) {}
  render() {
    if (!this.real) this.real = new HeavyImage(this.url);
    return this.real.render();
  }
}
```""",
         "Vue `reactive`, lazy loading ORM, API gateway, cache HTTP."),
        ("design-patterns-chain-of-responsibility", "Chain of Responsibility", "Comportemental",
         "Chaque handler décide de traiter ou de passer au suivant.",
         "Un seul gros middleware qui mélange auth, logs et métier.",
         "Chaîne de maillons : `auth → log → rateLimit → handler`.",
         "Support : niveau 1, puis 2, puis expert.",
         """```typescript
type Context = { userId?: string; path: string };
type Next = () => Promise<void>;

type Middleware = (ctx: Context, next: Next) => Promise<void>;

const auth: Middleware = async (ctx, next) => {
  if (!ctx.userId) throw new Error('401');
  await next();
};

const logger: Middleware = async (ctx, next) => {
  console.log(ctx.path);
  await next();
};

function run(chain: Middleware[], ctx: Context) {
  let i = 0;
  const next = async () => {
    if (i >= chain.length) return;
    await chain[i++](ctx, next);
  };
  return next();
}
```""",
         "Express, Koa, ASP.NET pipeline, validation de formulaires par étapes."),
    ]
    for slug, name, fam, one, prob, idea, analogy, ts, real in specs:
        sk = slug.replace("design-patterns-", "")
        ENRICHED[slug] = _p(
            slug, name, fam, one,
            f"{prob}\n\n{_anti('// Avant : un seul bloc qui fait tout\\nif (!user) throw new Error();\\nconsole.log(req.url);')}",
            idea,
            analogy,
            [("Handler/Builder", "Rôle central"), ("Client", "Compose la chaîne ou le builder")],
            ts,
            f"```python\n# Portage {name} : reprendre la structure TypeScript ci-dessus\n```",
            [f"Variantes multiples de {name.lower()}.", "Évolution fréquente du flux."],
            ["Cas unique et figé.", "Librairie standard suffisante."],
            ["Chaîne trop longue sans tests par maillon.", "Handler qui fait tout."],
            [("Decorator", "Ajoute une couche systématiquement")],
            real,
            f"Refactorise un bout de code vers {name} et écris 2 tests.",
            f"{name} : {one}",
        )


_bulk()

# Patterns restants avec contenu intermédiaire enrichi
for slug, name, fam, one, prob, idea, analogy, ts in [
    ("design-patterns-template-method", "Template Method", "Comportemental",
     "Template Method fixe le squelette d'un algorithme ; les sous-classes surchargent des étapes.",
     "Import CSV et JSON partagent extract/load mais pas transform.",
     "Classe de base avec `run()` final qui appelle des hooks protégés.",
     "Recette : étapes imposées, ingrédients variables.",
     """```typescript
abstract class ReportPipeline {
  run(source: string) {
    const raw = this.fetch(source);
    const cleaned = this.normalize(raw);
    return this.render(cleaned);
  }
  protected fetch(s: string) { return s; }
  protected abstract normalize(data: string): string;
  protected render(data: string) { return data; }
}

class CsvReport extends ReportPipeline {
  protected normalize(data: string) {
    return data.trim().toUpperCase();
  }
}
```"""),
    ("design-patterns-iterator", "Iterator", "Comportemental",
     "Iterator accède aux éléments d'une collection sans exposer sa structure.",
     "Parcourir une liste chaînée avec des `.next` manuels partout.",
     "Interface commune ; le langage fournit `for..of` / générateurs.",
     "Télécommande chaîne+ / chaîne-.",
     """```typescript
class BookCollection implements Iterable<string> {
  private books: string[] = [];
  add(b: string) { this.books.push(b); }
  *[Symbol.iterator]() {
    for (const b of this.books) yield b;
  }
}
```"""),
    ("design-patterns-abstract-factory", "Abstract Factory", "Créationnel",
     "Abstract Factory crée des familles d'objets cohérents (UI kit, thème).",
     "Boutons Windows mélangés avec checkboxes Mac.",
     "Une factory par thème : `createButton` + `createCheckbox` cohérents.",
     "Kit IKEA : vis et plateaux du même carton.",
     """```typescript
interface UIFactory {
  createButton(): { label: string; style: string };
  createCheckbox(): { checked: boolean; style: string };
}
class DarkFactory implements UIFactory {
  createButton() { return { label: 'OK', style: 'dark-rounded' }; }
  createCheckbox() { return { checked: false, style: 'dark-rounded' }; }
}
```"""),
    ("design-patterns-composite", "Composite", "Structurel",
     "Composite traite feuilles et conteneurs de la même façon.",
     "Menu avec sous-menus : code différent pour `Item` vs `Menu`.",
     "Interface `Component` avec `operation()` récursive.",
     "Dossier ou fichier : même commande `size()`.",
     """```typescript
interface FileNode {
  name: string;
  size(): number;
}
class File implements FileNode {
  constructor(public name: string, private kb: number) {}
  size() { return this.kb; }
}
class Folder implements FileNode {
  constructor(public name: string, private children: FileNode[] = []) {}
  size() { return this.children.reduce((s, c) => s + c.size(), 0); }
}
```"""),
    ("design-patterns-bridge", "Bridge", "Structurel",
     "Bridge sépare abstraction et implémentation pour éviter l'explosion de classes.",
     "Formes × rendu SVG/Canvas = 6 classes au lieu de 2 axes.",
     "La forme délègue au `Renderer` injecté.",
     "Télécommande et marque de TV interchangeables.",
     """```typescript
interface Renderer {
  drawCircle(x: number, y: number, r: number): void;
}
class SvgRenderer implements Renderer {
  drawCircle(x: number, y: number, r: number) {
    console.log(`<circle cx="${x}" cy="${y}" r="${r}"/>`);
  }
}
class Circle {
  constructor(private renderer: Renderer) {}
  paint() { this.renderer.drawCircle(0, 0, 10); }
}
```"""),
    ("design-patterns-prototype", "Prototype", "Créationnel",
     "Prototype clone un exemplaire au lieu de reconstruire depuis zéro.",
     "Recharger un template 2 Mo depuis la DB à chaque utilisateur.",
     "`clone()` copie l'état ; registre de prototypes nommés.",
     "Photocopieuse.",
     """```typescript
interface Cloneable<T> {
  clone(): T;
}
class GameLevel implements Cloneable<GameLevel> {
  constructor(public map: string[][], public difficulty: number) {}
  clone() {
    return new GameLevel(this.map.map((r) => [...r]), this.difficulty);
  }
}
```"""),
    ("design-patterns-flyweight", "Flyweight", "Structurel",
     "Flyweight partage l'état intrinsèque (texture) ; l'extrinsèque (position) est à part.",
     "10 000 arbres avec mesh dupliqué en mémoire.",
     "Cache de flyweights + données externes légères.",
     "Une notice de bibliothèque, plusieurs lecteurs.",
     """```typescript
type TreeType = { mesh: string; color: string };
const pool = new Map<string, TreeType>();
function getTreeType(key: string): TreeType {
  if (!pool.has(key)) pool.set(key, { mesh: key, color: 'green' });
  return pool.get(key)!;
}
class Tree {
  constructor(public type: TreeType, public x: number, public y: number) {}
}
```"""),
    ("design-patterns-mediator", "Mediator", "Comportemental",
     "Mediator centralise les échanges entre composants (évite N×N).",
     "10 champs React qui se `setState` mutuellement.",
     "Les widgets notifient le médiateur ; il met à jour les autres.",
     "Tour de contrôle aérienne.",
     """```typescript
class OrderFormMediator {
  private total = 0;
  private discount = 0;

  updateTotal(subtotal: number) {
    this.total = subtotal - this.discount;
    console.log('UI total', this.total);
  }

  applyDiscount(percent: number, subtotal: number) {
    this.discount = (subtotal * percent) / 100;
    this.updateTotal(subtotal);
  }
}
```"""),
    ("design-patterns-memento", "Memento", "Comportemental",
     "Memento capture l'état interne pour restauration ultérieure (undo).",
     "Exposer tout l'état de l'éditeur casse l'encapsulation.",
     "Originator crée un memento opaque ; Caretaker stocke la pile.",
     "Sauvegarde de partie ou Ctrl+Z.",
     """```typescript
class EditorSnapshot {
  constructor(readonly content: string) {}
}
class Editor {
  private snapshots: EditorSnapshot[] = [];
  constructor(public content = '') {}

  save() {
    this.snapshots.push(new EditorSnapshot(this.content));
  }

  undo() {
    const s = this.snapshots.pop();
    if (s) this.content = s.content;
  }
}
```"""),
    ("design-patterns-visitor", "Visitor", "Comportemental",
     "Visitor ajoute des opérations sur une hiérarchie sans la modifier.",
     "Ajouter `exportPdf` sur 15 types de nœuds AST.",
     "`accept(visitor)` double dispatch.",
     "Plusieurs experts inspectent le même bâtiment.",
     """```typescript
interface DocVisitor {
  visitHeading(text: string): void;
  visitParagraph(text: string): void;
}

class MarkdownVisitor implements DocVisitor {
  private out: string[] = [];
  visitHeading(t: string) { this.out.push(`# ${t}`); }
  visitParagraph(t: string) { this.out.push(t); }
  result() { return this.out.join('\\n\\n'); }
}
```"""),
    ("design-patterns-interpreter", "Interpreter", "Comportemental",
     "Interpreter représente une grammaire simple comme arbre d'expressions.",
     "Règles « SI age > 18 ET pays = FR » en chaînes non testables.",
     "Chaque règle est un nœud `interpret(ctx)`.",
     "Calculatrice avec + et *.",
     """```typescript
type Ctx = Record<string, number>;
interface Expr {
  eval(ctx: Ctx): number;
}
class Num implements Expr {
  constructor(private v: number) {}
  eval() { return this.v; }
}
class Plus implements Expr {
  constructor(private l: Expr, private r: Expr) {}
  eval(ctx: Ctx) { return this.l.eval(ctx) + this.r.eval(ctx); }
}
```"""),
]:
    ENRICHED[slug] = _p(
        slug, name, fam, one,
        f"{prob}\n\n### Code qui sent le besoin de {name}\n\nLe client contient trop de détails ; extrais les rôles du schéma.",
        idea,
        analogy,
        [("Client", "Déclenche l'opération"), (name, "Structure centrale"), ("Collaborateurs", "Implémentations ou états")],
        ts,
        f"```python\n# {name} — reproduis les classes TypeScript avec dataclasses / ABC\n```",
        ["Plusieurs variantes ou étapes.", "Équipe qui doit nommer la solution en review."],
        ["Script jetable.", "Un seul `if` stable."],
        ["Sur-ingénierie.", "Nom du pattern sans problème associé."],
        [("Voir série", "Articles patterns proches")],
        f"Repère {name} dans un framework que tu utilises (doc ou source).",
        f"Cartographie un module de ton projet : pourrait-il devenir {name} ?",
        f"{name} : {one}",
    )


def apply_enriched() -> None:
    """Remplace ou ajoute les patterns enrichis dans PATTERNS."""
    PATTERNS.update(ENRICHED)
