# Chapitre 8 - DeFi : introduction prudente

La **DeFi** (finance decentralisee) propose prets, exchanges, pools de liquidite via smart contracts. Rendements affiches eleves. Risques eleves. Chez DanielCraft, DeFi = chapitre "comprendre pour ne pas se faire manger", pas "farm all night".

Disclaimer : perte totale possible. Pas un conseil.

## Pools, IL, smart contract

Fournir de la liquidite : tu deposés deux actifs, tu gagnes des fees... et tu subis parfois l'**impermanent loss** (IL) si les prix divergent. Ajoute le risque de hack.

Exemple IL simplifie (intuition) :
- Tu deposés 50/50 token A et B
- A pump fort vs B
- En sortant, tu as moins de A que si tu avais HODL separement
Les fees peuvent compenser... ou non.

## Approvals

Autoriser un contrat a bouger tes jetons (approve). Approvals infinis + contrat malveillant = drain. Revoke periodique = hygiene.

## Petite histoire

Nora farm un pool "AP Y 90 %". Deux semaines plus tard : exploit. Elle avait mis "de l'argent de jeu" = 80 EUR. Douleureux. Survivable. Sam refuse tout APY a trois chiffres.

## Erreur classique

Bridger + farm + levier en une soiree. Trop de surfaces d'attaque.

## A toi

Si tu touches la DeFi un jour : montant max = argent que tu acceptes a zero. Ecris le chiffre.

:::retenir
DeFi = code + liquidite + incentives. APY haut = question rouge.
:::

:::attention
Approve infini = porte ouverte. Lis ce que tu signes.
:::

:::astuce
Commence par lire un protocole celebre en mode spectateur (docs), sans deposer.
:::
