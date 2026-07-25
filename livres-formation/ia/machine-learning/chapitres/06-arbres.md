# Chapitre 6 - Arbres de decision : des questions en cascade

Un **arbre de decision**, c'est un enchainement de questions simples sur les **features**, jusqu'a une feuille qui donne une prediction. Exemple : montant > 100 ? oui -> client deja revenu ? non -> risque de retour eleve. C'est lisible. Ca plait aux metiers. Ca capture des interactions (tel effet seulement si telle condition).

:::retenir
Un arbre pose des questions en cascade. Lisible pour le metier, fragile s'il devient trop profond.
:::

## Pourquoi c'est pedagogique

Tu peux montrer l'arbre a Noe et il comprend sans equation. Tu vois ou le modele coupe. Tu detectes des regles absurdes ("si code postal = 99999 alors ...") qui revelent un souci de donnees. Pour enseigner le machine learning, les arbres sont un pont en or entre intuition et pratique.

## Limites d'un arbre seul

Un arbre profond colle trop aux donnees d'entrainement (**overfitting**). Un arbre trop petit sous-apprend. Les frontieres sont souvent paralleles aux axes (questions du type feature > seuil), ce qui peut etre maladroit pour certaines formes. La solution courante : des ensembles d'arbres (**forets**, boosting). L'idee : plusieurs arbres votent ou se corrigent, plus robustes, un peu moins lisibles.

:::attention
Un arbre geant n'est pas un trophee. C'est souvent un drapeau rouge d'overfitting. Limite la profondeur et verifie sur **test**.
:::

## Regles de bonne vie

Commence par un arbre peu profond pour explorer. Controle la profondeur. Verifie sur test. Regarde l'importance des features (quelles questions servent souvent). Ne prends pas une importance comme une preuve causale : "associe a" n'est pas "cause".

:::astuce
Interdis les IDs uniques (numero de commande, email) comme features. L'arbre s'en sert comme antiseche, puis echoue en production.
:::

## Erreur classique

Montrer un arbre geant comme preuve de sophistication. Un arbre geant est souvent un drapeau rouge d'overfitting. Autre piege : laisser des IDs uniques (numero de commande) comme feature : l'arbre s'en sert comme antiseche, puis echoue en production.

## A toi

Sans code, ecris un mini-arbre a 3 questions pour une decision de ton quotidien pro. Est-il juste ? Ou revele-t-il un biais ?

## Forets et boosting (apercu)

Une **foret aleatoire** : beaucoup d'arbres, chacun voit un sous-ensemble, vote. Plus robuste, moins interpretable qu'un seul arbre. Le boosting : des arbres qui corrigent les erreurs les uns des autres, souvent tres performants sur tableaux. Tu peux les utiliser plus tard ; comprends d'abord un arbre seul pour garder l'intuition.

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
