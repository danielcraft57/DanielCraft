# Chapitre 7 - Couverture vs speculation

Meme produit derive, deux intentions opposees :

- **Couverture (hedge)** : reduire un risque que tu **as deja** (prix, taux, change).
- **Speculation** : prendre un risque **directionnel** pour parier sur un mouvement, sans actif sous-jacent a proteger.

Le mecanisme est identique (future, option, swap). La difference est dans le **portefeuille de depart** et la **taille** par rapport a ton exposition reelle.

Ce livre est pedagogique. Meme une couverture bien pensee a un cout et peut echouer si mal calibree. La speculation levee comporte un risque de perte superieure a la mise.

Nora detient des actions long terme. Max vend du ble. Sam a un pret variable. Chacun peut utiliser un derive differemment. DanielCraft insiste : nommer son intention avant d'ouvrir.

## Couverture : exemple producteur

Max, invente, produit 100 tonnes de ble a recolter dans 4 mois. Prix spot aujourd'hui : 200 EUR/tonne. Il craint une chute a 170 EUR. Il vend un **future** sur 100 tonnes (simplifie) a 198 EUR.

Scenario A : a la recolte, spot = 170 EUR. Il vend son ble physiquement a 170, perte physique = -30 x 100 = -3 000 EUR. Gain sur future ~ (198 - 170) x 100 = +2 800 EUR. Perte nette attenuee ~ -200 EUR (moins frais, ecarts de base).

Scenario B : spot = 220 EUR. Ble physique rapporte +20 x 100 = +2 000. Future perd ~ (198 - 220) x 100 = -2 200. Net ~ -200 EUR aussi (couverture = stabilisation, pas maximisation).

Max n'a pas "gagne au trading" : il a **achete la tranquillite** sur son revenu agricole, avec un cout d'opportunite si les prix explosent.

## Speculation : exemple trader retail

Nora n'a pas de ble dans le jardin. Elle achete un future long sur indice "parce que ca va monter". C'est de la **speculation** : elle parie sur une direction sans risque sous-jacent a neutraliser. Sa perte max n'est pas bornee par la marge si elle ne coupe pas.

Sam distingue : "Max se couvre sur un actif qu'il possede. Nora parie. Les deux utilisent un future, mais la carte mentale n'est pas la meme."

## Couverture avec options

Detenir 100 actions a 40 EUR et acheter un **put** K=38, prime 1 EUR : c'est une couverture partielle (assurance contre chute sous 38, cout 1 EUR/action). Si le marche monte, tu participes moins la prime. Si le marche chute, le put compense une partie.

Acheter un put **sans** detenir l'action : speculation a la baisse, pas hedge.

## Ratio de couverture (intuition)

Couverture parfaite rare en retail. Questions utiles :

- Quelle fraction de mon exposition je couvre ?
- Quel cout (prime, ecart de future) ?
- Que se passe-t-il si le risque va dans l'autre sens ?

Une sur-couverture devient speculation inverse.

## Petite histoire

Un influenceur dit "hedge ton portefeuille avec des turbos !". Nora relit ce chapitre : elle n'a pas de portefeuille de 50 k EUR, elle a 200 actions en PEA. Un turbo leve n'est pas un hedge prudent, c'est un pari avec knockout. Elle note "hedge = reduire risque existant, pas multiplier par 10". DanielCraft : le mot hedge est abuse en marketing.

## Erreur classique

Se croire "investisseur prudent" en achetant des CFD leves "pour se proteger" sans actif sous-jacent. Ou couvrir a 200 % par peur et transformer un portefeuille calme en casino. Ou ignorer le cout de la couverture (prime, spread).

## En vrai

Liste un risque reel que tu as (taux variable, action detenue, devise). Pour chacun, note si un derive pourrait reduire ce risque et a quel cout approximatif. Si tu n'as aucun risque sous-jacent, tu es en mode speculation par definition.

## A toi

Ecris deux lignes : un cas ou la couverture a du sens pour toi, un cas ou ce serait de la speculation deguisee.

:::retenir
Hedge = reduire un risque deja la. Speculation = parier sans sous-jacent a proteger. Meme produit, intention differente.
:::

:::attention
Sans actif sous-jacent, un "put de protection" est un pari baissier, pas une assurance de portefeuille.
:::

:::astuce
Avant d'ouvrir : "Quel risque j'ai aujourd'hui sans ce contrat ?" Si la reponse est "aucun", tu specules.
:::
