# Chapitre 7 - Les fonctions (des recettes reutilisables)

Une **fonction**, c'est une recette. Tu la definis une fois. Tu l'appelles quand tu veux. Tu copies moins. Tu corriges a un seul endroit. Ton code devient plus clair parce que chaque morceau a un nom qui dit ce qu'il fait. Chez DanielCraft, on prefere plusieurs petites fonctions a une usine de soixante lignes que personne n'ose toucher. Lea decoupe "calculer", "afficher", "valider". Max a compris le jour ou il a corrige un total de devis a un seul endroit au lieu de trois. Sam refuse les "fonctions fourre-tout" dans les copies : une fonction, une mission.

Les parametres sont les ingredients. Le **`return`**, c'est le gateau sorti du four. `console.log` dans la cuisine, ce n'est pas la meme chose que donner le gateau a table. Lea dit : "log pour toi, return pour le programme". Sam projette les deux versions cote a cote en cours. Le "ah" collectif quand `undefined` apparait sans `return`. Ensuite, plus personne ne confond afficher et renvoyer.

```js
function direSalut() {
  console.log("Salut !");
}
direSalut();
direSalut();
```

Avec des **parametres** (ingredients) : `direSalutA("Nora")`. Avec un resultat : **`return`**. Sans `return`, tu recuperes souvent `undefined` si tu attendais une valeur. Ce n'est pas un bug du navigateur. C'est toi qui as oublie de rendre le gateau. Lea le repete : log pour toi, return pour le programme.

:::retenir
Ecrire une fonction ne suffit pas : il faut l'appeler. Et si tu as besoin du resultat, il faut un `return`.
:::

## Ce que ce n'est pas

Ce n'est pas obligatoire d'ecrire des fleches `=>` tout de suite : **`function`** suffit largement pour debuter. Ce n'est pas "une fonction = tout le programme" : decoupe. Ce n'est pas oublier d'appeler : une fonction ecrite mais jamais appelee ne fait rien, comme une recette jamais cuisinee. Et ce n'est pas `return` optionnel quand tu as besoin du resultat. **`console.log`** dans la cuisine, ce n'est pas la meme chose que donner le gateau a table.

Max a mis six mois a vraiment sentir la difference entre afficher et renvoyer. Toi, tu peux la sentir ce chapitre avec un petit test volontaire.

## Parametres et return

```js
function direSalutA(prenom) {
  console.log("Salut " + prenom);
}

function double(n) {
  return n * 2;
}
const resultat = double(4); // 8
```

Petite forme moderne a reconnaitre : `const triple = (n) => n * 3;`. Pour l'instant, `function` suffit largement. Tu croiseras les fleches plus tard sans panique. Lea les utilise parfois pour des callbacks courts. Max reste sur `function` pour l'instant. Sam montre les deux sans imposer.

## Petite histoire

Lea avait copie le meme calcul de moyenne trois fois dans un script client. Un bug, trois corrections. Elle a fait `moyenne(a, b, c)`. Un fix. Le client n'a jamais su qu'il y avait eu un mini drame derriere la facture qui s'affichait enfin correctement.

Max ecrivait des fonctions sans `return` et affichait `undefined` en croyant a un bug du navigateur. Sam projette les deux versions cote a cote. Le "ah" collectif. Ensuite, plus personne ne confond afficher et renvoyer. C'est un de ces moments ou une ligne de code change ta facon de lire le reste du livre.

## Erreur classique

```js
function carre(n) {
  n * n; // resultat perdu
}
function carreOk(n) {
  return n * n;
}
```

Oublier d'appeler. Donner trop de responsabilites a une seule fonction. Nommer `fonction1`. Autre piege : appeler avec `()` trop tot dans un `addEventListener` (on y revient au chapitre evenements). Lea garde une regle : si ta fonction fait plus de quinze lignes, decoupe. `moyenne(12, 16)` renvoie `14`. Tu ranges le resultat dans une variable, puis tu l'affiches. Calcul et affichage restent separes.

:::attention
Sans `return`, tu recuperes `undefined` si tu attendais une valeur. Ce n'est pas le navigateur qui est bete : c'est toi qui as oublie de rendre le resultat.
:::

## Exemple complet

```js
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
  console.log(prenom + " : " + moy.toFixed(1) + "/20 - " + mention(moy));
}
afficherBulletin("Leo", 12, 15, 18);
```

Trois fonctions, trois roles. `moyenne` calcule. `mention` decide. `afficherBulletin` assemble. C'est le modele DanielCraft : petit, clair, testable. Tu peux tester `moyenne` seule sans toucher au reste.

## En vrai

Ecris `moyenne(a, b)` pour 12 et 16. Verifie le resultat dans la console. Puis retire le `return` une seconde : observe `undefined`. Remets. Le contraste enseigne mieux qu'un paragraphe de theorie. Lea le fait systematiquement. Max a mis six mois a vraiment sentir la difference : toi, tu la sens ce chapitre.

## A toi

Ecris `aireRectangle(largeur, hauteur)` avec return. `estMajeur(age)` qui renvoie un boolean. `saluer(prenom)` qui affiche sans return. Appelle les trois. Note en deux phrases la difference return vs log. Competence pilote pour la suite du livre : sans ca, tu confondras encore affichage et resultat. Chez DanielCraft, on separe les roles des le debut.
