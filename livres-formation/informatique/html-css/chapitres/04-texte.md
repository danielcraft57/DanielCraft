# Chapitre 4 - Titres, textes, paragraphes

Le texte, c'est le coeur de presque toutes les pages.

## Les titres : h1 a h6

```html
<h1>Le plus grand</h1>
<h2>Un cran en dessous</h2>
<h3>Encore un peu plus petit</h3>
```

Regle simple : un seul `h1` par page (le sujet principal). Ensuite tu mets des `h2` pour les parties, et des `h3` pour les sous-parties.

C'est comme un plan de redaction.
Ca aide aussi Google a comprendre ta page. Mais surtout : ca aide le lecteur.

## Les paragraphes

```html
<p>Une idee par paragraphe, c'est souvent plus clair.</p>
<p>Tu peux en mettre plusieurs a la suite.</p>
```

Ne mets pas tout dans un seul `<p>` geant.
Coupe. Respire. Lis a voix haute si besoin.

## Gras, italique, et cie

```html
<p>Voici un mot <strong>important</strong>.</p>
<p>Voici un mot <em>en emphase</em> (souvent en italique).</p>
<p>Un <mark>surlignage</mark> pour attirer l'oeil.</p>
```

`strong` = vraiment important.
`em` = on insiste un peu.
Evite de tout mettre en gras. Sinon plus rien ne ressort.

## Citations et code

```html
<blockquote>
  Une citation un peu longue.
</blockquote>

<p>En ligne, on peut citer <code>du code</code>.</p>
```

`code` est pratique quand tu expliques une balise dans une phrase.

## Commentaires (pour toi, pas pour le visiteur)

```html
<!-- Ceci ne s'affiche pas sur la page -->
```

Utile pour te laisser des notes. Ou desactiver un bout de code sans l'effacer.

## A eviter

N'utilise pas `h1` juste parce que "c'est plus gros" : la taille, c'est le job du CSS. Evite aussi de sauter de `h1` a `h4` sans raison. Et coupe les murs de texte : un lecteur a besoin de respirer.

## A toi

Ecris une mini page "Ma journee". Mets un h1 avec le titre, puis trois h2 (matin, apres-midi, soir), avec un petit paragraphe sous chaque h2.


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
