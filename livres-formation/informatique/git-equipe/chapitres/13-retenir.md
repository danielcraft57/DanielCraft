# Chapitre 13 - A retenir

Tu n'as pas besoin de tout memoriser par coeur. Tu as besoin d'une carte mentale stable. Voici la version poche du livre, a relire avant une journee d'equipe.

## Le flux

Tire `main` en debut de session. Cree une branche pour une intention. Commit. Pousse la branche. Ouvre une PR. Fais reviewer. Merge. Retire `main`. Recommence. Petit et frequent bat grand et rare.

## Les branches

`main` = reference. Feature/fix = travail. Noms clairs. Duree courte. Une intention par branche. Nettoie apres merge. GitHub Flow leger suffit a 2-5 personnes.

## Rebase et merge

Merge joint les histoires. Rebase rejoue tes commits sur une base plus recente. Utile sur une feature perso. Dangereux sur l'histoire partagee si tu force-push sans soin. Pas de dogme : une politique d'equipe ecrite.

## Historique

Messages qui disent le pourquoi. Petits commits coherents. Squash possible a l'integration. Amend seulement en local / branche perso. Pas de secrets dans Git.

## Revue

Bienveillante, utile, rapide. Description claire cote auteur. Regard priorise cote reviewer. Dire aussi ce qui est bien. Pas d'Approve fantome. Pas de tribunal.

## Protection et CI

`main` protegee : pas de push direct, PR, review. CI legere : tests sur la PR, feu vert avant merge. Filet technique + filet humain.

## Tags et releases

Nommer un commit livre : `vX.Y.Z`. Pousser le tag. Notes courtes. Aligner tag et deploiement.

## Cherry-pick et bisect

Cherry-pick : reprendre une cerise (un commit) ailleurs, surtout en urgence. Bisect : trouver le commit qui a casse par recherches successives. Outils de precision, pas de panique.

## Contribuer et secrets

Fork + upstream pour contribuer a un projet externe (chapitre 17). Jamais de cles dans le depot (chapitre 18). Les bonnes pratiques d'equipe tiennent en quelques phrases ecrites (chapitre 19).

## Phrase DanielCraft

Git en equipe, ce n'est pas "connaitre plus de commandes". C'est "se synchroniser sans se blesser". Les commandes servent ce but.

## A toi

Sans regarder le livre, ecris sur papier les 8 etapes du flux (pull main ... pull main). Si tu bloques, relis le chapitre 2. Si tu y arrives, tu as la colonne vertebrale.
