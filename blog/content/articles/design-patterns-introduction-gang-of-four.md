---
title: "Design patterns : des recettes pour un code plus clair"
date: 2026-04-01
excerpt: "Les 23 idees du Gang of Four, expliquees simplement : a quoi ca sert, quand s'en servir."
type: article
tags: [Design Patterns, GoF, junior, SOLID, architecture]
og_image: design-patterns-introduction-gang-of-four-1200x630.jpg
series: design-patterns-serie
series_order: 1
---

# Design patterns : des recettes pour un code plus clair

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-intro.svg" alt="Schema familles de design patterns" class="schema-inline" width="640" />
  <figcaption>Creationnels, structurels, comportementaux.</figcaption>
</figure>

Tu as déjà copié-collé du code sans comprendre sa structure ? Ou une classe de 800 lignes que personne n'ose toucher ? Les **design patterns** t'aident à **nommer** des solutions qui marchent, à **communiquer** avec ton équipe, et à **éviter** de réinventer la roue.

Cette série couvre les **23 patterns du Gang of Four (1994)**. Contrairement à beaucoup de catalogues, nous les classons ici du **plus populaire au moins rencontré** en entreprise — pour que tu apprennes d'abord ce que tu verras le plus souvent en code review et en entretien.

---

## Qu'est-ce qu'un design pattern ?

Un design pattern est une **solution réutilisable** à un problème récurrent de conception. Ce n'est pas une librairie : c'est une **organisation** de classes, modules et objets pour garder le code lisible, testable et évolutif.

### Analogie du quotidien

Imagine une cuisine : tu ne réinventes pas la recette de la sauce béchamel à chaque fois. Tu dis « béchamel », et tout le monde sait quoi faire. Un pattern, c'est pareil : tu dis « Observer » ou « Strategy », et l'équipe visualise la même structure sans redessiner le schéma au tableau.

### Ce qu'un pattern n'est pas

- Une règle absolue (« toujours Singleton » → faux).
- Du code à copier-coller sans réfléchir.
- Une excuse pour sur-architecturer un petit script.

### Ce qu'un pattern est

- Un **vocabulaire partagé** : « Observer ici » = tout le monde visualise la même chose.
- Une **réponse éprouvée** à un problème précis.
- Un **outil de réflexion** avant le dixième `if/else`.

---

## Les trois familles (rappel)

| Famille | Question | Exemples populaires |
|---------|----------|---------------------|
| **Créationnels** | Comment instancier ? | Singleton, Factory, Builder |
| **Structurels** | Comment composer ? | Adapter, Decorator, Facade |
| **Comportementaux** | Comment répartir les comportements ? | Observer, Strategy, Command |

En pratique : un **créationnel** t'aide quand `new` devient un casse-tête (config, variantes, coûts). Un **structurel** colle des briques incompatibles ou ajoute des couches sans tout casser. Un **comportemental** clarifie qui parle à qui, et comment un objet change de réaction selon le contexte.

Petit aperçu en code — sans pattern, tout est mélangé :

```javascript
// Tout dans une fonction : difficile à tester et à étendre
function checkout(user, cart, mode) {
  if (mode === 'express') { /* … */ }
  else if (mode === 'standard') { /* … */ }
  // + paiement, + logs, + emails…
}
```

Avec un vocabulaire de patterns, tu sépares : **Strategy** pour le mode d'expédition, **Observer** pour les notifications, **Facade** pour l'API publique. Ce n'est pas obligatoire dès la ligne 1 — c'est un langage pour refactoriser quand ça fait mal.

---

## Ordre de la série (popularité décroissante)

1. Singleton · 2. Factory Method · 3. Observer · 4. Strategy · 5. Decorator · 6. Adapter · 7. Facade · 8. Command · 9. Template Method · 10. Builder · 11. Iterator · 12. State · 13. Proxy · 14. Abstract Factory · 15. Composite · 16. Bridge · 17. Prototype · 18. Flyweight · 19. Chain of Responsibility · 20. Mediator · 21. Memento · 22. Visitor · 23. Interpreter

Tu peux lire linéairement ou sauter vers le pattern qui correspond à ta douleur du moment.

---

## SOLID en version junior

1. **S**ingle Responsibility — une raison de changer par classe.
2. **O**pen/Closed — étendre sans tout casser.
3. **L**iskov — les sous-types restent substituables.
4. **I**nterface Segregation — petites interfaces.
5. **D**ependency Inversion — dépendre d'abstractions.

Les patterns et SOLID se renforcent : Strategy et Decorator aident l'Open/Closed ; Factory et Dependency Injection poussent vers Dependency Inversion. Tu n'as pas besoin de réciter les lettres en entretien — montre que tu sépares les responsabilités.

---

## Comment lire chaque article

1. **En une phrase** + **Le problème** — si ça ne parle pas, passe.
2. **Schéma** + **TypeScript** — cœur de la série.
3. **Python** si tu es plutôt backend.
4. **Quand ne pas l'utiliser** — souvent le plus utile.
5. **Exercice** 25–35 min sur un mini-projet.

---

## Erreurs classiques des juniors

| Erreur | Conséquence | Attitude saine |
|--------|-------------|----------------|
| Pattern « pour faire joli » | Code verbeux | Commence simple ; refactorise quand ça fait mal |
| God Object | Tout dans une classe | Une responsabilité à la fois |
| Confondre Factory / Abstract Factory / Builder | Mauvais choix | Lis les 3 articles créationnels |
| Pas de tests | Pattern rigide | Test avant structure |

Un autre piège : vouloir appliquer les 23 patterns dans un projet scolaire. Choisis **un** problème réel (switch géant, couplage N×N, undo impossible) et un pattern adapté. Le reste viendra avec l'expérience.

---

## Exercice : cartographier ton projet

Sur un repo perso, note : création compliquée → créationnel ; API tierce → structurel ; gros `switch` comportement → comportemental. Pas besoin de tout refactoriser : entraîne ton **œil**. En 20 minutes, tu auras une carte mentale plus précieuse qu'une checklist mémorisée.

---

## Résumé

- 23 patterns GoF, expliqués pour juniors, avec schémas et exemples TS/Python.
- Ordre **popularité** (pas livre) pour un apprentissage pragmatique.
- Un pattern = un vocabulaire + une réponse à une douleur, pas une décoration.
- Article suivant : **Singleton**.

---

## Navigation

- Suivant : [Singleton](/blog/articles/design-patterns-singleton.html)
