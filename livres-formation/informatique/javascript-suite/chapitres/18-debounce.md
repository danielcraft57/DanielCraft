# Chapitre 18 - Debounce : ne pas frapper trop vite

Imagine une barre de recherche. A chaque lettre, tu lances un `fetch`. L'utilisateur tape "bonsoir" : sept requetes. Le serveur souffle. L'affichage clignote. Mauvaise idee.

Le debounce, c'est attendre un petit silence avant d'agir. Tu tapes, tu tapes, tu pauses 300 ms : la seulement, tu lances la recherche.

## Idee en code

```js
function debounce(fn, delai) {
  let timer;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delai);
  };
}

const rechercher = debounce((texte) => {
  console.log("Je cherche :", texte);
  // ici : fetch ou filtre local
}, 300);

input.addEventListener("input", (e) => rechercher(e.target.value));
```

## Quand l'utiliser

Recherche pendant la frappe. Redimensionnement de fenetre. Sauvegarde auto. Partout ou un evenement se repete trop vite.

## Quand ne pas l'utiliser

Un clic sur un bouton "Envoyer" : pas besoin. Un compteur de jeu a chaque frame : ce n'est pas le meme outil.

## En vrai

300 ms est un bon depart pour une recherche. Trop court : encore trop de requetes. Trop long : l'interface semble lente. Ajuste selon le feeling.

## A toi

Ajoute un debounce sur un champ input qui `console.log` la valeur. Tape vite. Verifie que le log n'apparait qu'apres une pause.
