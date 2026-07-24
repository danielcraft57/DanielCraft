# Chapitre 6 - async/await : du fetch lisible

Les `then` marchent. Mais quand tu enchaises plusieurs etapes, ca devient vite une chenille. `async` et `await` permettent d'ecrire presque comme du code "normal", ligne apres ligne, tout en restant asynchrone.

## Le geste de base

Tu marques une fonction avec `async`. Dedans, tu peux `await` une promesse. JavaScript attend le resultat de cette ligne, puis continue.

```js
async function chargerProduits() {
  const reponse = await fetch("https://exemple.api/produits");
  const produits = await reponse.json();
  console.log(produits);
}

chargerProduits();
```

Compare avec la version `then`. C'est la meme histoire, plus lisible. Chez DanielCraft, on passe souvent en `async/await` des que le flux depasse deux etapes.

## Reecrire l'exemple meteo

Version claire :

```js
async function afficherMeteo(ville) {
  const url = "https://exemple.api/meteo?ville=" + encodeURIComponent(ville);
  const reponse = await fetch(url);
  const data = await reponse.json();

  document.querySelector("#meteo").textContent =
    "A " + data.ville + ", il fait " + data.temp + "°C";
}
```

Tu lis de haut en bas. Demande. Lis JSON. Affiche. Le cerveau aime ca.

## Attention : await seulement dans async

Tu ne peux pas ecrire `await fetch(...)` tout seul au milieu d'un script classique (sauf modules top-level dans certains contextes modernes, on n'en fait pas une regle ici). Encapsule dans `async function ...`.

Aussi : une fonction `async` renvoie toujours une promesse. Si tu `return produits`, l'appelant recoit une promesse de produits. Il devra `await` ou `.then` a son tour.

```js
async function getProduits() {
  const reponse = await fetch("https://exemple.api/produits");
  return reponse.json();
}

async function demarrer() {
  const produits = await getProduits();
  console.log(produits.length);
}

demarrer();
```

## try/catch avec await

Les erreurs, on les detaille au chapitre suivant. Mais le reflexe arrive deja :

```js
async function afficherMeteo(ville) {
  try {
    const reponse = await fetch(
      "https://exemple.api/meteo?ville=" + encodeURIComponent(ville)
    );
    const data = await reponse.json();
    document.querySelector("#meteo").textContent =
      data.ville + " : " + data.temp + "°C";
  } catch (erreur) {
    document.querySelector("#meteo").textContent =
      "Meteo indisponible pour le moment.";
  }
}
```

`try/catch` autour d'`await`, c'est l'equivalent confortable de `.catch`.

## Quand garder then ?

Parfois un tout petit enchainement. Parfois une lib qui renvoie des promesses et tu branches un seul `then`. Ce n'est pas interdit. Mais pour du code que tu lis dans six mois, `async/await` gagne souvent.

## Erreur classique

Oublier `await` :

```js
const reponse = fetch(url); // reponse = Promise, pas Response
const data = await reponse.json(); // plante : Promise n'a pas .json
```

Ou croire que `async` magique rend le code synchrone pour tout le monde. Non : ca rend ton ecriture lineaire. Le temps, lui, continue de passer ailleurs.

## En vrai

Reprends un fetch en `then` que tu as deja. Reecris-le en `async/await`. Compare les deux versions cote a cote. Laquelle te parle le plus ? Garde celle-la pour la suite du livre.

## A toi

Ecris `async function chargerEtAfficher(url)` qui charge une liste JSON et remplit un `<ul>`. Ajoute un message "Chargement..." avant le fetch, puis remplace-le par le resultat. Tu dois sentir le rythme : avant / pendant / apres.
