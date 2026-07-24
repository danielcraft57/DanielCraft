# Chapitre 11 - Flexbox : ranger les blocs

Flexbox, c'est l'outil magique pour aligner des trucs.
Menu en ligne, colonnes, centrage... Ca sauve des vies.

## Idee simple

Tu as un parent (le conteneur).
Dedans, des enfants (les items).

Tu dis au parent : "range tes enfants en flex".

```html
<div class="rangée">
  <div>A</div>
  <div>B</div>
  <div>C</div>
</div>
```

Attends - apostrophe. Mieux :

```html
<div class="rangee">
  <div>A</div>
  <div>B</div>
  <div>C</div>
</div>
```

```css
.rangee {
  display: flex;
  gap: 16px;
}
```

`gap` = l'espace entre les enfants. Clean.

## Direction

```css
.rangee {
  display: flex;
  flex-direction: row; /* cote a cote (defaut) */
}

.colonne {
  display: flex;
  flex-direction: column; /* l'un sous l'autre */
}
```

## Aligner

```css
.rangee {
  display: flex;
  justify-content: space-between; /* horizontal si row */
  align-items: center;            /* vertical si row */
}
```

`justify-content` = sur l'axe principal.
`align-items` = sur l'axe croise.

Tu vas experimenter. C'est normal. Change une valeur, regarde, recommence.

## Centrer un truc au milieu (classique)

```css
.centre {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 200px;
}
```

## Les enfants peuvent grandir

```css
.rangee > div {
  flex: 1; /* partage l'espace equitablement */
}
```

## A toi

Fais une barre avec un logo a gauche et deux liens a droite.
Indice : `display: flex` + `justify-content: space-between` + `align-items: center`.


## En vrai, sur le terrain

Prends 10 minutes. Refais l'exemple du chapitre sans regarder.
Si tu bloques, relis juste la partie qui coinçe. Puis repars.

Le but c'est pas de memoriser. C'est de reconnaitre le motif la prochaine fois.

## Mini defi

Ecris 3 lignes de notes a toi-meme :
1. ce que tu as compris
2. ce qui reste flou
3. un truc a retester demain

Garde ces notes. Elles valent plus qu'un long cours jamais relu.
