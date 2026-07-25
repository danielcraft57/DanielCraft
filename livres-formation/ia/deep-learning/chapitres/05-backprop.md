# Chapitre 5 - Backpropagation : l'idee simple de l'apprentissage

La **backpropagation** (retour d'erreur), c'est la methode pour ajuster les poids apres avoir vu une erreur. Version histoire : le reseau fait une prediction (passe avant). On compare a la cible avec une fonction de **perte**. Puis on propage en arriere de petites indications : "toi, poids, monte un peu ; toi, descends". On repete sur beaucoup d'exemples, souvent par petits lots (**mini-batches**).

Chez DanielCraft, on veut que tu puisses raconter la boucle sans notes. Pas deriver sur un tableau avant le cafe. Raconter. Si tu racontes juste, tu ne te feras plus avoir par un jargon qui dit "on backprop" comme un sortilege.

:::retenir
Apprendre = reduire une erreur mesuree en ajustant des poids via passes avant / arriere. La backprop calcule comment chaque poids a contribue a l'erreur.
:::

## Ce que ce n'est pas

Ce n'est pas une comprehension du sens. La backprop optimise un critere. Si le critere est mal choisi, elle optimise mal - brillamment. Ce n'est pas non plus "comprendre comme un humain". Et ce n'est pas quelque chose que tu dois reprogrammer a la main en 2026 : les frameworks (PyTorch, TensorFlow...) calculent les gradients. Ton job : donnees, architecture raisonnable, loss adaptee, monitoring, regularisation.

## Image mentale : descente de gradient

Imagine etre dans le brouillard sur une colline et vouloir descendre : tu sens la pente sous tes pieds et tu fais un pas dans la direction qui descend. Le **gradient** est cette pente dans l'espace des poids. Le **taux d'apprentissage** (learning rate) est la taille du pas. Trop grand : tu sautes et tu diverges. Trop petit : tu rampes eternellement. Ines a vu une loss exploser apres avoir "mis le learning rate a fond pour aller plus vite". La colline n'aime pas les grands sauts aveugles.

:::idee
Quand la loss train ne baisse pas, demande d'abord : learning rate, bugs de donnees, mauvaise loss - avant d'ajouter dix couches.
:::

## Epochs et batches

Une **epoch** : un passage sur l'ensemble d'entrainement. Un **batch** : un sous-groupe d'exemples pour une mise a jour. Ces details changent stabilite et vitesse. En pratique, tu observes la courbe de loss train / validation. Si le train plonge et la validation remonte, tu n'as pas un succes : tu as souvent de l'overfitting en cours.

## Optimizers (apercu)

SGD, Adam et cousins : des facons d'utiliser les gradients pour mettre a jour les poids, avec des astuces de moment et d'adaptation du pas. Tu n'as pas a les reinventer. Sache qu'ils existent, qu'ils ont des reglages, et que le learning rate reste souvent le levier le plus sensible. Lea note dans ses briefs prestataires : "quels optimizer et learning rate, et comment vous arretez l'entrainement ?"

## Petite histoire

Sam a fait jouer la boucle a voix haute : batch, avant, loss, arriere, maj des poids, repeter. Un eleve a dit "c'est comme corriger une recette apres chaque degustation". Presque : sauf que tu corriges des milliers de dosages a la fois, un peu, souvent. Max a ajoute : "et si ma degustation est biaisee, je corrige dans le mauvais sens". Exact. Labels sales = apprentissage confiant vers le faux.

## Erreur classique

Croire que backprop "comprend". Autre piege : juger un entrainement seulement sur la loss train. Troisieme piege : changer cinq hyperparametres a la fois et ne plus savoir ce qui a aide. Change une chose, logge, compare a une baseline.

:::attention
Une loss train qui baisse n'est pas un produit. La validation et le terrain decident.
:::

## En vrai

Raconte la boucle en 6 etapes orales : batch, avant, loss, arriere, maj des poids, repeter. Chronometre-toi. Moins de 45 secondes nettes = socle acquis.

## A toi

Ecris les 6 etapes sans regarder. Puis ajoute une 7e ligne : "ce que je regarde pour savoir si ca generalise".

## Ce que tu retiens sans maths

Des millions (parfois milliards) de poids bougent pour reduire une erreur. Les frameworks font le calcul. Toi, tu choisis le probleme, tu soignes les donnees, tu lis les courbes, tu arrete quand la validation stagne (**early stopping**), tu refuses le theatre du "encore une epoch pour voir". Chez DanielCraft, l'apprentissage est une boucle disciplinaire autant qu'une formule.

## Scene Ines

Ines lance un petit entrainement de transfer learning. Elle regarde train et val. A l'epoch 7, train continue de baisser, val stagne. Elle stoppe, sauvegarde le meilleur checkpoint val, inspecte les erreurs. Elle n'a pas "fini le deep learning". Elle a pratique la backprop comme un pilote : capteurs, pas foi aveugle.

## Loss : le critere que tu choisis

Cross-entropy pour classer, erreur quadratique pour un nombre : la loss dit au reseau quoi minimiser. Si tu punis mal, tu obtiens un comportement confiant et hors sujet. Ines a un jour optimise l'accuracy globale alors que rater une piece critique coutait dix fois plus. Elle a change le critere (poids d'erreur, metrique metier). La backprop a alors pousse les poids dans une direction plus utile. Chez DanielCraft, on repete : optimiser juste un mauvais objectif, c'est encore se tromper.

## Mini-batch : pourquoi pas tout d'un coup

Tout le dataset a chaque pas serait trop lent et parfois trop lisse. Un exemple seul serait trop bruyant. Le mini-batch est le compromis. Tu n'as pas a choisir la taille parfaite jour 1. Tu dois savoir que ce levier existe, et qu'il change la stabilite des mises a jour.
