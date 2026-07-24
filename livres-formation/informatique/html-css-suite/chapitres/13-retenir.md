# Chapitre 13 - A retenir

Tu as parcouru pas mal de terrain. Avant les ateliers et les chapitres "affutage", on pose les pieces sur la table. Pas une encyclopedie. Une checklist mentale.

## Structure

Le HTML semantique nomme les pieces : `header`, `nav`, `main`, `article`, `section`, `footer`, parfois `aside`. Les `div` restent pour le layout neutre. Un `main`, un `h1` fort.

## Cascade

A poids egal, la derniere regle gagne. Les classes pesent plus que les types. Les ID pesent encore plus (evite-les pour le style quotidien). `!important` presque jamais. L'inspecteur montre qui gagne.

## Variables

`:root` pour la palette et les rythmes (`--couleur-principale`, `--espace`, `--rayon`...). `var(--nom)` partout. Une variable peut se redefinir localement dans un bloc. Changer le theme = changer le `:root` d'abord.

## Grid

`display: grid`, `grid-template-columns`, `gap`, `repeat`, `minmax` / `auto-fit` pour des galeries. `grid-template-areas` pour une page header/contenu/aside/pied. Placement simple avec `grid-column` si besoin.

## Flex vs Grid

Flex : une dimension (menus, barres, alignements). Grid : deux dimensions (plan de page, damier). Souvent Grid dehors, Flex dedans. Un mode par conteneur.

## Images

`max-width: 100%` + `height: auto`. `object-fit: cover` pour des cadres. `alt` utile. Poids du fichier soigne. `srcset` comme idee pour servir la bonne largeur.

## Formulaires

Labels visibles relies. Champs en pleine largeur dans un conteneur borne. Focus clair. Bouton de marque. Deux colonnes en Grid sur desktop si utile, une sur mobile.

## Mouvement

Transitions courtes sur l'etat de base. Hover doux. `prefers-reduced-motion` respecte. Pas de cirque.

## Accessibilite

Focus visible, contrastes, labels, ordre Tab logique. Voile sombre si texte sur photo. Tester au clavier.

## Mini-projet

Une home responsive qui assemble variables + Grid + semantique + formulaire + transitions legeres, c'est le niveau vise.

## Fil rouge

Page produit, blog, landing : les memes reflexes. Chez DanielCraft, on prefere une page simple solide a une page chargee fragile.

## A toi

Sans regarder tes notes, ecris dix lignes : cinq choses que tu sais faire maintenant, cinq pieges que tu veux eviter. Garde ce papier a cote des ateliers.
