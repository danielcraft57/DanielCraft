# Chapitre 6 - Les branches

Une **branche**, c'est une piste parallele. Tu experimentes sans casser la version stable. Sur **`main`**, tu gardes ce qui marche. Sur `idee-couleurs`, tu oses. Si ca marche, tu fusionneras. Si ca ne marche pas, tu jettes la branche. `main` reste intact. Chez DanielCraft, ce reflexe est pro meme en solo : avant chaque experience, nouvelle branche. Ce n'est pas de la paperasse. C'est une assurance.

Lea cree une branche par feature client. Une idee = une piste. Max a decouvert le "retour sur main" et a cru a la magie la premiere fois : les fichiers "revenaient" a l'etat d'avant. Sam fait creer `essai`, ajouter un fichier, revenir : le fichier disparait de la vue de travail. Lecon concrete en trente secondes. Toi, tu vas vivre ce moment. Ensuite, les branches ne seront plus abstraites. Elles seront un geste.

Sans branches, tu as un album. Avec branches, tu as des albums paralleles. Tu peux corriger un bug urgent sur `main` pendant qu'une feature avance ailleurs. Tu peux tester une typo risquee sans polluer la version stable. Tu peux jeter une piste sans pleurer. `main` est la route principale. Tu ouvres une route de chantier. Tu y poses des commits. Quand tu reviens sur `main`, tu revois le paysage d'avant. Les commits de la branche n'ont pas disparu : ils sont sur l'autre piste.

:::retenir
`main` garde ce qui marche. Une branche sert a oser. Si ca rate, tu jettes la piste, pas le projet.
:::

## Ce que ce n'est pas

Une branche, ce n'est pas une copie complete lourde du projet "comme un dossier zip". Git est malin : il partage l'historique commun et ne duplique pas tout betement. Ce n'est pas non plus un conflit automatique. Ce n'est pas obligatoire d'avoir dix branches ouvertes. Et ce n'est surtout pas "trop avance pour un debutant" : c'est le coeur de Git.

Ce n'est pas non plus "creer une branche = sauvegarder automatiquement". Tant que tu n'as pas commit sur la branche, tes fichiers modifies restent des griffonnages locaux. Une branche pointe vers un commit. Sans commit, tu n'as pas encore d'histoire sur cette piste. Lea le rappelle souvent. Max l'a appris en creant `essai` puis en oubliant de committer.

## Creer, changer, travailler

```bash
git branch
```

Souvent tu as `main` (ou `master` sur de vieux depots).

```bash
git branch idee-couleurs
git switch idee-couleurs
```

Ou en une commande :

```bash
git switch -c idee-couleurs
```

(`git checkout -b ...` existe encore. `switch` est plus clair.)

Modifie un fichier. Commit.

```bash
git log --oneline
```

Ces commits sont sur `idee-couleurs`. `main` n'a pas encore ces changements.

```bash
git switch main
```

Tes fichiers "reviennent" a l'etat de `main`. Magique la premiere fois. Normal ensuite. Sam fait creer `essai`, ajouter un fichier, commit, revenir sur `main` : le fichier disparait de la vue. Les eleves comprennent les branches en trente secondes.

Lea nomme ses branches comme des intentions : `fix-header`, `essai-typo`, `feature/contact`. Un nom flou (`test2`) devient une dette mentale en deux semaines. Sam interdit `test`, `tmp`, `new` en atelier. Trop vague. Trop vite oublie.

## A quoi ca sert vraiment ?

Tu lances une feature en cours. Tu corriges en urgence sur `main` pendant que tu experimentes ailleurs. Ou tu testes un essai risque, puis tu jettes la branche si ca ne marche pas. Lea a sauve un vendredi comme ca. Max a arrete de "commenter tout le CSS" pour experimenter : il branche. Sam dit aux eleves : "si tu as peur de casser, tu n'as pas encore cree de branche". Phrase un peu dure. Phrase juste.

## Renommer / supprimer

```bash
git branch -m ancien-nom nouveau-nom
git branch -d idee-couleurs
```

`-d` refuse s'il reste des commits non fusionnes. `-D` force (prudent). Chez DanielCraft, on prefere comprendre pourquoi `-d` refuse avant de forcer. Souvent, c'est Git qui te protege d'une perte. Ecoute-le. Puis decide.

:::astuce
Nomme tes branches comme des intentions : `fix-header`, `essai-typo`. Un nom flou (`test2`) devient une dette mentale en deux semaines.
:::

## Petite histoire

Sam a demande deux branches : `page-a` et `page-b`, un commit different sur chacune. Les eleves ont note ce que `log` montrait sur chaque. La difference est devenue visuelle. Lea nomme ses branches clairement. Max a jete une branche `essai-couleurs` apres un echec : `main` intact, zero stress. Chez DanielCraft, c'est le moment ou Git cesse d'etre "un truc de developpeurs" et devient une assurance pour tout projet un peu serieux.

## Erreur classique

Travailler sur `main` "parce que c'est plus simple", puis tout melanger. Oublier sur quelle branche tu es (`git branch` / `git status` te le disent). Supprimer avec `-D` trop vite. Autre piege : creer une branche sans commit dessus et s'etonner que "rien n'existe". Encore un piege : dix branches ouvertes sans fusionner pendant un mois. Merge souvent. Petits pas. On y vient au chapitre suivant.

## En vrai

Avant chaque experience : nouvelle branche. Reflexe pro, meme en solo. Fais l'exercice `essai` maintenant, pas "plus tard". Sens le retour sur `main`. Ce basculement doit devenir naturel. Ouvre aussi `git log --oneline --graph --all` pour voir plusieurs pistes.

## A toi

Cree une branche `essai`. Ajoute un fichier `essai.txt` et commit. Reviens sur `main`. Verifie que `essai.txt` n'est plus la (normal). Bonus : deux branches `page-a` et `page-b`, un commit different sur chacune, note ce que `log` montre. Ecris en une phrase : "a quoi me sert une branche sur mon prochain projet".
