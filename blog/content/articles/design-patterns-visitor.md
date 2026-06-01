---
title: "Visitor : pattern comportemental expliqué pour juniors"
date: 2026-04-23
excerpt: "Visitor ajoute des opérations sur une hiérarchie sans la modifier."
type: article
tags: [Design Patterns, GoF, Visitor, Comportemental, TypeScript, Python, junior]
og_image: design-patterns-visitor-1200x630.jpg
series: design-patterns-serie
series_order: 23
---

# Visitor : guide complet pour développeurs juniors

**Famille :** Comportemental · **Série :** Design Patterns GoF · **Article 23/24** · **Popularité :** #22 sur 23

Visitor ajoute des opérations sur une hiérarchie sans la modifier.


<figure>
  <img src="../../assets/images/blog/dp-visitor.svg" alt="Schéma du pattern Visitor" class="schema-inline" width="480" />
  <figcaption>Structure simplifiée du pattern Visitor — les flèches montrent qui dépend de qui.</figcaption>
</figure>

<figure>
  <img src="../../assets/images/blog/illustrations/dp-visitor-banner.webp" alt="Illustration Visitor" class="schema-inline" width="720" />
  <figcaption>Vue d'ensemble visuelle du pattern Visitor (Comportemental).</figcaption>
</figure>


---

## En une phrase

Visitor ajoute des opérations sur une hiérarchie sans la modifier.

---

## Le problème sans ce pattern

Ajouter `exportPdf` sur 15 types de nœuds AST.

### Code qui sent le besoin de Visitor

Le client contient trop de détails ; extrais les rôles du schéma.

### Symptômes dans ton code

- Fichiers qui grossissent à chaque nouvelle variante.
- Tests difficiles : trop de mocks ou d'effets de bord cachés.
- Tu as peur de toucher une classe car « tout dépend de tout ».

---

## L'idée du pattern Visitor

`accept(visitor)` double dispatch.

| Rôle | Responsabilité |
|------|----------------|
| **Client** | Déclenche l'opération |
| **Visitor** | Structure centrale |
| **Collaborateurs** | Implémentations ou états |

### Analogie du quotidien

Plusieurs experts inspectent le même bâtiment.

---

## Exemple complet en TypeScript

```typescript
interface DocVisitor {
  visitHeading(text: string): void;
  visitParagraph(text: string): void;
}

class MarkdownVisitor implements DocVisitor {
  private out: string[] = [];
  visitHeading(t: string) { this.out.push(`# ${t}`); }
  visitParagraph(t: string) { this.out.push(t); }
  result() { return this.out.join('\n\n'); }
}
```

### Ce qu'il faut retenir du code

- Le **client** dépend d'abstractions, pas de détails partout.
- Chaque nouvelle variante = **nouvelle classe** (ou module), pas un `if` de plus.
- Nomme tes types pour le **métier** (noms métier explicites, pas `Strategy1`).

---

## Exemple en Python

```python
# Visitor — reproduis les classes TypeScript avec dataclasses / ABC
```

---

## Quand utiliser Visitor

- Plusieurs variantes ou étapes.
- Équipe qui doit nommer la solution en review.

---

## Quand ne pas utiliser Visitor

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

Repère Visitor dans un framework que tu utilises (doc ou source).

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Non — on teste surtout ta capacité à reconnaître le problème. Le nom Visitor aide à communiquer en équipe.

**Ça remplace les frameworks ?** Non — React, Express ou Spring implémentent souvent ces idées pour toi. Comprendre Visitor te permet de les utiliser correctement.

**Je dois tout refactoriser ?** Non — applique le pattern quand la douleur est réelle (nouveaux bugs à chaque feature).

---

## Mini test unitaire (idée)

```typescript
// Exemple de test : mocke les collaborateurs, vérifie le comportement public
describe('Visitor', () => {
  it('fonctionne avec une variante', () => {
    // Arrange → Act → Assert
  });
});
```

Adapte ce squelette à ton framework (Jest, Vitest, pytest).

---

## Pas à pas : implémenter en 5 étapes

1. **Nomme le problème** — est-ce vraiment Visitor ?
2. **Dessine les rôles** sur papier (client, abstraction, implémentations).
3. **Écris un test** qui décrit le comportement attendu.
4. **Implémente une variante** — valide avant d'en ajouter d'autres.
5. **Documente en équipe** — « ici on utilise Visitor parce que… ».

---

## Checklist code review

- [ ] Le client ne dépend pas de classes concrètes inutiles
- [ ] Pas de sur-abstraction sur un cas unique
- [ ] Tests sur chaque variante / handler / état
- [ ] Nommage métier clair

---

## Exercice pratique (25–35 min)

Cartographie un module de ton projet : pourrait-il devenir Visitor ?

---

## Résumé

Visitor : Visitor ajoute des opérations sur une hiérarchie sans la modifier.

---

## Navigation dans la série

- Précédent : [Memento](/blog/articles/design-patterns-memento.html)
- Suivant : [Interpreter](/blog/articles/design-patterns-interpreter.html)
