# Chapitre 13 - A retenir

Tu as une carte. Pas un diplome de chercheur. Une carte. Le deep learning, ce sont des **reseaux a plusieurs couches** qui apprennent aussi des representations. Un **neurone** melange des entrees avec des poids, ajoute un biais, active. Les **couches** empilent des transformations. L'**activation** introduit le non-lineaire sans lequel la profondeur s'effondre. La **backprop** ajuste les poids a partir d'une erreur mesuree. Les **CNN** voient par filtres locaux. Les **RNN** portent une memoire sequentielle (overview utile). Les **transformers** misent sur l'attention, coeur de beaucoup de **LLM**. L'**overfitting** menace des que la capacite depasse le signal. Le **GPU** parallelise les matrices. Le **transfer learning** reutilise un cerveau deja forme. Les LLM sont du deep learning langage + alignement + usage (prompt, RAG, agents).

Chez DanielCraft, on resume autrement : matcher le probleme, reutiliser avant de reentrainer, mesurer sur le terrain, garder un humain quand le risque monte.

:::retenir
Carte DL : neurone -> couches -> activation -> backprop -> CNN / RNN / transformer -> overfitting -> GPU -> transfer -> LLM.
:::

## Ce que ce n'est pas

Ce n'est pas une checklist a reciter sans exemple. Ce n'est pas "tu peux tout deployer demain". Ce n'est pas non plus "le ML classique est mort". Sur un petit tableau, reviens au livre machine learning. Sur une image ou du langage riche, tu as maintenant les bons mots.

Tache claire -> assez de donnees / transfert -> architecture adaptee -> loss et metriques -> validation -> regularisation -> deploiement mesure -> surveillance. Prefere reutiliser avant de reentrainer le monde. Ines a cette boucle sur une feuille A4. Lea l'a collee dans ses briefs. Max l'a simplifiee en trois questions : "ca sert ?", "on mesure quoi ?", "si ca se trompe ?".

## Petite histoire

Sam demande a un eleve de tout raconter en deux minutes. L'eleve bloque sur backprop. Il relit le chapitre 5, recommence, passe. La carte n'est solide que si elle passe a l'oral. Chez DanielCraft, l'oral est le vrai test : si tu peux l'expliquer a un non-tech, c'est entre.

## Pont vers la pratique

Si tu utilises deja un chat : tu manipules un transformer aligne. Si tu classes des images : tu toucheras CNN / transfer. Si tu as un CSV : reviens au ML. La bonne stack est celle qui matche le probleme. Ines melange parfois vision (CNN) et doc utilisateur (LLM) : deux briques, un protocole de verification pour chacune.

## Erreur classique

Vouloir tout retenir comme une liste de courses sans scene concrete. Autre piege : passer aux ateliers sans avoir une tache personnelle en tete. Les ateliers collent mieux a ta vie si tu apportes ton probleme.

:::attention
Une carte sans exemple personnel devient du papier peint. Ajoute le tien.
:::

## En vrai

Ferme le livre (ou l'ecran). Sur une feuille blanche, reconstitue la carte en TES mots. Une seule face. Interdit de recopier les titres mot a mot : reformule.

## A toi

Carte mentale une page : un exemple vision et un exemple texte. Relie chaque boite a une decision que tu pourrais prendre cette semaine (meme minuscule).

## Anti-patterns a garder en tete

LLM pour classer trois categories sur un CSV de vingt colonnes. CNN from scratch avec quarante images. Agent autonome le jour 1. Transformer "parce que c'est moderne" la ou un modele simple suffit. Note tes anti-patterns personnels a cote de la carte.

## Suite immediate

Atelier intuition (neurone et couches), atelier plan CNN, atelier transformer / usage LLM, puis choix d'architecture, limites, bonnes pratiques, quiz. Tu n'empiles plus seulement des couches de neurones. Tu empiles des gestes. C'est le but.

## Checklist orale express

En moins de deux minutes : qu'est-ce qu'un neurone ? Pourquoi activer ? Comment apprend-on ? Pourquoi CNN sur image ? Pourquoi attention sur texte ? Qu'est-ce qui overfitte ? Pourquoi GPU ? Pourquoi transfer ? Lien LLM ? Si une case manque, tu sais ou revenir. Lea fait cette checklist avant chaque atelier client. Ines avant chaque demo.

## Ce que tu peux deja faire demain

Choisir une baseline simple sur un CSV. Planifier un transfer vision. Briefer un LLM avec faits et anti-invention. Dire non a un from scratch injustifie. Ces quatre gestes valent plus qu'une citation de papier. Chez DanielCraft, la carte sert a agir petit et juste.
