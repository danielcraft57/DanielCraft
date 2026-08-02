---
title: "Memento : sauvegarder pour pouvoir revenir en arriere"
date: 2026-04-22
excerpt: "Prendre une photo de l'etat, la ranger, la restaurer plus tard (Ctrl+Z)."
type: article
tags: [Design Patterns, GoF, Memento, Comportemental, TypeScript, Python, junior]
og_image: design-patterns-memento-1200x630.jpg
series: design-patterns-serie
series_order: 22
---

# Memento : sauvegarder pour pouvoir revenir en arriere

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-memento.svg" alt="Schema Memento" class="schema-inline" width="640" />
  <figcaption>Etat, save, changer, restore.</figcaption>
</figure>

**Famille :** Comportemental · **Série :** Design Patterns GoF · **Article 22/24** · **Popularité :** #21 sur 23

Memento capture un **instantané** de l'état interne d'un objet pour le restaurer plus tard — typiquement un **undo** — sans exposer cet état au reste du programme.

---

## En une phrase

Memento capture l'état interne pour restauration ultérieure (undo).

---

## Le problème sans ce pattern

Tu veux Ctrl+Z sur un éditeur. Première idée : exposer `content`, `cursor`, `selection` au client pour qu'il les stocke. Résultat : encapsulation cassée, n'importe qui peut écrire n'importe quoi, et chaque nouveau champ d'état force à mettre à jour tous les « sauveurs » externes.

Sans Memento, tu vois aussi des historiques « maison » où l'UI stocke des copies partielles (`lastText` seulement) : dès que tu ajoutes une couleur ou un zoom, l'undo devient incohérent. Le pattern force à décider *une fois* ce qui appartient à l'instantané.

### Symptômes dans ton code

- Getters/setters partout juste pour l'historique.
- Undo qui oublie un champ (curseur restauré, texte non).
- Historique qui mélange logique UI et détails métier.
- Impossible de limiter qui lit vraiment l'état sauvegardé.

---

## L'idée du pattern Memento

Trois rôles classiques :

| Rôle | Responsabilité |
|------|----------------|
| **Originator** | Objet métier ; crée et restaure un memento |
| **Memento** | Instantané opaque (ou à accès restreint) |
| **Caretaker** | Empile / dépile les mementos ; ne lit pas l'intérieur |

L'Originator seul sait ce qu'il y a dans le snapshot. Le Caretaker (souvent l'UI ou un service d'historique) ne fait que ranger les boîtes. Cette séparation est le cœur du pattern : tu peux changer le format interne du snapshot (ajouter un champ `cursor`) sans que le Caretaker ait à « comprendre » quoi que ce soit — il empile et dépile des objets opaques.

### Analogie du quotidien

Une **sauvegarde de partie** ou **Ctrl+Z**. Tu ne demandes pas au joueur de recopier manuellement chaque variable du jeu : tu cliques « save », le système fige l'état, et « load » / undo le remet. Le joueur (Caretaker) manipule des sauvegardes, pas les entrailles du moteur.

---

## Exemple en TypeScript

```typescript
class EditorSnapshot {
  constructor(readonly content: string) {}
}

class Editor {
  constructor(public content = '') {}

  save(): EditorSnapshot {
    return new EditorSnapshot(this.content);
  }

  restore(m: EditorSnapshot) {
    this.content = m.content;
  }
}

class History {
  private stack: EditorSnapshot[] = [];

  push(m: EditorSnapshot) { this.stack.push(m); }

  pop(): EditorSnapshot | undefined {
    return this.stack.pop();
  }
}

const editor = new Editor('bonjour');
const history = new History();
history.push(editor.save());
editor.content = 'bonjour monde';
const prev = history.pop();
if (prev) editor.restore(prev); // → « bonjour »
```

Ici `History` est le Caretaker : il stocke sans interpréter.

### Version Python minimale

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Snapshot:
    content: str

class Editor:
    def __init__(self, content: str = "") -> None:
        self.content = content

    def save(self) -> Snapshot:
        return Snapshot(self.content)

    def restore(self, m: Snapshot) -> None:
        self.content = m.content
```

---

## Quand utiliser Memento

- Undo / redo, checkpoints, brouillons.
- Tu dois figer un état **sans** ouvrir l'objet au monde.
- Transactions locales (essayer une action, rollback si échec).

## Quand ne pas utiliser Memento

- État énorme sans compaction (mémoire qui explose).
- Besoin d'audit détaillé des *commandes* → regarde plutôt **Command** (undo par inversion d'action).
- Simple formulaire où un `previousValue` local suffit.

---

## Erreurs fréquentes des juniors

- Laisser le Caretaker lire et modifier le contenu du memento.
- Snapshots trop gros (toute l'app) au lieu de l'état utile.
- Oublier deep copy : le memento partage encore des références mutables.
- Empiler à l'infini sans limite (max 50 undos).

---

## Patterns proches

- **Command** : undo via « commande inverse » plutôt que snapshot.
- **State** : change le comportement selon l'état ; Memento *photographie* l'état.
- **Prototype** : clone pour créer ; Memento clone pour *restaurer*.

---

## Dans le monde réel

Historique d'éditeurs (VS Code, Word), Redux DevTools (time-travel), sauvegardes de jeux, drafts d'emails. Beaucoup de libs appellent ça « snapshot » ou « checkpoint » — c'est l'esprit Memento.

En pratique, tu peux combiner **Memento** (état) et **Command** (intention) : la commande enregistre *ce qui a été fait*, le memento permet un retour rapide si l'inversion est trop complexe. Pour un canvas graphique, un snapshot compressé (diff) évite de recopier toute la scène à chaque coup de pinceau.

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Parfois dans un exo « implémente undo ».

**Ça remplace les frameworks ?** Non — les stores (Redux, Zustand) offrent déjà des mécanismes proches.

**Je dois tout refactoriser ?** Non — commence par un Originator + pile limitée.

---

## Checklist code review

- [ ] Le Caretaker n'inspecte pas l'intérieur du memento
- [ ] Copies suffisamment profondes
- [ ] Limite de taille de l'historique
- [ ] Tests : save → mutate → restore revient à l'original

---

## Exercice pratique (25–35 min)

Éditeur de texte minimal (une string). Boutons conceptuels save / undo. Ajoute ensuite le curseur (`number`) dans le snapshot et vérifie que undo le restaure aussi.

---

## Résumé

- Memento = photo de l'état + pile gérée par un Caretaker discret.
- Protège l'encapsulation tout en offrant Ctrl+Z.
- Surveille mémoire et profondeur de copie.

---

## Navigation dans la série

- Précédent : [Mediator](/blog/articles/design-patterns-mediator.html)
- Suivant : [Visitor](/blog/articles/design-patterns-visitor.html)
