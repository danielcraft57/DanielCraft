---
title: "Design system : composants, tokens et cohérence à l’échelle"
date: 2025-09-18
excerpt: "Pourquoi un design system n’est pas un catalogue : tokens, composants, guidelines, gouvernance et workflow dev. Objectif : cohérence, vitesse et qualité."
type: article
tags: [UI, design system, composants, tokens, front-end]
series: ux-ui-serie
series_order: 6
og_image: design-system-composants-tokens-1200x630.jpg
---

# Design system : composants, tokens et cohérence à l’échelle

Sans design system, chaque feature “réinvente” l’interface : boutons, espacements, états, erreurs…  
Résultat : incohérence, dette visuelle, vitesse qui s’écroule, et bugs UX partout.

Mais attention : un design system n’est pas une galerie Dribbble.  
C’est un **système de production** qui aligne design et dev.

---

## 1) Un design system, c’est quoi exactement ?

C’est l’ensemble de :

- **Design tokens** : couleurs, tailles, rayons, espacements, typographies
- **Composants** : bouton, input, modal, table, toast…
- **Règles d’usage** : quand utiliser quoi, patterns, accessibilité
- **Gouvernance** : qui décide, comment on change, comment on versionne

Le but n°1 : réduire le coût de décision.

---

## 2) Tokens : le socle (et la seule vérité)

Un token = une valeur nommée.

Exemples :

- `color.text.primary`
- `color.brand.600`
- `space.4`
- `radius.md`
- `font.size.sm`

Pourquoi c’est puissant :

- tu changes le thème sans tout casser
- tu garantis la cohérence
- tu peux synchroniser Figma ↔ code

La bonne pratique : éviter les noms “couleur‑technique” (`blue500`) au profit de noms “sémantiques” (`brand`, `success`, `danger`).

---

## 3) Composants : des UI “prêtes pour la vraie vie”

Un composant utile doit inclure :

- **états** : default / hover / active / disabled
- **accessibilité** : focus visible, aria, navigation clavier
- **variants** : sizes, intent (primary/secondary/danger)
- **comportements** : loading, erreurs, validations

Exemple : un bouton “pro” gère :

- l’état `loading`
- la prévention double clic
- le style focus (clavier)

---

## 4) Guidelines : éviter l’UI “au hasard”

Sans guidelines, même avec des composants, les écrans divergent.

Quelques guidelines utiles :

- hiérarchie : 1 action primaire par écran
- formulaires : validation, erreurs, labels
- contenus : titres, densité, vides
- tables : tri, pagination, filtres

Tu veux capturer les décisions récurrentes.

---

## 5) Gouvernance : sinon ça meurt

Un design system vit si tu as :

- un owner (ou une petite équipe)
- un process de contribution
- des règles de compatibilité / versioning
- des releases (changelog)

Sinon :

- chacun forke des variantes
- la dette revient en 3 mois

---

## 6) Workflow dev : Storybook, tests et qualité

Outils classiques :

- **Storybook** : doc vivante des composants
- tests visuels (screenshots) pour éviter les régressions
- lint / conventions UI
- tokens exportés (JSON) utilisés dans CSS/JS

Le design system devient un accélérateur quand il est **intégré au flux dev**, pas séparé.

---

## Conclusion

Un design system n’a de valeur que s’il :

- rend le produit plus cohérent
- accélère la livraison
- réduit les bugs UX

Commence petit : tokens + 5 composants critiques + guidelines de formulaires.  
Puis itère, comme un produit.

