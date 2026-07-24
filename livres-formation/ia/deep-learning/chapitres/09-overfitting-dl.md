# Chapitre 9 - Overfitting en deep learning

Les reseaux ont souvent des millions ou des milliards de parametres. Capacite enorme = facilite a coller au train. L'overfitting est donc central. Signes : accuracy train haute, validation basse ; ecarts qui se creusent au fil des epochs ; performances magiques sur un petit jeu.

## Remedes courants

Plus de donnees reelles. Data augmentation (surtout vision). Dropout (eteindre des neurones au hasard pendant l'entrainement). Weight decay / regularisation. Early stopping (arreter quand la validation n'ameliore plus). Architectures plus petites. Transfer learning plutot que from scratch. Label smoothing parfois. Et toujours : protocole de validation honnete.

## Generalisation dans le vrai monde

Meme avec une belle courbe, le deploiement peut casser si les photos changent (eclairage, telephone), si la langue change, si les utilisateurs detournent. Surveille. Recolte des cas d'echec. Reentraine. Le deep learning n'annule pas la boucle ML : il l'intensifie.

## Erreur classique

Augmenter la taille du modele des que ca coince. Parfois il faut mieux de donnees, pas plus de couches. Autre piege : data augmentation absurde qui cree des exemples impossibles et trompe le metier.

## A toi

Liste 4 remedes anti-overfitting applicables a ton idee de projet. Lesquels sont realistes cette semaine ?
## Courbes a surveiller

Loss train, loss val, metrique metier val. Si train plonge et val remonte : stop / regularise. Si les deux restent hauts : underfitting ou donnees insuffisantes / mal alignees. Apprends a lire ces courbes comme un medecin lit une tension.

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
