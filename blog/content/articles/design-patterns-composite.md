---
title: "Composite : pattern structurel expliqué pour juniors"
date: 2026-04-16
excerpt: "Composite traite feuilles et conteneurs de la même façon."
type: article
tags: [Design Patterns, GoF, Composite, Structurel, TypeScript, Python, junior]
og_image: design-patterns-composite-1200x630.jpg
series: design-patterns-serie
series_order: 16
---

# Composite : guide complet pour développeurs juniors

**Famille :** Structurel · **Série :** Design Patterns GoF · **Article 16/24** · **Popularité :** #15 sur 23

Composite traite feuilles et conteneurs de la même façon.

---

## En une phrase

Composite traite feuilles et conteneurs de la même façon.

<figure class="schema-figure">
  <img src="../../assets/images/blog/dp-composite.svg" alt="Schéma du pattern Composite" class="schema-inline" width="480" />
  <figcaption>Structure simplifiée du pattern Composite — les flèches montrent qui dépend de qui.</figcaption>
</figure>

---

## Le problème sans ce pattern

Menu avec sous-menus : code différent pour `Item` vs `Menu`.

### Code qui sent le besoin de Composite

Le client contient trop de détails ; extrais les rôles du schéma.

### Symptômes dans ton code

- Fichiers qui grossissent à chaque nouvelle variante.
- Tests difficiles : trop de mocks ou d'effets de bord cachés.
- Tu as peur de toucher une classe car « tout dépend de tout ».

---

## L'idée du pattern Composite

Interface `Component` avec `operation()` récursive.

| Rôle | Responsabilité |
|------|----------------|
| **Client** | Déclenche l'opération |
| **Composite** | Structure centrale |
| **Collaborateurs** | Implémentations ou états |

### Analogie du quotidien

Dossier ou fichier : même commande `size()`.

---

## Exemple complet en TypeScript

```typescript
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
```

### Ce qu'il faut retenir du code

- Le **client** dépend d'abstractions, pas de détails partout.
- Chaque nouvelle variante = **nouvelle classe** (ou module), pas un `if` de plus.
- Nomme tes types pour le **métier** (noms métier explicites, pas `Strategy1`).

---

## Exemple en Python

```python
# Composite — reproduis les classes TypeScript avec dataclasses / ABC
```

---

## Quand utiliser Composite

- Plusieurs variantes ou étapes.
- Équipe qui doit nommer la solution en review.

---

## Quand ne pas utiliser Composite

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

Repère Composite dans un framework que tu utilises (doc ou source).

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Non — on teste surtout ta capacité à reconnaître le problème. Le nom Composite aide à communiquer en équipe.

**Ça remplace les frameworks ?** Non — React, Express ou Spring implémentent souvent ces idées pour toi. Comprendre Composite te permet de les utiliser correctement.

**Je dois tout refactoriser ?** Non — applique le pattern quand la douleur est réelle (nouveaux bugs à chaque feature).

---

## Mini test unitaire (idée)

```typescript
// Exemple de test : mocke les collaborateurs, vérifie le comportement public
describe('Composite', () => {
  it('fonctionne avec une variante', () => {
    // Arrange → Act → Assert
  });
});
```

Adapte ce squelette à ton framework (Jest, Vitest, pytest).

---

## Pas à pas : implémenter en 5 étapes

1. **Nomme le problème** — est-ce vraiment Composite ?
2. **Dessine les rôles** sur papier (client, abstraction, implémentations).
3. **Écris un test** qui décrit le comportement attendu.
4. **Implémente une variante** — valide avant d'en ajouter d'autres.
5. **Documente en équipe** — « ici on utilise Composite parce que… ».

---

## Checklist code review

- [ ] Le client ne dépend pas de classes concrètes inutiles
- [ ] Pas de sur-abstraction sur un cas unique
- [ ] Tests sur chaque variante / handler / état
- [ ] Nommage métier clair

---

## Exercice pratique (25–35 min)

Cartographie un module de ton projet : pourrait-il devenir Composite ?

---

## Résumé

Composite : Composite traite feuilles et conteneurs de la même façon.

---

## Navigation dans la série

- Précédent : [Abstract Factory](/blog/articles/design-patterns-abstract-factory.html)
- Suivant : [Bridge](/blog/articles/design-patterns-bridge.html)
