# Chapitre 6 - Marge et appels de marge

Sur les marches a effet de levier (futures, CFD, forex retail), tu ne paies pas le nominal complet a l'ouverture. Tu depose une **marge** : un capital de garantie. Deux idees essentielles :

- **Marge initiale** : depot pour ouvrir la position.
- **Marge de variation** : ajustements quotidiens (ou intraday) selon le P&L latent.

Si ta position perd, ton compte est **debite**. Si le solde tombe sous la **marge de maintenance**, tu recois un **appel de marge** (margin call) : tu dois reconstituer, ou la position est **liquidee**.

Ce livre est pedagogique. Les exemples sont inventes. Le risque inclut une **perte superieure au depot initial** si tu ne coupes pas et que le marche gap contre toi, ou si tu ne peux pas honorer l'appel.

Nora confond marge et "frais". Max croit que 500 EUR de marge = perte max 500 EUR (faux sur future). Sam veut une image claire avant de toucher a une demo levee.

## Marge initiale vs exposition

Exposition = taille reelle de la position (en euros).
Marge initiale = fraction immobilisee.

Levier implicite ~ Exposition / Marge

Exemple :

- Exposition = 10 000 EUR (equivalent 1 contrat ou CFD)
- Marge initiale = 1 000 EUR
- Levier ~ 10x

Une baisse de 5 % du sous-jacent = -500 EUR sur l'exposition = **-50 %** sur ta marge de 1 000 EUR.

## Marge de variation : exemple journalier

Compte invente de Max, future sur indice :

- Solde initial : 5 000 EUR
- Marge initiale pour la position : 2 000 EUR (immobilisee)
- Marge de maintenance : 1 500 EUR
- Jour 1 : P&L latent = -400 EUR → solde = 4 600 EUR (OK)
- Jour 2 : P&L latent = -600 EUR → solde = 4 000 EUR (OK)
- Jour 3 : P&L latent = -900 EUR → solde = 3 100 EUR

Cumul perte sur position ~ -1 900 EUR depuis l'ouverture (simplifie). Si le solde disponible pour la marge tombe sous 1 500 EUR, **appel de marge** : Max doit virer des fonds ou reduire la position. S'il ne repond pas, **liquidation forcee** au pire moment pour lui.

Nora lit "liquidation" et comprend : ce n'est pas une punition morale, c'est une clause du contrat.

## Appel de marge : ce qui se passe en pratique

Le courtier te notifie : compte sous le seuil. Tu as un delai (quelques heures a 24-48 h selon contrat). Options :

1. **Virer des fonds** pour remonter au-dessus de la marge de maintenance.
2. **Cloturer partiellement** la position pour reduire l'exposition.
3. **Ne rien faire** → le courtier liquide souvent automatiquement.

En periode de forte volatilite, les appels peuvent s'enchaine. Le risque psychologique : "rattraper" en doublant la mise. DanielCraft : regle ecrite a l'avance, pas de decision a 2 h du matin.

## Marge sur CFD vs future

Meme logique, labels differents. CFD retail : marge exprimee en % du nominal (ex. 5 % = levier 20). Future : marge en EUR par contrat fixee par la chambre de compensation. Dans les deux cas : **mark-to-market** (valorisation au prix du jour) et debits/credits quotidiens.

## Petite histoire

Sam ouvre une demo CFD levee "juste pour voir". En une semaine calme, rien. Puis un jour -8 % sur l'indice : son solde demo perd 40 % en une session (levier 5). Elle ferme la demo et ecrit sur papier : "Appel de marge = realite, pas bug." Elle ne passe pas au compte reel. DanielCraft applaudit le geste.

## Erreur classique

Confondre marge initiale et perte max. Ignorer la marge de maintenance. Trader sans reserve de tresorerie pour honorer un appel. Croire que "ca remontera" avant liquidation.

## En vrai

Lis les conditions generales de marge de ton courtier (ou d'une demo). Note marge initiale %, maintenance %, politique de liquidation.

## A toi

Marge 800 EUR, levier 10x, sous-jacent -6 %. Calcule perte EUR et % sur marge. Solde restant 800 - perte. Sous maintenance 600 EUR, que se passe-t-il ?

:::retenir
Marge initiale ouvre la position ; marge de variation ajuste le P&L. Appel de marge si solde < maintenance → fonds ou liquidation.
:::

:::attention
Tu peux perdre plus que la marge initiale si le marche gap et que la liquidation intervient tard.
:::

:::astuce
Regle : reserve separee (poche B) jamais touchee pour "sauver" une position levee. Si tu en as besoin, tu es deja hors plan.
:::
