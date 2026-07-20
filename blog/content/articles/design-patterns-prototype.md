---
title: "Prototype : copier un modele plutot que tout recreer"
date: 2026-04-18
excerpt: "Cloner un objet existant puis ajuster — plus simple parfois que construire a neuf."
type: article
tags: [Design Patterns, GoF, Prototype, Créationnel, TypeScript, Python, junior]
og_image: design-patterns-prototype-1200x630.jpg
series: design-patterns-serie
series_order: 18
---

# Prototype : copier un modele plutot que tout recreer

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-prototype.svg" alt="Schema Prototype" class="schema-inline" width="640" />
  <figcaption>Modele, clone, ajuste, nouvelle copie.</figcaption>
</figure>

**Famille :** Créationnel · **Série :** Design Patterns GoF · **Article 18/24** · **Popularité :** #17 sur 23

Prototype clone un exemplaire au lieu de reconstruire depuis zéro.

---

## En une phrase

Prototype clone un exemplaire au lieu de reconstruire depuis zéro.

---

## Le problème sans ce pattern

Recharger un template 2 Mo depuis la DB à chaque utilisateur.

### Code qui sent le besoin de Prototype

Le client contient trop de détails ; extrais les rôles du schéma.

### Symptômes dans ton code

- Fichiers qui grossissent à chaque nouvelle variante.
- Tests difficiles : trop de mocks ou d'effets de bord cachés.
- Tu as peur de toucher une classe car « tout dépend de tout ».

---

## L'idée du pattern Prototype

`clone()` copie l'état ; registre de prototypes nommés.

| Rôle | Responsabilité |
|------|----------------|
| **Client** | Déclenche l'opération |
| **Prototype** | Structure centrale |
| **Collaborateurs** | Implémentations ou états |

### Analogie du quotidien

Photocopieuse.

---

## Exemple complet en TypeScript

```typescript
interface Cloneable<T> {
  clone(): T;
}
class GameLevel implements Cloneable<GameLevel> {
  constructor(public map: string[][], public difficulty: number) {}
  clone() {
    return new GameLevel(this.map.map((r) => [...r]), this.difficulty);
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
# Prototype — reproduis les classes TypeScript avec dataclasses / ABC
```

---

## Quand utiliser Prototype

- Plusieurs variantes ou étapes.
- Équipe qui doit nommer la solution en review.

---

## Quand ne pas utiliser Prototype

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

Repère Prototype dans un framework que tu utilises (doc ou source).

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Non — on teste surtout ta capacité à reconnaître le problème. Le nom Prototype aide à communiquer en équipe.

**Ça remplace les frameworks ?** Non — React, Express ou Spring implémentent souvent ces idées pour toi. Comprendre Prototype te permet de les utiliser correctement.

**Je dois tout refactoriser ?** Non — applique le pattern quand la douleur est réelle (nouveaux bugs à chaque feature).

---

## Mini test unitaire (idée)

```typescript
// Exemple de test : mocke les collaborateurs, vérifie le comportement public
describe('Prototype', () => {
  it('fonctionne avec une variante', () => {
    // Arrange → Act → Assert
  });
});
```

Adapte ce squelette à ton framework (Jest, Vitest, pytest).

---

## Pas à pas : implémenter en 5 étapes

1. **Nomme le problème** — est-ce vraiment Prototype ?
2. **Dessine les rôles** sur papier (client, abstraction, implémentations).
3. **Écris un test** qui décrit le comportement attendu.
4. **Implémente une variante** — valide avant d'en ajouter d'autres.
5. **Documente en équipe** — « ici on utilise Prototype parce que… ».

---

## Checklist code review

- [ ] Le client ne dépend pas de classes concrètes inutiles
- [ ] Pas de sur-abstraction sur un cas unique
- [ ] Tests sur chaque variante / handler / état
- [ ] Nommage métier clair

---

## Exercice pratique (25–35 min)

Cartographie un module de ton projet : pourrait-il devenir Prototype ?

---

## Résumé

Prototype : Prototype clone un exemplaire au lieu de reconstruire depuis zéro.

---

## Navigation dans la série

- Précédent : [Bridge](/blog/articles/design-patterns-bridge.html)
- Suivant : [Flyweight](/blog/articles/design-patterns-flyweight.html)
