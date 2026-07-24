# Chapitre 10 - Les boites (margin, padding, border)

En CSS, presque tout est une boite.
Un paragraphe = une boite. Une image = une boite. Un bouton = une boite.

## Le modele en boite

De l'exterieur vers l'interieur :
1. margin (marge exterieure - l'espace autour)
2. border (la bordure)
3. padding (marge interieure - l'air dans la boite)
4. le contenu

## Exemple concret

```css
.carte {
  background: white;
  border: 2px solid #333;
  padding: 20px;
  margin: 16px;
  border-radius: 12px;
}
```

`border-radius` arrondit les coins. Sympa.

## Margin vs padding (le piege classique)

Le padding, c'est l'espace *dans* la boite, entre le bord et le texte. La margin, c'est l'espace *hors* de la boite, entre cette boite et les autres.

Tu te tromperas. Tout le monde se trompe. Tu corrigeras.

## Largeur et hauteur

```css
.boite {
  width: 300px;
  max-width: 100%;
  height: auto;
}
```

`max-width: 100%` evite que ca deborde sur telephone. Bon reflexe.

## box-sizing (important)

```css
* {
  box-sizing: border-box;
}
```

Sans ca, padding + border peuvent agrandir la boite de facon bizarre.
Avec `border-box`, width inclut padding et border. Plus intuitif.
Mets ca presque toujours en haut de ton CSS.

## Display : block ou inline

Avec `block`, l'element prend toute la largeur (comme `p`, `div`, `h1`). Avec `inline`, il reste dans le flux du texte (comme `span`, ou un `a` sans style). Et `inline-block`, c'est un mix utile parfois : tu gardes le cote "dans la ligne", mais tu peux aussi mettre du padding proprement.

```css
span.badge {
  display: inline-block;
  padding: 4px 8px;
  background: #eee;
}
```

## A toi

Cree une classe `.carte` avec fond, padding, bordure, coins ronds.
Applique-la a une `div` qui contient un titre et un paragraphe.


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
