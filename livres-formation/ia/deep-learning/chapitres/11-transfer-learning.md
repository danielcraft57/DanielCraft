# Chapitre 11 - Transfer learning : reutiliser un cerveau deja forme

Le transfer learning, c'est repartir d'un modele deja entraine sur une tache large (ex. reconnaitre des objets sur des millions d'images, ou un modele de langage sur d'enormes corpus) et l'adapter a ton cas avec moins de donnees. Au lieu d'apprendre tout from scratch, tu reutilises des representations utiles.

## Pourquoi c'est le geste 2026

Parce que les donnees labellisees coutent cher, et parce que les modeles fondation existent. Ines telecharge un CNN preentraine, remplace la tete de classification, entraine surtout les dernieres couches sur ses pieces. Sur le texte, on fine-tune legerement, ou on fait du prompting / RAG sans tout retoucher. Le transfer learning est l'esprit ; le prompting est parfois la forme extreme "sans maj des poids".

## Strategies

Geler beaucoup de couches, entrainer la tete. Puis parfois deverrouiller plus profond a petit learning rate. Adapter avec peu de parametres (LoRA et cousins dans le monde LLM). Surveiller l'overfitting : meme un modele preentraine peut coller a 100 images.

## Limites

Si ton domaine est trop eloigne (images medicales tres specifiques vs photos web), le transfert aide moins ou demande plus de soin. Si tes labels sont sales, tu transfers aussi vers le sale. La licence et le cout des modeles comptent.

## Erreur classique

Reentrainer tout a gros learning rate et detruire les representations utiles (catastrophe forgetting). Ou croire que transfer learning dispense de validation.

## A toi

Decris un modele fondation que tu reuserais (vision ou texte) et ce que tu adapterais (classes, style, documents).
## Domaine shift

Si tes images de pieces sont greasy, floues, mal eclairees, et que le modele preentraine a vu des photos web propres, tu as un ecart de domaine. Le transfert aide encore souvent, mais prevoyez plus d'exemples cibles, une augmentation realiste, et une evaluation sur le vrai terrain.

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
