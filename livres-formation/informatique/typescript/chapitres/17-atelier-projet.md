# Chapitre 17 - Atelier : petit projet type de bout en bout

Objectif : enchainement complet. Une **interface**, un **etat**, des **fonctions**, un peu de **DOM** garde, zero `any`. Chez DanielCraft, cet atelier colle le mini-projet compteur et l'atelier interface : tu livres une mini todo affichee dans la page. Lea demande une V1 en moins de deux heures. Max ajoute trop de features ; Sam coupe : ajouter, afficher, basculer fait.

Tu n'as pas besoin d'un bundler. HTML + `tsc` suffisent. Si le DOM te stresse, repars du chapitre 12. Si l'interface te stresse, repars du 16.

:::retenir
Bout en bout = meme contrat de l'etat jusqu'a l'ecran. Compile souvent.
:::

## Mission

HTML minimal : `input#texte`, `button#ajouter`, `ul#liste`. Puis TypeScript :

```ts
interface TodoItem {
  id: number;
  texte: string;
  fait: boolean;
}

let todos: TodoItem[] = [];
let nextId: number = 1;

const input = document.querySelector<HTMLInputElement>("#texte");
const btn = document.querySelector<HTMLButtonElement>("#ajouter");
const liste = document.querySelector<HTMLUListElement>("#liste");

function rendre(): void {
  if (!liste) return;
  liste.innerHTML = "";
  for (const t of todos) {
    const li = document.createElement("li");
    li.textContent = (t.fait ? "[x] " : "[ ] ") + t.texte;
    li.addEventListener("click", () => {
      t.fait = !t.fait;
      rendre();
    });
    liste.appendChild(li);
  }
}

function ajouter(): void {
  if (!input) return;
  const texte = input.value.trim();
  if (!texte) return;
  todos.push({ id: nextId, texte, fait: false });
  nextId = nextId + 1;
  input.value = "";
  rendre();
}

btn?.addEventListener("click", ajouter);
rendre();
```

Compile, ouvre la page, ajoute deux taches, clique pour basculer.

## Ce que ce n'est pas

Ce n'est pas localStorage obligatoire. Ce n'est pas un design parfait. Ce n'est pas React. Si tu ajoutes dix boutons, tu quittes l'atelier. Lea dit "V1 moche qui compile > V5 jolie qui ment sur les types".

:::astuce
Si `innerHTML` te gene pour la securite plus tard, OK - ici on reste pedagogique. Le focus, c'est le typage de `todos`.
:::

## Petite histoire

Max a livre sans garder `input` contre `null`. `tsc` en strict l'a arrete. Lea a refuse un `todos: any[]`. Sam a demande un `trim()` avant push : les taches vides polluent. Ensemble, ils ont une demo stable. DanielCraft applaudit le cycle court, pas le framework.

## Erreur classique

Oublier de rappeler `rendre` apres mutation. Typer `texte` en number. Utiliser `as HTMLInputElement` sans query adequat. Autre piege : tout mettre dans un seul listener anonyme de 80 lignes - extraire aide le typage et la lecture.

:::attention
Apres chaque action qui change `todos`, rappelle l'affichage. Sinon ton etat type dit vrai et l'ecran ment.
:::

## En vrai / A toi

Ajoute un compteur "N restantes" dans un `span` type. Puis interdis les doublons de texte (optionnel). Ecris trois lignes de bilan : erreur `tsc` vue, correction, prochaine idee. Chez DanielCraft, le bilan ancre plus que la feature bonus.

## Gerer le temps

Prevois une heure calme. Quarante minutes de construction, dix de polish, dix de debrief. Si tu debloques trop longtemps sur le DOM, reviens au compteur minimal sans CSS. Si tu debloques sur les types, commente une ligne, isole l'erreur, corrige, decomment. Lea enseigne cet isolement. Max a tendance a tout reecrire ; Sam l'arrete.

Prepare aussi la demo : quels clics tu montres, quelle erreur tu as corrigee en route (raconte-la). Une demo qui inclut une erreur lue est plus pedagogique qu'une demo parfaite amnesique. Chez DanielCraft, on forme des gens qui racontent leur debug.

Livrable minimal accepte : HTML + TS + JS compile + README de cinq lignes (comment lancer `tsc`, comment ouvrir la page). Pas besoin de github. Besoin d'un dossier propre.
