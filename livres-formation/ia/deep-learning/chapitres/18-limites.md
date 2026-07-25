# Chapitre 18 - Limites du deep learning

Le deep learning est puissant et borne. Il demande des donnees, du calcul, de l'ingenierie. Il peut etre opaque. Il peut etre fragile hors distribution. Il peut encoder des biais. Il peut couter cher en inference a grande echelle. Il peut donner une illusion de comprehension. Chez DanielCraft, voir les limites n'est pas du pessimisme : c'est du professionnalisme.

Ce chapitre ne tranche pas tous les debats ethiques. Il exige que tu les voies assez pour decider en adulte.

:::retenir
Puissance ≠ comprehension. Prevois repli, abstention, mesure hors distribution, et couts reels.
:::

## Ce que ce n'est pas

Ce n'est pas une raison d'abandonner. Ce n'est pas non plus une excuse pour tout automatiser "parce que le score labo est beau". Ce n'est pas "les modeles simples n'ont pas de limites" : ils en ont d'autres. Et ce n'est pas uniquement un sujet recherche : en production, les limites arrivent en ticket support.

## Ce qu'il ne remplace pas

La definition du probleme. La qualite des labels. La decision ethique. La responsabilite legale. La connaissance terrain. Les modeles simples quand ils suffisent. Les processus humains de verification. Ines peut avoir un excellent CNN ; elle reste responsable si une mauvaise piece passe. Lea le rappelle dans ses CGV de projet. Max le sent dans sa garantie chantier.

## Image mentale : robustesse

Change l'eclairage, l'accent, le format de document, la saison : les performances chutent parfois. Les adversaires peuvent tromper certains modeles avec des perturbations. En production, prevois des replis : regles, humain, **abstention**. Parfois la meilleure sortie est "je ne sais pas / humain requis". Concois un seuil d'abstention. En vision comme en langage, l'abstention sauve des catastrophes.

:::idee
Ecris une phrase d'abstention pour ton projet avant d'ecrire une phrase de deploiement.
:::

## Environnement et cout

Entrainer et servir de gros modeles a un impact energie / argent. Utilise le plus petit modele qui fait le job. Prefere reutiliser. Mesure avant d'empiler. Sam fait calculer a ses eleves un ordre de grandeur : pas pour culpabiliser, pour choisir. Lea refuse les devis "on scale d'abord, on mesure apres".

## Petite histoire

Ines a deploye sans seuil d'abstention. Le modele classait "avec confiance" des pieces hors catalogue vers la classe la plus proche. Clients mecontents. Elle a ajoute un score minimum + file humaine. Le taux d'automatisation a baisse. La confiance client a monte. Chez DanielCraft, on appelle ca une victoire.

## Biais et angles morts

Les donnees d'entrainement portent des desequilibres. Un modele vision peut moins bien marcher sur certains eclairages, peaux, lieux, appareils. Un LLM peut reproduire des stereotypes ou des angles culturels. Tu n'as pas a tout resoudre seul. Tu as a tester des sous-groupes, ecouter les echecs, documenter. Ignorer n'est pas neutre.

## Erreur classique

Croire que "plus de deep learning" efface les limites. Autre piege : cacher les echecs pour proteger le score. Troisieme : confondre opacite du modele et absence de responsabilite humaine.

:::attention
Utiliser un outil puissant sans regarder ses effets collateraux, ce n'est pas de la neutralite technique. C'est une decision. Assume-la.
:::

## En vrai

Liste 5 limites qui s'appliquent a ton projet. Pour chacune, une mitigation : humain, regle, plus de donnees, modele plus petit, abstention, monitoring...

## A toi

Tableau 5 lignes : limite / impact / mitigation / responsable. Signe en bas. C'est ton mini plan de risque.

## Illusion de comprehension

Un texte fluide, une classe predite, une heatmap jolie : rien de tout cela ne prouve une comprehension humaine. Ce sont des comportements utiles sous conditions. Le chapitre LLM l'a dit ; les limites le martelent. Garde l'humilite quand tu presentes a un non-tech : tu vends un outil borne, pas un oracle.

## Hors distribution : trois exemples

Photo de nuit alors que le train etait de jour. Accent ou jargon absent du corpus. Format PDF scanne alors que le modele a vu du texte propre. Dans chaque cas, le systeme peut repondre quand meme - avec assurance. D'ou abstention et monitoring. Sam collectionne ces exemples pour sa classe ; Ines pour son journal d'incidents.

## Limites legales et organisationnelles

Qui est responsable si le modele se trompe ? Quelles donnees a-t-on le droit d'envoyer a une API ? Qui relit ? Ces questions ne sont pas "hors sujet technique". Elles bornent le deploiement autant qu'un manque de VRAM. Lea les met en page 1 du cadrage.
