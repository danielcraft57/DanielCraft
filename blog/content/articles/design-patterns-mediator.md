---
title: "Mediator : un chef d'orchestre entre les objets"
date: 2026-04-21
excerpt: "Les objets ne se parlent plus tous entre eux : ils passent par un centre."
type: article
tags: [Design Patterns, GoF, Mediator, Comportemental, TypeScript, Python, junior]
og_image: design-patterns-mediator-1200x630.jpg
series: design-patterns-serie
series_order: 21
---

# Mediator : un chef d'orchestre entre les objets

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-mediator.svg" alt="Schema Mediator" class="schema-inline" width="640" />
  <figcaption>Spaghetti versus centre de coordination.</figcaption>
</figure>

**Famille :** Comportemental · **Série :** Design Patterns GoF · **Article 21/24** · **Popularité :** #20 sur 23

Mediator centralise la communication entre plusieurs composants. Au lieu d'un graphe N×N de dépendances, chaque pièce parle au **médiateur**, qui orchestre les réactions.

---

## En une phrase

Mediator centralise les échanges entre composants (évite N×N).

---

## Le problème sans ce pattern

Un formulaire : pays → met à jour les provinces ; code promo → recalcule le total ; case « entreprise » → affiche SIRET. Sans médiateur, chaque champ appelle directement les autres (`setState` en chaîne). Ajoute un champ → tu rewires dix fichiers. Tests : mocker tout le monde.

Visuellement, ton graphe de dépendances ressemble à un plat de spaghetti : A connaît B et C, B connaît A et D, etc. Mediator transforme ça en étoile : A, B, C, D pointent vers un centre. Le centre peut grossir — d'où la discipline de le garder limité à la *coordination*, pas à tout le métier.

### Symptômes dans ton code

- Composants qui s'importent mutuellement (cycles).
- Effets de bord en cascade difficiles à suivre.
- Impossible de réutiliser un widget hors de ce formulaire.
- « Tout dépend de tout » : peur de toucher un input.

---

## L'idée du pattern Mediator

Les collègues (**Colleague**) ne se connaissent pas. Ils notifient le **Mediator**, qui décide qui mettre à jour.

| Rôle | Responsabilité |
|------|----------------|
| **Mediator** | Règles de coordination |
| **ConcreteMediator** | Formulaire, chat room, wizard… |
| **Colleague** | Widget / service ; parle au médiateur |

### Analogie du quotidien

Une **tour de contrôle aérienne**. Les avions ne se téléphonent pas deux à deux pour éviter les collisions : ils parlent à la tour, qui ordonne. Moins de spaghetti radio, plus de règles centralisées. Même idée dans une équipe avec un chef de projet qui synchronise les dépendances.

---

## Exemple en TypeScript

```typescript
class OrderFormMediator {
  private total = 0;
  private discount = 0;

  updateTotal(subtotal: number) {
    this.total = subtotal - this.discount;
    console.log('UI total', this.total);
  }

  applyDiscount(percent: number, subtotal: number) {
    this.discount = (subtotal * percent) / 100;
    this.updateTotal(subtotal);
  }
}

// Les « champs » n'appellent que le médiateur :
const form = new OrderFormMediator();
form.updateTotal(100);
form.applyDiscount(10, 100); // total → 90
```

Dans une UI réelle, `CountrySelect` et `ProvinceSelect` tiendraient une référence au même médiateur et appelleraient `onCountryChanged` / `onProvinceChanged`.

### Version Python minimale

```python
class ChatRoom:
    def __init__(self) -> None:
        self._users: dict[str, "User"] = {}

    def register(self, user: "User") -> None:
        self._users[user.name] = user
        user.room = self

    def broadcast(self, sender: str, message: str) -> None:
        for name, user in self._users.items():
            if name != sender:
                user.receive(sender, message)

class User:
    def __init__(self, name: str) -> None:
        self.name = name
        self.room: ChatRoom | None = None

    def send(self, message: str) -> None:
        assert self.room
        self.room.broadcast(self.name, message)

    def receive(self, sender: str, message: str) -> None:
        print(f"{self.name} ← {sender}: {message}")
```

Les utilisateurs ne se référencent pas entre eux : la room (Mediator) diffuse.

---

## Quand utiliser Mediator

- UI riches (formulaires, dialogs, dashboards) avec règles croisées.
- Chat / bus interne où les participants ne doivent pas se connaître.
- Réduire le couplage N×N entre modules d'un même sous-système.

## Quand ne pas utiliser Mediator

- Deux objets qui collaborent simplement — un appel direct suffit.
- Médiateur qui devient un **God Object** (toute la logique métier dedans).
- Besoin d'événements globaux découplés → parfois **Observer** / Event Bus plus adapté (attention à la différence : bus générique vs règles métier centralisées).

---

## Erreurs fréquentes des juniors

- Tout mettre dans le médiateur jusqu'à en faire un monolithe.
- Laisser quand même des appels directs « pour aller plus vite ».
- Confondre Mediator et **Facade** (Facade simplifie une API ; Mediator *orchestre* des pairs).
- Médiateur qui connaît 50 widgets concrets sans abstraction.

---

## Patterns proches

- **Observer** : diffusion d'événements ; Mediator encode souvent des *règles* de coordination.
- **Facade** : point d'entrée simplifié vers un sous-système, pas forcément entre pairs.
- **Command** : peut transporter les intentions vers le médiateur.

---

## Dans le monde réel

Contrôleurs de dialogs, Redux/store comme « hub » de formulaires, air traffic dans les sims, `Mediator` dans des libs UI, salles de chat. React Context + un petit orchestrateur joue souvent ce rôle sans s'appeler « Mediator ».

Pense aussi aux wizards multi-étapes : étape 1 valide → débloque étape 2 ; paiement échoué → revient à l'adresse. Si chaque étape appelle la suivante en dur, le flux devient illisible. Un médiateur « CheckoutWizard » concentre ces transitions et les rend testables (entrée événement → nouvelles étapes actives).

---

## Questions fréquentes (FAQ)

**C'est obligatoire en entretien ?** Parfois sous forme « comment éviter le couplage entre widgets ? »

**Ça remplace les frameworks ?** Non — les stores et contextes modernes incarnent souvent l'idée.

**Je dois tout refactoriser ?** Non — extrais d'abord le sous-graphe le plus spaghetti (3–4 champs liés).

---

## Checklist code review

- [ ] Les collègues ne s'importent pas entre eux
- [ ] Le médiateur reste focalisé (pas tout le domaine)
- [ ] Règles de coordination testables unitairement
- [ ] Nommage métier (`OrderFormMediator`, pas `Manager`)

---

## Exercice pratique (25–35 min)

Trois champs : pays, province, total. Sans médiateur, branche-les en direct. Refactorise avec un médiateur : changer le pays vide la province et recalcule. Compare le nombre d'imports croisés.

---

## Résumé

- Mediator = tour de contrôle : moins de liens N×N, plus de règles au centre.
- Idéal pour formulaires et collaborations locales.
- Garde le médiateur mince — sinon tu as juste déplacé le spaghetti.

---

## Navigation dans la série

- Précédent : [Chain of Responsibility](/blog/articles/design-patterns-chain-of-responsibility.html)
- Suivant : [Memento](/blog/articles/design-patterns-memento.html)
