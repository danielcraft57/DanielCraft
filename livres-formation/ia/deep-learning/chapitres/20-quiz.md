# Quiz final

1. Le "deep" de deep learning renvoie surtout a :
- A) La couleur sombre des GPU
- B) Des reseaux a plusieurs couches
- C) Une voix grave

2. Une activation non lineaire sert a :
- A) Decorar les graphiques
- B) Permettre aux couches empilees d'approximer des motifs complexes
- C) Remplacer les donnees

3. La backprop, en idee :
- A) Ajuste les poids a partir de l'erreur
- B) Efface le disque dur
- C) Genere des images sans modele

4. Un CNN est particulierement utile pour :
- A) Les filtres locaux sur images
- B) Remplacer toute base de donnees
- C) Facturer les API

5. Les transformers reposent surtout sur :
- A) L'attention entre positions / tokens
- B) Une unique droite de regression
- C) Un seul neurone

6. L'overfitting DL se manifeste souvent par :
- A) Train excellent, validation faible
- B) Train faible, validation parfaite toujours
- C) Absence totale d'erreur humaine

7. Un GPU aide surtout parce que :
- A) Il parallelise de gros calculs de matrices
- B) Il ecrit tes prompts
- C) Il anonymise les donnees tout seul

8. Le transfer learning, c'est :
- A) Reutiliser un modele preentraine pour l'adapter
- B) Transferer des fichiers par FTP uniquement
- C) Interdit en 2026

9. Un LLM est :
- A) Sans aucun lien avec le deep learning
- B) Un modele de deep learning (souvent transformer) pour le langage
- C) Un type de cable

10. Avant d'entrainer un gros reseau from scratch, DanielCraft recommande souvent :
- A) De regarder si un modele preentraine / une API / un modele simple suffit
- B) D'acheter dix GPU sans question metier
- C) D'ignorer la validation

## Corriges

1-B, 2-B, 3-A, 4-A, 5-A, 6-A, 7-A, 8-A, 9-B, 10-A.

9/10+ : bon socle. Sinon, relis couches, backprop, CNN/transformers, transfer, lien LLM.
## Bonus oral

Sans notes, explique a un ami : neurone, couche, backprop, CNN, transformer, transfer learning, lien LLM. Si tu bloques sur un, relis le chapitre, recommence.

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
