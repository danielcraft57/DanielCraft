---
title: "Mediator : pattern comportemental expliqué pour juniors"
date: 2026-04-21
excerpt: "Mediator centralise les échanges entre composants (évite N×N)."
type: article
tags: [Design Patterns, GoF, Mediator, Comportemental, TypeScript, Python, junior]
og_image: design-patterns-mediator-1200x630.jpg
series: design-patterns-serie
series_order: 21
---

# Mediator : guide complet pour développeurs juniors

**Famille :** Comportemental · **Série :** Design Patterns GoF · **Article 21/24** · **Popularité :** #20 sur 23

Mediator centralise les échanges entre composants (évite N×N).


<figure>
  <img src="../../assets/images/blog/dp-mediator.svg" alt="Schéma du pattern Mediator" class="schema-inline" width="480" />
  <figcaption>Structure simplifiée du pattern Mediator — les flèches montrent qui dépend de qui.</figcaption>
</figure>

<figure>
  <img src="../../assets/images/blog/illustrations/dp-mediator-banner.webp" alt="Illustration Mediator" class="schema-inline" width="720" />
  <figcaption>Vue d'ensemble visuelle du pattern Mediator (Comportemental).</figcaption>
</figure>


---

## En une phrase

Mediator centralise les échanges entre composants (évite N×N).

---

## Le problème sans ce pattern

10 champs React qui se `setState` mutuellement.

### Code qui sent le besoin de Mediator

Le client contient trop de détails ; extrais les rôles du schéma.

### Symptômes dans ton code

- Fichiers qui grossissent à chaque nouvelle variante.
- Tests difficiles : trop de mocks ou d'effets de bord cachés.
- Tu as peur de toucher une classe car « tout dépend de tout ».

---

## L'idée du pattern Mediator

Les widgets notifient le médiateur ; il met à jour les autres.

| Rôle | Responsabilité |
|------|----------------|
| **Client** | Déclenche l'opération |
| **Mediator** | Structure centrale |
| **Collaborateurs** | Implémentations ou états |

### Analogie du quotidien

Tour de contrôle aérienne.

---

## Exemple complet en TypeScript

```typescript
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
```

### Ce qu'il faut retenir du code

- Le **client** dépend d'abstractions, pas de détails partout.
- Chaque nouvelle variante = **nouvelle classe** (ou module), pas un `if` de plus.
- Nomme tes types pour le **métier** (noms métier explicites, pas `Strategy1`).

---

## Exemple en Python

```python
# Mediator — reproduis les classes TypeScript avec dataclasses / ABC
```

---

## Quand utiliser Mediator

- Plusieurs variantes ou étapes.
- Équipe qui doit nommer la solution en review.

---

## Quand ne pas utiliser Mediator

- Script jetable.
- Un seul `if` stable.

---

## Erreurs fréquentes des juniors

- Sur-ingénierie.
- Nom du pattern sans problème associé.

---

## Patterns proches

- **Voir série** : Articles patterns proches

---

## Dans le monde réel

Repère Mediator dans un framework que tu utilises (doc ou source).

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Non — on teste surtout ta capacité à reconnaître le problème. Le nom Mediator aide à communiquer en équipe.

**Ça remplace les frameworks ?** Non — React, Express ou Spring implémentent souvent ces idées pour toi. Comprendre Mediator te permet de les utiliser correctement.

**Je dois tout refactoriser ?** Non — applique le pattern quand la douleur est réelle (nouveaux bugs à chaque feature).

---

## Mini test unitaire (idée)

```typescript
// Exemple de test : mocke les collaborateurs, vérifie le comportement public
describe('Mediator', () => {
  it('fonctionne avec une variante', () => {
    // Arrange → Act → Assert
  });
});
```

Adapte ce squelette à ton framework (Jest, Vitest, pytest).

---

## Pas à pas : implémenter en 5 étapes

1. **Nomme le problème** — est-ce vraiment Mediator ?
2. **Dessine les rôles** sur papier (client, abstraction, implémentations).
3. **Écris un test** qui décrit le comportement attendu.
4. **Implémente une variante** — valide avant d'en ajouter d'autres.
5. **Documente en équipe** — « ici on utilise Mediator parce que… ».

---

## Checklist code review

- [ ] Le client ne dépend pas de classes concrètes inutiles
- [ ] Pas de sur-abstraction sur un cas unique
- [ ] Tests sur chaque variante / handler / état
- [ ] Nommage métier clair

---

## Exercice pratique (25–35 min)

Cartographie un module de ton projet : pourrait-il devenir Mediator ?

---

## Résumé

Mediator : Mediator centralise les échanges entre composants (évite N×N).

---

## Navigation dans la série

- Précédent : [Chain of Responsibility](/blog/articles/design-patterns-chain-of-responsibility.html)
- Suivant : [Memento](/blog/articles/design-patterns-memento.html)
