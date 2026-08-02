# Chapitre 13 - Mini-projet : carnet versionne

On enchaine le vrai **workflow** du quotidien. Pas un exercice isole dans le vide : un petit projet `carnet-git` avec README, notes, historique propre, branche de feature, ignore, push GitHub. Chez DanielCraft, ce mini-projet sert de preuve. Quand tu l'as fait une fois sans paniquer, tu peux rejouer le film complet sur un vrai site, un script, ou un dossier de formation. Le livre cesse d'etre theorique. Il devient muscle.

Lea le fait en quinze minutes maintenant qu'elle a l'habitude. Max a mis quarante minutes la premiere fois, vingt la deuxieme. Sam chronometre la classe et celebre le process, pas la vitesse. Toi, vise la clarte d'abord. La vitesse viendra quand tu n'auras plus a relire chaque chapitre. Si tu bloques sur une etape, c'est un signal : rouvre le chapitre concerne dix minutes, puis reviens.

Local d'abord. Histoire propre ensuite. Branche pour une idee isolee. Merge quand c'est pret. Ignore les secrets avant qu'ils ne passent. Remote pour la copie lointaine. Preuve URL dans le README pour montrer que tu sais boucler la boucle. Tu reconnaitras cette sequence dans presque tous les projets serieux : init, commit, branch, merge, ignore, push. Une fois dans les doigts, tu la rejoues partout. Chez DanielCraft, on forme au transfert, pas a la recopie.

:::astuce
Chronometre-toi la premiere fois, puis refais le mini-projet une semaine plus tard. Sam a vu le temps chuter de moitie chez ses eleves - la qualite montait en meme temps.
:::

## Ce que ce n'est pas

Ce n'est pas un monorepo d'entreprise avec vingt equipes. Ce n'est pas non plus "juste push n'importe quoi pour cocher la case". Ce n'est pas obligatoire d'ouvrir une pull request des la premiere passe - c'est la variante avancee, utile si tu as deja lu le chapitre 16. Les criteres minimum restent simples : au moins 4 commits lisibles, une branche fusionnee, un `.gitignore`, un projet visible sur GitHub (prive OK). Sans ca, le mini-projet ne compte pas comme reussi.

Ce n'est pas non plus une course. Si tu prends une heure la premiere fois en comprenant chaque geste, c'est mieux qu'un sprint opaque de douze minutes. Lea prefere la clarte. Max aussi, maintenant. Sam note le process dans la grille d'evaluation, pas le chrono seul.

## But

Un petit projet `carnet-git` avec un `README.md`, un `notes.md`, un historique propre, une branche de feature, et un push GitHub. C'est ton portfolio Git minimal. Lea le montre parfois a un client pour prouver qu'elle sait travailler proprement. Max l'a montre a un ami developpeur. Sam le demande en fin de module comme preuve.

## Etapes

### 1. Local

```bash
mkdir carnet-git
cd carnet-git
git init
```

Ecris un README (but + auteur). Commit : `Initialiser le carnet`

### 2. Notes

Ajoute `notes.md` avec trois idees courtes. Commit : `Ajouter les premieres notes`

### 3. Branche

```bash
git switch -c feature/note-git
```

Ajoute une note sur Git. Commit. Reviens sur `main` et merge.

### 4. Ignore

Ajoute `.gitignore` avec `.env` et un faux secret local. Commit : `Ignorer les fichiers sensibles`

### 5. GitHub

Cree le depot distant sur GitHub. Puis `remote add` + `push -u origin main`

### 6. Preuve

Copie l'URL GitHub dans ton `README.md`. Commit + push.

A chaque etape, lance `status`. Lis. Avance. Si quelque chose cloche, stop. Une commande. Un controle. Chez DanielCraft, c'est la methode anti-panic du mini-projet.

## Variante avancee

Ouvre une issue "Ameliorer le README". Cree une branche depuis cette idee. Ouvre une pull request (chapitre 16). Merge via la PR au lieu d'un merge local silencieux. Lea le fait systematiquement sur les projets clients, meme en solo, pour s'obliger a resumer son travail avant de fusionner. Max l'a ajoutee la deuxieme fois. Sam la propose en bonus, jamais en piege.

:::attention
Criteres minimum : 4 commits lisibles, une branche fusionnee, un `.gitignore`, un depot visible sur GitHub (prive OK). Sans ca, le mini-projet ne compte pas.
:::

## Petite histoire

Max a invite un ami en lecture seule sur le depot. L'ami a compris le README sans appeler Max. Max a ete fier - et a corrige deux messages de commit flous juste apres, parce que l'historique etait aussi visible que le README. Sam a fait refaire le mini-projet une semaine plus tard en classe : le temps a chute, la qualite a monte, les erreurs (oublier `.gitignore`, messages "update") ont presque disparu. Chez DanielCraft, on aime cette deuxieme passe. La premiere apprend. La seconde ancre. Lea le refait parfois quand elle change d'ordinateur : rituel de remise en main.

## Erreur classique

Sauter `.gitignore` "parce que c'est un faux projet". Messages "update" ou "test". Merger sans verifier `status` avant et apres. Pousser un secret "pour voir si Git le detecte" - spoiler : Git ne juge pas, il enregistre. Vouloir la variante PR avant d'avoir un historique local propre. Une marche apres l'autre. Autre piege : oublier l'URL dans le README - tu as pousse, mais tu n'as pas ferme la boucle "preuve".

## En vrai

Chronometre-toi sans stress. Vise moins de 20 minutes une fois a l'aise. Puis invite quelqu'un en lecture seule si tu peux : le regard exterieur revele les trous du README et les messages flous. Si tu es seul, relis ton `log --oneline` a voix haute comme si tu expliquais a Lea. Si ca sonne clair, c'est bon.

## A toi

Livrable : URL du depot (prive OK) + 4 commits lisibles minimum + branche fusionnee + `.gitignore`. Ecris aussi en trois lignes ce qui t'a freine pendant le mini-projet. On reutilise ca dans les ateliers. Garde l'URL : tu y reviendras au quiz et au bravo.
