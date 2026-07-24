# Chapitre 5 - CSS Grid : lignes et colonnes

Flexbox, tu le connais : super pour une rangee, un menu, aligner dans un sens. Grid, c'est autre chose. Tu poses un vrai damier. Lignes et colonnes. Ideal pour une page, une galerie, un tableau de cartes produit.

Tu n'abandonnes pas Flexbox. Tu ajoutes un outil. Souvent : Grid pour la structure de page, Flexbox pour les petits alignements a l'interieur d'une cellule.

Chez DanielCraft, Grid, c'est le plan au sol. Flex, c'est ranger les chaises dans une piece.

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

Sur une page boutique, ces trois cartes s'alignent proprement. Ajoute un quatrieme produit : il passe a la ligne suivante, toujours dans la grille.

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

## minmax et auto-fit (idee simple)

Pour une grille de cartes qui s'adapte sans media query compliquee :

```css
.grille {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem;
}
```

L'idee : chaque colonne fait au moins 220px, et on en met autant que ca rentre. Sur telephone, une colonne. Sur grand ecran, plusieurs. Tu peaufineras au chapitre mise en page et au mini-projet.

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

`gap` (et `row-gap` / `column-gap` si besoin) espace les cellules sans casser les bords externes. Sur un blog en grille de billets, c'est net, previsible, facile a retoucher avec une variable `--gap`.

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

Placement par ligne/colonne :

```css
.promo {
  grid-column: 2;
  grid-row: 1;
}
```

Reste lisible. N'en abuse pas au debut : une grille bien remplie dans l'ordre du HTML suffit souvent.

## Alignement dans les cellules

`justify-items` et `align-items` influencent le contenu dans chaque case. `justify-content` / `align-content` influencent la grille dans son conteneur quand il reste de l'espace. Pour une galerie de cartes, commence par laisser les items s'etirer (`stretch` par defaut) et controle le padding dans `.carte`.

## Erreur classique

Mettre `display: grid` et s'attendre a ce que Flexbox "merge" magiquement. Non : tu choisis l'outil du conteneur. Les enfants deviennent des items de grille.

Autre piege : trop de colonnes fixes en pixels sur mobile. Teste aussi en fenetre etroite. Et `gap` enorme qui etouffe le contenu sur petit ecran : passe `--gap` en plus petit sous une media query si besoin.

## En vrai

Prends trois cartes produit (meme fausses). Mets-les dans une grille a deux ou trois colonnes avec `gap`. Redimensionne la fenetre. Observe comment les items se placent. Compare mentalement a un Flexbox avec `flex-wrap` : Grid pense deja en colonnes declarees.

Ajoute une quatrieme carte "A la une" avec `grid-column: 1 / -1` au-dessus. Tu sens deja le pouvoir du placement.

## A toi

Cree une mini page "Ateliers" avec un titre et une grille de quatre cartes (titre + une phrase). `grid-template-columns: 1fr 1fr`, `gap: 1rem`. Sur feuille externe. Variables pour couleurs et gap. Pas besoin d'images. Le placement compte.
