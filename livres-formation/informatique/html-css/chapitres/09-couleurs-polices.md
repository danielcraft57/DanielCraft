# Chapitre 9 - Couleurs, polices, tailles

Maintenant on rend ca vivant.

## Couleurs

```css
body {
  color: #222222;        /* texte */
  background: #f7f3ee;   /* fond */
}

h1 {
  color: teal;
}
```

Tu peux ecrire :
- un nom (`red`, `teal`, `navy`)
- un code hex (`#ff6600`)
- du rgb (`rgb(255, 100, 50)`)

Hex, c'est le plus courant sur le web.
`#000000` = noir. `#ffffff` = blanc.

Astuce : des outils comme un color picker t'aident a choisir. Pas besoin de retenir les codes par coeur.

## Polices

```css
body {
  font-family: Georgia, "Times New Roman", serif;
  font-size: 18px;
  line-height: 1.6;
}
```

`font-family` = la police.
Si la premiere n'existe pas sur l'ordi, il prend la suivante.
`line-height: 1.6` = respirer entre les lignes. Plus agreable a lire.

### Polices "safe" pour commencer

- `Arial, sans-serif` (moderne, sans empattement)
- `Georgia, serif` (un peu plus litteraire)

Plus tard tu pourras charger des polices web (Google Fonts, etc.). Pas obligatoire au debut.

## Graisse et style

```css
h1 {
  font-weight: 700; /* gras */
}

em {
  font-style: italic;
}
```

## Taille du texte

```css
h1 { font-size: 2.5rem; }
p  { font-size: 1rem; }
```

`px` = pixels. Simple.
`rem` = relatif a la taille de base. Plus souple pour l'accessibilite.

Au debut, `px` c'est ok. Tu passeras a `rem` quand tu seras a l'aise.

## Centrer un texte

```css
h1 {
  text-align: center;
}
```

`left`, `right`, `center`, `justify`.

## A toi

- Fond doux (pas blanc crame si tu veux etre cosy)
- Texte sombre pour bien lire
- Titre colore
- Paragraphes un peu plus grands (16-18px minimum)


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
