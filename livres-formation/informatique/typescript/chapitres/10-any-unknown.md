# Chapitre 10 - any et unknown

**`any`** desactive le typage pour une valeur : TypeScript arrete de verifier. C'est pratique pour "faire taire" une erreur, et dangereux pour la meme raison. **`unknown`** dit : je ne sais pas encore, tu devras prouver avant d'utiliser. Chez DanielCraft, on enseigne `any` comme une sortie de secours rare, pas comme un style de vie. Lea le bannit des APIs internes. Max a mis `any` partout un week-end et a retrouve les bugs JS qu'il fuyait. Sam ecrit au tableau : "`any` = je renonce. `unknown` = je reporterai la preuve."

```ts
let souple: any = "salut";
souple = 12;
souple.foo.bar; // TS ne proteste pas - crash possible au runtime

let prudent: unknown = "salut";
// prudent.toUpperCase(); // erreur : il faut narrowing
if (typeof prudent === "string") {
  console.log(prudent.toUpperCase());
}
```

Le contraste est volontairement brutal. Avec `any`, le filet tombe. Avec `unknown`, le filet reste, mais tu dois passer le garde. Si tu viens du narrowing, tu as deja le reflexe.

:::retenir
Evite `any`. Prefere un vrai type, une union, ou `unknown` + narrowing si tu ne sais pas encore.
:::

## Ce que ce n'est pas

Ce n'est pas "interdit a vie" : un proto jetable peut avoir un `any` temporaire. Ce n'est pas non plus `unknown` partout par snobisme. Ce n'est pas `Object` comme substitut magique. Et ce n'est pas laisser `noImplicitAny` off pour ne jamais apprendre. En mode `strict`, TS te pousse a preciser - c'est voulu. Lea accepte un `any` local avec un `TODO` date, pas un `any` dans une interface partagee.

## Quand tu touches une donnee floue

```ts
function lireTitre(data: unknown): string {
  if (
    typeof data === "object" &&
    data !== null &&
    "titre" in data &&
    typeof (data as { titre: unknown }).titre === "string"
  ) {
    return (data as { titre: string }).titre;
  }
  return "(sans titre)";
}
```

Pour debuter, tu n'as pas besoin de ce niveau de garde complet. L'idee compte : `unknown` t'oblige a demander. Lea simplifie souvent avec une interface des qu'elle connait la forme. Max parse du JSON (`JSON.parse` renvoie souvent `any` selon le contexte) puis valide les champs un a un. Sam prefere "valider puis typer" a "typer puis prier".

:::attention
`JSON.parse` ne "devine" pas ton interface. Valide ou annote apres preuve. Un `as MonType` naif sur du JSON est un `any` deguise.
:::

## Petite histoire

Un stagiaire de Lea avait mis `any` sur toute la reponse HTTP. La demo a plante sur `undefined.toFixed`. Elle a remplace par une interface `ApiDevis` + un check minimal. Max a cherche "comment desactiver TypeScript" apres trois erreurs ; Sam lui a montre comment les lire. Le lendemain, Max utilisait `unknown` sur une entree utilisateur et etait fier du `typeof`. DanielCraft celebre ce basculement : du silence achete au filet choisi.

## Erreur classique

`any` pour faire compiler la CI. `any` copie-colle dans une interface. Croire que `unknown` est inutilisable (il l'est, avec narrowing). Autre piege : `as any` en fin de ligne "juste pour aujourd'hui" qui reste six mois. Mets un commentaire `// TODO typer` si tu dois vraiment, et reviens.

:::astuce
Si tu tapes `any`, demande-toi : "quelle union ou interface dirait la meme chose en plus honnete ?"
:::

## En vrai

Declare `let x: any` et appelle une methode inventee : observe le silence de `tsc`. Remplace par `unknown`, ajoute un `typeof`, vois la difference. Garde le second reflexe. Puis tente `JSON.parse('{"a":1}')` et refuse de le traiter comme interface sans check.

## Sortir du flou sans mentir

Le vrai travail avec des donnees floues, c'est la validation. Tu recois un JSON, tu verifies les champs, tu construis un objet type. Lea ecrit parfois une fonction `parseClient(data: unknown): Client | null`. Max a voulu un seul `as Client` ; ca a casse en prod sur un champ renomme. Sam montre les deux versions cote a cote : le parse est plus long, le crash disparait.

`any` reste tentant dans les callbacks obscurs ou les libs mal typees. Isole-le. Ne le laisse pas contaminer toute ton appli : une variable `any` infecte souvent ce qu'elle touche. Prefere typer le resultat des que tu controls la forme.

Enfin, rappelle-toi le but du livre : coder plus sur. `any` annule ce but localement. Si tu l'utilises, sache que tu es repasse en mode JS nu a cet endroit. Parfois ok. Souvent non.

## A toi

Ecris une fonction `toNumber(v: unknown): number | null` qui renvoie le nombre si `typeof v === "number"`, sinon `null`. Teste avec `12`, `"12"`, `true`. Chez DanielCraft, cette fonction est un modele mental anti-`any`. Si `"12"` te demange, ajoute une branche `parseFloat` consciente - pas un `as number`.
