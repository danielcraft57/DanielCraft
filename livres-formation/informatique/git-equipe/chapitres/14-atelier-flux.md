# Chapitre 14 - Atelier : flux d'equipe

Cet atelier fait vivre le chapitre 2 avec les mains. Tu joues deux roles : Alex (feature) et Blake (reviewer). Un seul ordinateur suffit. Chez DanielCraft, on prefere un atelier fait a fond a trois ateliers survoles. Chronometre : 45 a 90 minutes. Ecris le **livrable**. Sans livrable, le cerveau classe ca comme "lu", pas comme "su".

Tu vas marcher le **flux** complet une fois : `main` a jour, **branche**, commits, push, **PR**, **review**, **merge**, retour propre sur `main`. Lea fait ca chaque matin sans y penser. Max aussi. Sam a appris en se brulant. Toi, tu le fais lentement une fois pour que ca devienne un reflexe. Le depot de test, pas le client critique. Les mains d'abord, la vitesse ensuite. Si tu sautes une etape "parce que c'est petit", tu rates exactement le muscle a construire.

:::retenir
Le sentier complet, une fois lentement, vaut mieux que dix lectures du chapitre flux.
:::

## But et materiel

Partir de `main` a jour, creer une branche, pousser, ouvrir une PR, faire merger, revenir sur `main` proprement. Materiel : depot GitHub de test, Git configure, navigateur, une page `index.html` deja sur `main` (meme minimale). Pas ton vrai projet client. Si tu n'as pas de depot de test, cree-en un en dix minutes. L'atelier vaut ce detour.

Avant de commencer, ecris sur un papier les neuf etapes. Coche au fur et a mesure. Le papier force le rythme. Lea le fait encore parfois quand elle forme un stagiaire. Max prefere une checklist dans le README. Sam chronometre. Choisis ton outil, mais ne compte pas sur ta memoire seule.

## Etapes

1. Clone ou ouvre le depot, place-toi sur `main`, tire.

```bash
git switch main
git pull
```

2. Cree `feature/bandeau-accueil` et ajoute un bandeau texte dans `index.html` ("Bienvenue chez nous").

```bash
git switch -c feature/bandeau-accueil
```

3. Au moins deux commits : HTML, puis un peu de CSS si tu veux. Messages clairs (pourquoi). Pas "fix" et "update". Dis ce que le bandeau change pour l'humain.

4. Pousse la branche (pas `main`).

```bash
git push -u origin feature/bandeau-accueil
```

5. Ouvre une PR vers `main`. Titre clair. Description : but + "comment tester" (ouvrir l'accueil, voir le bandeau). Verifie `base: main` avant d'envoyer.

6. En mode Blake, relis le diff. Laisse un commentaire bienveillant (meme mineur). Approuve. Si tu es seul, change de casquette : relis comme si tu ne connaissais pas le commit.

7. Merge (bouton GitHub). Coche suppression de branche distante si proposee.

8. En local : reviens sur `main`, tire, supprime la branche locale.

```bash
git switch main
git pull
git branch -d feature/bandeau-accueil
```

9. Verifie `git status` propre et `git log --oneline -5` coherent. Le bandeau doit etre visible dans le navigateur sur `main`.

:::astuce
Variante a deux : Alex fait 1-5, Blake 6-7, Alex 8-9. Parlez a voix haute : "PR prete", "review ok", "c'est merge".
:::

## Petite histoire

Alex (toi) a voulu pousser direct sur `main` "parce que c'est petit". Blake a refuse. La PR a force une description. Deux jours plus tard, le bandeau avait un typo : la description "comment tester" a aide a le voir avant merge. Lea raconte souvent cette scene : le "petit truc" sans PR, c'est le piege classique. Max sourit. Sam coche la case Delete branch.

Chez DanielCraft, on chronometre parfois l'atelier. Quarante-cinq minutes suffisent si le depot de test est pret. Quatre-vingt-dix minutes si tu debutes vraiment le remote. L'important n'est pas le chronometre. C'est le sentier complet sans raccourci.

## Criteres et blocages

Aucun push direct sur `main`. PR avec description. `main` local a jour apres merge. Branche feature nettoye. Protection refuse un geste : c'est voulu, passe par la PR. Conflit : tire `main` dans ta feature, resols, pousse. Mauvais remote : `git remote -v`. Status sale : range avant de continuer. Tu n'es pas en retard. Tu es en train d'apprendre le vrai rythme.

Si la protection n'est pas activee, active-la maintenant (chapitre 7) et recommence l'etape push sur `main` : le refus du serveur ancre mieux qu'un paragraphe. Si tu n'as pas d'ami reviewer, ecris la revue dans `NOTES-REVIEW.md` comme a un collegue, puis Approuve. L'exercice du regard reste valable.

## Erreur classique

Sauter la description de PR. Ou merger sans regarder le diff "parce que c'est toi". Autre piege : laisser la branche locale pourrir apres merge. Autre piege : ouvrir la PR vers la mauvaise base. Verifie `base: main` avant de crier victoire. Autre piege : un seul commit "tout" alors que l'atelier demande au moins deux intentions separees.

:::attention
Merger sans regarder le diff "parce que c'est toi", c'est un Approve fantome deguise. Lis quand meme.
:::

## En vrai

Note en trois lignes ce qui t'a freine. Garde la note. Le prochain atelier ira plus vite. Si rien ne t'a freine, note ce qui t'a surpris positivement. Les deux comptent. Relis ta note avant l'atelier revue : tu sauras ou tu tends a raccourcir.

## A toi

Fais l'atelier maintenant. Coche les 9 etapes. Ecris le livrable : captures ou notes + trois freins. Range-le dans un dossier "ateliers-git". Dans une semaine, refais juste les etapes 5 a 9 sur une autre micro-feature. Le reflexe s'ancre. Bonus : ajoute dans le README du depot de test la recette en huit lignes du chapitre 2, puis verifie que ton atelier l'a suivie.
