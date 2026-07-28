# Chapitre 3 - Taux de change et parite

Le **taux de change** dit combien d'une devise il faut pour en obtenir une autre. La **parite** (au sens large ici) c'est ce rapport. Il bouge avec les taux d'interet, l'inflation, les flux commerciaux, la peur, la politique monetaire. Chez DanielCraft, on refuse le slogan "la paire va forcement remonter".

Disclaimer : pedagogie. Pas une prevision.

## Appreciation et depreciation

Si EUR/USD monte : l'euro s'apprecie vs dollar (ou le dollar se deprecie vs euro).  
Si EUR/USD baisse : l'euro se deprecie vs dollar.

Pour un Europeen qui visite New York :
- EUR/USD haut => plus de pouvoir d'achat en dollars (souvent)
- EUR/USD bas => sejour plus cher en euros

Pour Max qui importe en USD facture fixe en dollars :
- EUR/USD baisse => sa facture coutte **plus** d'euros
- EUR/USD monte => sa facture coutte **moins** d'euros

Exemple :
- Facture = 10 000 USD
- Taux 1,10 => cout = 10 000 / 1,10 = 9 091 EUR
- Taux 1,05 => cout = 10 000 / 1,05 = 9 524 EUR
- Ecart = +433 EUR pour le meme colis

C'est exactement le genre de risque que l'on **couvre** parfois avec un forward ou une option de change (voir livre **Produits derives** + chapitre hedging ici).

## PPP : intuition (sans doctorat)

La **parite de pouvoir d'achat** dit en gros : a long terme, les taux tendent a refleter les ecarts d'inflation. Si la zone A inflate plus que B, sa devise tend a se deprecier. C'est une boussole lente, pas un timing de trade.

## Petite histoire

Nora planifie un voyage dans 6 mois. Elle regarde le taux, calcule un budget a +/-5 %. Elle n'ouvre pas de compte levier "pour se couvrir". Elle met une marge dans le budget. Pour une PME, la couverture derive peut avoir un sens. Pour un voyage, souvent non.

## Erreur classique

Lire une seule cause ("la Fed va baisser => EUR/USD monte forcement"). Les marches price deja une partie des anticipations.

## En vrai

Prends une facture inventee en devise. Recalcule le cout EUR a deux taux (+/-3 %). Garde l'ecart en tete.

## A toi

Ecris : "Si EUR/USD baisse de 4 %, mon scenario perso/pro coute environ ... EUR de plus/moins."

:::retenir
Taux de change = prix relatif. Pour un importateur, une baisse de sa devise = facture plus lourde.
:::

:::attention
Anticipation de banque centrale != timing garanti.
:::

:::astuce
Toujours convertir le risque de change en euros concrets, pas en "pips abstraits".
:::
