# Chapitre 10 - GPU : pourquoi ca va plus vite (idee)

Un GPU (processeur graphique) est tres bon pour faire beaucoup de petites operations similaires en parallele - exactement le genre de calculs des reseaux (grosses multiplications de matrices). D'ou son role central dans l'entrainement et parfois l'inference des modeles lourds.

## CPU vs GPU (intuition)

CPU : excellent pour la logique variee, peu de coeurs tres flexibles. GPU : des milliers de petits coeurs pour le throughput. Entrainer un gros CNN ou un transformer sur CPU seul peut etre lent jusqu'a l'absurde. Sur GPU (ou TPU / accelerateurs), ca devient praticable.

## Ce que ca change pour toi

Tu n'as pas forcement besoin d'acheter une carte. Cloud, Google Colab, services managés, modeles deja entraines via API : autant de facons d'utiliser la puissance sans la posseder. Comprends juste pourquoi "il me faut un GPU" apparait dans les tutos, et pourquoi l'inference LLM a un cout (calcul = argent + energie).

## Limites

Memoire GPU (VRAMs) : un gros batch ou un long contexte peuvent saturer. Optimisations : precision reduite, quantization, distillation, batching. Encore une fois : idees, pas besoin de tout implementer jour 1.

## Erreur classique

Croire que sans GPU perso on ne peut rien apprendre. Tu peux comprendre, prototyper petit, utiliser des modeles preentraines, appeler des API. Autre piege : louer du calcul cher sans d'abord valider la question metier sur un sous-ensemble.

## A toi

Estime pour ton projet : est-ce que tu as besoin d'entrainer, de fine-tuner, ou seulement d'inferer via un modele existant ? Le besoin GPU change selon la reponse.
## Inference vs training

Entrainer est souvent le plus gourmand. Inferer (servir des predictions) peut aussi couter cher a grande echelle (millions de requetes LLM). Optimiser l'inference (quantization, batching, petit modele) est un metier. Pour un debutant : mesure avant d'acheter du fer.

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
