---
title: "Command : pattern comportemental expliqué pour juniors"
date: 2026-04-09
excerpt: "Command encapsule une requête en objet : exécution, annulation, file d'attente, historique."
type: article
tags: [Design Patterns, GoF, Command, Comportemental, TypeScript, Python, junior]
og_image: design-patterns-command-1200x630.jpg
series: design-patterns-serie
series_order: 9
---

# Command : guide complet pour développeurs juniors

**Famille :** Comportemental · **Série :** Design Patterns GoF · **Article 9/24** · **Popularité :** #8 sur 23

Command encapsule une requête en objet : exécution, annulation, file d'attente, historique.


<figure>
  <img src="../../assets/images/blog/dp-command.svg" alt="Schéma du pattern Command" class="schema-inline" width="480" />
  <figcaption>Structure simplifiée du pattern Command — les flèches montrent qui dépend de qui.</figcaption>
</figure>

<figure>
  <img src="../../assets/images/blog/illustrations/dp-command-banner.webp" alt="Illustration Command" class="schema-inline" width="720" />
  <figcaption>Vue d'ensemble visuelle du pattern Command (Comportemental).</figcaption>
</figure>


---

## En une phrase

Command encapsule une requête en objet : exécution, annulation, file d'attente, historique.

---

## Le problème sans ce pattern

Éditeur de texte sans Command :

```typescript
function onKey(type: string) {
  if (type === 'bold') document.execCommand('bold');
  // impossible de stocker l'historique proprement pour undo
}
```

Undo/redo devient un cauchemar de flags.

### Symptômes dans ton code

- Fichiers qui grossissent à chaque nouvelle variante.
- Tests difficiles : trop de mocks ou d'effets de bord cachés.
- Tu as peur de toucher une classe car « tout dépend de tout ».

---

## L'idée du pattern Command

Chaque action est un objet `execute()` / `undo()`. L'**Invoker** empile l'historique sans connaître les détails.

| Rôle | Responsabilité |
|------|----------------|
| **Command** | execute / undo |
| **Invoker** | Historique |
| **Receiver** | Document modifié |
| **Client** | UI |

### Analogie du quotidien

Commande au **restaurant** : le serveur note, la cuisine exécute plus tard — la commande est l'objet.

---

## Exemple complet en TypeScript

```typescript
interface Command {
  execute(): void;
  undo(): void;
}

class AddTextCommand implements Command {
  constructor(private doc: string[], private text: string) {}
  execute() { this.doc.push(this.text); }
  undo() { this.doc.pop(); }
}

class EditorInvoker {
  private history: Command[] = [];
  private pointer = -1;

  run(cmd: Command) {
    cmd.execute();
    this.history = this.history.slice(0, this.pointer + 1);
    this.history.push(cmd);
    this.pointer++;
  }

  undo() {
    if (this.pointer < 0) return;
    this.history[this.pointer--].undo();
  }
}

const doc: string[] = [];
const invoker = new EditorInvoker();
invoker.run(new AddTextCommand(doc, 'Hello'));
invoker.undo();
```

### Ce qu'il faut retenir du code

- Le **client** dépend d'abstractions, pas de détails partout.
- Chaque nouvelle variante = **nouvelle classe** (ou module), pas un `if` de plus.
- Nomme tes types pour le **métier** (noms métier explicites, pas `Strategy1`).

---

## Exemple en Python

```python
class Command(ABC):
    @abstractmethod
    def execute(self) -> None: ...
    @abstractmethod
    def undo(self) -> None: ...

class AddTextCommand(Command):
    def __init__(self, doc: list[str], text: str) -> None:
        self._doc = doc
        self._text = text
    def execute(self) -> None:
        self._doc.append(self._text)
    def undo(self) -> None:
        self._doc.pop()
```

---

## Quand utiliser Command

- Undo/redo.
- File d'attente de tâches (jobs).
- Macros rejouant plusieurs commandes.
- CQRS côté écriture.

---

## Quand ne pas utiliser Command

- Action unique sans historique.
- Overhead inutile pour un bouton.

---

## Erreurs fréquentes des juniors

- undo() qui ne restaure pas l'état exact.
- Commandes non idempotentes mal documentées.

---

## Patterns proches

- **Strategy** : Choisit un algorithme, pas une action réversible
- **Memento** : Snapshot d'état sans objet commande

---

## Dans le monde réel

Photoshop history. Redis queues. Git commit comme snapshot (proche, pas identique).

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Non — on teste surtout ta capacité à reconnaître le problème. Le nom Command aide à communiquer en équipe.

**Ça remplace les frameworks ?** Non — React, Express ou Spring implémentent souvent ces idées pour toi. Comprendre Command te permet de les utiliser correctement.

**Je dois tout refactoriser ?** Non — applique le pattern quand la douleur est réelle (nouveaux bugs à chaque feature).

---

## Mini test unitaire (idée)

```typescript
// Exemple de test : mocke les collaborateurs, vérifie le comportement public
describe('Command', () => {
  it('fonctionne avec une variante', () => {
    // Arrange → Act → Assert
  });
});
```

Adapte ce squelette à ton framework (Jest, Vitest, pytest).

---

## Pas à pas : implémenter en 5 étapes

1. **Nomme le problème** — est-ce vraiment Command ?
2. **Dessine les rôles** sur papier (client, abstraction, implémentations).
3. **Écris un test** qui décrit le comportement attendu.
4. **Implémente une variante** — valide avant d'en ajouter d'autres.
5. **Documente en équipe** — « ici on utilise Command parce que… ».

---

## Checklist code review

- [ ] Le client ne dépend pas de classes concrètes inutiles
- [ ] Pas de sur-abstraction sur un cas unique
- [ ] Tests sur chaque variante / handler / état
- [ ] Nommage métier clair

---

## Exercice pratique (25–35 min)

Implémente `MoveItemCommand` pour un panier (ajout/retrait avec undo).

---

## Résumé

Command = action comme objet, parfaite pour undo et files d'attente.

---

## Navigation dans la série

- Précédent : [Facade](/blog/articles/design-patterns-facade.html)
- Suivant : [Template Method](/blog/articles/design-patterns-template-method.html)
