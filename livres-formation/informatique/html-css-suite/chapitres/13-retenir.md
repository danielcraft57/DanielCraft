# Chapitre 13 - A retenir

Tu as parcouru pas mal de terrain. Avant les ateliers et les chapitres d'affutage, on pose les pieces sur la table. Pas une encyclopedie. Une checklist mentale en paragraphes, pour que ca tienne quand tu codes sans notes. Chez DanielCraft, on prefere cinq reflexes solides a cinquante astuces oubliees.

Imagine une page produit, un petit blog, une landing. Tu ouvres le fichier. Tu te demandes, dans l'ordre : la structure a-t-elle un sens ? Qui gagne en CSS ? Les couleurs viennent-elles d'un seul endroit ? Le plan tient-il en large et en etroit ? Les images et le formulaire sont-ils accueillants ? Le mouvement est-il calme ? Le clavier passe-t-il ? Si tu reponds oui a ca, tu es deja au niveau "suite", pas seulement "bases".

Lea resume ca en une phrase pour ses clients : "propre, coherent, utilisable". Max le vit autrement : "je retrouve mon bouton devis sur telephone". Sam le dit a ses eleves : "si tu expliques ta page a voix haute avec les balises, tu as gagne".

## Structure et cascade

Le HTML semantique nomme les pieces : `header`, `nav`, `main`, `article`, `section`, `footer`, parfois `aside`. Les `div` restent pour le layout neutre. Un `main`, un `h1` fort. Sans ca, ta page est un tas de boites anonymes - le navigateur et les lecteurs d'ecran galerent, et toi aussi dans six mois.

A poids egal, la derniere regle gagne. Les classes pesent plus que les types. Les ID pesent encore plus : evite-les pour le style quotidien. `!important` presque jamais. L'inspecteur montre qui gagne. Quand une couleur "ne change pas", ce n'est pas de la magie noire : c'est de la specificite. Relis le chapitre 3 si besoin, mais garde le reflexe inspecteur.

## Variables, Grid, Flex

`:root` pour la palette et les rythmes (`--couleur-principale`, `--espace`, `--rayon`...). `var(--nom)` partout. Une variable peut se redefinir localement dans un bloc. Changer le theme, c'est d'abord changer le `:root`. Lea ne chasse plus les hex dans cinquante classes : elle touche trois variables et la marque bascule.

Grid : `display: grid`, `grid-template-columns`, `gap`, `repeat`, `minmax` / `auto-fit` pour des galeries. `grid-template-areas` pour une page header / contenu / aside / pied. Placement simple avec `grid-column` si besoin. Flex : une dimension - menus, barres, alignements. Grid : deux dimensions - plan de page, damier. Souvent Grid dehors, Flex dedans. Un mode par conteneur. Ce n'est pas une guerre de camps : c'est une boite a outils.

:::retenir
Sens (HTML), marque (`:root`), plan (Grid/Flex), detail utile, puis verification (a11y, Tab). Les mots aident. Les pages livrees prouvent.
:::

## Images, formulaires, mouvement, accessibilite

Images : `max-width: 100%` + `height: auto`. `object-fit: cover` pour des cadres. `alt` utile. Poids du fichier soigne. `srcset` comme idee pour servir la bonne largeur. Formulaires : labels visibles relies, champs en pleine largeur dans un conteneur borne, focus clair, bouton de marque. Deux colonnes en Grid sur desktop si utile, une sur mobile.

Mouvement : transitions courtes sur l'etat de base, hover doux, `prefers-reduced-motion` respecte. Pas de cirque. Accessibilite : focus visible, contrastes, labels, ordre Tab logique. Voile sombre si texte sur photo. Tester au clavier. Ce n'est pas un chapitre "en plus" : c'est la qualite de la page pour de vrai monde.

## Ce que ce n'est pas

Ce n'est pas une liste a recracher au quiz sans avoir code. Ce n'est pas non plus "je connais les mots donc je sais faire une page pro". Le mini-projet vise une home responsive qui assemble variables + Grid + semantique + formulaire + transitions legeres. Les ateliers qui suivent font faire. Dark mode, perf et debug solidifient.

:::attention
Sauter directement aux ateliers sans ce recap, puis melanger trois approches de layout "parce que ca marchait sur Stack Overflow", c'est le piege. Les reflexes restent quand le framework change. Ici, HTML et CSS nus.
:::

## Petite histoire

Lea a refait une landing client en une soiree en suivant exactement cette checklist. Elle a trouve trois verts differents, un `div` menu, une image a 2 Mo, et zero focus. En deux heures, variables, semantique, Grid, image recompressee, outline de focus. Le client a dit "ca fait plus cher". C'etait juste plus propre. Max a demande a son neveu la meme checklist sur sa page artisan : le devis mobile a cesse de debord. Sam a transforme la checklist en oral de cinq minutes en classe. Ca marche.

## Erreur classique

Croire qu'un framework remplacera ces reflexes. Ou sauter le recap et tout melanger ensuite. Ou confondre "je connais les mots" et "je sais livrer".

## En vrai

Sans regarder tes notes, ouvre une page que tu as codee cette semaine. Coche mentalement : semantique, cascade comprise, variables, Grid ou Flex choisi, images, formulaire, transitions, a11y. Note les trous. Les ateliers sont la pour les boucher. Chronometre cinq minutes. Pas plus. La carte doit tenir sans roman.

## A toi

Ecris dix lignes : cinq choses que tu sais faire maintenant, cinq pieges que tu veux eviter. Garde ce papier a cote des ateliers. Chez DanielCraft, ce bout de papier vaut plus qu'un screenshot de quiz reussi. Bonus : montre-le a un ami et demande ce qui manque pour "oser envoyer la page".
