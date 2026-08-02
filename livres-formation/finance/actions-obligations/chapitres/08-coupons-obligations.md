# Chapitre 8 - Coupons et obligations : pricing simple

Une obligation, c'est une suite de cash-flows : coupons, puis nominal. Le **prix** theorique est la somme de ces flux **actualises** au taux du marche (YTM). Chez DanielCraft, on veut que tu saches faire un calcul pedagogique a la main, meme approximatif, avant de croire un ecran.

Disclaimer : exemples inventes. Pas un conseil d'achat.

## Formule de prix (coupons annuels)

P = somme de t=1 a n de [ C / (1+y)^t ] + F / (1+y)^n

avec :
- C = coupon annuel
- F = nominal
- y = taux actuariel (YTM) par an
- n = nombre d'annees

Exemple complet :
- F = 100
- Coupon = 5 % => C = 5
- n = 3 ans
- y = 5 % = 0,05

P = 5/1,05 + 5/1,05^2 + (5+100)/1,05^3
= 4,762 + 4,535 + 90,703
= 100,00

A parite : quand y = taux de coupon, le prix = nominal (cas annuel simple).

## Meme obligation, taux qui montent

Garde C = 5, F = 100, n = 3, mais y = 7 % = 0,07.

P = 5/1,07 + 5/1,07^2 + 105/1,07^3
= 4,673 + 4,367 + 85,722
= 94,76

Le prix baisse a ~94,76. Nora note : "mon coupon reste 5, mais la valeur de marche a baisse parce que le marche exige 7 %."

## Meme obligation, taux qui baissent

y = 3 % = 0,03.

P = 5/1,03 + 5/1,03^2 + 105/1,03^3
= 4,854 + 4,713 + 96,151
= 105,72

Prix ~105,72. Les anciennes obligations a 5 % deviennent rares / attractives : leur prix monte.

## Current yield vs YTM

Current yield = C / P

Sur l'exemple a y = 7 % (P ~ 94,76) :
Current yield = 5 / 94,76 ~ 5,28 %

Le YTM (~7 %) est plus haut que le current yield parce qu'il integre aussi le "chemin" vers le nominal a 100 (ici un gain en capital si tu tiens jusqu'a l'echeance).

YTM approx (rappel chapitre 3) :

YTM approx = [C + (F-P)/n] / [(F+P)/2]

= [5 + (100-94,76)/3] / [(100+94,76)/2]
= [5 + 1,75] / 97,38
= 6,75 / 97,38
~ 6,9 %

Proche de 7 %. Suffisant pour l'intuition.

## Petite histoire

Max achete une obligation "parce que le coupon est joli". Il ne regarde pas le prix (108). Apres une hausse de taux, le cours tombe a 99. Il panique. Sam lui rappelle : si son horizon etait l'echeance et le credit solide, le coupon continue ; la baisse de prix le touche surtout s'il revend maintenant. Horizon = decision.

## Erreur classique

Lire seulement le taux de coupon. Ou croire que "obligation = pas de baisse". Ou comparer deux YTM sans regarder la qualite de credit et la duration.

## Mini-exercice (corrige)

Obligation : F = 100, C = 4, n = 2, y = 6 %.

P = 4/1,06 + 104/1,06^2
= 3,774 + 92,560
= 96,33

Current yield = 4 / 96,33 ~ 4,15 %

## A toi

Refais le calcul avec y = 4 % (meme C, F, n). Le prix doit etre proche de 100. Verifie.

:::retenir
Prix obligataire = PV des coupons + PV du nominal. Taux monte => prix baisse (toutes choses egales).
:::

:::attention
YTM suppose detente jusqu'a echeance et reinvestissement des coupons : ce n'est pas une promesse de performance.
:::

:::astuce
Calcule toujours le prix a deux taux (ex. +1 % / -1 %) pour sentir la sensibilite avant d'acheter.
:::
