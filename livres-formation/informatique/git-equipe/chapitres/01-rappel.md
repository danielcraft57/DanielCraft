# Chapitre 1 - Rappel rapide et carte du livre

Tu as deja fait les bases. Init, clone, status, add, commit, log, branch, merge, pull, push, stash, undo, et une premiere pull request. Si un detail est flou, ce n'est pas grave : on ne va pas tout refaire. Ce livre part du moment ou Git devient un outil d'equipe.

Chez DanielCraft, on aime bien une image simple. Les bases, c'etait apprendre a conduire seul sur un parking. Ici, c'est la route a plusieurs : se synchroniser, se revoir le code, proteger la branche principale, et sortir une version sans panique.

## Ce que tu gardes en tete

Tu sais creer un commit. Tu sais creer une branche et fusionner. Tu sais pousser et tirer depuis GitHub (ou un equivalent). Tu as vu un conflit une fois. C'est assez pour avancer.

On ne revient pas sur `git init`, ni sur "c'est quoi un commit", ni sur l'installation. Si tu bloques sur ces mots, relis le premier livre Git. Ici, on monte d'un cran : travailler a 2, 3 ou 4 personnes sans se marcher dessus.

## La carte du livre

Imagine une petite equipe qui livre un site. Pour que ca marche vraiment, tu as besoin de plusieurs pieces.

D'abord un flux clair : qui pousse ou, quand on tire, comment on se parle. Ensuite une strategie de branches simple (souvent feature vers main). Rebase et merge, sans dogme : l'idee, les risques, le moment. Un historique propre (messages, petits commits, idee de squash). La revue de code humaine, bienveillante. Les branches protegees. Une CI legere sur les pull requests. Les tags et releases. Puis cherry-pick et bisect, deux outils pour "reprendre un commit" et "trouver le commit casse".

Plus loin : un mini-projet qui simule l'equipe, un recap, trois ateliers, le fork et l'upstream pour contribuer, l'hygiene des secrets, les bonnes pratiques, un quiz, et un bravo.

## Un fil rouge

On va souvent parler de trois personnages. Lea (front), Max (back), Sam (qui touche un peu a tout). Ils sont 3 sur un petit site vitrine + formulaire de contact. Parfois on ajoute un bug urgent ou une release. L'idee : des situations concretes, pas un manuel militaire.

Tu verras le meme geste sous plusieurs angles : partir d'une branche a jour, ouvrir une PR propre, repondre a une review, et ne jamais pousser directement sur `main` sans filet.

## Ce dont tu as besoin

Git installe. Un compte GitHub (ou GitLab). Un depot de test (cree-en un vide, pas ton vrai projet client). Un terminal. Et idealement un second compte ou un ami pour jouer la revue. Sinon, tu peux simuler seul en changeant de branche et en te commentant toi-meme.

## Comment lire ce livre

Lis dans l'ordre au debut. Flux, branches, rebase vs merge, historique, revue, protection : ca s'enchaine. Ensuite CI, tags, cherry-pick, bisect. Le mini-projet colle les briques. Les ateliers sont la pour faire, pas seulement lire.

Tu n'as pas besoin d'etre expert DevOps. On reste sur ce qu'une petite equipe utilise vraiment chaque semaine.

## Erreur classique

Croire que "je connais Git" = "je sais collaborer". Les bases sont le moteur. L'equipe, c'est le code de la route : priorites, reviews, branches protegees. Sans ca, tout le monde pousse sur `main` et un jour quelqu'un casse la prod un vendredi soir.

## En vrai

Ouvre un vieux depot ou tu as travaille a plusieurs. Note ce qui a frotte : conflits, messages flous, PR trop grosses, `main` non protegee, un secret qui a failli partir. Ce livre repond a ca.

## A toi

Ecris en trois phrases la regle d'or que tu voudrais dans ton equipe. Exemple : "jamais de push direct sur main", "toute feature passe par une PR", "on tire main avant de creer une branche". Garde ce but. On y reviendra.
