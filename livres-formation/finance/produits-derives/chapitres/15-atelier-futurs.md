# Chapitre 15 - Atelier : lire un future

Atelier corrige sur **future indice fictif Mini-Indice DC**. Tu lis une fiche contrat, calcules P&L et marge. Pas d'ordre reel.

Ce livre est pedagogique. Chiffres inventes, conventions simplifiees.

## Fiche contrat (inventee)

| Champ | Valeur |
|-------|--------|
| Sous-jacent | Indice DC 100 |
| Multiplicateur | 5 EUR / point |
| F0 (prix future ouverture) | 8 000 |
| Marge initiale | 4 000 EUR / contrat |
| Marge maintenance | 3 200 EUR |
| Position Max | Long 1 contrat |

Equity compte avant ouverture : **6 000 EUR** (Max garde 2 000 EUR en reserve non immobilisee).

## Question 1 : P&L a la cloture

Calcule profit long pour :

a) P_T = 8 120  
Profit = (8120 - 8000) x 5 = 120 x 5 = **+600 EUR**

b) P_T = 7 880  
Profit = (7880 - 8000) x 5 = -120 x 5 = **-600 EUR**

c) P_T = 7 600  
Profit = (7600 - 8000) x 5 = -400 x 5 = **-2 000 EUR**

## Question 2 : equity apres variation (sans appel)

Apres ouverture, marge immobilisee 4 000, reserve 2 000.

Apres (c) P_T = 7 600 intraday :

- P&L = -2 000
- Equity = 6 000 - 2 000 = **4 000 EUR**
- Marge maintenance = 3 200 → **pas d'appel** (4 000 > 3 200)

Apres chute supplementaire a P_T = 7 520 :

- P&L cumule = (7520 - 8000) x 5 = -2 400 EUR
- Equity = 6 000 - 2 400 = **3 600 EUR** → toujours OK

A P_T = 7 440 :

- P&L = (7440 - 8000) x 5 = -2 800 EUR
- Equity = **3 200 EUR** → **seuil maintenance**, appel de marge probable

A P_T = 7 360 :

- P&L = -3 200 EUR
- Equity = **2 800 EUR** < 3 200 → **appel** de au moins 400 EUR ou liquidation

Nora colore en rouge 7 360 sur sa fiche : "En 160 points, je suis en danger de liquidation."

## Question 3 : mouvement en % vs compte

Sous-jacent approx -2 % (8000 → 7840) :

P&L = -160 x 5 = -800 EUR sur equity 6 000 = **-13,3 % compte** avec une seule position "modest" en future.

Levier implicite sur marge : exposition = 8000 x 5 = 40 000 EUR (simplifie) vs marge 4 000 → 10x sur la marge.

## Question 4 : journal de bord (modele)

Max remplit :

"J'ai ouvert long 1 Mini-DC a 8000. Mon plan : couper si equity < 4 500 (-25 %). Choc -3 % indice = -1 200 EUR P&L. Je n'ajoute pas de marge pour rattraper."

Sam verifie : plan ecrit **avant** le trade fictif.

## Petite histoire

Max oublie la reserve 2 000 et croit qu'il n'a que 4 000 total. Il recalcule et voit qu'il confond marge et compte entier. DanielCraft : lire la fiche contrat ligne par ligne vaut plus qu'un clic.

## Erreur classique

Calculer P&L en points sans multiplier par 5. Oublier que l'equity inclut marge + cash libre selon broker.

## A toi

Recalcule (a) et (b) sans regarder. Puis trouve P_T ou equity tombe exactement a 3 000 EUR (liquidation zone).

Indice : profit = (P_T - 8000) x 5 = 6 000 - 3 000 = -3 000 → P_T - 8000 = -600 → **P_T = 7 400**.

:::retenir
P&L future = (P_T - F0) x multiplicateur. Compare equity a marge maintenance pour appel/liquidation.
:::

:::attention
-160 points peut etre -2 000 EUR. Les pourcentages "petits" sur l'indice ne le sont pas sur le compte.
:::

:::astuce
Toujours convertir points → EUR avant de juger si un mouvement est "supportable".
:::
