---
title: "Micro‑interactions : feedback, états et confiance utilisateur"
date: 2025-09-30
excerpt: "Loading, succès, erreurs, hover, focus : les micro‑interactions font la différence entre une UI “qui marche” et une UI rassurante. Patterns concrets."
type: article
tags: [UX, UI, micro-interactions, feedback, design]
series: ux-ui-serie
series_order: 9
og_image: micro-interactions-feedback-etats-1200x630.jpg
---

# Micro‑interactions : feedback, états et confiance utilisateur

Une interface est une conversation : l’utilisateur agit, le système répond.  
Les micro‑interactions sont ces petites réponses qui font dire :

- “OK, ça a pris en compte”
- “Je suis au bon endroit”
- “Je peux corriger”

Sans micro‑interactions, même un bon produit paraît fragile.

---

## 1) Le feedback : immédiat, clair, cohérent

Règle simple :

- < 100 ms : feedback visuel minimal (hover, press)
- 100–500 ms : changement d’état (spinner dans le bouton)
- > 500 ms : skeleton/loader + texte (“Chargement…”)

L’utilisateur doit comprendre : **est-ce en cours, réussi, ou en erreur ?**

---

## 2) Les 4 états essentiels (à documenter)

Sur 90 % des composants/écrans, tu as :

- **Loading** : attente
- **Empty** : pas de données (et ce n’est pas une erreur)
- **Error** : action possible ou explication
- **Success** : confirmation

Beaucoup d’UI ne gèrent que “success”, et c’est là que l’expérience s’effondre.

---

## 3) Boutons : le pattern “pro”

Un bouton robuste :

- a un état `disabled` (pas cliquable)
- un état `loading` (empêche les doubles clics)
- garde sa largeur (évite de sauter)
- affiche une confirmation (toast ou message)

Exemple UX :

- “Envoi…” → “Envoyé” + lien “Voir”

---

## 4) Erreurs : être utile, pas bruyant

Une erreur doit :

- être proche de l’endroit où ça se passe
- expliquer comment corriger
- éviter le jargon (“500”, “exception”)

Exemple :

> “Mot de passe trop court (min 12 caractères).”

Et si l’erreur est globale :

> “Impossible d’enregistrer. Vérifie ta connexion et réessaie.”

---

## 5) Transitions : guider sans distraire

Les transitions doivent :

- être rapides
- ne pas bloquer
- garder le contexte (on sait ce qui change)

Évite les animations “effet waouh” qui ralentissent l’usage.

---

## 6) Focus, hover, clavier : micro‑interaction = accessibilité

Le focus visible est une micro‑interaction cruciale :

- il indique la position (clavier)
- il rassure (action possible)

Même sur mouse, hover et active states donnent de la “matière” à l’UI.

---

## 7) Une checklist micro‑interactions pour un écran

Pour chaque action :

- que voit l’utilisateur **pendant** ?
- que voit l’utilisateur **après** ?
- que se passe‑t‑il si ça échoue ?
- puis‑je annuler / revenir ?

Si tu réponds clairement à ces 4 questions, ton écran devient “pro”.

---

## Conclusion

Les micro‑interactions ne sont pas du détail : ce sont des **garanties**.  
Elles transforment un produit qui “fonctionne” en produit qui inspire confiance.

