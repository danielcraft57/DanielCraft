# Chapitre 11 - Le DOM : changer la page

Tu as appris a trouver un element avec **querySelector**. Maintenant tu vas le modifier. Changer le texte d'un titre. Ajouter une classe qui allume une couleur. Creer un paragraphe qui n'existait pas une seconde avant. La page n'est plus figee comme une photo : ton script la sculpte en direct, dans le navigateur, en memoire. Ce n'est pas magie. Ce sont des methodes JavaScript qui agissent sur l'arbre HTML deja charge.

Chez DanielCraft, on prefere **`textContent`** pour debuter plutot que **`innerHTML`**. Pourquoi ? Parce que `textContent` met du texte, point. Pas de balises interpretees, pas de surprise si quelqu'un tape du code bizarre dans un champ. On prefere aussi les **classes CSS** plutot que d'eparpiller vingt lignes de `style.` en JavaScript. JS decide l'etat (actif, ouvert, erreur). CSS decide l'apparence. Lea toggle des classes `.active` sur des cartes clients. Max change un message de statut sur sa page plomberie. Sam montre la difference entre `textContent` et `innerHTML` avec un exemple prudent devant ses eleves. Trois metiers, meme reflexe : petit changement cible, bien place.

Tu as deja trouve la pancarte (chapitre precedent). Maintenant tu changes le texte dessus, tu colles un sticker colore (une classe), ou tu ajoutes une nouvelle pancarte avec `createElement` puis `appendChild`. Le magasin evolue sans reconstruire le batiment entier. Lea appelle ca "chirurgie locale". Max prefere ca aux "tout casser et recommencer". Sam dit : "le DOM, c'est la maquette vivante de ta page - pas le fichier sur le disque, la copie en cours dans le navigateur".

:::retenir
Trouve d'abord, modifie ensuite. `textContent` pour du texte simple. `classList` pour l'etat. `createElement` + `appendChild` pour ajouter.
:::

## Ce que ce n'est pas

Ce n'est pas encore les evenements clic - on y va juste apres. Ici, tu changes souvent au chargement de la page, pas en reaction a un geste utilisateur. Ce n'est pas reecrire tout le `body` pour changer un mot : c'est chirurgie locale, pas demolition totale. Ce n'est pas `innerHTML` avec des donnees non fiables venant de l'utilisateur : la, tu ouvres la porte aux bugs et aux failles. Et ce n'est pas styler vingt proprietes en JS si une seule classe CSS suffit. JS decide. CSS habille. Ne melange pas les roles.

Ce n'est pas non plus "modifier le fichier HTML sur disque". Quand tu changes le DOM en JavaScript, tu changes la page en memoire. Au prochain refresh, tu repars du fichier original. C'est normal. C'est le fonctionnement du web. Lea le rappelle souvent aux clients qui s'attendent a ce que le script "ecrive dans le HTML" comme dans Word.

## Changer le texte

```js
const titre = document.querySelector("#titre");
titre.textContent = "Nouveau titre";
```

`textContent` remplace tout le texte visible de l'element. Simple. Sur. Pour debuter, c'est ton outil numero un. `innerHTML` peut interpreter des balises HTML : utile si tu sais ce que tu fais, mais plus risque si le contenu vient de l'utilisateur ou d'une source externe. Lea a deja vu un client injecter du HTML casse parce qu'il croyait que "innerHTML = plus fort". Non. Plus puissant, pas plus sur.

## Classes, style et creation

```js
const carte = document.querySelector(".carte");
carte.classList.add("active");
carte.classList.remove("active");
carte.classList.toggle("active");

titre.style.color = "teal"; // ok pour tester
// Sur un vrai projet, prefere souvent les classes

const p = document.createElement("p");
p.textContent = "Je viens d'apparaitre";
document.body.appendChild(p);
```

Le couple **`classList`** + CSS est elegant : tu ajoutes `.active` en JS, tu definis `.active { background: gold; }` en CSS. Tu changes toute la charte sans retoucher dix scripts. `createElement` cree l'element en memoire. **`appendChild`** l'accroche au document pour qu'il devienne visible. Sans `appendChild`, tu as un element fantome : il existe en JS, mais personne ne le voit. Pour un etat (actif, ouvert, erreur), cree une classe CSS et toggle-la en JS. Moins de `style.` eparpilles, plus facile a maintenir.

:::attention
`createElement` seul ne suffit pas. Il faut `appendChild` (ou un equivalent) pour que l'element apparaisse dans la page.
:::

## Petite histoire

Lea remplacait des blocs entiers en `innerHTML` pour mettre a jour une liste de temoignages. Chaque fois, les ecouteurs d'evenements qu'elle avait branches sur les boutons "lire plus" disparaissaient. Elle est passee a des updates ciblees : changer le texte d'un `p`, toggle une classe sur un `div`. Probleme resolu en une session. Max mettait dix proprietes `style.` en ligne sur son bandeau de statut. Sam lui a dit : "une classe `.highlight`, c'est tout". Au prochain changement de charte graphique, Max a gagne une heure. Trois lecons, un meme reflexe : petit changement visible, bien place, testable tout de suite.

## Erreur classique

Modifier sans verifier que l'element existe : si `querySelector` renvoie `null`, tu plantes. Utiliser `innerHTML` pour du texte simple : c'est comme utiliser un marteau pour visser. Oublier `appendChild` apres `createElement` : l'element reste invisible. Croire que changer le JS change le fichier HTML sur disque : non, ca change la page en memoire. Au refresh, tu repars du fichier. Autre piege : mettre le script avant que le HTML existe. On y revient souvent. Script avant `</body>`, selecteur correct, element present.

## En vrai

Ouvre une page avec un paragraphe et un titre. Change le texte du paragraphe au chargement avec `textContent`. Ajoute une classe `highlight` a un titre (avec le CSS correspondant dans ta feuille de style). Cree un `p` dynamiquement avec ton prenom et ajoute-le au body. Tu dois voir les trois changements sans cliquer encore. Si ca marche, tu as le geste. Le chapitre suivant branchera l'interaction. Si quelque chose manque, loggue l'element : `null` ? Corrige avant de paniquer.

## A toi

Cree un `p` dynamiquement avec ton prenom et ajoute-le au body. Toggle une classe sur un bouton au chargement (meme sans clic encore : tu peux toggle au load pour tester). Verifie que le CSS de la classe existe vraiment. Prepare le terrain pour les evenements. Style DanielCraft : petit changement visible, puis on branche l'interaction au chapitre suivant. Note en une ligne ce que tu as change a l'ecran.
