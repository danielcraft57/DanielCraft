# Chapitre 3 - Options : call et put

Une **option** est un contrat qui donne a l'acheteur le **droit**, mais pas l'obligation, d'acheter ou de vendre un sous-jacent a un prix fixe (**strike K**) jusqu'a une **echeance** T. L'acheteur paie une **prime** au vendeur pour obtenir ce droit. Deux types :

- **Call** : droit d'**acheter** le sous-jacent au strike K.
- **Put** : droit de **vendre** le sous-jacent au strike K.

Ce livre est pedagogique. Les exemples sont inventes. Acheter ou vendre des options comporte un **risque de perte** ; vendre des options nue peut exposer a des pertes tres superieures a la prime encaissee.

Nora decouvre les options via un podcast. Max via une pub de courtier. Sam via un client qui "se couvre". DanielCraft les ramene au meme socle : call, put, strike, prime, payoff.

## Call : parier a la hausse avec perte limitee (acheteur)

Tu achetes un **call** si tu anticipes une hausse du sous-jacent S. A l'echeance, tu exerces si S > K : tu achetes a K alors que le marche vaut S. Sinon, tu laisses expirer : ta perte max est la **prime** payee.

Payoff a l'echeance pour un **long call** (par action, avant prime) :

Payoff call = max(S - K, 0)

Profit net = max(S - K, 0) - Prime

## Put : parier a la baisse ou se proteger

Tu achetes un **put** si tu anticipes une baisse, ou si tu detiens le sous-jacent et veux une assurance. A l'echeance, si S < K, tu vends a K. Payoff put :

Payoff put = max(K - S, 0)

Profit net = max(K - S, 0) - Prime

## Exemple numerique : long call

Donnees inventees :

- S (aujourd'hui) = 42 EUR
- Call, strike K = 40 EUR
- Prime payee = 2,50 EUR
- Echeance dans 2 mois

A l'echeance, scenario A : S = 48 EUR

Payoff = max(48 - 40, 0) = 8 EUR
Profit = 8 - 2,50 = **+5,50 EUR** par action

Scenario B : S = 38 EUR

Payoff = max(38 - 40, 0) = 0
Profit = 0 - 2,50 = **-2,50 EUR** (perte max = prime)

Scenario C : S = 41 EUR

Payoff = max(41 - 40, 0) = 1 EUR
Profit = 1 - 2,50 = **-1,50 EUR** (le sous-jacent a monte, mais pas assez pour couvrir la prime)

Nora note : "Il faut depasser K + prime pour etre gagnant sur un call achete."

## Exemple numerique : long put

Meme sous-jacent, put K = 42 EUR, prime = 1,80 EUR.

Scenario : S = 35 EUR a l'echeance

Payoff = max(42 - 35, 0) = 7 EUR
Profit = 7 - 1,80 = **+5,20 EUR**

Scenario : S = 45 EUR

Payoff = 0, profit = **-1,80 EUR**

Sam compare : le put protege contre une chute sous 42, mais coute 1,80 comme une assurance. Si le marche monte, l'assurance "expire sans sinistre".

## Acheteur vs vendeur d'options

L'**acheteur** paie la prime, risque limite (pour un acheteur pur). Le **vendeur** (writer) encaisse la prime et prend l'obligation inverse : s'il vend un call, il doit livrer si l'acheteur exerce ; s'il vend un put, il doit acheter. Le vendeur peut perdre bien plus que la prime. Ce livre ne pousse pas la vente nue d'options : c'est un niveau de risque pro.

## Petite histoire

Max voit "call a 0,10 EUR, gain illimite !". Il calcule : 0,10 EUR x 100 actions = 10 EUR de prime. Si le sous-jacent stagne, il perd 100 % de sa mise. Si le sous-jacent monte de 1 %, le call peut rester worthless. Il ecrit : "Pas illimite pour moi : perte max 10 EUR, gain seulement si gros mouvement." Il ne clique pas. DanielCraft valide.

## Erreur classique

Acheter un call OTM (hors de la monnaie) parce que la prime est "cheap", sans calculer le breakeven K + prime. Ou croire qu'un put achete sur une action que tu ne detiens pas est une "couverture" : c'est une speculation directionnelle.

## En vrai

Sur une plateforme demo ou une fiche pedagogique, repere un call et un put sur le meme sous-jacent et meme echeance. Note K, prime, S. Calcule le profit pour S +10 % et S -10 %.

## A toi

Call K=50, prime=3. Calcule profit pour S=55, S=50, S=45. Puis put K=50, prime=2,5 pour S=45 et S=55.

:::retenir
Call = droit d'acheter. Put = droit de vendre. Long option : perte max souvent = prime. Profit call = max(S-K,0) - prime.
:::

:::attention
Vendre des options nue : risque de perte potentiellement illimite (call) ou tres large (put).
:::

:::astuce
Breakeven call achete = K + prime. Breakeven put achete = K - prime.
:::
