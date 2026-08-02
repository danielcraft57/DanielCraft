# Chapitre 8 - Contango et backwardation

Sur les matieres, le prix **spot** et les prix des **futures** a differentes echeances forment une courbe. Si les echeances lointaines coutent plus cher que le proche, on parle souvent de **contango**. Si le proche est plus cher que le lointain, **backwardation**. Chez DanielCraft, ca sert a comprendre le cout de "rouler" une position, pas a impresionner au cafe.

Disclaimer : simplifie. Les courbes reelles ont des bosses.

## Contango : payer pour attendre

Exemple invente petrole :
- Spot / future proche = 70 USD
- Future a 6 mois = 74 USD

Contango = +4 USD. Si tu es long via futures et que tu **rolles** (passes d'une echeance a la suivante) dans un contango durable, tu peux "perdre" un peu a chaque roll meme si le spot ne bouge pas. Les ETF matieres a roll mensuel en souffrent parfois.

## Backwardation : le proche presse

Exemple :
- Proche = 80
- 6 mois = 75

Le marche paie plus cher l'immediat (stock tendu, demande urgente...). Un roll peut alors etre favorable aux longs (selon structure exacte).

## Lien avec la couverture

Un importateur qui hedge avec un future choisit une echeance proche de son besoin. Il ne "bat" pas le marche : il **fige** un prix. Le contango fait partie du cout de couverture (avec la marge, le basis, etc.). Detail des contrats : livre **Produits derives**.

## Petite histoire

Sam achete un produit "oil" sans lire le roll. En un an, le spot est plat, sa ligne est negative. Contango + frais. Il apprend a lire la courbe avant le logo du produit.

## Erreur classique

Comparer perf spot et perf d'un ETF futures sans parler des rolls.

## Mini-exercice

Proche 72, 3 mois 75, 6 mois 77. Contango. Ecart 0->6 mois = +5. Note "roll potentiellement couteux pour un long rollé".

## A toi

Sur une fiche ETF matiere, cherche "futures", "roll", "contango". Si absent : signal orange.

:::retenir
Contango = lointain > proche (souvent). Backwardation = inverse. Ca change le cout du roll.
:::

:::attention
Spot plat + contango = perf futures parfois negative.
:::

:::astuce
Avant un produit "petrole" papier, demande comment les echeances sont roulees.
:::
