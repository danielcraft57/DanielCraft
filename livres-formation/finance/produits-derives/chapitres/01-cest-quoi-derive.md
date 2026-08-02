# Chapitre 1 - C'est quoi un produit derive ?

Un **produit derive** est un contrat financier dont la valeur depend d'un autre actif, appele **sous-jacent**. Le sous-jacent peut etre une action, un indice, une matiere premiere, un taux d'interet ou une devise. Tu n'achetes pas directement l'actif : tu entres dans un accord qui fixe des droits ou des obligations selon l'evolution de ce sous-jacent. Ce n'est pas un actif "magique" qui contourne le risque. C'est un outil qui deplace, concentre ou transfere le risque entre deux parties.

Ce livre est pedagogique. Il ne remplace ni un conseiller agree, ni un banquier, ni un fiscaliste. Les exemples sont inventes pour apprendre. Investir et trader des produits derives comporte un **risque de perte en capital**, y compris une perte superieure a la mise initiale lorsque le levier est utilise. Ce livre vise a **comprendre**, pas a t'encourager a trader avec effet de levier.

Nora, salariee prudente, Max artisan, et Sam qui gere une petite activite : trois profils, une meme regle DanielCraft. Avant d'ouvrir un ecran de courtier, ils veulent savoir ce qu'ils regardent. Un derive n'est pas une action deguisee. C'est un contrat avec des regles precises, une echeance parfois, et souvent un effet de levier implicite.

## Derive = contrat, pas actif physique

Quand tu achetes une action, tu detiens une part de capital. Quand tu achetes un future ou une option, tu detiens un **contrat** : droit d'acheter, obligation de livrer, echange de flux, selon le produit. La valeur du contrat bouge parce que le sous-jacent bouge, parce que le temps passe, ou parce que la volatilite percue change. Rien ne garantit que tu gagnes. Le marche ne te doit rien.

Les grandes familles que tu croiseras dans ce livre :

- **Futurs (futures)** : engagement ferme d'acheter ou de vendre a un prix fixe a une date future.
- **Options (call et put)** : droit, pas obligation, d'acheter (call) ou de vendre (put) a un prix fixe (strike) avant ou a l'echeance.
- **Swaps** : echange de flux (souvent taux fixe contre taux variable) sur une duree.

D'autres produits retail (CFD, warrants, turbos) sont des variantes ou des emballages de ces mecanismes. Le vocabulaire change ; la logique sous-jacent / contrat reste.

## Pourquoi ces produits existent

Les derives ne sont pas nes pour les influenceurs TikTok. Ils servent d'abord a **couvrir** un risque existant : un agriculteur qui craint une chute du ble, une entreprise qui emprunte en variable et veut se fixer, un fonds qui protege un portefeuille. Ensuite viennent la **speculation** (parier sur une direction) et l'**arbitrage** (exploiter un ecart de prix). Les trois usages coexistent. Le debutant voit surtout la pub pour la speculation. DanielCraft te demande de comprendre les trois avant de cliquer.

Exemple invente : Sam importe du cafe. Elle craint que le prix monte de 10 % dans trois mois. Elle peut acheter un future sur le cafe pour "figer" un prix d'achat futur. Si le prix monte, le gain sur le future compense la hausse du cafe physique. Si le prix baisse, elle a "surpaye" sa couverture. Ce n'est pas un pari gratuit : c'est un **assurance** avec un cout.

## Derive vs action : ce qui change dans ta tete

Sur une action, ta perte max (sans levier) est ce que tu as paye. Sur un future ou un CFD leve, ta perte peut depasser ton depot. Sur une option achetee, ta perte max est souvent la **prime** payee. Sur une option vendue, le risque peut etre bien plus large. Le derive n'est ni "plus intelligent" ni "plus dangereux" en soi : il a une **carte de payoff** differente. Apprendre les derives, c'est apprendre ces cartes.

Nora note dans son carnet : "Quelle est ma perte max si j'ai tort ?" Cette question vaut plus qu'un graphique en chandelier.

## Petite histoire

Max voit une pub : "Multipliez vos gains avec les options !" Il ouvre le site, voit des boutons vert fluo, et sent l'urgence. Il ferme l'onglet, rouvre ce chapitre, et ecrit : "Un derive = contrat sur un sous-jacent. Je ne sais pas encore le payoff. Donc je ne signe pas." Le lendemain, le meme site promet "rendement garanti". Max reconnait le signal. DanielCraft prefere ce reflexe a n'importe quel screenshot de perf.

## Erreur classique

Croire qu'un derive "gagne plus" qu'une action parce que c'est complique. Ou confondre **droit** (option) et **obligation** (future). Ou ignorer que le sous-jacent peut bouger contre toi plus vite que tu ne peux reagir, surtout avec levier.

## En vrai

Prends une fiche produit au hasard (future indice, warrant, CFD). Repere : sous-jacent, echeance, effet de levier eventuel, perte max annoncee. Si un de ces champs est flou, c'est un signal orange.

## A toi

Ecris en trois lignes : ce qu'est un derive pour toi, un exemple de sous-jacent, et la question "perte max si j'ai tort" que tu poseras avant tout clic.

:::retenir
Derive = contrat dont la valeur depend d'un sous-jacent. Familles cles : futurs, options, swaps. Pas un raccourci sans risque.
:::

:::attention
Le levier peut faire perdre plus que le depot. Ce livre enseigne a comprendre, pas a trader agressivement.
:::

:::astuce
Avant tout produit derive, ecris sous-jacent + type de contrat + perte max. Si tu ne peux pas remplir, tu n'es pas pret.
:::
