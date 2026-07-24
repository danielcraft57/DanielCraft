# Chapitre 7 - Les fonctions (des recettes reutilisables)

Une fonction, c'est une recette.
Tu la definis une fois. Tu l'appelles quand tu veux.

## Creer et appeler

```js
function direSalut() {
  console.log("Salut !");
}

direSalut();
direSalut();
```

## Avec des ingredients (parametres)

```js
function direSalutA(prenom) {
  console.log("Salut " + prenom);
}

direSalutA("Nora");
direSalutA("Tom");
```

## Avec un resultat (return)

```js
function double(n) {
  return n * 2;
}

const resultat = double(4);
console.log(resultat); // 8
```

`return` renvoie une valeur. Sans `return`, tu obtiens `undefined`.

## Pourquoi c'est cool

- Moins de copie
- Code plus clair
- Plus facile a corriger

## Petite forme moderne (juste voir)

```js
const triple = (n) => n * 3;
```

Tu verras ca souvent. Pour l'instant, `function` suffit largement.

## A toi

Ecris `moyenne(a, b)` qui renvoie la moyenne de deux notes.
Teste avec 12 et 16.

## Erreur classique

Tu oublies `return`. La fonction fait son travail, mais tu recupères `undefined`.

Mauvais :

```js
function carre(n) {
  n * n; // resultat perdu
}
console.log(carre(4)); // undefined
```

Bon :

```js
function carre(n) {
  return n * n;
}
console.log(carre(4)); // 16
```

## Exemple complet

```js
// Mini calculateur de notes
function moyenne(a, b, c) {
  return (a + b + c) / 3;
}

function mention(note) {
  if (note >= 16) return "Tres bien";
  if (note >= 14) return "Bien";
  if (note >= 10) return "Passable";
  return "Insuffisant";
}

function afficherBulletin(prenom, n1, n2, n3) {
  const moy = moyenne(n1, n2, n3);
  const m = mention(moy);
  console.log(prenom + " : " + moy.toFixed(1) + "/20 - " + m);
}

afficherBulletin("Leo", 12, 15, 18);
afficherBulletin("Nina", 8, 9, 11);
```

Chaque fonction a un role clair. C'est plus facile a lire et a corriger.

## Mini defi

- Ecris `aireRectangle(largeur, hauteur)` avec `return`
- Ecris `estMajeur(age)` qui renvoie true ou false
- Ecris `saluer(prenom)` qui affiche un message (sans return)
- Appelle les 3 fonctions avec des valeurs differentes

## A retenir

- Une fonction = une recette reutilisable
- Parametres = ingredients, `return` = le plat fini
- Sans `return`, tu obtiens `undefined`
- Petites fonctions = code plus propre


## En vrai, sur le terrain

Ouvre la console. Retape l'exemple a la main.
Change une valeur. Regarde ce qui bouge. C'est comme ca que ca rentre.

## Mini defi

Inventes un tout petit cas perso (ton prenom, ton score, ton jeu prefere).
Repars de l'exemple avec TES donnees. Si ca marche, c'est bon signe.
