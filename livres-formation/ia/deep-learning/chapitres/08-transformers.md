# Chapitre 8 - Transformers : l'attention (overview)

Le transformer est l'architecture dominante du NLP moderne et le coeur de beaucoup de LLM. Idee centrale : l'attention. Chaque position (chaque token) peut regarder les autres positions et ponderer celles qui comptent pour construire une nouvelle representation. Contrairement aux RNN classiques, on peut paralleliser beaucoup mieux sur GPU.

## Attention en image mentale

Quand tu lis "le chat sur le tapis, il dort", le mot "il" doit se relier a "chat". L'attention apprend des liens utiles selon la tache. Multi-tetes : plusieurs types de liens en parallele. Empilement de blocs : representations de plus en plus riches. Ajoute des encodings de position (parce que sinon l'ordre serait moins clair).

## Encodeurs, decodeurs, seq2seq

Selon les modeles : encodeur seul (classification, embeddings), decodeur seul (generation de texte style GPT), encodeur-decodeur (traduction...). Tu n'as pas a tout memoriser. Retiens : attention + profondeur + plein de donnees + plein de calcul = capacites emergentes de langage.

## Lien pratique

Fine-tuning, RAG, prompting : ce sont des facons d'utiliser ces geants sans tout reentrainer. Comprendre le transformer te permet de comprendre pourquoi le contexte a une taille limite, pourquoi les tokens coutent, pourquoi un long document doit parfois etre coupe ou recherches par morceaux.

## Erreur classique

Dire "on a mis un transformer" comme garantie de qualite. L'architecture est un moteur ; donnees, alignement, evaluation et usage font le resultat. Autre piege : confondre "attention" technique et "attention" humaine consciente.

## A toi

Explique l'attention a un ami avec l'exemple du pronom "il". Puis ajoute : pourquoi un GPU aide a entrainer ca.
## Contexte et complexite

L'attention "tous sur tous" coute cher quand la sequence s'allonge (d'ou les limites de contexte et les recherches d'attention efficace). Comprendre ca, c'est comprendre pourquoi on resume, coupe, cherche en RAG, ou paie plus cher pour de longues fenetres.

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
