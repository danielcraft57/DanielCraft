# Chapitre 16 - Atelier : une interface pour un vrai objet

Objectif : modeliser un objet metier avec une **interface**, puis ecrire une ou deux fonctions qui la respectent. Chez DanielCraft, l'interface n'est pas un luxe academique. C'est la fiche que tu aurais dessinee sur papier. Lea commence souvent par les champs au tableau. Max code trop vite sans liste ; ici tu listes d'abord. Sam refuse les noms `Data` / `Info`.

Tu vas creer `TodoItem`, une petite liste, et des actions typees. Pas de framework. Juste la forme et les fonctions.

:::retenir
Interface = forme reutilisable. Fonction typee = usage honnete de cette forme.
:::

## Mission

1. Cree `atelier-interface.ts`.
2. Ecris :

```ts
interface TodoItem {
  id: number;
  texte: string;
  fait: boolean;
}

const todos: TodoItem[] = [
  { id: 1, texte: "Lire le chapitre 5", fait: true },
  { id: 2, texte: "Annoter mon script", fait: false },
  { id: 3, texte: "Compiler sans any", fait: false },
];

function restantes(items: TodoItem[]): TodoItem[] {
  return items.filter((t) => t.fait === false);
}

function marquerFait(item: TodoItem): void {
  item.fait = true;
}

console.log(restantes(todos));
marquerFait(todos[1]);
console.log(restantes(todos));
```

3. Compile. Ajoute volontairement un champ `titre` au lieu de `texte` sur un litteral, lis l'erreur, corrige.
4. Ajoute `email?: string` seulement si tu as un vrai besoin - sinon laisse.

## Ce que ce n'est pas

Ce n'est pas une app todo complete avec DOM (presque : atelier projet). Ce n'est pas le debat `type` vs `interface`. Ce n'est pas vingt champs "au cas ou". Trois champs utiles battent une usine. Lea coupe les proprietes decoratives.

:::astuce
Si `tsc` parle d'une propriete manquante, regarde l'interface avant le corps de la fonction.
:::

## Petite histoire

Lea a fait cet atelier avec un stagiaire qui ecrivait `tache.texte` et `tache.title` selon l'humeur. L'interface a force un seul mot. Max a oublie `fait` ; le compilateur a refuse l'objet. Sam a demande : "ton interface raconte-t-elle la realite ?" DanielCraft : si la fiche ment, le code ment.

## Erreur classique

Interface vide. `any` dans un champ "temporaire". Modifier l'interface pour accepter n'importe quoi apres une erreur. Autre piege : muter sans le vouloir dans une fonction qui devrait renvoyer une copie - pour debuter, la mutation simple de `fait` est OK si tu es conscient.

:::attention
Un litteral avec une cle inconnue est souvent refuse. C'est un cadeau : faute de frappe detectee tot.
:::

## En vrai / A toi

Ajoute `function compteRestantes(items: TodoItem[]): number`. Teste. Puis cree un quatrieme todo conforme. Si tu as le temps, ajoute `priorite?: "basse" | "haute"` et un filtre. Note ce que l'optionnel change dans tes `if`.

## Qualite de modele

Avant de coder, ecris sur papier les champs et pour chacun : obligatoire ou optionnel, type. Puis seulement code l'interface. Lea chronometre cette minute papier : elle evite les interfaces "au feeling". Max saute parfois l'etape et le regrette. Sam note le papier comme partie de la copie.

Quand tu as `priorite?`, teste deux todos : une avec priorite, une sans. Affiche autrement si haute. Tu touches union litterale + optionnel dans un vrai objet. C'est le coeur du chapitre 6 applique. Si `tsc` refuse un litteral `"moyenne"` hors union, c'est gagne : le filet marche.

Termine en renommant un champ dans l'interface et en suivant les erreurs. Tu verras la carte des usages. C'est une raison majeure d'aimer TypeScript en equipe.
