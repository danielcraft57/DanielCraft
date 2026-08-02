# Chapitre 11 - clone, push, pull

Voici le dialogue avec le serveur. **`clone`** recupere un depot existant. **`push`** envoie tes commits locaux. **`pull`** ramene les commits distants chez toi. Sans ce dialogue, Git reste un album solo. Avec ce dialogue, tu rentres dans le jeu equipe / sauvegarde distante. Chez DanielCraft, le reflexe du matin en collab, c'est `git pull` avant de recoder. Pas glamour. Fiable.

Lea pull, code, commit, push. Max oubliait le pull, se prenait des `rejected`, apprenait. Sam fait cloner un petit depot public en lecture seule pour explorer un `log` vivant. Trois gestes, une meme conversation. Toi, tu vas sentir la boucle complete : modifier, photographier, envoyer, recuperer. Quand quelque chose bloque, tu liras le message jusqu'au bout. Souvent, la reponse est dedans.

```text
toi (local) --push--> GitHub
toi (local) <--pull-- GitHub
```

`fetch` telecharge les infos sans fusionner tout de suite. `pull` ≈ `fetch` + merge (en simplifiant). Au debut, `pull` suffit. Ahead = tu as des commits locaux non pousses. Behind = le remote a avance. Rejected = tu as essaye de pousser alors que le remote avait des commits que tu n'avais pas. Ces trois mots reviennent tout le temps. Apprends-les comme un vocabulaire de survie. Chez DanielCraft, on les ecrit au tableau la premiere semaine : trois mots, trois reflexes.

:::retenir
Push refuse (`rejected`) ? Le remote a avance. `pull` d'abord, resous si besoin, puis `push`. Lis le message jusqu'au bout.
:::

## Ce que ce n'est pas

`push`, ce n'est pas `commit`. Si tu n'as pas commit, tu n'as rien a envoyer. `pull`, ce n'est pas "ecraser ton travail local sans regarder" - mais oui, ca peut creer des merges / conflits si les deux cotes ont avance. `clone`, ce n'est pas `init` : clone copie + configure souvent `origin`. Et ce n'est surtout pas une excuse pour pousser sur `main` partage sans convention d'equipe. Ce n'est pas non plus `force push` "parce que ca bloque" - hors sujet ici, et dangereux en equipe.

Ce n'est pas non plus "clone met a jour un dossier existant". Non : clone cree une copie. Pour mettre a jour, `pull`. Max a clone dix fois le meme depot dans dix dossiers avant de comprendre. Sam le montre explicitement. Lea rit, puis confirme : un dossier, un remote, des pulls. Chez DanielCraft, on prefere un `pull` du matin a dix clones paniques.

## clone, push, pull

```bash
git clone https://github.com/TON_COMPTE/mon-carnet.git
cd mon-carnet
```

`clone` = copie + lien `origin` deja configure.

```bash
git push
```

La premiere fois (si pas de `-u`) :

```bash
git push -u origin main
```

```bash
git pull
```

Reflexe avant de recommencer a coder le matin : `git pull`.

```bash
git fetch
```

Apercu utile. Pas obligatoire chaque jour pour ce livre. Utile quand tu veux regarder avant de fusionner. Lea fetche sur les gros projets. Max pull sur les petits. Les deux sont honnetes selon le contexte.

## Erreurs frequentes

`rejected` : le remote a des commits que tu n'as pas -> `pull` d'abord. Auth ratee : mauvais token / session. Mauvaise branche : tu pushes `main` alors que tu es ailleurs. Chez DanielCraft, on lit le message d'erreur jusqu'au bout avant de retaper la meme commande dix fois. Lea souligne la derniere ligne du message. Max a commence a le faire apres une heure perdue. Sam exige la traduction orale avant toute aide.

:::attention
`push` n'envoie que ce qui est commit. Si tu as modifie sans committer, rien ne part. Max a appris ca en voyant "Everything up-to-date" alors qu'il avait du travail non sauve.
:::

## Petite histoire

Max a modifie un fichier, commit, push. Puis il a edite une ligne sur GitHub via l'interface. En local, `git pull` a ramene le changement. La boucle est devenue concrete. Lea, sur un projet a deux, a impose "pull avant push". Les conflits ont baisse. Sam a fait cloner un depot open source, lire `log --oneline`, ne rien pousser. Explorer sans casser : excellent sport. Chez DanielCraft, on aime autant savoir lire un depot etranger que savoir pousser le sien.

## Erreur classique

Pousser sans pull sur une branche partagee. Croire que clone "met a jour" un dossier existant. Confondre le dossier parent et le dossier clone. Autre piege : force push "parce que ca bloque". Encore un piege : coder toute la journee sans pull le matin, puis decouvrir un mur de conflits a 18h. Pull tot. Petits pas. Moins de drames.

## En vrai

Sur un projet a deux : toujours `pull` avant de pousser. Ca diminue les conflits. Sur un projet solo : push quand meme assez souvent pour avoir une copie distante. Une fois par jour utile, c'est deja bien. Lea pousse a chaque feature terminee. Max pousse avant de fermer le PC. Sam pousse avant la pause dejeuner en demo. Choisis un rituel. Tiens-toi y. Si tu vois `rejected`, ne retape pas `push` dix fois : lis, `pull`, resous, puis `push`. Chez DanielCraft, un remote a jour bat une sauvegarde USB oubliee dans un tiroir.

## A toi

Modifie un fichier, commit, puis push. Change quelque chose sur GitHub via l'interface (petit edit). Fais `git pull` en local. Bonus : clone un petit depot public open source (lecture seule), explore `log --oneline`, ne push rien. Note en une phrase la difference entre ahead et behind.
