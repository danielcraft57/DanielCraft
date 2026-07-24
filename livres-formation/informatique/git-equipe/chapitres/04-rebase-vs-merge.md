# Chapitre 4 - Rebase vs merge : idee, quand, risques

Tu as deja fusionne avec `git merge`. Ca cree parfois un commit de merge, et l'historique montre que deux lignes se sont rejointes. Le rebase, c'est une autre facon de "mettre a jour" ta branche : rejouer tes commits comme s'ils etaient partis plus tard, sur une base plus recente.

Ce n'est pas une religion. Chez DanielCraft, on refuse le dogme "toujours rebase" ou "jamais rebase". On veut que tu comprennes l'idee, le moment, et le danger.

## L'idee en une image

Imagine que `main` avance. Ta feature est partie d'un vieux point. Merge, c'est coller les deux histoires avec un noeud. Rebase, c'est decouper tes commits de ta feature et les recoller proprement au bout de `main`, un par un.

Resultat frequent du rebase : un historique plus lineaire, plus facile a lire avec `git log --oneline`. Resultat frequent du merge : un historique qui montre vraiment les allers-retours d'equipe.

Les deux sont valides. Le choix depend du contexte et de l'accord d'equipe.

## Un cas concret : Lea met a jour sa feature

Lea est sur `feature/page-tarifs`. Max a merge un fix sur `main`. Lea veut ces changements avant sa PR.

Option merge :

```bash
git switch feature/page-tarifs
git fetch origin
git merge origin/main
```

Option rebase :

```bash
git switch feature/page-tarifs
git fetch origin
git rebase origin/main
```

Dans les deux cas, elle peut avoir des conflits. Elle les regle. La difference, c'est la forme de l'historique ensuite.

## Quand le rebase aide

Le rebase aide souvent sur une branche feature personnelle, pas encore partagee (ou partagee seulement par toi), pour la "reposer" sur `main` avant la review. L'historique de la PR devient une suite claire de commits, sans noeud de merge intermediaire.

Il aide aussi pour nettoyer localement avant de pousser (voir chapitre 5 sur l'historique propre), parfois avec un rebase interactif. Attention : interactif = plus de puissance, plus de responsabilite.

## Quand le merge est plus simple (et plus sur)

Si plusieurs personnes poussent sur la meme branche feature, un rebase + force push peut casser le travail des autres. Merge est alors plus doux : il n'exige pas de reecrire l'historique deja publie.

Si tu n'es pas a l'aise, merge. Un merge un peu bruyant bat un rebase mal compris qui reecrit l'histoire de tout le monde.

## Le risque numero un : reecrire l'histoire partagee

Rebase change les identifiants de commits (les hash). Ce ne sont plus "les memes" commits, ce sont des copies rejouees. Si tu as deja pousse ces commits et que d'autres les ont tires, tu dois souvent pousser avec `--force` (ou `--force-with-lease`). Sur `main`, c'est en general interdit et dangereux. Sur une branche perso, c'est parfois OK si tu es seul dessus.

Regle d'or : ne rebase pas `main`. Ne force-push pas `main`. Ne rebase pas la branche d'un collegue sans qu'il le sache.

```bash
# Sur TA feature, apres rebase local, si deja poussee :
git push --force-with-lease
```

`--force-with-lease` est plus poli que `--force` : il refuse d'ecraser si quelqu'un a pousse entre-temps. Prefere-le.

## Conflits : meme stress, meme methode

Que tu merges ou rebases, un conflit veut dire : deux changements touchent la meme zone. Tu ouvres le fichier, tu choisis (ou combines), tu marques resolu.

En merge :

```bash
git add fichier.html
git merge --continue
```

En rebase (souvent) :

```bash
git add fichier.html
git rebase --continue
```

Si tu es perdu pendant un rebase :

```bash
git rebase --abort
```

Tu reviens a l'etat d'avant le rebase. Respire. Recommence autrement si besoin (par exemple avec un merge).

## Sans dogme : une politique d'equipe possible

Exemple de politique simple pour une equipe de 3 :

On merge les pull requests dans `main` (bouton Merge sur GitHub, parfois "squash merge" - chapitre 5). Sur sa feature perso, chacun peut rebase sur `main` avant la PR pour limiter le bruit. Personne ne rebase une branche partagee sans message dans le canal.

Ecrivez deux phrases dans le README. Ca suffit.

## Erreur classique

Faire un rebase sur `main` local puis pousser en force "parce que mon log est plus joli". Ou lancer un rebase interactif le jour de la release sans filet. Ou expliquer a un stagiaire que merge est "moche" : tu crees de la honte inutile. L'outil sert l'equipe, pas l'inverse.

## En vrai

Sur un depot de test, cree une branche, fais deux commits, avance `main` avec un autre commit, puis teste les deux options (merge puis, dans une autre copie de branche, rebase). Regarde `git log --oneline --graph`. Vois la difference avec tes yeux, pas seulement dans un article.

```bash
git log --oneline --graph --decorate -15
```

## A toi

Choisis avec ton equipe (meme si l'equipe c'est toi et un ami) : "rebase OK sur feature perso, merge pour integrer dans main" ou "merge partout pour simplifier". Ecris le choix. Le pire choix, c'est le non-choix ou chacun fait sa religion en silence.
