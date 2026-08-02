# Chapitre 14 - Atelier : call et put sur papier

Atelier corrige. Entreprise fictive **Voltex** cotee 36 EUR. Tu calcules payoffs et profits sans plateforme. Pas d'ordre en vrai.

Ce livre est pedagogique. Les chiffres sont inventes pour l'exercice.

## Donnees

- S (aujourd'hui) = 36 EUR
- Echeance T = dans 3 mois (on raisonne a T)
- Call europeen K=40, prime payee = 1,20 EUR
- Put europeen K=34, prime payee = 0,90 EUR

Nora achete 100 calls. Max achete 100 puts "pour voir". Sam detient 100 actions Voltex a 36 et simule un protective put K=34 a 0,90.

## Partie A : long call (100 contrats)

Prime totale = 1,20 x 100 = **120 EUR** (cout max).

| S a T | Payoff unitaire max(S-K,0) | Profit total (x100) - 120 |
|-------|---------------------------|---------------------------|
| 30 | 0 | -120 |
| 38 | 0 | -120 |
| 40 | 0 | -120 |
| 42 | 2 | +80 |
| 46 | 6 | +480 |
| 50 | 10 | +880 |

Breakeven unitaire = K + prime = 40 + 1,20 = **41,20 EUR**.

Nora : "Il faut finir au-dessus de 41,20, pas 40."

## Partie B : long put (100 contrats)

Prime totale = 0,90 x 100 = **90 EUR**.

| S a T | Payoff max(K-S,0) | Profit total |
|-------|-------------------|--------------|
| 28 | 6 | +510 |
| 32 | 2 | +110 |
| 34 | 0 | -90 |
| 36 | 0 | -90 |
| 40 | 0 | -90 |

Breakeven = 34 - 0,90 = **33,10 EUR**.

Max : "Je gagne si Voltex s'effondre sous 33,10, pas sous 34."

## Partie C : protective put (Sam, 100 actions)

Detient 100 actions a 36 EUR (3 600 EUR). Achete put K=34, prime 0,90.

A T, S=28 :

- Perte action = (28-36) x 100 = -800
- Gain put = (34-28) x 100 = +600
- Prime = -90
- **Net ~ -290 EUR** (vs -800 sans put)

A T, S=42 :

- Gain action = +600
- Put expire 0
- Prime -90
- **Net ~ +510 EUR**

Sam ecrit : "Le put a coute 90 EUR d'assurance. Plancher effectif approx 33,10."

## Corrige express (questions guides)

1. Call : profit max a S=46 ? **+480 EUR**
2. Put : perte max ? **-90 EUR** (100 % prime)
3. Protective put a S=32 ? Net action+put = (32-36)*100 + (34-32)*100 - 90 = -400 + 200 - 90 = **-290 EUR**

## Petite histoire

Max voulait "acheter le call parce que c'est cheap OTM". L'atelier lui montre : a 38 EUR, perte 100 % de la prime. Il note "cheap ≠ bon odds". DanielCraft : l'atelier juge la clarte.

## Erreur classique

Oublier de soustraire la prime totale (x100). Confondre strike et breakeven.

## A toi

Recalcule la ligne S=42 pour le call et S=28 pour le put sans regarder. Puis ajoute une ligne S=41 pour le protective put de Sam.

:::retenir
Atelier = tableaux payoff x quantite - prime totale. Breakeven call = K+P, put = K-P.
:::

:::attention
100 contrats x prime = cout reel en EUR. Ne pense pas "juste 1,20 EUR".
:::

:::astuce
Garde ce modele de tableau pour tout nouveau call/put regarde sur une fiche produit.
:::
