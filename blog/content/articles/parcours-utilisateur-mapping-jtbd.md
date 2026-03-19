---
title: "Parcours utilisateur : user flows, journey map et JTBD"
date: 2025-09-16
excerpt: "Cartographier un parcours pour réduire la friction : user flow, journey map, Jobs To Be Done. Outils simples + exemples pour passer de l’idée à une expérience fluide."
type: article
tags: [UX, parcours, journey map, JTBD, produit]
series: ux-ui-serie
series_order: 5
og_image: parcours-utilisateur-mapping-jtbd-1200x630.jpg
---

# Parcours utilisateur : user flows, journey map et JTBD

Un produit échoue rarement parce qu’un bouton est “moche”.  
Il échoue parce que le parcours est confus : trop d’étapes, mauvais ordre, informations manquantes, ou anxiété (“est-ce que c’est bien pris en compte ?”).

Cartographier un parcours permet de **rendre visible** ce qui est habituellement implicite. Et donc de l’améliorer.

---

## 1) User flow : le minimum vital

Un **user flow** est un schéma d’étapes :

- point d’entrée
- décisions (“si connecté / si pas connecté”)
- étapes
- sortie (objectif atteint)

Il est parfait pour :

- aligner produit + design + dev
- repérer les dépendances (auth, paiement, permissions)
- définir le “happy path” et les erreurs majeures

Règle d’or : un flow efficace tient sur **une page**.

---

## 2) Journey map : comprendre l’expérience, pas seulement les écrans

Une **journey map** ajoute :

- émotions (stress, confiance, doute)
- contexte (mobile, transport, bureau)
- canaux (mail, SMS, app, support)

Elle est utile quand :

- l’expérience dépasse l’écran (onboarding, support, relances)
- la confiance est un enjeu (paiement, données sensibles)

Exemple : inscription

- écran : “Crée ton compte”
- émotion : “je me méfie, je ne veux pas de spam”
→ décision UX : expliquer clairement l’usage de l’email, rassurer, montrer la valeur.

---

## 3) JTBD : le travail à accomplir

JTBD (Jobs To Be Done) aide à éviter de raisonner en “features”.

Formule :

> “Quand [situation], je veux [motivation], afin de [résultat].”

Exemple :

> “Quand je prépare un devis pour un client pressé, je veux générer une proposition claire en 3 minutes, afin de répondre vite et ne pas perdre l’opportunité.”

Le “job” guide :

- l’ordre des étapes
- les informations essentielles
- les compromis (moins de champs, plus de guidance)

---

## 4) Transformer un flow en écrans

Une méthode simple :

1. Liste les étapes du flow (verbes) : “choisir”, “renseigner”, “valider”, “payer”
2. Pour chaque étape : une question
   - “Qu’est-ce que l’utilisateur doit décider ?”
   - “Quelles infos lui manquent ?”
3. Dessine un wireframe par étape
4. Ajoute les états : loading / empty / error / success

Tu construis un parcours **orienté décision**, pas une suite de pages.

---

## 5) Points de friction classiques (à chercher en priorité)

- **Sauts de contexte** : on demande une info trop tôt (ex. paiement avant la valeur)
- **Étapes inutiles** : confirmation double, écrans de transition vides
- **Anxiété** : pas de feedback, pas d’aperçu, pas de “ce qui va se passer”
- **Erreurs tardives** : validation à la fin seulement

---

## 6) Indicateurs simples pour mesurer l’amélioration

Même sans gros outillage :

- taux de complétion du parcours
- temps moyen pour accomplir la tâche
- drop-off par étape
- nombre de retours en arrière

Ces métriques sont une boussole : elles montrent où creuser.

---

## Conclusion

Un bon parcours n’est pas celui qui “montre tout”.  
C’est celui qui guide l’utilisateur vers son objectif, en réduisant :

- le nombre de décisions
- l’incertitude
- la charge mentale

User flows, journey maps et JTBD sont 3 outils complémentaires pour y arriver.

