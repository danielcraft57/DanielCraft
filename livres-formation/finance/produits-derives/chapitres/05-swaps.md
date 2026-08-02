# Chapitre 5 - Swaps : echange de flux

Un **swap** est un contrat entre deux parties pour **echanger des flux financiers** sur une duree definie, selon des regles fixees au depart. Le cas le plus connu en initiation est le **swap de taux** : une partie paie un taux **fixe**, l'autre un taux **variable** (souvent indexe sur Euribor ou SOFR), calcule sur un **montant notionnel**. Le notionnel sert au calcul des interets ; en general, on n'echange pas le notionnel entier a la fin, seulement les ecarts de coupons.

Ce livre est pedagogique. Les swaps sont surtout utilises par entreprises et institutions ; le retail les croise rarement directement, mais les comprendre eclaire les produits structures et la gestion de taux.

Nora a entendu "swap" dans un journal economique. Max confond swap et echange de devises au bureau de change. Sam, qui a un pret variable, se demande si un swap la concerne. DanielCraft clarifie sans jargon de salle de marche.

## Intuition : fixer ou liberer un taux

Imagine une entreprise qui emprunte 10 MEUR en **taux variable** : elle paie Euribor + 1 % chaque trimestre. Si les taux montent, sa facture monte. Elle peut conclure un swap : elle paie **2,5 % fixe** au swap counterparty et recoit en echange le **taux variable** sur 10 MEUR. Economiquement, elle a transforme une dette variable en dette synthetique fixe (simplification pedagogique). Si les taux montent, le swap compense une partie de la hausse ; si les taux baissent, elle "rate" la baisse sur la jambe fixe.

Ce n'est pas gratuit : le taux fixe du swap reflete les anticipations du marche au moment de la signature. Ce n'est pas une assurance sans cout.

## Exemple chiffre simplifie (taux fixe vs variable)

Montant **notionnel** N = 1 000 000 EUR (invente).
Swap 1 an, paiements annuels (tres simplifie).

- Partie A paie **fixe 3 %** : flux fixe = 0,03 x 1 000 000 = **30 000 EUR**
- Partie B paie **variable** : si taux variable = 2,2 %, flux var = **22 000 EUR**

A la fin de la periode, on **nettoie** souvent : la difference (30 000 - 22 000 = 8 000 EUR) est payee par B a A (selon conventions exactes). L'annee suivante, si le variable monte a 4 %, flux var = 40 000 EUR : A paie 30 000, B paie 40 000, net = 10 000 EUR de B vers A (sens inverse).

Sam ecrit : "Le notionnel sert a calculer, pas a se transferer en bloc." C'est une source de confusion frequente.

## Autres swaps (mention rapide)

- **Swap de devises** : echange de flux en EUR contre USD (couverture de change).
- **Swap sur indice actions (total return)** : echange rendement indice contre taux fixe.

Le retail voit surtout l'effet de ces produits **emballes** dans des obligations structurees ou des contrats pro. L'intuition reste : echange de flux futurs incertains contre certains ou inversement.

## Swap vs future vs option

- **Future** : prix fixe a l'avance pour livrer/acheter un sous-jacent a T.
- **Option** : droit asymetrique, prime payee.
- **Swap** : serie de flux futurs echanges, souvent sans date unique de "livraison" du sous-jacent.

Les trois sont des derives ; les cartes de risque different.

## Petite histoire

Max lit "la banque a swappe son dette". Il imagine un echange de sacs d'argent. En relisant l'exemple 30 000 / 22 000, il comprend : c'est un **echange de coupons**, pas un pret entre voisins. Il note dans son carnet DanielCraft : "Qui paie fixe, qui paie variable, sur quel notionnel ?"

## Erreur classique

Croire que le notionnel doit etre possede ou rembourse en une fois. Ou penser qu'un swap "elimine" tout risque de taux sans lire le taux fixe negocie. Ou confondre swap OTC (sur mesure, risque de contrepartie) et produits cotes.

## En vrai

Cherche "swap de taux definition AMF" ou fiche Banque de France. Note en une phrase : jambe fixe, jambe variable, notionnel.

## A toi

N = 500 000 EUR, fixe 2,8 %, variable 3,5 % (une periode). Calcule les deux flux et le net paye par qui.

:::retenir
Swap = echange de flux (souvent fixe vs variable) sur un notionnel. Le notionnel sert au calcul des interets.
:::

:::attention
Swaps OTC : risque de contrepartie si l'autre partie fait defaut. Niveau institutionnel surtout.
:::

:::astuce
Trois mots a noter : notionnel, jambe fixe, jambe variable. Si tu ne peux pas les definir, ne signe pas de produit "structure".
:::
