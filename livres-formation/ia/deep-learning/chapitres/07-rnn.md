# Chapitre 7 - RNN : sequences dans le temps (overview)

Les **RNN** (Recurrent Neural Networks) ont ete concus pour les **sequences** : texte, audio, series temporelles. Idee : traiter un element a la fois en maintenant un **etat memoire** qui resume le passe. Chaque nouveau mot (ou mesure) met a jour la memoire, puis on predit. C'est l'intuition "le contexte voyage dans le temps".

Chez DanielCraft, on en parle en overview : utile pour l'histoire du NLP et pour certaines taches sequentielles, pas comme le reflexe 2026 par defaut sur le langage generatif massif. Les **transformers** ont souvent pris le dessus a grande echelle. Comprendre les RNN t'evite quand meme de croire que le texte n'est qu'un sac de mots.

:::retenir
RNN = etat qui se met a jour a chaque pas de la sequence. Intuition pedagogique forte ; dominance transformers sur beaucoup de taches langage modernes.
:::

## Ce que ce n'est pas

Ce n'est pas une comprehension humaine du recit. Ce n'est pas non plus "obsolete donc inutile a connaitre" : l'intuition reste, et des variantes / hybrides existent encore. Ce n'est pas le meilleur choix automatique en 2026 pour un chatbot ou un resume long : un modele preentraine transformer resoudra souvent mieux, plus vite a l'usage.

Tu lis un journal de bord ligne apres ligne. Tu gardes en tete un resume. Chaque nouvelle ligne modifie le resume. A la fin, tu classes ou tu predits la suite. Le RNN fait un geste voisin, en vecteurs. Sur les longues sequences, les RNN simples oublient ou deviennent instables : gradients qui disparaissent ou explosent. Des variantes (**LSTM**, **GRU**) ont ameliore la memoire. Puis l'attention des transformers a change la donne en permettant de relier des positions plus directement, et de mieux paralleliser sur GPU.

:::astuce
Quand tu entends "sequence", demande : qu'est-ce qui depend du passe recent ? du passe lointain ? du futur (attention au split temporel) ?
:::

## Ou les situer en 2026

Pour le langage generatif massif : transformers. Pour comprendre l'histoire du NLP et certaines taches sequentielles legeres : utile. Pour l'audio et la parole, des architectures mixtes existent. Pour les series temporelles industrielles : parfois RNN/LSTM, parfois modeles statistiques, parfois transformers temporels. La lecon transversale : respecter le temps dans le split (pas de futur qui fuit dans le passe), et evaluer sur des periodes realistes.

## Petite histoire

Lea a herite d'un vieux notebook 2017 "RNN pour classer des tickets". Ca marchait mediocrement. Elle a remplace par un modele texte preentraine + une tete simple. Gain net, moins de maintenance. Max, lui, regarde des series de temperature de four : la, une approche sequentielle classique + regles metier reste pertinente. Sam insiste : choisir selon le probleme, pas selon la date du tutoriel.

## Erreur classique

Choisir un RNN parce qu'un tutoriel de 2017 le dit, alors qu'un modele preentraine transformer resoudrait mieux ton cas texte. Autre piege : croire qu'une memoire recurrente egale une comprehension. Troisieme : splitter une serie temporelle au hasard comme un CSV iid, et laisser le futur contaminer le passe.

:::attention
Le temps n'est pas une feature comme une autre. Fuite temporelle = illusion de performance.
:::

## En vrai

Donne un exemple de sequence dans ton metier : logs, phrases, mesures, messages clients. Entoure ce qui depend du passe recent. Une fleche suffit.

## A toi

Ecris ton exemple de sequence. Qu'est-ce qui depend du passe recent ? Du passe lointain ? Comment splitterais-tu train / validation dans le temps ?

## Series temporelles

Predire la demande, detecter une anomalie sur un capteur : le deep learning n'est pas obligatoire. Parfois un modele statistique simple + seuil metier gagne. Parfois un LSTM aide. Parfois un transformer temporel. Ines note dans son carnet : "sequence oui, deep learning peut-etre". Cette prudence est un acquis du livre.

## Pont vers les transformers

Le chapitre suivant remplace l'etat qui avance pas a pas par une idee d'**attention** : chaque position peut regarder les autres et ponderer. Tu garderas l'intuition sequence ; tu changeras surtout le mecanisme. Chez DanielCraft, on enseigne les RNN comme un pont, pas comme une destination forcee.

## LSTM / GRU en une image

Imagine une memoire avec des portes : quoi ecrire, quoi oublier, quoi lire. Les LSTM et GRU ont ajoute ce genre de controle pour mieux tenir sur des sequences plus longues que les RNN naifs. Tu n'as pas a coder les portes. Tu retiens : on a tente de soigner la memoire avant que l'attention des transformers ne propose un autre chemin, plus parallelisable.

## Split temporel : scene concrete

Max a des releves horaires. S'il melange hier et demain dans le train au hasard, le modele "voit" le futur. Score magique, deploiement mediocre. Regle : entrainer sur le passe, valider sur une periode plus recente non vue, tester plus tard encore. Chez DanielCraft, cette hygiene temporelle compte autant que le choix RNN vs autre.
