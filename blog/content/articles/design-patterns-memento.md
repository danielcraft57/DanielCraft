---
title: "Memento : pattern comportemental expliqué pour juniors"
date: 2026-04-22
excerpt: "Memento capture l'état interne pour restauration ultérieure (undo)."
type: article
tags: [Design Patterns, GoF, Memento, Comportemental, TypeScript, Python, junior]
og_image: design-patterns-memento-1200x630.jpg
series: design-patterns-serie
series_order: 22
---

# Memento : guide complet pour développeurs juniors

**Famille :** Comportemental · **Série :** Design Patterns GoF · **Article 22/24** · **Popularité :** #21 sur 23

Memento capture l'état interne pour restauration ultérieure (undo).

---

## En une phrase

Memento capture l'état interne pour restauration ultérieure (undo).

<figure class="schema-figure">
  <img src="../../assets/images/blog/dp-memento.svg" alt="Schéma du pattern Memento" class="schema-inline" width="480" />
  <figcaption>Structure simplifiée du pattern Memento — les flèches montrent qui dépend de qui.</figcaption>
</figure>

---

## Le problème sans ce pattern

Exposer tout l'état de l'éditeur casse l'encapsulation.

### Code qui sent le besoin de Memento

Le client contient trop de détails ; extrais les rôles du schéma.

### Symptômes dans ton code

- Fichiers qui grossissent à chaque nouvelle variante.
- Tests difficiles : trop de mocks ou d'effets de bord cachés.
- Tu as peur de toucher une classe car « tout dépend de tout ».

---

## L'idée du pattern Memento

Originator crée un memento opaque ; Caretaker stocke la pile.

| Rôle | Responsabilité |
|------|----------------|
| **Client** | Déclenche l'opération |
| **Memento** | Structure centrale |
| **Collaborateurs** | Implémentations ou états |

### Analogie du quotidien

Sauvegarde de partie ou Ctrl+Z.

---

## Exemple complet en TypeScript

```typescript
class EditorSnapshot {
  constructor(readonly content: string) {}
}
class Editor {
  private snapshots: EditorSnapshot[] = [];
  constructor(public content = '') {}

  save() {
    this.snapshots.push(new EditorSnapshot(this.content));
  }

  undo() {
    const s = this.snapshots.pop();
    if (s) this.content = s.content;
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
# Memento — reproduis les classes TypeScript avec dataclasses / ABC
```

---

## Quand utiliser Memento

- Plusieurs variantes ou étapes.
- Équipe qui doit nommer la solution en review.

---

## Quand ne pas utiliser Memento

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

Repère Memento dans un framework que tu utilises (doc ou source).

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Non — on teste surtout ta capacité à reconnaître le problème. Le nom Memento aide à communiquer en équipe.

**Ça remplace les frameworks ?** Non — React, Express ou Spring implémentent souvent ces idées pour toi. Comprendre Memento te permet de les utiliser correctement.

**Je dois tout refactoriser ?** Non — applique le pattern quand la douleur est réelle (nouveaux bugs à chaque feature).

---

## Mini test unitaire (idée)

```typescript
// Exemple de test : mocke les collaborateurs, vérifie le comportement public
describe('Memento', () => {
  it('fonctionne avec une variante', () => {
    // Arrange → Act → Assert
  });
});
```

Adapte ce squelette à ton framework (Jest, Vitest, pytest).

---

## Pas à pas : implémenter en 5 étapes

1. **Nomme le problème** — est-ce vraiment Memento ?
2. **Dessine les rôles** sur papier (client, abstraction, implémentations).
3. **Écris un test** qui décrit le comportement attendu.
4. **Implémente une variante** — valide avant d'en ajouter d'autres.
5. **Documente en équipe** — « ici on utilise Memento parce que… ».

---

## Checklist code review

- [ ] Le client ne dépend pas de classes concrètes inutiles
- [ ] Pas de sur-abstraction sur un cas unique
- [ ] Tests sur chaque variante / handler / état
- [ ] Nommage métier clair

---

## Exercice pratique (25–35 min)

Cartographie un module de ton projet : pourrait-il devenir Memento ?

---

## Résumé

Memento : Memento capture l'état interne pour restauration ultérieure (undo).

---

## Navigation dans la série

- Précédent : [Mediator](/blog/articles/design-patterns-mediator.html)
- Suivant : [Visitor](/blog/articles/design-patterns-visitor.html)
