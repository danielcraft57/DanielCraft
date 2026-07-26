# Chapitre 19 - Bonnes pratiques d'equipe

Les outils ne sauvent pas une equipe qui ne se parle pas. Les pratiques ci-dessous sont le minimum de politesse technique pour deux a cinq personnes. Adapte. Ecris. Rappel. Chez DanielCraft, on repete souvent : clarte, filets, bienveillance. Git est un moyen. Le produit et les humains sont la fin. Si une pratique Git rend tout le monde miserable sans gain de fiabilite, changez la pratique.

Tu n'as pas besoin de quinze regles. Tu as besoin de trois a cinq **pratiques** tenues. Les tenir bat les collectionner. Ce chapitre est une checklist vivante, pas un roman ISO. Lis-le une fois. Choisis. Ecris dans le README. Relis en retro.

:::retenir
Quelques regles tenues battent vingt regles ignorees. Ecris le contrat leger. Tiens-le.
:::

## Ecrire le contrat leger

Un README section "Comment on travaille" avec : branches, **PR** obligatoires, qui review, rebase ou merge, comment on release, ou vivent les secrets. Une demi-page. Pas un roman. Si ce n'est pas ecrit, chacun invente. Puis s'etonne. Lea invente "on pousse sur main si c'est petit". Max invente "rebase partout". Sam invente "pas besoin de review". Trois inventions, un vendredi triste.

Le contrat leger n'est pas fige. Apres deux semaines, ajustez une phrase. Une seule amelioration par retro suffit. Le document qui change un peu reste vivant. Celui qui ne change jamais devient decoratif.

## Petites PR, souvent

Livre des tranches. Review plus facile. Rollback plus simple. Moral plus haut. La "grosse PR du mois" est un anti-pattern courant. Cent vingt lignes se lisent. Deux mille cinq cents se feignent. Decoupe meme si ca demande deux merges. Le calendrier te remerciera. Le reviewer aussi.

## Synchroniser tot

Tire `main` souvent. Parle si tu touches une zone chaude. Evite les conflits-surprise. Le silence n'est pas de la concentration heroique : parfois c'est de la collision en preparation. Un message dans le canal coute dix secondes. Un conflit surprise sur le meme fichier coute une heure. Tu le sais depuis le chapitre 2. Tiens-le.

## Proteger ce qui compte

`main` **protegee**. Secrets hors Git. **CI** legere verte avant merge. Tags pour les versions livrees. Ces quatre gestes evitent une categorie entiere de vendredis tristes. Tu peux les activer en une apres-midi sur un depot de test. Habitude avant vitesse. Filet avant heroisme.

:::astuce
Quatre filets minimum : `main` protegee, secrets hors Git, CI legere, tags de release. Active-les tot, pas "quand on aura le temps".
:::

## Review comme un collegue, pas comme un juge

Aide. Questionne. Propose. Remarque le bien. Reponds vite. L'ego hors du diff. Approve conscient ou pas Approve. Request changes pour les vrais bloqueurs, pas pour une virgule. L'auteur ecrit "comment tester". Le reviewer suit "comment tester". Deux gestes, une equipe qui respire.

## Noms clairs partout

Branches, commits, PR, tags. Le futur lecteur est un humain fatigue a 18h. Ecris pour lui. `feature/page-tarifs` bat `max-wip`. "Corrige le timeout session" bat "fix". `v1.2.0` bat "version de mardi". La clarte est une forme de gentillesse.

## Une intention a la fois

Un bug urgent ne voyage pas cache dans une refonte. Deux branches. Deux PR. Le calendrier te remerciera. Cherry-pick si vraiment une cerise doit partir avant le panier. Bisect si tu cherches le commit casse. Outils de precision, pas de panique.

## Sabbat du force-push

Force-push seulement sur ta branche perso, avec `--force-with-lease`, en conscience. Jamais sur `main`. Jamais "pour voir" sur la branche d'un autre. Annonce dans le canal si la branche etait deja partagee. Le silence plus force-push egal egos et histoires ecrasees.

:::attention
`--force` sur `main` ou sur la branche d'un collegue sans annonce : non. Prefere `--force-with-lease` sur ta branche perso seulement.
:::

## Documenter les incidents sans humiliation

Quand ca casse : chronologie, cause, correctif, prevention. Pas de pile au milieu de la piece. Une equipe qui apprend plus vite gagne plus qu'une equipe qui punit. Max a casse la prod un vendredi. L'equipe a ecrit "protection main des le jour 1". Pas "Max est nul". Le process a gagne. Max aussi.

## Rituels hebdomadaires legers

Dix minutes lundi : branches mortes a supprimer ? CI rouge ignoree ? Secrets tournes apres un depart ? Une seule question par semaine suffit a eviter la poussiere. L'onboarding d'un nouveau : README "Comment on travaille", un acces, une petite PR de doc ou de typo pour vivre le flux. La premiere PR est un rituel d'equipe, pas un examen.

Quand casser une regle : rarement, explicitement, annonce dans le canal, remets la regle apres. Une regle sans exception jamais discutee devient du theatre. Une exception tous les jours devient l'absence de regle.

## Petite histoire

Lea a copie le process d'une grosse boite : trois approvals, douze checks, signatures. L'equipe de trois s'est bloque. Ils ont simplifie. Flux tenu. Reviews utiles. `main` protegee. CI d'un job. Trois pratiques non negociables dans le README. Deux mois plus tard, toujours tenues. Chez DanielCraft, on dit : le juste milieu, c'est quelques regles tenues, pas vingt ignorees.

## Erreur classique

Copier le process d'une FAANG a trois personnes. Ou n'avoir aucun process. Ou empiler bots et hooks avant d'avoir un flux tenu. Autre piege : ecrire quinze non negociables et n'en tenir aucune. Trois, tenues, battent quinze, ignorees.

## En vrai

Fais une retro de vingt minutes apres deux semaines de mini-projet. Qu'est-ce qui a frotte ? Quelle phrase ajouter au README ? Une seule amelioration suffit par retro. Mesure simple sans dashboard : push directs sur `main` (doit tendre vers zero), temps avant premier regard sur une PR, secrets revoques apres incident (doit etre "tous", tout de suite). Un ressenti honnete en retro suffit au debut.

## A toi

Choisis trois pratiques de ce chapitre et ecris-les comme "non negociables" pour ton equipe. Trois, pas quinze. Les tenir bat les collectionner. Colle-les sous l'ecran. Relis-les avant la prochaine PR.
