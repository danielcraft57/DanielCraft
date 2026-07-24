# Chapitre 2 - Un neurone : une petite decision ponderee

Un neurone artificiel, en version poche, prend des entrees numeriques, les multiplie par des poids, ajoute un biais, puis passe le resultat dans une fonction d'activation. Image : une recette qui melange des ingredients avec des dosages (poids), puis decide si le signal continue.

## Pourquoi des poids ?

Les poids s'ajustent pendant l'apprentissage. Si telle entree est importante pour la tache, son poids grossit (en valeur absolue). Si elle est inutile, elle s'attenue. Tu n'ecris pas la regle a la main ; tu laisses les exemples pousser les dosages.

## Limite d'un seul neurone

Un neurone seul est faible : il trace des frontieres simples. La puissance vient des reseaux : beaucoup de neurones organises en couches, qui composent des decisions. Comme une equipe : chacun voit un aspect ; ensemble ils resolvent un motif complexe.

## Lien humain (et ses limites)

Le nom "neurone" s'inspire du cerveau, mais ce n'est pas une copie fidele. C'est une metaphore ingenierie utile. N'en deduis pas qu'un reseau "pense" ou "sent". Il calcule une fonction tres flexible ajustee sur des donnees.

## Erreur classique

Imaginer un neurone unique qui "contient" le concept chat. Les concepts emergent souvent de patterns distribues dans beaucoup d'unites. Autre piege : fixer les poids a la main "logiquement" - l'apprentissage le fait mieux sur des taches complexes, a condition d'avoir des donnees.

## A toi

Invente 3 entrees pour predire "prendre un parapluie" (meteo, vent, distance). Imagine des poids. Ou ton intuition est-elle deja un mini-neurone ?
## Parametres et capacite

Chaque poids est un parametre. Plus tu en as, plus le reseau peut coller a des motifs complexes - et au bruit. La capacite n'est pas un trophée. C'est un budget a depenser avec des donnees et de la regularisation. Un neurone unique a peu de capacite ; un LLM en a une immense.

## Developpement : ce que le deep learning change vraiment

Le deep learning a deplace le curseur : des taches autrefois impossibles sans features handicraftées deviennent abordables si tu as des donnees et du calcul. Images, parole, langue. Mais il n'a pas aboli les fondamentaux : split honnete, metriques alignees, biais, monitoring, abstention. Il les a rendus plus urgents, parce que les systemes sont plus opaques et plus couts.

Quand tu entends "on a mis du deep learning", pose les questions de ce livre : combien de donnees ? preentraine ou from scratch ? quelle validation ? quel GPU / quel budget ? quel comportement hors distribution ? quel plan si le modele se trompe ? Tu passeras pour quelqu'un de serieux. C'est voulu.

## Intuition des representations

Une bonne representation rend le probleme plus simple pour la couche suivante. Au debut du reseau, l'entree est brute (pixels, tokens). Au milieu, des motifs. A la fin, une decision. Transfer learning = reutiliser un milieu deja riche. RAG cote LLM = injecter des faits dans le contexte plutot que de tout stocker dans les poids. Prompting = conditionner la representation de sortie sans maj de poids. Ces leviers sont differents, mais ils parlent le meme langage : influencer ce que le systeme "voit" avant de decider.

## Experimentation sobre

Change une chose a la fois. Logge. Compare a une baseline. Arrete-toi quand la validation stagne. Ne confonds pas agitation et progres. Un entrainement qui fait baisser la loss train sans ameliorer la val n'est pas un succes. Un petit modele qui generalise un peu est parfois preferable a un grand modele qui memorise.

## Ethique et impact

Derriere les perfs : energie, annotation, risques de surveillance, deepfakes, automatisation de decisions sensibles. Ce livre introductif ne tranche pas tous les debats. Il exige que tu les voies. Utiliser un outil puissant sans regarder ses effets collateraux, ce n'est pas de la neutralite technique. C'est une decision. Assume-la.

## Pour aller plus loin sans te perdre

Tu n'as pas a tout maitriser d'un coup. Reviens a ce chapitre quand tu butes sur un cas reel. Relis l'erreur classique. Refais le "A toi". Chez DanielCraft, on prefere trois relectures actives a une lecture passive de vingt pages. Si un paragraphe te semble encore flou, reformule-le a voix haute avec ton propre exemple. Des que ca passe a l'oral, c'est que c'est entre. Ensuite seulement, passe au chapitre suivant. Cette discipline lente cree une competence rapide sur la duree - le contraire du binge de tutos oublies le lendemain.
