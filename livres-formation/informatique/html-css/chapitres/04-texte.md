# Chapitre 4 - Titres, textes, paragraphes

Le texte, c'est le coeur de presque toutes les pages.

## Les titres : h1 a h6

```html
<h1>Le plus grand</h1>
<h2>Un cran en dessous</h2>
<h3>Encore un peu plus petit</h3>
```

Regle simple :
- Un seul `h1` par page (le sujet principal)
- Ensuite `h2` pour les parties
- `h3` pour les sous-parties

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

- Utiliser `h1` juste parce que "c'est plus gros" (utilise le CSS pour la taille)
- Sauter de `h1` a `h4` sans raison
- Des murs de texte sans retour

## A toi

Ecris une mini page "Ma journee" :
- h1 avec le titre
- 3 h2 (matin, apres-midi, soir)
- un petit paragraphe sous chaque h2
