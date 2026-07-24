# Chapitre 13 - Mini-projet : compteur de score

On assemble. Un petit score interactif.

## But

- Afficher un score
- Bouton +1
- Bouton -1
- Bouton reset
- Le score ne descend pas sous 0

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

- Les 3 boutons marchent
- Pas de score negatif
- Code range (const/let, fonctions courtes)

## Bonus

- Change la couleur du score si score >= 10
- Ajoute un message "Belle serie !"


## En vrai, sur le terrain

Ouvre la console. Retape l'exemple a la main.
Change une valeur. Regarde ce qui bouge. C'est comme ca que ca rentre.

## Mini defi

Inventes un tout petit cas perso (ton prenom, ton score, ton jeu prefere).
Repars de l'exemple avec TES donnees. Si ca marche, c'est bon signe.
