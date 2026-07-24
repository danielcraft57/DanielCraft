# Chapitre 9 - Modules : decouper le code

Quand ton fichier `app.js` fait 400 lignes, tu te perds. Tu cherches une fonction pendant cinq minutes. Tu as peur de casser quelque chose en touchant une ligne. Les modules existent pour ca : un fichier, une responsabilite.

En JavaScript moderne, tu ecris `export` pour sortir une fonction d'un fichier, et `import` pour la recuperer ailleurs. Dans le HTML, tu charges ton point d'entree avec `type="module"`.

```html
<script type="module" src="main.js"></script>
```

## Un exemple simple

Fichier `api.js` :

```js
export async function chargerListe(url) {
  const reponse = await fetch(url);
  if (!reponse.ok) throw new Error("Chargement impossible");
  return reponse.json();
}
```

Fichier `main.js` :

```js
import { chargerListe } from "./api.js";

const produits = await chargerListe("/api/produits.json");
console.log(produits);
```

Tu vois l'idee. `main.js` orchestre. `api.js` parle au reseau. Plus tard, tu peux ajouter `afficher.js` pour le DOM. Chaque fichier reste court.

## Pieges a connaitre

Les modules fonctionnent mieux avec un petit serveur local (pas toujours en ouvrant le fichier en `file://`). Si tu testes avec Live Server, VS Code, ou `python -m http.server`, tu es bien.

Les chemins relatifs comptent : `./api.js` veut dire "dans le meme dossier". Oublie le `./` et certains navigateurs ralentissent ou se plaignent.

N'exporte que ce qui est utile. Tout exporter "au cas ou" reforge le desordre.

## En vrai

Sur un vrai projet, tu n'as pas besoin de vingt fichiers le premier jour. Trois fichiers clairs battent un monstre de 800 lignes. DanielCraft te conseille de decouper des que tu recopies la meme fonction deux fois.

## A toi

Prends un vieux script unique. Identifie deux fonctions que tu pourrais sortir dans un autre fichier. Ecris mentalement leurs noms d'export. Tu n'as pas besoin de tout migrer maintenant. Juste sentir la decoupe.
