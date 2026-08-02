# Chapitre 7 - Flex vs Grid : quand choisir quoi

Tu as deux outils puissants. La question n'est plus "lequel est le meilleur ?" mais "lequel pour ce job ?". **Flexbox** brille dans une dimension : une rangee ou une colonne. Aligner, distribuer l'espace, centrer un bouton, faire un menu, coller une icone a un label. **Grid** brille en deux dimensions : lignes et colonnes en meme temps. Page entiere, galerie, tableau de cartes, zones nommees.

Chez DanielCraft, on dit souvent : Grid pour le plan de la page, Flex pour le mobilier dans chaque piece. Ce n'est pas une loi absolue. C'est un excellent reflexe de depart. Lea le note en commentaire CSS au-dessus de chaque conteneur. Max s'en fiche des noms tant que le devis tient sur telephone - mais le reflexe l'aide quand son neveu explique. Sam fait voter la classe avant de reveler l'outil : "rangee de liens ou damier ?"

## Choisis Flex quand...

Tu ranges des elements sur une seule ligne (ou une seule colonne) et tu veux controler l'espace entre eux. Exemples concrets : un menu horizontal (logo + liens), un bandeau (titre a gauche, bouton a droite), une carte produit (image au-dessus, puis en bas une rangee prix + bouton en Flex). Centrer un bloc dans un hero (souvent Flex sur le conteneur, ou Grid avec place-items - les deux marchent).

```css
.menu {
  display: flex;
  gap: 1rem;
  align-items: center;
  flex-wrap: wrap;
}
```

Simple, direct, parfait. Une **dimension**, un outil clair.

## Choisis Grid quand...

Tu penses deja "colonnes" et "lignes". Tu veux qu'un element occupe toute la largeur pendant que d'autres se partagent une rangee. Tu dessines header / contenu / aside.

```css
.galerie {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1rem;
}
```

Une galerie de cartes blog ou boutique : Grid. Essayer la meme chose en Flex + largeurs + wrap fonctionne, mais tu te bats plus pour des colonnes regulieres. Lea a arrete de "forcer des colonnes" en Flex des qu'elle a goute a `auto-fit`.

## Les deux ensemble

C'est normal et recommande.

```html
<div class="layout">
  <header class="entete">...</header>
  <main>
    <div class="grille-cartes">...</div>
  </main>
</div>
```

`.layout` en Grid (areas). `.entete` en Flex (logo / nav). `.grille-cartes` en Grid (produits). Chaque conteneur choisit son outil. Les enfants ne "melangent" pas les modes du parent : c'est le parent qui decide. Un mode par conteneur. Toujours. Au-dessus de chaque conteneur, un commentaire `/* Grid: plan */` ou `/* Flex: menu */` t'aidera dans six mois.

:::astuce
Avant de coder, ecris sur papier "Flex" ou "Grid" a cote de trois conteneurs de ta page. Le CSS sort plus court quand le choix est clair.
:::

## Cas limites utiles

Une seule colonne de sections qui s'empilent ? Tu n'as pas toujours besoin de Grid. Le flux normal HTML + des marges peut suffire. N'active pas un moteur de layout pour rien.

Un formulaire de deux champs cote a cote sur desktop ? Flex ou Grid, les deux collent. Grid avec `1fr 1fr` est tres clair. Flex avec `flex: 1` aussi. Choisis celui que tu lis le mieux dans six mois.

Un tableau de donnees ? Le HTML `<table>` reste souvent le bon sens semantique. Grid peut mimer un tableau pour des cards, mais pour des vraies donnees tabulaires, garde le tableau.

## Signes que tu as choisi le mauvais outil

Tu ajoutes des largeurs en % partout sur des enfants Flex pour "faire des colonnes" et tu pries pour le wrap : regarde Grid. Tu utilises Grid puis tu te bats avec `align-items` pour un simple menu de liens : reviens a Flex. Tu mets `position: absolute` partout pour sauver un layout : souvent un signe que Grid/Flex n'ont pas ete poses. (L'absolu a sa place pour un badge sur image, pas pour toute la page.)

## Mini decision rapide

Rangee de controles, menu, barre d'actions → Flex. Page ou galerie en damier → Grid. Les deux niveaux (page + barre) → Grid dehors, Flex dedans (ou l'inverse selon le cas, mais reste coherent).

## Ce que ce n'est pas

Ce n'est pas une guerre de camps. Flex n'est pas obsolete. Grid n'est pas "obligatoire partout parce que moderne". Et ce n'est surtout pas declarer `display: flex` et `display: grid` sur le meme element en esperant un hybride. La derniere declaration gagne.

:::attention
Un seul mode par conteneur. Si tu empiles `flex` puis `grid` sur le meme bloc, tu n'as pas un superpouvoir : tu as une derniere ligne qui ecrase l'autre.
:::

## Petite histoire

Lea a chronometre une refonte landing : elle a d'abord etiquete chaque conteneur Flex ou Grid sur papier. Le CSS est sorti plus court, plus clair. Max a vu son neveu se battre avec Flex pour une galerie de photos : passage a Grid, silence soulage. Sam a casse volontairement une page en mettant les deux `display` sur le header : les eleves ont vu lequel gagnait dans l'inspecteur.

## Erreur classique

Declarer flex et grid sur le meme element. Tout convertir en Grid "parce que c'est moderne". Forcer des colonnes en Flex avec des % partout. Sauver le layout a coups d'`absolute`.

## En vrai

Reprends une page landing. Identifie trois conteneurs. Pour chacun, ecris sur un papier "Flex" ou "Grid" et pourquoi. Puis code. Si un choix gene, switch et note la difference de lisibilite du CSS. L'outil qui produit le CSS le plus court et clair gagne souvent.

Sur une carte produit : essaye le corps de la carte en colonne Flex (`flex-direction: column`) et le footer de carte (prix + bouton) en Flex rangee. La page parente reste en Grid.

## A toi

Construis une mini page "Boutique" : layout page en Grid (entete / grille / pied), entete en Flex, grille de 3 produits en Grid `auto-fit`. Aucun `absolute` pour le plan. Une phrase en commentaire CSS au-dessus de chaque conteneur : `/* Grid: plan */` ou `/* Flex: menu */`.

:::retenir
Flex = une dimension. Grid = lignes + colonnes. Souvent Grid dehors, Flex dedans. Un mode par conteneur.
:::
