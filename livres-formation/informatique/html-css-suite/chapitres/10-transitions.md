# Chapitre 10 - Transitions legeres : du mouvement utile

Un bouton qui change de couleur d'un coup, c'est correct. Un bouton qui glisse doucement vers sa nouvelle couleur, c'est plus agreable. Les transitions CSS font ca : interpoler entre deux etats.

On reste leger. Pas de cirque. Pas de page qui rebondit partout. Chez DanielCraft, le mouvement sert la clarte : "tu survoles, ca reagit". Rien de plus.

## L'idee de base

Tu as un etat normal et un etat `:hover` (ou `:focus-visible`). Tu dis au navigateur : "quand ca change, prends 200ms".

```css
.bouton {
  background: var(--couleur-principale);
  color: #fff;
  transition: background-color 200ms ease, transform 200ms ease;
}

.bouton:hover {
  background: #144a3a;
  transform: translateY(-1px);
}
```

Important : la propriete `transition` se place en general sur l'etat de base (`.bouton`), pas seulement dans `:hover`. Ainsi l'aller et le retour sont doux.

## Que transitionner ?

De bons candidats : `color`, `background-color`, `opacity`, `transform`, `box-shadow` leger, `border-color`.

Des candidats plus risques : `width`, `height`, `top`, `left` (souvent moins fluides / plus coutueux). Preferer `transform` et `opacity` quand tu peux.

```css
.carte {
  transition: box-shadow 200ms ease, transform 200ms ease;
}

.carte:hover {
  transform: translateY(-2px);
  box-shadow: var(--ombre-hover, 0 8px 20px rgba(0, 0, 0, 0.12));
}
```

Sur une grille de produits, un leger lift au survol guide l'oeil sans hurler.

## Durees raisonnables

150ms a 300ms pour de l'UI. Au-dela, ca trainasse. En dessous de 100ms, on ne sent presque rien.

`ease`, `ease-out` : naturels pour des hovers. Evite `linear` sur un bouton (souvent mecanique).

## Liens et focus

```css
a {
  color: var(--couleur-principale);
  transition: color 150ms ease;
}

a:hover {
  color: #0f3d30;
}

a:focus-visible {
  outline: 2px solid var(--couleur-principale);
  outline-offset: 2px;
}
```

La transition sur la couleur, oui. Mais le focus doit rester net : un outline clair, pas uniquement un fondu invisible.

## Plusieurs proprietes

Tu peux lister plusieurs transitions, ou utiliser `transition: all 200ms ease` avec prudence. `all` est pratique en proto, un peu large en production : tu risques de transitionner des choses non voulues. Preferer la liste explicite quand tu peaufines.

## Respecter ceux qui veulent moins de mouvement

Certains reglent leur systeme pour reduire les animations.

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    transition-duration: 0.01ms !important;
    animation-duration: 0.01ms !important;
  }
}
```

Version simple et efficace pour un petit site. Le site reste utilisable, sans imposer de mouvement.

## Ce qu'on ne fait pas ici

Pas de carousel auto agressif. Pas de titre qui rebondit en boucle. Pas d'animation permanente qui distrait la lecture d'un article. Les vrais `@keyframes` complexes, ce n'est pas le coeur de ce livre : une transition hover bien faite vaut mieux.

## Erreur classique

Mettre `transition` seulement dans `:hover` : l'aller est doux, le retour est sec. Ou transitionner pendant 2 secondes : l'utilisateur a deja clique ailleurs.

Autre piege : `transform` sur un element qui casse un layout (ok en general) combine a des marges animees (moins ok). Garde simple.

## En vrai

Sur une landing, ajoute une transition a : le bouton principal, les cartes, les liens du menu (couleur). Rien d'autre. Navigue a la souris, puis au clavier. Si ca semble calme et net, c'est gagne.

Enleve ensuite toutes les transitions et remets-les une par une. Tu sentiras celles qui apportent vraiment.

## A toi

Page produit avec une carte et un bouton. Transitions 200ms sur carte (ombre + leger translate) et bouton (fond). Ajoute le media `prefers-reduced-motion`. Verifie hover et focus-visible.
