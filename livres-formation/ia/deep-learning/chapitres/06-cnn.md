# Chapitre 6 - CNN : voir par filtres locaux

CNN signifie Convolutional Neural Network : reseau a convolutions. Idee : au lieu de relier chaque pixel a chaque neurone (trop cher, trop de parametres), on fait glisser de petits filtres qui detectent des motifs locaux (bords, textures), partages sur toute l'image. Puis on empile : motifs plus riches, cartes de features, souvent reduction spatiale, puis decision.

## Pourquoi ca marche sur l'image

Un chat peut etre a gauche ou a droite : un filtre de "oreille" utile partout grace au partage de poids. La localite (un pixel depend surtout de son voisinage) est un a priori puissant. Les CNN ont domine la vision pendant des annees ; d'autres architectures existent aussi aujourd'hui, mais l'intuition convolution reste essentielle.

## Usages

Classification d'images, detection d'objets, segmentation, controle qualite sur chaine, lecture de documents scannes (avec d'autres briques). Ines peut entrainer ou, plus souvent, reutiliser un modele preentraine (transfer learning) sur ses pieces detachees.

## Erreur classique

Entrainer un CNN profond from scratch avec 200 photos. Tu overfitteras. Prefere transfer learning + data augmentation (rotation, crop...) avec prudence. Autre piege : juger sur des photos studio et deployer sur des photos floues de telephone.

## A toi

Decris 2 filtres mentaux utiles pour ton probleme vision (ex. "contour metallique", "trou de vis"). Pourquoi la localite aide ?
## Data augmentation utile

Rotation legere, crop, flip si pertinent, variation de luminosite - pour apprendre l'invariance. N'augmente pas d'une facon qui change le label (un flip peut casser un symbole directionnel). Toujours se demander : cette transformation existe-t-elle dans le vrai monde de deploiement ?

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
