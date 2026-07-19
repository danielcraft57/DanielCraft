---
title: "Chain of Responsibility : pattern comportemental expliqué pour juniors"
date: 2026-04-20
excerpt: "Chaque handler décide de traiter ou de passer au suivant."
type: article
tags: [Design Patterns, GoF, Chain of Responsibility, Comportemental, TypeScript, Python, junior]
og_image: design-patterns-chain-of-responsibility-1200x630.jpg
series: design-patterns-serie
series_order: 20
---

# Chain of Responsibility : guide complet pour développeurs juniors

**Famille :** Comportemental · **Série :** Design Patterns GoF · **Article 20/24** · **Popularité :** #19 sur 23

Chaque handler décide de traiter ou de passer au suivant.

---

## En une phrase

Chaque handler décide de traiter ou de passer au suivant.

<figure class="schema-figure">
  <img src="../../assets/images/blog/dp-chain-of-responsibility.svg" alt="Schéma du pattern Chain of Responsibility" class="schema-inline" width="480" />
  <figcaption>Structure simplifiée du pattern Chain of Responsibility — les flèches montrent qui dépend de qui.</figcaption>
</figure>

---

## Le problème sans ce pattern

Un seul gros middleware qui mélange auth, logs et métier.

```typescript
// Avant : un seul bloc qui fait tout\nif (!user) throw new Error();\nconsole.log(req.url);
```

### Symptômes dans ton code

- Fichiers qui grossissent à chaque nouvelle variante.
- Tests difficiles : trop de mocks ou d'effets de bord cachés.
- Tu as peur de toucher une classe car « tout dépend de tout ».

---

## L'idée du pattern Chain of Responsibility

Chaîne de maillons : `auth → log → rateLimit → handler`.

| Rôle | Responsabilité |
|------|----------------|
| **Handler/Builder** | Rôle central |
| **Client** | Compose la chaîne ou le builder |

### Analogie du quotidien

Support : niveau 1, puis 2, puis expert.

---

## Exemple complet en TypeScript

```typescript
type Context = { userId?: string; path: string };
type Next = () => Promise<void>;

type Middleware = (ctx: Context, next: Next) => Promise<void>;

const auth: Middleware = async (ctx, next) => {
  if (!ctx.userId) throw new Error('401');
  await next();
};

const logger: Middleware = async (ctx, next) => {
  console.log(ctx.path);
  await next();
};

function run(chain: Middleware[], ctx: Context) {
  let i = 0;
  const next = async () => {
    if (i >= chain.length) return;
    await chain[i++](ctx, next);
  };
  return next();
}
```

### Ce qu'il faut retenir du code

- Le **client** dépend d'abstractions, pas de détails partout.
- Chaque nouvelle variante = **nouvelle classe** (ou module), pas un `if` de plus.
- Nomme tes types pour le **métier** (noms métier explicites, pas `Strategy1`).

---

## Exemple en Python

```python
# Portage Chain of Responsibility : reprendre la structure TypeScript ci-dessus
```

---

## Quand utiliser Chain of Responsibility

- Variantes multiples de chain of responsibility.
- Évolution fréquente du flux.

---

## Quand ne pas utiliser Chain of Responsibility

- Cas unique et figé.
- Librairie standard suffisante.

---

## Erreurs fréquentes des juniors

- Chaîne trop longue sans tests par maillon.
- Handler qui fait tout.

---

## Patterns proches

- **Decorator** : Ajoute une couche systématiquement

---

## Dans le monde réel

Express, Koa, ASP.NET pipeline, validation de formulaires par étapes.

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Non — on teste surtout ta capacité à reconnaître le problème. Le nom Chain of Responsibility aide à communiquer en équipe.

**Ça remplace les frameworks ?** Non — React, Express ou Spring implémentent souvent ces idées pour toi. Comprendre Chain of Responsibility te permet de les utiliser correctement.

**Je dois tout refactoriser ?** Non — applique le pattern quand la douleur est réelle (nouveaux bugs à chaque feature).

---

## Mini test unitaire (idée)

```typescript
// Exemple de test : mocke les collaborateurs, vérifie le comportement public
describe('Chain of Responsibility', () => {
  it('fonctionne avec une variante', () => {
    // Arrange → Act → Assert
  });
});
```

Adapte ce squelette à ton framework (Jest, Vitest, pytest).

---

## Pas à pas : implémenter en 5 étapes

1. **Nomme le problème** — est-ce vraiment Chain of Responsibility ?
2. **Dessine les rôles** sur papier (client, abstraction, implémentations).
3. **Écris un test** qui décrit le comportement attendu.
4. **Implémente une variante** — valide avant d'en ajouter d'autres.
5. **Documente en équipe** — « ici on utilise Chain of Responsibility parce que… ».

---

## Checklist code review

- [ ] Le client ne dépend pas de classes concrètes inutiles
- [ ] Pas de sur-abstraction sur un cas unique
- [ ] Tests sur chaque variante / handler / état
- [ ] Nommage métier clair

---

## Exercice pratique (25–35 min)

Refactorise un bout de code vers Chain of Responsibility et écris 2 tests.

---

## Résumé

Chain of Responsibility : Chaque handler décide de traiter ou de passer au suivant.

---

## Navigation dans la série

- Précédent : [Flyweight](/blog/articles/design-patterns-flyweight.html)
- Suivant : [Mediator](/blog/articles/design-patterns-mediator.html)
