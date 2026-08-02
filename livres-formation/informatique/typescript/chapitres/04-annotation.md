# Chapitre 4 - Annoter une variable (: type)

L'**annotation** de type, c'est le `: type` apres le nom. Tu ecris `let score: number = 0`. Tu dis au compilateur : cette boite ne doit contenir que des nombres. Si plus tard tu fais `score = "dix"`, TypeScript refuse. Chez DanielCraft, on traite l'annotation comme une etiquette honnete sur un carton : pas de surprise a l'ouverture. Lea annote les entrees importantes. Max annote tout au debut pour apprendre. Sam montre aussi l'**inference** : parfois TS devine tout seul.

Deux styles cohabitent. Style explicite : tu ecris le type. Style inference : tu initialises clairement et TS deduit. Les deux sont valides. Pour debuter, explicite aide a voir le contrat. Ensuite, tu laisses inferer quand c'est evident. L'annotation brille surtout sur les parametres de fonctions et les valeurs qui changent au fil du script.

:::retenir
`: type` annonce le contrat de la variable. Le compilateur refuse ce qui casse le contrat.
:::

## Ce que ce n'est pas

Ce n'est pas obligatoire sur chaque ligne. Ce n'est pas une decoration "pro". Ce n'est pas non plus `as any` pour faire taire l'erreur. Et ce n'est pas changer le type a l'execution : apres compile, l'annotation disparait. Le JS restant n'a plus le `: number`.

## Syntaxe claire

```ts
let message: string = "Bonjour";
let compteur: number = 0;
const PI: number = 3.14;
let pret: boolean = false;

compteur = compteur + 1;
// compteur = "un"; // erreur de compilation
```

Avec `const`, la valeur ne change pas, mais le type reste utile pour documenter. Lea prefere `const` des que possible, comme en JS. Max a trop utilise `let` partout ; Sam l'a ramene a `const` + annotation.

```ts
const ville = "Lyon"; // string infere
let etape: string;
etape = "paiement"; // ok
// etape = 3; // erreur
```

Tu peux declarer sans valeur initiale si tu annotes : TypeScript sait deja la forme attendue. Sans annotation et sans valeur, c'est plus flou - evite.

:::astuce
Si tu declares sans initialiser, annote. Sinon initialise clairement pour laisser inferer.
:::

## Petite histoire

Lea avait une variable `statut` qui passait de `"ok"` a `1` selon les branches. En JS, silence. En TS avec `statut: string`, le `1` a ete refuse. Elle a cree une union plus tard (`"ok" | "ko"`). Mais le premier cran, c'etait l'annotation simple. Max a annote `total: number` et a vu disparaitre trois bugs de concatenation `"10" + 5`. Sam projette avant/apres : la salle comprend mieux qu'avec un discours sur "le systeme de types".

## Erreur classique

Annoter `any` partout "pour que ca compile". Reannoter une inference evidente en empilant du bruit. Oublier que `let x;` sans type ni valeur devient facilement problematique en mode strict. Autre piege : confondre annotation (`: string`) et assertion forcee (`as string`). La premiere demande une vraie verification. La seconde dit "fais-moi confiance" - a utiliser avec parcimonie, rarement en debutant.

:::attention
`as string` n'est pas une annotation pedagogique. Prefere `: string` et des valeurs coherentes. Le forcage cache les vrais problemes.
:::

## En vrai

Prends trois `let` de ton dernier script JS. Ajoute des annotations. Compile. Si une erreur apparait, celebre : tu as trouve un flou. Corrige la valeur ou le type, pas le silence.

## Ou annoter en priorite

Annoter partout fatigue et ajoute du bruit. Annoter nulle part laisse le flou. Le bon milieu debutant : parametres de fonctions, variables d'etat qui vivent longtemps (`score`, `todos`), valeurs qui traversent plusieurs fonctions. Lea annote les frontieres. Max annote aussi les locales le temps d'apprendre, puis allege. Sam dit : "si tu hesites sur le type, c'est peut-etre que la variable fait trop de choses".

L'inference n'est pas ton ennemie. `const n = 3` est clairement un number. Tu n'as pas besoin de `const n: number = 3` sauf pour pedagogie. En revanche, `let data;` sans valeur est un piege : precise le type ou initialise tout de suite. En mode strict, TypeScript te pousse dans ce sens. Accepte la pression : elle remplace des bugs plus tard.

Quand une annotation et une valeur se contredisent, crois le compilateur. Soit tu as menti sur le type, soit tu as mis la mauvaise valeur. Corrige l'un des deux, pas le message avec un `as`.

## A toi

Ecris :

```ts
let titre: string;
let pages: number;
let publie: boolean;
```

Assigne des valeurs coherentes, puis tente une mauvaise assignation sur chacune. Lis les trois messages. Note le pattern. Chez DanielCraft, lire l'erreur fait partie du typage autant que l'ecrire.
