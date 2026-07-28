# Chapitre 19 - Black-Scholes : intuition (pas le doctorat)

**Black-Scholes** (1973) est un modele qui estime le prix theorique d'une option europeenne a partir de cinq inputs :

- **S** : prix spot du sous-jacent aujourd'hui
- **K** : strike
- **T** : temps jusqu'a l'echeance (en annees)
- **r** : taux sans risque
- **sigma** : volatilite du sous-jacent (souvent **volatilite implicite** deduite du marche)

Ce chapitre donne l'**intuition**, pas la preuve mathematique. Tu n'as pas besoin de deriver l'equation pour etre prudent sur les options.

Ce livre est pedagogique. Black-Scholes est utile en salle de marche ; il est **approximatif** dans le monde reel.

Nora voit "IV crush" sur Twitter. Max confond volatilite historique et implicite. Sam veut savoir pourquoi la prime explose avant une annonce. DanielCraft : inputs et limites.

## Idee centrale

Le modele suppose que le sous-jacent suit un mouvement aleatoire continu (pas de sauts), avec volatilite constante, pas de cout de transaction, taux connus. Sous ces hypotheses, on peut calculer une **prime theorique** pour un call ou put europeen.

En pratique, le marche **price** les options via la **vol implicite** : quelle sigma rend le modele egal au prix cote ? Si sigma implicite monte, les primes montent meme si S stagne.

## d1 et d2 (mention legere, sans preuve)

Le call theorique peut s'ecrire schematiquement :

C = S x N(d1) - K x e^(-rT) x N(d2)

Ou N() est la fonction de repartition normale, et d1, d2 combinent ln(S/K), (r + sigma²/2)T, sigma√T. **Tu n'as pas a calculer d1/d2 a la main** pour ce livre. Retiens seulement :

- d1, d2 melangent **ratio S/K**, **temps T**, **vol sigma**, **taux r**.
- Plus T long → plus de valeur temps.
- Plus sigma eleve → plus chere l'option (call et put longs).

## Exemple pedagogique qualitatif

Voltex S = 40, call K = 40, T = 1 mois.

- Cas calme : sigma implicite 15 % → prime ~ 0,80 EUR (invente)
- Avant resultats : sigma 35 % → prime ~ 2,20 EUR

Le sous-jacent n'a pas bouge. La prime a **plus que double** parce que le marche price un **evenement**. Apres l'annonce (resultats sans surprise), sigma retombe a 18 %, prime ~ 1,00 EUR. L'acheteur avant l'annonce peut perdre sur la prime malgre une direction correcte : **IV crush**.

Max ecrit : "J'achetais la volatilite chere, pas seulement la direction."

## Limites du modele (important)

Black-Scholes **mal capture** :

- **Sauts** (gap overnight, krach, rachat)
- **Queues epaisses** (evenements extremes plus frequents que la cloche de Gauss)
- Volatilite **non constante** (sourire de vol)
- Dividendes discrets, couts de transaction
- Marches illiquides (warrants, options OTM fines)

Les pros utilisent BS comme **repere**, puis ajustements. Le retail qui croit "BS dit que c'est cheap" sans lire le contexte se fait surprendre.

## Lien avec delta (ch. 4)

En BS, le delta du call = N(d1). ATM approx delta 0,5 quand T pas trop court. Coherence avec l'intuition du chapitre 4.

## Petite histoire

Sam achete un call "cheap" sigma 10 % sur une biotech avant FDA. Resultat favorable, action +8 %, option +5 % seulement : vol effondree. Elle decouvre IV crush. DanielCraft : le chapitre 19 explique sa facture.

## Erreur classique

Croire que BS "prouve" le prix juste du marche. Acheter options sans regarder vol implicite vs historique. Utiliser une calculette BS sans comprendre les inputs.

## En vrai

Sur une chaine d'options publique, compare vol implicite ATM et historique 30 jours (si affiche). Note l'ecart sans trader.

## A toi

Liste les 5 inputs BS de memoire. Pour chacun, ecris "si ca monte, la prime call tend a..." (qualitatif).

:::retenir
BS : 5 inputs S, K, T, r, sigma. Vol implicite = ce que le marche croit. Modele utile, pas verite ; sauts et IV crush existent.
:::

:::attention
Acheter une option avant evenement = souvent acheter sigma chere. Direction juste ≠ profit garanti.
:::

:::astuce
Si tu ne peux pas nommer les 5 inputs, tu n'as pas le niveau pour vendre des options ou trader vol activement.
:::
