# Chapitre 13 - Mini-projet : compteur de score

On assemble. C'est le moment ou tout ce que tu as appris se rencontre : **variables**, **DOM**, **evenements**. Le but est simple et concret : afficher un score, le faire monter avec un bouton +1, le faire descendre avec -1 (sans passer sous zero), le remettre a zero avec reset. Simple en apparence. Mais ca assemble la chaine complete que tu retrouveras sur presque chaque page interactive. Chez DanielCraft, ce mini-projet est le "hello world" utile : tu touches, ca repond, tu comprends le fil du debut a la fin.

Lea utilise des compteurs similaires pour des demos clients : "regardez, votre page peut compter les demandes de devis en test". Max a fait le sien pour un mini jeu avec ses neveux un dimanche pluvieux. Sam note : si les trois boutons marchent, le score ne descend jamais sous zero, et le code est range avec une fonction `afficher`, c'est reussi. Pas besoin de perfection. Pas besoin de localStorage encore. Besoin d'un geste fini que tu peux montrer sans rougir.

Un tableau de score au basketball de salon. Tu ajoutes un point, tu retires un point (sans passer en negatif), tu remets a zero pour une nouvelle manche. L'afficheur au mur, c'est le DOM (`#score`). Les boutons sur la table, ce sont les evenements. La variable `score` en memoire, c'est le vrai chiffre. Trois pieces, un systeme. Change la memoire, puis mets a jour l'ecran. Dans cet ordre. Toujours.

## Ce que ce n'est pas

Ce n'est pas un jeu AAA avec des graphismes et du son obligatoire. Ce n'est pas localStorage encore - ca viendra dans l'atelier todo et le chapitre 18. Ce n'est pas "parfait ou rien" : une version 1 qui marche bat une version mentale jamais codee. Et ce n'est pas copier-coller sans retaper : les doigts apprennent. Sam interdit parfois le copier-coller en atelier. Lea chronometre parfois : "version 1 en vingt minutes". L'objectif, c'est finir.

## HTML

```html
<h1>Score</h1>
<p id="score">0</p>
<button id="plus">+1</button>
<button id="moins">-1</button>
<button id="reset">Reset</button>
<script src="script.js"></script>
```

Place le script avant `</body>`. Les ids doivent correspondre exactement a ce que tu selectionnes en JS. Une faute de frappe, et tu ecoutes le vide.

## CSS (simple)

```css
body {
  font-family: Georgia, serif;
  text-align: center;
  margin-top: 3rem;
  background: #f4f1ec;
}
#score { font-size: 3rem; }
button {
  font: inherit;
  margin: 0.3rem;
  padding: 0.5rem 0.9rem;
}
```

Le CSS n'est pas l'objet du chapitre, mais un minimum de style rend la demo presentable. Max a ajoute un fond bleu pale. Ses neveux ont trouve ca "officiel".

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

La fonction **`afficher`** centralise la mise a jour de l'ecran. Chaque listener change `score`, puis appelle `afficher()`. Pas de duplication. Lea insiste : un seul endroit qui ecrit dans le DOM pour le score. Si demain tu changes l'affichage, tu touches une fonction.

:::retenir
Change la memoire (`score`), puis mets a jour l'ecran (`afficher`). Dans cet ordre. Toujours.
:::

## Criteres de reussite

Les trois boutons marchent. Le score ne descend jamais sous zero. `const` pour les elements DOM, `let` pour `score` (car il change). Fonction `afficher` courte et reutilisee. Script avant `</body>`. Tu as clique partout sans erreur en console. C'est entre.

## Petite histoire

Lea chronometre parfois ses stagiaires : "version 1 en vingt minutes, sans perfection". Max a ajoute un son bete au clic +1, ses neveux ont crie comme au basket. Sam interdit le copier-coller sans retaper : "les doigts apprennent ce que les yeux survolent". Tu peux retaper ligne par ligne. C'est voulu. Le projet finit quand tu as teste chaque bouton dix fois et que tu peux expliquer chaque ligne a voix haute.

## Erreur classique

Oublier `afficher()` apres un changement de score : la variable bouge en memoire, l'ecran reste fige. Laisser descendre sous zero : oublier le `if (score > 0)`. Selecteurs faux : `#score` vs `#Score`. Mettre `score` en `const` puis tenter de reassigner : erreur immediate. Autre piege : tout coller dans un seul listener geant. Decoupe. Un listener par bouton. Respire.

:::astuce
Si l'ecran ne bouge pas : loggue `score` dans le listener. Si le chiffre change en console mais pas a l'ecran, tu as oublie `afficher()`.
:::

## Bonus (quand la base marche)

Message si score >= 10 ("Bravo champion !"). Couleur differente via une classe CSS togglee. Bouton +5 pour accelerer. Plus tard : sauver dans localStorage (chapitre 18). Mais d'abord : la base qui marche. DanielCraft insiste : version 1 livrable avant version 2 fancy.

## En vrai

Construis-le en une session courte. Une heure max si tu retapes. Clique partout. Casse volontairement un id, regarde l'erreur en console, repare. Tu valides la chaine complete : HTML, CSS, JS, DOM, evenements. C'est un vrai cran. Lea chronometre parfois : "version 1 en vingt minutes". L'objectif, c'est finir, pas peaufiner eternellement.

## A toi

Ajoute une regle perso (exemple : score max 20, ou message a 10). Documente-la en trois lignes dans un commentaire ou un post-it. Chez DanielCraft, un projet fini avec une note vaut mieux qu'un projet "presque" jamais montre. Montre ton compteur a quelqu'un - meme trente secondes. Le geste compte.
