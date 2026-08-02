# Chapitre 1 - Salut, c'est quoi Git ?

Git, ce n'est pas un reseau social pour developpeurs, et ce n'est pas non plus une baguette magique qui "sauvegarde tout seul" dans le nuage. C'est un outil pour garder l'**historique** de ton projet : qui a change quoi, quand, et pourquoi. Chaque "photo" s'appelle un **commit**. Tu modifies des fichiers. Tu dis a Git : "garde cette version". Plus tard, tu peux revenir en arriere, comparer deux moments, essayer une idee sur une **branche** parallele, ou travailler a plusieurs sans t'ecraser mutuellement. En 2026, quand une equipe dit "c'est sur le repo", elle parle presque toujours d'un **depot** Git, souvent heberge aussi sur GitHub ou GitLab.

Chez DanielCraft, on aime une image nette. Ton projet, c'est un album de photos. Chaque commit, c'est une photo datee avec un petit titre. Les branches, ce sont des albums paralleles : tu peux tester une mise en page risquee sans toucher a la version stable. Lea versionne ses sites clients et retrouve un CSS ecrase en trente secondes. Max versionne un carnet de devis pour ne plus perdre ses calculs. Sam fait versionner les exercices de ses eleves pour montrer qui a change quoi. Trois metiers, meme logique : ne plus perdre le fil, oser experimenter, collaborer sans panique.

Git ne remplace pas ta tete. Il ne decide pas si ton code est bon. Il enregistre ce que tu choisis d'enregistrer. Si tu commit un secret ou un fichier casse, Git le gardera aussi - proprement, avec une date. C'est pour ca qu'on apprend le `.gitignore` et les messages clairs. L'outil est puissant parce qu'il est honnete : il fait ce que tu lui demandes, pas ce que tu voulais dire en pensant fort.

:::retenir
Git photographie ton travail. Toi, tu choisis quand declencher, sur quelle branche, et ce que tu fusionnes.
:::

## Ce que ce n'est pas

Ce n'est pas GitHub. Git, c'est le logiciel sur ton ordi. GitHub, c'est un site qui heberge des depots Git en ligne et ajoute la collaboration (issues, pull requests, review). Tu peux utiliser Git tout seul, sans compte, dans un dossier local. GitHub devient utile quand tu veux partager, sauvegarder au loin, ou travailler a plusieurs. Ce n'est pas non plus "trop complique pour un debutant". Les cinq commandes du quotidien - status, add, commit, log, push - suffisent deja a etre utile. Le reste vient apres, quand tu as un vrai probleme a resoudre.

Ce n'est pas non plus un disque dur magique dans le nuage. Tant que tu n'as pas pousse ailleurs, l'historique vit surtout chez toi. Utile pour travailler. Pas suffisant comme seule sauvegarde lointaine si ton disque lache. Et ce n'est surtout pas une excuse pour committer des secrets : mots de passe, cles API, fichiers `.env`. On y reviendra avec `.gitignore`.

## Ce que tu vas savoir faire

Dans ce livre, tu vas installer Git et configurer ton nom et ton email. Tu creeras un depot avec `git init`. Tu manipuleras `add`, `commit`, `status` et `log`. Tu feras des branches, des fusions et des conflits. Tu ecriras un `.gitignore`. Tu cloneras, pousseras et tireras depuis GitHub. Tu tapoteras stash et les annulations simples. Tu liras et ouvriras une pull request. Puis un mini-projet, un recap, trois ateliers, un quiz, et un bravo.

Niveau debutant solide. Pas besoin d'etre "dev senior". Besoin de curiosite, de taper les commandes dans un vrai dossier, et d'accepter de lire les messages que Git t'envoie au lieu de cliquer au hasard.

## Comment lire ce livre

Lis dans l'ordre au debut. Les premiers chapitres posent le sol : init, add, commit, branches. Les ateliers font faire avec les mains. Le quiz verifie sans humilier. Tu peux revenir ensuite a un chapitre precis (conflits, stash, PR) comme a une fiche. A chaque fin de chapitre, il y a un "A toi". Fais-le. Cinq minutes valent mieux qu'une lecture passive. Git s'apprend en cassant volontairement, puis en reparant. Casse sur `mes-tests-git`, pas sur le projet client du vendredi soir.

:::astuce
Cree un dossier `mes-tests-git` des le chapitre 2. Tout ce livre s'y joue. Tu peux casser sans paniquer.
:::

## Petite histoire

Lea a ecrase un fichier CSS important un jeudi soir. Avant Git, c'etait la panique et une sauvegarde "final_v3_vrai_definitif". Avec Git, elle a ouvert `git log --oneline`, retrouve le commit d'avant, compare avec `git diff`, respire, restaure. Vingt minutes au lieu de deux heures de stress. Max a voulu essayer une mise en page risquee sur une branche `feature/nouveau-header`. Ca n'a pas marche. Il a jete la branche. `main` etait intact. Sam a montre un conflit en classe : les eleves ont vu les marqueurs `<<<<<<<`, discute, choisi, commit. Le conflit est devenu un exercice, pas un drame. Chez DanielCraft, c'est exactement le but : rendre l'erreur reversible et la collaboration visible.

## Erreur classique

Croire que "Git, c'est trop complique pour moi". Ou croire que "je vais tout casser des que je tape une commande". Souvent, le probleme n'est pas Git. C'est l'absence de terrain de jeu : tu testes sur un projet critique la veille d'une livraison. Cree `mes-tests-git`. Casse la. Repars. Autre piege : tout apprendre d'un coup (rebase interactif, hooks, sous-modules) avant de maitriser status, add, commit, log. Commence petit. Monte ensuite. Encore un piege : confondre "j'ai Git" et "mon travail est sauvegarde". Sans push ou backup, tu restes dependant d'un seul disque.

:::attention
Git enregistre ce que tu lui demandes. Secret committe = secret dans l'historique. On apprend `.gitignore` tot dans le livre.
:::

## En vrai

Dis a voix haute : "Je veux une machine a photos de mon travail". C'est Git. Ouvre un terminal si tu peux. Si `git --version` repond deja, note le numero quelque part. Sinon, le chapitre suivant installe. Tu n'as rien a prouver a personne. Tu as juste a commencer dans un dossier de test.

Une sauvegarde cloud copie des fichiers. Git raconte une histoire : qui, quand, pourquoi, quoi. Tu peux comparer deux moments precis. Tu peux isoler une experience sur une branche. Ce n'est pas la meme promesse. Chez DanielCraft, on garde les deux idees distinctes : sauvegarder n'est pas versionner, versionner n'est pas publier.

## A toi

Ecris 3 peurs ou doutes sur Git (ex : "j'ai peur d'effacer", "je ne comprends pas les branches"). Garde ce papier. On y repondra dans le livre. Puis ecris une tache concrete que tu aimerais versionner : site web, notes de cours, scripts Python, carnet de devis. Ce sera ton fil rouge.
