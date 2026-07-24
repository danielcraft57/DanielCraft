# Chapitre 2 - Ou ecrire du JavaScript ?

Trois facons simples. On commence par la plus claire.

## 1. Dans un fichier .js (le mieux)

Cree `script.js` :

```js
console.log("Salut depuis mon fichier !");
```

Dans ton HTML, juste avant `</body>` :

```html
<script src="script.js"></script>
```

Pourquoi avant `</body>` ?
Parce que la page est deja la. Plus simple pour debuter.

## 2. Direct dans le HTML (pour tester)

```html
<script>
  console.log("Coucou");
</script>
```

Pratique 2 minutes. Sur un vrai projet, prefere un fichier `.js`.

## 3. La console du navigateur

1. Ouvre ta page
2. F12 (outils developpeur)
3. Onglet Console
4. Tape : `console.log("test")`
5. Entree

`console.log` = "affiche ca dans la console".
C'est ton ami pour verifier que ca marche.

## Mini structure de dossier

```
mon-site/
  index.html
  style.css
  script.js
```

## A toi

1. Cree `index.html` + `script.js`
2. Relie-les
3. Affiche ton prenom avec `console.log`
4. Ouvre la console. Si tu le vois : gagne.

## Erreur classique

Tu mets le script en haut du HTML, avant le contenu. Le JS tourne avant que les elements existent. Resultat : erreur ou `null`.

Mauvais :

```html
<head>
  <script src="script.js"></script>
</head>
<body>
  <h1 id="titre">Salut</h1>
</body>
```

Bon : le `<script>` juste avant `</body>`, ou utilise `defer` si tu le mets dans le `<head>`.

## Exemple complet

Structure complete qui marche du premier coup :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Mon premier JS</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1 id="titre">Coucou</h1>
  <script src="script.js"></script>
</body>
</html>
```

```js
// script.js
const titre = document.querySelector("#titre");
console.log("Le titre dit :", titre.textContent);
console.log("Script charge avec succes !");
```

Ouvre la console. Tu dois voir les deux lignes.

## Mini defi

- Cree le dossier `mon-site/` avec les 3 fichiers
- Dans `script.js`, affiche ton age et ta ville
- Change le chemin volontairement (`scrip.js`) et note l'erreur dans la console
- Remets le bon chemin et verifie que ca marche

## A retenir

- Fichier `.js` separe = la bonne habitude
- `<script src="...">` juste avant `</body>` pour debuter
- `console.log` = ton outil de debug numero 1
- La console (F12) permet de tester du code vite


## En vrai, sur le terrain

Ouvre la console. Retape l'exemple a la main.
Change une valeur. Regarde ce qui bouge. C'est comme ca que ca rentre.

## Mini defi

Inventes un tout petit cas perso (ton prenom, ton score, ton jeu prefere).
Repars de l'exemple avec TES donnees. Si ca marche, c'est bon signe.
