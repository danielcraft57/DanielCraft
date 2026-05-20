---
title: "Flyweight : pattern structurel expliqué pour juniors"
date: 2026-04-19
excerpt: "Flyweight partage l'état intrinsèque (texture) ; l'extrinsèque (position) est à part."
type: article
tags: [Design Patterns, GoF, Flyweight, Structurel, TypeScript, Python, junior]
og_image: design-patterns-flyweight-1200x630.jpg
series: design-patterns-serie
series_order: 19
---

# Flyweight : guide complet pour développeurs juniors

**Famille :** Structurel · **Série :** Design Patterns GoF · **Article 19/24** · **Popularité :** #18 sur 23

Flyweight partage l'état intrinsèque (texture) ; l'extrinsèque (position) est à part.


<figure>
  <img src="../../assets/images/blog/dp-flyweight.svg" alt="Schéma du pattern Flyweight" class="schema-inline" width="480" />
  <figcaption>Structure simplifiée du pattern Flyweight — les flèches montrent qui dépend de qui.</figcaption>
</figure>

<figure>
  <img src="../../assets/images/blog/illustrations/dp-flyweight-banner.webp" alt="Illustration Flyweight" class="schema-inline" width="720" />
  <figcaption>Vue d'ensemble visuelle du pattern Flyweight (Structurel).</figcaption>
</figure>


---

## En une phrase

Flyweight partage l'état intrinsèque (texture) ; l'extrinsèque (position) est à part.

---

## Le problème sans ce pattern

10 000 arbres avec mesh dupliqué en mémoire.

### Code qui sent le besoin de Flyweight

Le client contient trop de détails ; extrais les rôles du schéma.

### Symptômes dans ton code

- Fichiers qui grossissent à chaque nouvelle variante.
- Tests difficiles : trop de mocks ou d'effets de bord cachés.
- Tu as peur de toucher une classe car « tout dépend de tout ».

---

## L'idée du pattern Flyweight

Cache de flyweights + données externes légères.

| Rôle | Responsabilité |
|------|----------------|
| **Client** | Déclenche l'opération |
| **Flyweight** | Structure centrale |
| **Collaborateurs** | Implémentations ou états |

### Analogie du quotidien

Une notice de bibliothèque, plusieurs lecteurs.

---

## Exemple complet en TypeScript

```typescript
type TreeType = { mesh: string; color: string };
const pool = new Map<string, TreeType>();
function getTreeType(key: string): TreeType {
  if (!pool.has(key)) pool.set(key, { mesh: key, color: 'green' });
  return pool.get(key)!;
}
class Tree {
  constructor(public type: TreeType, public x: number, public y: number) {}
}
```

### Ce qu'il faut retenir du code

- Le **client** dépend d'abstractions, pas de détails partout.
- Chaque nouvelle variante = **nouvelle classe** (ou module), pas un `if` de plus.
- Nomme tes types pour le **métier** (noms métier explicites, pas `Strategy1`).

---

## Exemple en Python

```python
# Flyweight — reproduis les classes TypeScript avec dataclasses / ABC
```

---

## Quand utiliser Flyweight

- Plusieurs variantes ou étapes.
- Équipe qui doit nommer la solution en review.

---

## Quand ne pas utiliser Flyweight

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

Repère Flyweight dans un framework que tu utilises (doc ou source).

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Non — on teste surtout ta capacité à reconnaître le problème. Le nom Flyweight aide à communiquer en équipe.

**Ça remplace les frameworks ?** Non — React, Express ou Spring implémentent souvent ces idées pour toi. Comprendre Flyweight te permet de les utiliser correctement.

**Je dois tout refactoriser ?** Non — applique le pattern quand la douleur est réelle (nouveaux bugs à chaque feature).

---

## Mini test unitaire (idée)

```typescript
// Exemple de test : mocke les collaborateurs, vérifie le comportement public
describe('Flyweight', () => {
  it('fonctionne avec une variante', () => {
    // Arrange → Act → Assert
  });
});
```

Adapte ce squelette à ton framework (Jest, Vitest, pytest).

---

## Pas à pas : implémenter en 5 étapes

1. **Nomme le problème** — est-ce vraiment Flyweight ?
2. **Dessine les rôles** sur papier (client, abstraction, implémentations).
3. **Écris un test** qui décrit le comportement attendu.
4. **Implémente une variante** — valide avant d'en ajouter d'autres.
5. **Documente en équipe** — « ici on utilise Flyweight parce que… ».

---

## Checklist code review

- [ ] Le client ne dépend pas de classes concrètes inutiles
- [ ] Pas de sur-abstraction sur un cas unique
- [ ] Tests sur chaque variante / handler / état
- [ ] Nommage métier clair

---

## Exercice pratique (25–35 min)

Cartographie un module de ton projet : pourrait-il devenir Flyweight ?

---

## Résumé

Flyweight : Flyweight partage l'état intrinsèque (texture) ; l'extrinsèque (position) est à part.

---

## Navigation dans la série

- Précédent : [Prototype](/blog/articles/design-patterns-prototype.html)
- Suivant : [Chain of Responsibility](/blog/articles/design-patterns-chain-of-responsibility.html)
