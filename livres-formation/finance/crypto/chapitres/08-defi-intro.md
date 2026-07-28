# Chapitre 8 - DeFi : introduction prudente

La **DeFi** (finance decentralisee) propose prets, exchanges, pools de liquidite via smart contracts. Rendements affiches eleves. Risques eleves. Chez DanielCraft, DeFi = chapitre "comprendre pour ne pas se faire manger", pas "farm all night".

Disclaimer : perte totale possible. Pas un conseil. Si tu ne touches jamais la DeFi, ce chapitre reste utile : tu reconnaitras les pieges dans les pubs.

## Pools, IL, smart contract

Fournir de la liquidite : tu deposés deux actifs, tu gagnes des fees... et tu subis parfois l'**impermanent loss** (IL) si les prix divergent. Ajoute le risque de hack. Les fees peuvent compenser... ou non. Un APY a trois chiffres est souvent une question rouge, pas une aubaine.

Exemple IL simplifie (intuition) :
- Tu deposés 50/50 token A et B
- A monte fort vs B
- En sortant, tu as moins de A que si tu avais garde separement
Ce n'est pas "vol". C'est la mecanique du pool. Beaucoup la decouvrent apres coup.

## Approvals

Autoriser un contrat a bouger tes jetons (**approve**). Approvals infinis + contrat malveillant = drain. Revoke periodique = hygiene. Lire le to et le montant avant de signer n'est pas optionnel. C'est le metier du debutant prudent.

## Petite histoire

Nora farm un pool "APY 90 %". Deux semaines plus tard : exploit. Elle avait mis "de l'argent de jeu" = 80 EUR. Douloureux. Survivable. Sam refuse tout APY a trois chiffres. Max lit les docs d'un protocole celebre en mode spectateur pendant une semaine, sans deposer. Il apprend plus que Nora en une nuit de farm.

## Erreur classique

Bridger + farm + levier en une soiree. Trop de surfaces d'attaque. Confondre "TVL eleve" et "sur". Signer un approve infini "pour aller plus vite".

## En vrai

Ouvre la doc d'un protocole connu (lecture). Note en trois puces : quoi, risques listes, ce que tu ne comprends pas. Pas de depot.

## A toi

Si tu touches la DeFi un jour : montant max = argent que tu acceptes a zero. Ecris le chiffre (0 autorise).

:::retenir
DeFi = code + liquidite + incentives. APY haut = question rouge.
:::

:::attention
Approve infini = porte ouverte. Lis ce que tu signes.
:::

:::astuce
Commence par lire un protocole en mode spectateur, sans deposer.
:::
