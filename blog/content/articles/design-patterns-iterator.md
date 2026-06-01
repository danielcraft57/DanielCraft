---
title: "Iterator : pattern comportemental expliqué pour juniors"
date: 2026-04-12
excerpt: "Iterator accède aux éléments d'une collection sans exposer sa structure."
type: article
tags: [Design Patterns, GoF, Iterator, Comportemental, TypeScript, Python, junior]
og_image: design-patterns-iterator-1200x630.jpg
series: design-patterns-serie
series_order: 12
---

# Iterator : guide complet pour développeurs juniors

**Famille :** Comportemental · **Série :** Design Patterns GoF · **Article 12/24** · **Popularité :** #11 sur 23

Iterator accède aux éléments d'une collection sans exposer sa structure.


<figure>
  <img src="../../assets/images/blog/dp-iterator.svg" alt="Schéma du pattern Iterator" class="schema-inline" width="480" />
  <figcaption>Structure simplifiée du pattern Iterator — les flèches montrent qui dépend de qui.</figcaption>
</figure>

<figure>
  <img src="../../assets/images/blog/illustrations/dp-iterator-banner.webp" alt="Illustration Iterator" class="schema-inline" width="720" />
  <figcaption>Vue d'ensemble visuelle du pattern Iterator (Comportemental).</figcaption>
</figure>


---

## En une phrase

Iterator accède aux éléments d'une collection sans exposer sa structure.

---

## Le problème sans ce pattern

Parcourir une liste chaînée avec des `.next` manuels partout.

### Code qui sent le besoin de Iterator

Le client contient trop de détails ; extrais les rôles du schéma.

### Symptômes dans ton code

- Fichiers qui grossissent à chaque nouvelle variante.
- Tests difficiles : trop de mocks ou d'effets de bord cachés.
- Tu as peur de toucher une classe car « tout dépend de tout ».

---

## L'idée du pattern Iterator

Interface commune ; le langage fournit `for..of` / générateurs.

| Rôle | Responsabilité |
|------|----------------|
| **Client** | Déclenche l'opération |
| **Iterator** | Structure centrale |
| **Collaborateurs** | Implémentations ou états |

### Analogie du quotidien

Télécommande chaîne+ / chaîne-.

---

## Exemple complet en TypeScript

```typescript
class BookCollection implements Iterable<string> {
  private books: string[] = [];
  add(b: string) { this.books.push(b); }
  *[Symbol.iterator]() {
    for (const b of this.books) yield b;
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
# Iterator — reproduis les classes TypeScript avec dataclasses / ABC
```

---

## Quand utiliser Iterator

- Plusieurs variantes ou étapes.
- Équipe qui doit nommer la solution en review.

---

## Quand ne pas utiliser Iterator

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

Repère Iterator dans un framework que tu utilises (doc ou source).

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Non — on teste surtout ta capacité à reconnaître le problème. Le nom Iterator aide à communiquer en équipe.

**Ça remplace les frameworks ?** Non — React, Express ou Spring implémentent souvent ces idées pour toi. Comprendre Iterator te permet de les utiliser correctement.

**Je dois tout refactoriser ?** Non — applique le pattern quand la douleur est réelle (nouveaux bugs à chaque feature).

---

## Mini test unitaire (idée)

```typescript
// Exemple de test : mocke les collaborateurs, vérifie le comportement public
describe('Iterator', () => {
  it('fonctionne avec une variante', () => {
    // Arrange → Act → Assert
  });
});
```

Adapte ce squelette à ton framework (Jest, Vitest, pytest).

---

## Pas à pas : implémenter en 5 étapes

1. **Nomme le problème** — est-ce vraiment Iterator ?
2. **Dessine les rôles** sur papier (client, abstraction, implémentations).
3. **Écris un test** qui décrit le comportement attendu.
4. **Implémente une variante** — valide avant d'en ajouter d'autres.
5. **Documente en équipe** — « ici on utilise Iterator parce que… ».

---

## Checklist code review

- [ ] Le client ne dépend pas de classes concrètes inutiles
- [ ] Pas de sur-abstraction sur un cas unique
- [ ] Tests sur chaque variante / handler / état
- [ ] Nommage métier clair

---

## Exercice pratique (25–35 min)

Cartographie un module de ton projet : pourrait-il devenir Iterator ?

---

## Résumé

Iterator : Iterator accède aux éléments d'une collection sans exposer sa structure.

---

## Navigation dans la série

- Précédent : [Builder](/blog/articles/design-patterns-builder.html)
- Suivant : [State](/blog/articles/design-patterns-state.html)
