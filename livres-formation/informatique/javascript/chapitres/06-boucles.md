# Chapitre 6 - Les boucles (repete sans te fatiguer)

Une **boucle**, c'est faire la meme chose plusieurs fois sans copier-coller quarante lignes identiques. Afficher une table de multiplication. Parcourir une liste de prenoms. Compter de 1 a 100. Repeter tant qu'une condition reste vraie. Chez DanielCraft, on aime les boucles parce qu'elles revelent tout de suite si tu comprends le compteur - ou si tu crees une boucle infinie qui freeze le navigateur. Lea les utilise pour generer des listes de tags sur les pages clients. Max pour numeroter des etapes sur sa page devis. Sam pour les tables de multiplication en cours. Trois usages, une meme logique : le compteur doit avancer.

Une boucle, c'est une machine. Tu regles le debut, la fin, le pas. Ou tu dis "continue tant qu'il reste des vies". Si tu n'enleves jamais de vie, la machine ne s'arrete pas. Lea appelle ca "oublier le frein". Max a vu Chrome geler une fois sur sa page plomberie. Il n'oublie plus d'incrementer. Sam chronometre en cours : "qui trouve l'oubli ?". Les eleves deviennent des chasseurs de freins.

```js
for (let i = 1; i <= 5; i = i + 1) {
  console.log("Tour numero " + i);
}
```

Lecture : commence a 1, tant que `i <= 5`, a chaque tour ajoute 1. Le **`while`** repete tant qu'une condition reste vraie. Attention : si tu oublies de faire evoluer la condition, boucle infinie. Le navigateur rale. Toi aussi. Coupe l'onglet, respire, ajoute le frein. Max l'a vecu une fois. Il n'oublie plus.

:::retenir
Boucle = repeter avec un compteur qui avance. Oublie le frein = page freeze. Nombre de tours connu -> `for`. "Tant que" -> `while`.
:::

## Ce que ce n'est pas

Ce n'est pas encore `map` / `filter` (plus tard, quand les tableaux seront familiers). Ce n'est pas "while partout" : si tu connais le nombre de tours, **`for`** est souvent plus clair. Ce n'est pas une excuse pour ne pas penser : une boucle mal bornee freeze la page et te fait perdre ton travail non sauvegarde. Et ce n'est pas "copier-coller dix `console.log`" : la boucle existe precisement pour eviter ca.

Sam dit aux eleves : une boucle, c'est une machine. Si tu ne regles pas le frein, la machine ne s'arrete pas. Ce n'est pas une metaphore jolie. C'est la realite du code.

## while et parcours de liste

```js
let vies = 3;
while (vies > 0) {
  console.log("Il reste " + vies + " vies");
  vies = vies - 1;
}

const fruits = ["pomme", "banane", "kiwi"];
for (const fruit of fruits) {
  console.log(fruit);
}
```

`for...of` parcourt un tableau simplement. On creuse les tableaux au chapitre 8. Pour debuter, c'est souvent le plus lisible : tu dis "pour chaque fruit, affiche-le". Pas besoin de gerer l'index a la main.

:::attention
Dans un `while`, verifie toujours que quelque chose change a chaque tour. Sinon : boucle infinie, page freeze.
:::

## Petite histoire

Max a freeze Chrome avec un `while` ou il affichait `i` sans l'incrementer. Il a coupe l'onglet, un peu pale, puis a compris. Lea montre toujours ou le compteur avance avant de lancer la boucle. Sam chronometre : "qui trouve l'oubli en moins de trente secondes ?". Les eleves deviennent des chasseurs de freins. L'erreur devient un reflexe a chercher, pas une humiliation devant la classe.

Lea, elle, utilise les boucles pour generer des menus de navigation sur les sites clients : dix liens, une boucle, pas dix lignes copiees. Max numerote ses etapes de devis. Sam fait calculer la somme de 1 a 100 en classe. Quand quelqu'un obtient 5050, la boucle devient concrete.

## Erreur classique

```js
let i = 0;
while (i < 5) {
  console.log(i);
  // oubli de i = i + 1
}
```

Corrige en faisant evoluer `i`. Autre piege : commencer a 1 ou a 0 selon le besoin, et se tromper sur la borne `<=` vs `<`. Affiche le compteur. Compte a la main une fois. Ca clarifie. Lea trace la boucle sur papier avant de coder quand c'est un peu complique. Si tu hesites entre `for` et `while` : nombre de tours connu -> `for`. "Tant que" une condition -> `while`.

## Exemple complet

```js
const mots = ["le", "chat", "dort", "sur", "tapis"];
let compteur = 0;
for (const mot of mots) {
  if (mot.length >= 4) {
    compteur = compteur + 1;
    console.log(mot + " compte !");
  }
}
console.log("Total mots longs : " + compteur);

for (let n = 1; n <= 10; n = n + 1) {
  console.log("3 x " + n + " = " + (3 * n));
}
```

Tu melanges boucle, condition et compteur. C'est le trio qui reviendra partout dans le livre. Lis ligne par ligne. Sens le rythme. Puis modifie un nombre et relance.

## En vrai

Affiche la table de 7 (7x1 a 7x10) avec un `for`. Puis les pairs de 2 a 20. Deux boucles, deux victoires. Si tu freeze, cherche le frein avant de tout recommencer : ou le compteur devrait avancer ? Ajoute-le. Relance. Tu as appris plus qu'avec une page de theorie. Sam chronometre ce geste en classe. Max l'a appris une fois pour toutes.

## A toi

Calcule la somme de 1 a 100 (tu dois obtenir 5050). Parcours un tableau de prenoms avec "Salut, ...". Bonus : arrete si tu trouves `"stop"`. Ecris ta phrase anti-boucle-infinie sur un post-it. Reflexe DanielCraft : toujours montrer ou le compteur avance, avant de lancer la boucle. Tu prepares les tableaux du chapitre suivant avec un sol solide.
