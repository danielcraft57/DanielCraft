# Chapitre 10 - Le DOM : trouver des elements

Le **DOM**, c'est la page vue par JavaScript. Des elements. Ce que tu as ecrit en HTML, accessible en JS. Avant de changer quoi que ce soit, tu dois trouver. Sans trouver, tu modifies le vide. Tu obtiens `null`. Tu rages. Puis tu comprends. Chez DanielCraft, on compare `querySelector` aux selecteurs CSS : `#id`, `.classe`, `balise`. Si tu as fait le livre HTML/CSS, tu es deja a moitie chez toi. Lea vit la-dedans tous les jours. Max a sourit le jour ou `#titre` a marche du premier coup. Sam dit : si tu as `null`, tu n'as pas encore trouve - arrete-toi avant de modifier.

En 2026, quand quelqu'un dit "je selectionne un element", il parle le plus souvent de **`querySelector`**. Derriere, il y a d'autres methodes (`getElementById`, `getElementsByClassName`...). Pour toi, une seule suffit largement pour debuter. Le geste reste le meme : ecrire le bon selecteur, verifier avec `console.log`, continuer seulement si tu tiens quelque chose. Tu restes le pilote. Le DOM te repond.

Tu es dans un magasin. Le DOM est le plan. `querySelector` est "allez chercher l'article avec cette etiquette". Si l'etiquette n'existe pas, tu reviens les mains vides (`null`). Ensuite seulement tu peux etiqueter, deplacer, changer le prix. Lea dit : "trouver avant de modifier" - comme une loi d'atelier. Max compare ca a chercher une piece dans sa camionnette : si tu n'as pas la bonne reference, tu ne demontes pas le robinet au hasard.

```html
<h1 id="titre">Salut</h1>
<button class="btn">Clique</button>
```

```js
const titre = document.querySelector("#titre");
const bouton = document.querySelector(".btn");
console.log(titre);
console.log(bouton);
```

`querySelectorAll` renvoie une liste. `console.log(titre)` te dit si tu tiens quelque chose. `null` = selecteur faux, ou script trop tot. Rappel du chapitre 2 : script juste avant `</body>`. Sans ca, tu cherches un acteur qui n'est pas encore entre en scene. Lea le repete aux stagiaires jusqu'a ce que ca rentre. Max l'a appris a la dure. Sam le piege volontairement en cours.

:::retenir
Trouver avant de modifier. `querySelector` + `console.log`. Si `null`, corrige le selecteur ou l'emplacement du script.
:::

## Ce que ce n'est pas

Ce n'est pas encore modifier (chapitre suivant). Ici, tu cherches et tu verifies. Ce n'est pas jQuery. Ce n'est pas "getElementById obligatoire" : **`querySelector`** suffit largement pour debuter. Et ce n'est pas ignorer `null` : tu verifies. Toujours. Avant de toucher `.textContent` ou d'ecouter un clic. Modifier `null`, c'est l'erreur classique "Cannot read properties of null".

Ce n'est pas non plus confondre `#` et `.`. `#titre` cible un id. `.titre` cible une classe. Une lettre, un monde. Lea a perdu vingt minutes sur une majuscule dans un id. Max aussi. Sam fait un jeu : trois mauvais selecteurs, un bon. Les eleves `console.log` jusqu'a trouver.

## Selectionner et verifier

```js
const items = document.querySelectorAll("li");
console.log(items.length);
console.log(titre);
console.log(titre.textContent);
```

Meme logique qu'en CSS. C'est pour ca que ca devient vite naturel si tu as fait le livre HTML/CSS. `#` pour un id, `.` pour une classe, `balise` pour un type d'element. Une lettre, un monde. `querySelector` prend le premier match. `querySelectorAll` prend tous les matches. Pour debuter, loggue toujours. Si tu vois l'element dans la console, tu tiens. Si tu vois `null`, tu cherches encore.

:::astuce
Des que tu selectionnes, fais un `console.log`. Si tu vois `null`, arrete-toi : corrige le selecteur ou l'emplacement du script avant de continuer.
:::

## Petite histoire

Lea a eu un bug "impossible" sur une page fleuriste : id `Titre` en HTML, `#titre` en JS. Casse. Une majuscule. Vingt minutes. Max avait le script dans le `head`. `null` systematiquement. Il a deplace avant `</body>`. Marche. Sam fait un jeu en classe : trois mauvais selecteurs, un bon. Les eleves `console.log` jusqu'a trouver. Le geste devient un reflexe, pas une punition. Personne ne dit "JS est casse". On dit "je n'ai pas encore trouve".

Lea rappelle aussi : si tu as plusieurs `.btn`, `querySelector` ne prend que le premier. Pour tous, `querySelectorAll`. Max a clique sur le "mauvais" bouton pendant une semaine avant de comprendre. Sam le montre cote a cote. Le contraste enseigne.

## Erreur classique

Selecteur faux. Script trop tot. Confondre `#` et `.`. Oublier que `querySelector` ne prend que le premier match. Pour plusieurs, `querySelectorAll`. Autre piege : croire que "ca ne marche pas" sans jamais logger ce que tu as vraiment dans les mains. Ou corriger dix lignes de logique alors que le probleme etait une faute dans l'id HTML. Chez DanielCraft, on lit d'abord ce que la console montre. Ensuite on agit.

:::attention
`#titre` et `.titre` ne sont pas la meme chose. Id vs classe. Verifie le HTML avant de blamer JS.
:::

## Exemple complet

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Selection DOM</title>
</head>
<body>
  <h1 id="titre">Ma page</h1>
  <button class="btn">Action</button>
  <ul>
    <li>Un</li>
    <li>Deux</li>
  </ul>
  <script src="script.js"></script>
</body>
</html>
```

```js
const titre = document.querySelector("#titre");
const bouton = document.querySelector(".btn");
const items = document.querySelectorAll("li");

console.log(titre.textContent);
console.log(bouton);
console.log("Nombre de li :", items.length);
```

Ouvre la page. Ouvre la console. Tu dois voir le texte du titre, l'element bouton, et `2`. Si tu vois `null`, deplace le script ou corrige le selecteur. C'est le geste DanielCraft : observer, comprendre, corriger.

## En vrai

Cree une page avec un `h1` id. Selectionne-le. `console.log` son `textContent`. Si `null`, deplace le script avant `</body>`. Puis casse volontairement le selecteur (`#Titre` au lieu de `#titre`). Lis. Repare. Ce contraste vaut une demi-heure de cours. Lea le fait avec chaque stagiaire. Max s'en souvient encore.

## A toi

Selectionne un bouton par classe et tous les `li`. Affiche les longueurs et les textes. Invente un cas perso (ton score, ton jeu, ta page artisan). Note ton selecteur gagnant sur un post-it. Chez DanielCraft, trouver avant de modifier est une loi d'atelier - tu la reutiliseras au chapitre suivant des que tu changeras la page.
