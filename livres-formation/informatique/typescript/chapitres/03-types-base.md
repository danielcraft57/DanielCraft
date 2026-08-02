# Chapitre 3 - Les types de base

En JavaScript, tu as deja croise des **string**, **number**, **boolean**, plus `null` et `undefined`. TypeScript nomme ces formes explicitement pour que le compilateur puisse verifier. Une string, c'est du texte entre guillemets. Un number, c'est un nombre (entier ou decimal). Un boolean, c'est `true` ou `false`. Chez DanielCraft, on commence toujours par ces trois-la : ils couvrent 80 % des annotations debutantes. Lea type les libelles, Max type les totaux, Sam type les interrupteurs `actif` / `inactif`.

Il existe aussi `null` (vide volontaire) et `undefined` (pas encore defini). Tu les rencontreras surtout avec les unions et les optionnels plus tard. Pour l'instant, retiens : connaitre le type, c'est savoir ce que tu peux faire avec la boite. Tu ne fais pas `.toUpperCase()` sur un nombre. Tu ne multiplies pas deux booleans en esperant un prix. Le type n'est pas une decoration : c'est une promesse sur les operations autorisees.

:::retenir
string = texte. number = nombre. boolean = vrai/faux. Ces trois types portent deja beaucoup de code debutant.
:::

## Ce que ce n'est pas

Ce n'est pas encore les objets complexes, les tableaux, ni `any`. Ce n'est pas "tous les types du manuel" (tuple, enum, never...). Ce n'est pas non plus inventer des types fantaisie sans besoin. Et ce n'est pas croire que TypeScript change la valeur a l'execution : les types s'effacent au compile. Le runtime reste du JS. Lea le rappelle aux stagiaires : "apres `tsc`, il ne reste que du JavaScript honnete".

## Annoter pour sentir

```ts
let titre: string = "Devis plomberie";
let total: number = 120;
let paye: boolean = false;

// titre = 10; // erreur
// total = "cent"; // erreur
paye = true;
```

Lea ecrit parfois sans annotation quand l'inference suffit : `let ville = "Lyon"` est deja vu comme string. Mais pour apprendre, annoter a la main force le reflexe. Max annote toujours au debut. Sam alterne : "d'abord explicite, ensuite tu laisses inferer".

```ts
let score = 0; // infere : number
score = score + 1;
```

Tu peux aussi croiser les trois types dans une petite fiche :

```ts
const prenom: string = "Sam";
const sessions: number = 3;
const certifie: boolean = true;
console.log(prenom, sessions, certifie);
```

## Petite histoire

Max stockait un prix en string `"45"` puis tentait `prix * 1.2`. En JS, ca peut "marcher" bizarrement ou produire des surprises. En TS, si `prix` est `string`, le compilateur te regarde de travers selon le contexte. Il a passe `prix` en `number` et le calcul est devenu honnete. Lea a un tableau mental : texte pour afficher, nombre pour calculer, boolean pour brancher. Sam colle ce tableau au mur de la salle. DanielCraft adore ces cartes simples : elles evitent dix debates abstraites.

## Erreur classique

Confondre `number` et string numerique `"42"`. Utiliser `Boolean` (objet) au lieu de `boolean` (type primitif) par copie de doc. Ou typer tout en string "parce que c'est plus simple" et perdre les calculs. Autre piege : croire que `null` et `undefined` sont la meme chose. Proches, pas identiques. On y revient avec `|`.

:::attention
`"42"` est une string. `42` est un number. Pour calculer, tu veux le second. Pour afficher, le premier peut suffire.
:::

## En vrai

Dans la console TS (ou un fichier), declare trois variables : `prenom`, `age`, `inscrit` avec les bons types. Affiche-les. Tente une mauvaise assignation et lis le message. Note le mot-cle du type dans l'erreur : c'est ton vocabulaire. Puis change volontairement un type et regarde comment le message evolue. Ce petit jeu bat une page de theorie.

## Choisir le bon type

Devant une valeur, pose trois questions. Est-ce du texte a afficher ou concatener ? -> `string`. Est-ce une quantite a calculer ? -> `number`. Est-ce un interrupteur oui/non ? -> `boolean`. Si la reponse est "parfois texte, parfois nombre", tu n'es plus sur un type de base seul : tu vises une union (chapitre suivant sur `|`). Lea applique ce test en revue de code. Max l'ecrit encore sur un post-it. Sam le fait dire a voix haute avant d'annoter.

Les nombres en JavaScript / TypeScript ne distinguent pas entier et flottant comme certains langages. `1` et `1.5` sont tous deux `number`. Pour de l'argent, tu resteras prudent (arrondis), mais le type reste `number` au debut. Les booleans ne sont pas des strings `"true"`. Si tu lis un formulaire, tu convertis explicitement.

Enfin, souviens-toi : le type guide le compilateur. Il disparait au runtime. Ton `boolean` compile devient un vrai/faux JS classique. C'est pour ca que TS n'est pas "un autre moteur" : c'est un controleur avant le moteur.

## A toi

Ecris un mini "fiche contact" : `nom: string`, `telephone: string`, `age: number`, `clientActif: boolean`. Remplis avec tes valeurs. Change un type volontairement, corrige. Chez DanielCraft, cette fiche reviendra sous forme d'interface au chapitre 5. Garde le fichier : tu le reprendras.
