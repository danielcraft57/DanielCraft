# Chapitre 13 - Retenir l'essentiel

Avant ateliers et quiz, on range les formules et reflexes dans une trousse. Chez DanielCraft, retenir = pouvoir recalculer et **refuser** un produit opaque.

Ce livre est pedagogique. Cette synthese ne remplace pas les chapitres detailles.

## Derives : definitions

- **Derive** = contrat dont la valeur depend d'un sous-jacent.
- **Future** = engagement ferme ; profit long ~ (P_T - F0) x multiplicateur.
- **Call** = droit d'acheter ; **Put** = droit de vendre au strike K.
- **Swap** = echange de flux (fixe vs variable) sur notionnel.

## Options : formules cle

- Intrinsique call = max(S - K, 0)
- Intrinsique put = max(K - S, 0)
- Profit long call = max(S - K, 0) - Prime
- Profit long put = max(K - S, 0) - Prime
- Breakeven call = K + Prime ; breakeven put = K - Prime
- Delta ~ sensibilite prime au sous-jacent ; ~0,5 call ATM

## Marge et levier

- Levier = Exposition / Fonds propres
- Variation compte ~ Levier x Variation sous-jacent (%)
- Exemple : 10x et -5 % sous-jacent ~ -50 % compte
- Marge initiale ≠ perte max (futures, CFD)
- Appel de marge → fonds ou liquidation

## Couverture vs speculation

- **Hedge** = reduire risque deja present.
- **Speculation** = parier sans sous-jacent a proteger.
- Protective put = action + put ; covered call = action + vente call.

## Produits retail a risque eleve

- **CFD** : difference de prix, leve, overnight, perte rapide jusqu'a 100 % depot.
- **Turbo** : barriere knockout → perte totale possible intraday.
- **Warrant** : proche option, risque emetteur.

## Black-Scholes (intuition)

- Inputs : S, K, T, r, sigma (volatilite).
- Modele utile, pas verite ; sauts et crashes mal captures.
- Vol implicite = ce que le marche "croit" sur l'amplitude future.

## Comportement DanielCraft

- Poches A/B/C : jamais loyer sur derive leve.
- Comprendre payoff et **perte max** avant tout clic.
- Simuler d'abord ; demo levier bas si tu testes.
- Verifier intermediaire agree AMF/UE, lire KID.

## Phrase anti-panique

"Mon horizon est ___, ma perte max acceptee est ___, je ne decide pas sur une pub x10. Je relis ch. 13 si j'hesite."

## A toi

Recopie sur papier 5 formules et la phrase anti-panique. C'est ton aide-memoire de crise.

:::retenir
Formules payoff + levier + perte max : la trousse minimale avant quiz et ateliers.
:::

:::attention
Une checklist ne remplace pas le refus d'un produit que tu ne comprends pas.
:::

:::astuce
Relis ce chapitre avant tout premier ordre reel - ou avant de dire non definitivement au levier, ce qui est souvent le bon choix.
:::
