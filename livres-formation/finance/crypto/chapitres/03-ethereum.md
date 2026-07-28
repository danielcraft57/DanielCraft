# Chapitre 3 - Ethereum et smart contracts

**Ethereum (ETH)** est une blockchain programmable. Au-dela d'un simple transfert, on y deploie des **smart contracts** : programmes qui executent des regles (echange, pret, NFT...) sans intermediaire classique. Chez DanielCraft, "programmable" veut aussi dire **piratable** et **complexe**.

Disclaimer : pedagogie. Gas, bridges, contrats = surface d'attaque.

## Smart contract : promesse et bug

Le contrat fait ce que le code dit... y compris les bugs. Audits aident ; ils ne sont pas une assurance. Un yield "20 %" peut cacher un risque de smart contract, d'oracle, ou de rug.

Exemple invente :
- Tu deposés 1 000 USDC dans un protocole
- Un bug drainé le pool
- Solde affiche : 0
Pas d'hotline qui "annule". Parfois des fonds sont recuperes. Souvent non.

## Gas : le prix de l'execution

Chaque action coute du **gas** (paye en ETH ou equivalent). Quand le reseau saturen, le gas explose. Un transfert de 5 EUR peut couter plus cher que le transfert. Max apprend a regarder le cout **avant** de signer.

## Petite histoire

Sam teste un mint NFT. Gas 80 EUR pour un jeton a 10 EUR. Il annule. Lecon : lire le cout total, pas le prix affiche.

## Erreur classique

Signer une transaction illegible "parce que MetaMask a pop". Ou bridger sans comprendre les deux bouts.

## En vrai

Sur un explorateur de blocs (lecture seule), regarde une transaction : from, to, fees. Curiosite sans depot.

## A toi

Ecris : "Je ne signe rien dont je ne peux pas expliquer le to et le montant."

:::retenir
ETH = machine a contrats. Flexible = aussi fragile si tu ne lis pas.
:::

:::attention
Yield eleve DeFi = souvent risque eleve (code, liquidite, oracle).
:::

:::astuce
Regarde toujours le gas estime avant Confirm.
:::
