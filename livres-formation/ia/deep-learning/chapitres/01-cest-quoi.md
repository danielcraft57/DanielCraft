# Chapitre 1 - Salut, c'est quoi le deep learning ?

Le deep learning, c'est une famille de machine learning qui utilise des reseaux de neurones artificiels avec plusieurs couches. "Deep" veut dire profond : beaucoup d'etages de transformation entre l'entree et la sortie. Ces modeles ont casse des plafonds sur l'image, la voix, puis le langage. Les LLM dont on parle tous les jours sont, sous le capot, des architectures de deep learning specialisees (souvent des transformers).

Chez DanielCraft, on ne commence pas par les equations. On commence par l'intuition : empiler des filtres qui apprennent a reconnaitre des motifs de plus en plus abstraites - bords, formes, objets, ou pour le texte : fragments, structures, intentions probables.

## Ce que ce livre couvre

Neurone, couches, activations, idee simple de la backprop, CNN, RNN, transformers (overview), overfitting en deep learning, idee des GPU, transfer learning, lien avec les LLM, ateliers, limites, bonnes pratiques, quiz. Tu sortiras capable d'expliquer a un ami comment ca marche "en gros", et de ne pas te faire impressionner par un jargon vide.

## Deep learning vs ML classique

Sur un petit tableau de 10 colonnes numeriques, un modele scikit-learn simple gagne souvent. Sur une image brute (des milliers de pixels) ou du texte long, le deep learning brille parce qu'il apprend aussi des representations, pas seulement une decision sur des features deja ciselees a la main. En 2026, les deux coexistent. Choisir, c'est matchier le probleme.

## Fil rouge

Ines developpe une appli qui reconnait des pieces detachees sur photo, puis veut comprendre comment les assistants texte fonctionnent. Elle n'a pas besoin de reinventer un laboratoire. Elle a besoin d'une carte mentale solide pour dialoguer avec des outils, des prestataires, et plus tard du code.

## Erreur classique

Croire que deep learning = toujours mieux. Ou croire qu'il faut un cluster de GPU pour comprendre. Comprendre d'abord ; scaler ensuite.

## A toi

Ecris un probleme "image ou texte" ou le deep learning semble pertinent, et un probleme "petit tableau" ou un modele simple suffit. Garde la distinction.
## Pourquoi "representations"

En ML classique, tu ciselais souvent les features a la main. En deep learning, les couches apprennent aussi des features internes. Sur une image, tu ne codes pas "bord vertical" a la main ; une convolution peut l'apprendre. Sur du texte, tu n'inventes pas toutes les associations ; l'attention les pondere. Cette automatisation a un prix : opaqueite, besoin de donnees/calcul, risque d'overfitting. Le jeu n'en vaut la chandelle que si le probleme le demande.

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
