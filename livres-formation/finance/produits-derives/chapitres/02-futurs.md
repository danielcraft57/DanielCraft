# Chapitre 2 - Les futurs (futures)

Un **future** (contrat a terme negocie) est un engagement ferme : tu t'engages a acheter ou vendre une quantite definie d'un sous-jacent a un **prix fixe** (F0) a une **date d'echeance** (ou a la livrer selon les regles du marche). Contrairement a une option, tu n'as pas le "droit de ne rien faire". Si tu es acheteur (long), tu profites quand le prix monte. Si tu es vendeur (short), tu profites quand le prix baisse. C'est un outil puissant, souvent leve par la **marge**.

Ce livre est pedagogique. Il ne remplace ni un conseiller agree, ni un banquier. Les exemples sont inventes. Les futurs comportent un **risque de perte en capital**, y compris une perte superieure au depot de marge si le marche bouge fort contre toi.

Nora, Max et Sam n'ont pas l'intention de devenir pit traders. Ils veulent comprendre ce que signifie "long future CAC" quand ils lisent la presse ou qu'un ami en parle.

## Mecanisme en une phrase

A l'ouverture, tu fixes un prix F0. A l'echeance (ou a la cloture), le prix de reglement est P_T. Si tu es **long** (acheteur de future), ton profit par contrat est approximativement :

Profit long = (P_T - F0) x Multiplicateur

Le **multiplicateur** convertit le mouvement de prix en euros. Sur un indice, il peut etre 10 EUR par point. Sur une matiere premiere, il depend du contrat (barils, onces, tonnes).

Si tu es **short** (vendeur de future) :

Profit short = (F0 - P_T) x Multiplicateur

## Exemple chiffre invente

Max simule un future sur un indice. Donnees :

- F0 = 7 500 (prix du future a l'ouverture)
- Multiplicateur = 10 EUR par point
- Position : long 1 contrat
- A l'echeance, P_T = 7 650

Profit = (7 650 - 7 500) x 10 = 150 x 10 = **+1 500 EUR**

Si P_T = 7 350 :

Profit = (7 350 - 7 500) x 10 = -150 x 10 = **-1 500 EUR**

Max n'a pas "investi" 7 500 EUR. Il a depose une **marge** bien plus petite. C'est la que le levier entre en jeu : un petit depot controle une grande exposition.

## Marge initiale : intuition

Pour ouvrir une position future, tu depose une **marge initiale** aupres de la chambre de compensation ou du courtier. Ce n'est pas le prix total du sous-jacent. C'est un **garantie** partielle. Si ta position perd de l'argent, la marge est debitee. Si elle tombe sous un seuil (**marge de maintenance**), tu recois un **appel de marge** : tu dois reconstituer le compte ou ta position est liquidee.

Exemple simplifie :

- Marge initiale = 3 000 EUR
- Perte journaliere = -800 EUR
- Solde marge = 2 200 EUR

Si la marge de maintenance est 2 500 EUR, tu es en deficit. Le courtier te demande au moins 300 EUR sous 24 h, sinon liquidation automatique. Nora lit ce scenario et note : "Je peux perdre plus vite que je ne peux remplir mon compte courant."

## Futur vs achat d'action

Acheter une action, c'est payer le prix plein (sans levier). Acheter un future, c'est t'engager sur une exposition large avec peu de capital immobilise. Le future **standardise** aussi : meme echeance, meme taille de contrat, liquidite sur les marches organises. Les entreprises l'utilisent pour se couvrir ; les speculators pour parier. DanielCraft insiste : le meme produit, deux intentions tres differentes.

## Petite histoire

Sam lit qu'un "trader a gagne 40 % en une semaine sur le petrole". Elle calcule avec les chiffres de ce chapitre : +40 % sur quoi ? Sur la marge ou sur le capital total ? Si marge = 5 000 et gain = 2 000, c'est +40 % sur la marge, mais 2 000 EUR absolus. Si le meme trade avait ete -40 %, elle aurait perdu 2 000 EUR et peut-etre recu un appel de marge. Elle ferme l'article et garde son plan : comprendre d'abord, ne pas copier.

## Erreur classique

Confondre le prix du future F0 et le prix spot du sous-jacent. Ils sont proches mais pas identiques (cout de portage, taux, dividendes). Autre piege : croire que la marge initiale = perte max. Sur un future, la perte max n'est pas bornee par la marge si tu ne coupes pas la position.

## En vrai

Cherche une fiche de contrat future (Eurex, CME, ou fiche pedagogique AMF). Note multiplicateur, marge initiale indicative, echeance. Calcule le P&L pour un mouvement de -3 % du sous-jacent en supposant un multiplicateur donne.

## A toi

Sur papier : F0 = 100, multiplicateur = 50, long 1 contrat. Calcule le profit si P_T = 108, puis si P_T = 94. Ecris la perte en EUR et en % de marge si marge = 500 EUR.

:::retenir
Future = engagement ferme. Profit long = (P_T - F0) x multiplicateur. Marge initiale != perte max.
:::

:::attention
Appel de marge et liquidation : tu peux perdre vite, plus que prevu si tu ne comprends pas le levier.
:::

:::astuce
Toujours calculer P&L en euros absolus, pas seulement en "points" de l'indice.
:::
