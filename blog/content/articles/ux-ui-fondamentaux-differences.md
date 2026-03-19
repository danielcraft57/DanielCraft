---
title: "UX vs UI : différences, rôles et comment les faire marcher ensemble"
date: 2025-09-02
excerpt: "UX et UI sont souvent confondus. Voici une définition claire, les responsabilités, les livrables, et une méthode simple pour aligner produit, design et dev."
type: article
tags: [UX, UI, design, ergonomie, produit]
series: ux-ui-serie
series_order: 1
og_image: ux-ui-fondamentaux-differences-1200x630.jpg
---

# UX vs UI : différences, rôles et comment les faire marcher ensemble

« On refait l’UX ? » — parfois cette phrase veut dire : *changer les couleurs*.  
Et « on fait l’UI » veut parfois dire : *mettre des boutons*. Résultat : confusion, tensions, et un produit qui avance au hasard.

Cet article met tout à plat, de façon **pragmatique** : ce qu’est l’UX, ce qu’est l’UI, ce que ça change dans un projet, et comment organiser le travail pour que design et dev se renforcent.

---

## 1) UX et UI : une définition simple

- **UX (User Experience)** : l’expérience globale.  
  L’utilisateur comprend‑il ce qui se passe ? Atteint‑il son objectif ? Est‑ce fluide, rassurant, cohérent ?

- **UI (User Interface)** : l’interface visible et interactive.  
  Typographie, couleurs, espacements, composants, états, micro‑interactions.

Une manière simple de le voir :

- UX = **le parcours** (structure, logique, friction, clarté)
- UI = **le rendu** (forme, hiérarchie visuelle, feedback)

Les deux sont inséparables : une bonne UI peut cacher un mauvais parcours pendant un temps, mais pas longtemps.

---

## 2) Qui fait quoi (et pourquoi ce n’est jamais “un seul rôle”)

Dans la vraie vie :

- Un **Product** clarifie objectifs, KPIs, contraintes, priorités.
- Un **UX designer** structure : besoins, tâches, parcours, tests.
- Un **UI designer** systématise : composants, styles, hiérarchie, cohérence.
- Un **dev** rend tout ça concret : performance, accessibilité, états réels, edge cases.

La compétence clé n’est pas le titre, c’est la capacité à **prendre de bonnes décisions** avec des contraintes.

---

## 3) Livrables utiles (et ceux qui font perdre du temps)

Ce qui aide réellement :

- **User stories + critères d’acceptation** (clairs et testables)
- **User flow / parcours** (schéma simple)
- **Wireframes** (structure, sans fioritures)
- **Prototype cliquable** (pour valider un scénario)
- **Design system** (composants + règles)
- **Spécifications d’états** (loading, empty, error, success)

Ce qui peut être contre‑productif :

- Maquettes pixel‑perfect trop tôt, sans validation du parcours
- Docs interminables, jamais lues
- Un design system “catalogue” sans usage réel

Un bon livrable = celui qui **réduit l’incertitude** et **évite un aller‑retour**.

---

## 4) La règle d’or : partir de la tâche, pas de l’écran

Un écran n’est qu’un moyen. La question est :

> Quelle tâche l’utilisateur veut accomplir, dans quel contexte, avec quelles contraintes ?

Exemple (bête mais fréquent) :

- Objectif : *envoyer un devis en 2 minutes depuis un téléphone*
- Contrainte : réseau moyen, une main, stress, peu de temps

Une UI “belle” ne compense pas un parcours qui demande 12 champs obligatoires et 3 pages.

---

## 5) Une méthode simple pour aligner tout le monde

Quand tu démarres une feature, fais ce mini‑rituel :

1. **Objectif utilisateur** : “Je veux … pour …”
2. **Critère de succès** : “On considère que c’est réussi si …”
3. **Parcours cible** : 5–7 étapes max, “happy path” + 2 échecs majeurs
4. **États** : loading / vide / erreur / succès
5. **Instrumentation** : 1–2 événements analytics utiles

En 30 minutes, tu évites 3 jours d’itérations floues.

---

## 6) UX/UI côté dev : le piège des “fausses finitions”

Deux pièges classiques :

- **Tout est beau… en données parfaites**  
  (pas d’erreur, pas de latence, pas de permissions)
- **Tout marche… mais c’est anxiogène**  
  (pas de feedback, pas d’état, pas de confirmation)

Un produit “pro” est un produit qui gère :

- Les formulaires incomplets
- Les erreurs API
- Les listes vides
- Les permissions
- Les retards réseau

UX et UI, c’est aussi ça : l’interface quand *ça se passe mal*.

---

## 7) Conclusion : l’UX est un système, l’UI est son langage

Si tu retiens une idée :

- UX = **les décisions** (parcours, priorités, clarté)
- UI = **l’exécution visuelle** (hiérarchie, cohérence, feedback)

Le meilleur combo est celui où :

- l’UX réduit la friction
- l’UI rend la friction visible (et rassure)
- le dev rend tout robuste, accessible et performant

La suite de la série va creuser l’ergonomie (heuristiques), la recherche utilisateur, le design system, l’accessibilité et les micro‑interactions.

