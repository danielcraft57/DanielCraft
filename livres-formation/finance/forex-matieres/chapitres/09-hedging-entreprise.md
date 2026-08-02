# Chapitre 9 - Hedging pour l'entreprise

Se **couvrir** (hedger), c'est reduire un risque deja present dans l'activite : factures en devises, achats de matieres, taux d'interet. Ce n'est pas "parier a l'envers pour s'amuser". Chez DanielCraft, la couverture sert a **dormir**, pas a battre le marche.

Disclaimer : pedagogie. Une vraie politique de couverture se construit avec un pro (banque, tresorerie, conseil). Les exemples sont inventes.

Les outils sont souvent des **produits derives** : forward de change, future matiere, option (prime = assurance), parfois swap. Ce chapitre dit **pourquoi** et **quand**. Le mecanisme detaille (payoff, marge, call/put) est dans **Finance - Produits derives**.

## Cas 1 : importateur en USD

Max commande 50 000 USD de pieces, paiement dans 3 mois. Il craint une **baisse de l'euro** (EUR/USD down) qui alourdit sa facture en EUR.

Aujourd'hui : EUR/USD = 1,10 => cout theorique = 50 000 / 1,10 = 45 455 EUR.  
Si taux a 1,05 : cout = 47 619 EUR (+2 164 EUR).

Pistes de couverture (idees, pas prescriptions) :
- **Forward** de change : figer un taux aujourd'hui pour dans 3 mois
- **Call** sur USD / put sur EUR (selon cotation) : assurance avec prime
- Ne rien faire + marge dans le prix de vente (acceptation du risque)

Voir derives : chapitres forwards/futures, options, couverture vs speculation.

## Cas 2 : exposition petrole / energie

Sam a des couts carburant. Il peut :
- revoir ses contrats clients (indexation)
- et/ou utiliser un **future** energie pour figer un prix d'achat (si taille et expertise suffisent)
- ou un **call** (plafond de prix) en payant une prime

Couverture parfaite rare : il reste le **basis** (ecart entre ton prix reel et l'indice hedge).

## Couverture vs speculation (rappel)

| | Couverture | Speculation |
|---|---|---|
| Risque de depart | Deja la (facture, stock) | Cree par le trade |
| But | Reduire la variance | Gagner sur une direction |
| Succes | Stabiliser le resultat | Battre le marche |

Si tu n'as **pas** d'exposition sous-jacente et que tu ouvres un future petrole "pour jouer", ce n'est plus de la couverture.

## Petite histoire

Nora voit un broker : "hedgez comme les banks". Elle n'a qu'un voyage. Elle met 5 % de marge budget. Max, lui, demande a sa banque un forward sur sa vraie facture. Deux gestes coherents avec la taille du risque.

## Erreur classique

Sous-hedger puis sur-hedger en panique. Ou "couvrir" avec un levier 30 sur CFD sans lien avec le flux reel.

## En vrai

Liste tes flux en devise / matiere sur 12 mois (meme approx). S'il n'y en a pas, tu n'as rien a hedger retail.

## A toi

Ecris un mini cahier des charges : exposition, horizon, outil envisage (forward / option / rien), perte max acceptable.

:::retenir
Couverture = reduire un risque d'activite, souvent via derives. Speculer = autre metier.
:::

:::attention
Sans exposition reelle, un "hedge" est souvent un pari renomme.
:::

:::astuce
Relis Finance - Produits derives (couverture vs speculation, futures, options) avant tout contrat.
:::
