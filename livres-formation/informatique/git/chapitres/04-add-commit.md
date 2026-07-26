# Chapitre 4 - add et commit (la photo)

Le duo du quotidien : `git add` pour preparer, puis `git commit` pour prendre la photo. Sans ce duo, tu modifies des fichiers, mais Git n'enregistre pas d'etape claire. Avec ce duo, tu construis un album lisible. Chez DanielCraft, on repete : un **commit** = une etape claire. Pas "update". Pas "wip final vrai". Un **message** qui dit quoi / pourquoi. Si demain tu ouvres `log --oneline` et que tu rougis, le probleme n'est pas Git. C'est la legende de la photo.

Lea commit souvent, petit. Une correction de CSS, un commit. Une section de page, un commit. Max commit moins souvent au debut, puis comprend qu'il perd la finesse de l'historique : impossible de revenir juste avant le bug sans tout perdre. Sam interdit les messages "asdf" en atelier. Trois styles, une meme exigence : demain, ton `log` doit se lire comme un journal de bord, pas comme un griffonnage de fin de soiree.

Tu vas aussi rencontrer `status` en boucle. Avant `add`, apres `add`, apres `commit`. Ce n'est pas de la paranoia. C'est le tableau de bord. Tu regardes ce qui est stage, ce qui ne l'est pas, ce qui est ignore. Tu decides. Puis tu photographies. Le geste exact : tu ranges sur la table ce que tu veux dans la photo (`add`), tu declenches (`commit`) avec une legende (`-m`), et `log --oneline` te montre l'album compact.

:::retenir
`add` prepare. `commit` photographie. Sans message clair, tu as une photo sans legende.
:::

## Ce que ce n'est pas

`add`, ce n'est pas "envoyer sur GitHub". `commit`, non plus. Ce n'est pas non plus une sauvegarde cloud. C'est une photo locale dans l'historique. Ce n'est pas obligatoire d'ajouter tout avec `git add .` les yeux fermes : regarde `status` avant. Tu ne veux pas photographier un secret. Et ce n'est surtout pas `commit --amend` en mode reflexe sur un commit deja partage : prudence. Amend est un outil local, pour corriger la derniere photo avant de la montrer a tout le monde.

Ce n'est pas non plus "un commit par jour maximum". Au contraire : plusieurs petits commits clairs battent un mega-commit de trois jours. Lea le sait. Max l'a appris apres avoir du demeler un commit "toute la feature". Sam chronometre la lisibilite du log, pas le nombre de commits.

## Ajouter et committer

```bash
git add readme.txt
git status
```

Le fichier passe en "staged" (index). Pret pour le commit.

```bash
git add .
```

Le point = "tout ce qui a change ici". Pratique. Mais regarde `status` avant.

```bash
git commit -m "Premier commit : readme de base"
```

`-m` = message en une ligne. Prefere un verbe a l'imperatif : "Ajouter", "Clarifier", "Corriger". On detaille les messages au chapitre 12. Des maintenant, vise quelque chose que tu comprendras demain matin.

## Voir que ca a marche, puis continuer

```bash
git status
git log --oneline
```

`status` devrait dire que rien ne reste a commit. `log` montre ta photo. Change `readme.txt`, puis :

```bash
git status
git add readme.txt
git commit -m "Clarifier le titre du carnet"
```

Chaque commit = une etape claire. Lea lit ses messages comme un journal de bord. Max cree `todo.txt` avec 3 taches, commit, coche une tache, commit encore : son `log --oneline` raconte une histoire en quatre lignes. Sam demande aux eleves de lire le log d'un camarade : si personne ne comprend, on reecrit les prochaines legendes.

## Amend (apercu, avec prudence)

Tu viens de commit et tu as oublie un fichier ?

```bash
git add fichier_oublie.txt
git commit --amend --no-edit
```

Ca refait le dernier commit. Ne l'utilise pas sur un commit deja pousse si tu travailles en equipe (sauf si tu sais pourquoi). Sam le montre, puis dit "maintenant oublie-le une semaine". Lea amend seulement quand elle est seule sur la branche et que rien n'est parti sur le remote. Max a amend trop tot une fois, force-push ensuite, et a compris pourquoi Sam avait dit non.

## Petite histoire

Lea a fait deux commits sur un readme. Le premier "creation". Le second "ajout section contact". Un client a demande "c'etait quoi avant ?". Elle a montre `log` et `diff`. Credibilite immediate. Chez DanielCraft, un historique clair est une forme de professionnalisme - meme en solo. Max, lui, a d'abord commit "aaa" puis "bbb". Quand Sam a projete le log, la classe a ri. Max aussi. Puis il a recommence avec des messages propres. La honte productive marche mieux qu'un long sermon.

## Erreur classique

Message "update". `add .` sans lire `status`. Croire que commit pousse en ligne. Oublier `add` puis s'etonner que le commit "n'a rien". Autre piege : un seul mega-commit de trois jours de travail - impossible a relire, impossible a revenir proprement. Encore un piege : committer des fichiers generes ou des secrets "pour plus tard on nettoiera". Non. Plus tard, le secret est deja dans l'historique.

:::attention
`git add .` ajoute tout le dossier. Regarde `status` avant : un `.env` oublie peut finir dans l'historique.
:::

## En vrai

Apres chaque commit, `git log --oneline`. Tu dois voir tes messages s'empiler. Si un message te fait honte, c'est un signal : ecris mieux le prochain, pas un roman sur le passe. Fais deux ou trois photos aujourd'hui sur ton carnet de tests. Sens le rythme. C'est ce rythme que tu rejoueras sur un vrai projet.

## A toi

Fais 2 commits : d'abord la creation du readme, puis l'ajout d'une ligne. Puis cree `todo.txt` avec 3 taches, commit, coche une tache, commit encore. Quatre photos. Un album qui parle. Demain, relis `log --oneline` sans ouvrir les fichiers : tu dois comprendre l'histoire.
