# Chapitre 16 - Atelier : conflit en equipe

Les conflits font peur parce qu'ils arrivent souvent le vendredi. Ici, tu vas en creer un expres, le resoudre calmement, et voir que ce n'est qu'un fichier qui demande un choix.

## But

Provoquer un conflit sur le meme fichier, le resoudre, finir sur une `main` propre. Duree : 45 a 75 minutes.

## Scenario

Deux branches touchent le titre de `index.html` (ou le texte du bandeau). Alex change le titre vers "Atelier Git equipe". Blake change le titre vers "Site vitrine DanielCraft". Les deux partent du meme `main`.

## Etapes

1. Sur `main` a jour, note le titre actuel.

```bash
git switch main
git pull
```

2. Branche Alex :

```bash
git switch -c feature/titre-atelier
```

Modifie le titre. Commit. Pousse. Ouvre une PR. Merge-la dans `main` (avec review rapide ou auto-merge sur depot de test).

3. Sans tirer encore, cree la branche Blake depuis l'ancien point... Astuce simple pour solo :

Apres le merge d'Alex, cree la branche Blake depuis un commit ou le titre n'etait pas encore celui d'Alex, OU plus simple pour solo :

```bash
git switch main
git pull
git switch -c feature/titre-vitrine
```

Modifie le meme endroit avec un autre texte. Commit.

4. Ramene `main` dans ta branche Blake :

```bash
git fetch origin
git merge origin/main
```

Le conflit apparait. Ouvre le fichier. Tu vois les marqueurs :

```text
<<<<<<< HEAD
titre de Blake
=======
titre d'Alex (venu de main)
>>>>>>> ...
```

5. Choisis une version, ou combine ("Site vitrine DanielCraft - atelier Git"). Enleve les marqueurs. Sauve.

6. Marque resolu et termine le merge :

```bash
git add index.html
git commit
```

(si Git a ouvert un message de merge, valide-le)

7. Pousse. Ouvre la PR. Explique dans la description : "Resolution de conflit sur le titre, version combinee telle." Review. Merge.

8. Tire `main` localement. Verifie le titre final dans le navigateur.

```bash
git switch main
git pull
```

## Variante rebase

Au lieu de `git merge origin/main`, tente `git rebase origin/main`, resols, `git rebase --continue`, puis `git push --force-with-lease` sur la branche perso. Compare le ressenti avec le merge.

## Criteres de reussite

Aucun marqueur `<<<<<<<` reste dans les fichiers. Le site s'affiche. L'historique montre la resolution. Tu peux expliquer a voix haute ce que tu as choisi et pourquoi.

## Si panique

```bash
git merge --abort
```

ou

```bash
git rebase --abort
```

Puis recommence. Abandonner proprement est une competence.

## Apres l'atelier

Ecris la regle d'equipe : "si on touche aux memes zones, on se parle avant" + "on synchronise main souvent". Le meilleur conflit est celui evite tot. Le deuxieme meilleur est celui resolu sans drama.
