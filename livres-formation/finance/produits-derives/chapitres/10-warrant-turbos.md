# Chapitre 10 - Warrants et turbos : pieges

Les **warrants** et **turbos** (certificats a effet de levier) sont des produits **emballes** pour le retail : tu paies une prime ou un montant, tu obtiens une exposition levee a un sous-jacent, souvent avec une **barriere** ou un **knockout**. Si la barriere est touchee, le produit peut **expirer worthless** en une session : perte totale ou quasi totale de la mise.

Ce livre est pedagogique. Ce chapitre met en garde : ce ne sont pas des substitutes prudents aux actions ou ETF. Risque de **perte totale** de la prime rapide.

Nora confond warrant et option exchange. Max a vu un turbo "x10 sur le DAX". Sam cherche le mot "barriere" dans la fiche. DanielCraft : lire la barriere avant le levier affiche.

## Warrant : option retail simplifiee

Un **warrant** ressemble a une option emise par une banque : call ou put, strike, echeance, prime. Differences pratiques : emetteur = banque (risque emetteur), parfois moins liquide, spreads plus larges, documentation KID obligatoire en UE.

Exemple invente : warrant call sur action TechCo, strike 100, prime 3 EUR, echeance 6 mois. Si TechCo finit a 90, perte max = **3 EUR** (100 % de la prime). Comme un long call, mais verifie frais et spread a l'achat/vente.

## Turbo : levier + barriere knockout

Un **turbo** (ou mini-certificat leve) a :

- **Sous-jacent** (indice, action, devise)
- **Levier** effectif variable (recalcule chaque jour)
- **Barriere knockout** : si le sous-jacent la touche, le turbo est **desactive** (valeur residuelle parfois proche de zero)

Exemple pedagogique :

- Turbo long sur indice, barriere knockout a 7 000
- Indice spot = 7 500
- Tu paies 5 EUR par certificat (prime-like)
- Indice chute a 6 990 intraday → **knockout** → certificat ~ 0 EUR

Max pensait "je perds proportionnellement". Non : la barriere **casse** le produit. Le -6,8 % sur l'indice peut devenir -100 % sur le turbo.

## Pourquoi le levier affiche ment parfois

Le levier annonce (x10, x15) est **instantane**. Quand le sous-jacent bouge, le levier effectif change. Pres de la barriere, la sensibilite explose : petit mouvement, gros P&L ou knockout.

Nora calcule : barriere a 2 % sous le spot, gap overnight de -3 % → knockout sans possibilite de sortir au prix mental.

## Warrant vs option vs turbo

- **Option exchange** : marche standardise, chambre de compensation.
- **Warrant** : emis par banque, retail, echeance longue parfois.
- **Turbo** : pari leve court terme, barriere = fusee.

Aucun n'est "investissement tranquille" par nature.

## Petite histoire

Sam achete un turbo "parce que l'indice va rebondir". Barriere touchee en 20 minutes. Perte 800 EUR sur "juste un test". Elle ferme son compte warrants et ecrit : "Perte max = 100 % prime, vitesse max = intraday." DanielCraft : la lecon vaut 800 EUR si elle ne recommence pas.

## Erreur classique

Acheter un turbo sans lire la barriere knockout. Croire que "long turbo" = long indice proportionnel. Ignorer le risque emetteur et le spread a la revente.

## En vrai

Ouvre un KID de turbo sur le site d'une banque FR. Surligne barriere, levier, scenario de perte totale.

## A toi

Turbo long, spot 120, barriere 114, prix 8 EUR. Indice finit a 113,5. Que vaut le turbo ? Compare au warrant call strike 120 prime 8 si S=113,5 a echeance.

:::retenir
Warrant ~ option retail emise par banque. Turbo = levier + barriere knockout : perte totale possible tres vite.
:::

:::attention
Toucher la barriere knockout = produit mort, souvent perte 100 % de la mise. Pas un produit d'epargne.
:::

:::astuce
Regle DanielCraft : si tu ne peux pas expliquer la barriere en une phrase, tu n'aches pas.
:::
