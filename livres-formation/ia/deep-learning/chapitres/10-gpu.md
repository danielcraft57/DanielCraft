# Chapitre 10 - GPU : pourquoi ca va plus vite (idee)

Un **GPU** (processeur graphique) est tres bon pour faire beaucoup de petites operations similaires en parallele - exactement le genre de calculs des reseaux (grosses multiplications de matrices, attentions, convolutions). D'ou son role central dans l'**entrainement** et parfois l'**inference** des modeles lourds.

Chez DanielCraft, on demystifie le fer. Tu n'as pas besoin d'acheter une carte pour comprendre. Tu as besoin de savoir pourquoi les tutos disent "il me faut un GPU", pourquoi l'inference LLM coute de l'argent, et comment choisir entre entrainer, fine-tuner, ou seulement appeler un modele existant.

:::retenir
GPU = parallelisme massif pour des calculs de matrices. Utile ; pas un sesame moral ni un prerequis pour apprendre.
:::

## Ce que ce n'est pas

Ce n'est pas obligatoire pour comprendre le deep learning. Ce n'est pas une garantie de bon modele. Ce n'est pas non plus "CPU = inutile" : le CPU reste excellent pour la logique variee, le data loading, beaucoup de pipelines. Et ce n'est pas un permis de louer du calcul cher avant d'avoir valide la question metier sur un sous-ensemble.

**CPU** : peu de coeurs tres flexibles, excellent pour des taches variees. **GPU** : des milliers de petits coeurs pour le throughput sur des operations similaires. Entrainer un gros CNN ou un transformer sur CPU seul peut etre lent jusqu'a l'absurde. Sur GPU (ou TPU / accelerateurs), ca devient praticable. Lea compare : "couteau suisse vs usine a parallele". Grossier. Utile.

:::astuce
Avant d'acheter ou louer, ecris : j'entraine, je fine-tune, ou j'inferre seulement ? Le besoin GPU change selon la reponse.
:::

## Ce que ca change pour toi

Cloud, notebooks heberges, services geres, modeles deja entraines via API : autant de facons d'utiliser la puissance sans la posseder. Ines protototype d'abord avec un modele preentraine et un petit set. Elle ne loue du GPU serieusement qu'apres un go metier. Max, lui, n'a besoin que d'une API vision de temps en temps : zero carte chez lui, zero honte.

## Inference vs training

Entrainer est souvent le plus gourmand. Inferer (servir des predictions) peut aussi couter cher a grande echelle - millions de requetes LLM, latence, energie. Optimiser l'inference (quantization, batching, petit modele) est un metier. Pour un debutant : mesure avant d'acheter du fer. Sam fait estimer a ses eleves un cout mensuel grossier : requetes x tokens x prix, plus le temps de verification humaine.

## Limites memoire

La **VRAM** est finie. Un gros batch ou un long contexte peuvent saturer. Optimisations possibles plus tard : precision reduite, quantization, distillation, batching, gradient checkpointing. Idees, pas besoin de tout implementer jour 1. Retiens surtout : "out of memory" n'est pas une fatalite morale, c'est un signal de dimensionnement.

## Petite histoire

Un prestataire a propose a Lea "on loue huit GPU une semaine pour tout reentrainer". Lea a demande le baseline transfer learning sur un seul accelerateur leger. Resultat deja utile. Les huit GPU sont restes dans le devis, non signes. Chez DanielCraft, on aime cette scene : le calcul suit la preuve, pas l'inverse.

## Erreur classique

Croire que sans GPU perso on ne peut rien apprendre. Autre piege : louer du calcul cher sans valider la question metier. Troisieme : confondre "j'ai un GPU" et "mon protocole de validation est propre".

:::attention
Le fer accelere une boucle. Il ne remplace ni les labels, ni les metriques, ni le jugement.
:::

## En vrai

Pour ton projet : entrainer, fine-tuner, ou inferer via un modele existant / une API ? Ecris la reponse en une phrase et le besoin GPU associe (aucun / ponctuel / serieux).

## A toi

Remplis le tableau mental : tache, volume de donnees, besoin calcul, alternative sans GPU. Une decision claire en bas de page.

## Energie et argent

Calcul = argent + energie. Utiliser le plus petit modele qui fait le job, reutiliser des poids preentraines, preferer l'inference sobre : ce sont des gestes techniques et ethiques a la fois. Ines le note a cote de ses metriques. Ce n'est pas du greenwashing de slide ; c'est du dimensionnement adulte.

## Cloud, Colab, API : trois portes

Porte 1 : notebook heberge avec GPU ponctuel pour apprendre. Porte 2 : cloud loue a l'heure pour un fine-tune serieux. Porte 3 : API - tu n'as pas le fer, tu achetes l'inference. Ines utilise 1 pour prototyper, 3 pour certains textes, 2 seulement apres go metier. Max reste souvent en 3. Lea met les trois portes dans ses devis pour eviter le "il nous faut huit cartes" sans preuve.

## Precision et quantization (apercu)

On peut parfois calculer avec moins de bits pour aller plus vite ou tenir en memoire. Quantization, distillation : mots que tu rencontreras si tu optimises l'inference. Jour 1, retiens seulement : il existe des leviers avant d'acheter plus de fer. Mesure d'abord le besoin.
