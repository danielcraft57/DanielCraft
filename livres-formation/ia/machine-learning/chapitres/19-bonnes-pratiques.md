# Chapitre 19 - Bonnes pratiques ML

## Avant de coder

Clarifier la decision metier. Definir y. Definir l'instant de prediction. Estimer le cout des erreurs. Verifier qu'on a (ou peut avoir) des labels. Preferer un projet petit qui decide vraiment a un modele "interessant" qui ne change rien.

## Pendant

Split honnete. Baseline. Modele simple. Pipeline. Metriques alignees. Inspection des erreurs. Features disponibles. Mesure par sous-groupes. Journaliser les experiences (ce que tu as essaye, scores, conclusions).

## Apres

Sauvegarder artefacts + definitions. Monitoring. Plan de reentrainement. Point humain sur decisions a fort impact. Communication claire des limites aux utilisateurs du score.

## Culture

Celebrer les baselines battues honnetement, pas les scores magiques. Preferer la clarte a la magie. Dire "je ne sais pas encore" quand le signal est faible.

## A toi

Transforme cette page en checklist murale de 12 cases. Coche a chaque projet.
## Ritual de fin de sprint

Une heure : relire les erreurs, mettre a jour la doc features, verifier le monitoring, supprimer une experience morte, ecrire ce qu'on ne tentera plus. Les projets ML meurent souvent d'accumulation, pas de manque d'idees.

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
