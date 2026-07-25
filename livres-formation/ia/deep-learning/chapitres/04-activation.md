# Chapitre 4 - Activations : introduire du non-lineaire

Si tu n'empilais que des additions et multiplications lineaires, plusieurs couches denses s'effondreraient en une seule transformation lineaire. Les fonctions d'**activation** cassent cette linearite. Elles permettent au reseau de tordre l'espace et d'approximer des motifs complexes. Sans elles, la "profondeur" serait surtout du theatre.

Chez DanielCraft, on retient une phrase : l'activation est le geste qui rend l'empilement utile. Tu n'as pas a collectionner vingt variantes. Tu as a comprendre le role, quelques classiques, et le piege de la saturation.

:::retenir
Sans non-linearite entre les couches, pas de profondeur utile. Activation = tordre le signal pour approximer du complexe.
:::

## Ce que ce n'est pas

Ce n'est pas la meme chose que la fonction de **perte** (loss). L'activation transforme des signaux a l'interieur du reseau ; la loss mesure l'erreur pour apprendre. Ce n'est pas non plus une decoration de graphique. Et ce n'est pas "une seule activation pour tout" : les couches cachees et la sortie ont souvent des besoins differents.

## Image mentale

Imagine un score brut qui sort d'une somme ponderee. **ReLU** laisse passer les positifs et coupe les negatifs : simple, souvent efficace en couches cachees. **Sigmoid** ecrase vers 0..1 : utile parfois pour une probabilite binaire. **Softmax** transforme plusieurs scores en une distribution qui somme a 1 : langage courant des classifieurs multi-classes. Pour un LLM, la sortie ressemble a une distribution sur le vocabulaire : "quel prochain token est probable ?".

Ines, pour ses pieces, pense "scores bruts puis softmax vers classes". Elle n'a pas besoin de deriver la formule pour choisir la bonne idee.

## En sortie

La derniere activation depend de la tache : nombre libre (regression), probabilite (classification binaire), distribution sur classes (softmax), ou distribution sur vocabulaire (LLM). Choisir une mauvaise sortie, c'est comme demander a un thermometre d'afficher une couleur sans legende. Lea a vu un prestataire sortir des scores non normalises et les presenter comme des "pourcentages de confiance" a un client. Confusion garantie.

:::idee
Avant de parler "confiance", demande : cette sortie est-elle une probabilite calibree, un score brut, ou une impression marketing ?
:::

## Softmax en sortie (intuition)

Pour plusieurs classes, on obtient des scores bruts puis un softmax les transforme en nombres positifs qui somment a 1. Utile pour choisir la classe ou pour lire une incertitude relative. Ce n'est pas une garantie de calibration parfaite : un modele peut etre tres "sur" et faux. Sam le dit aux eleves : distribution n'egal pas verite.

## Petite histoire

Max a demande a Ines pourquoi "couper les negatifs" aidait. Elle a pris l'image d'un robinet : parfois tu veux eteindre un signal inutile pour laisser d'autres chemins s'exprimer. ReLU est brutal et efficace souvent. D'autres activations existent quand ReLU "tue" trop de neurones (dying ReLU) - variantes que tu rencontreras si tu codes. Pour comprendre, retiens le besoin de non-linearite d'abord.

## Erreur classique

Utiliser une activation qui sature trop et "tue" le **gradient** : l'apprentissage n'avance plus. D'ou la popularite de ReLU et variantes dans beaucoup de couches cachees. Autre piege : confondre activation et loss. Troisieme piege : lire un softmax comme une certitude metier sans evaluation hors distribution.

:::attention
Fluide et "99 %" a l'ecran n'egalent pas competent. Verifie sur des cas reels.
:::

## En vrai

Explique a voix haute, en cinq lignes, pourquoi on active non lineairement entre les couches. Si tu bloques, relis l'image de l'effondrement lineaire.

## A toi

Explique a un ami (ou sur papier) pourquoi on active non lineairement entre les couches. Ajoute un exemple de sortie pour une tache binaire et une tache multi-classes.

## Lien avec la backprop

Au chapitre suivant, tu verras que l'apprentissage remonte une erreur a travers ces activations. Si une activation ecrase trop le signal, le message "monte / descends un peu" s'affaiblit. D'ou l'importance pratique du choix - pas pour le snobisme mathematique, pour que l'entrainement bouge.

## Scene DanielCraft

Lea prepare un atelier client. Elle ecrit au tableau : "lineaire empile = encore lineaire" puis "activation = pliure". La salle retient mieux que dix slides de formules. Chez DanielCraft, on prefere cette pliure mentale a une encyclopedie d'activations jamais utilisees.

## ReLU vs saturations (terrain)

Ines a vu une fois une courbe plate : loss qui ne bouge presque plus. Cause probable : signaux ecrases, gradients faibles. Elle a change d'activation cachee vers une variante plus "passante", baisse legerement le learning rate, et la courbe a repris. Tu n'as pas a memoriser le nom de chaque variante. Tu as a reconnaitre le symptome : "plus rien n'apprend" peut venir d'une non-linearite mal choisie autant que d'un bug de labels.

## Activation et lecture metier

Quand un softmax sort 0.91 sur une piece, Lea demande : "calibre sur quel set ?". Si le set est studio et le terrain est neon, le 0.91 ment poliment. L'activation organise des nombres ; elle ne certifie pas le monde. Sam le fait repeter : distribution utile, verite a verifier.
