# Chapitre 10 - Cherry-pick : reprendre un commit ailleurs

Parfois tu as un commit parfait... mais pas sur la bonne branche. Le fix est sur une feature longue. La prod brule. Tu voudrais juste cette correction sur `main`, sans merger toute la feature. `git cherry-pick` copie un commit (son **diff**) et le rejoue sur ta branche actuelle. Nouveau **hash**, meme idee. Chez DanielCraft, on dit : tu cueilles une **cerise** sur un arbre (une branche) et tu la poses sur un autre plateau. Tu ne demenages pas l'arbre. Tu ne contournes pas la review non plus : tu ouvres quand meme une PR courte.

Max a trois commits sur `feature/refonte-login` :

```text
a111 - prepare la structure
b222 - corrige le timeout session  <-- celui-la est urgent
c333 - nouveau design du formulaire
```

La prod a besoin de `b222` maintenant. Merger toute la feature amenerait le design inacheve. **Cherry-pick** sur une branche `fix/` courte, puis **PR** express :

```bash
git switch main
git pull
git switch -c fix/timeout-session
git cherry-pick b222
```

Si ca s'applique proprement, tu as le fix sur une branche courte. Tu ouvres une PR. Tu merges. La feature de Max continue sa vie. Plus tard, quand la feature rejoindra `main`, Git gerera souvent le doublon assez bien (pas toujours magique : reste attentif). Trouve le commit :

```bash
git log --oneline feature/refonte-login
```

Tu copies le hash court ou long. Tu cherry-pick ce hash.

:::retenir
Cherry-pick egal une cerise urgente, pas le panier entier. Pour une feature complete, passe par une PR normale.
:::

## Conflits et limites

Comme un merge ou un rebase, ca peut conflictuer. Tu resolus, tu `git add`, tu continues :

```bash
git cherry-pick --continue
```

Ou tu abandonnes :

```bash
git cherry-pick --abort
```

Tu peux enchainer plusieurs cherry-picks, ou donner un intervalle selon les cas. Pour debuter, un commit a la fois. C'est plus clair mentalement. Cherry-pick brille pour 1 (parfois 2-3) commits cibles. Pour une feature entiere : merge ou PR normale. Si tu cherry-picks vingt commits d'une feature, tu es en train de merger a la main, mal. Apres cherry-pick, tu as deux commits cousins (meme changement, hash differents) sur deux lignes d'histoire. Les messages restent importants.

:::attention
Si le commit cueilli depend d'un commit precedent non pris, tu peux casser la compilation. Lis `git show` avant de cueillir.
:::

Sam : "Le timeout session casse la prod." Max : "Le fix est dans ma grosse branche refonte, commit b222." Sam : "On cherry-pick b222 sur une fix branche, PR express, on livre. Ta refonte continue." C'est ca, l'outil au service du calendrier. Pas un tour de magie pour eviter le travail : une extraction ciblee. Si `b222` suppose que `a111` a cree une fonction, cherry-pick de `b222` seul peut casser la compilation. Alors tu cherry-picks `a111` puis `b222`, ou tu recrees un fix minimal sur `main` a la main. Lis le commit avant de cueillir la cerise :

```bash
git show b222
```

Lea a appris a noter dans la PR feature : "timeout deja livre via cherry-pick le ...". Quand la grosse branche arrive, moins de surprise.

## Petite histoire

Lea a cherry-picke depuis le mauvais hash. Le code ne compilait plus. Elle a lu `git show`, recommence proprement, PR courte, merge. Quand la refonte de Max est arrivee, Git a vu des changements deja presents. Un conflit "deja applique". Note dans la PR feature : "timeout deja livre via cherry-pick le ...". Respire, resols, continue.

Chez DanielCraft, cherry-pick n'est pas un plan B pour eviter la review. Tu ouvres quand meme une PR courte. Le filet reste.

## Erreur classique

Cherry-pick depuis le mauvais hash. Ou cherry-pick d'un commit qui depend d'un commit precedent non pris. Ou cherry-pick directement sur `main` sans PR alors que `main` est protegee... passe par une branche fix. Autre piege : utiliser cherry-pick pour "eviter la review". Non. Tu ouvres quand meme une PR courte.

:::astuce
Toujours `git show <hash>` avant `git cherry-pick <hash>`. Une minute de lecture evite une heure de debug.
:::

## En vrai

Sur un depot de test, cree une branche avec deux commits distincts (deux fichiers differents). Reviens sur `main`, cherry-pick seulement le second. Verifie que seul le second changement est la :

```bash
git log --oneline -5
git show HEAD
```

Puis ouvre une PR courte meme sur le depot de test. Le geste compte autant que la commande.

## A toi

Ecris dans ton carnet d'equipe : "Cherry-pick egal cerise urgente, pas panier entier." Quand la prod brulera, tu auras la phrase au lieu de la panique. Bonus : ajoute "toujours `git show` avant de cueillir".

## Zoom : urgence sans chaos

La prod brule. La feature est longue. La tentation, c'est de merger tout ou de pousser direct. Cherry-pick + branche fix + PR courte, c'est le chemin du milieu. Lea l'a appris apres un vendredi trop long. Max aussi. Sam l'enseigne avant l'incendie. Chez DanielCraft, on prefere une cerise bien posee a un panier renverse sur `main`.
