# Chapitre 16 - Pull requests (PR)

Une **pull request**, c'est "peux-tu fusionner mon travail dans la branche principale ?". C'est le coeur de la **collaboration** sur GitHub et la plupart des hebergeurs modernes. Tu proposes. Quelqu'un lit. On discute. On merge. L'historique reste plus clair qu'un push silencieux sur `main` a 23h un vendredi. Chez DanielCraft, meme en solo, une PR t'oblige a resumer ton travail avant de fusionner. C'est sain. Ca evite les merges "fix stuff" sans contexte.

Lea ouvre des PR pour chaque feature client, meme petite. Max a commence en mergeant tout seul en local, puis a adopte les PR pour s'entrainer avant de rejoindre une equipe. Sam fait lire deux PR open source en classe : le format revient partout, du petit projet perso au gros framework. Toi, tu vas en ouvrir une, meme pour une ligne de README. L'objectif n'est pas la paperasse. C'est la relecture. C'est le pont social au-dessus du pont technique Git.

Tu crees une branche pour une idee. Tu commits proprement. Tu push la branche sur le remote. Sur GitHub, tu ouvres Compare & pull request. Tu ecris but, changes, comment tester. Quelqu'un review (ou toi-meme le lendemain avec un oeil frais). On merge. En local, tu reviens sur `main` et tu `pull` pour recuperer la fusion. Sans description, le pont est glissant. Lea met toujours "comment tester" meme quand elle merge seule. Chez DanielCraft, "comment tester" est non negociable sur une PR serieuse.

:::retenir
Une bonne description PR : but en deux lignes, liste des fichiers changes, comment tester. Sans ca, la review double de temps.
:::

## Ce que ce n'est pas

Une PR, ce n'est pas un virus ni une formalite inutile reservee aux grosses boites. Ce n'est pas non plus "seulement pour les equipes de dix personnes". Ce n'est pas un commit : c'est une proposition de fusion entre branches, avec discussion. Ce n'est pas obligatoire d'utiliser squash si ton equipe prefere merge commit - demande la convention, note-la. Et ce n'est surtout pas une excuse pour une PR monstrueuse de 40 fichiers sans description : personne ne reviewera correctement. Prefere trois petites PR a une usine a gaz.

Ce n'est pas non plus "obligatoire d'attendre quelqu'un d'autre". En solo, tu peux ouvrir, relire le lendemain, merger toi-meme. L'oeil frais compte. Lea le fait souvent. Max aussi, maintenant. Sam l'impose comme exercice : review le lendemain, pas dans la seconde.

## Scenario type

Tu crees une branche avec `git switch -c feature/login`. Tu fais tes commits locaux avec des messages clairs. Tu push : `git push -u origin feature/login`. Sur GitHub, tu cliques Compare & pull request. Tu remplis titre + description. Quelqu'un review, commente des lignes si besoin. On merge sur GitHub. En local : `git switch main` puis `git pull`. La boucle est complete. Max l'a faite dix fois en solo avant de la faire en equipe : zero surprise le jour J. Lea la rejoue sur chaque feature. Sam la chronometre en atelier sans stresser sur la vitesse.

## Pourquoi pas merger en silence ?

Ca permet la relecture, la discussion, les tests automatiques (CI) si tu en ajoutes plus tard, et un historique plus clair avec une trace de la decision. Meme en solo, une PR t'oblige a resumer : "qu'est-ce que j'ai change et pourquoi ?". Draft PR : tu peux ouvrir en brouillon pour montrer l'avancement sans demander le merge tout de suite. Lea adore les drafts sur les gros sujets client : le client voit l'avancement, personne ne merge par accident. Max a decouvert les drafts apres une merge prematuree. Sam les recommande des qu'une feature depasse une demi-journee.

:::astuce
Lea ouvre des draft PR sur les gros sujets : tu montres l'avancement sans demander le merge tout de suite. Utile pour debloquer une discussion.
:::

## Bonne description

Voici un modele simple qui marche :

```text
## But
Ajouter un formulaire de contact.

## Changes
- page contact.html
- validation email basique

## Test
Ouvrir /contact et envoyer un faux message.
```

En review, on commente des lignes precises. Tu pousses des commits sur la meme branche : la PR se met a jour automatiquement. Simple et puissant. Chez DanielCraft, on refuse le dogme "squash obligatoire" : on veut une convention ecrite, meme courte, dans CONTRIBUTING.md. Coherent bat clever.

## Merge buttons

Tu verras souvent Create a merge commit, Squash and merge (souvent propre pour petites features), et Rebase and merge. Chacun laisse une trace differente dans l'historique. Demande la convention de ton equipe. En solo, choisis-en une et tiens-toi y. L'important : etre coherent, pas etre "le plus clever". Lea squash souvent sur les petites features. Max garde le merge commit pour voir la jonction. Sam montre les trois sans religion.

## Petite histoire

Max a ouvert une PR vers `main` sur son carnet-git, merge lui-meme apres relecture le lendemain, puis `pull` en local. La boucle est devenue reelle, pas theorique. Lea a mis un modele de description dans son README (section Contributing) pour ne plus reinventer la roue. Sam a fait comparer une PR claire et une PR "fix stuff" en timing : le temps de review doublait sur la mauvaise. La qualite de la demande change la qualite de la reponse. Toujours. Chez DanielCraft, c'est une lecon de collab autant qu'une lecon de Git.

## Erreur classique

PR sans description ("voir commits" n'est pas une description). Travailler directement sur `main` "parce que je suis seul" jusqu'au jour ou tu ne l'es plus. Force push sur la branche de PR partagee sans prevenir. Ouvrir une PR avant d'avoir un `.gitignore` et un README - tu demandes une review sur un chantier sale. Autre piege : PR de 800 lignes "parce que c'etait plus simple". Personne ne reviewera bien. Decoupe.

## En vrai

Lis 2 PR open source sur GitHub (Documentation, typo fix, petit feature). Tu verras le meme format partout. Puis ouvre la tienne, meme pour une ligne de README. Merge-la proprement. Refais `git pull` en local. C'est ton diplome du chapitre. Garde le modele de description. Tu le reutiliseras.

## A toi

Cree une branche avec 1 commit utile. Push. Ouvre une PR vers `main`. Merge-la toi-meme apres relecture. Puis `git pull` en local. Bonus : ecris un modele de description PR dans ton README (section Contributing). Garde-le pour les projets futurs.
