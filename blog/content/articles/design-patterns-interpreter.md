---
title: "Interpreter : comprendre un petit langage"
date: 2026-04-24
excerpt: "Lire une expression simple (regles, formules) et l'evaluer."
type: article
tags: [Design Patterns, GoF, Interpreter, Comportemental, TypeScript, Python, junior]
og_image: design-patterns-interpreter-1200x630.jpg
series: design-patterns-serie
series_order: 24
---

# Interpreter : comprendre un petit langage

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-interpreter.svg" alt="Schema Interpreter" class="schema-inline" width="640" />
  <figcaption>Texte, parse, arbre, evaluer, resultat.</figcaption>
</figure>

**Famille :** Comportemental · **Série :** Design Patterns GoF · **Article 24/24** · **Popularité :** #23 sur 23

Interpreter représente une grammaire simple comme arbre d'expressions.

---

## En une phrase

Interpreter représente une grammaire simple comme arbre d'expressions.

---

## Le problème sans ce pattern

Règles « SI age > 18 ET pays = FR » en chaînes non testables.

### Code qui sent le besoin de Interpreter

Le client contient trop de détails ; extrais les rôles du schéma.

### Symptômes dans ton code

- Fichiers qui grossissent à chaque nouvelle variante.
- Tests difficiles : trop de mocks ou d'effets de bord cachés.
- Tu as peur de toucher une classe car « tout dépend de tout ».

---

## L'idée du pattern Interpreter

Chaque règle est un nœud `interpret(ctx)`.

| Rôle | Responsabilité |
|------|----------------|
| **Client** | Déclenche l'opération |
| **Interpreter** | Structure centrale |
| **Collaborateurs** | Implémentations ou états |

### Analogie du quotidien

Calculatrice avec + et *.

---

## Exemple complet en TypeScript

```typescript
type Ctx = Record<string, number>;
interface Expr {
  eval(ctx: Ctx): number;
}
class Num implements Expr {
  constructor(private v: number) {}
  eval() { return this.v; }
}
class Plus implements Expr {
  constructor(private l: Expr, private r: Expr) {}
  eval(ctx: Ctx) { return this.l.eval(ctx) + this.r.eval(ctx); }
}
```

### Ce qu'il faut retenir du code

- Le **client** dépend d'abstractions, pas de détails partout.
- Chaque nouvelle variante = **nouvelle classe** (ou module), pas un `if` de plus.
- Nomme tes types pour le **métier** (noms métier explicites, pas `Strategy1`).

---

## Exemple en Python

```python
# Interpreter — reproduis les classes TypeScript avec dataclasses / ABC
```

---

## Quand utiliser Interpreter

- Plusieurs variantes ou étapes.
- Équipe qui doit nommer la solution en review.

---

## Quand ne pas utiliser Interpreter

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

Repère Interpreter dans un framework que tu utilises (doc ou source).

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Non — on teste surtout ta capacité à reconnaître le problème. Le nom Interpreter aide à communiquer en équipe.

**Ça remplace les frameworks ?** Non — React, Express ou Spring implémentent souvent ces idées pour toi. Comprendre Interpreter te permet de les utiliser correctement.

**Je dois tout refactoriser ?** Non — applique le pattern quand la douleur est réelle (nouveaux bugs à chaque feature).

---

## Mini test unitaire (idée)

```typescript
// Exemple de test : mocke les collaborateurs, vérifie le comportement public
describe('Interpreter', () => {
  it('fonctionne avec une variante', () => {
    // Arrange → Act → Assert
  });
});
```

Adapte ce squelette à ton framework (Jest, Vitest, pytest).

---

## Pas à pas : implémenter en 5 étapes

1. **Nomme le problème** — est-ce vraiment Interpreter ?
2. **Dessine les rôles** sur papier (client, abstraction, implémentations).
3. **Écris un test** qui décrit le comportement attendu.
4. **Implémente une variante** — valide avant d'en ajouter d'autres.
5. **Documente en équipe** — « ici on utilise Interpreter parce que… ».

---

## Checklist code review

- [ ] Le client ne dépend pas de classes concrètes inutiles
- [ ] Pas de sur-abstraction sur un cas unique
- [ ] Tests sur chaque variante / handler / état
- [ ] Nommage métier clair

---

## Exercice pratique (25–35 min)

Cartographie un module de ton projet : pourrait-il devenir Interpreter ?

---

## Résumé

Interpreter : Interpreter représente une grammaire simple comme arbre d'expressions.

---

## Navigation dans la série

- Précédent : [Visitor](/blog/articles/design-patterns-visitor.html)
- Suivant : [Interpreter](/blog/articles/design-patterns-interpreter.html)
