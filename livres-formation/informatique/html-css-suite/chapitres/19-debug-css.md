# Chapitre 19 - Debug CSS : outils, outline, hypotheses

Ca ne s'affiche pas comme tu veux. Normal. Le debug CSS est un metier de detective : hypothese, test, observation. Pas de panique aleatoire ni de `!important` en rafale.

Chez DanielCraft, on debug comme on range un atelier : une cause a la fois, de la lumiere partout. Lea ouvre l'inspecteur avant de reecrire un composant. Max appelle son neveu quand ca "debord" - et le neveu, s'il a lu ce chapitre, demande d'abord quelle hypothese. Sam note au tableau : "une cause, un test". Les eleves qui suivent ca avancent deux fois plus vite.

## Ce que ce n'est pas

Ce n'est pas ajouter des marges negatives au hasard pour "ramener" un bloc. Ce n'est pas creer une classe `.fix` avec `!important` sur tout. Ce n'est pas modifier le HTML structure pour compenser un CSS confus sans comprendre. Et ce n'est pas changer cinq proprietes d'un coup en esperant que ca se remette. Le tire a l'aveugle fatigue plus que la methode.

## Methode en cinq gestes

Tu reproduis le bug a une largeur precise. Tu inspectes l'element. Tu lis qui gagne sur la propriete concernee. Tu poses une hypothese unique a voix haute : "je pense que la carte debord parce que l'image n'a pas `max-width: 100%`". Tu testes uniquement ca. Si faux, nouvelle hypothese. Si vrai, tu nettoies les outlines de debug et tu continues. Le muscle, c'est l'hypothese, pas le genie nocturne.

Sam force ses eleves a dire la phrase avant de toucher le CSS. Si tu ne peux pas finir la phrase, tu n'as pas encore d'hypothese - tu as de la panique. Lea le fait seule devant l'inspecteur. Max l'a appris apres une heure de marges negatives. Cinq minutes de methode battent quarante minutes de tire a l'aveugle.

:::retenir
Reproduire, inspecter, lire qui gagne, une hypothese a voix haute, un seul test. Le muscle, c'est l'hypothese unique.
:::

## L'inspecteur et l'outline

F12 (ou clic droit, Inspecter). Onglet Styles : regles actives, regles barrees. Onglet Calcule / Computed : valeur finale. Boite (margin/padding) visualisee. Si une couleur "ne change pas", regarde qui gagne (specificite, ordre, inline). Le chapitre cascade t'a prepare : l'inspecteur le montre en vrai.

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

Tu vois les boites. Tu vois les debordements. Tu enleves ensuite. C'est un projecteur, pas une deco. Active aussi le mode "montrer les grilles Flex/Grid" de l'inspecteur sur le conteneur.

:::astuce
Outline temporaire sur `.layout > *` pendant cinq minutes. Tu vois les boites. Tu enleves apres. Projecteur, pas deco.
:::

## Checklist des pieges frequents

`max-width` manquant sur image ou iframe. Parent en Grid/Flex mais enfant avec largeur fixe trop grande. `overflow` qui cache focus, ombre ou menu. Mauvaise `grid-area` (typo dans le nom). Media query jamais atteinte (breakpoint ou syntaxe). Classe mal orthographiee dans le HTML (`.carte` vs `cart`). Fichier CSS non lie, mauvais chemin, ou ancien cache (rechargement force).

```css
* {
  box-sizing: border-box;
}
```

Souvent en debut de feuille. Sinon `width: 100%` + padding peut faire deborder. Debug Grid : colorie les zones, verifie que chaque ligne de `grid-template-areas` a le meme nombre de cellules, regarde si un enfant sans area se place dans la premiere case libre. Debug Flex : `flex-wrap` oublie, parfois `min-width: 0` sur un enfant qui refuse de retrecir. Debug focus : cherche `outline: none` ou un overflow qui coupe, Tab en regardant `:focus`.

## Petite histoire

Lea a perdu quarante minutes sur un menu qui "mangeait" le focus : un `overflow: hidden` sur le header. Outline partout, hypothese, correctif, cinq minutes. Max avait un bouton qui sortait de l'ecran : image sans `max-width`. Sam a casse volontairement une page en cours (faute de `grid-area`) et a chronometre le debug methodique versus le debug panique. Methode : gagnante, sans drama.

:::attention
Corriger le symptome (marge negative, taille magique) au lieu de la cause. Empiler les `!important` jusqu'a ne plus savoir qui commande. Quand tu ne sais plus, repars de l'inspecteur et d'une seule propriete.
:::

## Erreur classique

Desactiver le cache mentalement ("ca marche chez moi") sans hard refresh. Changer cinq proprietes d'un coup. Modifier le HTML structure pour compenser un CSS confus sans comprendre.

## En vrai

Casse volontairement une page qui marche : retire `max-width` sur une image, faute une `grid-area`, baisse un breakpoint. Puis debug avec la methode en cinq minutes : reproduire, inspecter, lire qui gagne, hypothese unique, tester. Remets propre. Fais la meme chose sur un conflit de couleur. Tu entraines le reflexe.

## A toi

Prends un bug reel sur ton mini-projet (meme petit). Ecris l'hypothese en une phrase. Corrige. Ajoute en commentaire CSS une ligne `/* fix: image max-width - debord mobile */` le temps de t'en souvenir, puis efface le commentaire si trop bruyant. Garde surtout la phrase d'hypothese dans ton carnet. C'est ca, le vrai outil.
