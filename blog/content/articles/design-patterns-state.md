---
title: "State : pattern comportemental expliqué pour juniors"
date: 2026-04-13
excerpt: "State délègue le comportement à des objets d'état selon le contexte."
type: article
tags: [Design Patterns, GoF, State, Comportemental, TypeScript, Python, junior]
og_image: design-patterns-state-1200x630.jpg
series: design-patterns-serie
series_order: 13
---

# State : guide complet pour développeurs juniors

**Famille :** Comportemental · **Série :** Design Patterns GoF · **Article 13/24** · **Popularité :** #12 sur 23

State délègue le comportement à des objets d'état selon le contexte.

---

## En une phrase

State délègue le comportement à des objets d'état selon le contexte.

<figure class="schema-figure">
  <img src="../../assets/images/blog/dp-state.svg" alt="Schéma du pattern State" class="schema-inline" width="480" />
  <figcaption>Structure simplifiée du pattern State — les flèches montrent qui dépend de qui.</figcaption>
</figure>

---

## Le problème sans ce pattern

Un `switch(status)` de 80 lignes pour une commande e-commerce.

```typescript
// Avant : un seul bloc qui fait tout\nif (!user) throw new Error();\nconsole.log(req.url);
```

### Symptômes dans ton code

- Fichiers qui grossissent à chaque nouvelle variante.
- Tests difficiles : trop de mocks ou d'effets de bord cachés.
- Tu as peur de toucher une classe car « tout dépend de tout ».

---

## L'idée du pattern State

Chaque état (`Draft`, `Paid`, `Shipped`) implémente les transitions autorisées.

| Rôle | Responsabilité |
|------|----------------|
| **Handler/Builder** | Rôle central |
| **Client** | Compose la chaîne ou le builder |

### Analogie du quotidien

Distributeur : pas de soda tant que pas payé.

---

## Exemple complet en TypeScript

```typescript
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
```

### Ce qu'il faut retenir du code

- Le **client** dépend d'abstractions, pas de détails partout.
- Chaque nouvelle variante = **nouvelle classe** (ou module), pas un `if` de plus.
- Nomme tes types pour le **métier** (noms métier explicites, pas `Strategy1`).

---

## Exemple en Python

```python
# Portage State : reprendre la structure TypeScript ci-dessus
```

---

## Quand utiliser State

- Variantes multiples de state.
- Évolution fréquente du flux.

---

## Quand ne pas utiliser State

- Cas unique et figé.
- Librairie standard suffisante.

---

## Erreurs fréquentes des juniors

- Chaîne trop longue sans tests par maillon.
- Handler qui fait tout.

---

## Patterns proches

- **Decorator** : Ajoute une couche systématiquement

---

## Dans le monde réel

Workflow Jira, formulaires multi-étapes, jeux (menu / play / pause).

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Non — on teste surtout ta capacité à reconnaître le problème. Le nom State aide à communiquer en équipe.

**Ça remplace les frameworks ?** Non — React, Express ou Spring implémentent souvent ces idées pour toi. Comprendre State te permet de les utiliser correctement.

**Je dois tout refactoriser ?** Non — applique le pattern quand la douleur est réelle (nouveaux bugs à chaque feature).

---

## Mini test unitaire (idée)

```typescript
// Exemple de test : mocke les collaborateurs, vérifie le comportement public
describe('State', () => {
  it('fonctionne avec une variante', () => {
    // Arrange → Act → Assert
  });
});
```

Adapte ce squelette à ton framework (Jest, Vitest, pytest).

---

## Pas à pas : implémenter en 5 étapes

1. **Nomme le problème** — est-ce vraiment State ?
2. **Dessine les rôles** sur papier (client, abstraction, implémentations).
3. **Écris un test** qui décrit le comportement attendu.
4. **Implémente une variante** — valide avant d'en ajouter d'autres.
5. **Documente en équipe** — « ici on utilise State parce que… ».

---

## Checklist code review

- [ ] Le client ne dépend pas de classes concrètes inutiles
- [ ] Pas de sur-abstraction sur un cas unique
- [ ] Tests sur chaque variante / handler / état
- [ ] Nommage métier clair

---

## Exercice pratique (25–35 min)

Refactorise un bout de code vers State et écris 2 tests.

---

## Résumé

State : State délègue le comportement à des objets d'état selon le contexte.

---

## Navigation dans la série

- Précédent : [Iterator](/blog/articles/design-patterns-iterator.html)
- Suivant : [Proxy](/blog/articles/design-patterns-proxy.html)
