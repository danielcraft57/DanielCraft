# Chapitre 4 - Regression : predire un nombre

La regression vise a predire une valeur numerique. Prix, duree, temperature, nombre de visites, panier moyen. L'image mentale la plus simple : une courbe (souvent une droite au debut) qui relie des X a un y. Tu ajustes la courbe pour qu'elle passe "au mieux" pres des points d'entrainement, puis tu lis la prediction pour un nouveau X.

## Regression lineaire : l'intuition

Imagine predire le loyer a partir de la surface. En gros, loyer ≈ a * surface + b. Le modele cherche a et b qui minimisent une erreur (souvent la distance verticale aux points). Ce n'est pas toujours realiste (les relations sont courbes, il y a d'autres facteurs), mais c'est un excellent premier modele : simple, interpretable, rapide a diagnostiquer.

## Au-dela de la droite

Tu peux ajouter des features (quartier, etage, presence d'ascenseur). Tu peux transformer (log du prix). Tu peux utiliser des modeles plus souples (arbres, forets). La regle DanielCraft : commence simple, mesure, complexifie seulement si le gain est reel sur le jeu de test et en conditions proches du deploiement.

## Erreurs et unites

Une erreur de 50 euros sur un loyer a 500 euros n'est pas la meme chose qu'une erreur de 50 euros sur un loyer a 3 000 euros. D'ou l'importance des metriques (chapitre dedie) et du sens metier. Noe qui predit des ventes veut savoir s'il se trompe de 5 unites ou de 500 - ca change les commandes fournisseurs.

## Pieges

Fuites de donnees (utiliser une info du futur). Outliers qui tirent la droite. Relations non lineaires ignorees. Croire que R2 eleve sur train suffit. Predire un nombre puis le traiter comme une certitude dans une decision automatique sans marge.

## Erreur classique

Extrapolateur fou : entrainer sur des surfaces de 20 a 80 m2 puis predire pour 300 m2 comme si la droite restait valable. Les modeles sont souvent locaux a la zone vue.

## A toi

Choisis une cible numerique. Dessine a la main une relation simple avec une feature. Ou croit-elle ? Ou casse-t-elle ?
## Interpretable d'abord

Une regression lineaire bien faite te dit : "toutes choses egales par ailleurs dans le modele, +10 m2, +X euros". Attention au piege causal : ce n'est pas une preuve que agrandir cree le loyer. Mais pour diagnostiquer et communiquer, c'est precieux. Les modeles boites noires viendront plus tard, si le gain le justifie.

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
