# Chapitre 19 - Bonnes pratiques d'equipe

Les outils ne sauvent pas une equipe qui ne se parle pas. Les pratiques ci-dessous sont le minimum de politesse technique pour 2 a 5 personnes. Adapte. Ecris. Rappel.

## Ecrire le contrat leger

Un README section "Comment on travaille" avec : branches, PR obligatoires, qui review, rebase ou merge, comment on release, ou vivent les secrets. Une demi-page. Pas un roman ISO.

Si ce n'est pas ecrit, chacun invente. Puis s'etonne.

## Petites PR, souvent

Livre des tranches. Review plus facile. Rollback plus simple. Moral plus haut. La "grosse PR du mois" est un anti-pattern courant.

## Synchroniser tot

Tire `main` souvent. Parle si tu touches une zone chaude. Evite les conflits-surprise. Le silence n'est pas de la concentration heroique : parfois c'est de la collision en preparation.

## Proteger ce qui compte

`main` protegee. Secrets hors Git. CI legere verte avant merge. Tags pour les versions livrees. Ces quatre gestes evitent une categorie entiere de vendredis tristes.

## Review comme un collegue, pas comme un juge

Aide. Questionne. Propose. Remarque le bien. Reponds vite. L'ego hors du diff.

## Noms clairs partout

Branches, commits, PR, tags. Le futur lecteur est un humain fatigue a 18h. Ecris pour lui.

## Une intention a la fois

Un bug urgent ne voyage pas cache dans une refonte. Deux branches. Deux PR. Le calendrier te remerciera.

## Sabbat du force-push

Force-push seulement sur ta branche perso, avec `--force-with-lease`, en conscience. Jamais sur `main`. Jamais "pour voir" sur la branche d'un autre.

## Documenter les incidents sans humiliation

Quand ca casse : chronologie, cause, correctif, prevention. Pas de pile au milieu de la piece. Une equipe qui apprend plus vite gagne plus qu'une equipe qui punit.

## Chez DanielCraft

On repete souvent : clarte, filets, bienveillance. Git est un moyen. Le produit et les humains sont la fin. Si une pratique Git rend tout le monde miserable sans gain de fiabilite, changez la pratique.

## Erreur classique

Copier le process d'une FAANG a trois personnes. Ou n'avoir aucun process. Le juste milieu : quelques regles tenues, pas vingt regles ignorees.

## En vrai

Fais une retro de 20 minutes apres deux semaines de mini-projet. Qu'est-ce qui a frotte ? Quelle phrase ajouter au README ? Une seule amelioration suffit par retro.


## Rituels hebdomadaires legers

Dix minutes lundi : branches mortes a supprimer ? CI rouge ignoree ? Secrets tournes apres un depart ? Une seule question par semaine suffit a eviter la poussiere.

## Onboarding d'un nouveau

Le premier jour, on ne lui demande pas de "lire tout le wiki". On lui donne le README "Comment on travaille", un acces, une petite PR de doc ou de typo pour vivre le flux. La premiere PR est un rituel d'equipe, pas un examen.

## Quand casser une regle

Rarement. Explicitement. Annonce dans le canal. Remets la regle apres. Une regle sans exception jamais discutee devient du theatre ; une exception tous les jours devient l'absence de regle.

## Mesure simple

Nombre de push directs sur main (doit tendre vers zero). Temps moyen avant premier regard sur une PR. Nombre de secrets revoques apres incident (doit etre "tous", tout de suite). Tu n'as pas besoin d'un dashboard : un ressenti honnete en retro suffit au debut.


## A toi

Choisis trois pratiques de ce chapitre et ecris-les comme "non negociables" pour ton equipe. Trois, pas quinze. Les tenir bat les collectionner.
