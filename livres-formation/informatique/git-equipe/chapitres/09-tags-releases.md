# Chapitre 9 - Tags et releases

Un commit a un hash du genre `a3f19c2`. Pratique pour Git, penible pour les humains. Un tag, c'est un nom stable colle sur un commit : `v1.0.0`, `v1.1.0`, `v2.0.0`. Une release, c'est souvent ce tag + des notes ("ce qui change pour les utilisateurs").

Quand Sam dit "le bug est sur la 1.2", tout le monde doit pouvoir retrouver le meme code. Les tags servent a ca.

## L'idee

Tu livres le site. Ca marche. Tu marques le commit actuel :

```bash
git tag -a v1.0.0 -m "Premiere version publique du site"
git push origin v1.0.0
```

`-a` cree un tag annote (avec message et auteur). C'est en general preferable aux tags legeres pour les versions.

Plus tard, tu pourras revenir a ce point precis, construire a partir de lui, ou comparer :

```bash
git checkout v1.0.0
```

(tu seras en "detached HEAD" : normal pour inspecter une version ; reviens sur une branche apres)

```bash
git switch main
```

## SemVer en version poche

Beaucoup d'equipes utilisent Major.Minor.Patch : `v1.2.3`.

Patch : correctif sans changer l'usage (`v1.2.3` -> `v1.2.4`). Minor : nouveaute compatible (`v1.2.4` -> `v1.3.0`). Major : changement qui casse des usages (`v1.3.0` -> `v2.0.0`).

Pour un site vitrine, tu peux simplifier : `v1`, `v2`, ou des dates. L'important est d'etre coherent dans l'equipe.

## Release sur GitHub

Sur GitHub, tu peux creer une Release a partir d'un tag : titre, notes, fichiers attaches parfois. Lea ecrit : "Ajout page tarifs, fix formulaire email". Max deploie en sachant quoi tester. Le client comprend ce qui a bouge.

Chez DanielCraft, une release courte et honnete bat un roman marketing.

## Qui cree le tag ?

Souvent la personne qui livre, apres le merge sur `main`, sur le commit de `main` a jour. Pas sur une feature random. Pas "je tag chez moi sans pousser" : les autres ne verront rien.

```bash
git switch main
git pull
git tag -a v1.2.0 -m "Tarifs + fix email"
git push origin v1.2.0
```

## Tags et branches

Une branche bouge. Un tag, en principe, non. `main` avance. `v1.2.0` reste le souvenir d'un instant. C'est pour ca que c'est utile : point fixe dans un fleuve.

Evite de deplacer un tag deja publie (`git tag -f` puis force push) sauf correction immediate et annoncee. Les gens ont peut-etre deja tire `v1.2.0`.

## Lier tag et deploiement

Idealement : le meme commit tague est celui que tu deploies. Si tu deploies un commit et tu tags un autre, tu mens a ton futur toi. Aligne les gestes : merge, tag, deploy, notes.

## Erreur classique

Ne jamais taguer, puis chercher pendant une heure "la version de mardi". Ou taguer `v1` dix fois en le deplacant. Ou mettre dans les notes de release des secrets (non). Ou oublier de pousser le tag : tout le monde croit que la 1.2 n'existe pas.

## En vrai

Sur le depot de test, cree `v0.1.0` sur `main`, pousse le tag, cree une Release GitHub avec trois lignes de notes. Ensuite avance `main` d'un commit et cree `v0.1.1`. Liste :

```bash
git tag
```

Sens la chronologie.


## Notes de release qui aident

Mauvais : "divers fixes". Meilleur : "Fix validation email du formulaire contact. Ajout section tarifs sur /offres. Pas de migration base."

Ecris pour la personne qui va tester et pour celle qui va communiquer au client. Pas pour impressionner.

## Revenir en arriere grace a un tag

Un bug grave sur `v1.3.0`. Tu sais que `v1.2.0` etait sain. Tu peux inspecter, comparer, ou redeployer l'ancien artefact issu de ce tag selon votre pipeline. Sans tag, tu fouilles les dates et les souvenirs. Avec tag, tu as un nom.

```bash
git log --oneline v1.2.0..v1.3.0
```

Tu vois ce qui a change entre les deux. Utile pour enqueter (complement de bisect parfois).

## Tags legers vs annotes

Les tags legers sont juste un nom. Les annotes portent un message et des metadonnees. Pour les versions, prefere annote. Pour un marqueur purement local de travail, un leger peut suffire (et souvent tu n'en as pas besoin).


## A toi

Decide avec l'equipe le schema de versions (SemVer simple ou autre) et qui a le droit de publier une release. Une phrase dans le README suffit : "On tague main apres chaque livraison utile : vX.Y.Z."
