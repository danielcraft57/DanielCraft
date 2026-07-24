# Chapitre 13 - A retenir

Deep learning = reseaux a plusieurs couches. Neurone = melange pondere + activation. Couches = transformations empilees. Activation = non-linearite. Backprop = ajuster les poids via l'erreur. CNN = filtres locaux pour l'image. RNN = memoire sequentielle (overview historique utile). Transformers = attention, coeur des LLM. Overfitting = capacite vs donnees. GPU = parallelisme pour matrices. Transfer learning = reutiliser un modele fondation. LLM = deep learning langage + alignement + usage (prompt/RAG/agents).

## Boucle DanielCraft DL

Tache claire -> assez de donnees / transfert -> architecture adaptee -> loss et metriques -> validation -> regularisation -> deploiement mesure -> surveillance. Prefere reutiliser avant de reentrainer le monde.

## A toi

Carte mentale une page, TES mots, un exemple vision et un exemple texte.
## Pont vers la pratique

Si tu utilises deja ChatGPT : tu manipules un transformer aligne. Si tu classes des images : tu toucheras CNN/transfer. Si tu as un CSV : reviens au livre ML. La bonne stack est celle qui matche le probleme.

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
