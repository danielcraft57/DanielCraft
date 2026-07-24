# Chapitre 5 - Les conditions (if)

Parfois tu veux : "si ca, alors ca".

## if / else

```js
const age = 15;

if (age >= 18) {
  console.log("Majeur");
} else {
  console.log("Mineur");
}
```

## else if

```js
const note = 14;

if (note >= 16) {
  console.log("Excellent");
} else if (note >= 10) {
  console.log("C'est valide");
} else {
  console.log("On revise");
}
```

## Comparaisons utiles

- `===` egal (strict, recommande)
- `!==` different
- `>` `<` `>=` `<=`

Evite `==` pour l'instant. `===` est plus clair.

## Et / Ou

```js
const aUnTicket = true;
const estVip = false;

if (aUnTicket || estVip) {
  console.log("Tu peux entrer");
}

if (aUnTicket && estVip) {
  console.log("Acces premium");
}
```

`||` = ou
`&&` = et

## A toi

Demande-toi (en dur dans le code) un `motDePasse`.
Si c'est `"secret123"`, affiche "OK".
Sinon "Refuse".

## Erreur classique

Tu utilises `=` au lieu de `===` dans un `if`. `=` donne une valeur. `===` compare.

Mauvais :

```js
if (motDePasse = "secret123") { // assigne, ne compare pas !
  console.log("OK");
}
```

Bon :

```js
if (motDePasse === "secret123") {
  console.log("OK");
}
```

## Exemple complet

```js
// Controle d'acces simple
const age = 16;
const aInvitation = true;
const estBlackliste = false;

function peutEntrer(age, invitation, blackliste) {
  if (blackliste) {
    return "Acces refuse : compte bloque";
  }
  if (age < 13) {
    return "Acces refuse : trop jeune";
  }
  if (age >= 18 || invitation) {
    return "Bienvenue !";
  }
  return "Acces refuse : invitation requise";
}

console.log(peutEntrer(age, aInvitation, estBlackliste));
console.log(peutEntrer(10, true, false));
console.log(peutEntrer(20, false, false));
```

Teste en changeant les valeurs en haut du fichier.

## Mini defi

- Cree une variable `temperature`
- Si >= 25, affiche "Chaud"
- Sinon si >= 15, affiche "Correct"
- Sinon affiche "Froid"
- Ajoute un cas : si temperature > 35, affiche "Canicule !"

## A retenir

- `if` / `else if` / `else` = decisions en chaine
- `===` pour comparer, pas `=`
- `&&` = et, `||` = ou
- Garde les conditions simples et lisibles


## En vrai, sur le terrain

Ouvre la console. Retape l'exemple a la main.
Change une valeur. Regarde ce qui bouge. C'est comme ca que ca rentre.

## Mini defi

Inventes un tout petit cas perso (ton prenom, ton score, ton jeu prefere).
Repars de l'exemple avec TES donnees. Si ca marche, c'est bon signe.
