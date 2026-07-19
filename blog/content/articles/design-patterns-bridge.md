---
title: "Bridge : pattern structurel expliqué pour juniors"
date: 2026-04-17
excerpt: "Bridge sépare abstraction et implémentation pour éviter l'explosion de classes."
type: article
tags: [Design Patterns, GoF, Bridge, Structurel, TypeScript, Python, junior]
og_image: design-patterns-bridge-1200x630.jpg
series: design-patterns-serie
series_order: 17
---

# Bridge : guide complet pour développeurs juniors

**Famille :** Structurel · **Série :** Design Patterns GoF · **Article 17/24** · **Popularité :** #16 sur 23

Bridge sépare abstraction et implémentation pour éviter l'explosion de classes.

---

## En une phrase

Bridge sépare abstraction et implémentation pour éviter l'explosion de classes.

<figure class="schema-figure">
  <img src="../../assets/images/blog/dp-bridge.svg" alt="Schéma du pattern Bridge" class="schema-inline" width="480" />
  <figcaption>Structure simplifiée du pattern Bridge — les flèches montrent qui dépend de qui.</figcaption>
</figure>

---

## Le problème sans ce pattern

Formes × rendu SVG/Canvas = 6 classes au lieu de 2 axes.

### Code qui sent le besoin de Bridge

Le client contient trop de détails ; extrais les rôles du schéma.

### Symptômes dans ton code

- Fichiers qui grossissent à chaque nouvelle variante.
- Tests difficiles : trop de mocks ou d'effets de bord cachés.
- Tu as peur de toucher une classe car « tout dépend de tout ».

---

## L'idée du pattern Bridge

La forme délègue au `Renderer` injecté.

| Rôle | Responsabilité |
|------|----------------|
| **Client** | Déclenche l'opération |
| **Bridge** | Structure centrale |
| **Collaborateurs** | Implémentations ou états |

### Analogie du quotidien

Télécommande et marque de TV interchangeables.

---

## Exemple complet en TypeScript

```typescript
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
```

### Ce qu'il faut retenir du code

- Le **client** dépend d'abstractions, pas de détails partout.
- Chaque nouvelle variante = **nouvelle classe** (ou module), pas un `if` de plus.
- Nomme tes types pour le **métier** (noms métier explicites, pas `Strategy1`).

---

## Exemple en Python

```python
# Bridge — reproduis les classes TypeScript avec dataclasses / ABC
```

---

## Quand utiliser Bridge

- Plusieurs variantes ou étapes.
- Équipe qui doit nommer la solution en review.

---

## Quand ne pas utiliser Bridge

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

Repère Bridge dans un framework que tu utilises (doc ou source).

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Non — on teste surtout ta capacité à reconnaître le problème. Le nom Bridge aide à communiquer en équipe.

**Ça remplace les frameworks ?** Non — React, Express ou Spring implémentent souvent ces idées pour toi. Comprendre Bridge te permet de les utiliser correctement.

**Je dois tout refactoriser ?** Non — applique le pattern quand la douleur est réelle (nouveaux bugs à chaque feature).

---

## Mini test unitaire (idée)

```typescript
// Exemple de test : mocke les collaborateurs, vérifie le comportement public
describe('Bridge', () => {
  it('fonctionne avec une variante', () => {
    // Arrange → Act → Assert
  });
});
```

Adapte ce squelette à ton framework (Jest, Vitest, pytest).

---

## Pas à pas : implémenter en 5 étapes

1. **Nomme le problème** — est-ce vraiment Bridge ?
2. **Dessine les rôles** sur papier (client, abstraction, implémentations).
3. **Écris un test** qui décrit le comportement attendu.
4. **Implémente une variante** — valide avant d'en ajouter d'autres.
5. **Documente en équipe** — « ici on utilise Bridge parce que… ».

---

## Checklist code review

- [ ] Le client ne dépend pas de classes concrètes inutiles
- [ ] Pas de sur-abstraction sur un cas unique
- [ ] Tests sur chaque variante / handler / état
- [ ] Nommage métier clair

---

## Exercice pratique (25–35 min)

Cartographie un module de ton projet : pourrait-il devenir Bridge ?

---

## Résumé

Bridge : Bridge sépare abstraction et implémentation pour éviter l'explosion de classes.

---

## Navigation dans la série

- Précédent : [Composite](/blog/articles/design-patterns-composite.html)
- Suivant : [Prototype](/blog/articles/design-patterns-prototype.html)
