# Chapitre 15 - Atelier : CNN et transfer learning (plan de projet)

Objectif : ecrire un plan de projet vision realiste. Duree : 40 minutes.

## Etapes

1) Definir 3 a 10 classes d'images. 2) Estimer combien de photos par classe tu peux collecter. 3) Decrire les conditions reelles (eclairage, flou, telephone). 4) Choisir un modele preentraine a adapter. 5) Plan d'augmentation de donnees (liste). 6) Split train/val/test. 7) Metriques (accuracy + erreurs couteuses). 8) Plan anti-overfitting. 9) Critere go/no-go avant deploiement. 10) Idee GPU : local, cloud, ou seulement inference API.

## Livrable

Document "plan CNN" de 1 a 2 pages. Pas besoin d'avoir entraine pour valider le plan.

## Conseil

Si tu as moins de 50 images au total, reste sur proof of concept et transfer learning agressif, ou reconsidere la faisabilite.
## Go / no-go

Ecris a l'avance : "si la metrique X sur test terrain < Y, on n'automatise pas, on garde un humain dans la boucle". Signe-le. Tu evites le deploiement par enthousiasme.

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
