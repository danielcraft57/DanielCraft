# Chapitre 10 - Duration et convexite

La **duration** mesure la sensibilite du prix d'une obligation aux taux. Dit simplement : si les taux montent, le prix des obligations existantes baisse souvent ; si les taux baissent, le prix monte souvent. Plus la duration est longue, plus le choc est fort. Chez DanielCraft, on l'utilise comme radar, pas comme oracle.

Disclaimer : approximations pedagogiques. Pas un conseil.

## Duration modifiee : formule utile

Approximation au premier ordre :

Variation du prix (%) ~ - D_mod x Delta y

avec Delta y en decimal (1 % = 0,01) ou, si D_mod est exprime "par point de pourcentage", Delta y en points (1 pour 1 %).

Exemple clair (Delta y en %) :
- D_mod = 5
- Hausse des taux = +1 point

Variation ~ -5 x 1 % = -5 %

Si le prix etait 100, estimation ~95. Ce n'est pas exact au centime, mais ca evite de croire que "obligation = stable a 0 %".

## Pourquoi certaines obligations bougent plus

Toutes choses egales par ailleurs :
- maturite plus longue => duration plus elevee
- coupon plus faible => duration plus elevee (plus de poids sur le nominal lointain)
- un zero-coupon a une duration egale a sa maturite (cas simple)

Exemple de lecture :
- Fonds A : duration 2 => choc taux +1 % ~ -2 %
- Fonds B : duration 8 => choc +1 % ~ -8 %

Nora, horizon 2 ans, refuse B pour sa poche "presque sure". Max, horizon 10 ans et estomac solide, peut accepter une duration plus haute dans une poche clairement separee.

## Convexite : la correction au second ordre

La relation prix / taux n'est pas une droite. La **convexite** corrige l'erreur de la duration seule :

Variation (%) ~ - D_mod x Delta y + 0,5 x Convexite x (Delta y)^2

Exemple pedagogique :
- D_mod = 5
- Convexite = 40 (ordre de grandeur invente pour l'exo)
- Delta y = +0,01 (soit +1 %)

Terme duration : -5 x 0,01 = -0,05 = -5 %
Terme convexite : 0,5 x 40 x (0,01)^2 = 20 x 0,0001 = 0,002 = +0,2 %

Variation estimee ~ -4,8 %

Sur une hausse de taux, la convexite positive "adoucit" un peu la baisse estimee par la seule duration. Sur une baisse de taux, elle ajoute un peu de hausse. L'idee : la duration seule exagere souvent la baisse et sous-estime un peu la hausse (pour une obligation a convexite positive classique).

## Petite histoire

Sam lit "rendement 4,2 %" sur un ETF obligataire. Duration 7,2. Il simule +2 % de taux : ~ -14 % avant convexite. Il decide de reduire la poche ou d'allonger son horizon. Le chiffre l'a calme plus qu'un reel "rates are dead".

## Erreur classique

Confondre duration et "je suis rembourse dans X annees" sans lire la sensibilite. Ou empiler des obligations longues pour "booster le rendement" sans buffer de volatilite. Ou ignorer le risque credit en ne regardant que la duration.

## Mini-exercice (corrige)

Prix = 102, D_mod = 6, Delta y = -0,5 % (baisse des taux).

Variation ~ -6 x (-0,5 %) = +3 %

Prix estime ~ 102 x 1,03 = 105,06

Ajoute une convexite 30 et Delta y = -0,005 :
0,5 x 30 x (0,005)^2 = 15 x 0,000025 = 0,000375 ~ +0,04 %
Effet faible ici : la duration domine sur un petit mouvement.

## En vrai

Sur une fiche ETF obligations : duration modifiee, sensibilite, maturite moyenne, notation. Si duration absente, signal orange.

## A toi

Ecris ta baisse max acceptable (ex. -5 %). Deduits une duration max approx (si +1 % de taux te fait peur a -5 %, duration max ~ 5). Garde ce plafond sur une feuille.

:::retenir
Duration = radar de sensibilite aux taux. Convexite = correction fine, pas une excuse pour ignorer le risque.
:::

:::attention
Une obligation peut baisser nettement meme avec un coupon regulier.
:::

:::astuce
Pour chaque fonds obligataire, note "choc +1 %" = -duration % avant d'augmenter la poche.
:::
