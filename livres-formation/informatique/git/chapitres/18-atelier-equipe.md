# Chapitre 18 - Atelier : workflow d'equipe (simule)

Meme seul, tu peux simuler deux personnes. L'idee n'est pas de "faire semblant pour le prof". C'est d'entrainer la vraie boucle : branche, push, **PR**, review, merge, pull. Chez DanielCraft, cet atelier prepare mieux a une equipe reelle qu'un chapitre theorique sur "la collab". Quand tu arrives en stage ou en freelance multi-dev, tu as deja joue Alice et Bob. Le stress baisse. Les reflexes montent. Tu n'inventes pas les regles sous pression. Tu les as deja ecrites.

Lea joue Alice et Bob sur deux dossiers clones. Max protege **`main`** sur GitHub apres s'etre force-push une fois de trop sur un depot de test (heureusement, pas en prod). Sam colle une mini charte dans `CONTRIBUTING.md` et la fait lire a voix haute avant le premier commit. Toi, tu vas jouer le jeu jusqu'au bout : deux PR mergees, historique lisible, charte ecrite. Objectif : 2 PR mergees, historique lisible. Duree : 40 a 60 minutes.

Deux personnes. Un depot. Une `main` protegee. Des branches courtes. Des PR petites. Une review meme rapide. Un merge. Un pull. La culture se code dans `CONTRIBUTING.md` autant que dans les habitudes. Chez DanielCraft, dix lignes de charte prevennent dix conflits evitables. Lea le sait. Max l'a appris. Sam l'enseigne avant le premier binome.

:::attention
`git push --force` reecrit l'histoire distante. Sur une branche partagee, ca peut effacer le travail des autres. A bannir sur `main` tant que tu ne maitrises pas.
:::

## Ce que ce n'est pas

Ce n'est pas une invitation a `push --force` sur `main` "parce que ca debloque". Ce n'est pas non plus "commit direct sur main parce que je suis seul donc les regles ne comptent pas". Les regles d'equipe s'entrainent avant d'etre imposees par un lead dev. Ce n'est pas obligatoire d'etre deux humains physiques : deux dossiers clones du meme depot suffisent. Alice a la main le matin, Bob l'apres-midi. Ou deux fenetres, deux navigateurs. Ce n'est pas non plus "provoquer un conflit des la premiere minute" - garde ca pour l'atelier conflits. Ici, on apprend a collaborer proprement d'abord.

## Idee et tour de jeu

Deux dossiers locaux : `alice/carnet` et `bob/carnet`. Tous deux clones du meme depot GitHub (ton carnet-git ou un depot de test). Alice cree une branche `feature/alice`, commit sur une zone de fichier (ex : README), push, ouvre une PR. Bob (toi, plus tard) fait `pull` sur `main` apres le merge. Bob cree `feature/bob` sur une autre zone (ex : notes.md), push, PR. Alice review - meme si c'est toi sous un autre compte ou le lendemain avec un oeil neuf. Regle d'or : une zone de fichier differente par personne au debut. Ca limite les conflits inutiles pendant l'apprentissage. Plus tard, tu gereras les vrais conflits. Ici, tu installes la boucle.

## Regles d'equipe simples

Personne ne commit directement sur `main` : branche + PR. Messages clairs, pas "update". PR petites : une idee, quelques fichiers. `pull` le matin avant de coder. Ne jamais forcer (`push --force`) sur `main`. Ne jamais committer `.env`. Chez DanielCraft, on ecrit ces regles dans CONTRIBUTING.md avant de coder. Dix lignes. Culture visible. Lea les lit en debut de mission. Max les a ignorees une fois. Il a regrette. Sam les fait lire a voix haute.

## force push ?

```bash
git push --force
```

A bannir sur les branches partagees tant que tu ne maitrises pas. Ca reecrit l'histoire distante. Ca peut effacer le travail des autres sans qu'ils le voient tout de suite. On le range dans "outils dangereux, pas jouets". Max l'a utilise une fois sur une branche perso. Jamais sur `main`. Lea protege `main` sur GitHub pour ne pas avoir a se faire confiance a 23h. Sam raconte l'histoire du force push "qui a tout efface" sans donner de noms. La peur utile. Pas la panique.

## Protection de branche

Sur GitHub : Settings -> Branches -> proteger `main`. Exige une PR pour merger. C'est une ceinture de securite. Lea l'active meme sur ses depots solo "serieux". Bon reflexe : tu ne peux plus te merger en panic sur main sans passer par la PR. Sam le recommande des le premier projet eleve heberge sur GitHub. Max l'a active apres son incident. Mieux vaut avant.

:::astuce
Protege `main` sur GitHub (Settings -> Branches). Meme en solo, c'est une ceinture de securite qui t'oblige a passer par une PR.
:::

## Mini charte (a coller)

Personne ne pousse en force sur `main`. Toute feature passe par une PR. On review au moins 1 fois (meme soi-meme en solo, le lendemain). On ne commit pas `.env`. On ecrit des messages qui se lisent dans `log --oneline`. Colle ca dans `CONTRIBUTING.md`. Dix lignes suffisent. La culture se code aussi dans un fichier texte. Tu peux ajouter "PR petites" et "pull le matin". Lea a ajoute "PR petites" apres une review de 800 lignes qui lui a coute une soiree entiere. Regle ecrite, douleur evitee la fois suivante.

## Petite histoire

Max a joue Alice/Bob un dimanche, merge deux PR, vu un historique lisible sur GitHub, sourit. Il a dit "c'est con mais ca change tout" - con en apparence, decisif en pratique. Sam a fait lire la charte a voix haute avant le premier commit en binome. Lea a ajoute "PR petites" apres sa soiree perdue. Chez DanielCraft, on aime ces regles courtes parce qu'elles tiennent. Les chartes de vingt pages, personne ne les lit. Dix lignes, oui.

## Erreur classique

Travailler tous les deux sur la meme ligne du meme fichier "pour voir le conflit" des la premiere minute - garde ca pour l'atelier conflits. Force push "parce que ca bloque". Oublier de `pull` apres un merge distant. Oublier d'ecrire CONTRIBUTING.md : les regles restent dans la tete, donc elles disparaissent. Autre piege : faire une seule PR monstrueuse "pour aller plus vite". Tu n'iras pas plus vite. Tu revieweras moins bien.

## En vrai

La prochaine fois que tu travailles vraiment a deux (stage, projet associatif, client avec un dev interne), relis ta charte avant de coder. Dix lignes prevennent dix conflits evitables. Lea le fait systematiquement en debut de mission. Max aussi, maintenant. Sam le fait avant chaque atelier binome.

## A toi

Joue Alice et Bob sur un depot de test. 2 PR mergees. Historique lisible. Ecris `CONTRIBUTING.md`. Puis protege `main` si tu peux. Livrable : depot avec 2 PR mergees + charte + notes de ce que "Alice" a dit a "Bob" en review. Garde ce depot. C'est une preuve de collab autant qu'une preuve de Git.
