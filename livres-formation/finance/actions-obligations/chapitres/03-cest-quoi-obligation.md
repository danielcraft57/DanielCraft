# Chapitre 3 - C'est quoi une obligation ?

Une **obligation** est un titre de dette. L'emetteur (Etat, entreprise) emprunte de l'argent. Toi, tu lui pretes. En echange, tu recois en general des **coupons** (interets) et, a l'echeance, le **nominal** (le capital rembourse), sauf defaut. Chez DanielCraft, on dit : l'obligation, c'est un pret emballe, pas un livret magique.

Ce livre est pedagogique. Les exemples sont inventes. Ce n'est pas un conseil personnalise.

## Les trois mots a tatouer

- **Nominal** (ou face) : le montant de reference, souvent 100 ou 1 000 EUR.
- **Taux de coupon** : le pourcentage applique au nominal pour calculer le coupon.
- **Echeance** : la date de remboursement du nominal.

Formule du coupon annuel :

Coupon annuel = Nominal x Taux de coupon

Exemple :
- Nominal = 1 000 EUR
- Taux coupon = 3 %

Coupon annuel = 1 000 x 0,03 = 30 EUR

Si le coupon est verse une fois par an, tu recois 30 EUR chaque annee jusqu'a l'echeance (sauf defaut).

## Prix de marche vs nominal

Le prix de l'obligation sur le marche secondaire n'est pas toujours egal au nominal. Si les taux du marche montent apres emission, les anciennes obligations a coupon faible deviennent moins attractives : leur **prix baisse**. Si les taux baissent, leur prix monte souvent.

Exemple invente :
- Obligation A : nominal 100, coupon 2 %, reste 5 ans.
- Nouveaux taux du marche : 4 %.

Personne n'achatera A a 100 si on peut avoir 4 % ailleurs. Le prix de A doit baisser pour que le rendement global (coupons + "pull to par") redevienne competitif. Nora note : "mon coupon reste 2 EUR pour 100 de nominal, mais si j'ai achete a 92, mon rendement effectif n'est plus 2 %."

## Yield to maturity (YTM) : intuition

Le **YTM** (taux actuariel a l'echeance) est le rendement annualise que tu obtiens si :
1. tu achetes au prix actuel,
2. tu touches tous les coupons,
3. tu es rembourse au nominal a l'echeance,
4. tu reinvestis les coupons au meme taux (hypothese).

Approximation pedagogique (YTM approche) :

YTM approx = [C + (F - P) / n] / [(F + P) / 2]

avec :
- C = coupon annuel
- F = nominal (face)
- P = prix actuel
- n = annees restantes

Exemple :
- C = 30, F = 1 000, P = 950, n = 5

YTM approx = [30 + (1 000 - 950) / 5] / [(1 000 + 950) / 2]
= [30 + 10] / 975
= 40 / 975
~ 4,10 %

Ce n'est pas le YTM exact (qui resout une equation de prix), mais c'est assez bon pour comprendre : prix sous le pari => rendement > coupon.

## Petite histoire

Sam voit "obligation 5 %" et croit gagner 5 % sur son cash. En realite, le prix cote 108 : il paie une prime. Son YTM est plus bas que 5 %. Il apprend a lire prix + coupon + echeance, pas le seul chiffre marketing.

## Erreur classique

Confondre taux de coupon et rendement reel. Ou croire qu'une obligation ne peut jamais baisser. Ou ignorer le **risque de credit** (l'emetteur peut defaillir).

## En vrai

Sur une fiche obligataire ou un ETF obligations, cherche : coupon, maturite moyenne, duration, notation credit. Si une ligne manque, c'est un signal orange.

## A toi

Inventer une obligation : nominal 100, coupon 2,5 %, prix 97, n = 4. Calcule coupon annuel et YTM approx. Ecris une phrase : "je gagne surtout grace a ...".

:::retenir
Obligation = pret. Coupon = interet. Prix et taux du marche bougent a l'envers.
:::

:::attention
Coupon fixe ne veut pas dire prix fixe sur le marche secondaire.
:::

:::astuce
Toujours noter le trio : prix / coupon / echeance avant de juger "interessant".
:::
