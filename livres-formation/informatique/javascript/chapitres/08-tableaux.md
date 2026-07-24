# Chapitre 8 - Les tableaux (des listes)

Un tableau, c'est une file d'attente d'elements.
Index commence a 0. Oui, a 0. Bizarre au debut, puis normal.

## Creer

```js
const courses = ["pain", "lait", "oeufs"];
```

## Lire / modifier

```js
console.log(courses[0]); // pain
courses[1] = "lait d'avoine";
```

## Longueur

```js
console.log(courses.length); // 3
```

## Ajouter / retirer

```js
courses.push("beurre");     // ajoute a la fin
const dernier = courses.pop(); // retire le dernier
```

## Parcourir

```js
for (let i = 0; i < courses.length; i = i + 1) {
  console.log(courses[i]);
}

// ou :
for (const item of courses) {
  console.log(item);
}
```

## Includes

```js
if (courses.includes("pain")) {
  console.log("On a du pain");
}
```

## A toi

Fais une liste de 4 jeux.
Ajoutes-en un avec `push`.
Affiche tous les jeux avec une boucle.

## Erreur classique

Tu confonds l'index et la longueur. Le dernier index n'est pas `length`, c'est `length - 1`.

Mauvais :

```js
const fruits = ["pomme", "poire"];
console.log(fruits[2]); // undefined (index 2 n'existe pas)
```

Bon :

```js
console.log(fruits[fruits.length - 1]); // poire
```

## Exemple complet

```js
// Liste de courses avec actions
const courses = ["pain", "lait", "oeufs"];

// Ajouter
courses.push("fromage");
console.log("Apres ajout :", courses);

// Parcourir et numeroter
for (let i = 0; i < courses.length; i = i + 1) {
  console.log(i + 1 + ". " + courses[i]);
}

// Chercher
const cherche = "lait";
if (courses.includes(cherche)) {
  console.log(cherche + " est dans la liste");
}

// Retirer le dernier
const retire = courses.pop();
console.log("Retire : " + retire);
console.log("Liste finale :", courses);
```

## Mini defi

- Cree un tableau de 5 films
- Affiche le 1er et le dernier
- Ajoute un film avec `push`, retire-en un avec `pop`
- Parcours avec `for...of` et affiche chaque titre en majuscules (`.toUpperCase()`)

## A retenir

- Index commence a 0
- `push` ajoute, `pop` retire a la fin
- `length` = nombre d'elements
- `includes` cherche un element dans le tableau


## En vrai, sur le terrain

Ouvre la console. Retape l'exemple a la main.
Change une valeur. Regarde ce qui bouge. C'est comme ca que ca rentre.

## Mini defi

Inventes un tout petit cas perso (ton prenom, ton score, ton jeu prefere).
Repars de l'exemple avec TES donnees. Si ca marche, c'est bon signe.
