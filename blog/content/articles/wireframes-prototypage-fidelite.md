---
title: "Maquettes : du croquis au prototype"
date: 2025-09-09
excerpt: "Low-fi, mid-fi, high-fi : choisir le bon niveau de détail selon la question à tester."
type: article
tags: [UX, wireframe, prototypage, UI, méthode]
series: ux-ui-serie
series_order: 3
og_image: wireframes-prototypage-fidelite-1200x630.jpg
---

# Maquettes : du croquis au prototype

Faire une maquette « belle » trop tôt, c'est un piège classique. Tu figes la forme alors que le problème n'est pas encore clair. Tout le monde commente la couleur du bouton pendant que le parcours reste bancal. À l'inverse, rester trop longtemps en blocs gris peut bloquer l'alignement : les stakeholders ne « voient » pas le produit, le branding reste abstrait, la hiérarchie floue.

L'enjeu n'est pas d'être puriste. C'est d'utiliser le bon niveau de fidélité pour valider la bonne décision au bon moment - et d'accepter que plus on avance vers le hi-fi, plus chaque changement coûte cher.

## Trois niveaux, trois types de questions

Le low-fi - wireframes papier ou blocs gris - sert à valider la structure et le parcours. Layout, hiérarchie, navigation. Le contenu placeholder est acceptable. L'avantage, c'est la vitesse : tu itères en minutes, pas en demi-journées. Personne ne s'attache à un rectangle gris comme à une maquette brandée.

Le mid-fi ajoute des composants plus réalistes, des textes plus proches du réel, des états esquissés (loading, erreur, vide). Tu valides surtout l'interaction et la compréhension. Est-ce que la personne sait quoi faire ? Est-ce que l'ordre des étapes tient la route ?

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/wireframe-fidelite.svg" alt="Schéma low-fi, mid-fi et high-fi pour le prototypage" class="schema-inline" width="640" />
  <figcaption>Low-fi pour la structure, mid-fi pour l'interaction, high-fi pour le look - et le coût de changement grimpe à chaque cran.</figcaption>
</figure>

Le hi-fi, c'est la maquette ou le prototype pixel-perfect : typo, couleurs, icônes, [micro-interactions](/blog/articles/micro-interactions-feedback-etats.html). Tu valides le look & feel et les détails [UI](/blog/articles/ux-ui-fondamentaux-differences.html). C'est aussi le moment où tu prépares le handoff - si ton [design system](/blog/articles/design-system-composants-tokens.html) suit, sinon tu prépares surtout des allers-retours.

La règle simple : chaque niveau répond à une question différente. Mélanger les questions, c'est mélanger les feedbacks.

## Le piège « on valide le design »

En réunion, on croit valider le parcours, l'[ergonomie](/blog/articles/ergonomie-heuristiques-nielsen.html), la compréhension. Mais si tu montres du hi-fi trop tôt, la conversation dérive. « Je préfère ce bleu. » « L'arrondi des cards. » « Et si on mettait une illustration ? » Ce n'est pas de la mauvaise foi. C'est humain : le cerveau accroche à ce qui est visible et poli.

La solution n'est pas d'interdire le goût. C'est de séquencer. Low-fi pour valider la logique. Hi-fi quand la logique est stable. Tu peux même le dire explicitement en début de revue : « Aujourd'hui on ne parle pas de couleurs. On parle de parcours. » Ça marche mieux que tu ne le crois.

## Prototype et maquette, ce n'est pas la même chose

Une maquette est une photo. Elle montre. Un prototype répond à des questions : que se passe-t-il si je clique ? Où est mon feedback ? Que voit l'utilisateur si c'est vide ou en erreur ?

Même un prototype low-fi peut être très efficace s'il couvre le happy path, une ou deux erreurs clés, et un état vide important. Tu n'as pas besoin de cinquante écrans. Tu as besoin de scénarios risqués. Prototyper ce qui est évident, c'est du théâtre. Prototyper ce qui peut casser, c'est de la méthode.



<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/wireframe-quand-monter.svg" alt="Schema de montee en fidelite wireframe vers prototype" class="schema-inline" width="640" />
  <figcaption>La fidelite suit la question : structure, flow, puis polish.</figcaption>
</figure>

## Une méthode simple en quatre temps

D'abord le user flow : dessine le parcours en cinq à sept étapes max. Ensuite les wireframes low-fi - un écran par étape. Puis un prototype cliquable : navigation et actions clés. Enfin le hi-fi ciblé, uniquement sur les écrans qui partent vraiment en développement.

Tu évites de « designer » vingt écrans alors que cinq partiront. Tu gardes de l'énergie pour les états et les edge cases, qui sont souvent là où le produit se joue.

Avant de monter en fidélité, pose-toi quelques questions. L'objectif utilisateur est-il clair sur chaque écran ? Y a-t-il une action principale ? La navigation est-elle cohérente ? Les états existent-ils - loading, erreur, vide, succès ? Les textes clés (labels, titres, erreurs) sont-ils compréhensibles ? Si ça bloque déjà ici, le hi-fi ne te sauvera pas. Il embellira le problème.

## Prototyper côté code (quand ça a du sens)

Si tu as déjà un design system solide, tu peux prototyper en code : Storybook, routes avec de la fake data, skeletons et états réels. L'avantage, c'est que tu valides des choses que Figma ment parfois - scroll, responsive, perf, [accessibilité](/blog/articles/accessibilite-wcag-checklist.html) clavier. L'inconvénient, c'est le coût : itérer sur un concept encore instable en code, c'est cher.

La bonne heuristique : concept flou = low-fi. Concept stable + système de composants prêt = prototype code bienvenu. Ne force pas l'un ou l'autre par dogme.

## Stakeholders : faire accepter le low-fi

Parfois le frein n'est pas technique, c'est politique. Un client ou un sponsor veut « voir le rendu ». Tu peux répondre de deux façons. Soit tu cèdes et tu perds deux jours de polish sur un parcours encore instable. Soit tu montres un low-fi cliquable avec un scénario réel, et tu expliques : « On valide d'abord que ça marche. Ensuite on l'habille. »

Un truc qui marche bien : présenter le low-fi comme un outil de décision, pas comme un « design incomplet ». Tu annonces ce qui est en scope et ce qui ne l'est pas. Tu notes les retours hors sujet (couleurs, branding) dans un parking pour plus tard. Tu reviens au hi-fi quand les décisions de parcours sont prises. La plupart des gens comprennent - surtout si tu leur fais gagner du temps.

## Choisir, c'est aussi dire non

Un bon prototype n'est pas « beau ». Il est utile : il réduit un doute précis. Low-fi pour décider vite, mid-fi pour comprendre l'interaction, hi-fi pour exécuter proprement. Et surtout : prototype ce qui est risqué, pas ce qui flatte l'ego en présentation.

Si tu sens que l'équipe débat du rayonnement d'une ombre alors que personne n'a testé le parcours d'inscription, redescends d'un cran de fidélité. Ce n'est pas un recul. C'est de la discipline. Le design qui avance, c'est celui qui change d'outil quand la question change - pas celui qui polish avant d'avoir compris. Garde cette phrase sous le coude : la fidélité suit la certitude. Pas l'inverse.
