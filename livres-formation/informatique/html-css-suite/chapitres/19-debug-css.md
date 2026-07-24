# Chapitre 19 - Debug CSS : outils, outline, hypotheses

Ca ne s'affiche pas comme tu veux. Normal. Le debug CSS est un metier de detective : hypothese, test, observation. Pas de panique aleatoire ni de `!important` en rafale.

Chez DanielCraft, on debug comme on range un atelier : une cause a la fois, de la lumiere partout.

## L'inspecteur, ton meilleur ami

F12 (ou clic droit → Inspecter). Selectionne l'element. Onglet Styles : regles actives, regles barrees. Onglet Calcule / Computed : valeur finale. Boite (margin/padding) visualisee.

Si une couleur "ne change pas", regarde qui gagne (specificite, ordre, inline). Tu as le chapitre cascade pour ca : l'inspecteur le montre en vrai.

## Outline sur tout (temporaire)

Quand tu ne vois plus qui est qui :

```css
* {
  outline: 1px solid tomato;
}
```

Ou plus cible :

```css
.layout > * {
  outline: 2px dashed #1a5f4a;
}
```

Tu vois les boites. Tu vois les debordements. Tu enleves ensuite. C'est un projecteur, pas une deco.

Certains navigateurs ont aussi un mode "montrer les grilles Flex/Grid" dans l'inspecteur : active-le sur le conteneur.

## Hypothese claire

Avant de taper dix changements, ecris (meme mentalement) :

"Je pense que la carte debord parce que l'image n'a pas `max-width: 100%`."

Puis teste uniquement ca. Si faux, nouvelle hypothese : "le parent n'a pas de largeur bornee" / "un padding s'ajoute a une width 100%" / etc.

Changer cinq trucs a la fois, c'est tirer a l'aveugle.

## Pieges frequents (checklist)

`max-width` manquant sur image ou iframe.

Parent en Grid/Flex mais enfant avec largeur fixe trop grande.

`overflow` cache quelque chose d'important (focus, ombre, menu).

Mauvaise `grid-area` (typo dans le nom).

Media query jamais atteinte (breakpoint trop bas/haut, ou faute de syntaxe).

Classe mal orthographiee dans le HTML (`.carte` vs `cart`).

Fichier CSS non lie, ou mauvais chemin, ou ancien cache (rechargement force).

## Box model et width

```css
* {
  box-sizing: border-box;
}
```

Souvent en debut de feuille. Sinon `width: 100%` + padding peut faire deborder. Si un element "depasse un peu", verifie le box-sizing.

## Debug Grid

Colorie les zones. Verifie que chaque ligne de `grid-template-areas` a le meme nombre de cellules. Verifie les noms `grid-area`. Regarde si un enfant sans area se place dans la premiere case libre et pousse le reste.

## Debug Flex

`flex-wrap` oublie sur un menu qui debord. `min-width: auto` sur un enfant qui refuse de retrecir (parfois `min-width: 0` sur un enfant Flex/Grid aide dans des cas de texte long). Commence simple avant ce cas avance.

## Debug focus / a11y

Si le focus "disparait", cherche `outline: none` ou un overflow qui coupe. Tab en regardant l'inspecteur (element `:focus`).

## Methode en 5 minutes

1. Reproduire le bug (largeur precise).
2. Inspecter l'element fautif.
3. Lire la propriete concernee (qui gagne ?).
4. Poser une hypothese unique.
5. Tester. Si ok, nettoyer les outlines et commentaires de debug.

## Erreur classique

Ajouter des marges negatives au hasard pour "ramener" un bloc. Ca masque le vrai probleme. Ou creer une classe `.fix` avec `!important` sur tout. Ou modifier le HTML structure pour compenser un CSS confus sans comprendre.

## En vrai

Casse volontairement une page qui marche : retire `max-width` sur une image, faute une `grid-area`, baisse un breakpoint. Puis debug avec la methode. Remets propre. Tu entraines le reflexe.

Fais la meme chose sur un conflit de couleur (classe vs type). Regarde la regle barree.

## A toi

Prends un bug reel sur ton mini-projet (meme petit). Ecris l'hypothese en une phrase. Corrige. Ajoute en commentaire CSS une ligne `/* fix: image max-width - debord mobile */` le temps de t'en souvenir, puis efface le commentaire si trop bruyant. Le muscle, c'est l'hypothese, pas le commentaire.
