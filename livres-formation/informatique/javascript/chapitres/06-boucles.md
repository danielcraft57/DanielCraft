# Chapitre 6 - Les boucles (repete sans te fatiguer)

Une boucle = faire la meme chose plusieurs fois.
Sans copier-coller 40 lignes.

## for (classique)

```js
for (let i = 1; i <= 5; i = i + 1) {
  console.log("Tour numero " + i);
}
```

Lecture :
1. commence a 1
2. tant que `i <= 5`
3. a chaque tour, ajoute 1

## while

```js
let vies = 3;

while (vies > 0) {
  console.log("Il reste " + vies + " vies");
  vies = vies - 1;
}
```

Attention : si tu oublies de faire baisser `vies`, boucle infinie.
Le navigateur va raler. Toi aussi.

## Boucler sur une liste (aperçu)

```js
const fruits = ["pomme", "banane", "kiwi"];

for (const fruit of fruits) {
  console.log(fruit);
}
```

On creusera les tableaux juste apres.

## A toi

Affiche la table de 7 (de 7x1 a 7x10) avec une boucle `for`.

## Erreur classique

Tu oublies d'avancer le compteur dans une boucle `while`. Le programme tourne a l'infini. Le navigateur freeze.

Mauvais :

```js
let i = 0;
while (i < 5) {
  console.log(i);
  // oubli de i = i + 1
}
```

Bon :

```js
let i = 0;
while (i < 5) {
  console.log(i);
  i = i + 1;
}
```

## Exemple complet

```js
// Compter les mots de 4 lettres ou plus
const mots = ["le", "chat", "dort", "sur", "tapis"];
let compteur = 0;

for (const mot of mots) {
  if (mot.length >= 4) {
    compteur = compteur + 1;
    console.log(mot + " compte !");
  }
}

console.log("Total mots longs : " + compteur);

// Table de multiplication 3
console.log("--- Table de 3 ---");
for (let n = 1; n <= 10; n = n + 1) {
  console.log("3 x " + n + " = " + (3 * n));
}
```

`.length` donne la taille d'un texte. Pratique dans les boucles.

## Mini defi

- Affiche les nombres pairs de 2 a 20 avec une boucle `for`
- Fais la somme de 1 a 100 (resultat attendu : 5050)
- Parcours un tableau de prenoms et affiche "Salut, [prenom] !"
- Bonus : arrete la boucle si tu trouves "stop" dans la liste

## A retenir

- `for` = quand tu connais le nombre de tours
- `while` = tant qu'une condition est vraie
- `for...of` = parcourir un tableau simplement
- Toujours faire evoluer le compteur pour eviter l'infini


## En vrai, sur le terrain

Ouvre la console. Retape l'exemple a la main.
Change une valeur. Regarde ce qui bouge. C'est comme ca que ca rentre.

## Mini defi

Inventes un tout petit cas perso (ton prenom, ton score, ton jeu prefere).
Repars de l'exemple avec TES donnees. Si ca marche, c'est bon signe.
