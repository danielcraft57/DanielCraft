# Chapitre 8 - CI legere : des tests automatiques sur la PR

La revue humaine regarde le sens. La CI regarde la mecanique : est-ce que ca build ? Est-ce que les tests passent ? Est-ce que le linter crie ? Tu n'as pas besoin d'une usine NASA. Tu as besoin d'un feu vert / feu rouge simple sur chaque pull request.

CI veut dire Continuous Integration : a chaque proposition de changement, une machine rejoue des verifications.

## L'idee sans jargon

Lea ouvre une PR. GitHub Actions (ou GitLab CI, ou autre) lance un petit script : installer, tester, parfois builder. Au bout de deux minutes, un point vert ou rouge apparait sur la PR. Max voit le rouge avant de merger. Lea corrige. On gagne une categorie entiere de "ouille, j'avais oublie".

Chez DanielCraft, on aime la CI qui tient sur une page de config et qui finit vite. Si la CI met 40 minutes, les gens la contournent mentalement.

## Un exemple mental : site statique + tests JS

Imagine le site de Lea, Max et Sam. Ils ont quelques tests automatiques sur des fonctions de validation (email, telephone). Sur chaque PR, la CI fait :

```text
1. Recuperer le code de la PR
2. Installer les dependances
3. Lancer les tests
4. Afficher succes ou echec
```

Pas besoin de deployer en production depuis la CI le premier jour. Juste verifier.

## A quoi ca ressemble (idee)

Sur GitHub Actions, un fichier dans `.github/workflows/ci.yml` decrit le travail. L'idee generale, pas un tutoriel exhaustif :

```text
on: pull_request
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - recuperer le code
      - installer Node (ou Python, etc.)
      - npm test (ou pytest, etc.)
```

Tu adapteras a ton stack. L'important est le reflexe : PR = verification automatique.

## Faire de la CI un filet, pas une humiliation

Quand c'est rouge, le message doit aider. "3 tests failed" avec le nom du test bat "Error". L'auteur corrige sans honte. La CI n'est pas la, pour punir. Elle est la pour attraper tot.

Si la CI est flaky (rouge au hasard), corrige-la vite. Une CI menteuse est pire que pas de CI : on ignore le rouge.

## Lien avec les branches protegees

Tu peux exiger que le check `test` soit vert avant merge. Alors plus personne ne merge "on verra bien". Le bouton Merge attend le vert.

## Que mettre dans une CI legere ?

Pour commencer : installer + tests unitaires rapides. Ensuite eventuellement lint. Ensuite eventuellement un build. Evite d'ajouter dix outils le meme jour. Chaque outil doit gagner sa place.

Si vous n'avez aucun test encore, une CI qui lance au moins un script `npm test` (meme minimal) cree le rituel. Puis vous ajoutez de vrais tests au fil des bugs.

## Secrets dans la CI

Parfois la CI a besoin d'un token. Stocke-le dans les secrets du depot (reglages GitHub), pas dans le fichier yaml. Le chapitre 18 insiste : les cles ne vivent pas dans Git.

## Erreur classique

Copier une mega config internet avec cache, matrix, deploy, notifications Slack, et ne plus comprendre pourquoi c'est rouge. Ou bloquer le merge sur un check optionnel qui casse souvent. Ou n'avoir de CI que sur `main` apres merge : trop tard, le mal est deja integre.

## En vrai

Ajoute un test minuscule qui echoue si une fonction `validerEmail` accepte `"a@b"`. Ouvre une PR qui casse volontairement. Regarde le rouge. Corrige. Regarde le vert. Ce petit theatre ancre le geste.


## Ce que la CI ne remplace pas

Elle ne remplace pas la revue humaine sur le sens produit. Elle ne garantit pas qu'un bouton est joli. Elle ne comprend pas qu'un texte client est faux. Elle attrape les regressions mecaniques. Garde les deux filets.

## Faire grandir la CI sans l'exploser

Semaine 1 : tests unitaires. Semaine 3 : lint. Plus tard : build de preview. Chaque ajout doit reduire une douleur reelle. Si personne ne regarde un check, retire-le ou repare-le.

## Echec utile vs echec bruyant

Utile : "test validerEmail refuse a@b". Bruyant : stack trace de 200 lignes sans nom de test. Investis cinq minutes pour rendre le rouge lisible. Toute l'equipe gagne a chaque PR.

## Qui possede la CI ?

Tout le monde. Si c'est "le truc de Sam", Sam en vacances = CI rouge ignoree. Documente en cinq lignes comment relancer et ou est le fichier de config.


## A toi

Ecris la promesse de votre CI en une phrase dans le README : "Chaque PR lance les tests ; on ne merge pas au rouge." Si vous n'avez pas encore de CI, ecris la phrase et mets la mise en place dans le mini-projet (chapitre 12) ou juste apres.
