# Chapitre 12 - Les evenements (reagir aux clics)

La page devient interactive ici.

## click

```html
<button id="bouton">Clique-moi</button>
<p id="message"></p>
```

```js
const bouton = document.querySelector("#bouton");
const message = document.querySelector("#message");

bouton.addEventListener("click", function () {
  message.textContent = "Bravo, tu as clique !";
});
```

`addEventListener` = "quand cet evenement arrive, fais ca".

## Compteur

```js
let clics = 0;

bouton.addEventListener("click", function () {
  clics = clics + 1;
  message.textContent = "Clics : " + clics;
});
```

## Autres evenements utiles

- `input` : quand on ecrit dans un champ
- `submit` : envoi de formulaire
- `mouseover` : souris au-dessus (moins prioritaire)

## Eviter le rechargement de formulaire

```js
form.addEventListener("submit", function (event) {
  event.preventDefault();
  // ton code ici
});
```

`preventDefault` dit au navigateur : "laisse, je gere".

## A toi

Bouton + compteur.
Chaque clic ajoute 1.
Affiche le total dans un `p`.


## En vrai, sur le terrain

Ouvre la console. Retape l'exemple a la main.
Change une valeur. Regarde ce qui bouge. C'est comme ca que ca rentre.

## Mini defi

Inventes un tout petit cas perso (ton prenom, ton score, ton jeu prefere).
Repars de l'exemple avec TES donnees. Si ca marche, c'est bon signe.
