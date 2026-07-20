---
title: "Proxy : un intermediaire qui controle l'acces"
date: 2026-04-14
excerpt: "Un objet devant un autre : cache, securite, ou chargement lazy."
type: article
tags: [Design Patterns, GoF, Proxy, Structurel, TypeScript, Python, junior]
og_image: design-patterns-proxy-1200x630.jpg
series: design-patterns-serie
series_order: 14
---

# Proxy : un intermediaire qui controle l'acces

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-proxy.svg" alt="Schema Proxy" class="schema-inline" width="640" />
  <figcaption>Client, proxy, vrai objet.</figcaption>
</figure>

**Famille :** Structurel · **Série :** Design Patterns GoF · **Article 14/24** · **Popularité :** #13 sur 23

Proxy contrôle l'accès à un objet coûteux ou distant (lazy, cache, sécurité).

---

## En une phrase

Proxy contrôle l'accès à un objet coûteux ou distant (lazy, cache, sécurité).

---

## Le problème sans ce pattern

Charger une image 4K à chaque rendu même hors écran.

```typescript
// Avant : un seul bloc qui fait tout\nif (!user) throw new Error();\nconsole.log(req.url);
```

### Symptômes dans ton code

- Fichiers qui grossissent à chaque nouvelle variante.
- Tests difficiles : trop de mocks ou d'effets de bord cachés.
- Tu as peur de toucher une classe car « tout dépend de tout ».

---

## L'idée du pattern Proxy

Même interface que le sujet ; chargement réel au premier `render()`.

| Rôle | Responsabilité |
|------|----------------|
| **Handler/Builder** | Rôle central |
| **Client** | Compose la chaîne ou le builder |

### Analogie du quotidien

Secrétaire qui filtre les appels avant le directeur.

---

## Exemple complet en TypeScript

```typescript
interface Image {
  render(): string;
}

class HeavyImage implements Image {
  constructor(private url: string) {
    console.log('Chargement lourd', url);
  }
  render() { return `<img src="${this.url}"/>`; }
}

class ImageProxy implements Image {
  private real: HeavyImage | null = null;
  constructor(private url: string) {}
  render() {
    if (!this.real) this.real = new HeavyImage(this.url);
    return this.real.render();
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
# Portage Proxy : reprendre la structure TypeScript ci-dessus
```

---

## Quand utiliser Proxy

- Variantes multiples de proxy.
- Évolution fréquente du flux.

---

## Quand ne pas utiliser Proxy

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

Vue `reactive`, lazy loading ORM, API gateway, cache HTTP.

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Non — on teste surtout ta capacité à reconnaître le problème. Le nom Proxy aide à communiquer en équipe.

**Ça remplace les frameworks ?** Non — React, Express ou Spring implémentent souvent ces idées pour toi. Comprendre Proxy te permet de les utiliser correctement.

**Je dois tout refactoriser ?** Non — applique le pattern quand la douleur est réelle (nouveaux bugs à chaque feature).

---

## Mini test unitaire (idée)

```typescript
// Exemple de test : mocke les collaborateurs, vérifie le comportement public
describe('Proxy', () => {
  it('fonctionne avec une variante', () => {
    // Arrange → Act → Assert
  });
});
```

Adapte ce squelette à ton framework (Jest, Vitest, pytest).

---

## Pas à pas : implémenter en 5 étapes

1. **Nomme le problème** — est-ce vraiment Proxy ?
2. **Dessine les rôles** sur papier (client, abstraction, implémentations).
3. **Écris un test** qui décrit le comportement attendu.
4. **Implémente une variante** — valide avant d'en ajouter d'autres.
5. **Documente en équipe** — « ici on utilise Proxy parce que… ».

---

## Checklist code review

- [ ] Le client ne dépend pas de classes concrètes inutiles
- [ ] Pas de sur-abstraction sur un cas unique
- [ ] Tests sur chaque variante / handler / état
- [ ] Nommage métier clair

---

## Exercice pratique (25–35 min)

Refactorise un bout de code vers Proxy et écris 2 tests.

---

## Résumé

Proxy : Proxy contrôle l'accès à un objet coûteux ou distant (lazy, cache, sécurité).

---

## Navigation dans la série

- Précédent : [State](/blog/articles/design-patterns-state.html)
- Suivant : [Abstract Factory](/blog/articles/design-patterns-abstract-factory.html)
