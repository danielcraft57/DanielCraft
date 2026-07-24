# Chapitre 17 - Fork et upstream : contribuer ailleurs

Jusqu'ici, tu etais "dans" le depot de l'equipe : tu avais le droit de pousser des branches. Sur un projet open source (ou le depot d'une autre equipe), tu n'as souvent pas ce droit. Le chemin classique : fork, clone, branche, PR vers le projet original.

Ce chapitre pose le vocabulaire et le geste, sans transformer le livre en encyclopedie GitHub.

## Les mots

Fork : une copie du depot sur ton compte GitHub. Tu pousses sur ton fork librement.

Origin : en general, apres clone de ton fork, `origin` pointe vers ton fork.

Upstream : le depot d'origine (celui de l'equipe ou du projet public). Tu le configures pour recuperer les nouveautes, pas pour y pousser directement (tu n'en as souvent pas le droit).

Pull request : tu demandes au projet original d'integrer ta branche (depuis ton fork vers upstream).

## Scenario concret

Lea veut corriger une typo dans la doc d'un outil qu'elle utilise. Elle ne peut pas pousser sur le depot officiel. Elle fork. Elle clone son fork. Elle cree `fix/typo-readme`. Elle corrige. Elle pousse sur son fork. Elle ouvre une PR vers le depot officiel.

Chez DanielCraft, c'est aussi comme ca qu'on contribue a un outil ami : propre, petit, respectueux des regles du projet (CONTRIBUTING, style, licence).

## Les commandes d'installation

Apres avoir fork sur GitHub et clone ton fork :

```bash
git remote -v
git remote add upstream https://github.com/ORG/PROJET.git
git fetch upstream
```

Remplace l'URL. Verifie :

```bash
git remote -v
```

Tu dois voir `origin` (ton fork) et `upstream` (l'original).

## Rester a jour avec upstream

Avant une nouvelle contribution :

```bash
git switch main
git fetch upstream
git merge upstream/main
git push origin main
```

(adapte le nom de branche par defaut si le projet utilise autre chose)

Ainsi ton `main` local et celui de ton fork suivent le projet. Ta prochaine feature part d'une base saine.

## Le flux de contribution

```bash
git switch main
git pull origin main
git switch -c fix/typo-readme
# ... corrections, commits ...
git push -u origin fix/typo-readme
```

Puis sur GitHub : Pull request de `ton-compte:fix/typo-readme` vers `ORG/PROJET:main`.

Lis les commentaires des mainteneurs. Corrige. Sois patient. Une contribution refusee n'est pas une attaque personnelle : parfois le timing, parfois la direction du projet.

## Bonnes manieres

PR petite. Sujet unique. Message et description clairs. Respecter le style du projet. Ne pas reformater 200 fichiers "en passant". Ne pas ouvrir dix PR de bruit le premier jour.

Si le projet a un fichier `CONTRIBUTING.md`, lis-le. Ca evite 80% des malentendus.

## Et dans une entreprise ?

Parfois tu n'as pas de fork : tu as directement acces au depot, et le chapitre 2 suffit. Le fork sert surtout quand les droits d'ecriture sont limites, ou pour isoler des experiences. Comprendre fork/upstream reste utile des que tu touches l'open source.

## Erreur classique

Pousser vers `upstream` alors que tu n'as pas les droits (erreur) ou, pire, croire que `git push` sans remote precise ira "au bon endroit". Verifie. Autre piege : laisser ton fork moisir six mois, puis ouvrir une PR sur une base obsolete : sync d'abord.

## En vrai

Fork un petit projet (meme un depot demo), ajoute `upstream`, synchronise `main`, ouvre une PR minuscule sur ton propre fork vers un second depot de test si besoin, pour voir les boutons GitHub. L'important est de voir origin vs upstream une fois dans l'interface.


## PR cross-fork : ce que voit le mainteneur

Le mainteneur recoit une PR depuis ton fork. Il voit tes commits, ta discussion, peut demander des changements. Tu pousses sur ta branche de ton fork ; la PR se met a jour. Tu n'as pas besoin d'acces write sur upstream pour iterer.

Quand c'est merge, tu sync ton `main` depuis upstream (fetch + merge) pour rester aligne, et tu peux supprimer ta branche de feature sur ton fork.

## Fork pour experimenter

Meme avec acces write, certains forkent pour tenter une idee folle sans polluer les branches de l'equipe. Moins courant en petite boite, courant en open source. L'idee reste : isolation + proposition.

## Droits et organisations

Dans une org GitHub, on t'ajoute parfois en write sur le depot : pas besoin de fork. On t'ajoute parfois seulement en lecture + process fork/PR : besoin de fork. Demande quel modele est en place. Ne suppose pas.


## A toi

Dessine sur papier trois boites : ton PC, ton fork, le depot original. Fleches : fetch upstream, push origin, PR vers upstream. Si le dessin est clair, le modele est clair.
