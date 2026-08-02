# Chapitre 1 - Rappel rapide et carte du livre

Tu as deja fait les bases. Init, clone, status, add, commit, log, branch, merge, pull, push, stash, undo, et une premiere pull request. Si un detail est flou, ce n'est pas grave : on ne va pas tout refaire. Ce livre part du moment ou Git devient un outil d'**equipe**, pas un carnet personnel. Chez DanielCraft, on aime une image nette : les bases, c'etait apprendre a conduire seul sur un parking. Ici, c'est la route a plusieurs. Se synchroniser, se revoir le code, proteger la branche principale, sortir une version sans panique.

Tu sais creer un **commit**, creer une **branche**, fusionner, pousser et tirer depuis GitHub ou un equivalent. Tu as vu un conflit une fois. C'est assez pour avancer. On ne revient pas sur `git init`, ni sur "c'est quoi un commit", ni sur l'installation. Si tu bloques sur ces mots, relis le premier livre Git. Ici, on monte d'un cran : travailler a deux, trois ou quatre personnes sans se marcher dessus.

## Ce que ce n'est pas

Ce n'est pas un dictionnaire exhaustif de Git. Ce n'est pas non plus un cours DevOps pour cent personnes. Ce n'est pas "apprendre encore une fois ce que tu sais deja". Et ce n'est surtout pas "connaitre Git" confondu avec "savoir collaborer". Les bases sont le moteur. L'equipe, c'est le code de la route : priorites, reviews, **branches protegees**. Sans ca, tout le monde pousse sur `main` et un jour quelqu'un casse la prod un vendredi soir.

Ce n'est pas non plus un livre ou l'on te juge si tu as oublie une option obscure. On veut des gestes tenables. Petit. Frequent. Clair.

Imagine une petite equipe qui livre un site vitrine avec formulaire de contact. Pour que ca marche vraiment, plusieurs pieces s'emboitent. D'abord un **flux** clair : qui pousse ou, quand on tire, comment on se parle. Ensuite une strategie de branches simple, souvent feature vers main. Rebase et merge sans dogme : l'idee, les risques, le moment. Un historique propre avec des messages qui racontent le pourquoi. La revue de code humaine, bienveillante. Les branches protegees. Une CI legere sur les pull requests. Les tags et releases. Puis cherry-pick et bisect, deux outils pour reprendre un commit et trouver celui qui a casse.

:::retenir
Connaitre Git, ce n'est pas encore savoir collaborer. Le flux d'equipe, c'est le vrai cran suivant.
:::

Lea (front), Max (back) et Sam (fullstack) reviendront souvent. Ils sont trois sur ce petit site. Parfois on ajoute un bug urgent ou une release. Des situations concretes, pas un manuel militaire. Tu verras le meme geste sous plusieurs angles : partir d'une branche a jour, ouvrir une PR propre, repondre a une review, ne jamais pousser directement sur `main` sans filet.

## Ce que tu vas savoir faire

Dans ce livre, tu vas poser un flux d'equipe tenable, choisir une strategie de branches simple, comprendre rebase vs merge sans religion, garder un historique lisible, faire des revues utiles, proteger `main`, ajouter une CI legere, taguer des releases, cherry-picker en urgence, bisecter un bug, simuler l'equipe en mini-projet, contribuer via fork, et garder les secrets hors du depot. Puis un recap, trois ateliers, les bonnes pratiques, un quiz, et un bravo.

Niveau debutant solide qui a deja les bases Git. Pas besoin d'etre expert DevOps. Besoin de curiosite et d'honnetete : Git aide a collaborer ; il ne remplace pas la communication.

## Comment lire ce livre

Lis dans l'ordre au debut. Les premiers chapitres posent le sol. Les ateliers font faire. Le quiz verifie. Tu peux revenir ensuite a un chapitre precis (rebase, revue, secrets) comme a une fiche. A chaque fin de chapitre, il y a un "A toi". Fais-le. Cinq minutes valent mieux qu'une lecture passive de quarante pages. Tape les commandes sur un depot de test, pas sur le client critique.

## Petite histoire

Lea avait "deja Git" sur son CV. Le premier jour en equipe, Max lui a dit : "Tu as pousse sur main ?" Elle avait oublie la regle. Sam a du revert un vendredi. Personne n'avait ecrit le flux. Ce livre existe pour que cette scene ne se repete pas chez toi. Trois personnes, un README, un filet technique, et des vendredis plus calmes.

Chez DanielCraft, on a vu la meme scene trop souvent : talent technique, zero contrat leger. Le code etait bon. Le vendredi, non.

## Erreur classique

Croire que "je connais Git" egal "je sais collaborer". Ou croire que "on est que deux, on peut tout faire sur main". A deux, un revert malheureux, et vous avez le meme probleme qu'a dix. La discipline legere protege aussi les petites equipes. Autre piege : lire ce livre sans depot de test. Tu retiens les mots, pas les gestes.

:::attention
Sans depot de test, tu monologues. Avec un depot de test, tu t'entraines. Cree-en un avant le chapitre 2.
:::

## En vrai

Ouvre un vieux depot ou tu as travaille a plusieurs. Note ce qui a frotte : conflits, messages flous, PR trop grosses, `main` non protegee, un secret qui a failli partir. Ce livre repond a ca. Si tu n'as pas de depot, cree-en un vide sur GitHub. Git installe, un terminal, idealement un second compte ou un ami pour jouer la revue. Sinon, simule seul en changeant de branche et en te commentant toi-meme.

## A toi

Ecris en trois phrases la regle d'or que tu voudrais dans ton equipe. Exemple : "jamais de push direct sur main", "toute feature passe par une PR", "on tire main avant de creer une branche". Garde ce but. On y reviendra au mini-projet et dans le README.

## Petite scene DanielCraft

Lea ouvre le README. Max ajoute une ligne sur les PR. Sam active la protection de `main` sur le depot de test. Trois gestes, une meme posture : on se protege avant d'aller vite. C'est exactement l'esprit de ce livre.

:::astuce
Avant le chapitre 2, cree un depot de test vide et invite un ami (ou un second compte) pour jouer la revue. Le livre devient concret des la page suivante.
:::
