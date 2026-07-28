# Chapitre 19 - Bonnes pratiques debutantes

Des pratiques simples valent mieux qu'une religion de types. Chez DanielCraft, on vise **strict**, des **noms clairs**, des **petits contrats**, des erreurs lues, peu de magie. Lea active `strict` tot. Max ajoute des interfaces quand une forme revient deux fois. Sam refuse les fichiers de 800 lignes "tout typer plus tard".

Tu n'as pas besoin d'etre parfait. Tu as besoin d'etre coherent. Une annotation honnete, une interface nommee, un `if` de narrowing, un `tsc` frequent : ce quartet porte deja loin.

:::retenir
Strict, noms clairs, petits contrats, compile souvent. Evite `any` et les casts de panique.
:::

## Ce que ce n'est pas

Ce n'est pas "zero `any` a vie sous peine de mort". Ce n'est pas configurer vingt plugins. Ce n'est pas typer pour typer (annoter `const x: number = 1` partout sans gain). Ce n'est pas non plus attendre le setup parfait avant d'ecrire. Lea livre avec une config courte comprise.

## Gestes qui marchent

1. Active `"strict": true` dans `tsconfig` des que tu peux.
2. Type les frontieres : entrees de fonctions, donnees externes, props d'objets partages.
3. Nomme les interfaces comme le metier : `TodoItem`, `DevisLigne`.
4. Prefere union de litteraux aux strings libres pour les etats.
5. Narrow au lieu de caster.
6. Corrige la premiere erreur `tsc` d'abord.
7. Laisse inferer quand c'est evident ; explicite quand ca documente.

```ts
// frontiere claire
function creerTodo(texte: string): TodoItem {
  return { id: Date.now(), texte, fait: false };
}
```

:::astuce
Si une forme d'objet apparait deux fois, extrais une interface. Une seule fois, un litteral annote peut suffire.
:::

## Petite histoire

Lea a herite d'un projet sans strict. Chaque semaine un bug "possibly undefined". Elle a active strict module par module. Douloureux deux jours, puis calme. Max a renomme `IData` en `Client`. Sam a coupe un fichier monstre en trois avec des contrats nets. DanielCraft mesure la pratique a la facilite de relire, pas au nombre de types exotiques.

## Erreur classique

Sur-typer du bruit. Sous-typer les frontieres importantes. Copier une config incomprise. Autre piege : bonnes pratiques en reunion, `any` en prod le vendredi. Ecris une checklist courte et utilise-la.

:::attention
Une bonne pratique non appliquee ne protege personne. Choisis trois gestes et tiens-les deux semaines.
:::

## En vrai

Ouvre ton `tsconfig`. Verifie `strict`. Parcours un fichier : renomme une interface floue, retire un `any`, ajoute un narrowing. Commit mental : "trois gestes".

## Ritualiser

Une bonne pratique tient si elle devient rituel. Avant demo : `tsc` vert. Avant commit mental : pas de `any` nouveau. Avant d'ajouter une option tsconfig : une phrase "pourquoi". Lea a ces trois rituels. Max en a ajoute un : montrer le projet a quelqu'un meme trente secondes. Sam ajoute : expliquer une erreur en francais.

Tu peux aussi tenir un fichier `NOTES.md` avec tes interfaces cles et tes pieges. Ce n'est pas de la paperasse : c'est une memoire externe. Chez DanielCraft, on prefere une note courte a une documentation fantome de cinquante pages.

Quand une pratique te ralentit sans securite gagnee, ajuste. Le but n'est pas d'obeir a une liste. Le but est de livrer du code plus sur, plus lisible, plus corrigible.

## A toi

Ecris ta checklist perso (5 lignes max). Exemple : strict / pas d'any / interfaces nommees / lire tsc / DOM garde. Colle-la. Chez DanielCraft, la checklist courte bat le manifeste.
