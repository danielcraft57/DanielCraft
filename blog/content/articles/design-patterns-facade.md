---
title: "Facade : une porte simple vers un systeme complexe"
date: 2026-04-08
excerpt: "Cacher 10 appels techniques derriere une methode claire."
type: article
tags: [Design Patterns, GoF, Facade, Structurel, TypeScript, Python, junior]
og_image: design-patterns-facade-1200x630.jpg
series: design-patterns-serie
series_order: 8
---

# Facade : une porte simple vers un systeme complexe

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-facade.svg" alt="Schema Facade" class="schema-inline" width="640" />
  <figcaption>Une methode claire versus dix appels techniques.</figcaption>
</figure>

**Famille :** Structurel · **Série :** Design Patterns GoF · **Article 8/24** · **Popularité :** #7 sur 23

Facade offre une interface simple qui orchestre un sous-système complexe.

---

## En une phrase

Facade offre une interface simple qui orchestre un sous-système complexe.

---

## Le problème sans ce pattern

Démarrer l'application oblige chaque module à connaître l'ordre d'initialisation :

```typescript
await loadConfig();
const db = await connectDb(process.env.DB_URL);
await migrate(db);
const cache = await connectRedis();
await warmCache(cache, db);
queue.start();
http.listen(3000);
```

Un oubli ou un mauvais ordre = crash au boot.

### Symptômes dans ton code

- Fichiers qui grossissent à chaque nouvelle variante.
- Tests difficiles : trop de mocks ou d'effets de bord cachés.
- Tu as peur de toucher une classe car « tout dépend de tout ».

---

## L'idée du pattern Facade

`AppFacade.start()` encapsule les étapes. Les modules internes restent découplés ; seul la facade connaît l'orchestration.

| Rôle | Responsabilité |
|------|----------------|
| **Client** | main.ts, CLI |
| **Facade** | start(), stop() |
| **Subsystem** | DB, cache, queue… |

### Analogie du quotidien

Réception d'**hôtel** : une clé, pas besoin de gérer ménage, cuisine et spa séparément.

---

## Exemple complet en TypeScript

```typescript
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
```

### Ce qu'il faut retenir du code

- Le **client** dépend d'abstractions, pas de détails partout.
- Chaque nouvelle variante = **nouvelle classe** (ou module), pas un `if` de plus.
- Nomme tes types pour le **métier** (noms métier explicites, pas `Strategy1`).

---

## Exemple en Python

```python
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
```

---

## Quand utiliser Facade

- Sous-système avec 5+ composants à initialiser.
- Tu veux une API stable pour des clients externes.
- Onboarding : un seul point d'entrée documenté.

---

## Quand ne pas utiliser Facade

- Le sous-système tient en 2 appels — pas besoin de facade.
- La facade devient un God Object qui connaît tout le métier.

---

## Erreurs fréquentes des juniors

- Mettre la logique métier dans la facade.
- Exposer tous les subsystèmes au client (perd l'intérêt).

---

## Patterns proches

- **Adapter** : Une classe legacy
- **Mediator** : Coordonne des collègues égaux

---

## Dans le monde réel

Frameworks `NestFactory.create()`, `SpringApplication.run()`. Scripts `docker compose up` qui masquent réseau + volumes.

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Non — on teste surtout ta capacité à reconnaître le problème. Le nom Facade aide à communiquer en équipe.

**Ça remplace les frameworks ?** Non — React, Express ou Spring implémentent souvent ces idées pour toi. Comprendre Facade te permet de les utiliser correctement.

**Je dois tout refactoriser ?** Non — applique le pattern quand la douleur est réelle (nouveaux bugs à chaque feature).

---

## Mini test unitaire (idée)

```typescript
// Exemple de test : mocke les collaborateurs, vérifie le comportement public
describe('Facade', () => {
  it('fonctionne avec une variante', () => {
    // Arrange → Act → Assert
  });
});
```

Adapte ce squelette à ton framework (Jest, Vitest, pytest).

---

## Pas à pas : implémenter en 5 étapes

1. **Nomme le problème** — est-ce vraiment Facade ?
2. **Dessine les rôles** sur papier (client, abstraction, implémentations).
3. **Écris un test** qui décrit le comportement attendu.
4. **Implémente une variante** — valide avant d'en ajouter d'autres.
5. **Documente en équipe** — « ici on utilise Facade parce que… ».

---

## Checklist code review

- [ ] Le client ne dépend pas de classes concrètes inutiles
- [ ] Pas de sur-abstraction sur un cas unique
- [ ] Tests sur chaque variante / handler / état
- [ ] Nommage métier clair

---

## Exercice pratique (25–35 min)

Écris `DeployFacade.deploy(env)` qui enchaîne build, tests, push image, rollout K8s — une commande pour l'équipe.

---

## Résumé

Facade = point d'entrée simple vers la complexité.

---

## Navigation dans la série

- Précédent : [Adapter](/blog/articles/design-patterns-adapter.html)
- Suivant : [Command](/blog/articles/design-patterns-command.html)
