# Chapitre 6 - CNN : voir par filtres locaux

**CNN** signifie Convolutional Neural Network : reseau a **convolutions**. Idee : au lieu de relier chaque pixel a chaque neurone (trop cher, trop de parametres), on fait glisser de petits **filtres** qui detectent des motifs locaux - bords, textures - partages sur toute l'image. Puis on empile : motifs plus riches, cartes de features, souvent reduction spatiale, puis decision.

Chez DanielCraft, c'est le chapitre vision par excellence. Si tu bosses l'image, tu dois sentir pourquoi la localite compte. Si tu ne bosses pas l'image, tu comprends quand meme pourquoi "aplatir une photo dans un dense" est souvent une mauvaise premiere idee.

:::retenir
CNN = filtres locaux partages qui glissent sur l'image. A priori de localite + partage de poids.
:::

## Ce que ce n'est pas

Ce n'est pas la seule architecture vision en 2026 (les vision transformers existent aussi). Ce n'est pas magique avec 200 photos from scratch. Ce n'est pas non plus "regarder" comme un humain : ce sont des motifs statistiques appris. Et ce n'est pas un permis de juger sur des photos studio pour deployer sur du flou de telephone.

## Image mentale

Un chat peut etre a gauche ou a droite : un filtre d'"oreille" utile partout grace au partage de poids. Un pixel depend surtout de son voisinage : la localite est un a priori puissant. Les premieres couches tendent vers des motifs simples ; plus loin, des formes plus abstraites. Ines imagine deux filtres mentaux pour ses pieces : "contour metallique", "trou de vis". Elle sait que le reseau apprendra ses propres filtres ; l'exercice sert a sentir le besoin.

:::idee
Avant d'entrainer, decris les conditions reelles : eclairage, flou, angle, telephone. Le modele vivra la-bas, pas dans ton dossier "jolies photos".
:::

## Usages

Classification d'images, detection d'objets, segmentation, controle qualite sur chaine, lecture de documents scannes (avec d'autres briques). Ines peut entrainer ou, plus souvent, reutiliser un modele preentraine (**transfer learning**) sur ses pieces detachees. Lea demande a ses prestataires vision : "preentraine ou from scratch ?", "quelles augmentations ?", "quel set terrain ?".

## Data augmentation utile

Rotation legere, crop, flip si pertinent, variation de luminosite - pour apprendre l'invariance. N'augmente pas d'une facon qui change le label : un flip peut casser un symbole directionnel. Toujours se demander : cette transformation existe-t-elle dans le vrai monde de deploiement ? Max a ri : "retourner ma piece a l'envers, ca arrive ; ecrire du texte a l'envers sur mon compteur, non".

## Petite histoire

Ines a 180 photos. Tentation : CNN profond from scratch. Resultat : overfitting. Elle passe a un backbone preentraine, remplace la tete de classification, augmente prudemment, valide sur photos chantier. Le score "labo" baisse. Le score "telephone sous neon" monte. Sam utilise cette histoire en cours : la realite bat le leaderboard interne.

## Erreur classique

Entrainer un CNN profond from scratch avec trop peu d'images. Prefere transfer learning + augmentation avec prudence. Autre piege : juger sur studio, deployer sur terrain. Troisieme : data augmentation absurde qui cree des exemples impossibles et trompe le metier.

:::attention
Un beau score sur un set propre ne prouve rien sur le flou, la pluie, ou l'angle bizarre du client.
:::

## En vrai

Prends 10 photos de ton probleme (ou imagine-les). Note 3 variations que le modele verra forcement en production. Ton plan d'augmentation doit en couvrir au moins deux sans casser le label.

## A toi

Decris 2 filtres mentaux utiles pour ton probleme vision (ex. "contour metallique", "trou de vis"). Pourquoi la localite aide ? Cinq a huit lignes.

## Lien avec la suite

Le chapitre overfitting te dira comment lire les courbes. Le transfer learning te dira comment reutiliser un cerveau deja forme. L'atelier CNN te fera ecrire un plan de projet sans pretendre avoir deja 10 000 labels. Chez DanielCraft, le plan honnete vaut mieux que le notebook theatral.

## Partage de poids : economie et invariances

Un filtre de 3x3 sur une grande image reutilise les memes dosages partout. Moins de parametres qu'un dense naif. Meilleure chance d'apprendre un motif "bord" utile a gauche comme a droite. C'est pour ca que les CNN ont domine la vision pendant des annees. Les vision transformers changent parfois la donne aujourd'hui ; l'intuition convolution reste un socle. Lea demande quand meme : "pourquoi cette famille pour mon cas ?" - la reponse doit citer la localite, pas la mode.

## De la carte de features a la decision

Apres plusieurs convolutions et reductions spatiales, tu obtiens des cartes plus abstraites, puis souvent une tete dense ou une tete de detection. Ines n'a pas besoin de dessiner chaque tenseur. Elle doit savoir ou brancher le transfer : souvent garder le corps, changer la tete, evaluer sur le terrain.

## Detection et segmentation (apercu)

Classer toute l'image est un cas. Detecter des objets avec des boites, ou segmenter pixel par pixel, demande d'autres tetes et plus de labels. Ines commence souvent par la classification de piece entiere. Elle note detection comme etape 2 si le besoin metier le prouve. Ne saute pas les marches : chaque marche a son cout d'annotation.
