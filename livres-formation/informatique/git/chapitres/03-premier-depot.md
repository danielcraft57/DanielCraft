# Chapitre 3 - Ton premier depot

Un **depot** (repository), c'est un projet suivi par Git. Pas une usine. Pas un compte en ligne. Un dossier + une memoire cachee `.git`. Tu initialises. Tu ajoutes des fichiers. Tu regardes `status`. Tu comprends les **zones**. A partir de la, chaque chapitre ajoute une commande utile. Mais le sol, c'est ici : un depot propre, dans le bon dossier, avec un premier fichier. Sans ce sol, les branches et les push ne sont que du jargon.

Chez DanielCraft, on insiste sur "le bon dossier" parce que le classique du debutant, c'est `git init` dans le dossier utilisateur entier. Lea l'a failli faire un soir de fatigue. Max verifie toujours avec `cd` avant de taper `init`. Sam fait dire a voix haute le chemin complet. Une ceremonie ridicule qui evite une galere reelle : un `.git` qui essaie de suivre des milliers de fichiers personnels. Toi, avant chaque `init`, tu demandes : "suis-je bien dans le dossier du projet, et seulement de ce projet ?"

Quand `git init` reussit, presque rien ne change a l'oeil nu. Pourtant quelque chose d'immense vient d'arriver : Git a allume la machine a photos dans ce dossier. Tu ne le vois pas tant que tu n'actives pas "elements caches" dans l'explorateur. Le dossier `.git` est la. Ne le touche pas a la main. C'est la memoire. Si tu le supprimes, tu perds l'historique local.

Trois zones structurent tout le reste du livre. Le **dossier de travail** : tes fichiers normaux, ceux que tu ouvres dans l'editeur. L'**index** / staging : ce que tu prepares pour la photo, apres `add`. Le depot : l'historique des commits, dans `.git`. Tu ecris dans tes fichiers. Tu choisis quoi photographier (`add`). Tu valides la photo (`commit`). Beaucoup de debutants confondent index et historique. `status` te le dit clairement si tu apprends a le lire : untracked, staged, modified, clean.

:::retenir
`git init` allume la machine a photos dans ce dossier. Ce n'est ni un commit, ni une publication en ligne.
:::

## Ce que ce n'est pas

`git init`, ce n'est pas publier sur internet. Ce n'est pas un commit. Ce n'est pas "sauvegarder dans le cloud". C'est allumer la machine a photos dans ce dossier. Point. Et ce n'est surtout pas une invitation a fouiller `.git` a la main : ne le touche pas. Ce n'est pas non plus `git clone` : clone copie un depot existant depuis ailleurs ; init demarre un depot neuf ici. Les deux menent a un dossier avec un `.git`, mais le chemin n'est pas le meme.

Ce n'est pas non plus "finir le projet". Un depot vide avec un readme est deja un debut propre. Lea initialise parfois avant d'avoir ecrit une ligne de CSS. Max initialise des qu'il a un carnet de notes. Sam initialise avec la classe des qu'un exercice commence. Habitude : allumer tot, photographier souvent.

## Creer, initialiser, premier fichier

```bash
mkdir mon-carnet
cd mon-carnet
git init
```

Git cree un dossier cache `.git`.

Cree `readme.txt` avec :

```text
Mon carnet de tests Git
```

Puis :

```bash
git status
```

Git dit souvent quels fichiers sont non suivis (untracked), modifies, ou prets a commit. Lis `status` souvent. C'est ton tableau de bord. Lea le lance presque apres chaque geste. Max le lance quand il a un doute. Sam le lance avant de repondre a un eleve. Chez DanielCraft, on prefere dix `status` de trop qu'un commit a l'aveugle.

:::astuce
Lis `git status` a voix haute apres chaque geste. En une semaine, les mots untracked, staged et clean deviennent familiers.
:::

## git init dans un projet existant

Tu peux lancer `git init` dans un dossier qui a deja des fichiers. Puis tu choisis quoi ajouter. Utile pour "mettre sous Git" un site ou un script deja commence. Verifie quand meme que tu n'es pas dans un mega-dossier plein de secrets, de telechargements, ou de `node_modules` enormes. Si le dossier est sale, nettoie ou ignore avant le premier gros `add`. On detaille `.gitignore` plus loin. Ici, retiens juste : init dans le bon endroit, avec les bons fichiers sous les yeux.

## Petite histoire

Max a active "elements caches" dans l'explorateur Windows. Apres `init`, `.git` est apparu. Sensation concrete : "il s'est passe quelque chose". Sam a fait ajouter `notes.txt`, relancer `status`, comparer avec avant. Les eleves ont vu le mot untracked. Lea a lu a voix haute : "untracked files". Chez DanielCraft, on celebre ce moment : tu vois le langage de Git avant de le commander.

Lea, le meme soir, a initialise un second dossier par erreur dans le mauvais chemin. Elle a vu des centaines de fichiers untracked. Elle a compris. Elle a ferme. Elle a recommence dans `mes-tests-git`. Lecon gratuite. Toi, si `status` te montre la moitie de ton disque, stop. Tu es au mauvais endroit.

## Erreur classique

`git init` dans le mauvais dossier (ex : ton dossier utilisateur entier). Verifie avec `cd` et `pwd` (ou `cd` sous PowerShell) avant. Autre piege : paniquer parce que `status` "parle anglais". Normal. Apprends les mots : untracked, staged, nothing to commit. Encore un piege : supprimer `.git` "pour nettoyer" sans comprendre que tu effaces l'historique. Si tu veux recommencer un depot de test, oui, tu peux supprimer `.git` dans `mes-tests-git`. Sur un projet client, jamais sans savoir ce que tu fais.

:::attention
Ne touche jamais le dossier `.git` a la main. C'est la memoire de Git. Si tu le supprimes, tu perds l'historique local.
:::

## En vrai

Ouvre l'explorateur. Active "elements caches". Tu dois voir `.git` apparaitre apres `init`. Ajoute un second fichier `notes.txt`. Relance `status`. Compare avec avant. Dis a voix haute ce que Git sait maintenant de ton dossier. Si tu peux le dire simplement, tu as compris le chapitre.

Imagine une chaine. Tu ecris dans tes fichiers (zone de travail). Tu choisis quoi photographier (`add` = index). Tu valides la photo (`commit` = historique). Si `status` dit "Changes to be committed", c'est pret pour la photo. Si ca dit "Changes not staged", il manque un `add`. Si ca dit "nothing to commit, working tree clean", tu es a jour. Cette lecture vaut dix tutoriels.

## A toi

Fais `git init` dans `mes-tests-git` (ou `mon-carnet`). Cree un fichier texte. Lance `git status` et lis le resultat a voix haute. Ecris en une phrase : "ce que Git sait de mon dossier maintenant". Garde cette phrase. Au chapitre suivant, elle changera apres ton premier commit.
