---
title: "Template Method : pattern comportemental expliqué pour juniors"
date: 2026-04-10
excerpt: "Template Method fixe le squelette d'un algorithme ; les sous-classes surchargent des étapes."
type: article
tags: [Design Patterns, GoF, Template Method, Comportemental, TypeScript, Python, junior]
og_image: design-patterns-template-method-1200x630.jpg
series: design-patterns-serie
series_order: 10
---

# Template Method : guide complet pour développeurs juniors

**Famille :** Comportemental · **Série :** Design Patterns GoF · **Article 10/24** · **Popularité :** #9 sur 23

Template Method fixe le squelette d'un algorithme ; les sous-classes surchargent des étapes.


<figure>
  <img src="../../assets/images/blog/dp-template-method.svg" alt="Schéma du pattern Template Method" class="schema-inline" width="480" />
  <figcaption>Structure simplifiée du pattern Template Method — les flèches montrent qui dépend de qui.</figcaption>
</figure>

<figure>
  <img src="../../assets/images/blog/illustrations/dp-template-method-banner.webp" alt="Illustration Template Method" class="schema-inline" width="720" />
  <figcaption>Vue d'ensemble visuelle du pattern Template Method (Comportemental).</figcaption>
</figure>


---

## En une phrase

Template Method fixe le squelette d'un algorithme ; les sous-classes surchargent des étapes.

---

## Le problème sans ce pattern

Import CSV et JSON partagent extract/load mais pas transform.

### Code qui sent le besoin de Template Method

Le client contient trop de détails ; extrais les rôles du schéma.

### Symptômes dans ton code

- Fichiers qui grossissent à chaque nouvelle variante.
- Tests difficiles : trop de mocks ou d'effets de bord cachés.
- Tu as peur de toucher une classe car « tout dépend de tout ».

---

## L'idée du pattern Template Method

Classe de base avec `run()` final qui appelle des hooks protégés.

| Rôle | Responsabilité |
|------|----------------|
| **Client** | Déclenche l'opération |
| **Template Method** | Structure centrale |
| **Collaborateurs** | Implémentations ou états |

### Analogie du quotidien

Recette : étapes imposées, ingrédients variables.

---

## Exemple complet en TypeScript

```typescript
abstract class ReportPipeline {
  run(source: string) {
    const raw = this.fetch(source);
    const cleaned = this.normalize(raw);
    return this.render(cleaned);
  }
  protected fetch(s: string) { return s; }
  protected abstract normalize(data: string): string;
  protected render(data: string) { return data; }
}

class CsvReport extends ReportPipeline {
  protected normalize(data: string) {
    return data.trim().toUpperCase();
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
# Template Method — reproduis les classes TypeScript avec dataclasses / ABC
```

---

## Quand utiliser Template Method

- Plusieurs variantes ou étapes.
- Équipe qui doit nommer la solution en review.

---

## Quand ne pas utiliser Template Method

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

Repère Template Method dans un framework que tu utilises (doc ou source).

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Non — on teste surtout ta capacité à reconnaître le problème. Le nom Template Method aide à communiquer en équipe.

**Ça remplace les frameworks ?** Non — React, Express ou Spring implémentent souvent ces idées pour toi. Comprendre Template Method te permet de les utiliser correctement.

**Je dois tout refactoriser ?** Non — applique le pattern quand la douleur est réelle (nouveaux bugs à chaque feature).

---

## Mini test unitaire (idée)

```typescript
// Exemple de test : mocke les collaborateurs, vérifie le comportement public
describe('Template Method', () => {
  it('fonctionne avec une variante', () => {
    // Arrange → Act → Assert
  });
});
```

Adapte ce squelette à ton framework (Jest, Vitest, pytest).

---

## Pas à pas : implémenter en 5 étapes

1. **Nomme le problème** — est-ce vraiment Template Method ?
2. **Dessine les rôles** sur papier (client, abstraction, implémentations).
3. **Écris un test** qui décrit le comportement attendu.
4. **Implémente une variante** — valide avant d'en ajouter d'autres.
5. **Documente en équipe** — « ici on utilise Template Method parce que… ».

---

## Checklist code review

- [ ] Le client ne dépend pas de classes concrètes inutiles
- [ ] Pas de sur-abstraction sur un cas unique
- [ ] Tests sur chaque variante / handler / état
- [ ] Nommage métier clair

---

## Exercice pratique (25–35 min)

Cartographie un module de ton projet : pourrait-il devenir Template Method ?

---

## Résumé

Template Method : Template Method fixe le squelette d'un algorithme ; les sous-classes surchargent des étapes.

---

## Navigation dans la série

- Précédent : [Command](/blog/articles/design-patterns-command.html)
- Suivant : [Builder](/blog/articles/design-patterns-builder.html)
