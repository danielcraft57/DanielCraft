# Chapitre 12 - Les evenements (reagir aux clics)

Jusqu'ici, ton JavaScript agissait surtout au chargement. La page se chargeait, le script modifiait quelque chose, fin de l'histoire. Maintenant, la page devient vraiment interactive. Tu ecoutes. Tu reponds. Un clic, un message. Un clic, un compteur qui monte. Un submit de formulaire, une verification avant envoi. C'est ici que le web cesse d'etre une brochure et devient un outil. Chez DanielCraft, **`addEventListener`** est le geste cle : "quand cet evenement arrive sur cet element, fais ca".

Lea branche des boutons CTA sur des pages clients : "demander un devis", "voir les tarifs". Max compte les clics de test sur son bouton "Appeler maintenant" pour montrer a sa femme que la page "vit". Sam fait applaudir la classe au premier compteur qui marche en direct - c'est un moment. Trois metiers, meme logique : le HTML propose l'element, le JS dispose de la reaction quand on ecoute. Sans listener, la sonnette existe mais personne ne reagit.

Une sonnette a la porte. L'evenement, c'est l'appui. Le listener, c'est toi derriere la porte, pret a reagir. Sans listener, la sonnette existe (HTML) mais personne ne bouge. Avec listener, la maison s'anime : message, compteur, validation. Lea dit : "le HTML propose, le JS dispose - mais seulement quand on ecoute". Commence par **`click`** : le plus clair, le plus testable. Une interaction nette vaut dix demos floues.

:::retenir
addEventListener = "quand cet evenement arrive sur cet element, fais ca". Tu donnes la recette, tu ne la lances pas tout de suite.
:::

```html
<button id="bouton">Clique-moi</button>
<p id="message"></p>
```

```js
const bouton = document.querySelector("#bouton");
const message = document.querySelector("#message");
bouton.addEventListener("click", function () {
  message.textContent = "Bravo, tu as clique !";
});
```

## Ce que ce n'est pas

Ce n'est pas `onclick="..."` colle partout dans le HTML. Ca marche, oui, mais on prefere separer : HTML pour la structure, JS pour le comportement. Ce n'est pas ecouter avant d'avoir l'element en memoire : si le script est trop haut ou l'id faux, tu ecoutes le vide. Ce n'est pas oublier **`preventDefault`** sur un submit si tu geres toi-meme le formulaire : sans ca, la page recharge et tes logs disparaissent. Et ce n'est pas dix ecouteurs identiques copies-colles sans fonction : une logique claire, un listener propre, eventuellement une fonction reutilisable.

Ce n'est pas non plus appeler la fonction tout de suite dans `addEventListener`. Tu passes la recette, tu ne lances pas le plat. `addEventListener("click", maFonction)` - pas `maFonction()`. Lea a deja vu un junior se demander pourquoi son alert s'affichait au chargement au lieu du clic. La reponse etait dans les parentheses.

## Compteur et formulaires

```js
let clics = 0;
bouton.addEventListener("click", function () {
  clics = clics + 1;
  message.textContent = "Clics : " + clics;
});

form.addEventListener("submit", function (event) {
  event.preventDefault();
  // ton code ici
});
```

Tu peux garder un compteur avec `let clics = 0` et l'afficher a chaque clic. Tu croiseras aussi `input` (ecriture dans un champ), `submit` (envoi de formulaire), parfois `mouseover` ou `keydown`. Commence par `click`. **`preventDefault`** dit au navigateur : "laisse, je gere". Utile pour ne pas recharger la page pendant tes tests. Sans ca, tu cliques, la page part, tu ne comprends rien. Lea a perdu une heure la-dessus un mardi matin. Max aussi. Maintenant ils le mettent en premier sur tout formulaire test.

:::astuce
Premier test d'un listener : mets `console.log("clic")` dedans. Preuve de vie avant la logique metier. Si tu vois "clic" en console, le fil est branche.
:::

## Petite histoire

Lea avait un formulaire de contact qui "mangeait" ses logs a chaque test : la page rechargeait, les `console.log` disparaissaient, elle croyait que son code ne marchait pas. `preventDefault` a tout change en une ligne. Max mettait le listener sur un id faux (`#bouton` au lieu de `#btn`) : silence total, pas d'erreur visible si tu ne log pas. Sam exige un `console.log("clic")` en premier dans chaque handler avant d'ecrire le vrai code. Preuve de vie. Ensuite seulement la logique metier. Trois scenes, une methode : ecouter le bon element, prouver que ca reagit, puis construire.

## Erreur classique

Element `null`, donc erreur au `addEventListener` : selecteur faux ou script trop haut. Oublier que la fonction listener n'est pas appelee avec `()` dans le add : tu passes la fonction, tu ne l'executes pas tout de suite. Mettre la logique hors du listener et s'etonner que ca ne reagit pas au clic : le code s'execute une fois au chargement, pas a chaque clic. Croire que "ca marche" sans jamais cliquer vraiment : teste. Clique dix fois. Souris. C'est vivant ou ce ne l'est pas.

:::attention
Ecris `addEventListener("click", maFonction)` - pas `maFonction()`. Tu donnes la recette, tu ne la lances pas tout de suite.
:::

## En vrai

Cree un bouton et un paragraphe. Branche un compteur : chaque clic ajoute 1, affiche le total dans le `p`. Clique dix fois. Regarde le chiffre monter. Puis ajoute un mini formulaire avec `preventDefault` qui affiche le prenom saisi dans un paragraphe sans recharger la page. Si les deux marchent, tu as le coeur du web interactif. Le mini-projet du chapitre 13 va assembler ca proprement. Si le formulaire recharge, cherche `preventDefault` avant de reecrire dix lignes.

## A toi

Ajoute un bouton reset qui remet le compteur a zero. Puis un mini formulaire avec `preventDefault` qui affiche le prenom saisi dans un `p`. Teste chaque piece separement avant d'assembler. Tu prepares le mini-projet compteur. Facons DanielCraft : petit, clair, testable, un geste a la fois. Note en une phrase ce qui a bloque, s'il y a eu un blocage.
