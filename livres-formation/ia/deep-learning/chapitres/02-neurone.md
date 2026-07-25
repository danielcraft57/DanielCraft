# Chapitre 2 - Un neurone : une petite decision ponderee

Un **neurone artificiel**, en version poche, prend des entrees numeriques, les multiplie par des **poids**, ajoute un **biais**, puis passe le resultat dans une fonction d'**activation**. Pense a une recette qui melange des ingredients avec des dosages, puis decide si le signal continue. Ce n'est pas une cellule vivante. C'est une petite fonction flexible, ajustable sur des exemples.

Chez DanielCraft, on insiste sur cette sobriete : si tu comprends un neurone, tu comprends le brique de base. Le reste du livre n'est "que" de l'organisation - couches, specialisations, astuces d'apprentissage - autour de cette brique.

:::retenir
Neurone = entrees x poids + biais, puis activation. Les poids s'apprennent sur des exemples.
:::

## Ce que ce n'est pas

Ce n'est pas une copie fidele du cerveau. Le nom s'inspire de la biologie ; l'ingenierie a pris ce qu'il lui fallait et a laisse le reste. Ce n'est pas non plus une unites qui "contient" a elle seule le concept chat, piece, ou spam. Les concepts emergent souvent de patterns distribues dans beaucoup d'unites. Et ce n'est pas une excuse pour fixer les poids a la main "logiquement" sur des taches complexes : l'apprentissage le fait mieux, a condition d'avoir des donnees.

Imagine predire "prendre un parapluie". Entrees possibles : probabilite de pluie, force du vent, distance a parcourir. Chaque entree a un poids. Si la pluie compte beaucoup, son poids grossit en valeur absolue. Si le vent est du bruit, il s'attenue. Le biais decale le seuil de decision. L'activation decide comment ce score brut devient un signal utile - coupe, ecrase, laisse passer.

Ines, sur ses pieces, imagine des entrees plus abstraites plus tard (motifs de texture, contours). Mais le geste mental reste le meme : melanger, ponderer, activer.

## Pourquoi des poids ?

Les poids s'ajustent pendant l'apprentissage. Tu n'ecris pas la regle complete a la main ; tu laisses les exemples pousser les dosages. Chaque poids est un **parametre**. Plus tu en as dans un reseau, plus tu peux coller a des motifs complexes - et au bruit. La capacite n'est pas un trophee. C'est un budget a depenser avec des donnees et de la regularisation. Un neurone unique a peu de capacite ; un LLM en a une immense.

:::astuce
Quand quelqu'un dit "le modele a appris", traduis : "des poids ont bouge pour reduire une erreur mesuree".
:::

## Limite d'un seul neurone

Un neurone seul est faible : il trace des frontieres simples. La puissance vient des **reseaux** : beaucoup de neurones organises en couches, qui composent des decisions. Comme une equipe : chacun voit un aspect ; ensemble ils resolvent un motif complexe. C'est pour ca que le chapitre suivant parle d'empiler.

## Petite histoire

Lea devait expliquer a un client pourquoi "un neurone" n'allait pas reconnaitre une piece metallique sur photo. Elle a dessine trois fleches (entrees), des dosages, une petite case "activation", une sortie. Le client a sourit : "donc c'est une balance ?". Presque. Une balance qui s'auto-regle sur des milliers d'exemples. Max, le meme jour, a compare ca a son "feeling" de chantier : il pondere humidite, temperature, type de joint. Difference : lui assume ; le neurone optimise un critere sans comprendre le metier.

## Erreur classique

Imaginer un neurone unique qui "contient" le concept. Autre piege : croire que plus de parametres = toujours plus intelligent. Sans donnees et sans controle, plus de parametres = plus de memorisation du train. Sam le dit a ses eleves : capacite sans discipline, c'est du par coeur.

:::attention
Le nom "neurone" est une metaphore utile. N'en deduis pas que le reseau "pense" ou "sent".
:::

## En vrai

Prends une decision binaire de ton quotidien (sortir le linge, accepter un devis, classer un mail). Liste trois signaux d'entree. Imagine des poids. Tu viens de faire un mini-neurone mental - sans code.

## A toi

Invente 3 entrees pour predire "prendre un parapluie" (meteo, vent, distance). Imagine des poids. Ou ton intuition est-elle deja un mini-neurone ? Ecris-le en cinq lignes.

## Parametres et capacite

Chaque connexion poids compte. Dans un reseau profond, on parle de millions, parfois de milliards de parametres. Cette capacite explique les succes spectaculaires - et les echecs d'overfitting. Plus loin, on verra comment la **backprop** ajuste ces dosages, et comment le transfer learning reutilise des poids deja utiles plutot que de tout reinventer.

## Scene Ines

Ines pose sur une feuille : "entree brute = pixels", "sortie = classe de piece". Entre les deux, elle dessine des neurones en couches sans encore les detailer. Elle sait deja une chose : la decision finale n'est qu'une combinaison ponderee de signaux appris. Cette phrase lui evite de croire au mystere. Chez DanielCraft, c'est exactement le niveau de clarte qu'on vise au chapitre 2.

## Trois nombres pour sentir

Prends pluie=0.8, vent=0.2, distance=0.5. Imagine poids 2.0, 0.1, 0.5 et biais -1.0. Score brut = 0.8*2 + 0.2*0.1 + 0.5*0.5 - 1.0 = 0.92. Avec ReLU, la sortie reste 0.92. Change la pluie a 0.1 : le score bascule. Tu viens de voir un neurone reagir sans framework. Chez DanielCraft, ce mini calcul vaut mieux qu'une slide animee : tu sens le dosage.

## Du neurone au reseau (teaser)

Demain, tu empileras. Garde cette idee : chaque neurone ne "voit" qu'une combinaison. La richesse nait de l'organisation. Ines ecrit sur son carnet : "1 neurone = 1 vote pondere ; le comite decide plus loin". C'est assez pour passer au chapitre couches sans mystere.
