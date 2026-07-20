---
title: "Abstract Factory : des familles d'objets qui vont ensemble"
date: 2026-04-15
excerpt: "Creer des lots coherents (theme clair / sombre) sans melanger les pieces."
type: article
tags: [Design Patterns, GoF, Abstract Factory, Créationnel, TypeScript, Python, junior]
og_image: design-patterns-abstract-factory-1200x630.jpg
series: design-patterns-serie
series_order: 15
---

# Abstract Factory : des familles d'objets qui vont ensemble

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-abstract-factory.svg" alt="Schema Abstract Factory" class="schema-inline" width="640" />
  <figcaption>Familles assorties, ne pas melanger.</figcaption>
</figure>

**Famille :** Créationnel · **Série :** Design Patterns GoF · **Article 15/24** · **Popularité :** #14 sur 23

Abstract Factory crée des familles d'objets cohérents (UI kit, thème).

---

## En une phrase

Abstract Factory crée des familles d'objets cohérents (UI kit, thème).

---

## Le problème sans ce pattern

Boutons Windows mélangés avec checkboxes Mac.

### Code qui sent le besoin de Abstract Factory

Le client contient trop de détails ; extrais les rôles du schéma.

### Symptômes dans ton code

- Fichiers qui grossissent à chaque nouvelle variante.
- Tests difficiles : trop de mocks ou d'effets de bord cachés.
- Tu as peur de toucher une classe car « tout dépend de tout ».

---

## L'idée du pattern Abstract Factory

Une factory par thème : `createButton` + `createCheckbox` cohérents.

| Rôle | Responsabilité |
|------|----------------|
| **Client** | Déclenche l'opération |
| **Abstract Factory** | Structure centrale |
| **Collaborateurs** | Implémentations ou états |

### Analogie du quotidien

Kit IKEA : vis et plateaux du même carton.

---

## Exemple complet en TypeScript

```typescript
interface UIFactory {
  createButton(): { label: string; style: string };
  createCheckbox(): { checked: boolean; style: string };
}
class DarkFactory implements UIFactory {
  createButton() { return { label: 'OK', style: 'dark-rounded' }; }
  createCheckbox() { return { checked: false, style: 'dark-rounded' }; }
}
```

### Ce qu'il faut retenir du code

- Le **client** dépend d'abstractions, pas de détails partout.
- Chaque nouvelle variante = **nouvelle classe** (ou module), pas un `if` de plus.
- Nomme tes types pour le **métier** (noms métier explicites, pas `Strategy1`).

---

## Exemple en Python

```python
# Abstract Factory — reproduis les classes TypeScript avec dataclasses / ABC
```

---

## Quand utiliser Abstract Factory

- Plusieurs variantes ou étapes.
- Équipe qui doit nommer la solution en review.

---

## Quand ne pas utiliser Abstract Factory

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

Repère Abstract Factory dans un framework que tu utilises (doc ou source).

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Non — on teste surtout ta capacité à reconnaître le problème. Le nom Abstract Factory aide à communiquer en équipe.

**Ça remplace les frameworks ?** Non — React, Express ou Spring implémentent souvent ces idées pour toi. Comprendre Abstract Factory te permet de les utiliser correctement.

**Je dois tout refactoriser ?** Non — applique le pattern quand la douleur est réelle (nouveaux bugs à chaque feature).

---

## Mini test unitaire (idée)

```typescript
// Exemple de test : mocke les collaborateurs, vérifie le comportement public
describe('Abstract Factory', () => {
  it('fonctionne avec une variante', () => {
    // Arrange → Act → Assert
  });
});
```

Adapte ce squelette à ton framework (Jest, Vitest, pytest).

---

## Pas à pas : implémenter en 5 étapes

1. **Nomme le problème** — est-ce vraiment Abstract Factory ?
2. **Dessine les rôles** sur papier (client, abstraction, implémentations).
3. **Écris un test** qui décrit le comportement attendu.
4. **Implémente une variante** — valide avant d'en ajouter d'autres.
5. **Documente en équipe** — « ici on utilise Abstract Factory parce que… ».

---

## Checklist code review

- [ ] Le client ne dépend pas de classes concrètes inutiles
- [ ] Pas de sur-abstraction sur un cas unique
- [ ] Tests sur chaque variante / handler / état
- [ ] Nommage métier clair

---

## Exercice pratique (25–35 min)

Cartographie un module de ton projet : pourrait-il devenir Abstract Factory ?

---

## Résumé

Abstract Factory : Abstract Factory crée des familles d'objets cohérents (UI kit, thème).

---

## Navigation dans la série

- Précédent : [Proxy](/blog/articles/design-patterns-proxy.html)
- Suivant : [Composite](/blog/articles/design-patterns-composite.html)
