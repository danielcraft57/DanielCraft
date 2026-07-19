---
title: "Petits signaux : dire à l'utilisateur ce qui se passe"
date: 2025-09-30
excerpt: "Hover, chargement, erreur, succes : le timing du feedback cree la confiance."
type: article
tags: [UX, UI, micro-interactions, feedback, design]
series: ux-ui-serie
series_order: 9
og_image: micro-interactions-feedback-etats-1200x630.jpg
---

# Petits signaux : dire à l'utilisateur ce qui se passe

Une interface est une conversation. L'utilisateur agit, le système répond. Les micro-interactions sont ces petites réponses qui font dire « OK, c'est pris en compte », « je suis au bon endroit », « je peux corriger ». Sans elles, même un bon produit paraît fragile - comme quelqu'un qui ne réagit jamais quand tu lui parles.

On parle de hover, focus, press, loading, succès, erreur. Pas de spectacle. De feedback. La différence entre une [UI](/blog/articles/ux-ui-fondamentaux-differences.html) qui « marche » et une UI qui rassure tient souvent là, dans ces 200 millisecondes et ces messages bien placés.

## Feedback : immédiat, clair, cohérent

Règle de timing simple. Moins de 100 ms : feedback visuel minimal - hover, press. Entre 100 et 500 ms : changement d'état, spinner dans le bouton. Au-delà : skeleton ou loader avec un texte (« Chargement… »). L'utilisateur doit toujours savoir si c'est en cours, réussi, ou en erreur.

Le silence est le pire feedback. Un clic sans réaction, même une demi-seconde, et le doute s'installe. Double clic. Rechargement. Ticket support. Tu n'as pas « un bug de perf » seulement - tu as une conversation cassée.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/micro-interactions-etats.svg" alt="Schéma des états UI : idle, hover, loading, error, success" class="schema-inline" width="640" />
  <figcaption>Idle → hover → loading → error ou success : chaque état doit être pensé, pas improvisé en prod.</figcaption>
</figure>

Reste cohérent : le même type d'action doit répondre de la même façon. Un toast ici, un message inline là, un rien ailleurs - l'utilisateur apprend moins vite et se méfie plus.

## Les états à documenter (pas seulement le succès)

Sur la plupart des composants et écrans, tu as au minimum idle, hover (et focus), loading, empty, error, success. Beaucoup d'équipes ne livrent que le succès. C'est là que l'expérience s'effondre au premier réseau lent ou au premier champ invalide.

Empty n'est pas error : « aucune donnée » doit proposer une prochaine étape, pas un écran mort. Error doit être actionnable. Success doit confirmer sans noyer. Loading doit empêcher les actions dangereuses (double soumission) sans figer toute la page si ce n'est pas nécessaire.

Documente ces états dans le [design system](/blog/articles/design-system-composants-tokens.html) et dans Storybook. Si ce n'est pas dans la story, ça n'existera pas en prod - ou ça existera en version bricolée à 23h.

## Boutons : le pattern qui inspire confiance

Un bouton robuste a un disabled clair, un loading qui bloque le double clic, une largeur stable (pas de saut quand le label devient « Envoi… »), et une confirmation après coup - toast ou message. Exemple : « Envoi… » puis « Envoyé » avec un lien « Voir ».

Le disabled sans explication frustre. Si tu désactives, dis pourquoi à proximité - champ manquant, droits insuffisants. Sinon l'utilisateur pense que l'UI est cassée.



<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/micro-timing-feedback.svg" alt="Schema du timing des micro-interactions UI" class="schema-inline" width="640" />
  <figcaption>Le timing du feedback cree (ou casse) la confiance.</figcaption>
</figure>

Même logique pour les actions destructives : demande de confirmation, wording clair, feedback après coup. La micro-interaction ici, c'est aussi la prévention de l'erreur, pas seulement l'animation.

## Erreurs : utiles, pas bruyantes

Une erreur proche de l'endroit où ça se passe, qui explique comment corriger, sans jargon (« 500 », « exception »). « Mot de passe trop court (min. 12 caractères). » Si l'erreur est globale : « Impossible d'enregistrer. Vérifie ta connexion et réessaie. »

Évite l'avalanche de toasts rouges. Évite le message unique en haut de page pour dix champs. Évite de vider le formulaire après une erreur - tu punis l'utilisateur pour un oubli. L'erreur bien conçue réduit le support. L'erreur mal conçue le multiplie.

## Transitions : guider sans distraire

Rapides, non bloquantes, qui gardent le contexte - on comprend ce qui change. Évite les animations « waouh » qui ralentissent l'usage. Le motion sert la continuité (d'où vient ce panneau ?) et l'attention (où regarder ?), pas le portfolio.

Sur mobile, encore plus vrai : chaque milliseconde compte, et les effets lourds coûtent en perf et en batterie. Sobriété. Intention.

## Focus, hover, clavier : [accessibilité](/blog/articles/accessibilite-wcag-checklist.html) = micro-interaction

Le focus visible indique la position au clavier et rassure sur l'action possible. Hover et active donnent de la matière à la souris. Ce ne sont pas des « plus ». Ce sont des états de base. Les enlever pour un look minimaliste, c'est couper la conversation pour une partie des utilisateurs.

Teste Tab sur ton parcours. Si tu te perds, les utilisateurs clavier aussi. Si le focus est invisible, tu as un bug UX - pas un choix de style.

## Quatre questions par action

Pour chaque action critique : que voit l'utilisateur pendant ? Après ? Si ça échoue ? Peut-il annuler ou revenir ? Si tu réponds clairement, l'écran devient « pro » sans ajouter de features.

Ajoute ces questions à la review design ou à la Definition of Done. Ça coûte peu. Ça évite les écrans muets. Et ça aligne design et front sur les états avant le merge, pas après le ticket support.

## Optimistic UI et limites

L'UI optimiste - afficher le succès avant la confirmation serveur - peut donner une sensation de vitesse. Elle marche quand l'échec est rare et réversible. Elle casse la confiance quand l'action est critique (paiement, suppression) ou quand le rollback est confus. Dans ces cas, un loading honnête bat un succès prématuré suivi d'un « finalement non ».

Même idée pour les skeletons : utiles pour indiquer la structure pendant le chargement, trompeurs s'ils restent trop longtemps sans message. Au-delà de quelques secondes, dis ce qui se passe. L'utilisateur préfère un texte clair à une animation élégante qui ment sur le temps restant.

## Ce qu'il ne faut pas animer

Tout n'a pas besoin de micro-interaction. Les listes longues qui rebondissent, les pages qui glissent pour le plaisir, les loaders décoratifs sur des actions instantanées - ça distrait. Réserve le motion aux moments où l'état change vraiment : ouverture, soumission, erreur, succès. Moins il y en a, plus chaque signal compte.

Les micro-interactions ne sont pas du détail. Ce sont des garanties. Elles transforment un produit qui fonctionne en produit qui inspire confiance. Idle, hover, loading, error, success - dessine la conversation complète, pas seulement la phrase du milieu.
