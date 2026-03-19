---
title: "Wireframes & prototypage : choisir le bon niveau de fidélité"
date: 2025-09-09
excerpt: "Low-fi, mid-fi, hi-fi : quel prototype pour quelle décision ? Méthode, pièges classiques et une checklist pour avancer vite sans surdesigner."
type: article
tags: [UX, wireframe, prototypage, UI, méthode]
series: ux-ui-serie
series_order: 3
og_image: wireframes-prototypage-fidelite-1200x630.jpg
---

# Wireframes & prototypage : choisir le bon niveau de fidélité

Faire une maquette “belle” trop tôt est un piège : tu figes la forme alors que le problème n’est pas encore clair.  
À l’inverse, rester en wireframe gris trop longtemps peut bloquer l’alignement (stakeholders, branding, hiérarchie).

L’enjeu : utiliser **le bon niveau de fidélité** pour valider **la bonne décision** au bon moment.

---

## 1) Les 3 niveaux (et ce qu’ils valident)

### Low‑fi (wireframes)
Objectif : valider **structure + parcours**.

- Layout, hiérarchie, navigation
- Contenu “placeholder” acceptable
- Rapide à itérer

### Mid‑fi (structure + premiers composants)
Objectif : valider **interaction + compréhension**.

- Composants “réalistes”
- États (loading/error/empty) esquissés
- Textes plus proches du réel

### Hi‑fi (maquette / prototype pixel‑perfect)
Objectif : valider **look & feel + détails UI**.

- Typo, couleurs, icônes
- Micro‑interactions
- Prêt pour handoff dev (si le système suit)

---

## 2) Le piège numéro 1 : “On valide le design”

En réunion, on croit valider :

- le parcours
- l’ergonomie
- la compréhension

Mais si c’est hi‑fi, tout le monde commente :

- la couleur du bouton
- l’arrondi des cards
- “je préfère ce bleu”

Solution : **low‑fi pour valider la logique**, hi‑fi quand la logique est stable.

---

## 3) Prototype ≠ maquette

Une maquette est une photo. Un prototype répond à :

- “Que se passe‑t‑il si je clique ?”
- “Où est mon feedback ?”
- “Que voit l’utilisateur si c’est vide / en erreur ?”

Même un prototype low‑fi peut être très efficace s’il couvre :

- le happy path
- 1 ou 2 erreurs clés
- 1 état vide important

---

## 4) Une méthode simple en 4 étapes

1. **User flow** : dessiner le parcours (5–7 étapes max)
2. **Wireframes low‑fi** : 1 écran par étape
3. **Prototype cliquable** : navigation + actions clés
4. **Hi‑fi ciblé** : uniquement sur les écrans qui partent en dev

Tu évites de “designer” 20 écrans alors que 5 partiront réellement.

---

## 5) Checklist wireframes “suffisants”

Avant de passer à la fidélité supérieure, vérifie :

- l’objectif utilisateur est clair sur chaque écran
- il y a une action principale (CTA)
- la navigation est cohérente
- les states existent (loading / error / empty / success)
- les textes clés sont compréhensibles (labels, titres, erreurs)

Si ça bloque déjà ici, le hi‑fi ne te sauvera pas.

---

## 6) Bonus : prototypage rapide côté dev

Tu peux aussi prototyper en code (surtout si tu as déjà un design system) :

- Storybook / playground composants
- routes “fake data”
- skeleton + états

Avantage : tu valides des choses réelles (scroll, responsive, performance).  
Inconvénient : plus coûteux si tu itères sur un concept instable.

---

## Conclusion

Un bon prototype n’est pas “beau”, il est **utile** : il réduit un doute précis.  
Low‑fi pour décider vite, hi‑fi pour exécuter proprement, et surtout : **prototype ce qui est risqué**, pas ce qui est évident.

