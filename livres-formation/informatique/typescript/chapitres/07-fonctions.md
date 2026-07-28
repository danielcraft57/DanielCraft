# Chapitre 7 - Fonctions typees

Une **fonction** typee annonce le type de ses parametres et souvent le type de retour. Tu ecris `function double(n: number): number`. Le contrat est visible : entre un nombre, ressort un nombre. Chez DanielCraft, c'est le meilleur endroit pour annoter, parce que les bugs aiment se cacher dans les appels. Lea type toutes les entrees publiques. Max a compris `return` + type de retour le jour ou `tsc` a refuse un `return "ok"` dans une fonction `: number`. Sam separe encore `console.log` (effet) et `return` (valeur).

```ts
function direSalutA(prenom: string): void {
  console.log("Salut " + prenom);
}

function moyenne(a: number, b: number): number {
  return (a + b) / 2;
}

const m = moyenne(12, 16);
```

`void` signifie : pas de valeur utile renvoyee (souvent pour les fonctions qui affichent seulement). Sans annotation de retour, TypeScript infere souvent correctement. Explicite reste pedagogique. Quand tu partages une fonction avec quelqu'un d'autre, le type de retour lit comme une notice.

:::retenir
Type les parametres d'abord. Le type de retour documente ce que l'appelant recoit.
:::

## Ce que ce n'est pas

Ce n'est pas obligatoire d'annoter le retour si l'inference est evidente - mais c'est utile pour apprendre. Ce n'est pas une fleche `=>` obligatoire : `function` suffit. Ce n'est pas `Function` (type trop large). Et ce n'est pas oublier d'appeler : une fonction typee non appelee ne fait toujours rien. Lea dit : "un contrat sans appel, c'est une promesse non tenue".

## Parametres optionnels et defauts

```ts
function saluer(prenom: string, titre?: string): string {
  if (titre) {
    return titre + " " + prenom;
  }
  return prenom;
}

function clamp(n: number, max: number = 100): number {
  return n > max ? max : n;
}
```

Le `?` sur un parametre le rend facultatif. Une valeur par defaut (`= 100`) aussi, avec une nuance : le defaut fournit une vraie valeur. Lea utilise les defauts pour les seuils. Max prefere parfois deux fonctions courtes plutot qu'un parametre optionnel obscur. Sam rappelle l'ordre : parametres obligatoires d'abord, optionnels ensuite.

:::astuce
Si un parametre est souvent absent, donne un defaut clair. Si son absence change vraiment le comportement, garde `?` et un `if`.
:::

## Petite histoire

Lea avait `calculerTotal(lignes)` sans types. Un stagiaire passait une string. Le total devenait absurde. Avec `lignes: { prix: number; qte: number }[]` et un retour `number`, l'editeur a bloque l'appel foireux. Max a type `estMajeur(age: number): boolean` et a cesse de renvoyer `"oui"`. Sam applaudit les fonctions courtes : une mission, un retour clair. Chez DanielCraft, une signature lisible vaut un paragraphe de commentaire.

## Erreur classique

Annoter le retour `number` puis `return` sans valeur (ou return string). Oublier le type d'un parametre et se retrouver avec `any` implicite selon la config. Donner trop de responsabilites a une seule fonction typee "usine". Autre piege : confondre `void` et `undefined`. Pour debuter, `void` = "je n'utilise pas le retour".

:::attention
Si tu annonces `: number` et que tu rates le `return`, TypeScript te le dit. Ecoute-le : c'est exactement le filet voulu.
:::

## En vrai

Ecris `aireRectangle(largeur: number, hauteur: number): number`. Teste. Retire un `return`, lis l'erreur, remets. Puis ajoute `estMajeur(age: number): boolean`. Appelle les deux depuis un petit `main` mental : entrees claires, sorties claires.

## Signatures comme documentation

La signature d'une fonction typee est une doc courte qui ne ment pas. `moyenne(a: number, b: number): number` dit tout. Lea lit les signatures avant le corps en revue. Max a commence a ecrire la signature d'abord, puis le corps : ca l'oblige a clarir l'intention. Sam refuse les fonctions `faireTout(data: any): any` en copie.

Pense aussi aux fonctions pures vs effets. Une fonction qui calcule et `return` est facile a typer et a tester mentalement. Une fonction qui touche le DOM en plus melange les roles. Dans le mini-projet, `add` change l'etat, `render` affiche. Types simples des deux cotes. Chez DanielCraft, cette separation est une pratique autant qu'une affaire de types.

Si le retour est une union (`string | null`), documente-le. L'appelant saura qu'il doit narrowing. Cacher un `null` possible derriere un mensonge `: string` revient au chapitre optionnels : contrat deshonnete.

## A toi

Ecris `function labelProduit(nom: string, prix: number): string` qui renvoie `"nom - prix EUR"`. Ecris `function logErreur(msg: string): void`. Appelle les deux. Note return vs void. Chez DanielCraft, ce reflexe porte tout le reste du livre. Si tu bloques, relis seulement les signatures avant le corps.
