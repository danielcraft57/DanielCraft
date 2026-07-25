# Chapitre 14 - Atelier : intuition neurone et couches

Objectif : solidifier l'image mentale sans code obligatoire. Duree visee : environ 30 minutes. Tu sors avec un dessin explicable a un collegue non tech - le meilleur test de comprehension selon DanielCraft.

Cet atelier n'est pas un examen. C'est une gymnastique. Ines le fait avant chaque nouveau projet vision pour "remettre les briques a plat". Lea s'en sert pour briefer. Sam le transforme en exercice de classe.

:::retenir
Si tu peux expliquer ton dessin et la boucle d'apprentissage a quelqu'un, l'atelier a reussi.
:::

## Ce que ce n'est pas

Ce n'est pas un TP PyTorch obligatoire. Le code optionnel existe pour les curieux ; le coeur est papier + oral. Ce n'est pas non plus "faire joli". Un schema sale et juste bat un schema parfait et creux.

## Image mentale de depart

Un neurone : entrees, poids, biais, activation, sortie. Une couche : plusieurs neurones en parallele. Un petit reseau : empilement. Une boucle : batch, avant, loss, arriere, maj des poids, repeter. Tu vas faire vivre ces quatre phrases.

## Exercices (dans l'ordre)

1) Dessine un neurone a 3 entrees, avec poids, biais, activation. Invente des nombres simples et calcule a la main une sortie **ReLU** (max(0, somme)). Ne cherche pas la beaute ; cherche le geste.

2) Empile 2 couches denses sur papier (tailles 3 -> 4 -> 1). Explique oralement le passage avant : que recoit chaque etage, que produit-il ?

3) Ecris la boucle d'apprentissage en 6 etapes. Chronometre une version orale de 40 secondes.

4) Identifie pour ton projet (ou celui d'Ines : pieces sur photo) : entree brute, representation utile imaginee, sortie. Trois fleches suffisent.

5) Option code : un mini reseau toy dans un notebook (meme 20 lignes) pour voir la loss baisser sur une fonction simple. Seulement si tu en as envie et le temps.

:::idee
Fais l'exercice 1 au stylo, pas au clavier. La main ralentit assez pour que le concept accroche.
:::

## Petite histoire

Max a refuse d'abord : "je suis pas developpeur". Lea lui a fait faire le neurone parapluie (pluie, vent, distance). En dix minutes, il expliquait poids et seuil a son apprenti. Le code peut attendre. L'intuition, non.

## Erreur classique

Sauter au code optionnel sans dessin. Ou recopier un schema internet sans nombres. Ou expliquer avec des mots savants pour masquer un trou. Si tu bloques, reviens au chapitre 2 et 5, puis recommence l'oral.

:::attention
L'atelier echoue si tu ne parles a personne. Trouve un humain, meme presse, meme distant.
:::

## En vrai

Appelle ou assieds quelqu'un. Montre le dessin. Demande : "reformule la backprop en une phrase". Si la personne y arrive apres toi, tu as transmis. C'est le livrable invisible.

## Livrable

Une feuille dessinee + 10 lignes d'explication que tu pourrais envoyer a un collegue non tech. Garde la feuille : l'atelier CNN s'appuiera sur la meme discipline de clarte.

## A toi

Coche : neurone calcule, reseau 3-4-1 explique, boucle orale OK, fleches projet OK, explication lue a quelqu'un. Une case vide = cinq minutes de plus, pas un abandon.

## Variante Ines

Remplace le parapluie par "piece A / pas piece A". Entrees inventees : score contour, score texture, score trou. Meme neurone. Plus proche de son appli. Adapte a ton domaine : le transfert d'intuition est le vrai sujet.

## Grille d'auto-evaluation

Apres l'atelier, note 1 a 5 : clarte du dessin, exactitude du calcul ReLU, fluidite de l'oral backprop, pertinence des fleches projet, qualite de l'explication non tech. Tout score sous 3 = cinq minutes de rattrapage cible. Sam utilise la grille en classe ; Lea en autofeedback.

## Piege du vocabulaire savant

Si tu dis "gradient stochastique" mais tu ne sais pas raconter batch / avant / loss / arriere, tu te caches. Inverse la priorite : histoire simple d'abord, mot savant ensuite. Chez DanielCraft, le jargon arrive en recompense de la clarte, pas en camouflage.
