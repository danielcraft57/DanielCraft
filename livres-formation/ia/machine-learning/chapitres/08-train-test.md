# Chapitre 8 - Train / test : apprendre sans se mentir

Si tu evalues un modele sur les memes exemples que ceux qui ont servi a l'entrainer, tu te mentiras presque toujours : le modele a pu "retenir" au lieu de generaliser. D'ou le geste sacre : separer les donnees. Train pour apprendre. Test pour juger, une fois, proprement. Parfois un jeu de validation pour choisir des reglages, puis un test final touche rarement.

## Comment separer

Aleatoire quand les lignes sont independantes. Temporelle quand le temps compte (entraine sur le passe, teste sur le futur) - souvent plus realiste pour Noe et les ventes. Par groupe (par client) si plusieurs lignes appartiennent a la meme entite et que tu ne veux pas de fuite. Le pourcentage classique 80/20 n'est qu'une habitude ; l'important est le protocole honnete.

## Validation croisee (idee)

Quand tu as peu de donnees, tu peux tourner plusieurs decoupes (cross-validation) et moyenner les scores. Ca stabilise l'estimation. Ca ne remplace pas un vrai test sur des donnees plus recentes si ton monde change.

## Fuite (data leakage)

Toute information du test qui contamine le train ou le preprocessing fait exploser les scores artificiellement. Exemples : normaliser sur tout le dataset avant split ; choisir les features en regardant le test ; inclure la cible deguisee. Le pipeline doit ajuster ses transformations sur le train uniquement, puis les appliquer au test.

## Ritual DanielCraft

1) Definir la question et le moment de prediction. 2) Split honnete. 3) Baseline stupide (toujours predire la moyenne / la classe majoritaire). 4) Modele simple. 5) Comparer au baseline sur test. Si tu ne bats pas le baseline, tu n'as pas encore de victoire.

## Erreur classique

Retoucher le modele jusqu'a ce que le score test soit parfait... en regardant le test cinquante fois. Tu as transforme le test en train mental. Garde un jeu final rare, ou accepte une validation croisee declaree.

## A toi

Decris ton split : methode (aleatoire / temps / groupe), proportions, baseline stupide. Ecris pourquoi ce split evite (ou non) la fuite.
## Simulation de production

Le meilleur test ressemble au futur : memes sources, memes delais, memes manquants. Si en labo tu as des champs complets et en prod la moitie manquent, ton score labo ment. Construis un jeu qui imite la prod, meme plus petit.

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
