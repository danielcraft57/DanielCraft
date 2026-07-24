# Chapitre 2 - Apprentissage supervise : apprendre avec les bonnes reponses

L'apprentissage supervise, c'est quand chaque exemple d'entrainement vient avec la "bonne reponse". On appelle souvent X les entrees (features) et y la cible (label). Exemple : surface et quartier (X) -> prix du loyer (y). Ou : texte du mail (X) -> spam / pas spam (y). Le modele apprend une relation. Ensuite, sur de nouveaux X, il propose un y.

Pourquoi "supervise" ? Parce que les labels jouent le role d'un superviseur : ils corrigent. Sans labels, tu ne peux pas faire de supervise classique. Or labelliser coute cher (temps humain, expertise). C'est souvent le vrai frein des projets, pas l'algorithme a la mode.

## Deux grandes familles

Si y est un nombre continu (prix, temperature, duree), on parle souvent de regression. Si y est une categorie (spam/ham, malade/sain, chat/chien, risque faible/moyen/eleve), on parle de classification. Les frontieres peuvent etre floues (une note sur 5 peut etre traitee comme nombre ou comme classes). L'important est de savoir ce que tu veux predire et comment tu mesureras l'erreur.

## Le deroulement mental

1) Collecter des exemples labels. 2) Nettoyer. 3) Separer train/test. 4) Choisir un modele simple. 5) Entrainer sur train. 6) Evaluer sur test. 7) Inspecter les erreurs. 8) Iterer sur les features et les donnees avant de complexifier le modele. Chez DanielCraft, on insiste : les donnees et la question metier d'abord, la usine a gaz algo ensuite.

## Exemple Noe

Noe labelise 2 000 commandes : retour oui/non. Features possibles : montant, categorie produit, delai de livraison promis, client deja revenu ou non, pays. Cible : retour. C'est du supervise (classification). S'il veut predire le montant du prochain panier, c'est une regression. Meme boutique, deux questions, deux cibles.

## Limites

Si tes labels sont sales (annotateurs fatigues, definitions floues), le modele apprend le flou. Si tes exemples ne representent pas le futur (tu n'as que des clients urbains et tu deploies a la campagne), le modele generalise mal. Le supervise n'est pas une garantie de justice ni de verite ; c'est une methode d'apprentissage a partir d'exemples.

## Erreur classique

Entrainer et "tester" sur les memes lignes, puis crier victoire. Ou changer la definition du label en cours de route sans le dire. Clarifie y comme tu clarifierais un cahier des charges.

## A toi

Decris un jeu supervise perso : que sont X, que sont y, qui labellise, combien d'exemples tu pourrais avoir en un mois.
## Qualite des labels

Un label flou produit un modele flou. Si deux annotateurs ne sont pas d'accord sur "retour abusif" versus "retour legitime", le modele apprend le desaccord. Investis du temps dans une definition ecrite, des exemples frontieres, et parfois un double annotation sur un echantillon. C'est moins glamorous que d'essayer un nouvel algo. C'est souvent ce qui decide du succes.

## Volume : combien faut-il ?

Ca depend de la difficulte et du nombre de features. Des centaines peuvent suffire pour une separation simple. Des dizaines de milliers pour un probleme bruyant. Des millions dans certains domaines. Plutot que de mythifier un chiffre, commence petit, mesure, regarde les erreurs, decide si plus de labels changerait vraiment la donne. Parfois oui. Parfois le probleme est mal pose.

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
