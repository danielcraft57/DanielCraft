# Chapitre 19 - Erreurs JS frequentes (et comment les lire)

Le navigateur parle. Apprends a l'ecouter.

## Ouvre la console

F12 -> Console.
Rouge = probleme.
Lis la ligne. Souvent y'a un numero de ligne.

## "X is not defined"

Tu utilises une variable qui n'existe pas.
Faute de frappe classique : `scoree` au lieu de `score`.

## "Cannot read properties of null"

Ton `querySelector` a renvoye `null`.
Selecteur faux, ou script trop tot.

## "Unexpected token"

Syntaxe cassee.
Parenthese, crochet, ou guillemet non ferme.

## Boucle infinie

La page freeze.
Tu as un `while` qui ne finit jamais.
Coupe l'onglet. Corrige. Reprends.

## Methode anti-stress

1. Lis le message
2. Va a la ligne indiquee
3. `console.log` juste avant
4. Corrige le plus petit truc possible
5. Reteste

## Exercice

Casse volontairement ton compteur (renomme un id).
Lis l'erreur.
Repare.
Tu viens d'apprendre un vrai metier : comprendre les messages.
