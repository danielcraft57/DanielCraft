# Chapitre 3 - Les variables (des boites a infos)

Une variable, c'est une boite avec une etiquette.
Tu ranges une valeur. Tu la reutilises plus tard.

## let et const

```js
let age = 12;
const prenom = "Leo";
```

Avec `let`, tu pourras changer la valeur plus tard. Avec `const`, tu ne changes pas : c'est une constante. Astuce debutant : utilise `const` par defaut, et passe a `let` seulement si tu dois vraiment modifier la valeur.

## Changer une valeur

```js
let score = 0;
score = 10;
score = score + 1; // 11
```

## Noms clairs

Oui :

```js
let nombreDeClics = 0;
const messageBienvenue = "Salut";
```

Non (ou alors on se perd) :

```js
let x = 0;
let a1 = "Salut";
```

## Attention

```js
const ville = "Lyon";
ville = "Paris"; // erreur
```

`const` protege. C'est voulu.

## A toi

Cree une constante `prenom` avec ton prenom entre guillemets, puis un `let points = 0`. Ajoute 5 points, et affiche le prenom et les points avec `console.log`. Tu dois voir les deux infos dans la console.

## Erreur classique

Tu reutilises un nom sans le declarer. JS cree une variable globale par accident. Ca casse tout sur une grosse page.

Mauvais :

```js
score = 10; // oubli de let ou const
```

Bon :

```js
let score = 10;
```

Autre piege : tu changes une `const`. Le navigateur bloque. C'est normal, c'est la protection.

## Exemple complet

```js
// Un mini profil joueur
const pseudo = "PixelFox";
let niveau = 1;
let xp = 0;

// On gagne de l'xp
xp = xp + 50;
console.log(pseudo + " a " + xp + " xp");

// Passage de niveau
if (xp >= 50) {
  niveau = niveau + 1;
  xp = xp - 50;
  console.log("Niveau up ! Tu es niveau " + niveau);
}

console.log("Etat final : niveau " + niveau + ", xp " + xp);
```

Lis la console ligne par ligne. Tu vois comment les valeurs changent.

## Mini defi

Cree trois `const` : prenom, ville, animal prefere. Cree aussi deux `let` : compteurVisites et derniereNote. Modifie seulement les `let`, laisse les `const` tranquilles. Ensuite, affiche une phrase qui melange tout avec des `+`. Si la console rale quand tu touches une `const`, c'est que tu as bien compris la protection.

## A retenir

Prends `const` par defaut, et `let` seulement si tu dois changer la valeur. Un nom clair vaut mieux que `x` ou `a1`. Declare toujours avec `let` ou `const` : une variable, c'est une boite etiquetee que tu reutilises.


## En vrai, sur le terrain

Ouvre la console. Retape l'exemple a la main.
Change une valeur. Regarde ce qui bouge. C'est comme ca que ca rentre.

## Mini defi

Inventes un tout petit cas perso (ton prenom, ton score, ton jeu prefere).
Repars de l'exemple avec TES donnees. Si ca marche, c'est bon signe.
