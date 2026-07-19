---
title: "Builder : pattern créationnel expliqué pour juniors"
date: 2026-04-11
excerpt: "Builder construit pas à pas un objet complexe avec une API fluide."
type: article
tags: [Design Patterns, GoF, Builder, Créationnel, TypeScript, Python, junior]
og_image: design-patterns-builder-1200x630.jpg
series: design-patterns-serie
series_order: 11
---

# Builder : guide complet pour développeurs juniors

**Famille :** Créationnel · **Série :** Design Patterns GoF · **Article 11/24** · **Popularité :** #10 sur 23

Builder construit pas à pas un objet complexe avec une API fluide.

---

## En une phrase

Builder construit pas à pas un objet complexe avec une API fluide.

<figure class="schema-figure">
  <img src="../../assets/images/blog/dp-builder.svg" alt="Schéma du pattern Builder" class="schema-inline" width="480" />
  <figcaption>Structure simplifiée du pattern Builder — les flèches montrent qui dépend de qui.</figcaption>
</figure>

---

## Le problème sans ce pattern

Un `User` a 12 champs optionnels : `new User(a,b,c,...)` illisible.

```typescript
// Avant : un seul bloc qui fait tout\nif (!user) throw new Error();\nconsole.log(req.url);
```

### Symptômes dans ton code

- Fichiers qui grossissent à chaque nouvelle variante.
- Tests difficiles : trop de mocks ou d'effets de bord cachés.
- Tu as peur de toucher une classe car « tout dépend de tout ».

---

## L'idée du pattern Builder

Étapes nommées qui retournent `this`, `build()` valide et retourne l'objet immuable.

| Rôle | Responsabilité |
|------|----------------|
| **Handler/Builder** | Rôle central |
| **Client** | Compose la chaîne ou le builder |

### Analogie du quotidien

Composer un burger : pain, steak, sauce — étape par étape.

---

## Exemple complet en TypeScript

```typescript
class HttpRequest {
  constructor(
    public method: string,
    public url: string,
    public headers: Record<string, string> = {},
    public body?: string,
  ) {}
}

class RequestBuilder {
  private method = 'GET';
  private url = '/';
  private headers: Record<string, string> = {};
  private body?: string;

  setMethod(m: string) { this.method = m; return this; }
  setUrl(u: string) { this.url = u; return this; }
  addHeader(k: string, v: string) { this.headers[k] = v; return this; }
  setBody(b: string) { this.body = b; return this; }

  build() {
    if (!this.url.startsWith('/')) throw new Error('URL invalide');
    return new HttpRequest(this.method, this.url, this.headers, this.body);
  }
}

const req = new RequestBuilder()
  .setMethod('POST')
  .setUrl('/api/users')
  .addHeader('Content-Type', 'application/json')
  .setBody('{"name":"Loic"}')
  .build();
```

### Ce qu'il faut retenir du code

- Le **client** dépend d'abstractions, pas de détails partout.
- Chaque nouvelle variante = **nouvelle classe** (ou module), pas un `if` de plus.
- Nomme tes types pour le **métier** (noms métier explicites, pas `Strategy1`).

---

## Exemple en Python

```python
# Portage Builder : reprendre la structure TypeScript ci-dessus
```

---

## Quand utiliser Builder

- Variantes multiples de builder.
- Évolution fréquente du flux.

---

## Quand ne pas utiliser Builder

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

Prisma query builder, `StringBuilder`, Docker Compose multi-services.

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Non — on teste surtout ta capacité à reconnaître le problème. Le nom Builder aide à communiquer en équipe.

**Ça remplace les frameworks ?** Non — React, Express ou Spring implémentent souvent ces idées pour toi. Comprendre Builder te permet de les utiliser correctement.

**Je dois tout refactoriser ?** Non — applique le pattern quand la douleur est réelle (nouveaux bugs à chaque feature).

---

## Mini test unitaire (idée)

```typescript
// Exemple de test : mocke les collaborateurs, vérifie le comportement public
describe('Builder', () => {
  it('fonctionne avec une variante', () => {
    // Arrange → Act → Assert
  });
});
```

Adapte ce squelette à ton framework (Jest, Vitest, pytest).

---

## Pas à pas : implémenter en 5 étapes

1. **Nomme le problème** — est-ce vraiment Builder ?
2. **Dessine les rôles** sur papier (client, abstraction, implémentations).
3. **Écris un test** qui décrit le comportement attendu.
4. **Implémente une variante** — valide avant d'en ajouter d'autres.
5. **Documente en équipe** — « ici on utilise Builder parce que… ».

---

## Checklist code review

- [ ] Le client ne dépend pas de classes concrètes inutiles
- [ ] Pas de sur-abstraction sur un cas unique
- [ ] Tests sur chaque variante / handler / état
- [ ] Nommage métier clair

---

## Exercice pratique (25–35 min)

Refactorise un bout de code vers Builder et écris 2 tests.

---

## Résumé

Builder : Builder construit pas à pas un objet complexe avec une API fluide.

---

## Navigation dans la série

- Précédent : [Template Method](/blog/articles/design-patterns-template-method.html)
- Suivant : [Iterator](/blog/articles/design-patterns-iterator.html)
