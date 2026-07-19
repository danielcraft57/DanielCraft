---
title: "UX et UI : la sensation contre le look"
date: 2025-09-02
excerpt: "L'expérience vécue vs l'interface visible — et comment les faire marcher ensemble."
type: article
tags: [UX, UI, design, ergonomie, produit]
series: ux-ui-serie
series_order: 1
og_image: ux-ui-fondamentaux-differences-1200x630.jpg
---

# UX et UI : la sensation contre le look

Tu as deja entendu "on refait l'UX" pour parler d'un changement de couleur ? Ou "on fait l'UI" pour dire "on met des boutons" ? Ca arrive tout le temps.

Le probleme, ce n'est pas le vocabulaire. C'est que derriere ces mots flous, le projet avance au feeling. Produit, design et dev ne parlent plus de la meme chose. Et l'utilisateur trinque.

Cet article remet les pieds sur terre. Ce qu'est vraiment l'**UX**. Ce qu'est l'**UI**. Ce que ca change dans un sprint. Et comment faire travailler tout le monde dans le meme sens.

## Deux mots, deux jobs (qui se croisent)

L'UX, User Experience, c'est l'**experience** globale. Est-ce que la personne comprend ou elle est ? Est-ce qu'elle atteint son objectif sans se battre avec l'outil ? Est-ce que le parcours est rassurant ?

Tu peux avoir une interface jolie et une UX pourrie : l'utilisateur clique, hesité, revient en arriere, abandonne. Il ne dira pas "l'UI est belle". Il dira "c'est complique".

L'UI, User Interface, c'est le **rendu** visible et interactif. La typo, les couleurs, les espaces, les composants, les etats d'un bouton. C'est le langage visuel du produit. Une bonne UI clarifie. Une mauvaise UI noie l'intention sous du bruit - meme si le parcours etait bien pense.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/ux-vs-ui.svg" alt="Schéma UX vs UI : expérience vécue et interface visible" class="schema-inline" width="640" />
  <figcaption>UX = comment ça se vit. UI = comment ça se voit. Les deux se renforcent - ou s'annulent.</figcaption>
</figure>

Une image mentale qui marche bien : l'UX, c'est le **trajet**. L'UI, c'est la signaletique et le vehicule. Tu peux peindre une voiture magnifique. Si le GPS te fait faire trois detours pour une adresse a deux coins, tu ne reviendras pas.

## Qui fait quoi (le titre compte moins que la decision)

Dans la vraie vie, les roles se chevauchent. Un product owner clarifie l'objectif et les priorites. Un UX designer creuse le besoin, structure les taches, teste. Un UI designer systematise : composants, styles, coherence. Un developpeur rend tout ca concret - perf, accessibilite, cas limites.

Ce qui compte vraiment, ce n'est pas qui porte quel badge sur LinkedIn. C'est qui prend les bonnes **decisions** avec les contraintes du moment. Petite equipe ? La meme personne peut faire UX et UI. Grosse boite ? Les roles se specialisent. Le piege reste le meme : croire que "le design" se resume a coller des pixels alors que le parcours n'est meme pas valide.

## Des livrables qui reduisent le doute

Certains artefacts aident vraiment. Une user story avec des criteres testables. Un **user flow** d'une page. Des **wireframes** qui montrent la structure sans se battre sur la couleur. Un prototype cliquable. Un design system vivant. Des specs d'etats : loading, vide, erreur, succes.

Sans ca, le dev invente. Et l'utilisateur decouvre des trous.

D'autres livrables font perdre du temps. La maquette pixel-perfect trop tot. Le document de 40 pages que personne ne lit. Le design system "vitrine" sans usage reel. Un bon livrable, c'est celui qui evite un aller-retour - pas celui qui impressionne en reunion.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/ux-ui-livrables.svg" alt="Schema des livrables UX versus UI" class="schema-inline" width="640" />
  <figcaption>UX produit des decisions ; UI les rend visibles et coherentes.</figcaption>
</figure>

Pour aller plus loin sur les maquettes, vois [wireframes et fidelite](/blog/articles/wireframes-prototypage-fidelite.html). Sur le systeme de composants : [design system](/blog/articles/design-system-composants-tokens.html).

## Partir de la tache, pas de l'ecran

Un ecran n'est qu'un moyen. La vraie question : quelle **tache** l'utilisateur veut accomplir, dans quel contexte, avec quelles contraintes ?

Exemple banal. Objectif : envoyer un devis en deux minutes depuis un telephone. Contrainte : reseau moyen, une main libre, client qui attend. Si tu demandes douze champs obligatoires et trois pages avant validation, aucune UI "premium" ne sauvera le parcours. L'utilisateur abandonnera - ou enverra un devis bancal par WhatsApp.

Cette regle change la facon de demarrer une feature. Tu ne commences pas par "on a besoin d'un ecran parametres". Tu commences par "la personne doit pouvoir X sans Y". Ensuite tu dessines le chemin le plus court. Ensuite seulement tu habilles. Pour cartographier ca proprement : [parcours et JTBD](/blog/articles/parcours-utilisateur-mapping-jtbd.html).

## Un mini-rituel pour aligner tout le monde

Avant de plonger dans Figma ou dans le code, prends trente minutes. Objectif utilisateur en une phrase : "Je veux … pour …". Critere de succes : "On considere que c'est reussi si …". Parcours cible en cinq a sept etapes max - le happy path, plus deux echecs majeurs. Etats a prevoir. Un ou deux evenements analytics utiles.

Ce rituel parait simple. Il evite trois jours d'iterations floues. Produit, design et tech repartent avec la **meme carte**.

## Le piege des fausses finitions cote dev

Deux classiques. Tout est beau… avec des donnees parfaites : pas d'erreur, pas de latence. Ou tout "marche"… mais c'est anxiogene : pas de feedback, pas d'etat, pas de confirmation. L'utilisateur clique, rien ne bouge, il reclique, double paiement.

Un produit pro, c'est un produit qui gere les formulaires incomplets, les erreurs API, les listes vides, les droits insuffisants. UX et UI, c'est aussi - et surtout - l'interface quand ca se passe **mal**. C'est la que la confiance se gagne. Pour ces petits signaux : [micro-interactions](/blog/articles/micro-interactions-feedback-etats.html).

## Faire marcher UX et UI ensemble

Si tu retiens une seule idee : l'UX, ce sont les decisions - parcours, priorites, clarte. L'UI, c'est l'execution visuelle - hierarchie, coherence, feedback. Le meilleur combo, c'est celui ou l'UX reduit la friction, l'UI rend les actions comprehensibles, et le dev rend le tout robuste et accessible.

Tu n'as pas besoin d'une armee. Tu as besoin d'un vocabulaire partage, d'un parcours valide avant le polish, et d'une obsession pour les etats reels. La suite de la serie creuse l'[ergonomie Nielsen](/blog/articles/ergonomie-heuristiques-nielsen.html), la [recherche utilisateur](/blog/articles/ux-recherche-utilisateur-interviews-tests.html), la [typo et la grille](/blog/articles/ui-typographie-couleurs-grille.html), l'[accessibilite](/blog/articles/accessibilite-wcag-checklist.html) et comment [mesurer l'UX](/blog/articles/mesurer-ux-kpis-analytics-ab-testing.html).
