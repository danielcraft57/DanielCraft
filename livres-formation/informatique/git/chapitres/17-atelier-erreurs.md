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

Lis d'abord la **derniere** partie du message. Ne panic pas sur le pave rouge. Lance `git status` pour savoir ou tu es. Une action a la fois.

## Exercices

Provoque un push reject (pull manquant) et reparer. Provoque un conflit et le resoudre. Ajoute un secret au mauvais moment, puis retire-le avec `rm --cached`.

## Check

Tu sais expliquer 4 messages courants sans google.

## Traduction rapide

Si le working tree est clean, rien a commit. Untracked : add ou ignore. Ahead : push. Behind : pull. Rejected : pull puis push. Conflict : editer + add + commit.

Garde ces reflexions sous la main la premiere semaine.
