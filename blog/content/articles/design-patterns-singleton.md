---
title: "Singleton : pattern créationnel expliqué pour juniors"
date: 2026-04-02
excerpt: "Le Singleton garantit qu'une classe n'a qu'une seule instance et fournit un point d'accès global contrôlé."
type: article
tags: [Design Patterns, GoF, Singleton, Créationnel, TypeScript, Python, junior]
og_image: design-patterns-singleton-1200x630.jpg
series: design-patterns-serie
series_order: 2
---

# Singleton : guide complet pour développeurs juniors

**Famille :** Créationnel · **Série :** Design Patterns GoF · **Article 2/24** · **Popularité :** #1 sur 23

Le Singleton garantit qu'une classe n'a qu'une seule instance et fournit un point d'accès global contrôlé.


<figure>
  <img src="../../assets/images/blog/dp-singleton.svg" alt="Schéma du pattern Singleton" class="schema-inline" width="480" />
  <figcaption>Structure simplifiée du pattern Singleton — les flèches montrent qui dépend de qui.</figcaption>
</figure>

<figure>
  <img src="../../assets/images/blog/illustrations/dp-singleton-banner.webp" alt="Illustration Singleton" class="schema-inline" width="720" />
  <figcaption>Vue d'ensemble visuelle du pattern Singleton (Créationnel).</figcaption>
</figure>


---

## En une phrase

Le Singleton garantit qu'une classe n'a qu'une seule instance et fournit un point d'accès global contrôlé.

---

## Le problème sans ce pattern

Tu charges la configuration `.env` à plusieurs endroits avec `new Config()`. Résultat : flags incohérents, double connexion, tests impossibles à isoler.

```typescript
// Anti-pattern : plusieurs instances
const a = new AppConfig();
const b = new AppConfig();
// a et b peuvent diverger si le constructeur relit le disque
```

### Symptômes dans ton code

- Fichiers qui grossissent à chaque nouvelle variante.
- Tests difficiles : trop de mocks ou d'effets de bord cachés.
- Tu as peur de toucher une classe car « tout dépend de tout ».

---

## L'idée du pattern Singleton

Cache le constructeur et expose `getInstance()` (lazy) ou exporte un **module unique** (pattern module ES).

| Rôle | Responsabilité |
|------|----------------|
| `Singleton` | Instance unique + accès global |
| Client | Appelle `getInstance()` au lieu de `new` |

| Rôle | Responsabilité |
|------|----------------|
| **Singleton** | Stocke l'instance statique, constructeur privé |
| **Client** | Utilise getInstance() |

### Analogie du quotidien

Comme le **maire d'une ville** : une seule personne occupe le poste ; les services administratifs passent par lui, on n'en nomme pas un nouveau par formulaire.

---

## Exemple complet en TypeScript

```typescript
class AppConfig {
  private static instance: AppConfig | null = null;

  private constructor(
    public readonly apiUrl: string,
    public readonly env: 'dev' | 'prod',
  ) {}

  static getInstance(): AppConfig {
    if (!AppConfig.instance) {
      AppConfig.instance = new AppConfig(
        import.meta.env.VITE_API_URL ?? 'http://localhost:3000',
        (import.meta.env.MODE === 'production' ? 'prod' : 'dev') as 'dev' | 'prod',
      );
    }
    return AppConfig.instance;
  }
}

const a = AppConfig.getInstance();
const b = AppConfig.getInstance();
console.log(a === b); // true
```

### Ce qu'il faut retenir du code

- Le **client** dépend d'abstractions, pas de détails partout.
- Chaque nouvelle variante = **nouvelle classe** (ou module), pas un `if` de plus.
- Nomme tes types pour le **métier** (noms métier explicites, pas `Strategy1`).

---

## Exemple en Python

```python
class AppConfig:
    _instance: "AppConfig | None" = None

    def __init__(self, api_url: str, env: str) -> None:
        if AppConfig._instance is not None:
            raise RuntimeError("Utilise AppConfig.get()")
        self.api_url = api_url
        self.env = env

    @classmethod
    def get(cls) -> "AppConfig":
        if cls._instance is None:
            cls._instance = cls("https://api.example.com", "prod")
        return cls._instance
```

---

## Quand utiliser Singleton

- Ressource réellement unique (pool de connexions maîtrisé, identifiant machine).
- Coût d'initialisation élevé partagé par toute l'application.

---

## Quand ne pas utiliser Singleton

- Tests unitaires : l'état global pollue les tests parallèles.
- Plusieurs instances légitimes (un panier par utilisateur).
- En TypeScript moderne : préfère un module `config.ts` exporté ou l'injection de dépendances.

---

## Erreurs fréquentes des juniors

- Singleton « par défaut » sur toutes les classes.
- God Object : tout l'état métier dans l'instance unique.
- Oublier le thread-safety en Java/C# (double-checked locking).

---

## Patterns proches

- **Factory Method** : Délègue la création sans imposer une instance unique
- **Injection de dépendances** : Passe Config en paramètre — plus testable

---

## Dans le monde réel

Node.js : certains drivers utilisent un pool singleton. En front, évite le singleton DOM ; préfère un store (Zustand, Pinia) avec un seul provider.

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Non — on teste surtout ta capacité à reconnaître le problème. Le nom Singleton aide à communiquer en équipe.

**Ça remplace les frameworks ?** Non — React, Express ou Spring implémentent souvent ces idées pour toi. Comprendre Singleton te permet de les utiliser correctement.

**Je dois tout refactoriser ?** Non — applique le pattern quand la douleur est réelle (nouveaux bugs à chaque feature).

---

## Mini test unitaire (idée)

```typescript
// Exemple de test : mocke les collaborateurs, vérifie le comportement public
describe('Singleton', () => {
  it('fonctionne avec une variante', () => {
    // Arrange → Act → Assert
  });
});
```

Adapte ce squelette à ton framework (Jest, Vitest, pytest).

---

## Pas à pas : implémenter en 5 étapes

1. **Nomme le problème** — est-ce vraiment Singleton ?
2. **Dessine les rôles** sur papier (client, abstraction, implémentations).
3. **Écris un test** qui décrit le comportement attendu.
4. **Implémente une variante** — valide avant d'en ajouter d'autres.
5. **Documente en équipe** — « ici on utilise Singleton parce que… ».

---

## Checklist code review

- [ ] Le client ne dépend pas de classes concrètes inutiles
- [ ] Pas de sur-abstraction sur un cas unique
- [ ] Tests sur chaque variante / handler / état
- [ ] Nommage métier clair

---

## Exercice pratique (25–35 min)

Remplace ton `Logger.getInstance()` par un logger injecté dans chaque service. Écris 2 tests : avec mock, sans état partagé.

---

## Résumé

Une instance, un accès — utile pour de vraies ressources uniques ; dangereux comme variable globale déguisée.

---

## Navigation dans la série

- Précédent : [Introduction](/blog/articles/design-patterns-introduction-gang-of-four.html)
- Suivant : [Factory Method](/blog/articles/design-patterns-factory-method.html)
