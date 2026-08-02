# Chapitre 4 - Prime et delta (intuition)

La **prime** d'une option est le prix que paie l'acheteur au vendeur. Elle se decompose en deux idees :

- **Valeur intrinseque** : ce que vaut le droit si on exercait tout de suite.
- **Valeur temps** : ce que le marche paie pour la possibilite que le sous-jacent bouge encore avant l'echeance.

Le **delta** mesure la sensibilite de la prime (ou du payoff) a une petite variation du sous-jacent S. C'est une pente locale : "si S monte de 1 EUR, la prime du call varie d'environ delta EUR."

Ce livre est pedagogique. Les exemples sont inventes. Comprendre prime et delta ne supprime pas le risque de perte totale de la prime.

Nora veut savoir pourquoi elle paie 2 EUR pour un call alors que le sous-jacent n'est qu'a 0,50 EUR "dans la monnaie". Max veut savoir pourquoi sa prime fond chaque jour sans que le cours bouge. Sam veut une intuition, pas un doctorat.

## Valeur intrinseque

Pour un **call** :

Intrinsique call = max(S - K, 0)

Pour un **put** :

Intrinsique put = max(K - S, 0)

Si S = 43, K = 40 (call) : intrinseque = 3 EUR.
Si S = 38, K = 40 (call) : intrinseque = 0 (option OTM, hors de la monnaie).

La **prime** affichee sur l'ecran = intrinseque + valeur temps (plus des micro-effets de taux et volatilite qu'on simplifie ici).

## Valeur temps : pourquoi la prime fond

Plus tu approches de l'echeance, moins il reste de "chances" que le sous-jacent bouge en ta faveur. La valeur temps tend vers 0 a l'echeance. C'est le **theta** (decroissance temporelle), qu'on mentionne sans formaliser : l'acheteur d'option paie un "loyer" pour le temps.

Exemple invente :

- Call ATM (at the money, S = K = 50), prime = 2,00 EUR a 60 jours de l'echeance
- Intrinsique = max(50-50,0) = 0
- Valeur temps = 2,00 EUR entiere

A 7 jours de l'echeance, si S reste a 50, la prime peut etre 0,40 EUR : la valeur temps s'est evaporee. Max lit "mon option a perdu 80 % alors que l'indice n'a pas bouge" : c'est normal pour un acheteur, surtout OTM ou ATM.

## Delta : intuition sans formule lourde

Le **delta** d'un call long est entre 0 et 1 (souvent exprime en 0,50 = 50 %). Il approxime :

Variation prime ~ Delta x Variation S

Pour un call **ATM** proche de l'echeance, delta ~ **0,50** : si S monte de 1 EUR, la prime monte d'environ 0,50 EUR (toutes choses egales par ailleurs).

Pour un call profond ITM (in the money), delta approche 1 : l'option se comporte un peu comme l'action.
Pour un call profond OTM, delta approche 0 : la prime reagit peu au sous-jacent.

Exemple pedagogique :

- Call, delta = 0,55, S passe de 40 a 41 (+1 EUR)
- Variation prime ~ 0,55 x 1 = +0,55 EUR (ordre de grandeur)

Nora teste sur une plateforme demo : ce n'est jamais exact a l'euro pres (volatilite, temps), mais l'ordre de grandeur l'aide a ne pas paniquer.

## Prime, volatilite et attentes

Si le marche anticipe de **gros mouvements** (volatilite implicite elevee), les primes montent : l'option "coute cher". Apres un choc, les primes gonflent ; en periode calme, elles compressent. Acheter une option juste avant un evenement connu (resultats, BCE) peut payer cher la volatilite deja pricee. DanielCraft : lire la prime, c'est lire ce que le marche "croit" sur l'amplitude future.

## Petite histoire

Sam achete un call a 1,20 EUR, S monte de 2 % en une semaine, sa prime passe a 1,15 EUR. Elle croit que "ca ne marche pas". En relisant ce chapitre, elle voit : une partie etait valeur temps, la volatilite a baisse, le delta n'etait pas 1. Elle note : "Le sous-jacent et l'option ne bougent pas pareil." Elle garde la demo, pas le compte reel.

## Erreur classique

Croire que "S monte donc mon call gagne toujours". Ignorer valeur temps et volatilite. Ou comparer deux primes sans regarder K, T, et S.

## En vrai

Choisis une option sur demo. Note S, K, prime, jours restants. Estime intrinseque a la main. Regarde comment la prime change sur 3 jours sans toucher au marche (theta).

## A toi

S=45, K=42, prime call=4,20. Calcule intrinseque. Combien reste-t-il de valeur temps ? Si delta=0,70 et S monte a 46, estime la nouvelle prime (~4,90).

:::retenir
Prime = intrinseque + valeur temps. Intrinsique call = max(S-K,0). Delta ~ sensibilite de la prime au sous-jacent ; ~0,5 pour call ATM.
:::

:::attention
La valeur temps fond vers l'echeance : tu peux perdre sur l'option meme si S stagne.
:::

:::astuce
Avant d'acheter, ecris intrinseque et valeur temps. Si valeur temps > 70 % de la prime, tu paies surtout du temps.
:::
