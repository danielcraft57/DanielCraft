---
title: "Strategy : pattern comportemental expliqué pour juniors"
date: 2026-04-05
excerpt: "Strategy encapsule des algorithmes interchangeables injectés au runtime."
type: article
tags: [Design Patterns, GoF, Strategy, Comportemental, TypeScript, Python, junior]
og_image: design-patterns-strategy-1200x630.jpg
series: design-patterns-serie
series_order: 5
---

# Strategy : guide complet pour développeurs juniors

**Famille :** Comportemental · **Série :** Design Patterns GoF · **Article 5/24** · **Popularité :** #4 sur 23

Strategy encapsule des algorithmes interchangeables injectés au runtime.


<figure>
  <img src="../../assets/images/blog/dp-strategy.svg" alt="Schéma du pattern Strategy" class="schema-inline" width="480" />
  <figcaption>Structure simplifiée du pattern Strategy — les flèches montrent qui dépend de qui.</figcaption>
</figure>

<figure>
  <img src="../../assets/images/blog/illustrations/dp-strategy-banner.webp" alt="Illustration Strategy" class="schema-inline" width="720" />
  <figcaption>Vue d'ensemble visuelle du pattern Strategy (Comportemental).</figcaption>
</figure>


---

## En une phrase

Strategy encapsule des algorithmes interchangeables injectés au runtime.

---

## Le problème sans ce pattern

```typescript
function shipping(cost: number, mode: string) {
  if (mode === 'express') return cost + 15;
  if (mode === 'standard') return cost + 5;
  if (mode === 'pickup') return 0;
  throw new Error('mode inconnu');
}
```

### Symptômes dans ton code

- Fichiers qui grossissent à chaque nouvelle variante.
- Tests difficiles : trop de mocks ou d'effets de bord cachés.
- Tu as peur de toucher une classe car « tout dépend de tout ».

---

## L'idée du pattern Strategy

Interface `ShippingStrategy` + implémentations ; le `Checkout` reçoit la stratégie par injection.

| Rôle | Responsabilité |
|------|----------------|
| **Context** | Utilise une Strategy |
| **Strategy** | Interface compute() |
| **ConcreteStrategy** | Express, Standard… |

### Analogie du quotidien

GPS : mode voiture / vélo / piéton — même destination, algorithme différent.

---

## Exemple complet en TypeScript

```typescript
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
```

### Ce qu'il faut retenir du code

- Le **client** dépend d'abstractions, pas de détails partout.
- Chaque nouvelle variante = **nouvelle classe** (ou module), pas un `if` de plus.
- Nomme tes types pour le **métier** (noms métier explicites, pas `Strategy1`).

---

## Exemple en Python

```python
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
```

---

## Quand utiliser Strategy

- Plusieurs variantes d'un même calcul.
- Changer d'algorithme à l'exécution (config utilisateur).

---

## Quand ne pas utiliser Strategy

- Un seul algorithme stable.
- Quelques `if` lisibles suffisent.

---

## Erreurs fréquentes des juniors

- Une stratégie par ligne de `if` sans interface commune.
- Stratégies avec effets de bord cachés.

---

## Patterns proches

- **State** : Change le comportement selon l'état interne
- **Template Method** : Squelette fixe, étapes en sous-classes

---

## Dans le monde réel

Paiement Stripe (cartes, wallets). Tri : `Array.sort(compareFn)` en JS est Strategy.

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Non — on teste surtout ta capacité à reconnaître le problème. Le nom Strategy aide à communiquer en équipe.

**Ça remplace les frameworks ?** Non — React, Express ou Spring implémentent souvent ces idées pour toi. Comprendre Strategy te permet de les utiliser correctement.

**Je dois tout refactoriser ?** Non — applique le pattern quand la douleur est réelle (nouveaux bugs à chaque feature).

---

## Mini test unitaire (idée)

```typescript
// Exemple de test : mocke les collaborateurs, vérifie le comportement public
describe('Strategy', () => {
  it('fonctionne avec une variante', () => {
    // Arrange → Act → Assert
  });
});
```

Adapte ce squelette à ton framework (Jest, Vitest, pytest).

---

## Pas à pas : implémenter en 5 étapes

1. **Nomme le problème** — est-ce vraiment Strategy ?
2. **Dessine les rôles** sur papier (client, abstraction, implémentations).
3. **Écris un test** qui décrit le comportement attendu.
4. **Implémente une variante** — valide avant d'en ajouter d'autres.
5. **Documente en équipe** — « ici on utilise Strategy parce que… ».

---

## Checklist code review

- [ ] Le client ne dépend pas de classes concrètes inutiles
- [ ] Pas de sur-abstraction sur un cas unique
- [ ] Tests sur chaque variante / handler / état
- [ ] Nommage métier clair

---

## Exercice pratique (25–35 min)

Implémente `DiscountStrategy` (étudiant, membre, aucun) pour un panier e-commerce.

---

## Résumé

Strategy = algorithmes plugables — évite les switch qui grossissent à chaque release.

---

## Navigation dans la série

- Précédent : [Observer](/blog/articles/design-patterns-observer.html)
- Suivant : [Decorator](/blog/articles/design-patterns-decorator.html)
