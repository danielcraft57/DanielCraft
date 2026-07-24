# Chapitre 3 - Strategie de branches simple (main + feature)

Une branche, tu la connais deja : une ligne d'historique parallele. En equipe, la question n'est plus "comment creer une branche", c'est "quelles branches on garde, et pour quoi faire".

Si tout le monde invente ses noms et ses durees, le depot devient un grenier. Si vous vous mettez d'accord une fois, Git devient invisible : il porte le travail sans drama.

## Le modele simple : main + features

`main` (parfois encore `master` ; on prefere `main`) est la branche de reference. Elle doit etre deployable, ou au moins "connue bonne".

Chaque nouvelle idee vit sur une branche feature (ou fix) :

```bash
git switch main
git pull
git switch -c feature/page-prix
```

Quand c'est pret et review : merge dans `main` via pull request. Puis on efface la branche feature. Elle a servi. Elle n'a pas vocation a vivre des mois.

C'est le modele qu'on recommande pour 2 a 5 personnes chez DanielCraft. Clair. Suffisant. Facile a expliquer a un stagiaire le premier jour. On l'appelle parfois "GitHub Flow" en version legere : une branche courte, une PR, un merge, on recommence.

## Noms de branches qui aident

Un bon nom dit l'intention. `feature/page-prix`, `fix/login-timeout`, `chore/maj-dependances`.

Tu peux utiliser `feature/` pour une nouveaute, `fix/` pour un correctif, `chore/` pour du menage (deps, config), `docs/` pour la doc. Ce n'est pas une loi universelle. C'est une convention d'equipe. Choisissez-en une et tenez-la.

Evite `max-wip`, `test2`, `final-final-v3`. Dans six mois, personne ne saura ce que c'etait. Y compris Max.

## Combien de temps une branche vit-elle ?

Idealement : heures ou quelques jours. Pas trois semaines sans sync.

Plus une branche vit longtemps, plus `main` avance sans elle, plus le retour sera douloureux. Synchronise souvent :

```bash
git switch main
git pull
git switch feature/page-prix
git merge main
```

Ou avec rebase (chapitre suivant). L'idee : ramener regulierement les nouveautes de `main` dans ta feature, avant le gros conflit du vendredi.

## Et develop ? Et release ?

GitFlow (avec `develop`, `release/*`, `hotfix/*`) existe. Il aide les grosses organisations avec des calendriers de release lourds. Pour une petite equipe produit qui deploie souvent, c'est souvent trop de ceremony.

Trunk-based development (tout le monde merge tres souvent dans `main`, parfois avec feature flags) est une autre ecole. Puissant, mais demande discipline et souvent une CI solide.

Pour ce livre : maitrise d'abord main + feature + PR. Tu pourras complexifier plus tard si le besoin est reel, pas par snobisme.

## Une branche par intention

Si Lea corrige un bug login et ajoute une page prix dans la meme branche, la review melange deux sujets. Au merge, si la page prix est douteuse mais le bug urgent, vous etes bloques.

Deux branches. Deux PR. Le bug peut partir ce soir. La page prix demain apres discussion.

## Branches partagees

Parfois deux personnes travaillent sur la meme feature. Possible. Alors : communication forte, petits commits, pull frequents sur la branche feature. Evite que chacun reecrive l'historique de l'autre (rebase force) sans se parler.

En general, preferer decouper le travail pour que chacun ait sa branche. Moins de friction.

## Hotfix : le petit frere du fix

Un bug en production. Sam cree `fix/bouton-payer` depuis `main` a jour, corrige, ouvre une PR courte, fait merger vite, deploie. Meme modele que la feature. Juste plus urgent, donc plus petit, plus cible.

Ne cree pas une usine a gaz "hotfix process" a trois personnes. Cree une branche claire et une PR lisible.

## Nettoyage

Apres merge, supprime la branche locale et distante. GitHub a souvent une case "Delete branch" apres merge. Localement :

```bash
git switch main
git pull
git branch -d feature/page-prix
```

De temps en temps, liste les vieilles branches. Un depot avec 80 branches mortes fatigue tout le monde.

```bash
git branch -a
```

## Carte mentale pour un stagiaire

Jour 1, tu peux coller ca au mur : "1. Je tire main. 2. Je cree feature/ou-fix/quelque-chose. 3. Je commit. 4. Je pousse ma branche. 5. J'ouvre une PR. 6. On review. 7. On merge. 8. Je retive main et j'efface ma branche." Si le stagiaire retient ca, il est deja utile a l'equipe.

## Erreur classique

Creer `feature/mega-refonte` et y vivre trois mois. Ou committer directement sur `main` "juste pour un petit truc". Les petits trucs s'accumulent. Puis un jour `main` est cassee et personne ne sait quel petit truc a fait le mal.

Autre piege : dix branches `feature/tmp` sans description. Le grenier gagne.

## En vrai

Ouvre ton depot. Liste les branches avec `git branch -a`. Combien sont mortes ? Combien ont un nom obscur ? Note trois renommages ou suppressions a faire. Hygiene = clarte.

## A toi

Ecris dans le README : "On travaille avec main + feature/*. Toute integration passe par une PR. Les branches feature vivent moins d'une semaine si possible." Adapte si besoin, mais ecris quelque chose. Une regle ecrite bat une regle imaginee.
