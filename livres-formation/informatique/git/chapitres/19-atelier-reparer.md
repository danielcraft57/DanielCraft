# Chapitre 19 - Atelier : reparer sans paniquer

Les seniors aussi cassent. La difference : ils savent lire **`status`** et choisir un outil sur. Cet atelier transforme la panique en **checklist**. Chez DanielCraft, on prefere un repair lent et juste a un reset heroique. La vitesse sans lecture produit des degats. La lenteur methodique produit des projets qui tiennent. Toi, tu vas te constituer une boite a outils mentale : savoir quoi faire, dans quel ordre, selon que c'est pousse ou non.

Lea commence toujours par `status` + `log --oneline -5`. Max copie le dossier s'il doute. Sam fait casser volontairement, puis reparer, puis ecrire dans `notes.md`. Objectif : casser volontairement, reparer, documenter. Duree : 30 a 45 minutes. Ce n'est pas un permis de destruction. C'est un entrainement de pompier : tu allumes un petit feu controle pour apprendre a l'eteindre.

Panique. Stop. Status. Log. Questions : pousse ? seul ? Puis une hypothese. Une commande. Nouveau status. Si ca derape : abort, copie, aide. Chez DanielCraft, la checklist est le vrai super-pouvoir. Lea la sort avant les commandes. Max aussi, maintenant. Sam l'affiche au tableau pendant l'atelier. Toi, tu vas l'imprimer mentalement.

:::retenir
En local, pas pousse : reset possible. Deja pousse / equipe : revert. Si tu hesites, copie le dossier ailleurs avant tout `--hard`.
:::

## Ce que ce n'est pas

Ce n'est pas un permis de `reset --hard` partout. Ce n'est pas non plus "Google la premiere commande et colle". Checklist d'abord. Est-ce deja pousse ? Suis-je seul sur la branche ? Alors seulement : restore / reset / revert. Ce n'est pas une humiliation si tu abort un merge. C'est de la gestion de risque. Ce n'est surtout pas "reparer sans documenter" : tu re-paniqueras la prochaine fois. Ecris. Ton `notes.md` devient ton manuel perso.

## Checklist anti-stress

Commence par `git status`, puis `git log --oneline -5`. Demande-toi : est-ce deja pousse ? Suis-je seul sur la branche ? Une hypothese, une commande, un nouveau `status`. Si un conflit te depasse : `git merge --abort`, respire, reessaye plus tard. Si tu hesites sur `--hard`, copie le dossier ailleurs. La copie n'est pas une preuve de faiblesse. C'est une assurance. Max l'appelle "le parachute USB". Lea copie dans un dossier `_backup` date. Sam exige la copie avant tout marteau en atelier debutant.

## Cas 1 - Mauvais fichier stage

```bash
git restore --staged mauvais.txt
```

Le fichier reste sur le disque. Il sort juste de l'index. Tu as retire un objet de la table avant la photo. Pas de drame.

## Cas 2 - Mauvais message (pas encore push)

```bash
git commit --amend -m "Meilleur message"
```

Corrige la legende de la derniere photo. Seulement si pas encore pousse / pas partage. Sinon, discussion d'equipe. Lea amend souvent en solo local. Jamais apres un push partage sans accord.

## Cas 3 - Commit en trop (pas push)

```bash
git reset --soft HEAD~1
```

Annule le commit, garde les changements stages. Tu peux recommencer proprement. Utile quand tu as photographie trop tot.

## Cas 4 - Commit deja push (equipe)

```bash
git revert HEAD
git push
```

Nouveau commit d'annulation. Historique honnete. Prefere ca sur `main` partage. C'est le geste adulte du chapitre 15, mis en pratique ici.

## Cas 5 - Mauvaise branche

Tu as commit sur `main` au lieu de `feature` :

```bash
git switch -c feature/oubli
git switch main
git reset --hard HEAD~1
git switch feature/oubli
```

Seulement si le commit n'est pas utile sur `main` et pas partage. Sinon : demande conseil / fais une PR depuis ce commit autrement. Ne recopie pas cette sequence les yeux fermes. Lis la condition. Sam insiste la-dessus. Lea aussi.

## Cas 6 - Conflit qui te depasse

```bash
git merge --abort
```

Repars. Demande de l'aide. Reessaye plus tard. Ce n'est pas un aveu d'echec. C'est de la gestion de risque. Max abort. Lea abort. Sam celebre l'abort. Tu peux aussi. Sam a vu un eleve vouloir `--hard` tout de suite : il a fait lire la checklist d'abord. Le geste dangereux est devenu inutile. C'est le succes de l'atelier.

:::astuce
Avant tout `--hard`, dis a voix haute : "est-ce pousse ? suis-je seul ?". Si tu hesites, copie le dossier. La checklist bat le marteau.
:::

## Petite histoire

Max a amend un message non pousse, sourit. Lea a revert un commit pousse sans reecrire l'histoire des autres. Sam a vu un eleve vouloir `--hard` tout de suite : il a fait lire la checklist d'abord. Le geste dangereux est devenu inutile. Chez DanielCraft, c'est le succes de l'atelier. Pas "savoir detruire vite". Savoir choisir lentement. La prochaine panique reelle, tu sortiras la checklist avant le marteau. Tu passeras pour quelqu'un de calme. Tu le seras vraiment.

## Erreur classique

Enchainer reset + amend + force push. Reparer sans savoir si c'est pousse. Oublier d'ecrire ce que tu as fait - tu re-paniqueras la prochaine fois. Documente. Ton `notes.md` devient ton manuel perso. Autre piege : reparer le symptome (message rouge) sans comprendre la cause (mauvaise branche, pull manquant, secret stage). Status d'abord. Toujours.

## Exercice final atelier

Casse volontairement (mauvais add, mauvais message, petit conflit). Repare avec la methode ci-dessus. Ecris dans `notes.md` ce que tu as fait. Bonus : un cas "deja push" avec `revert`. Chronometre sans stress. Vise la clarte du compte-rendu plus que la vitesse.

## En vrai

Imprime mentalement la checklist. La prochaine panique, sors-la avant les commandes. Dis-la a voix haute si besoin. Lea le fait encore parfois a 23h. Max aussi. Sam le recommande sans ironie. Le rituel bat l'ego.

## A toi

Fais l'exercice final. Puis explique a voix haute quand tu choisis `restore`, `reset`, ou `revert`. Si tu distingues les trois sans notes, tu as gagne l'atelier. Garde ton `notes.md` : c'est ton diplome anti-panic.
