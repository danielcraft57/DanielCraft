# Chapitre 6 - Unions et optionnels (| et ?)

Parfois une valeur peut etre **soit** une chose **soit** une autre. C'est une **union** : `string | number`. Parfois une propriete peut etre absente. C'est l'**optionnel** : `email?: string`. Chez DanielCraft, ces deux outils evitent le mensonge du "toujours present, toujours le meme type". Lea type un id comme `number | string` quand l'API est capricieuse. Max marque `telephone?` sur ses contacts incomplets. Sam dit : "l'union dit les choix. Le point d'interrogation dit le droit a l'absence."

```ts
let id: number | string;
id = 12;
id = "abc-12";
// id = true; // erreur

interface Contact {
  nom: string;
  email?: string;
}

const a: Contact = { nom: "Lea" };
const b: Contact = { nom: "Max", email: "max@ex.com" };
```

Avant d'utiliser `email`, tu verifies qu'il existe. Avant de traiter `id` comme un nombre, tu verifies le type. C'est le pont vers le narrowing du chapitre 9. Sans ces deux outils, tu serais tente d'inventer des valeurs fantomes ("") juste pour "satisfaire" le type. Mieux vaut dire la verite au compilateur.

:::retenir
`|` = plusieurs types possibles. `?` = propriete facultative. Les deux rendent le contrat honnete.
:::

## Ce que ce n'est pas

Ce n'est pas une excuse pour `string | number | boolean | null | undefined | any`. Une union trop large ne protege plus. Ce n'est pas non plus `?` partout "au cas ou" : trop d'optionnels = code plein de `if` defensifs. Et ce n'est pas confondre `email?: string` avec `email: string | undefined` (proches, nuances selon le contexte). Pour debuter, `?` sur les champs vraiment facultatifs suffit. Lea limite volontairement ses unions a deux ou trois membres utiles.

## Petits exemples utiles

```ts
type Statut = "brouillon" | "envoye" | "paye";

let s: Statut = "brouillon";
s = "paye";
// s = "annule"; // erreur si pas dans l'union

function longueur(x: string | string[]): number {
  return x.length; // ok : les deux ont length
}
```

Les unions de litteraux (`"ok" | "ko"`) sont excellentes pour les etats finis. Lea les prefere aux strings libres qui acceptent `"OKK"` par faute de frappe. Max a remplace trois booleans confus par un statut clair. Sam fait lister les etats au tableau avant d'ouvrir l'editeur : le type ecrit la reunion.

:::astuce
Pour un etat metier (brouillon / envoye / paye), prefere une union de litteraux a une string ouverte.
:::

## Petite histoire

Sam a montre un formulaire ou `age` arrivait parfois vide. Les eleves voulaient `age: number`. Il a propose `age?: number` puis un test avant calcul. Lea, en prod, avait un bug parce qu'elle lisait `contact.email.toLowerCase()` sans guard. L'optionnel + un `if (contact.email)` a ferme le trou. Max a applique le meme geste sur `notes?` de ses devis. DanielCraft resume : un type honnete vaut mieux qu'une valeur inventee pour faire plaisir au compilateur.

## Erreur classique

Ecrire `string | any` (inutile). Utiliser `?` puis acceder sans verifier. Creer une union de dix types au lieu de modeliser mieux. Autre piege : optionnel sur un champ vraiment obligatoire metier, puis decouvrir le trou en production. DanielCraft : le type doit raconter la realite, pas la fantasmer.

:::attention
Si une propriete est `?`, verifie avant d'appeler une methode dessus. Sinon tu retrouves l'erreur runtime que TS essayait d'eviter.
:::

## En vrai

Modele `interface Message { texte: string; auteur?: string }`. Cree deux messages, un avec auteur, un sans. Ecris une fonction qui affiche `auteur` seulement s'il existe. Compile. Puis ajoute une union `priorite: "basse" | "haute"` et teste une mauvaise valeur.

## Honneter le contrat

Les unions et optionnels existent pour coller a la realite. Un formulaire incomplet a des champs vides. Une API legacy renvoie parfois un id string. Mentir avec `email: string` alors qu'il manque souvent, c'est fabriquer des crashes. Lea prefere un `email?` + un message "email manquant" qu'un crash `.toLowerCase`. Max a mis trop d'`?` un temps ; son code etait plein de branches. Sam l'a aide a distinguer "rare mais possible" et "toujours la".

Pour les etats, les unions de litteraux brillent. `"brouillon" | "envoye" | "paye"` empeche `"payee"` avec accent foireux ou `"PAYE"`. Tu gagnes de l'autocompletion et tu perds des fautes. Combine avec un `switch` plus tard si besoin ; pour l'instant, des `if` suffisent.

Rappel : une union n'est pas un tableau. `string | number` est une valeur qui est l'un ou l'autre. `(string | number)[]` est une liste dont chaque case est l'un ou l'autre. Ce n'est pas la meme histoire. Lis a voix haute si tu bloques.

## A toi

Type `let code: string | number`. Assigne les deux formes. Ecris `interface Ligne { label: string; quantite?: number }`. Cree trois lignes differentes. Chez DanielCraft, ce duo `|` et `?` revient sans cesse dans les APIs et formulaires. Note une phrase : "ou est-ce que mon code ment encore ?"
