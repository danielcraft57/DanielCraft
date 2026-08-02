# Chapitre 4 - Rebase vs merge : idee, quand, risques

Tu as deja fusionne avec `git merge`. Ca cree parfois un commit de merge, et l'historique montre que deux lignes se sont rejointes. Le **rebase**, c'est une autre facon de "mettre a jour" ta branche : rejouer tes commits comme s'ils etaient partis plus tard, sur une base plus recente. Ce n'est pas une religion. Chez DanielCraft, on refuse le dogme "toujours rebase" ou "jamais rebase". On veut que tu comprennes l'idee, le moment, et le danger. Un outil mal compris fait plus de degats qu'un outil "moins elegant" bien tenu.

Imagine que `main` avance. Ta feature est partie d'un vieux point. **Merge**, c'est coller les deux histoires avec un noeud. Rebase, c'est decouper tes commits de ta feature et les recoller proprement au bout de `main`, un par un. Resultat frequent du rebase : un historique plus lineaire, plus facile a lire avec `git log --oneline`. Resultat frequent du merge : un historique qui montre vraiment les allers-retours d'equipe. Les deux sont valides. Le choix depend du contexte et de l'accord d'equipe.

:::retenir
Merge et rebase sont deux outils. Ni honte, ni heroisme. Choisis, ecris la politique, respecte-la.
:::

## Un cas concret : Lea met a jour sa feature

Lea est sur `feature/page-tarifs`. Max a merge un fix sur `main`. Lea veut ces changements avant sa PR. Option merge :

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

Dans les deux cas, elle peut avoir des conflits. Elle les regle. La difference, c'est la forme de l'historique ensuite. Le rebase aide souvent sur une branche feature personnelle, pas encore partagee, pour la "reposer" sur `main` avant la review. Il aide aussi pour nettoyer localement avant de pousser, parfois avec un rebase interactif. Attention : interactif egal plus de puissance, plus de responsabilite.

## Quand le merge est plus simple (et plus sur)

Si plusieurs personnes poussent sur la meme branche feature, un rebase plus force push peut casser le travail des autres. Merge est alors plus doux : il n'exige pas de reecrire l'historique deja publie. Si tu n'es pas a l'aise, merge. Un merge un peu bruyant bat un rebase mal compris qui reecrit l'histoire de tout le monde. Regle d'or : ne rebase pas `main`. Ne force-push pas `main`. Ne rebase pas la branche d'un collegue sans qu'il le sache.

```bash
# Sur TA feature, apres rebase local, si deja poussee :
git push --force-with-lease
```

`--force-with-lease` est plus poli que `--force` : il refuse d'ecraser si quelqu'un a pousse entre-temps. Prefere-le. Que tu merges ou rebases, un **conflit** veut dire : deux changements touchent la meme zone. Tu ouvres le fichier, tu choisis ou combines, tu marques resolu. En merge : `git add fichier.html` puis `git merge --continue`. En rebase : `git add fichier.html` puis `git rebase --continue`. Si tu es perdu : `git rebase --abort`. Tu reviens a l'etat d'avant. Respire.

:::attention
Ne rebase jamais `main` partagee. Ne force-push jamais `main`. Sur une feature perso deja poussee, prefere `--force-with-lease`.
:::

Exemple de politique simple pour une equipe de trois : on merge les pull requests dans `main` (bouton Merge sur GitHub, parfois "squash merge" - chapitre 5). Sur sa feature perso, chacun peut rebase sur `main` avant la PR pour limiter le bruit. Personne ne rebase une branche partagee sans message dans le canal. Ecrivez deux phrases dans le README. Ca suffit. L'outil sert l'equipe, pas l'inverse.

Sam explique souvent le graphique : merge = noeud visible, rebase = ligne droite. Lea prefere la ligne droite sur sa feature. Max prefere merge partout "parce que je dors mieux". Les deux politiques marchent si elles sont ecrites.

## Petite histoire

Sam a explique a un stagiaire que merge etait "moche". Le stagiaire a eu peur de merge pendant un mois. Puis il a fait un rebase force sur une branche partagee. Deux heures de reparations. Chez DanielCraft, on dit : merge et rebase sont deux outils. Ni honte, ni heroisme. Choisis, ecris, respecte.

Lea, elle, a teste les deux sur un depot de jouet. Elle a regarde `git log --graph`. Elle a choisi. Depuis, plus de dogme silencieux dans l'equipe.

## Erreur classique

Faire un rebase sur `main` local puis pousser en force "parce que mon log est plus joli". Ou lancer un rebase interactif le jour de la release sans filet. Ou expliquer que merge est "moche" : tu crees de la honte inutile. Le pire choix, c'est le non-choix ou chacun fait sa religion en silence.

:::astuce
Si tu es perdu en plein rebase : `git rebase --abort`. Tu reviens a l'avant. Puis tu respireras, puis tu recommenceras.
:::

## En vrai

Sur un depot de test, cree une branche, fais deux commits, avance `main` avec un autre commit, puis teste les deux options (merge puis, dans une autre copie de branche, rebase). Regarde la difference avec tes yeux :

```bash
git log --oneline --graph --decorate -15
```

## A toi

Choisis avec ton equipe (meme si l'equipe c'est toi et un ami) : "rebase OK sur feature perso, merge pour integrer dans main" ou "merge partout pour simplifier". Ecris le choix. Le pire choix, c'est le non-choix.
