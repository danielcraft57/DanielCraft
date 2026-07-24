# Chapitre 10 - Cherry-pick : reprendre un commit ailleurs

Parfois tu as un commit parfait... mais pas sur la bonne branche. Le fix est sur une feature longue. La prod brule. Tu voudrais juste cette correction sur `main`, sans merger toute la feature.

`git cherry-pick` copie un commit (son diff) et le rejoue sur ta branche actuelle. Nouveau hash, meme idee.

## L'image

Chez DanielCraft, on dit : tu cueilles une cerise sur un arbre (une branche) et tu la poses sur un autre plateau. Tu ne demenages pas l'arbre.

## Un cas concret

Max a trois commits sur `feature/refonte-login` :

```text
a111 - prepare la structure
b222 - corrige le timeout session  <-- celui-la est urgent
c333 - nouveau design du formulaire
```

La prod a besoin de `b222` maintenant. Merger toute la feature amenerait le design inacheve. Cherry-pick :

```bash
git switch main
git pull
git switch -c fix/timeout-session
git cherry-pick b222
```

Si ca s'applique proprement, tu as le fix sur une branche courte. Tu ouvres une PR. Tu merges. La feature de Max continue sa vie. Plus tard, quand la feature rejoindra `main`, Git gerera souvent le doublon assez bien (pas toujours magique : reste attentif).

## Trouver le commit

```bash
git log --oneline feature/refonte-login
```

Tu copies le hash court ou long. Tu cherry-pick ce hash.

## Conflits pendant un cherry-pick

Comme un merge ou un rebase, ca peut conflictuer. Tu resolus, tu `git add`, tu continues :

```bash
git cherry-pick --continue
```

Ou tu abandonnes :

```bash
git cherry-pick --abort
```

## Plusieurs commits

Tu peux enchaine plusieurs cherry-picks, ou donner un intervalle selon les cas. Pour debuter, un commit a la fois. C'est plus clair mentalement.

## Ce n'est pas un remplacement de merge

Si tu cherry-picks vingt commits d'une feature, tu es en train de merger a la main, mal. Cherry-pick brille pour 1 (parfois 2-3) commits cibles. Pour une feature entiere : merge ou PR normale.

## Attention a l'historique

Apres cherry-pick, tu as deux commits cousins (meme changement, hash differents) sur deux lignes d'histoire. Les messages restent importants : garde un message qui dit encore le pourquoi. Si besoin, retouche le message au moment du pick (options avancees) ou amend local avant push.

## Erreur classique

Cherry-pick depuis le mauvais hash. Ou cherry-pick d'un commit qui depend d'un commit precedent non pris (le code ne compile plus). Ou cherry-pick directement sur `main` sans PR alors que `main` est protegee... passe par une branche fix.

Autre piege : utiliser cherry-pick pour "eviter la review". Non. Tu ouvres quand meme une PR courte.

## En vrai

Sur un depot de test, cree une branche avec deux commits distincts (deux fichiers differents). Reviens sur `main`, cherry-pick seulement le second. Verifie que seul le second changement est la. Sens l'outil.

```bash
git log --oneline -5
git show HEAD
```


## Dialogue d'equipe typique

Sam : "Le timeout session casse la prod."
Max : "Le fix est dans ma grosse branche refonte, commit b222."
Sam : "On cherry-pick b222 sur une fix branche, PR express, on livre. Ta refonte continue."

C'est ca, l'outil au service du calendrier. Pas un tour de magie pour eviter le travail : une extraction ciblee.

## Dependances entre commits

Si `b222` suppose que `a111` a cree une fonction, cherry-pick de `b222` seul peut casser la compilation. Alors tu cherry-picks `a111` puis `b222`, ou tu recrees un fix minimal sur `main` a la main. Lis le commit avant de cueillir la cerise.

```bash
git show b222
```

## Apres le merge du cherry-pick, la feature longue

Quand la refonte de Max arrivera, Git pourra voir des changements deja presents. Parfois ca se passe bien. Parfois il y a un conflit "deja applique". Respire, resols, continue. Note dans la PR feature : "timeout deja livre via cherry-pick le ...".


## A toi

Ecris dans ton carnet d'equipe : "Cherry-pick = cerise urgente, pas panier entier." Quand la prod brulera, tu auras la phrase au lieu de la panique.
