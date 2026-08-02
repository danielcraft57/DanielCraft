# Chapitre 11 - Bisect : trouver le commit qui a casse

Il y a deux semaines, le formulaire marchait. Aujourd'hui, non. Entre les deux, vingt commits. Personne ne sait lequel a casse. Lire chaque diff a la main est long. `git bisect` fait une recherche par dichotomie : il te fait tester le milieu, puis la moitie restante, jusqu'au premier commit coupable. Chez DanielCraft, **bisect** est le detecteur gentil de l'historique : pas pour blamer une personne, pour trouver un changement.

Tu dis a Git : "la, c'etait bon" (un vieux commit). "la, c'est mauvais" (souvent HEAD). Git te pose au milieu. Tu testes. Tu dis bon ou mauvais. Git reduit. En quelques etapes, tu as le commit qui a introduit le bug. L'outil te guide. Toi, tu restes calme et methodique.

:::retenir
Bisect trouve un changement. Il ne juge pas un collegue. On corrige, on ajoute un test si possible, on avance.
:::

## Le deroulement

```bash
git bisect start
git bisect bad
git bisect good v1.1.0
```

Ici, tu marques la version taguee `v1.1.0` comme bonne, et l'etat actuel comme mauvais. Git checkout un commit du milieu. Tu testes le site (formulaire, page, test auto...).

Si c'est encore casse :

```bash
git bisect bad
```

Si ca marche :

```bash
git bisect good
```

Tu repetes. A la fin, Git affiche le premier commit mauvais. Tu lis le diff :

```bash
git show
```

Puis tu sors du mode bisect :

```bash
git bisect reset
```

Tu reviens ou tu etais. Ensuite tu corriges (souvent une nouvelle branche fix depuis `main`).

## Automatiser un peu

Si tu as un test qui echoue de facon fiable, tu peux laisser Git lancer le test a ta place (`git bisect run ...`). Utile, un cran plus avance. Pour commencer, le mode manuel suffit : tu ouvres le navigateur, tu cliques, tu dis bon/mauvais. Lea prefere le manuel au debut : elle voit le site, elle comprend. Max automatise des qu'il a un test solide.

## Bien choisir good et bad

Il te faut un point vraiment bon. Un **tag** de release aide. Ou un commit que tu te souviens avoir teste. Si ton "good" n'est pas vraiment bon, bisect te menera nulle part utile.

Bad = l'etat casse. Good = l'etat sain. Ne les inverse pas : tu obtiendrais le message inverse de la realite. Note ta procedure de test sur un papier (trois clics). Reproduis toujours pareil. Si tu changes de methode au milieu, tu pollues la recherche.

:::attention
Oublier `git bisect reset` laisse le depot dans un etat etrange. Des que tu as le coupable, reset, puis branche fix.
:::

Mardi, le bouton Envoyer ne fait plus rien. Vendredi dernier, demo client OK. Entre les deux, dix-huit commits. Sam lance bisect avec le tag `v0.2.0` comme good. Huit tests manuels plus tard, Git pointe un commit "ajoute tracker clic" qui avait casse le handler. Pas de chasse aux sorcieres : un revert cible ou un fix, plus un test. L'apres-midi est sauvee.

Ferme les caches navigateur si besoin. Tu testes le code d'un commit ancien : normal que le site ait l'air "en retard". Tu n'enquetes pas sur le design. Tu enquetes sur le bug.

## Ce que bisect n'est pas

Ce n'est pas une excuse pour humilier l'auteur du commit. Le commit "coupable" est une info technique. Peut-etre que le bug dependait d'un environnement. Peut-etre que le test manquait. On corrige. On ajoute un test si possible. On avance. Ce n'est pas non plus magique si le bug est **flaky** (parfois oui, parfois non) : bisect souffre. Si le bug vient d'une donnee externe, pas du code, bisect ne peut pas inventer la cause. Si plusieurs commits combines causent le probleme, tu trouveras souvent le premier qui fait basculer le test : lis le contexte autour.

## Petite histoire

Lea cherchait au hasard pendant une heure. Sam a dit : "tu as un tag bon ?" Oui, `v0.2.0`. Bisect. Huit etapes. Commit trouve. Max a ajoute un test pour que la CI attrape ca la prochaine fois. Trois roles, une meme lecon : methode avant panique.

Chez DanielCraft, on affiche parfois la phrase au-dessus de l'ecran : "Avant de chercher au hasard, tente bisect."

## Erreur classique

Oublier `git bisect reset` et rester dans un etat etrange. Ou marquer bad/good a l'envers. Ou chercher au hasard pendant une heure alors qu'un tag `v1.1.0` "bon" etait sous la main. Autre piege : changer la procedure de test au milieu de la recherche.

:::astuce
Note trois clics de test sur un papier avant de lancer bisect. Reproduis toujours la meme procedure.
:::

## En vrai

Dans un depot de test, introduis volontairement un bug a un commit (par exemple une fonction `addition(a, b)` qui retourne `a - b`), puis ajoute d'autres commits innocents. Lance bisect depuis un bon tag jusqu'a HEAD. Verifie que Git trouve le commit faute. C'est le meilleur tutoriel.

Apres avoir trouve : `git bisect reset`, puis branche fix depuis `main`, correctif, test, PR. Eventuellement ajoute un test automatique pour que la CI attrape ca la prochaine fois. Bisect t'a montre le ou ; la CI evite d'y retourner.

## A toi

Ajoute dans tes notes : "Avant de chercher au hasard pendant une heure, je tente bisect si j'ai un point good." Le reflexe compte plus que la syntaxe parfaite.
