# Chapitre 3 - Apprentissage non supervise : trouver des structures sans label

Parfois, tu n'as pas de bonne reponse y. Tu as seulement des descriptions de clients, de produits, de comportements. L'apprentissage **non supervise** cherche des structures : des groupes (**clustering**), des reductions de dimensions, des motifs inhabituels. Personne n'a dit "voici la verite" ; le modele propose une organisation. A toi de juger si elle est utile.

:::retenir
Sans label, on organise. Avec label, on predit une cible. Ne confonds pas les deux outils.
:::

## Clustering : regrouper

L'idee : mettre ensemble ce qui se ressemble selon certaines mesures. Noe peut regrouper ses clients en "acheteurs occasionnels petit panier", "fideles gros panier", "chasseurs de promo". Ces noms, c'est lui qui les donne apres coup. L'algorithme sort des groupes chiffres ; l'humain interprete. Si l'interpretation est forcee, le clustering devient de la science fiction marketing.

## Quand s'en servir

Explorer. Segmenter pour adapter un message. Detecter des anomalies (un point tres loin des autres). Reduire la complexite avant une autre etape. Ce n'est generalement pas le meilleur outil si tu as deja un **label** clair et une decision binaire a prendre - dans ce cas, le **supervise** est plus direct.

:::astuce
Avant de fixer le nombre de clusters, demande : "quelle action change si ce groupe existe ?" Si aucune, tu explores encore.
:::

## Attention aux illusions

Les groupes dependent des **features** choisies et de l'echelle des variables. Si tu melanges "age" et "revenu annuel" sans normaliser, une variable ecrase l'autre. Si tu demandes 8 clusters parce que "ca fait joli", tu obtiendras 8 clusters meme si 3 suffisaient. Le non supervise demande de la sobriete et de la validation metier : est-ce que ces groupes changent une action ?

:::attention
Normalise (ou standardise) avant de clusterer des variables d'echelles differentes. Sinon une seule colonne dicte les groupes.
:::

## Lien avec le reste de l'IA

Les **embeddings** (representations vectorielles) utilises autour des LLM sont cousins de cette logique : mettre proche ce qui "se ressemble" dans un espace. Tu n'as pas besoin des maths ici. Retiens l'intuition : sans label, on organise ; avec label, on predit une cible.

## Erreur classique

Prendre les clusters comme une verite sociologique. Ou les vendre a un client comme "preuves scientifiques" sans test terrain. Autre piege : oublier la saisonnalite (un cluster "inactif" en aout n'est pas un cluster "perdu").

## A toi

Liste 10 entites de ton monde (clients, tickets, articles). Quelles features utiliserais-tu pour les regrouper ? Quelle decision changerait si les groupes etaient bons ?

## Valider un clustering sans label magique

Tu peux regarder la stabilite (est-ce que les groupes bougent beaucoup si tu reechantillonnes ?). Tu peux demander a un expert metier si les groupes suggerent des actions differentes. Tu peux mesurer un indicateur externe (taux de reponse a une campagne par cluster). Sans au moins une de ces validations, le clustering reste une jolie projection, pas une decision.

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
