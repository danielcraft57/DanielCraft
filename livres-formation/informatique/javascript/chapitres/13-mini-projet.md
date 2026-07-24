# Chapitre 13 - Mini-projet : compteur de score

On assemble. Un petit score interactif.

## But

Tu vas afficher un score a l'ecran, avec un bouton +1, un bouton -1 et un bouton reset. Le score ne doit jamais descendre sous 0. C'est simple, mais ca assemble variables, DOM et evenements.

## HTML

```html
<h1>Score</h1>
<p id="score">0</p>
<button id="plus">+1</button>
<button id="moins">-1</button>
<button id="reset">Reset</button>
<script src="script.js"></script>
```

## CSS (simple)

```css
body {
  font-family: Georgia, serif;
  text-align: center;
  margin-top: 3rem;
  background: #f4f1ec;
}

#score {
  font-size: 3rem;
}

button {
  font: inherit;
  margin: 0.3rem;
  padding: 0.5rem 0.9rem;
}
```

## JS

```js
const scoreEl = document.querySelector("#score");
const plusBtn = document.querySelector("#plus");
const moinsBtn = document.querySelector("#moins");
const resetBtn = document.querySelector("#reset");

let score = 0;

function afficher() {
  scoreEl.textContent = score;
}

plusBtn.addEventListener("click", function () {
  score = score + 1;
  afficher();
});

moinsBtn.addEventListener("click", function () {
  if (score > 0) {
    score = score - 1;
    afficher();
  }
});

resetBtn.addEventListener("click", function () {
  score = 0;
  afficher();
});

afficher();
```

## Criteres de reussite

Les trois boutons doivent marcher. Le score ne passe jamais en negatif. Et ton code reste range : `const` / `let` bien choisis, fonctions courtes. Si ces trois points sont la, le mini-projet tient.

## Bonus

Quand le score atteint 10 ou plus, change sa couleur. Tu peux aussi afficher un message "Belle serie !" pour celebrer. Petit detail, gros effet.


## En vrai, sur le terrain

Ouvre la console. Retape l'exemple a la main.
Change une valeur. Regarde ce qui bouge. C'est comme ca que ca rentre.

## Mini defi

Inventes un tout petit cas perso (ton prenom, ton score, ton jeu prefere).
Repars de l'exemple avec TES donnees. Si ca marche, c'est bon signe.
