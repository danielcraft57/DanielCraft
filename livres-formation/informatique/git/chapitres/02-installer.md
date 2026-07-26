# Chapitre 2 - Installer Git

Avant de photographier un projet, il te faut Git qui repond vraiment. Pas une icone dans le menu demarrer. Une commande `git --version` qui affiche un numero, dans un vrai **terminal**, sur ta machine. Sur Windows, le chemin simple reste git-scm.com : tu telecharges l'**installateur**, tu suis l'assistant (les options par defaut vont bien au debut), tu ouvres un terminal, tu verifies. Si un numero apparait, c'est bon. Sans ca, tout le reste du livre reste theorique, et la theorie ne sauve pas un fichier ecrase un jeudi soir.

Chez DanielCraft, on traite aussi la config comme obligatoire. Git a besoin de savoir qui tu es pour signer tes commits. Chaque photo de l'album portera ton nom et ton email. Lea a oublie une fois et s'est retrouvee avec une identite bizarre dans l'historique. Max a configure avec l'email de son futur compte GitHub des le premier jour. Sam verifie la config au tableau avant le premier commit de la classe. Toi, tu vas faire pareil avant de toucher `add` ou `commit`.

Installer, c'est aussi choisir ou tu tapes. PowerShell, Git Bash, terminal integre de VS Code : les commandes de ce livre restent les memes. Ce qui change, c'est le confort. Au debut, reste sur les messages de commit en une ligne avec `-m "..."`. Plus simple que de te battre avec un editeur vi ouvert par surprise parce que tu as oublie le `-m`.

:::retenir
Sans `git --version` et sans `user.name` / `user.email`, tu n'es pas pret. Configure avant le premier commit, pas apres.
:::

## Ce que ce n'est pas

Installer Git, ce n'est pas creer un compte GitHub. Tu peux versionner en local des semaines sans compte en ligne. Ce n'est pas non plus tout comprendre de l'univers DevOps. Ce n'est pas obligatoire d'ouvrir vingt options avancees de l'installateur Windows : les defauts suffisent pour apprendre. Et ce n'est surtout pas "optionnel" de renseigner `user.name` et `user.email`. Sans ca, Git rale, ou pire, enregistre une fausse identite que tu regretteras quand tu pousseras sur un projet d'equipe.

Ce n'est pas non plus "terminer le livre d'un coup". Ce chapitre est un sas. Tu installes. Tu configures. Tu crees un dossier de test. Puis tu passes au depot.

## Windows et verification

1. Va sur git-scm.com
2. Telecharge l'installateur
3. Suis l'assistant (defauts OK au debut)
4. Ouvre un terminal et tape :

```bash
git --version
```

Si un numero s'affiche, l'appareil est la. Note-le quelque part dans un fichier `notes.md` si tu veux. Ce n'est pas pour briller. C'est pour savoir quoi dire si un jour un outil demande "quelle version de Git ?".

:::astuce
Git Bash, PowerShell ou le terminal VS Code : les commandes sont les memes. Choisis celui ou tu te sens le plus a l'aise et garde-le une semaine.
:::

## Premiere config (obligatoire)

```bash
git config --global user.name "Ton Prenom"
git config --global user.email "ton@email.com"
```

Verifie :

```bash
git config --global --list
```

Utilise un email que tu assumeras (souvent celui de ton compte GitHub). Ce n'est pas de la paperasse. C'est ta **signature** sur l'historique. Lea a mis son email pro. Max a mis celui de son compte GitHub avant meme de creer le compte - il a juste veille a rester coherent. Sam exige l'email "officiel" des eleves pour que les commits soient lisibles en correction.

:::attention
Sans `user.name` et `user.email`, Git enregistre une fausse identite. Configure avant ton premier commit, pas apres.
:::

## Ou taper les commandes ?

Tu peux utiliser le terminal Windows (PowerShell), Git Bash (installe avec Git), ou le terminal integre de VS Code. Les commandes de ce livre marchent dans ces environnements. Si `git` n'est pas reconnu juste apres l'install, ferme et rouvre le terminal : le PATH se met a jour au demarrage. Si ca bloque encore, redemarre une fois. Chez DanielCraft, on aime ces petites verites de terrain plus que les theories parfaites.

## Aide integree

```bash
git help
git help commit
git commit -h
```

Tu n'as pas a tout lire. Tu dois savoir que l'aide existe. "Je ne sais pas" suivi de `git help` bat "j'invente une commande" neuf fois sur dix. Lea ouvre `git help commit` quand elle oublie un flag. Max a commence a le faire apres avoir tape trois fois une fausse option. Sam projette l'aide au tableau pour montrer que Git n'est pas un mur opaque.

## Petite histoire

Lea a installe Git un lundi matin, configure, ouvert VS Code, tape `git --version` dans le terminal integre. Sensation : "l'outil est la". Elle a cree aussitot un dossier `mes-tests-git` sur le bureau, pas dans Documents/ProjetsClients. Terrain de jeu separe. Max a fait pareil le soir meme, en notant ses deux commandes de config dans un carnet papier. Sam refuse de demarrer un atelier sans cette verification collective : `git --version` a voix haute, puis config, puis dossier de test. Trois minutes qui evitent une heure de "chez moi ca marche pas". Chez DanielCraft, c'est exactement le genre de ceremonie ridicule qui sauve des soirees.

## Erreur classique

Tu commits sans avoir configure le nom et l'email. Git rale. Ou pire : il utilise une fausse identite que tu pousseras ensuite sur GitHub. Configure tout de suite. Autre classique : croire que l'install a echoue parce que tu es dans le mauvais terminal - reouvre, retape, verifie le PATH si besoin. Encore un piege : installer Git et passer directement a un projet client critique. Non. Cree `mes-tests-git`. Casse la. Apprends la. Autre erreur : vouloir "tout configurer" (editeur par defaut, aliases, credential helper avance) avant d'avoir fait un seul commit. Trop tot. Les defauts suffisent.

## En vrai

Ouvre VS Code. Ouvre le terminal. Tape `git --version`. Si ca marche la, tu es pret pour la suite. Cree aussi le dossier `mes-tests-git` sur ton disque : c'est ton terrain de jeu pour tout le livre. Ecris dedans un petit `notes.md` avec la date et la version de Git. Tu viens de commencer ton album avant meme le premier vrai commit.

## A toi

1. Lance `git --version`.
2. Configure `user.name` et `user.email`.
3. Affiche la config avec `git config --global --list`.
4. Cree `mes-tests-git`.

Note le tout dans un fichier `notes.md` si tu veux garder une trace. Demain matin, avant le chapitre 3, retape juste `git --version` pour sentir que l'outil est toujours la. Cinq secondes. Habitude posee.
