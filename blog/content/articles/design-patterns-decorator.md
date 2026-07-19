---
title: "Decorator : pattern structurel expliqué pour juniors"
date: 2026-04-06
excerpt: "Decorator ajoute des responsabilités à un objet par composition, sans modifier sa classe."
type: article
tags: [Design Patterns, GoF, Decorator, Structurel, TypeScript, Python, junior]
og_image: design-patterns-decorator-1200x630.jpg
series: design-patterns-serie
series_order: 6
---

# Decorator : guide complet pour développeurs juniors

**Famille :** Structurel · **Série :** Design Patterns GoF · **Article 6/24** · **Popularité :** #5 sur 23

Decorator ajoute des responsabilités à un objet par composition, sans modifier sa classe.

---

## En une phrase

Decorator ajoute des responsabilités à un objet par composition, sans modifier sa classe.

<figure class="schema-figure">
  <img src="../../assets/images/blog/dp-decorator.svg" alt="Schéma du pattern Decorator" class="schema-inline" width="480" />
  <figcaption>Structure simplifiée du pattern Decorator — les flèches montrent qui dépend de qui.</figcaption>
</figure>

---

## Le problème sans ce pattern

Tu veux buffer + compression + chiffrement sur un flux : `BufferedCompressedEncryptedReader` multiplie les sous-classes.

### Symptômes dans ton code

- Fichiers qui grossissent à chaque nouvelle variante.
- Tests difficiles : trop de mocks ou d'effets de bord cachés.
- Tu as peur de toucher une classe car « tout dépend de tout ».

---

## L'idée du pattern Decorator

Chaque décorateur implémente la même interface et délègue au composant interne après sa couche.

| Rôle | Responsabilité |
|------|----------------|
| **Component** | Interface commune |
| **ConcreteComponent** | Objet de base |
| **Decorator** | Wrap + délègue |

### Analogie du quotidien

Gâteau : génoise → crème → glaçage, couche par couche.

---

## Exemple complet en TypeScript

```typescript
interface DataSource {
  write(data: string): void;
  read(): string;
}

class FileSource implements DataSource {
  private content = '';
  write(data: string) { this.content += data; }
  read() { return this.content; }
}

abstract class DataSourceDecorator implements DataSource {
  constructor(protected wrappee: DataSource) {}
  write(data: string) { this.wrappee.write(data); }
  read() { return this.wrappee.read(); }
}

class EncryptionDecorator extends DataSourceDecorator {
  write(data: string) { super.write(btoa(data)); }
  read() { return atob(super.read()); }
}

let source: DataSource = new FileSource();
source = new EncryptionDecorator(source);
source.write('secret');
```

### Ce qu'il faut retenir du code

- Le **client** dépend d'abstractions, pas de détails partout.
- Chaque nouvelle variante = **nouvelle classe** (ou module), pas un `if` de plus.
- Nomme tes types pour le **métier** (noms métier explicites, pas `Strategy1`).

---

## Exemple en Python

```python
class DataSource(ABC):
    @abstractmethod
    def read(self) -> str: ...
    @abstractmethod
    def write(self, data: str) -> None: ...

class EncryptionDecorator(DataSource):
    def __init__(self, wrappee: DataSource) -> None:
        self._w = wrappee
    def write(self, data: str) -> None:
        import base64
        self._w.write(base64.b64encode(data.encode()).decode())
    def read(self) -> str:
        import base64
        return base64.b64decode(self._w.read().encode()).decode()
```

---

## Quand utiliser Decorator

- Empiler des options (streams, middleware HTTP).
- HOC React qui enrichit un composant.

---

## Quand ne pas utiliser Decorator

- Peu de combinaisons possibles.
- Ordre des couches critique et non documenté.

---

## Erreurs fréquentes des juniors

- Trop de couches = debug difficile.
- Décorateur non substituable (viole Liskov).

---

## Patterns proches

- **Adapter** : Change l'interface
- **Proxy** : Contrôle l'accès

---

## Comparaisons utiles

| Pattern | Rôle |
|---------|------|
| Decorator | Ajoute une responsabilité |
| Adapter | Change l'interface |
| Proxy | Contrôle l'accès |

---

## Dans le monde réel

Express middleware : `app.use(logger)`, `app.use(auth)` — chaîne de décorateurs autour du handler.

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Non — on teste surtout ta capacité à reconnaître le problème. Le nom Decorator aide à communiquer en équipe.

**Ça remplace les frameworks ?** Non — React, Express ou Spring implémentent souvent ces idées pour toi. Comprendre Decorator te permet de les utiliser correctement.

**Je dois tout refactoriser ?** Non — applique le pattern quand la douleur est réelle (nouveaux bugs à chaque feature).

---

## Mini test unitaire (idée)

```typescript
// Exemple de test : mocke les collaborateurs, vérifie le comportement public
describe('Decorator', () => {
  it('fonctionne avec une variante', () => {
    // Arrange → Act → Assert
  });
});
```

Adapte ce squelette à ton framework (Jest, Vitest, pytest).

---

## Pas à pas : implémenter en 5 étapes

1. **Nomme le problème** — est-ce vraiment Decorator ?
2. **Dessine les rôles** sur papier (client, abstraction, implémentations).
3. **Écris un test** qui décrit le comportement attendu.
4. **Implémente une variante** — valide avant d'en ajouter d'autres.
5. **Documente en équipe** — « ici on utilise Decorator parce que… ».

---

## Checklist code review

- [ ] Le client ne dépend pas de classes concrètes inutiles
- [ ] Pas de sur-abstraction sur un cas unique
- [ ] Tests sur chaque variante / handler / état
- [ ] Nommage métier clair

---

## Exercice pratique (25–35 min)

`Coffee` + `MilkDecorator` + `SugarDecorator` qui ajoutent au prix.

---

## Résumé

Decorator = composition dynamique de comportements.

---

## Navigation dans la série

- Précédent : [Strategy](/blog/articles/design-patterns-strategy.html)
- Suivant : [Adapter](/blog/articles/design-patterns-adapter.html)
