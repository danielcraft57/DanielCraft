# Chapitre 4 - Les types simples

Les valeurs n'ont pas toutes la meme "forme".

## Texte (string)

```js
const phrase = "Bonjour";
const autre = 'Hey';
```

Guillemets doubles ou simples, les deux marchent.
Reste coherent dans un fichier.

## Nombre (number)

```js
const prix = 19.99;
const quantite = 3;
const total = prix * quantite;
```

## Vrai / faux (boolean)

```js
const estConnecte = true;
const aFini = false;
```

Utile pour les decisions.

## undefined et null (juste savoir)

`undefined`, c'est "pas encore defini". `null`, c'est volontairement "vide". Pas besoin d'en faire des tartines au debut : sache juste que ces deux etats existent.

## Assembler du texte

```js
const prenom = "Maya";
console.log("Salut " + prenom);
console.log(`Salut ${prenom}`); // plus moderne, pratique
```

Les backticks \` \` permettent d'inserer `${...}` dedans.

## A toi

Fais un mini ticket de caisse. Range le prix d'un article, la quantite, calcule le total, puis affiche un message du genre "Total = ...". Tu dois voir le calcul et le texte dans la console.

## Erreur classique

Tu additionnes un nombre et du texte sans faire attention. JS colle les morceaux au lieu de calculer.

Mauvais :

```js
const total = "19" + 3; // "193" (texte)
```

Bon :

```js
const total = 19 + 3; // 22 (nombre)
```

Ou convertis avec `Number("19")` si la valeur vient d'un champ texte.

## Exemple complet

```js
// Mini facture
const client = "Maya";
const article = "Casque";
const prixUnitaire = 29.99;
const quantite = 2;
const tauxTva = 0.2;

// Calculs
const sousTotal = prixUnitaire * quantite;
const montantTva = sousTotal * tauxTva;
const totalTTC = sousTotal + montantTva;

// Message avec template literal
const recu = `
Facture pour ${client}
- ${quantite} x ${article} : ${sousTotal.toFixed(2)} EUR
- TVA : ${montantTva.toFixed(2)} EUR
= Total : ${totalTTC.toFixed(2)} EUR
`;

console.log(recu);
```

`.toFixed(2)` arrondit a 2 decimales. Pratique pour l'argent.

## Mini defi

Cree une variable texte, une nombre, et une booleenne. Affiche le type de chaque valeur avec `typeof maVariable`. Fais un calcul prix fois quantite, puis un message avec des backticks. Enfin, teste `"5" + 2` et `5 + 2`, et note bien la difference : l'un colle du texte, l'autre calcule.

## A retenir

Une string, c'est du texte. Un number, c'est un nombre. Un boolean, c'est `true` ou `false`. Pour comparer sans melanger les types, utilise `===`. Les backticks \`...\` avec `${...}` simplifient l'assemblage de texte. Et attention aux guillemets : ils peuvent transformer un nombre en texte sans que tu le voies.


## En vrai, sur le terrain

Ouvre la console. Retape l'exemple a la main.
Change une valeur. Regarde ce qui bouge. C'est comme ca que ca rentre.

## Mini defi

Inventes un tout petit cas perso (ton prenom, ton score, ton jeu prefere).
Repars de l'exemple avec TES donnees. Si ca marche, c'est bon signe.
