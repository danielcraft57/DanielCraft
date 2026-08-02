# Chapitre 8 - Les conflits

Un **conflit**, c'est Git qui ne sait pas choisir. Deux versions du meme endroit. Il te demande d'arbitrer. Ce n'est pas un echec. C'est Git qui dit : "decide, humain". Chez DanielCraft, on provoque un conflit volontairement dans les ateliers, pour enlever la peur. Lea les resolvait deja. Max paniquait. Sam a transforme la panique en methode. Toi, tu vas faire pareil. La premiere fois, les **marqueurs** `<<<<<<<` font peur. La dixieme, tu souffles, tu choisis, tu enleves les marqueurs, tu `add`, tu `commit`. Muscle. Pas magie.

Un conflit arrive quand deux histoires touchent la meme zone du meme fichier. Toi hier et toi aujourd'hui. Toi et Lea. Deux branches. Local et remote. Peu importe. Git ne "plante" pas. Il refuse de mentir en choisissant a ta place. Tu peux reduire la frequence avec de petits commits et des merges frequents. Tu ne peux pas promettre zero conflit a vie. Mieux vaut savoir nager que croire que la mer n'existe pas.

Deux stylos ont ecrit sur la meme ligne. Git pose les deux versions dans le fichier avec des balises. Tu gardes A, ou B, ou un melange intelligent. Tu enleves les balises. Tu dis a Git : "voila la version choisie" (`add` + `commit`). Si tu es perdu au milieu, **`git merge --abort`** te ramene avant le merge. Apprends ce frein d'urgence tot. Max l'appelle "le bouton panique honnete". Sam l'enseigne avant meme de provoquer le conflit.

:::attention
Ne committe jamais un fichier qui contient encore `<<<<<<<`. Git croit que c'est resolu. Ton programme, lui, plantera.
:::

## Ce que ce n'est pas

Un conflit, ce n'est pas "Git est casse". Ce n'est pas non plus "ton projet est perdu". Ce n'est pas automatique d'accepter "incoming" sans lire. Et ce n'est surtout pas une raison de jeter Git. C'est le prix normal de deux personnes (ou deux branches) qui touchent la meme zone. Ce n'est pas non plus une excuse pour laisser les marqueurs dans le code "on verra demain". Demain, le build casse. Aujourd'hui, tu nettoies.

Ce n'est pas non plus "toujours accepter les deux versions". Parfois le melange intelligent est juste. Parfois une seule version est juste. Parfois il faut ecrire une troisieme version a la main. Lis. Comprends. Puis choisis. Lea refuse les boutons "accepter tout" tant qu'elle n'a pas lu le diff.

## Comment ca arrive et a quoi ca ressemble

Sur `main`, tu modifies la ligne 1 de `readme.txt`. Sur une branche, tu modifies aussi la ligne 1. Tu merges : boum, conflit.

Dans le fichier :

```text
<<<<<<< HEAD
version de main
=======
version de la branche
>>>>>>> idee-couleurs
```

Tu gardes ce que tu veux. Tu enleves les marqueurs `<<<<<<<` etc. Completement. Aucun marqueur ne doit rester. Ensuite seulement tu stages et tu conclus.

## Resolving

Ouvre le fichier. Corrige a la main. Fais `git add fichier_corrige.txt`, puis `git commit` pour conclure le merge. Ou, si ton outil propose "accepter actuel / entrant / les deux", OK - mais comprends ce que tu acceptes. Lea refuse les boutons automatiques tant qu'elle n'a pas lu le diff. Max a accepte "les deux" une fois sans lire : le fichier compilait pour Git, pas pour le navigateur. Sam fait relancer le site apres chaque resolution. Le conflit "resolu" doit aussi etre juste pour le produit.

:::astuce
Lea refuse les boutons "accepter tout" tant qu'elle n'a pas lu le diff. Dix secondes de lecture valent une heure de debug.
:::

## Annuler un merge en cours

Si tu es perdu :

```bash
git merge --abort
```

Retour avant le merge. Respire. Recommence plus tard, plus calme. Ce n'est pas un aveu d'echec. C'est de la gestion de risque. Lea abort quand elle est fatiguee. Max abort quand le fichier devient illisible. Sam celebre l'abort autant que la resolution propre. Les deux sont des competences.

## Eviter les conflits (un peu)

Fais des petits commits. Parle-toi en equipe. Merge souvent (pas attendre 3 semaines). Evite que deux personnes editent la meme zone sans coordination. Decoupe les fichiers si possible. Chez DanielCraft, on prefere la prevention polie a l'heroisme du dimanche soir. Lea se repartit les fichiers avec un collegue. Max annonce "je touche au header". Sam impose des zones differentes en binome au debut. Moins de drames. Plus d'apprentissage utile.

## Petite histoire

Max a provoque un conflit volontairement, vu les marqueurs, choisi la version claire, termine le merge. Il a dit : "c'est juste un formulaire a remplir". Sam a note 3 regles perso au tableau pour limiter les conflits. Lea a raconte un conflit client resolu en dix minutes parce que les commits etaient petits. La culture compte autant que la commande. Chez DanielCraft, on veut que tu sortes de ce chapitre avec moins de peur, pas avec zero conflit a vie - promesse impossible.

## Erreur classique

Laisser les marqueurs `<<<<<<<` dans le fichier et committer. Accepter "les deux" sans relire. Abandonner le projet au lieu d'`abort`. Autre piege : resoudre "au feeling" sans lancer le programme / ouvrir la page - un conflit "resolu" peut etre logique pour Git et faux pour le produit. Encore un piege : paniquer et lancer dix commandes d'affilee. Une action. Un status. Ensuite seulement.

## En vrai

Un conflit n'est pas un echec. C'est Git qui dit : "decide humain". Provoque-en un volontairement aujourd'hui, tant que le dossier est un terrain de jeu. Sens les marqueurs. Enleve-les. Termine. Ensuite tu sauras.

## A toi

Provoque un conflit volontairement sur `readme.txt`. Resols-le. Termine le merge. Puis note 3 regles perso pour limiter les conflits dans ton prochain projet. Garde-les a cote de ton `.gitignore` mental. Relis-les avant ta premiere collab reelle.
