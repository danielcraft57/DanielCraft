# Chapitre 9 - Strategies simples (niveau debutant)

Ce chapitre presente quatre **strategies de base** avec payoffs chiffres. Pas de strangles, pas de iron condors : juste ce qu'il faut pour lire un ecran sans paniquer. Chaque strategie = une **carte de gain/perte** a l'echeance (options) ou a la cloture (actions + options).

Ce livre est pedagogique. Les exemples sont inventes. Combiner options ne supprime pas le risque ; certaines strategies (vente nue) sont exclues ici volontairement.

Nora veut proteger son PEA sans tout vendre. Max veut comprendre les tweets "covered call". Sam teste sur papier. DanielCraft : strategies simples, chiffres d'abord.

## 1. Long call (pari haussier, perte limitee)

Deja vu ch. 3. Acheter un call K, payer prime P.

Profit = max(S - K, 0) - P

Exemple : K=50, P=2, S=56 → profit = 6 - 2 = **+4**.

## 2. Long put (pari baissier ou assurance)

Acheter un put K, prime P.

Profit = max(K - S, 0) - P

Exemple : K=50, P=1,5, S=44 → profit = 6 - 1,5 = **+4,5**.

## 3. Covered call (action + vente de call)

Tu **detiens** l'action et tu **vends** un call OTM (strike au-dessus du cours). Tu encaisse la prime, tu limites ton gain au-dessus du strike.

Hypothese : 100 actions achetees a 48 EUR. Vente call K=52, prime 1,20 EUR/action.

A l'echeance :

- S ≤ 52 : tu gardes actions + prime 1,20. Dividendes eventuels en plus.
- S = 55 : tu es assigne, vends a 52. Gain actions = (52 - 48) x 100 = 400 EUR. Plus prime 120 EUR. Total **520 EUR**. Tu "rates" la hausse au-dela de 52.

Max note : "Je trade un peu de hausse future contre cash maintenant." Ce n'est pas neutre : si l'action s'effondre, la prime ne compense qu'une petite baisse.

## 4. Protective put (action + achat de put)

Tu **detiens** l'action et tu **aches** un put (assurance).

100 actions a 40 EUR. Put K=38, prime 1 EUR.

A l'echeance :

- S = 30 : put vaut 8, perte action -10, put +8, prime -1 → net action+put ~ -3 EUR/action vs -10 sans put.
- S = 50 : put expire 0, tu perds la prime 1, tu profite de la hausse actions.

Nora : "Assurance qui coute 1 EUR par action, plafond de douleur reduit sous 38."

## Comparaison rapide

| Strategie | Intention | Risque principal |
|-----------|-----------|------------------|
| Long call | Speculation hausse | Perte prime |
| Long put | Speculation baisse / hedge | Perte prime |
| Covered call | Revenu + plafond hausse | Baisse action non couverte |
| Protective put | Plancher sur baisse | Cout prime |

## Petite histoire

Sam voit "strategie zero risque covered call". Elle calcule : si l'action -30 %, la prime 1,20 ne sauve rien. Elle renomme mentalement : "revenu limite, pas zero risque." DanielCraft prefere ce renommage au slogan broker.

## Erreur classique

Faire un covered call sans detenir les actions (naked call = risque pro). Acheter protective put sur un montant d'actions disproportionne par rapport au cout cumule des primes. Enchainer strategies sans additionner les primes.

## En vrai

Dessine sur papier les 4 payoffs pour S de 30 a 60 avec les chiffres du chapitre. Une courbe par strategie.

## A toi

Covered call : 50 actions a 20 EUR, call K=22 prime 0,80. Calcule resultat total pour S=18, S=22, S=25.

:::retenir
Long call/put = paris directionnels a perte max prime. Covered call = prime + plafond hausse. Protective put = plancher sur baisse.
:::

:::attention
Vendre un call sans actions = risque potentiellement illimite. Hors niveau debutant.
:::

:::astuce
Additionne toujours prime x nombre d'actions pour voir le cout ou revenu en euros, pas en pourcentage flou.
:::
