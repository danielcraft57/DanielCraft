# Chapitre 10 - Le DOM : trouver des elements

Le DOM, c'est la page vue par JavaScript.
Des elements. Des noeuds. Bref : ce que tu as ecrit en HTML, accessible en JS.

## Selectionner

HTML :

```html
<h1 id="titre">Salut</h1>
<button class="btn">Clique</button>
```

JS :

```js
const titre = document.querySelector("#titre");
const bouton = document.querySelector(".btn");
```

`#titre` vise un id, `.btn` vise une classe. C'est la meme logique qu'en CSS, et c'est pour ca que ca devient vite naturel.

## querySelectorAll

```js
const items = document.querySelectorAll("li");
console.log(items.length);
```

Ca renvoie une liste d'elements.

## Verifier

```js
console.log(titre);
```

Si tu vois `null`, ton selecteur est faux, ou le script tourne trop tot.
Rappel : mets le `<script>` juste avant `</body>`.

## A toi

Dans ta page :
1. un `h1` avec un id
2. selectionne-le en JS
3. `console.log` son texte avec `titre.textContent`


## En vrai, sur le terrain

Ouvre la console. Retape l'exemple a la main.
Change une valeur. Regarde ce qui bouge. C'est comme ca que ca rentre.

## Mini defi

Inventes un tout petit cas perso (ton prenom, ton score, ton jeu prefere).
Repars de l'exemple avec TES donnees. Si ca marche, c'est bon signe.
