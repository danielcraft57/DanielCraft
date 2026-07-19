---
title: "Observer : pattern comportemental expliqué pour juniors"
date: 2026-04-04
excerpt: "Le Observer notifie automatiquement tous les abonnés quand l'état d'un sujet change."
type: article
tags: [Design Patterns, GoF, Observer, Comportemental, TypeScript, Python, junior]
og_image: design-patterns-observer-1200x630.jpg
series: design-patterns-serie
series_order: 4
---

# Observer : guide complet pour développeurs juniors

**Famille :** Comportemental · **Série :** Design Patterns GoF · **Article 4/24** · **Popularité :** #3 sur 23

Le Observer notifie automatiquement tous les abonnés quand l'état d'un sujet change.

---

## En une phrase

Le Observer notifie automatiquement tous les abonnés quand l'état d'un sujet change.

<figure class="schema-figure">
  <img src="../../assets/images/blog/dp-observer.svg" alt="Schéma du pattern Observer" class="schema-inline" width="480" />
  <figcaption>Structure simplifiée du pattern Observer — les flèches montrent qui dépend de qui.</figcaption>
</figure>

---

## Le problème sans ce pattern

```typescript
class Product {
  setStock(n: number) {
    this.stock = n;
    new EmailService().sendLowStockAlert(this);
    new Dashboard().refresh(this);
    new SlackNotifier().post(this.stock);
  }
}
```
Chaque nouveau canal modifie `Product`. Une erreur Slack peut casser la mise à jour du stock.

### Symptômes dans ton code

- Fichiers qui grossissent à chaque nouvelle variante.
- Tests difficiles : trop de mocks ou d'effets de bord cachés.
- Tu as peur de toucher une classe car « tout dépend de tout ».

---

## L'idée du pattern Observer

Sépare **Subject** (état + abonnés) et **Observer** (réactions). Le sujet appelle `notify()` sans connaître les détails.

| Rôle | Responsabilité |
|------|----------------|
| **Subject** | attach / detach / notify |
| **Observer** | update(event) |
| **ConcreteSubject** | État métier (stock, panier…) |

### Analogie du quotidien

Newsletter : tu t'abonnes, l'éditeur publie, tous les abonnés reçoivent le mail.

---

## Exemple complet en TypeScript

```typescript
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
```

### Ce qu'il faut retenir du code

- Le **client** dépend d'abstractions, pas de détails partout.
- Chaque nouvelle variante = **nouvelle classe** (ou module), pas un `if` de plus.
- Nomme tes types pour le **métier** (noms métier explicites, pas `Strategy1`).

---

## Exemple en Python

```python
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
```

---

## Quand utiliser Observer

- Plusieurs réactions au même changement d'état.
- Ajouter des réactions sans modifier la source.
- UI réactive (modèle → vues).

---

## Quand ne pas utiliser Observer

- Une seule réaction → simple callback.
- Microservices distribués → bus de messages (Kafka), pas Observer in-process.
- Oublier le désabonnement → fuite mémoire.

---

## Erreurs fréquentes des juniors

- Pas de `unsubscribe` en SPA.
- Notifier pendant une mutation partielle.
- Observer qui modifie le sujet dans `update` → boucles.
- EventBus global non typé.

---

## Patterns proches

- **Mediator** : Coordonne des collègues, ne diffuse pas un état
- **Pub/Sub** : Bus intermédiaire optionnel

---

## Comparaisons utiles

| Approche | Usage |
|----------|-------|
| Observer GoF | Domaine métier clair |
| EventEmitter | Modules techniques Node |
| RxJS | Flux complexes avec opérateurs |
| Store React/Zustand | UI : le sujet est le store |

---

## Dans le monde réel

React : hooks + state. Vue : réactivité. Node : `EventEmitter`. Domain-Driven Design : événements de domaine.

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Non — on teste surtout ta capacité à reconnaître le problème. Le nom Observer aide à communiquer en équipe.

**Ça remplace les frameworks ?** Non — React, Express ou Spring implémentent souvent ces idées pour toi. Comprendre Observer te permet de les utiliser correctement.

**Je dois tout refactoriser ?** Non — applique le pattern quand la douleur est réelle (nouveaux bugs à chaque feature).

---

## Mini test unitaire (idée)

```typescript
// Exemple de test : mocke les collaborateurs, vérifie le comportement public
describe('Observer', () => {
  it('fonctionne avec une variante', () => {
    // Arrange → Act → Assert
  });
});
```

Adapte ce squelette à ton framework (Jest, Vitest, pytest).

---

## Pas à pas : implémenter en 5 étapes

1. **Nomme le problème** — est-ce vraiment Observer ?
2. **Dessine les rôles** sur papier (client, abstraction, implémentations).
3. **Écris un test** qui décrit le comportement attendu.
4. **Implémente une variante** — valide avant d'en ajouter d'autres.
5. **Documente en équipe** — « ici on utilise Observer parce que… ».

---

## Checklist code review

- [ ] Le client ne dépend pas de classes concrètes inutiles
- [ ] Pas de sur-abstraction sur un cas unique
- [ ] Tests sur chaque variante / handler / état
- [ ] Nommage métier clair

---

## Exercice pratique (25–35 min)

Crée `CartSubject` + observers badge panier et analytics. Ajoute un 3e observer sans toucher `CartSubject`. Teste le désabonnement.

---

## Résumé

Subject notifie, Observer réagit — découplage fort ; pense toujours au cycle de vie des abonnements.

---

## Navigation dans la série

- Précédent : [Factory Method](/blog/articles/design-patterns-factory-method.html)
- Suivant : [Strategy](/blog/articles/design-patterns-strategy.html)
