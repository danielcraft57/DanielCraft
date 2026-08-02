# Chapitre 8 - CI legere : des tests automatiques sur la PR

La revue humaine regarde le sens. La **CI** regarde la mecanique : est-ce que ca build ? Est-ce que les tests passent ? Est-ce que le linter crie ? Tu n'as pas besoin d'une usine NASA. Tu as besoin d'un feu vert / feu rouge simple sur chaque pull request. CI veut dire Continuous Integration : a chaque proposition de changement, une machine rejoue des verifications. Chez DanielCraft, on aime la CI qui tient sur une page de config et qui finit vite. Si la CI met quarante minutes, les gens la contournent mentalement.

Lea ouvre une PR. GitHub Actions (ou GitLab CI, ou autre) lance un petit script : installer, tester, parfois builder. Au bout de deux minutes, un point vert ou rouge apparait sur la PR. Max voit le rouge avant de merger. Lea corrige. On gagne une categorie entiere de "ouille, j'avais oublie". Imagine le site de Lea, Max et Sam. Ils ont quelques **tests** automatiques sur des fonctions de validation (email, telephone). Sur chaque PR, la CI fait : recuperer le code de la PR, installer les dependances, lancer les tests, afficher succes ou echec. Pas besoin de deployer en production depuis la CI le premier jour. Juste verifier.

:::retenir
Une CI legere et lisible bat une mega config que personne ne comprend. Vert ou rouge, vite, clair.
:::

## L'idee sans jargon

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

Tu adapteras a ton stack. L'important est le reflexe : PR egal verification automatique. Quand c'est rouge, le message doit aider. "3 tests failed" avec le nom du test bat "Error". L'auteur corrige sans honte. La CI n'est pas la pour punir. Elle est la pour attraper tot. Si la CI est **flaky** (rouge au hasard), corrige-la vite. Une CI menteuse est pire que pas de CI : on ignore le rouge.

:::attention
Une CI flaky (rouge au hasard) est pire que pas de CI : l'equipe apprend a ignorer le rouge. Repare-la ou retire le check.
:::

Tu peux exiger que le check `test` soit vert avant merge. Alors plus personne ne merge "on verra bien". Le bouton Merge attend le vert. Pour commencer : installer plus tests unitaires rapides. Ensuite eventuellement lint. Ensuite eventuellement un build. Evite d'ajouter dix outils le meme jour. Chaque outil doit gagner sa place. Si vous n'avez aucun test encore, une CI qui lance au moins un script `npm test` (meme minimal) cree le rituel. Puis vous ajoutez de vrais tests au fil des bugs. La CI ne remplace pas la revue humaine sur le sens produit. Elle ne garantit pas qu'un bouton est joli. Elle attrape les regressions mecaniques. Garde les deux filets.

Parfois la CI a besoin d'un token. Stocke-le dans les **secrets** du depot (reglages GitHub), pas dans le fichier yaml. Le chapitre 18 insiste : les cles ne vivent pas dans Git. Semaine 1 : tests unitaires. Semaine 3 : lint. Plus tard : build de preview. Chaque ajout doit reduire une douleur reelle. Si personne ne regarde un check, retire-le ou repare-le. Tout le monde possede la CI. Si c'est "le truc de Sam", Sam en vacances egal CI rouge ignoree.

## Petite histoire

Max a copie une mega config internet avec cache, matrix, deploy, notifications Slack. Personne ne comprenait pourquoi c'etait rouge. L'equipe a tout retire et remis un seul job `npm test`. Deux minutes, vert ou rouge lisible. Moral remonte. Investis cinq minutes pour rendre le rouge lisible. Toute l'equipe gagne a chaque PR.

Lea a casse volontairement un test sur une PR de demo. Elle a vu le rouge. Elle a corrige. Elle a vu le vert. Ce petit theatre a ancre le geste mieux qu'un powerpoint. Chez DanielCraft, on adore ce theatre.

## Erreur classique

Copier une mega config internet et ne plus comprendre pourquoi c'est rouge. Ou bloquer le merge sur un check optionnel qui casse souvent. Ou n'avoir de CI que sur `main` apres merge : trop tard, le mal est deja integre. Ou croire que la CI remplace toute review humaine.

:::astuce
Commence par un seul job rapide sur `pull_request`. Ajoute lint et build seulement quand ils gagnent une vraie douleur.
:::

## En vrai

Ajoute un test minuscule qui echoue si une fonction `validerEmail` accepte `"a@b"`. Ouvre une PR qui casse volontairement. Regarde le rouge. Corrige. Regarde le vert. Ce petit theatre ancre le geste. Si tu n'as pas encore GitHub Actions, ecris d'abord la phrase README : le rituel commence par l'intention ecrite.

## A toi

Ecris la promesse de votre CI en une phrase dans le README : "Chaque PR lance les tests ; on ne merge pas au rouge." Si vous n'avez pas encore de CI, ecris la phrase et mets la mise en place dans le mini-projet (chapitre 12) ou juste apres. Bonus : chronometre un run vert. S'il depasse cinq minutes sans raison, simplifie.

## Zoom : vert lisible, rouge utile

Une CI qui dit "Error" sans nom de test, c'est un feu rouge opaque. Investis cinq minutes pour rendre le message lisible. Lea l'a fait apres une apres-midi perdue. Max aussi. Sam refuse les configs copiees sans lecture. Chez DanielCraft, la CI legere et lisible bat la mega usine ignoree.
