# Chapitre 9 - Narrowing (resserrer le type)

Le **narrowing**, c'est quand TypeScript comprend qu'a cet endroit du code, une union est devenue un type plus precis. Tu testes avec `typeof`, avec `if (valeur)`, avec une comparaison, et dans la branche le type se resserre. Chez DanielCraft, on presente ca comme un entonnoir : large a l'entree, etroit apres le garde. Lea ecrit `if (typeof id === "string")` avant d'appeler `.toUpperCase()`. Max a longtemps ignore les guards et forcait avec `as`. Sam refuse les `as` debutants : "prouve d'abord".

```ts
function labelId(id: string | number): string {
  if (typeof id === "string") {
    return id.toUpperCase(); // ici : string
  }
  return "N-" + id; // ici : number
}
```

Apres le `typeof === "string"`, TS sait que tu as une string. Dans le `else`, il reste le number. Tu n'as pas menti. Tu as filtre. Ce geste est le compagnon naturel des unions et des optionnels : sans lui, tu retombes dans le forcage ou dans le crash runtime.

:::retenir
Narrowing = prouver le type dans un `if` (souvent avec `typeof`) pour que TS autorise les operations sures.
:::

## Ce que ce n'est pas

Ce n'est pas de la magie runtime speciale TypeScript : ce sont des tests JS classiques que le compilateur lit. Ce n'est pas `as Type` (assertion). Ce n'est pas non plus obligatoire partout : si le type est deja precis, pas besoin. Et ce n'est pas un chapitre "avance interdit debutants" : c'est le geste quotidien des unions. Lea narrowing sans le nommer parfois : elle dit juste "je verifie avant".

## Guards utiles pour debuter

```ts
function afficherEmail(email: string | undefined): void {
  if (!email) {
    console.log("(pas d'email)");
    return;
  }
  console.log(email.toLowerCase()); // string
}

function taille(x: string | string[]): number {
  if (Array.isArray(x)) {
    return x.length;
  }
  return x.length; // string aussi a length, mais tu vois le pattern
}
```

Pour les optionnels, un simple `if (valeur)` narrow souvent vers la presence. Pour les objets, tu croiseras plus tard les type guards personnalises ; ici, `typeof` et tests de presence suffisent. Max a appris `Array.isArray` le jour ou une union string/tableau l'a bloque dix minutes.

:::astuce
Quand `tsc` dit qu'une propriete n'existe pas sur l'union, ajoute un `if`/`typeof` au lieu d'un `as`.
:::

## Petite histoire

Lea recevait `reponse: string | number` d'un vieux formulaire. Sans narrowing, `.trim()` cassait sur les nombres. Avec `typeof`, deux branches propres. Max affichait `contact.email` optionnel ; un `if (contact.email)` a fait disparaitre l'erreur et le crash. Sam projette le message d'erreur "Property does not exist" puis le `if` qui le soigne. La salle retient mieux que le jargon "narrowing". DanielCraft celebre le `if` qui prouve.

## Erreur classique

Utiliser `as string` pour faire taire l'erreur sans tester. Tester trop tard (apres l'appel dangereux). Oublier le `return` dans la branche d'echec et laisser TS confus. Autre piege : `typeof null` (curiosite JS) - pour debuter, prefere des unions claires et des tests de presence.

:::attention
`as` force. Narrowing prouve. Prefere prouver. Le forcage revient te mordre au runtime.
:::

## En vrai

Ecris `function describe(x: string | number)` qui log "texte: ..." ou "nombre: ...". Utilise `typeof`. Compile. Retire le `if`, observe l'erreur sur une methode string, remets. Note la difference de message : c'est ton professeur.

## Prouver avant d'agir

Le narrowing est le geste anti-crash par excellence. Tu ne demandes pas a TypeScript de "croire". Tu lui montres un test que JavaScript fera vraiment. `typeof`, `===`, `in`, `Array.isArray`, un simple `if (valeur)` : autant de preuves. Lea refuse les PR ou un `as` remplace un `if` de trois lignes. Max a gagne en confiance le jour ou il a ecrit un narrowing sans y penser. Sam fait effacer le `if` en live pour revoir l'erreur revenir : pedagogie brutale et efficace.

Attention aux fausses preuves. Un test trop large ne resserre pas. Un test apres l'usage dangereux arrive trop tard. Place le garde avant l'appel de methode. Structure souvent en early return : si invalide, message et `return` ; ensuite le type est sur.

Ce chapitre se relie a `unknown` : tu narrowing pour sortir de l'inconnu. Il se relie aux optionnels : tu narrowing pour prouver la presence. Une seule idee sous plusieurs syntaxes.

## A toi

Prends `interface User { nom: string; age?: number }`. Ecris `function ageLabel(u: User): string` qui renvoie `"age inconnu"` ou `"N ans"` apres narrowing sur `u.age`. Chez DanielCraft, ce reflexe est le compagnon naturel des unions. Si tu reussis, tu es pret pour `unknown` au chapitre suivant.
