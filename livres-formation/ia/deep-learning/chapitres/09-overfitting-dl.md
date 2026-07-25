# Chapitre 9 - Overfitting en deep learning

Les reseaux ont souvent des millions ou des milliards de **parametres**. Capacite enorme = facilite a coller au train. L'**overfitting** est donc central en deep learning, plus encore qu'avec un petit modele. Signes classiques : accuracy train haute, validation basse ; ecarts qui se creusent au fil des epochs ; performances magiques sur un petit jeu trop vu.

Chez DanielCraft, on traite l'overfitting comme un risque de metier, pas comme une note de bas de page. Un modele qui recite le dossier d'entrainement et se plante sur le telephone du client n'est pas "presque bon". Il est dangereux s'il decide seul.

:::retenir
Capacite sans donnees ni regularisation = memorisation. Surveille train et validation ensemble.
:::

## Ce que ce n'est pas

Ce n'est pas "le modele est trop intelligent". C'est souvent le contraire de la generalisation utile. Ce n'est pas non plus resolu en ajoutant toujours plus de couches. Parfois il faut mieux de donnees, pas plus de profondeur. Et ce n'est pas uniquement un probleme de vision : le texte, l'audio, les series temporelles overfitent aussi.

Imagine un eleve qui apprend par coeur dix sujets d'examen. Le jour J, le sujet change d'un cran : il panique. Le reseau fait un geste voisin s'il a trop de capacite et trop peu de diversite. La **generalisation**, c'est reussir sur des cas nouveaux issus du meme phenomene - pas reinventer le monde, mais ne pas coller au bruit du train.

Ines regarde deux courbes. Train plonge. Val remonte. Elle n'ajoute pas de neurones. Elle regularise, arrete tot, ou collecte mieux.

## Remedes courants

Plus de donnees reelles. **Data augmentation** (surtout vision), avec prudence. **Dropout** (eteindre des neurones au hasard pendant l'entrainement). Weight decay / regularisation. **Early stopping** (arreter quand la validation n'ameliore plus). Architectures plus petites. **Transfer learning** plutot que from scratch. Label smoothing parfois. Et toujours : protocole de validation honnete, set de test rarement touche.

:::astuce
Liste tes remedes realistes "cette semaine" separement de tes remedes "un jour". L'action bat la wishlist.
:::

## Courbes a surveiller

Loss train, loss val, metrique metier val. Si train plonge et val remonte : stop / regularise. Si les deux restent hauts : underfitting, ou donnees insuffisantes / mal alignees, ou bugs. Apprends a lire ces courbes comme un medecin lit une tension. Lea demande a ses prestataires des captures de courbes, pas seulement un score final.

## Generalisation dans le vrai monde

Meme avec une belle courbe, le deploiement peut casser si les photos changent (eclairage, telephone), si la langue change, si les utilisateurs detournent. Surveille. Recolte des cas d'echec. Reentraine. Le deep learning n'annule pas la boucle ML : il l'intensifie. Max a vu un modele de "defaut visible" rate tous les defauts sous LED froide : le train etait sous LED chaude. Overfitting au contexte, pas seulement aux labels.

## Petite histoire

Sam a donne a sa classe un mini-jeu : 20 images, gros reseau, score train 100 %. Puis 5 images legerement differentes : catastrophe. Ensuite : modele plus petit + transfer + early stopping. Moins spectaculaire. Plus honnete. La classe a retenu. Chez DanielCraft, on garde cette pedagogie : faire sentir la claque avant de vendre le remede.

## Erreur classique

Augmenter la taille du modele des que ca coince. Autre piege : data augmentation absurde qui change le label. Troisieme : retoucher le test jusqu'a ce qu'il "marche" - tu overfitte alors au test lui-meme.

:::attention
Ne touche pas au test final comme a un joystick. Sinon tu perds ton juge impartial.
:::

## En vrai

Ouvre (ou imagine) une courbe train/val. Ecris en une phrase ce que tu ferais a l'epoch ou val stagne. Si ta phrase est "encore 50 epochs", recommence.

## A toi

Liste 4 remedes anti-overfitting applicables a ton idee de projet. Lesquels sont realistes cette semaine ? Encadre-les.

## Capacite et humilite

Un petit modele qui generalise un peu est parfois preferable a un grand modele qui memorise. En 2026, la tentation du "plus gros" est partout. Ton avantage, apres ce chapitre, c'est de savoir dire non. Ines l'ecrit sur un post-it au-dessus de son ecran : "val d'abord".

## Dropout et weight decay (intuition)

Dropout : pendant l'entrainement, tu "eteins" des neurones au hasard pour eviter que le reseau compte trop sur une co-adaptation fragile. Weight decay : tu penalises des poids trop gros, ce qui freine la memorisation excessive. Ce ne sont pas des sortileges. Ce sont des freins. Lea demande lesquels sont actifs avant d'accepter un score. Early stopping reste souvent le frein le plus simple et le plus oublie.

## Overfitting au protocole

Tu peux aussi overfitter au test en le regardant trop souvent, ou a une augmentation absurde, ou a un seul telephone. Elargis la notion : ce n'est pas seulement train vs val. C'est tout ce qui fait coller a un artefact au lieu du phenomene. Chez DanielCraft, on appelle ca "generaliser au vrai usage", pas au dossier du jour.
