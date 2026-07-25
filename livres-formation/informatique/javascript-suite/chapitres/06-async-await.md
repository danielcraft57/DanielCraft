# Chapitre 6 - async/await : du fetch lisible

Les then marchent. Mais quand tu enchaines plusieurs etapes, ou quand tu lis ton propre code six mois plus tard, la chaine devient une chenille difficile a suivre. **async** et **await** permettent d'ecrire presque comme du code "normal", ligne apres ligne, tout en restant asynchrone. Tu gardes la page reactive, mais ton cerveau lit de haut en bas. Chez DanielCraft, on passe souvent en async/await des que le flux depasse deux etapes. Ce n'est pas un autre concept magique : c'est la meme histoire de promesse, mieux racontee.

Lea a reecrit ses chargeurs de produits en async/await et a divise par deux le temps de debug. Max, qui code un peu le soir, prefere cette syntaxe parce qu'elle ressemble a une recette de cuisine. Sam la montre apres les promesses pour que ses eleves voient que ce n'est pas un autre concept : c'est la meme histoire, mieux ecrite. Si tu as bien digere then/catch, ce chapitre devrait te faire sourire de soulagement.

## Le geste de base

Tu marques une fonction avec async. Dedans, tu peux await une promesse. JavaScript attend le resultat de cette ligne, puis continue. La page, elle, n'est pas fige : d'autres evenements peuvent encore se produire.

```js
async function chargerProduits() {
  const reponse = await fetch("https://exemple.api/produits");
  const produits = await reponse.json();
  console.log(produits);
}

chargerProduits();
```

Compare avec la version then du chapitre precedent. C'est la meme histoire, plus lisible. Demande. Lis JSON. Utilise. Le cerveau aime ca. Tu n'as plus a sauter mentalement d'un then a l'autre pour suivre le fil.

## Reecrire l'exemple meteo

Version claire pour afficher la meteo d'une ville. Tu lis de haut en bas sans sauter entre then. Chaque await marque un point d'attente explicite.

```js
async function afficherMeteo(ville) {
  const url = "https://exemple.api/meteo?ville=" + encodeURIComponent(ville);
  const reponse = await fetch(url);
  const data = await reponse.json();

  document.querySelector("#meteo").textContent =
    "A " + data.ville + ", il fait " + data.temp + " degres";
}
```

Quand Lea revoit ce code dans un an, elle comprend en dix secondes ce qu'il fait. C'est exactement le genre de lisibilite qu'on cherche dans un vrai projet, meme petit.

## Attention : await seulement dans async

Tu ne peux pas ecrire await fetch(...) tout seul au milieu d'un script classique (sauf modules top-level dans certains contextes modernes, qu'on ne generalise pas ici). Encapsule dans async function. Aussi : une fonction async renvoie toujours une **promesse**. Si tu return produits, l'appelant recoit une promesse de produits. Il devra await ou .then a son tour.

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

Ce decoupage est propre : getProduits parle au reseau, demarrer orchestre. Tu retrouveras ce pattern au chapitre modules. Separar "qui charge" et "qui affiche" commence deja ici, meme dans un seul fichier.

:::attention
Oublier await est le piege classique : const reponse = fetch(url) te donne une Promise, pas une Response. Ensuite reponse.json() plante. Ou attendre json() sans await et te demander pourquoi data est encore une Promise.
:::

## try/catch avec await

Les erreurs reseau se detailent au chapitre suivant. Mais le reflexe arrive deja. **try/catch** autour d'await, c'est l'equivalent confortable de .catch. Meme role, syntaxe plus familiere pour qui vient de langages synchrones.

```js
async function afficherMeteo(ville) {
  try {
    const reponse = await fetch(
      "https://exemple.api/meteo?ville=" + encodeURIComponent(ville)
    );
    const data = await reponse.json();
    document.querySelector("#meteo").textContent =
      data.ville + " : " + data.temp + " degres";
  } catch (erreur) {
    document.querySelector("#meteo").textContent =
      "Meteo indisponible pour le moment.";
  }
}
```

Tu gardes le meme confort de lecture que le chemin heureux, tout en protegeant le chemin rate. Au chapitre suivant, on ajoutera response.ok pour completer le filet.

:::astuce
Quand tu encapsules plusieurs await dans un try, un seul catch couvre fetch, json() et souvent l'affichage. Commence large, puis affine si tu as besoin de messages differents.
:::

## Quand garder then ?

Parfois un tout petit enchainement. Parfois une lib qui renvoie des promesses et tu branches un seul then. Ce n'est pas interdit. Mais pour du code que tu lis et modifies regulierement, async/await gagne souvent. L'important : comprendre les deux, choisir selon la lisibilite. DanielCraft ne dogmatise pas : on choisit ce qui se relit le mieux dans six mois. then, c'est lire une recette en notes en marge ("quand la pizza arrive, fais ceci"). async/await, c'est lire la recette dans l'ordre avec des pauses marquees ("attends que le four chauffe, puis enfourne"). Le resultat final est le meme. L'experience de lecture change. Choisis l'outil qui te fait moins d'erreurs de lecture.

## Erreur classique

Oublier await :

```js
const reponse = fetch(url); // reponse = Promise, pas Response
const data = await reponse.json(); // plante : Promise n'a pas .json
```

Ou croire que async magique rend le code synchrone pour tout le monde. Non : ca rend ton ecriture lineaire. Le temps, lui, continue de passer. La page reste interactive. Ou mettre await dans une fonction non async : erreur de syntaxe immediate, heureusement. Ou oublier await sur reponse.json() et te demander pourquoi data est une Promise.

## Petite histoire

Max a copie un tuto avec await sans async sur la fonction. Rien ne marchait. En ajoutant async devant function, tout s'est debloque. Lea, elle, a deja vu des juniors oublier await sur reponse.json() et se demander pourquoi data est une Promise. Ces deux oublis sont les plus frequents. Garde-les en tete. Sam les ecrit au tableau avant chaque atelier fetch.

## En vrai

Reprends un fetch en then que tu as deja ecrit (chapitre 4 ou 5). Reecris-le en async/await. Compare les deux versions cote a cote. Laquelle te parle le plus ? Garde celle-la pour la suite du livre et pour tes projets perso. L'exercice n'est pas de "preferer la mode" : c'est de preferer ce que tu debogues plus vite.

## A toi

Ecris async function chargerEtAfficher(url) qui charge une liste JSON et remplit un ul. Ajoute un message "Chargement..." avant le fetch, puis remplace-le par le resultat ou une erreur. Tu dois sentir le rythme : avant / pendant / apres. Ce rythme, c'est celui de toute appli web qui parle au reseau.

:::retenir
async/await = meme promesse, lecture lineaire - await dans une fonction async, try/catch pour l'echec, ne jamais oublier await.
:::
