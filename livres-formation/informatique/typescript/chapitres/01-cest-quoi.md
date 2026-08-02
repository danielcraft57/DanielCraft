# Chapitre 1 - C'est quoi TypeScript ?

Tu connais deja un peu **JavaScript** : variables, fonctions, tableaux, un peu de DOM. TypeScript, c'est JavaScript avec un filet de securite. Tu ajoutes des **types** pour dire clairement ce que chaque valeur est censee etre. Avant d'executer, un **compilateur** (`tsc`) lit ton code et te signale les incoherences. Ensuite, il produit du JavaScript classique que le navigateur ou Node comprend. Chez DanielCraft, on presente TS comme un garde-fou amical - pas comme un club de theory. Lea l'utilise pour eviter les bugs betes avant la demo. Max a compris le jour ou `tsc` a refuse un nombre la ou il attendait un texte. Sam dit a ses eleves : "TS ne remplace pas JS. Il te force a preciser."

Le geste mental est simple. En JS, tu peux ecrire `prenom = 42` par accident et t'en rendre compte trop tard. En TypeScript, tu annonces `prenom: string` et le compilateur proteste si tu ranges un nombre. Tu restes le pilote. TS te rappelle juste les regles que tu as posees. Ce livre suit le livre JavaScript bases : meme personnages, meme rythme petit-clair-testable. On suppose que tu as deja touche `const`, `function` et un `if`.

:::retenir
TypeScript = JavaScript + types. Tu ecris en `.ts`, tu compiles en `.js`, le navigateur execute le JS.
:::

## Ce que ce n'est pas

Ce n'est pas un autre langage mysterieux sans lien avec JS. Ce n'est pas obligatoire pour "faire du web" des le jour un. Ce n'est pas un framework (React et cie). Ce n'est pas magie : si tu ecris flou, TS te le dira, mais tu dois encore penser. Et ce n'est pas "tout typer parfaitement le premier soir". Commence par annoter des variables et des fonctions simples.

Ce n'est pas non plus Java, malgre le nom proche de "type". Lea rappelle souvent : le vrai travail, c'est encore la logique. Les types aident a ne pas se tromper de forme.

## Ce que tu vas savoir faire

A la fin de ce livre, tu sauras installer l'intuition de `tsc` et `tsconfig`, annoter des variables, modeliser des objets avec des **interfaces**, utiliser unions et optionnels, typer fonctions et tableaux, faire un peu de **narrowing**, eviter `any`, lire une erreur du compilateur sans paniquer, toucher le DOM legerement type, et livrer un mini projet compteur ou todo type. Niveau debutant solide. Pas de monorepo. Pas de decorateurs. Juste du TS clair.

## Comment lire ce livre

Lis dans l'ordre au debut. Les premiers chapitres posent le sol : idee, install, types, annotations. Le milieu construit interfaces, unions, fonctions, tableaux, narrowing. Les ateliers font faire. Le quiz verifie. A chaque fin, un "A toi". Fais-le. Cinq minutes actives battent une lecture passive.

Chez DanielCraft, on forme des gens qui livrent petit, souvent, proprement - pas des collectionneurs de configs Vite jamais ouvertes. Tu ecris. Tu lances `tsc`. Tu corriges. Ce rythme bat une soiree de videos sans fichier `.ts`.

## Petite histoire

Lea livrait un script de devis. En JS seul, un client passait une chaine la ou le total attendait un nombre. La page affichait `NaN` en plein appel. Avec TypeScript, le meme glissement aurait ete bloque avant la demo. Elle a ajoute trois annotations et un interface `Devis`. Quarante minutes. Le client n'a jamais su qu'il y avait eu un mini drame. Lea, si.

Max voulait juste "moins d'erreurs betes" sur son compteur. Il a renomme `app.js` en `app.ts`, ajoute `: number` sur le score, et regarde `tsc` lui dire non quand il ecrivait `score = "dix"`. Sam desactive volontairement le typage en cours : les eleves voient reapparaitre le flou. L'idee rentre sans jargon. Personne ne dit "c'est trop". Ils disent "ah, c'est un garde".

## Erreur classique

Croire que TypeScript s'execute directement dans le navigateur comme un fichier `.ts` nu. En vrai, tu compiles (ou un outil le fait pour toi) vers du **JavaScript**. Autre piege : vouloir tout le manuel TypeScript avant d'annoter une seule variable. Ou penser que TS remplace HTML/CSS/JS. Lea garde une regle : une annotation claire bat dix options avancees. DanielCraft insiste : petit, clair, testable.

:::attention
Sans compilation (ou outil equivalent), le navigateur ne "mange" pas le TypeScript. Le produit final reste du JavaScript.
:::

## En vrai

Ouvre un petit script JS que tu as deja. Imagine une ligne ou une mauvaise valeur ferait mal : un total, un prenom, un id DOM. Note en une phrase ce que tu voudrais "garantir" comme type. Tu poseras mieux tes priorites pour la suite. Puis dis-toi : ce livre va transformer cette intention en syntaxe `: string`, `: number`, `interface`, etc.

## A toi

Ecris en trois phrases : (1) un endroit de ton code JS ou un type t'aurait aide, (2) ce que tu acceptes d'apprendre d'abord (annotations, interfaces...), (3) ce que tu ne feras pas encore (generics avances, monorepo). Garde ce papier pour le mini-projet du chapitre 13. Chez DanielCraft, ce petit brief vaut plus qu'une heure de tutorials flous.

## Exemple pour sentir

```ts
let prenom: string = "Lea";
// prenom = 42; // erreur : number n'est pas assignable a string

function double(n: number): number {
  return n * 2;
}
console.log(double(4));
```

Tu n'as pas besoin de tout comprendre maintenant. L'idee : tu annonces le contrat, le compilateur verifie. Dans ce livre, on demonte ca piece par piece, avec Lea, Max et Sam - et DanielCraft comme fil : petit, clair, testable.
