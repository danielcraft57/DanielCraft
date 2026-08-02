# Chapitre 1 - Salut, c'est quoi le machine learning ?

Le **machine learning**, c'est l'art d'apprendre a une machine a partir d'exemples, au lieu d'ecrire a la main toutes les regles. Tu montres des cas. Le modele ajuste ses parametres. Ensuite, face a un cas nouveau, il predit, classe, regroupe, ou estime un nombre. Ce n'est pas de la magie. Ce n'est pas non plus "l'IA qui ecrit des romans". C'est souvent plus discret, et partout : spam, recommandations, detection de fraude, prevision de demande, diagnostic assiste, tri de photos.

Chez DanielCraft, on aime partir d'une image simple. Imagine que tu veux savoir si un mail est indesirable. Au lieu d'ecrire mille regles ("si le mot viagra alors spam"), tu montres des milliers de mails deja labels "spam" ou "pas spam". Le modele cherche des motifs. Puis il score de nouveaux mails. Il se trompera parfois. Ton travail, c'est de mesurer ces erreurs, de choisir les bons exemples, et de savoir quand ne pas faire confiance.

:::retenir
Le machine learning apprend sur des exemples. Il predit, il ne "comprend" pas comme toi.
:::

## Ce que ce livre va faire

Tu vas comprendre l'apprentissage **supervise** et non supervise, la regression, la classification, les arbres de decision, le decoupage **train/test**, l'**overfitting**, les **features**, les metriques, l'idee de pipeline, les biais dans les donnees, et l'esprit de scikit-learn sans jargon opaque. Puis un recap, des ateliers, des bonnes pratiques, un quiz, un bravo. Niveau debutant curieux. Pas besoin d'etre data scientist. Besoin d'aimer les exemples concrets.

## Machine learning vs IA generative

Un LLM genere du texte. Un modele de machine learning "classique" repond souvent a une question etroite : quel prix ? quelle classe ? quel cluster ? Les deux existent en 2026. Ce livre se concentre sur le second, parce que beaucoup de decisions metier reposent encore la-dessus, et parce que comprendre ca t'aide aussi a demystifier l'IA en general.

:::astuce
Avant de lire plus loin, note une prediction utile dans ton metier (un nombre ou une classe). Tu t'en serviras comme fil rouge.
:::

## Fil rouge

On suivra Noe, qui tient une petite boutique en ligne d'equipement sportif. Il veut predire si une commande risque un retour, estimer un volume de ventes, et regrouper ses clients par comportements. Il n'a pas une equipe data. Il a un tableur, un peu de Python plus tard, et surtout besoin d'idees justes. Toi aussi, tu pourras substituer ton contexte.

## Erreur classique

Croire que "plus de donnees = automatiquement mieux" sans regarder la qualite. Ou croire qu'un score eleve sur les donnees d'entrainement prouve que le modele est bon. Spoiler du chapitre overfitting : non.

:::attention
Un score brillant sur l'entrainement ne prouve rien. Ce qui compte, c'est le comportement sur des cas nouveaux.
:::

## A toi

Ecris une prediction utile dans ton monde (nombre ou classe). Note quelles donnees tu aurais, et ce qui se passerait si le modele se trompe. Garde ce papier.

## Ou le ML se cache dans ta vie

Ton streaming te propose une serie : un modele a estime une preference. Ta banque bloque une carte : un score d'anomalie a clignote. Ton app photo regroupe des visages : un regroupement / reconnaissance. Ton outil mail range des pourriels : une classification. Rarement tu vois le mot "machine learning" sur le bouton. Souvent tu vois juste un comportement. Ce livre te rend capable de reconnaitre la logique derriere le comportement, et surtout de la construire proprement quand tu en as besoin.

## Ce que "apprendre" veut dire ici

Apprendre, ce n'est pas memoriser une lecon scolaire. C'est ajuster des parametres pour reduire une erreur moyenne sur des exemples, puis esperer que ca tienne sur des exemples nouveaux. Cette esperance n'est pas automatique. Elle se merite par la qualite des donnees, le split, les metriques, et l'humilite face au deploiement. Chez DanielCraft, on celebre les projets qui battent une baseline honnete, pas ceux qui affichent 99,9 % sans contexte.

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
