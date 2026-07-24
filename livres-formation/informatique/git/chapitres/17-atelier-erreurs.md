# Chapitre 17 - Atelier : lire les messages Git

Git parle anglais souvent. On traduit.

## "nothing to commit, working tree clean"

Rien a photographier. Tout est deja commit. OK.

## "untracked files"

Fichiers pas encore suivis. `add` si tu les veux. Sinon `.gitignore`.

## "Your branch is ahead of origin/main"

Tu as des commits locaux non pousses. `git push`.

## "Your branch is behind"

Le remote a avance. `git pull` avant de continuer.

## "rejected ... fetch first"

Push refuse. Tire d'abord. Resous. Repush.

## "merge conflict"

Ouvre les fichiers marques. Nettoie. `add`. commit de merge.

## "Permission denied" / auth

Probleme d'identifiants (HTTPS token, SSH key, droits du depot).

## Methode

1. Lis la **derniere** partie du message
2. Ne panic pas sur le pavé rouge
3. `git status` pour savoir ou tu es
4. Une action a la fois

## Exercices

1. Provoque un push reject (pull manquant) et reparer
2. Provoque un conflit et le resoudre
3. Ajoute un secret au mauvais moment, retire-le avec `rm --cached`

## Check

Tu sais expliquer 4 messages courants sans google.
## Traduction rapide

| Message (idee) | Action |
|----------------|--------|
| working tree clean | Rien a commit |
| untracked | add ou ignore |
| ahead | push |
| behind | pull |
| rejected | pull puis push |
| conflict | editer + add + commit |

Garde ce tableau sous la main la premiere semaine.
