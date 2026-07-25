# Chapitre 16 - Atelier : classification et cout des erreurs

Objectif : concevoir un classifieur en pensant **faux positifs** / **faux negatifs**. Duree : 45 minutes. Ici, le score n'est pas le heros. Le heros, c'est le cout : qui souffre si tu te trompes d'un cote, qui souffre de l'autre.

Prends un cas binaire de ton monde (retour oui/non, fraude, ticket urgent...). Ecris les couts avant de toucher a un modele. Ensuite seulement, choisis un **seuil**, une **metrique**, et des **features** sans fuite. Tu sortiras avec une fiche de decision, pas avec un chiffre orphelin.

:::retenir
Le seuil suit les couts. L'accuracy globale ne decide rien seule sur une classe rare.
:::

## Etapes

1) Choisis une cible binaire. 2) Ecris le cout d'un faux positif et d'un faux negatif. 3) Propose un seuil de decision (haut/bas) aligne a ces couts. 4) Dessine une **matrice de confusion** vide et imagine des effectifs. 5) Choisis precision ou rappel comme metrique principale + une de garde-fou. 6) Liste 5 features sans fuite temporelle. 7) Decris une **baseline** (classe majoritaire). 8) Option code : arbre peu profond + matrice de confusion.

## Livrable

Fiche "decision classification" avec couts, seuil, metriques, features, plan d'inspection des erreurs (regarder 20 cas).

## Piege a eviter

Optimiser l'**accuracy** globale alors que la classe rare est la seule qui compte.

:::attention
Si ta classe positive fait 5 %, un modele "toujours negatif" a 95 % d'accuracy et zero utilite. Regarde la detection de la classe rare.
:::

## Prolongement

Fais varier le seuil (bas / milieu / haut) et raconte pour chaque seuil qui gagne et qui perd. Choisis explicitement. Documente.

Quand tu as choisi, explique ton choix a voix haute comme si Noe te demandait pourquoi. Si tu bloques sur "parce que le score est mieux", recommence : le score doit servir une decision, pas l'inverse.

## Developpement : penser comme un artisan des modeles

Le machine learning n'est pas un distributeur de verite. C'est un artisanat de decisions sous incertitude. Tu choisis une question, tu rassembles des exemples, tu acceptes une erreur moyenne, tu te donnes les moyens de la mesurer, tu decides si cette erreur est tolerable pour le cas d'usage. Beaucoup de frustration vient d'attendre la perfection la ou il fallait un score utile avec un humain dans la boucle.

Quand Noe predit un risque de retour, il ne remplace pas le service client. Il priorise. Quand un hopital utilise un score (hors du perimetre de ce livre introductif, et avec des cadres stricts), l'enjeu n'est plus le meme : les couts d'erreur explosent, les biais deviennent critiques, la gouvernance monte. Adapte toujours la profondeur de ta demarche a l'impact. Un modele jouet sur un CSV public n'exige pas la meme revue qu'un score qui bloque un credit.

## Donnees : le personnage principal

Les algorithmes changent. Les principes de donnees restent : definition claire, representativite, fraicheur, droits, documentation, absence de fuite, inspection des cas bizarres. Passe plus de temps sur les donnees que sur le shopping d'algorithmes. C'est le conseil le moins glamour et le plus rentable du livre. Un arbre simple sur des features excellentes bat une usine a gaz sur un tableau sale.

## Mise en production (apercu)

Un notebook n'est pas un produit. En production, tu dois gerer des entrees manquantes nouvelles, des categories inconnues, des delais, des journaux, des versions, des rollback, des alertes si la metrique chute. Tu n'as pas a tout construire aujourd'hui. Tu dois savoir que ca existe, pour ne pas crier victoire trop tot apres un score de validation. Prevour des le jour 1 un chemin "humain si doute".

## Culture et communication

Apprends a dire "non" a un modele inutile. Apprends a dire "pas encore" quand les labels manquent. Apprends a dire "voici les limites" quand tu presentes un score. Cette honnetete te rend plus credible que n'importe quel jargon. Chez DanielCraft, on forme des gens capables de tenir cette conversation avec un metier, un manager, ou un client.

## Pour aller plus loin sans te perdre

Tu n'as pas a tout maitriser d'un coup. Reviens a ce chapitre quand tu butes sur un cas reel. Relis l'erreur classique. Refais le "A toi". Chez DanielCraft, on prefere trois relectures actives a une lecture passive de vingt pages. Si un paragraphe te semble encore flou, reformule-le a voix haute avec ton propre exemple. Des que ca passe a l'oral, c'est que c'est entre. Ensuite seulement, passe au chapitre suivant. Cette discipline lente cree une competence rapide sur la duree - le contraire du binge de tutos oublies le lendemain.
