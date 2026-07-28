# Chapitre 12 - Mini-projet : couverture fictive

Ce mini-projet relie les chapitres 1 a 11 **sur papier**. Aucun ordre reel, aucun levier obligatoire. Deux postures possibles (choisis une) :

- **Posture A** : "Je refuse le levier" - tu documentes pourquoi et comment tu te contentes de comprendre les payoffs.
- **Posture B** : "Je simule seulement" - demo ou tableur, levier max 2, capital fictif 1 000 EUR.

Ce livre est pedagogique. Le livrable est un dossier ecrit, pas une perf de trading.

Nora choisit A (son PEA suffit). Max choisit B pour voir la marge bouger. Sam hesite, puis A avec quiz choc. DanielCraft valide les deux si le dossier est honnete.

## Etape 1 : fiche identite (30 min)

Reponds par ecrit :

1. Quel risque reel j'ai aujourd'hui (actions, taux, change, aucun) ?
2. Levier : 0 en reel ? Pourquoi ?
3. Poches A/B/C : combien ne doit **jamais** aller sur un derive ?

## Etape 2 : simulation papier ou demo (1 h)

**Scenario invente** : indice a 7 200. Tu "ouvres" lundi un long future fictif F0=7 200, multiplicateur 10, marge 2 500 EUR, ou un call K=7 200 prime 120 EUR (10 contrats fictifs).

Note chaque jour (tableur) :

| Jour | Spot | P&L future | P&L call | Solde marge |
|------|------|------------|----------|-------------|
| Lun | 7200 | 0 | -120 (prime) | 2500 |
| Mar | 7128 | -720 | ? | ? |
| ... | ... | ... | ... | ... |

Mercredi, impose un **choc -10 %** : spot passe a 6 480.

Calcule :

- P&L future = (6480 - 7200) x 10 = **-7 200 EUR** (liquidation bien avant en vrai)
- Call : probablement perte proche de 100 % prime si OTM

## Etape 3 : quiz choc -10 % (15 min)

Sans calculatrice d'abord, estime :

1. Avec levier 5x et capital 1 000 EUR, perte approx sur -10 % sous-jacent ?
2. Marge 2 000, perte -7 200 : que fait le courtier ?
3. Call prime 120, spot -10 % en 2 jours : perte max ?

Reponses attendues (apres calcul) :

1. ~ -50 % compte (5 x 10 %)
2. Liquidation / appel de marge impossible a honorer
3. Perte max = 120 EUR (prime) si OTM, peut etre 100 %

## Etape 4 : decision ecrite (10 min)

Modele :

"Apres ce projet, je [refuse / limite] le levier parce que ___. Mon prochain geste concret est ___ (relire ch. 13, refaire atelier, rien en reel). Date de relecture : ___."

## Petite histoire

Max complete le choc -10 % et voit -7 200 sur marge 2 500. Il ecrit en gros : "Ce n'est pas un bug, c'est le contrat." Il supprime l'app de CFD de son telephone. Nora garde son PEA et achete un put fictif sur papier pour comprendre l'assurance. Deux chemins, meme clarte.

## Erreur classique

Transformer le mini-projet en "je vais me refaire en reel avec 50 EUR". Ou sauter le choc -10 % parce que c'est "impossible". Les gaps arrivent.

## En vrai

Range ton dossier (4 pages max). Relis-le dans 3 semaines. Si tu as oublie pourquoi tu as refuse le levier, relis ch. 6 et 11.

## A toi

Fais les etapes 1 a 4 cette semaine. Posture A ou B, mais choc -10 % obligatoire.

:::retenir
Mini-projet = papier ou demo, choc -10 % inclus, decision ecrite. Refuser le levier est une reponse valide et mature.
:::

:::attention
Ne transfere pas les montants fictifs sur un compte reel "pour voir en vrai avec peu".
:::

:::astuce
Garde le tableau du choc -10 % : c'est ton vaccin anti-FOMO quand une pub promet x10.
:::
