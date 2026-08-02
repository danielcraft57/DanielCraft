# Chapitre 7 - Features : ce que le modele "voit"

Les **features** sont les caracteristiques en entree. Le modele ne voit pas "un client". Il voit des nombres, des categories encodees, des indicateurs. Si tu lui donnes de mauvaises features, le plus bel algorithme restera myope. A l'inverse, de bonnes features avec un modele simple battent souvent un modele complexe sur des entrees pauvres.

:::retenir
Le modele ne voit que tes features. Qualite et disponibilite a l'instant T battent la complexite de l'algo.
:::

## Types courants

Numeriques (age, montant). Categoriques (pays, categorie produit). Boolennes (deja client). Temporelles (jour de la semaine, mois - attention aux fuites). Texte (qui demande un travail de transformation). Issues de calcul (ratio panier / moyenne historique). Chez DanielCraft, on encourage a ecrire la liste des features comme un contrat : nom, definition, comment calculee, disponible au moment de la prediction ?

## Disponible au bon moment

Si tu predit un retour au moment de l'achat, tu n'as pas le droit d'utiliser "a contacte le support 3 jours apres". Ca n'existe pas encore. Cette **fuite** temporelle rend les scores magnifiques en labo et nuls en vrai. Pose toujours la question : est-ce que j'aurai cette info a l'instant T ou je predit ?

:::attention
Toute info connue seulement apres la prediction est interdite. Sinon ton score labo ment.
:::

## Nettoyage et preparation

Valeurs manquantes : imputer, signaler, ou exclure selon le cas. Unites coherentes. Outliers inspectes. Categories rares regroupees. Texte normalise si besoin. Scaling pour certains modeles (pas toujours pour les arbres). Le **pipeline** (chapitre dedie) industrialise ces gestes pour ne pas tricher entre train et test.

## Feature engineering

C'est l'art de creer des variables utiles : jour ferie oui/non, distance a un entrepot, prix relatif a la categorie, nombre d'achats 90 derniers jours. Ca demande du sens metier. Noe sait que les retours explosent sur une taille de textile ; une feature "categorie = textile" + "taille commandee vs taille habituelle" peut valoir mieux qu'un reseau de neurones mal nourri.

:::astuce
Noe cree "delai promis - delai median historique" plutot que le seul delai brut. Une feature relative bat souvent une colonne brute.
:::

## Erreur classique

Tout garder "au cas ou" (bruit, fuites, colonnes identifiantes). Ou tout jeter trop vite. Autre piege : encoder mal une categorique ordinaire comme un nombre (Paris=1, Lyon=2, Marseille=3) et laisser un modele lineaire croire a un ordre absurde.

## A toi

Pour ton sujet, liste 8 features candidates. Barre celles indisponibles a l'instant de prediction. Il reste quoi ?

## Documentation des features

Nom, definition, formule, source, fraicheur, dispo a T, valeurs manquantes possibles, exemples. Une page tableur suffit au debut. Quand le projet grossit, cette page evite les conflits ("moi je croyais que montant = TTC"). Chez DanielCraft, on dit qu'une feature non documentee est une dette.

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
