# Chapitre 19 - Staking et mining (idee)

**Mining** (preuve de travail) et **staking** (preuve d'enjeu) sont deux facons de participer a la securite / au fonctionnement d'un reseau - avec des economiques, des contraintes et des risques tres differents. Chez DanielCraft, on les lit comme des **mecanismes**, pas comme des livrets. Le mot "yield" sur une landing page n'est pas un taux de livret assure.

Disclaimer pedagogique : rendements variables, parfois illusoires apres inflation du jeton, frais, et baisse du sous-jacent. Pas un conseil de staker ou de miner. Perte totale possible (phishing de site "stake", slashing, bug, lockup pendant un crash, materiel de mining invendable). Exemples en euros inventes.

Nora voit "APY 8 %" et entend "interet". Max entend "usine a electricite". Sam entend "smart contract + lock". Les trois doivent ralentir.

## Mining : industrie, pas hobby laptop

Le mining (ex. logique historique Bitcoin) consomme du calcul et de l'energie pour proposer des blocs et gagner des recompenses (plus frais). En pratique contemporaine grand public, c'est surtout une **industrie** : machines specialisees, electricite, bruit, chaleur, maintenance, difficulte du reseau, prix de l'actif, revente du hardware. Ce n'est pas "lancer un exe sur un PC gaming et devenir libre".

Risques miner : electricite plus chere que le revenu ; hardware qui se deprecie ; chaleur / voisinage ; complexite fiscale et legale locale ; concentration industrielle face a laquelle un amateur est handicape. Pour ce livre : comprendre que mining = infra, pas un bouton "earn" equivalent au staking retail.

Si quelqu'un te vend un "kit mining garanti" avec rendement fixe et urgence, relis le chapitre arnaques. La garantie marketing et le mining reel cohabitent mal.

## Staking : lock, recompenses, risques

Le staking consiste typiquement a immobiliser des tokens pour participer au consensus (directement ou via delegue / pool / validateur) et recevoir des recompenses. Variantes : staking natif, staking via exchange (contrepartie plateforme), liquid staking (jeton derive + smart contracts).

Risques a nommer sans fard :
- **Lockup / unbonding** : tu ne sors pas instantanement ; pendant le delai, le prix peut chuter.
- **Slashing** : penalites si le validateur se comporte mal (selon protocole).
- **Smart contract / protocole** : bugs, exploits, depeg du jeton liquide de staking.
- **Contrepartie** : si tu stake sur un CEX, tu ajoutes le risque plateforme.
- **Phishing** : faux sites "stake now" qui demandent la seed ou une approval drain.

Lecture prudente d'un APY : un staking affiche 4 % sur un actif qui fait -40 % sur la periode = net douloureux. Compare toujours rendement affiche et volatilite du sous-jacent. Exemple invente : 2 000 EUR staked, "4 %" annuel nominal ~ 80 EUR si tout va bien - pendant que -30 % sur l'actif => -600 EUR de mark-to-market. Le yield n'a pas "protege". Il a parfois console.

## Staking vs mining (tableau mental en prose)

Mining = capital hardware + energie + operation ; revenu lie a la puissance relative et au prix ; sortie = vendre des machines. Staking = capital tokens + choix de validateur / contrat ; revenu en tokens ; sortie = unlock selon regles. Mining te met dans une usine. Staking te met dans un calendrier de lock et une surface logicielle. Ni l'un ni l'autre n'annule le risque de prix. Les deux attirent des arnaques paralleles ("cloud mining miracle", "stake x2 rewards").

## Petite histoire

Sam clique un site inconnu "x2 staking rewards". Champ seed. Il ferme, sue, relit arnaques. Max stake via un acteur connu, montant modeste, lit la duree d'unlock **avant** de locker, accepte que le rendement ne compensera pas un -50 %. Nora refuse le cloud mining "cle en main" d'une pub : trop beau, trop urgent. DanielCraft valide le refus autant que le staking prudent - et refuse le mining cosplay.

## Erreur classique

Staker l'argent du loyer pour "l'APY". Signer sur un site de staking non verifie. Ignorer l'unbonding. Confondre liquid staking token avec cash. Acheter des machines sur promesse de ROI fixe. Oublier la fiscalite potentielle des recompenses (journal !).

## En vrai

Si tu considers le staking : ecris trois champs avant tout clic - montant, duree / condition de sortie, risques nommes (lock, contrat, contrepartie). Si mining : ecris electricite + hardware + "est-ce un metier ?". Souvent la reponse honnete est non.

## A toi

Complete : "Si staking : montant = ... ; unlock = ... ; je refuse tout site qui demande la seed." Ou ecris "pas de staking / mining pour l'instant" - reponse valide.

:::retenir
Staking = rendement + contraintes + risques. Mining = industrie, pas un hobby laptop.
:::

:::attention
Site staking + demande seed = arnaque. APY ne neutralise pas un -40 % sur l'actif.
:::

:::astuce
Lis la duree de unlock / unbonding avant de locker le moindre token.
:::
