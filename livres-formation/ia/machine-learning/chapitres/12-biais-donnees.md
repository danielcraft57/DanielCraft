# Chapitre 12 - Biais dans les donnees : le modele herite

Un modele supervise apprend ce que tu lui montres. Si tes exemples sous-representent une population, si tes labels portent un prejudice historique, si tes mesures sont biaisées, le modele industrialise le probleme - souvent plus vite et a plus grande echelle. Ce n'est pas "la faute de l'algorithme" comme creature malveillante. C'est un miroir statistique + une decision de deploiement.

## Types de biais utiles a connaitre

Biais de selection : tu n'observes que ceux qui sont entres dans ton systeme. Biais de label : les annotateurs (ou l'historique) favorisent une classe. Biais de mesure : un capteur ou un process sous-estime un groupe. Biais de feedback : le modele influence le monde, qui renvoie des donnees qui confirment le modele. Chez DanielCraft, on demande toujours : qui manque dans le jeu ? Qui a labellise ? Qui paie l'erreur ?

## Exemple Noe

Si Noe n'a historique que sur des clients urbains aises et deploie un score de retour partout, il peut mal traiter d'autres segments. Si les retours textiles sont sur-labels "abusifs" a cause d'un a priori d'equipe, le classifieur apprend l'a priori. Corriger, ce n'est pas seulement "ajouter de l'ethique en slide" : c'est revoir labels, echantillonnage, metriques par segment, et parfois refuser d'automatiser.

## Que faire concrètement

Mesurer les performances par sous-groupes pertinents. Inspecter les erreurs. Interroger la representativite. Documenter les limites. Garder un humain sur les decisions a fort impact. Eviter les proxies dangereux (utiliser un code postal pour estimer "fiabilite" de facon opaque). Preferer la transparence a la magie.

## Lien legal et moral

Selon le domaine (credit, emploi, sante...), des cadres existent. Ce livre ne remplace pas un conseil juridique. Il pose le reflexe : un beau score global ne lave pas une injustice locale. Si tu deploies, assume.

## Erreur classique

Croire que retirer une variable sensible (genre, origine) suffit toujours : d'autres features la reconstruisent. Ou croire que "c'est des maths donc neutre". Les maths operent sur un monde deja charge.

## A toi

Pour ton projet, nomme un sous-groupe qui pourrait etre mal servi. Quelle metrique regarderas-tu separement ?
## Processus de revue

Avant deploiement a impact : qui est affecte ? Quelles metriques par groupe ? Quel recours humain ? Quelle doc des limites ? Qui signe le go ? Ce n'est pas de la paperasse gratuite. C'est ce qui distingue un prototype jouet d'un systeme responsable.

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
