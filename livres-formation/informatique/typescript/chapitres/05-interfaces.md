# Chapitre 5 - Les interfaces (objets types)

Un objet JS, c'est des etiquettes + des valeurs : `{ nom: "Lea", age: 29 }`. Une **interface** TypeScript decrit la forme attendue de cet objet. Tu dis : un `Client` a un `nom` string et un `age` number. Ensuite, toute variable `Client` doit respecter ce contrat. Chez DanielCraft, l'interface est la fiche produit du code : claire, partageable, stable. Lea cree `interface Devis` avant d'ecrire la logique. Max a longtemps passe des objets "au feeling" ; une interface lui a evite d'oublier `email`. Sam fait dessiner la fiche au tableau avant le clavier.

```ts
interface Client {
  nom: string;
  age: number;
  ville: string;
}

const c: Client = {
  nom: "Max",
  age: 34,
  ville: "Nantes",
};
```

Si tu oublies `ville`, `tsc` proteste. Si tu mets `age: "trente"`, aussi. L'interface ne cree pas l'objet a l'execution : elle guide le compilateur. Apres compile, il reste un objet JS normal.

:::retenir
Une interface decrit la forme d'un objet. Tu la reutilises pour typer variables, parametres et retours.
:::

## Ce que ce n'est pas

Ce n'est pas une classe (pas d'instances "new" obligatoires ici). Ce n'est pas une base de donnees. Ce n'est pas obligatoire pour un objet litteral unique jete une fois. Ce n'est pas non plus `type` vs `interface` en debat infinite : pour debuter, **interface** sur les objets suffit largement. Et ce n'est pas remplir vingt champs "au cas ou".

## Proprietes et reemploi

```ts
interface Produit {
  id: number;
  label: string;
  prix: number;
}

function afficherPrix(p: Produit): void {
  console.log(p.label + " : " + p.prix + " EUR");
}

afficherPrix({ id: 1, label: "Joint", prix: 4.5 });
```

Lea passe des `Produit` a plusieurs fonctions sans recopier la forme. Max a commence a documenter ses objets "todo" avec une interface : fini les `tache.texte` vs `tache.title` melanges. Sam exige un nom d'interface qui parle : `TodoItem`, pas `Data` ou `Stuff`.

:::astuce
Nomme l'interface comme un nom commun clair : `Client`, `TodoItem`, `DevisLigne`. Evite `IData1`.
:::

## Petite histoire

Lea et un stagiaire echangeaient un objet "commande" par message. Sans interface, chacun inventait des cles. Avec `interface Commande`, le stagiaire a vu tout de suite les champs manquants dans l'editeur. La revue de code a dure dix minutes au lieu d'une heure de "ah oui j'avais mis `name` pas `nom`". Max a copie le geste sur sa todo artisan. DanielCraft adore ces gains invisibles : moins de theatre, plus de livraison.

## Erreur classique

Creer une interface puis passer un objet avec des cles en trop sans savoir si c'est autorise (selon le contexte d'assignation, TS est strict sur l'exces pour les litteraux). Oublier une propriete obligatoire. Dupliquer la meme forme dans cinq fichiers au lieu d'exporter. Autre piege : interface vide "pour plus tard". Prefere attendre d'avoir deux champs reels.

:::attention
Si un litteral object a une propriete inconnue pour l'interface, TypeScript peut refuser. C'est voulu : ca detecte les fautes de frappe (`emial` au lieu de `email`).
:::

## En vrai

Modele une fiche `Livre` avec `titre`, `pages`, `lu` (boolean). Cree un objet conforme. Passe-le a une fonction `resume(l: Livre)`. Compile. Retire un champ, observe l'erreur, remets.

## Faire vivre une interface

Une interface utile se lit comme une fiche. Tu dois pouvoir dire : "un TodoItem, c'est un id, un texte, et un flag fait". Si tu ne peux pas, simplifie. Lea interdit les interfaces de quinze champs pour un atelier d'une heure. Max a appris a sortir les details rares en optionnel plutot qu'a tout rendre obligatoire. Sam fait comparer deux interfaces mal nommees et bien nommees : la salle vote toujours pour la claire.

Tu peux reutiliser la meme interface dans plusieurs fichiers plus tard (export/import). Pour ce livre, un seul fichier suffit. L'idee compte : une seule source de verite pour la forme. Si tu changes `texte` en `title`, tu changes l'interface et `tsc` te montre tous les endroits a mettre a jour. C'est exactement le service rendu.

Evite aussi de confondre interface et valeur. L'interface ne "contient" pas les todos. Le tableau `TodoItem[]` contient les todos. L'interface dit seulement a quoi ressemble chaque element. Chez DanielCraft, cette phrase revient souvent parce qu'elle evite une confusion durable.

## A toi

Ecris `interface TodoItem { id: number; texte: string; fait: boolean; }`. Cree deux todos. Ecris `function marquerFait(t: TodoItem): void` qui met `fait` a `true` et log. Chez DanielCraft, cette interface reviendra dans les ateliers et le mini-projet.
