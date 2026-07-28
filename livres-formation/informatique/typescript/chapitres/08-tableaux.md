# Chapitre 8 - Tableaux types

Un **tableau** type dit ce qu'il contient : `number[]` ou `Array<number>`. Les deux formes marchent ; `number[]` est courte et courante. Chez DanielCraft, on type les listes des le debut parce que c'est la que les melanges arrivent : un prix string au milieu de nombres, un todo sans `id`. Lea ecrit `lignes: DevisLigne[]`. Max a longtemps pousse n'importe quoi dans `let liste = []` ; en strict, TS demande souvent de preciser. Sam fait remplir un tableau homogene au tableau avant le code.

```ts
const notes: number[] = [12, 15, 18];
notes.push(14);
// notes.push("bien"); // erreur

const prenoms: string[] = ["Lea", "Max", "Sam"];
```

Tu peux typer un tableau d'objets avec une interface :

```ts
interface TodoItem {
  id: number;
  texte: string;
  fait: boolean;
}

const todos: TodoItem[] = [
  { id: 1, texte: "Compiler", fait: true },
  { id: 2, texte: "Annoter", fait: false },
];
```

Une liste typee, c'est aussi de l'autocompletion : sur `todos[0].`, l'editeur propose `id`, `texte`, `fait`. Lea adore ce confort. Max a cesse de chercher "c'etait `title` ou `texte` ?" dans trois fichiers.

:::retenir
`Type[]` = liste d'elements de ce type. Homogene autant que possible.
:::

## Ce que ce n'est pas

Ce n'est pas un objet (les index sont numeriques, ordres). Ce n'est pas une union magique `(string | number)[]` a utiliser partout : possible, mais souvent signe que le modele est flou. Ce n'est pas `any[]` "pour aller vite". Et ce n'est pas oublier que `push` doit respecter le type des elements. Sam dit : "si tu melanges, c'est souvent deux listes qui se cachent".

## Lire et transformer

```ts
function moyenne(notes: number[]): number {
  if (notes.length === 0) {
    return 0;
  }
  let somme = 0;
  for (const n of notes) {
    somme += n;
  }
  return somme / notes.length;
}

const m = moyenne([10, 12, 14]);
```

Lea type le parametre `notes: number[]` et le retour. Max a decouvert que `todos.filter(...)` garde souvent un type coherent. Sam insiste sur le cas liste vide : decide un comportement (0, erreur, message) au lieu de laisser `NaN`. Chez DanielCraft, gerer le vide fait partie du typage autant que le `[]` lui-meme.

:::astuce
Si ta liste peut etre vide, gere `length === 0` avant de diviser ou de prendre `[0]`.
:::

## Petite histoire

Max melangeait ids number et string dans un meme tableau "parce que l'API...". En TS, il a choisi `string[]` et normalise tout en string a l'entree. Moins heroique, plus stable. Lea a type `Produit[]` et a vu l'autocompletion proposer `prix` partout. Sam montre aux eleves l'erreur `push` d'un mauvais type : le "ah" collectif revient a chaque promo. Une seule erreur de `push`, et le message devient pedagogique.

## Erreur classique

Declarer `let items = []` sans type puis empiler des formes differentes. Utiliser `Array` sans parametre. Croire que `todos[0]` est toujours defini (il peut etre `undefined` si vide). Autre piege : tableau de `any` pour "passer". DanielCraft refuse ce raccourci en formation. Prefere annoter des le `const`.

:::attention
Acceder a `liste[0]` sur une liste peut-etre vide : verifie la longueur ou assume le risque consciemment.
:::

## En vrai

Cree `const prix: number[] = [4.5, 10, 2]`. Calcule la somme dans une fonction typee. Ajoute un produit via `push`. Tente un `push` de string, lis l'erreur. Puis filtre les prix superieurs a 5 et observe que le resultat reste `number[]`.

## Listes et coherence

Une liste typee protege surtout la coherence des elements. Si tu pushes un objet incomplet dans `TodoItem[]`, `tsc` rale tout de suite. Lea adore ca en atelier : le stagiaire voit l'oubli `fait` avant la demo. Max poussait des shapes differentes "temporairement" ; le temporaire restait. Sam impose un seul type d'element par liste debutante.

Tu croiseras `readonly Type[]` plus tard pour interdire `push`. Pas besoin maintenant. Tu croiseras aussi les tuples `[string, number]`. Pas besoin non plus pour un compteur ou une todo. Reste sur `Type[]` tant que ta liste est vraiment une liste ouverte.

Quand tu filtres, le type reste souvent `Type[]`. Quand tu maps vers autre chose, le type de sortie change : `todos.map(t => t.texte)` donne `string[]`. Observe l'inference. Si elle te surprend, annote le resultat. Chez DanielCraft, observer l'inference est une competence, pas de la paresse.

## A toi

Modele `TodoItem[]` avec trois taches. Ecris `function restantes(todos: TodoItem[]): TodoItem[]` qui renvoie celles ou `fait === false`. Affiche le resultat. Chez DanielCraft, ce pattern liste + filtre revient dans le mini-projet. Garde le fichier pour le chapitre 13.
