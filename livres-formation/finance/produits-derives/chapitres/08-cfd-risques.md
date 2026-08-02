# Chapitre 8 - CFD : risques majeurs

Un **CFD** (Contract for Difference) est un contrat entre toi et le **courtier** : tu ne possedes pas l'actif sous-jacent. Tu gagnes ou perds la **difference** de prix entre l'ouverture et la cloture, eventuellement ajustee de **financement overnight** et de **spreads**. Les CFD retail sont presque toujours **leves** : une petite marge controle une grande exposition.

Ce livre est pedagogique. Ce chapitre **n'est pas un conseil d'achat**. Les CFD comportent un **risque eleve de perte rapide**, et entre **70 et 80 %** des comptes CFD retail perdent de l'argent selon les avertissements reguliers europeens (ordre de grandeur AMF/ESMA, verifie les stats a jour sur le KID).

Nora a vu une pub "tradez l'or sans frais". Max confond CFD et ETF. Sam veut la liste des risques avant meme une demo. DanielCraft : comprendre pour refuser ou limiter, pas pour se sentir invincible.

## Mecanisme en clair

Tu ouvres long CFD sur action X a 100 EUR, taille equivalent 1 000 EUR (levier 10, marge 100 EUR). X monte a 105 : gain ~ 50 EUR (+50 % sur marge). X baisse a 95 : perte ~ 50 EUR (-50 %). X baisse a 90 : perte ~ 100 EUR = **100 % de la marge**, appel de marge ou liquidation.

Profit long CFD (simplifie, sans frais) :

P&L ~ (P_cloture - P_ouverture) x Quantite

La quantite est souvent derivee du nominal / prix.

## Levier et perte superieure au depot

Reglementation UE : protection du solde negatif pour retail en conditions normales, mais cela **n'elimine pas** les pertes rapides jusqu'a **100 % du capital** depose, ni les appels de marge sur certains profils/produits. En gap de marche (ouverture en gap), la cloture peut etre pire que ton stop theorique.

Exemple invente :

- Compte = 2 000 EUR
- Position levee 5x = 10 000 EUR d'exposition
- Mouvement -4 % = -400 EUR (-20 % compte)
- Trois jours mauvais cumules -10 % sous-jacent ~ -1 000 EUR (-50 % compte)

Sam ecrit : "Je peux perdre la moitie en une semaine sans 'faillite' du compte."

## Overnight et couts caches

Garder une position ouverte **overnight** declenche souvent des **frais de financement** (swap daily) : tu paies ou recois selon direction et taux. Les day traders les ignorent ; les swing traders les subissent. Ajoute **spread** (ecart achat/vente) et commissions eventuelles. Un CFD "sans commission" n'est pas gratuit : le spread est le cout.

## Contrepartie : tu trades contre le courtier

Sur beaucoup de CFD retail, le courtier est **contrepartie** ou internalise le flux (market maker). Conflits d'interet possibles, risque si le courtier est mal capitalise (cas extremes). Prefere un **intermediaire agree** AMF/UE, lis les infos sur la politique d'execution.

## CFD vs action vs future

- **Action** : propriete, pas de levier obligatoire, pas de funding daily.
- **Future** : marche organise, marge standardisee, contrat reglemente.
- **CFD** : flexible, retail, leve, OTC avec le courtier.

Le CFD est pratique pour speculer a court terme ; il est **mal adapte** au debutant qui cherche a "investir tranquillement".

## Petite histoire

Max ouvre une demo CFD avec levier 30 "pour apprendre vite". En deux sessions, +15 % puis -40 %. Il ferme, imprime l'avertissement AMF sur les CFD, et le colle dans son carnet. Nora lui dit : "Tu as paye zero EUR pour la lecon." DanielCraft : demo oui, reel non sans formation longue.

## Erreur classique

Croire que le levier "augmente les chances de gagner". Ignorer overnight sur positions tenues 2 semaines. Choisir un courtier non agree parce que le levier est plus haut. Mettre de l'argent "poche A" (loyer, courses) sur un CFD.

## En vrai

Lis le **KID** (Key Information Document) d'un CFD sur un actif que tu connais. Note levier max, cout overnight, % de comptes perdants affiche.

## A toi

Calcule P&L pour marge 500 EUR, levier 20, sous-jacent -3 % puis -7 %. A -7 %, quel % de la marge reste-t-il ?

:::retenir
CFD = pari sur difference de prix avec le courtier, souvent leve. Risque perte rapide jusqu'a 100 % du depot. Overnight + spread = couts.
:::

:::attention
Ce livre ne recommande pas les CFD. Majorite des comptes retail perdants. Ne jamais utiliser l'argent necessaire au quotidien.
:::

:::astuce
Si tu testes, demo seulement, levier minimal, journal de trades. Arret si tu ne peux pas expliquer le P&L a la main.
:::
