# Chapitre 10 - Transitions legeres : du mouvement utile

Un bouton qui change de couleur d'un coup, c'est correct. Un bouton qui glisse doucement vers sa nouvelle couleur, c'est plus agreable. Les transitions CSS font ca : interpoler entre deux etats quand une propriete change. Tu survoles, le navigateur anime. Tu quittes, il revient. Rien de magique. Juste une consigne de duree et de courbe.

Chez DanielCraft, le mouvement sert la clarte. "Tu survoles, ca reagit." Pas "la page rebondit partout". Lea, freelance web, ajoute 200ms sur ses CTA et ses cartes produit : le client sent que le site est soigne. Max, artisan, veut juste que son bouton devis ne sursaute pas. Sam, enseignant, montre a ses eleves qu'un hover calme vaut mieux qu'un carousel agressif. Trois usages, meme regle : leger, utile, respectueux.

## Ce que ce n'est pas

Ce n'est pas une animation permanente. Ce n'est pas un titre qui danse en boucle. Ce n'est pas un pretexte pour `transition: all 2s` sur tout le document. Et ce n'est surtout pas une excuse pour cacher un focus clavier derriere un fondu invisible. La transition embellit un etat clair. Elle ne remplace pas un etat clair.

## Etat de base, puis hover

Tu as un etat normal et un etat `:hover` (ou `:focus-visible`). Tu dis au navigateur : "quand ca change, prends 200ms". La propriete `transition` se place en general sur l'etat de base, pas seulement dans `:hover`. Ainsi l'aller et le retour sont doux. Sans ca, l'aller est fluide et le retour est sec - comme une porte qui s'ouvre lentement et claque au retour.

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

:::astuce
Place `transition` sur `.bouton`, pas seulement dans `:hover`. Tu evites le retour sec et tu gardes un aller-retour coherent.
:::

## Que transitionner ?

De bons candidats : `color`, `background-color`, `opacity`, `transform`, `box-shadow` leger, `border-color`. Des candidats plus risques : `width`, `height`, `top`, `left` - souvent moins fluides, plus coutueux pour le navigateur. Preferer `transform` et `opacity` quand tu peux.

```css
.carte {
  transition: box-shadow 200ms ease, transform 200ms ease;
}

.carte:hover {
  transform: translateY(-2px);
  box-shadow: var(--ombre-hover, 0 8px 20px rgba(0, 0, 0, 0.12));
}
```

Sur une grille de produits, un leger lift au survol guide l'oeil sans hurler. Lea l'utilise sur ses cartes boutique. Max s'en passe parfois : un site artisan peut rester tres calme et quand meme clair.

## Durees et courbes

150ms a 300ms pour de l'UI. Au-dela, ca trainasse. En dessous de 100ms, on ne sent presque rien. `ease` et `ease-out` sont naturels pour des hovers. Evite `linear` sur un bouton : ca sonne mecanique. Tu peux lister plusieurs proprietes, ou utiliser `transition: all 200ms ease` avec prudence en proto. En peaufinage, prefere la liste explicite : tu evites de transitionner des choses non voulues.

## Liens, focus, et accessibilite du mouvement

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

La transition sur la couleur, oui. Le focus doit rester net : un outline clair, pas uniquement un fondu. Certains reglent leur systeme pour reduire les animations. Respecte-les.

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

Version simple et efficace pour un petit site. Sam l'ajoute systematiquement dans ses demos : le site reste utilisable, sans imposer de mouvement.

:::retenir
Transitions courtes (150-300ms) sur l'etat de base. Hover doux. Focus net. `prefers-reduced-motion` respecte. Calme et net gagne.
:::

## Petite histoire

Lea avait mis des transitions de 800ms partout "pour faire pro". Les clients cliquaient avant la fin du fondu. Elle est redescendue a 200ms, a limite aux boutons et cartes, et a ajoute `prefers-reduced-motion`. Le site a soudain paru plus serieux, pas moins. Max, lui, n'avait aucune transition. Son neveu a ajoute un hover sur le bouton devis. Max a garde ca - et rien d'autre. Suffisant.

## Erreur classique

Mettre `transition` seulement dans `:hover` : l'aller est doux, le retour est sec. Ou transitionner pendant 2 secondes. Ou animer `width`/`height` alors qu'un `transform` suffisait. Ou croire que "plus ca bouge, plus c'est moderne". Non.

## En vrai

Sur une landing, ajoute une transition a : le bouton principal, les cartes, les liens du menu (couleur). Rien d'autre. Navigue a la souris, puis au clavier. Enleve ensuite toutes les transitions et remets-les une par une. Tu sentiras celles qui apportent vraiment. Si ca semble calme et net, c'est gagne.

## A toi

Page produit avec une carte et un bouton. Transitions 200ms sur carte (ombre + leger translate) et bouton (fond). Ajoute le media `prefers-reduced-motion`. Verifie hover et focus-visible. Note en une phrase ce que tu as refuse d'animer - ce refus compte autant que ce que tu as anime.
