# Chapitre 17 - Atelier : lire les messages Git

Git parle anglais souvent. On traduit. Une **erreur** ou un **status**, c'est un GPS, pas une insulte personnelle. Chez DanielCraft, cet atelier forme l'autonomie : si tu sais lire quatre messages courants sans Google, tu te debloques seul neuf fois sur dix. Lea gagne des heures par mois. Max a arrete de paniquer devant le pave rouge du terminal. Sam exige la derniere partie du message avant toute aide en classe : "traduis d'abord, on discute ensuite". Toi, tu vas te constituer un petit lexique vivant, dans un fichier, avec tes mots.

Objectif : reconnaitre et reparer. Duree : 25 a 40 minutes. Materiel : ton carnet de tests + un remote GitHub si possible (prive OK). Sans remote, les exercices ahead/behind perdent une partie de leur sens - fais-les quand tu peux. Un atelier fait a fond bat trois ateliers survoles en dix minutes. Sam chronometre le process, pas la vitesse de clic.

Le terminal t'envoie un message. Tu lis la fin d'abord - souvent la plus claire. Tu traduis en une phrase francaise. Tu lances `status` pour situer la carte. Tu choisis une action. Tu verifies. Si ca n'a pas marche, tu ne lances pas dix autres commandes. Tu relis. Tu ajustes. C'est un dialogue. Pas un combat. Chez DanielCraft, le rouge veut dire "attention", pas "fin du monde".

:::retenir
Ahead = push. Behind = pull. Rejected = pull puis push. Conflict = editer + add + commit. Garde ces reflexes la premiere semaine.
:::

## Ce que ce n'est pas

Ce n'est pas un dictionnaire exhaustif de Git. Ce n'est pas non plus "cliquer jusqu'a ce que ca parte" en esperant le hasard. Lis. Traduis en francais simple. Une action. Verifie avec `status`. Ce n'est pas une course. Ce n'est pas "Googler la premiere commande sans comprendre si c'est pousse ou non". La methode DanielCraft est lente au debut, rapide ensuite. Lea le confirme. Max aussi, apres avoir clique au hasard trop longtemps.

## Traductions utiles

Quand Git dit "nothing to commit, working tree clean", ca veut dire : rien a photographier, tout est deja commit. OK, tu peux coder ou changer de branche. "Untracked files" : des fichiers pas encore suivis. `add` si tu les veux, `.gitignore` si tu ne les veux jamais. "Your branch is ahead of origin/main" : tu as des commits locaux non pousses. `git push`. "Your branch is behind" : le remote a avance. `git pull` avant de continuer ou de pousser. "rejected ... fetch first" : push refuse, le serveur a des commits que tu n'as pas. Tire d'abord, resous, repush. "merge conflict" : ouvre les fichiers marques, nettoie les `<<<<<<<`, `add`, commit de merge. "Permission denied" ou probleme d'auth : identifiants HTTPS, cle SSH, ou droits sur le depot.

Ces phrases reviennent. Apprends-les comme un vocabulaire de survie. Pas comme une poesie. Lea les a dans un fichier. Max aussi. Sam les projette.

## Methode DanielCraft

Lis d'abord la derniere partie du message. C'est souvent la plus claire. Ne panic pas sur le pave rouge : rouge = attention, pas fin du monde. Lance `git status` pour savoir ou tu es exactement. Une action a la fois. Si tu changes dix choses sans relire, tu ne sauras plus ce qui a repare quoi. Lea garde un fichier `atelier-messages-git.md` dans chaque nouveau projet avec ses traductions perso. Chez DanielCraft, on veut ce fichier plus qu'une capture d'ecran oubliee.

:::attention
Ne clique pas au hasard jusqu'a ce que ca parte. Lis, traduis, une action, verifie avec `status`. C'est la methode DanielCraft.
:::

## Exercice 1 - Ahead / behind (10 min)

Fais un commit local sans push. Lis le status "ahead". Push. Puis, si tu peux, edite un fichier directement sur GitHub (interface web) et `pull` en local pour voir "behind" disparaitre apres synchro. Note la sequence exacte. Max l'a colle dans son carnet : "ahead = j'ai oublie de push". Ecris la tienne avec tes mots.

## Exercice 2 - Rejected (10 min)

Provoque un push reject (pull manquant) et repare. Note la sequence exacte qui t'a debloque. Souvent : pull, resoudre conflit eventuel, push. Sam fait cet exercice en binome : l'un push, l'autre push aussi sans pull - le reject arrive naturellement. Solo, tu peux editer sur GitHub puis push depuis local sans pull : meme lecon.

## Exercice 3 - Conflit (10 min)

Provoque un conflit volontaire (meme fichier modifie en local et sur le remote, ou deux branches). Resous-le. Verifie qu'aucun marqueur `<<<<<<<` ne reste avant le commit. Relis le diff une fois : c'est bon entrainement pour la vraie vie. Lea refuse de conclure tant que le rendu n'est pas verifie.

## Exercice 4 - Secret (8 min)

Ajoute un faux secret au mauvais moment, puis retire-le avec `rm --cached` + `.gitignore` + commit propre. Si c'etait un vrai secret deja pousse, tu changerais aussi le secret cote serveur - Git ne "descommit" pas l'historique facilement. Note la difference entre "retire du suivi" et "efface du passe public". Important.

## Petite histoire

Max a provoque un push rejected volontairement un samedi matin. Il a lu le message, tire, repousse. Dix minutes plus tard, il expliquait "ahead" et "behind" a un camarade sans notes. Lea garde son fichier `atelier-messages-git.md` dans chaque nouveau projet client. Sam le consulte en fin de promo : les memes erreurs reviennent toujours aux memes endroits - push oublie, pull oublie, conflit panique. L'atelier ne les elimine pas. Il les rend previsibles. Chez DanielCraft, previsible bat heroique.

## Erreur classique

Cliquer au hasard jusqu'a ce que ca parte. Changer dix choses d'un coup sans relire `status`. Googler la premiere commande sans comprendre si c'est pousse ou non. Faire l'atelier sans remote : ahead/behind restent abstraits. Autre piege : noter les traductions sans refaire les exercices - le cerveau classe ca comme "lu", pas "su". Les mains d'abord. Les notes ensuite.

## En vrai

La prochaine fois qu'un message apparait en rouge, ecris ta traduction en une phrase avant d'agir. Ce micro-rituel change tout. Lea le fait depuis six mois. Max aussi. Sam l'impose en classe. Toi, commence aujourd'hui. Une phrase. Puis une action. Puis status.

## A toi

Fais les quatre exercices. Livrable : un fichier `atelier-messages-git.md` avec 4 messages traduits, une sequence de reparation, 5 lignes de lecons. Puis explique a voix haute, comme a Max ou Lea, la difference entre "ahead" et "behind". Si tu y arrives sans notes, c'est bon signe.
