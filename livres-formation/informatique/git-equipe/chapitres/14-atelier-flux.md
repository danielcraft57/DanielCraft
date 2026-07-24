# Chapitre 14 - Atelier : flux d'equipe

Cet atelier fait vivre le chapitre 2 avec les mains. Tu joues deux roles : Alex (feature) et Blake (reviewer). Un seul ordinateur suffit.

## But

Partir de `main` a jour, creer une branche, pousser, ouvrir une PR, faire merger, revenir sur `main` proprement. Chronometre : 45 a 90 minutes.

## Materiel

Un depot GitHub de test. Git configure. Navigateur. Une page `index.html` deja sur `main` (meme minimale).

## Etapes

1. Clone le depot (ou ouvre-le) et place-toi sur `main`.

```bash
git switch main
git pull
```

2. Cree la branche `feature/bandeau-accueil` et ajoute un bandeau texte dans `index.html` ("Bienvenue chez nous").

```bash
git switch -c feature/bandeau-accueil
```

3. Fais au moins deux commits : un pour le HTML, un pour un peu de CSS si tu veux. Messages clairs.

4. Pousse la branche (pas `main`).

```bash
git push -u origin feature/bandeau-accueil
```

5. Ouvre une pull request vers `main`. Titre clair. Description avec but et "comment tester" (ouvrir l'accueil, voir le bandeau).

6. En mode Blake, relis le diff. Laisse un commentaire bienveillant (meme mineur). Approuve.

7. Merge la PR (bouton GitHub). Coche la suppression de branche distante si proposee.

8. En local, reviens sur `main`, tire, supprime la branche locale.

```bash
git switch main
git pull
git branch -d feature/bandeau-accueil
```

9. Verifie que `git status` est propre et que `git log --oneline -5` montre le merge (ou le squash) attendu.

## Variante a deux personnes

Alex fait 1-5. Blake fait 6-7. Alex fait 8-9. Parlez dans un canal : "PR prete", "review ok", "c'est merge".

## Criteres de reussite

Aucun push direct sur `main`. La PR a une description. `main` local est a jour apres merge. La branche feature est nettoye.

## Si ca bloque

Protection de branche refuse un geste : c'est voulu, passe par la PR. Conflit : tire `main` dans ta feature, resols, pousse. Mauvais remote : verifie `git remote -v`.

## Apres l'atelier

Note en trois lignes ce qui t'a freine. Garde la note. Le prochain atelier ira plus vite.
