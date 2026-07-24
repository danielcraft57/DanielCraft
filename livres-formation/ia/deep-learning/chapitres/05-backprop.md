# Chapitre 5 - Backpropagation : l'idee simple de l'apprentissage

La backpropagation (retour d'erreur), c'est la methode pour ajuster les poids apres avoir vu une erreur. Version histoire : le reseau fait une prediction (avant). On compare a la cible avec une fonction de perte. Puis on propage en arriere de petites indications : "toi, poids, monte un peu ; toi, descends". On repete sur beaucoup d'exemples (souvent par petits lots, mini-batches).

## Descente de gradient (intuition)

Imagine etre dans le brouillard sur une colline et vouloir descendre : tu sens la pente sous tes pieds et tu fais un pas dans la direction qui descend. Le gradient est cette pente dans l'espace des poids. Le taux d'apprentissage (learning rate) est la taille du pas. Trop grand : tu sautes et tu diverges. Trop petit : tu rampe eternelle.

## Ce que tu retiens sans maths

Apprendre = reduire une erreur mesuree en ajustant des millions (parfois milliards) de poids via des passes avant/arriere. Les frameworks (PyTorch, TensorFlow...) calculent les gradients pour toi. Ton job : donnees, architecture raisonnable, loss adaptee, monitoring, regularisation.

## Epochs, batches

Une epoch : un passage sur l'ensemble d'entrainement. Un batch : un sous-groupe d'exemples pour une mise a jour. Ces details changent stabilite et vitesse. En pratique, tu observes la courbe de loss train/validation.

## Erreur classique

Croire que backprop "comprend" le sens. Elle optimise un critere. Si le criter est mal choisi, elle optimise mal. Autre piege : juger un entrainement seulement sur la loss train.

## A toi

Raconte la boucle en 6 etapes orales : batch, avant, loss, arriere, maj des poids, repeter. Si tu peux sans notes, c'est gagne.
## Optimizers (apercu)

SGD, Adam et cousins : des facons d'utiliser les gradients pour mettre a jour les poids, avec des astuces de moment et d'adaptation du pas. Tu n'as pas a les reinventer. Sache qu'ils existent, qu'ils ont des reglages, et que le learning rate reste souvent le levier le plus sensible.

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
