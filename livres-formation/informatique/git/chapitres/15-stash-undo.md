# Chapitre 15 - Stash et annuler (avec prudence)

Parfois tu dois changer de branche alors que tu as des modifs pas pretes. Parfois tu as commit trop vite avec un mauvais message. Parfois tu dois annuler quelque chose deja partage avec l'equipe. Ce chapitre te donne des outils - et surtout une **regle d'or** qui evite les catastrophes. Chez DanielCraft, on enseigne la prudence avant la puissance : un **`reset --hard`** mal place fait plus de degats qu'un conflit bien resolu en quinze minutes. La puissance sans frein n'est pas du professionnalisme. C'est de la roulette.

Lea **stash** pour repondre a une urgence client sans committer un brouillon a moitie. Max a decouvert **`revert`** apres avoir panique sur `main` partage. Sam interdit `--hard` en atelier tant que `status` n'a pas ete lu a voix haute devant la classe. Trois postures, une meme discipline : lire, comprendre si c'est local ou partage, puis agir une fois. Toi, tu vas apprendre a choisir. Pas a enchainer trois resets "au hasard" en esperant que ca marche.

Regle d'or : en local, pas pousse -> **reset** possible avec prudence. Deja pousse / equipe -> **revert** (ou discussion avant tout geste heroique). Avant tout geste destructeur : `git status`, `git log --oneline -5`, puis demande-toi "est-ce pousse ?", "suis-je seul sur la branche ?". Si tu as un doute, copie le dossier ailleurs. Respire. Puis choisis une commande, pas trois d'un coup. Max appelle ca "la pause cafe anti `--hard`". Lea appelle ca "la checklist". Sam appelle ca "la survie".

:::attention
`reset --hard` sur un commit deja partage peut effacer le travail des autres. En equipe, prefere `revert`. C'est le geste "adulte".
:::

## Ce que ce n'est pas

Annuler, ce n'est pas "Git efface internet" ni "personne ne verra jamais". Ce n'est pas non plus gratuit : `restore` jette des modifs non commit. `reset --hard` jette encore plus, sans filet. Ce n'est pas interchangeable au hasard : stash met de cote temporairement, restore annule local sur un fichier, reset reecrit l'historique local, revert ajoute un commit d'annulation propre. Et ce n'est surtout pas la meme chose avant ou apres un push partage. La question "est-ce deja pousse ?" change tout. Si tu ne sais pas repondre, tu n'es pas pret a taper `--hard`.

Ce n'est pas non plus "stash = sauvegarde eternelle". Stash est un tiroir temporaire. Ne laisse pas pourrir dix stash oublies pendant trois mois. Lea nettoie sa pile chaque vendredi. Max a perdu le fil d'un stash trop vieux. Sam limite a deux stash max en atelier.

## stash

Quand tu es en plein milieu d'un travail et qu'une urgence tombe :

```bash
git stash
git switch autre-branche
# ... tu fais le fix urgent ...
git switch -
git stash pop
```

`stash` = met de cote proprement. `stash pop` = recupere et enleve de la pile. Pour voir ce qui dort :

```bash
git stash list
```

Utile. Pas un tiroir magique infini. Si `stash pop` cree un conflit, c'est normal parfois : tu as change la meme zone entre-temps. Resous comme un conflit classique. Puis continue. Lea l'a vecu. Cinq minutes. Pas de drame.

## restore et reset (apercus)

Pour annuler des modifs sur un fichier non commit :

```bash
git restore fichier.txt
```

Revient a la derniere version commit pour ce fichier. Les changements non commits sont perdus. Pour retirer du staging sans perdre le fichier :

```bash
git restore --staged fichier.txt
```

Pour annuler un commit local pas encore pousse :

```bash
git reset --soft HEAD~1
```

Annule le commit, garde les changements stages. Ou :

```bash
git reset HEAD~1
```

Annule le commit, garde les changements non stages. Enfin, le marteau :

```bash
git reset --hard HEAD~1
```

Revient en arriere et jette les modifs. Puissant. Dangereux. Pas sur un commit deja partage sans discussion d'equipe. Sam le montre une fois, puis range le marteau. Lea ne l'utilise presque jamais. Max l'a utilise trop tot, une fois, sur un depot de test. Heureusement, pas en prod.

## revert (plus sur en equipe)

```bash
git revert HEAD
```

Cree un nouveau commit qui annule le precedent. L'historique reste honnete : l'erreur est visible, l'annulation aussi. Prefere ca sur `main` partage. Chez DanielCraft, c'est souvent le geste "adulte" quand plusieurs personnes lisent le meme depot. Tu n'effaces pas le passe. Tu ajoutes une correction visible. Les autres comprennent. L'histoire reste lisible. Max a fait un commit "oops", puis `revert`, puis regarde le `log` : l'erreur etait la, l'annulation aussi, personne n'a perdu le fil.

:::retenir
En local, pas pousse : reset possible. Deja pousse / equipe : revert. Stash = tiroir temporaire, pas sauvegarde eternelle.
:::

## Petite histoire

Max a fait un commit "oops" sur une branche deja mergee sur `main` partage. Il a panique une seconde, puis `revert`, puis regarde le `log` : l'erreur etait la, l'annulation aussi, l'histoire restait lisible. Lea a stash, change de branche, corrige un bug hot pour un client, revenu sur sa feature, `stash pop` avec un petit conflit qu'elle a resolu en cinq minutes. Sam a fait copier le dossier avant un `--hard` "pour voir" en atelier. La copie n'a pas servi ce jour-la. Le reflexe, si. Bonne assurance. Chez DanielCraft, on celebre le geste juste plus que le geste spectaculaire.

## Erreur classique

`--hard` sur un commit pousse "parce que personne ne regardera". `stash pop` avec conflits sans comprendre d'ou ils viennent. `commit --amend` apres push sur une branche partagee. Autre piege : enchainer trois resets "au hasard" en esperant que ca marche - une action, un controle `status`, ensuite seulement la suivante. Encore un piege : confondre restore (fichier local) et revert (nouveau commit d'annulation). Deux outils. Deux moments. Deux risques.

## En vrai

Avant un `--hard`, respire. Copie le dossier ailleurs si tu as un doute. Modifie un fichier sur ton carnet de tests, fais `stash`, verifie que `status` est propre, puis `stash pop`. Tu verras que rien n'a disparu dans le neant. Git range. Il ne te punissait pas. Ensuite fais un petit `revert` sur une branche de test. Regarde le log. Sens l'honnetete de l'historique.

## A toi

Fais un commit "oops" sur une branche de test. Annule-le avec `revert`. Regarde le `log`. Bonus : scenario stash complet (modifs -> stash -> switch -> retour -> pop). Ecris en trois lignes ta regle d'or perso : quand tu utilises restore, reset, revert, stash. Colle ca dans `notes.md`. Tu y reviendras a l'atelier reparer.
