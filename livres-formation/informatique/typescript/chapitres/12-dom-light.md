# Chapitre 12 - DOM legerement type

Tu as deja selectionne des elements en JavaScript : `document.querySelector`, `getElementById`, `textContent`. En TypeScript, le DOM reste le meme, mais les types te rappellent qu'un element peut etre **absent** (`null`) et qu'un element generique n'a pas toujours les proprietes d'un `HTMLInputElement`. Chez DanielCraft, on reste leger : pas de framework, juste des gardes simples. Lea type ses boutons apres les avoir trouves. Max oubliait le `null` et voyait `Object is possibly 'null'`. Sam insiste : "trouve, verifie, utilise".

```ts
const btn = document.querySelector("#plus");
if (btn) {
  btn.addEventListener("click", () => {
    console.log("clic");
  });
}
```

Souvent `querySelector` renvoie `Element | null`. Si tu as besoin d'un champ `value`, tu vises un input :

```ts
const input = document.querySelector<HTMLInputElement>("#nom");
if (input) {
  console.log(input.value);
}
```

Le generique `<HTMLInputElement>` dit a TS quelle forme tu attends. Ca ne garantit pas que le HTML est juste : si l'id pointe un `div`, tu auras un souci runtime. Lea verifie aussi le HTML. Max a appris a lire `null` comme "pas trouve", pas comme "TypeScript est mechant".

:::retenir
DOM type = selection + garde `null` (+ type d'element si tu lis `value`, etc.).
:::

## Ce que ce n'est pas

Ce n'est pas un cours HTML complet. Ce n'est pas React. Ce n'est pas `document.getElementById!` partout avec assertion non-null. Ce n'est pas non plus typer tout le document. Et ce n'est pas paniquer si TS te demande un `if` : c'est exactement le filet utile sur une page incomplete.

## Gestes du quotidien

```ts
const scoreEl = document.querySelector<HTMLElement>("#score");
const plus = document.querySelector<HTMLButtonElement>("#plus");

function afficher(n: number): void {
  if (!scoreEl) return;
  scoreEl.textContent = String(n);
}

plus?.addEventListener("click", () => {
  // logique compteur plus loin
});
```

L'operateur `?.` (optionnel) evite d'ecouter un bouton absent. Lea l'aime pour les scripts de demo. Max prefere un `if (plus)` explicite au debut. Sam accepte les deux si le garde existe vraiment.

:::astuce
Si tu lis `.value`, vise `HTMLInputElement` (ou `HTMLTextAreaElement`). Si tu changes seulement le texte, `HTMLElement` suffit souvent.
:::

## Petite histoire

Lea branchait un compteur. Sans garde, un mauvais id plantait la page. Avec `if (!scoreEl) return`, le script restait silencieux et elle voyait tout de suite l'id manque dans le HTML. Max a force `as HTMLInputElement` sur un span : `value` etait `undefined` a l'execution. Sam a efface le `as` et ajoute le bon selecteur. DanielCraft : le type suit le HTML, il ne le remplace pas.

## Erreur classique

Ignorer `null`. Utiliser `!` apres chaque query "pour compiler". Croire que le generique `querySelector<T>` valide le DOM. Autre piege : tout mettre en `any` des que le DOM resiste. Prefere un `if` et un type precis.

:::attention
`querySelector<HTMLInputElement>` ne verifie pas le HTML. Il change seulement ce que TypeScript croit. Aligne id et balise.
:::

## En vrai

Cree une page minimale avec un `span#score` et un `button#plus`. Selectionne les deux en TS, garde contre `null`, change le texte au clic. Compile. Retire un id, observe le comportement de ton garde.

## DOM et types : le duo

Le DOM est vivant : l'utilisateur clique, le HTML peut etre incomplet, un id peut manquer. TypeScript ne remplace pas ces realites. Il te force a les admettre. Lea regarde toujours le HTML en meme temps que le TS. Max ouvrait seulement le `.ts` et perdait du temps. Sam projette les deux fichiers. Chez DanielCraft, "aligner les ids" est une pratique autant qu'une annotation.

Pour les evenements, tu verras parfois `Event`, `MouseEvent`. Au debut, une fleche `() => add(1)` suffit sans typer l'event. Si tu as besoin de `event.target`, tu narrowing ou tu cast avec prudence vers un element connu. Reste simple : le compteur n'a pas besoin d'une these sur les events.

Si tu compiles vers un JS charge en `defer` / fin de body, le DOM existe souvent au demarrage du script. Si tu charges trop tot, `getElementById` renvoie null. Encore une fois : le type te le rappelle, le HTML/timing decide.

## Lien avec le livre JS

En JavaScript bases, tu selectionnais et tu ecoutais des clics. Ici, tu fais pareil avec un filet. Le querySelector peut etre null : TS te le rappelle. value existe sur un input : TS te pousse vers HTMLInputElement. Rien de magique, juste plus de franchise. Lea dit que TS rend visibles des pieges que JS laissait silencieux. Max confirme apres son premier null. Sam en fait le pont officiel entre les deux livres.

## A toi

Ecris un script qui lit un `input#prenom` et ecrit "Bonjour X" dans un `p#out` au clic d'un bouton. Types + gardes. Chez DanielCraft, ce micro-DOM prepare le mini-projet compteur.
