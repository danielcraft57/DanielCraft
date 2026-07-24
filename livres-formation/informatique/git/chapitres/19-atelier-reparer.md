# Chapitre 19 - Atelier : reparer sans paniquer

## Cas 1 - Mauvais fichier stage

```bash
git restore --staged mauvais.txt
```

## Cas 2 - Mauvais message (pas encore push)

```bash
git commit --amend -m "Meilleur message"
```

## Cas 3 - Commit en trop (pas push)

```bash
git reset --soft HEAD~1
```

## Cas 4 - Commit deja push (equipe)

```bash
git revert HEAD
git push
```

## Cas 5 - Mauvaise branche

Tu as commit sur `main` au lieu de `feature` :

```bash
git switch -c feature/oubli
git switch main
git reset --hard HEAD~1
git switch feature/oubli
```

Seulement si le commit n'est pas utile sur `main` et pas partage.
Sinon : demande conseil / fais une PR depuis ce commit autrement.

## Cas 6 - Conflit qui te depasse

```bash
git merge --abort
```

Repars. Demande de l'aide. Reessaye plus tard.

## Checklist anti-stress

Commence par `git status`, puis `git log --oneline -5`. Demande-toi : est-ce deja pousse ? Suis-je seul sur la branche ? Alors seulement : restore / reset / revert.

## Exercice final atelier

Casse volontairement (mauvais add, mauvais message, petit conflit).
Repare avec la methode ci-dessus.
Ecris dans `notes.md` ce que tu as fait.

## En vrai

Les seniors aussi cassent.
La difference : ils savent lire `status` et choisir un outil sur.
