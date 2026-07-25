# Chapitre 2 - Ou ecrire du JavaScript ?

Tu sais deja ce que fait JavaScript : il reagit, il decide, il fait bouger la page. Maintenant, la question pratique : ou tu ecris ces instructions ? Pas dans le vide. Pas n'importe comment. Trois endroits existent quand tu debutes, et chacun a son role. Le plus important pour un vrai projet : un fichier **`.js`** separe, branche dans le HTML comme tu branches deja ton CSS. Tu crees `script.js`, tu y mets ton code, tu le relies avec un tag `<script src="script.js">` juste avant `</body>`. Le navigateur charge d'abord la page, puis le script. Les elements HTML existent deja. Ton code peut les trouver sans panique.

Chez DanielCraft, ce reflexe revient dans tous les livres informatique : structure propre, un fichier par role, pas de magma. Lea, freelance web, ne colle presque jamais de gros scripts dans le HTML une fois le projet depasse dix lignes. Max, artisan plombier avec sa page vitrine, a appris apres avoir perdu son compteur de devis dans un tas de balises qu'il n'osait plus toucher. Sam, enseignant, retire des points quand le script est "n'importe ou" dans la copie d'un eleve. Trois metiers, une meme discipline : savoir ou vit le code, et pourquoi.

Tu peux aussi ecrire un petit bloc `<script>` directement dans le HTML pour tester deux minutes. Ou taper dans la **console** du navigateur (F12) pour verifier une idee sans sauvegarder. Les trois servent. La discipline, c'est le fichier `.js` pour tout projet qui dure plus d'une session. La console pour l'exploration rapide. Le script inline pour le tout premier "coucou" qui te donne confiance.

:::retenir
Fichier `.js` separe pour les vrais projets. Console pour tester vite. Script avant `</body>` pour eviter les `null`.
:::

## Ce que ce n'est pas

Ce n'est pas "mettre le script n'importe ou et prier". Ce n'est pas encore une lecon sur `defer` ou `async` - tu les croiseras plus tard dans des tutos, pas besoin de tout maitriser aujourd'hui. Ce n'est pas une application Node.js ou un serveur : ici, on reste dans le navigateur, sur ta page HTML locale ou en ligne. Et ce n'est pas "ignorer la console" : si tu ne la regardes pas, tu rates la moitie des indices quand quelque chose ne marche pas.

Ce n'est pas non plus copier un script trouve en ligne sans comprendre ou il est branche. Le chemin du fichier, l'emplacement du tag `<script>`, ce sont des details qui font la difference entre "ca marche du premier coup" et "bouton mort depuis trois heures". Lea le dit souvent a ses stagiaires : le branchement, c'est la moitie du travail.

## Fichier .js (le mieux)

```js
console.log("Salut depuis mon fichier !");
```

Dans le HTML, juste avant `</body>` :

```html
<script src="script.js"></script>
```

**console.log** affiche dans la console. C'est ton ami pour verifier que le script est charge, que ta variable contient ce que tu crois, que ton selecteur a trouve quelque chose. Sans lui, tu codes a l'aveugle. Lea loggue presque tout au debut. Sam exige un log par exercice : si tu ne peux pas montrer ce que tu vois, tu ne peux pas prouver que ca marche.

Le HTML est la scene, le CSS le decor, le fichier JS le livret. Tu le branches en fin de scene pour que les elements existent deja. Si tu lis le livret trop tot, tu cherches un bouton qui n'est pas ne : tu obtiens **`null`**. Lea resume : "la page d'abord, le cerveau ensuite".

:::astuce
Place toujours le `<script src="...">` juste avant `</body>` pour debuter. Moins de `null`, moins de panique.
:::

## Direct dans le HTML / console

```html
<script>
  console.log("Coucou");
</script>
```

Pratique deux minutes pour un test ultra rapide. Sur un vrai projet, prefere le fichier `.js` separe. Et la console : F12, onglet Console, tape `console.log("test")`, Entree. Ideal pour verifier une idee en trente secondes. Max adore ca pour "est-ce que 19 + 3 donne bien 22 ?". Sam fait tester la console avant le premier fichier.

## Mini structure

```
mon-site/
  index.html
  style.css
  script.js
```

Trois fichiers, trois roles. Tu sais ou chercher quand ca casse. Chez DanielCraft, cette arborescence revient dans presque tous les mini-projets. Lea cree ce trio des la premiere heure. Max l'a copie pour sa page artisan. Sam le fait reproduire en classe.

## Petite histoire

Lea a passe une heure sur un "bouton mort" pour un client fleuriste : le script etait dans le `head`, le bouton plus bas dans le body. `querySelector` renvoyait `null` parce que le bouton n'existait pas encore au moment ou le script s'executait. Elle a deplace le script avant `</body>`. Marche du premier coup. Quarante minutes perdues pour une ligne deplacee - mais quarante minutes qu'elle n'oubliera plus.

Max avait ecrit `scrip.js` au lieu de `script.js` dans le `src`. La console disait 404. Il a lu le message, corrige une lettre, souri. Sam casse volontairement le chemin en cours pour forcer la lecture d'erreur. Les eleves apprennent a regarder avant de reecrire dix lignes de logique qui n'etaient pas le probleme.

## Erreur classique

Script trop haut dans le HTML, avant les elements dont tu as besoin. Resultat : erreur ou `null`. Mauvais chemin de fichier (une lettre suffit : `scrip.js` vs `script.js`). Oublier d'ouvrir la console et croire que "rien ne se passe" alors que le log est la, invisible si tu ne regardes pas. Autre piege : tout coller dans le HTML puis ne plus oser toucher au code par peur de tout casser. Le fichier separe rassure : un endroit, une verite, tu peux modifier sans panique.

:::attention
Si tu as `null` sur un element, verifie d'abord l'emplacement du script et le chemin du fichier - avant de changer dix lignes de logique.
:::

## Exemple complet

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Mon premier JS</title>
</head>
<body>
  <h1 id="titre">Coucou</h1>
  <script src="script.js"></script>
</body>
</html>
```

```js
const titre = document.querySelector("#titre");
console.log("Le titre dit :", titre.textContent);
console.log("Script charge avec succes !");
```

Ouvre la page. Ouvre la console. Tu dois voir les deux messages. Si tu ne vois rien, le chemin ou l'emplacement du script est suspect. Lis l'erreur. Repare. C'est le geste DanielCraft : observer, comprendre, corriger - pas deviner.

## En vrai

Cree `index.html` + `script.js`. Relie-les. Affiche ton prenom avec `console.log`. Ouvre la console. Si tu le vois : gagne. Puis casse le chemin volontairement (`scriptt.js`), lis l'erreur 404, repare. Ce geste vaut plus qu'une page de theorie. Lea le fait avec chaque nouveau stagiaire. Max l'a fait une fois, il s'en souvient encore. Toi aussi, tu peux graver ce reflexe aujourd'hui.

## A toi

Affiche ton age et ta ville dans la console. Invente un tout petit cas perso (ton jeu prefere, ton animal). Note en une ligne ou tu as place le script et pourquoi. Reflexe DanielCraft : savoir expliquer son branchement, pas juste copier-coller. Si tu ne peux pas expliquer le `src` a voix haute, tu ne le maitrises pas encore - et c'est ok, tu le notes et tu recommences.
