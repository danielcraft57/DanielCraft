# Chapitre 15 - Atelier : annoter sans paniquer

Objectif : prendre un petit bout de JavaScript flou et le rendre honnete avec des **annotations**. Pas de genie. Pas de config de 80 lignes. Chez DanielCraft, un atelier se juge a "ca compile et je comprends", pas a "c'est impressionnant". Lea chronometre souvent 45 minutes. Max paniquait au premier rouge ; ici tu vas le lire. Sam interdit `any` pendant l'exercice.

Tu vas declarer des variables typees, une petite fonction, et corriger volontairement des erreurs. Le but n'est pas zero erreur du premier coup. Le but, c'est le cycle : ecrire, `tsc`, lire, corriger.

:::retenir
Annoter, c'est nommer le contrat. Si `tsc` proteste, tu as trouve un flou : corrige la valeur ou le type.
:::

## Mission

1. Cree `atelier-types.ts`.
2. Declare :
   - `titre: string`
   - `prix: number`
   - `promo: boolean`
3. Ecris `function label(titre: string, prix: number): string` qui renvoie `"titre - prix EUR"`.
4. Appelle la fonction et `console.log` le resultat.
5. Introduis une mauvaise assignation, lis l'erreur, corrige.

```ts
let titre: string = "Joint silicone";
let prix: number = 4.5;
let promo: boolean = false;

function label(titre: string, prix: number): string {
  return titre + " - " + prix + " EUR";
}

console.log(label(titre, prix));
```

## Ce que ce n'est pas

Ce n'est pas l'heure des interfaces completes (atelier suivant). Ce n'est pas le DOM. Ce n'est pas "faire joli". Si tu ajoutes dix variables inutiles, tu te disperses. Lea coupe le superflu. Max a tendance a sur-annoter ; Sam lui demande : "cette annotation enseigne-t-elle encore quelque chose ?"

:::astuce
Quand tu bloques, commente la ligne fautive, recompile, isole. Une erreur a la fois.
:::

## Petite histoire

Max a rate `promo: boolean` en mettant `"non"`. L'erreur etait claire. Il a sourit malgre lui. Lea a ajoute une annotation de retour manquante puis l'a retiree pour montrer l'inference. Sam a termine l'atelier en demandant a chacun de lire une erreur a voix haute. DanielCraft : la voix haute transforme le rouge en phrase.

## Erreur classique

Mettre `any` pour finir plus vite. Annoter `string` sur un prix calcule. Oublier d'appeler la fonction. Autre piege : copier le corrige sans casser puis reparer. L'atelier vit dans la casse volontaire.

:::attention
Ne "repare" pas avec `as any`. Si le type gene, change la donnee ou le contrat - pas le silence.
:::

## En vrai / A toi

Fais la mission. Puis ajoute `remise: number` et une fonction `prixFinal(prix: number, remise: number): number`. Compile. Note une phrase sur ce que `tsc` t'a appris aujourd'hui. Garde le fichier pour le comparer a l'atelier interface.

## Deroule detaille

Installe le rythme. Ouvre ton editeur. Cree le fichier. Ecris les quatre variables annotees avec des valeurs coherentes. Ecris `labelProduit` et appelle-la avec `titre` et `prix`. Ecris `appliquerRemise` avec un taux `0.1`. Affiche avant/apres. Compile. Si `tsc` est vert, casse : passe `"dix"` en prix. Lis. Corrige.

Ensuite ajoute `estCher`. Teste avec 50 et 150. Ajoute `formatStock`. Enchaine les `console.log` pour voir un petit ticket produit dans le terminal. Lea demande souvent une capture des logs. Max aime voir les strings se construire. Sam regarde surtout s'il reste un `any` cache.

Si tu debutes vraiment sur `tsc`, reviens trente secondes au chapitre 2. Pas de honte. L'atelier suppose le pipeline, pas la perfection memoire. Chez DanielCraft, ce muscle nourrit l'atelier interface suivant.
