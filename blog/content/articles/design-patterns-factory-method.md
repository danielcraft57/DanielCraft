---
title: "Factory Method : laisser creer sans se prendre la tete"
date: 2026-04-03
excerpt: "Demander un objet a une fabrique au lieu de tout construire a la main."
type: article
tags: [Design Patterns, GoF, Factory Method, Créationnel, TypeScript, Python, junior]
og_image: design-patterns-factory-method-1200x630.jpg
series: design-patterns-serie
series_order: 3
---

# Factory Method : laisser creer sans se prendre la tete

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-factory-method.svg" alt="Schema Factory Method" class="schema-inline" width="640" />
  <figcaption>Demande, fabrique, produit adapte.</figcaption>
</figure>

**Famille :** Créationnel · **Série :** Design Patterns GoF · **Article 3/24** · **Popularité :** #2 sur 23

La Factory Method délègue la création d'objets aux sous-classes sans que le client connaisse la classe concrète.

---

## En une phrase

La Factory Method délègue la création d'objets aux sous-classes sans que le client connaisse la classe concrète.

---

## Le problème sans ce pattern

Chaque export PDF/CSV/JSON ajoute un `if` dans le service :

```typescript
function exportData(type: string, rows: Row[]) {
  if (type === 'pdf') { /* 40 lignes */ }
  else if (type === 'csv') { /* ... */ }
  // chaque format = modifier cette fonction
}
```

### Symptômes dans ton code

- Fichiers qui grossissent à chaque nouvelle variante.
- Tests difficiles : trop de mocks ou d'effets de bord cachés.
- Tu as peur de toucher une classe car « tout dépend de tout ».

---

## L'idée du pattern Factory Method

Une classe abstraite (ou interface) déclare `createExporter()` ; chaque sous-classe retourne le bon produit. Le client appelle `run()` sur le service, pas `new PdfExporter()` partout.

| Rôle | Responsabilité |
|------|----------------|
| **Creator** | Déclare la factory method + logique qui l'utilise |
| **ConcreteCreator** | Implémente createProduct() |
| **Product** | Interface commune des objets créés |

### Analogie du quotidien

Tu commandes le **plat du jour** au restaurant : la salle ne cuisine pas — la cuisine (sous-classe) choisit le plat selon les stocks.

---

## Exemple complet en TypeScript

```typescript
interface Exporter {
  export(rows: Record<string, unknown>[]): string;
}

abstract class ExportService {
  protected abstract createExporter(): Exporter;

  run(rows: Record<string, unknown>[]) {
    return this.createExporter().export(rows);
  }
}

class CsvExportService extends ExportService {
  protected createExporter(): Exporter {
    return {
      export: (rows) =>
        [Object.keys(rows[0] ?? {}).join(','), ...rows.map((r) => Object.values(r).join(','))].join('\n'),
    };
  }
}

class JsonExportService extends ExportService {
  protected createExporter(): Exporter {
    return { export: (rows) => JSON.stringify(rows, null, 2) };
  }
}

function download(userChoice: 'csv' | 'json', rows: Record<string, unknown>[]) {
  const service =
    userChoice === 'csv' ? new CsvExportService() : new JsonExportService();
  return service.run(rows);
}
```

### Ce qu'il faut retenir du code

- Le **client** dépend d'abstractions, pas de détails partout.
- Chaque nouvelle variante = **nouvelle classe** (ou module), pas un `if` de plus.
- Nomme tes types pour le **métier** (noms métier explicites, pas `Strategy1`).

---

## Exemple en Python

```python
from abc import ABC, abstractmethod

class Exporter(ABC):
    @abstractmethod
    def export(self, rows: list[dict]) -> str: ...

class ExportService(ABC):
    @abstractmethod
    def create_exporter(self) -> Exporter: ...

    def run(self, rows: list[dict]) -> str:
        return self.create_exporter().export(rows)

class CsvExportService(ExportService):
    def create_exporter(self) -> Exporter:
        class _Csv(Exporter):
            def export(self, rows: list[dict]) -> str:
                if not rows:
                    return ""
                keys = rows[0].keys()
                lines = [",".join(keys)]
                lines += [",".join(str(r[k]) for k in keys) for r in rows]
                return "\n".join(lines)
        return _Csv()
```

---

## Quand utiliser Factory Method

- Le type de produit dépend du contexte (config, tenant, environnement).
- Tu veux ajouter des variantes sans toucher au code client (Open/Closed).

---

## Quand ne pas utiliser Factory Method

- Une seule implémentation stable.
- Création triviale (`return new Date()`).

---

## Erreurs fréquentes des juniors

- Confondre avec Abstract Factory (famille entière d'objets).
- Hiérarchie inutile pour 2 produits figés.

---

## Patterns proches

- **Abstract Factory** : Crée des familles d'objets liés
- **Simple Factory** : Fonction unique non GoF mais courante

---

## Dans le monde réel

Django : `Model.objects` est une factory. Les frameworks UI créent des composants via des registres de factory.

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Non — on teste surtout ta capacité à reconnaître le problème. Le nom Factory Method aide à communiquer en équipe.

**Ça remplace les frameworks ?** Non — React, Express ou Spring implémentent souvent ces idées pour toi. Comprendre Factory Method te permet de les utiliser correctement.

**Je dois tout refactoriser ?** Non — applique le pattern quand la douleur est réelle (nouveaux bugs à chaque feature).

---

## Mini test unitaire (idée)

```typescript
// Exemple de test : mocke les collaborateurs, vérifie le comportement public
describe('Factory Method', () => {
  it('fonctionne avec une variante', () => {
    // Arrange → Act → Assert
  });
});
```

Adapte ce squelette à ton framework (Jest, Vitest, pytest).

---

## Pas à pas : implémenter en 5 étapes

1. **Nomme le problème** — est-ce vraiment Factory Method ?
2. **Dessine les rôles** sur papier (client, abstraction, implémentations).
3. **Écris un test** qui décrit le comportement attendu.
4. **Implémente une variante** — valide avant d'en ajouter d'autres.
5. **Documente en équipe** — « ici on utilise Factory Method parce que… ».

---

## Checklist code review

- [ ] Le client ne dépend pas de classes concrètes inutiles
- [ ] Pas de sur-abstraction sur un cas unique
- [ ] Tests sur chaque variante / handler / état
- [ ] Nommage métier clair

---

## Exercice pratique (25–35 min)

Ajoute un format `xlsx` via une nouvelle sous-classe `XlsxExportService` sans modifier `download()`.

---

## Résumé

Factory Method = création polymorphe par sous-classes — idéal quand le « quel produit » varie selon le contexte.

---

## Navigation dans la série

- Précédent : [Singleton](/blog/articles/design-patterns-singleton.html)
- Suivant : [Observer](/blog/articles/design-patterns-observer.html)
