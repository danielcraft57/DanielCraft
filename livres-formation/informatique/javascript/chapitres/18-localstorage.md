# Chapitre 18 - Garder des infos (localStorage)

Des fois tu veux que ca reste apres un refresh.
`localStorage` range des textes dans le navigateur.

## Idee simple

```js
localStorage.setItem("prenom", "Nora");
const prenom = localStorage.getItem("prenom");
console.log(prenom);
```

## Attention

Ca stocke des **strings**.
Pour un nombre ou une liste, on passe souvent par JSON.

```js
const score = 12;
localStorage.setItem("score", String(score));

const lu = Number(localStorage.getItem("score"));
```

Pour un tableau :

```js
const taches = ["acheter du pain", "reviser JS"];
localStorage.setItem("taches", JSON.stringify(taches));

const retrouvees = JSON.parse(localStorage.getItem("taches") || "[]");
```

## Brancher sur la todo

Quand tu ajoutes une tache, sauvegarde la liste.
Au chargement, relis et reaffiche.

Pseudo-plan :
1. tableau `taches = []`
2. a chaque ajout : `push` + sauvegarde + rendu
3. au demarrage : charger + rendu

## Limites

- C'est local a ce navigateur
- L'utilisateur peut vider ses donnees
- Pas pour des secrets (mots de passe, etc.)

## A toi

Sauvegarde le score du compteur (chapitre 13) dans `localStorage`.
Au rechargement, le score revient.
Petit pouvoir. Gros effet "waouh".
