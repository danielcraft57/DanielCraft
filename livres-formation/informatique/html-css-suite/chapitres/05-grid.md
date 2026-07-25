# Chapitre 5 - CSS Grid : lignes et colonnes

Flexbox, tu le connais : super pour une rangee, un menu, aligner dans un sens. **Grid**, c'est autre chose. Tu poses un vrai damier. Lignes et colonnes. Ideal pour une page, une galerie, un tableau de cartes produit. Tu n'abandonnes pas Flexbox. Tu ajoutes un outil. Souvent : Grid pour la structure de page, Flexbox pour les petits alignements a l'interieur d'une cellule.

Chez DanielCraft, Grid, c'est le plan au sol. Flex, c'est ranger les chaises dans une piece. Lea pose d'abord la grille de cartes boutique, ensuite le Flex du footer de carte (prix + bouton). Max voit "rayons dans l'atelier". Sam dessine des colonnes au tableau avant d'ouvrir l'editeur.

## Allumer la grille

```css
.grille {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 1rem;
}
```

`1fr` veut dire "une part de l'espace libre". Trois colonnes egales, avec un espace `gap` entre les cases. Pas besoin de margin bridouilles entre chaque carte.

```html
<div class="grille">
  <article class="carte">Produit A</article>
  <article class="carte">Produit B</article>
  <article class="carte">Produit C</article>
</div>
```

Sur une page boutique, ces trois cartes s'alignent proprement. Ajoute un quatrieme produit : il passe a la ligne suivante, toujours dans la grille. Le **gap** est le petit heros : il espace sans casser les bords externes. Commence par colonnes + `gap`. Les lignes se creent souvent toutes seules. N'empile pas dix placements manuels tant que le flux HTML suffit.

## Colonnes plus expressives

Tu peux melanger unites :

```css
.page {
  display: grid;
  grid-template-columns: 200px 1fr;
  gap: 2rem;
}
```

Colonne fixe a gauche (menu), le reste a droite (contenu). Ou l'inverse pour une landing avec une grosse zone texte et une colonne etroite.

`repeat` evite de se repeter :

```css
.galerie {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}
```

## minmax et auto-fit

Pour une grille de cartes qui s'adapte sans media query compliquee :

```css
.grille {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem;
}
```

L'idee : chaque colonne fait au moins 220px, et on en met autant que ca rentre. Sur telephone, une colonne. Sur grand ecran, plusieurs. Tu peaufineras au chapitre mise en page et au mini-projet. Lea adore `auto-fit` + `minmax` pour les galeries produit : moins de breakpoints, plus de fluidite.

:::astuce
Relie `gap` a une variable `--gap` : tu retouches le rythme de toute la grille en une ligne, et tu peux le reduire sous media query.
:::

## Lignes et hauteur

Souvent, les lignes se creent toutes seules selon le contenu. Tu peux aussi les guider :

```css
.hero-grille {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: auto auto;
  gap: 1.5rem;
}
```

Pour commencer, concentre-toi sur les colonnes et le `gap`. Les lignes suivront.

## Gap, le petit heros

`gap` (et `row-gap` / `column-gap` si besoin) espace les cellules sans casser les bords externes. Sur un blog en grille de billets, c'est net, previsible, facile a retoucher.

```css
:root {
  --gap: 1.25rem;
}

.grille {
  gap: var(--gap);
}
```

## Placement simple

Sans dessiner toute la page, tu peux deja etendre un element :

```css
.carte-large {
  grid-column: 1 / -1;
}
```

Cette carte occupe toute la largeur de la grille (de la premiere a la derniere ligne de colonnes). Utile pour un article epingle au-dessus d'une grille de billets.

```css
.promo {
  grid-column: 2;
  grid-row: 1;
}
```

Reste lisible. N'en abuse pas au debut : une grille bien remplie dans l'ordre du HTML suffit souvent. Sam rappelle : "placement manuel = epice, pas plat principal".

## Alignement dans les cellules

`justify-items` et `align-items` influencent le contenu dans chaque case. `justify-content` / `align-content` influencent la grille dans son conteneur quand il reste de l'espace. Pour une galerie de cartes, commence par laisser les items s'etirer (`stretch` par defaut) et controle le padding dans `.carte`.

## Ce que ce n'est pas

Ce n'est pas "Flexbox est mort". Ce n'est pas non plus mettre `display: grid` et s'attendre a ce que Flex "merge" magiquement. Non : tu choisis l'outil du conteneur. Les enfants deviennent des items de grille. Et ce n'est pas dix colonnes fixes en pixels sur mobile.

:::attention
Trop de colonnes fixes en pixels + `gap` enorme sur petit ecran etouffe le contenu. Teste en fenetre etroite. Passe `--gap` en plus petit sous media query si besoin.
:::

## Petite histoire

Lea a remplace un Flex + largeurs en % bancal par `repeat(auto-fit, minmax(220px, 1fr))`. Les cartes boutique se sont alignees sans media query. Max a vu la demo et a dit "c'est comme des etageres qui s'adaptent a la piece". Sam a ajoute une carte "A la une" avec `grid-column: 1 / -1` : les eleves ont compris le placement en une minute.

## Erreur classique

Mettre `display: grid` et esperer un hybride Flex. Autre piege : trop de colonnes fixes sur mobile. Autre : placement manuel partout alors que l'ordre HTML suffisait. Autre encore : oublier `gap` et compenser avec des margins sur chaque carte.

## En vrai

Prends trois cartes produit (meme fausses). Mets-les dans une grille a deux ou trois colonnes avec `gap`. Redimensionne la fenetre. Observe comment les items se placent. Compare mentalement a un Flexbox avec `flex-wrap` : Grid pense deja en colonnes declarees.

Ajoute une quatrieme carte "A la une" avec `grid-column: 1 / -1` au-dessus. Tu sens deja le pouvoir du placement.

## A toi

Cree une mini page "Ateliers" avec un titre et une grille de quatre cartes (titre + une phrase). `grid-template-columns: 1fr 1fr`, `gap: 1rem`. Sur feuille externe. Variables pour couleurs et gap. Pas besoin d'images. Le placement compte.

:::retenir
Grid = lignes + colonnes. `fr`, `gap`, `repeat`, `minmax` / `auto-fit`. Flex reste pour une dimension. Un mode par conteneur.
:::
