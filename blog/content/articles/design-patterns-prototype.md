---
title: "Prototype : copier un modele plutot que tout recreer"
date: 2026-04-18
excerpt: "Cloner un objet existant puis ajuster — plus simple parfois que construire a neuf."
type: article
tags: [Design Patterns, GoF, Prototype, Créationnel, TypeScript, Python, junior]
og_image: design-patterns-prototype-1200x630.jpg
series: design-patterns-serie
series_order: 18
---

# Prototype : copier un modele plutot que tout recreer

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-prototype.svg" alt="Schema Prototype" class="schema-inline" width="640" />
  <figcaption>Modele, clone, ajuste, nouvelle copie.</figcaption>
</figure>

**Famille :** Créationnel · **Série :** Design Patterns GoF · **Article 18/24** · **Popularité :** #17 sur 23

Prototype crée de nouveaux objets en **clonant** un exemplaire déjà configuré, plutôt qu'en reconstruisant tout depuis zéro (constructeurs lourds, chargements réseau, templates).

---

## En une phrase

Prototype clone un exemplaire au lieu de reconstruire depuis zéro.

---

## Le problème sans ce pattern

Tu as un modèle coûteux : carte de jeu 2 Mo, document Word prérempli, config serveur avec 40 champs. Pour chaque utilisateur / niveau / variante, tu recharges depuis la DB ou tu recopies 40 lignes de constructeur. C'est lent, verbeux, et fragile : un oubli de champ = bug silencieux.

Le pattern répond aussi à un autre besoin : **créer sans connaître la classe exacte**. Si le client reçoit déjà un objet « modèle » (chargé depuis un fichier, choisi dans un menu), `clone()` suffit — pas besoin d'un `switch` sur le type pour rappeler le bon constructeur.

### Symptômes dans ton code

- Constructeurs monstres avec dix paramètres optionnels.
- `Object.assign` / `JSON.parse(JSON.stringify)` partout sans règle claire.
- Copies qui partagent encore des références (mutation surprise).
- Impossible de créer une variante sans connaître toutes les classes concrètes.

---

## L'idée du pattern Prototype

Chaque objet « modèle » sait se **cloner**. Le client demande une copie, puis ajuste ce qui change (difficulté, couleur, titre). Optionnel : un **registre** de prototypes nommés (`'niveau-facile'`, `'facture-fr'`). Le registre évite que le client fasse `new ConcreteClass(...)` : il demande `registry.get('niveau-facile').clone()` et reste découplé des classes concrètes.

| Rôle | Responsabilité |
|------|----------------|
| **Prototype** | Interface `clone()` |
| **ConcretePrototype** | Copie son état (souvent deep copy) |
| **Client** | Clone puis personnalise |
| **Registry** (optionnel) | Catalogue de modèles prêts |

### Analogie du quotidien

Une **photocopieuse** (ou un « dupliquer la slide » dans un diaporama). Tu ne redessines pas la présentation : tu photocopies le modèle, puis tu changes le titre et la date. Le coûteux (mise en page) est déjà là.

---

## Exemple en TypeScript

```typescript
interface Cloneable<T> {
  clone(): T;
}

class GameLevel implements Cloneable<GameLevel> {
  constructor(
    public map: string[][],
    public difficulty: number,
  ) {}

  clone() {
    // deep copy de la carte pour éviter de partager les lignes
    return new GameLevel(
      this.map.map((row) => [...row]),
      this.difficulty,
    );
  }
}

const base = new GameLevel([['G', 'W'], ['E', 'G']], 1);
const hard = base.clone();
hard.difficulty = 5;
hard.map[0][0] = 'B'; // n'altère pas base
```

### Version Python minimale

```python
import copy

class GameLevel:
    def __init__(self, map_grid: list[list[str]], difficulty: int):
        self.map = map_grid
        self.difficulty = difficulty

    def clone(self) -> "GameLevel":
        return GameLevel(copy.deepcopy(self.map), self.difficulty)

base = GameLevel([["G", "W"], ["E", "G"]], 1)
hard = base.clone()
hard.difficulty = 5
```

---

## Quand utiliser Prototype

- Création **coûteuse** (I/O, parsing, calcul) et variantes nombreuses.
- Tu ne veux pas exposer les classes concrètes au client (registre).
- Objets avec beaucoup d'état déjà correct « par défaut ».

## Quand ne pas utiliser Prototype

- Objets triviaux : un `new User(name)` suffit.
- État mutable partagé sans deep copy → bugs subtils.
- Confusion avec **Flyweight** (partager l'immuable) : Prototype *duplique*, Flyweight *partage*.

---

## Erreurs fréquentes des juniors

- Clone **superficiel** : tableaux / objets imbriqués encore partagés.
- Cloner des ressources non clonables (sockets, connexions DB) sans stratégie.
- Utiliser `JSON` pour cloner : perd les méthodes, dates, `undefined`, Map/Set.
- Pattern « parce que le livre le dit » sur un DTO de 3 champs.

---

## Patterns proches

- **Factory Method / Abstract Factory** : créent sans forcément partir d'un exemplaire.
- **Builder** : construit étape par étape ; Prototype copie un état déjà valide.
- **Flyweight** : partage au lieu de cloner — souvent complémentaire (partager textures, cloner positions).

---

## Dans le monde réel

`Object.create` / prototypes JS (héritage), `structuredClone`, `clone()` Java, duplication de documents (Google Docs, Figma « duplicate »), prefabs Unity / Godot. Dès que tu « dupliques puis tweakes », tu es dans l'esprit Prototype.

Autre scénario métier : un **template d'e-mail** ou de contrat chargé une fois (parsing HTML, variables). Pour chaque envoi, tu clones le template, tu remplis nom / montant, tu envoies. Sans clone, tu reparserais le même fichier à chaque destinataire — inutile et plus lent.

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Moins que Singleton/Factory — utile si on parle perf ou copies d'état.

**Ça remplace les frameworks ?** Non — les moteurs de jeu et les éditeurs l'implémentent déjà.

**Je dois tout refactoriser ?** Non — commence par un modèle cher à créer, ajoute `clone()` propre (deep où il faut).

---

## Checklist code review

- [ ] Deep vs shallow copy décidé explicitement
- [ ] Le clone ne mute pas l'original (test unitaire)
- [ ] Pas de ressources externes « semi-clonées » par accident
- [ ] Nommage métier (`GameLevel.clone`, pas `copyStuff`)

---

## Exercice pratique (25–35 min)

Modélise une « fiche produit » (nom, prix, tags[]). Implémente `clone()` avec deep copy des tags. Vérifie qu'ajouter un tag sur la copie ne change pas l'original.

---

## Résumé

- Prototype = photocopieuse : copie un modèle, ajuste le détail.
- Utile quand créer from scratch est cher ou verbeux.
- Attention au **deep copy** : c'est là que se cachent les bugs.

---

## Navigation dans la série

- Précédent : [Bridge](/blog/articles/design-patterns-bridge.html)
- Suivant : [Flyweight](/blog/articles/design-patterns-flyweight.html)
