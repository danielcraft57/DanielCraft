# Chapitre 3 - Ethereum et smart contracts

**Ethereum (ETH)** est une blockchain programmable. Au-dela d'un simple transfert, on y deploie des **smart contracts** : programmes qui executent des regles (echange, pret, NFT...) sans intermediaire classique. Chez DanielCraft, "programmable" veut aussi dire **piratable** et **complexe**. Admirer la machine n'oblige pas a y deposer ton annee de marge.

Disclaimer : pedagogie. Gas, bridges, contrats = surface d'attaque. Perte totale possible.

## Smart contract : promesse et bug

Le contrat fait ce que le code dit... y compris les bugs. Les audits aident. Ils ne sont pas une assurance. Un yield "20 %" peut cacher un risque de smart contract, d'oracle, de gouvernance, ou de rug. "Trustless" veut dire "tu fais confiance au code et a ses hypothese", pas "zero risque".

Exemple invente :
- Tu deposés 1 000 USDC dans un protocole
- Un bug draine le pool
- Solde affiche : 0
Pas d'hotline qui "annule" comme une carte bancaire. Parfois des fonds sont recuperes. Souvent non.

## Gas : le prix de l'execution

Chaque action coute du **gas** (paye en ETH ou equivalent). Quand le reseau sature, le gas explose. Un transfert de 5 EUR peut couter plus cher que le transfert. Max apprend a regarder le cout **avant** de signer. Sam annule un mint quand le gas depasse le prix du jeton. Ce n'est pas de la lachete. C'est de l'arithmetique.

Les **bridges** (passerelles entre chaines) ajoutent une couche : deux bouts a comprendre, plus le pont lui-meme. Beaucoup de hacks historiques passent par la. Si tu ne peux pas expliquer les deux bouts, tu n'es pas pret a bridger "pour tester un farm".

## Petite histoire

Sam teste un mint NFT. Gas 80 EUR pour un jeton a 10 EUR. Il annule. Nora lit une doc de protocole une semaine avant de deposer 50 EUR "argent de jeu". Max refuse de signer une popup MetaMask illegible "parce que ca urge". Trois tempos. Une meme hygiene : lire le to, le montant, le cout.

## Erreur classique

Signer une transaction illegible. Bridger sans comprendre. Chasser un airdrop via un lien Discord. Confondre "contrat populaire" et "contrat sur".

## En vrai

Sur un explorateur de blocs (lecture seule), regarde une transaction : from, to, fees. Curiosite sans depot. Decris-la a voix haute en une phrase.

## A toi

Ecris et signe (sur papier) : "Je ne signe rien dont je ne peux pas expliquer le to et le montant."

:::retenir
ETH = machine a contrats. Flexible = aussi fragile si tu ne lis pas.
:::

:::attention
Yield eleve DeFi = souvent risque eleve (code, liquidite, oracle).
:::

:::astuce
Regarde toujours le gas estime avant Confirm.
:::
