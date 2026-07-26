# Chapitre 3 - Strategie de branches simple (main + feature)

Une branche, tu la connais deja : une ligne d'historique parallele. En equipe, la question n'est plus "comment creer une branche", c'est "quelles branches on garde, et pour quoi faire". Si tout le monde invente ses noms et ses durees, le depot devient un grenier. Si vous vous mettez d'accord une fois, Git devient invisible : il porte le travail sans drama. Chez DanielCraft, on recommande pour deux a cinq personnes le modele **main** plus **features**. Clair. Suffisant. Facile a expliquer a un stagiaire le premier jour. On l'appelle parfois **GitHub Flow** en version legere : une branche courte, une PR, un merge, on recommence. Pas besoin de six types de branches pour livrer un site vitrine. Besoin d'une intention claire et d'une duree courte.

`main` (parfois encore `master` ; on prefere `main`) est la branche de reference. Elle doit etre deployable, ou au moins "connue bonne". Chaque nouvelle idee vit sur une branche feature ou fix :

```bash
git switch main
git pull
git switch -c feature/page-prix
```

Quand c'est pret et review : merge dans `main` via **pull request**. Puis on efface la branche feature. Elle a servi. Elle n'a pas vocation a vivre des mois.

:::retenir
Une branche feature a une intention, un nom clair, et une duree courte. Apres merge, elle disparait.
:::

## Noms et duree de vie

Un bon nom dit l'intention. `feature/page-prix`, `fix/login-timeout`, `chore/maj-dependances`. Tu peux utiliser `feature/` pour une nouveaute, `fix/` pour un correctif, `chore/` pour du menage, `docs/` pour la doc. Ce n'est pas une loi universelle. C'est une convention d'equipe. Choisissez-en une et tenez-la. Evite `max-wip`, `test2`, `final-final-v3`. Dans six mois, personne ne saura ce que c'etait. Y compris Max.

Idealement, une branche vit heures ou quelques jours. Pas trois semaines sans sync. Plus une branche vit longtemps, plus `main` avance sans elle, plus le retour sera douloureux. Synchronise souvent :

```bash
git switch main
git pull
git switch feature/page-prix
git merge main
```

Ou avec rebase (chapitre suivant). L'idee : ramener regulierement les nouveautes de `main` dans ta feature, avant le gros conflit du vendredi.

:::astuce
Si ta branche a plus d'une semaine, synchronise `main` dedans aujourd'hui. Pas "quand j'aurai le temps".
:::

## Ce que ce n'est pas (encore)

GitFlow avec `develop`, `release/*`, `hotfix/*` existe. Il aide les grosses organisations avec des calendriers de release lourds. Pour une petite equipe produit qui deploie souvent, c'est souvent trop de ceremony. Trunk-based development (tout le monde merge tres souvent dans `main`, parfois avec feature flags) est une autre ecole. Puissant, mais demande discipline et souvent une CI solide. Pour ce livre : maitrise d'abord main plus feature plus PR. Tu pourras complexifier plus tard si le besoin est reel, pas par snobisme.

Si Lea corrige un bug login et ajoute une page prix dans la meme branche, la review melange deux sujets. Au merge, si la page prix est douteuse mais le bug urgent, vous etes bloques. Deux branches. Deux PR. Le bug peut partir ce soir. La page prix demain apres discussion. Un bug en production : Sam cree `fix/bouton-payer` depuis `main` a jour, corrige, ouvre une PR courte, fait merger vite, deploie. Meme modele que la feature. Juste plus urgent, donc plus petit, plus cible. Ne cree pas une usine a gaz "hotfix process" a trois personnes.

Apres merge, supprime la branche locale et distante. GitHub a souvent une case "Delete branch" apres merge. Localement :

```bash
git switch main
git pull
git branch -d feature/page-prix
```

De temps en temps, liste les vieilles branches. Un depot avec quatre-vingts branches mortes fatigue tout le monde. Jour 1, tu peux coller au mur : "1. Je tire main. 2. Je cree feature/ou-fix/quelque-chose. 3. Je commit. 4. Je pousse ma branche. 5. J'ouvre une PR. 6. On review. 7. On merge. 8. Je retive main et j'efface ma branche."

## Petite histoire

Max a cree `feature/mega-refonte` et y a vecu trois mois. Le merge a ete un vendredi noir. Lea et Sam ont passe le week-end a resoudre des conflits melanges avec trois sujets differents. Depuis, l'equipe a ecrit : "Les branches feature vivent moins d'une semaine si possible." Une regle ecrite bat une regle imaginee.

Chez DanielCraft, on raconte souvent cette scene pour calmer les ambitions de branche eternelle. L'ambition, c'est bien. La tranche livrable, c'est mieux.

## Erreur classique

Creer `feature/mega-refonte` et y vivre trois mois. Ou committer directement sur `main` "juste pour un petit truc". Les petits trucs s'accumulent. Puis un jour `main` est cassee et personne ne sait quel petit truc a fait le mal. Autre piege : dix branches `feature/tmp` sans description. Le grenier gagne. Parfois deux personnes travaillent sur la meme feature : communication forte, petits commits, pull frequents. Evite que chacun reecrive l'historique de l'autre sans se parler.

:::attention
Un "petit truc" sur `main` sans PR, c'est souvent le debut d'une chasse au bug sans filet. Passe par une branche, meme pour dix lignes.
:::

## En vrai

Ouvre ton depot. Liste les branches avec `git branch -a`. Combien sont mortes ? Combien ont un nom obscur ? Note trois renommages ou suppressions a faire. Hygiene egal clarte.

## A toi

Ecris dans le README : "On travaille avec main plus feature/*. Toute integration passe par une PR. Les branches feature vivent moins d'une semaine si possible." Adapte si besoin, mais ecris quelque chose. Une regle ecrite bat une regle imaginee.
