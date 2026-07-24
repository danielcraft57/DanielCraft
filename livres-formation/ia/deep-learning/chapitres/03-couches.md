# Chapitre 3 - Couches : empiler des transformations

Une couche, c'est un groupe de neurones qui recoivent les sorties de la couche precedente. Couche d'entree : tes donnees (pixels, tokens embeds, mesures). Couches cachees : transformations internes. Couche de sortie : prediction (classes, nombres, tokens suivants...).

## Profondeur

Plus de couches peuvent representer des fonctions plus riches - mais coutent plus cher a entrainer, et overfitent plus facilement si les donnees manquent. "Deep" n'est pas un concours de profondeur. C'est un compromis signal / donnees / calcul / regularisation.

## Representations

Les premieres couches d'un CNN tendent a detecter des motifs locaux simples ; plus loin, des formes plus abstraites. Dans le texte, des couches successives melangent le contexte. Tu n'as pas a visualiser chaque neurone. Retiens : le reseau apprend aussi comment representer l'entree, pas seulement la derniere decision.

## Fully connected vs specialise

Une couche dense relie tout a tout (couteux sur de grandes entrees). Les CNN partagent des filtres locaux sur l'image. Les transformers utilisent des mecanismes d'attention pour relier des positions du sequence. L'architecture encode un a priori : localite pour l'image, dependances longues pour le langage, etc.

## Erreur classique

Ajouter des couches parce que "deep = moderne" sans mesurer. Ou ignorer la taille d'entree (aplatir une image 4K dans une couche dense naive : explosion de parametres).

## A toi

Dessine un reseau a 3 etages pour classer spam/texte court : entree, cachee, sortie. Que sort la derniere couche (2 scores ? 1 probabilite ?).
## Largeur vs profondeur

Elargir une couche (plus de neurones) ou approfondir (plus de couches) ne produit pas le meme effet. Trop large et trop profond sans donnees : overfitting et cout. Les architectures modernes jouent sur des blocs repetes, des connexions residuelles, des normes - details que tu rencontreras plus tard. Ici, retiens le levier : forme du reseau = hypothese sur la structure du probleme.

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
