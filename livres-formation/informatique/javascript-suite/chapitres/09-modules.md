# Chapitre 9 - Modules : decouper le code

Quand ton fichier app.js fait 400 lignes, tu te perds. Tu cherches une fonction pendant cinq minutes. Tu as peur de casser quelque chose en touchant une ligne au milieu. Tu recopies la meme logique fetch dans trois endroits et tu ne sais plus laquelle est a jour. Les modules existent pour ca : un fichier, une responsabilite, des imports et exports explicites.

En JavaScript moderne, tu ecris export pour sortir une fonction ou une valeur d'un fichier, et import pour la recuperer ailleurs. Dans le HTML, tu charges ton point d'entree avec type="module". Le navigateur sait alors que les fichiers peuvent s'importer entre eux avec des chemins relatifs.

```html
<script type="module" src="main.js"></script>
```

Chez DanielCraft, on conseille de decouper des que tu recopies la meme fonction deux fois, ou des que tu ne trouves plus rien sans Ctrl+F. Lea decoupe en api.js, afficher.js et main.js des la deuxieme feature. Max met tout dans un fichier au debut, puis migre quand ca devient confus. Sam montre les deux phases pour que ses eleves comprennent le pourquoi.

## Un exemple simple

Fichier api.js :

```js
export async function chargerListe(url) {
  const reponse = await fetch(url);
  if (!reponse.ok) throw new Error("Chargement impossible");
  return reponse.json();
}
```

Fichier main.js :

```js
import { chargerListe } from "./api.js";

const produits = await chargerListe("/api/produits.json");
console.log(produits);
```

Tu vois l'idee. main.js orchestre. api.js parle au reseau. Plus tard, tu peux ajouter afficher.js pour le DOM. Chaque fichier reste court et se presente en une phrase : "Moi, je charge les donnees." "Moi, je dessine la liste." "Moi, je branche les boutons." Imagine une cuisine. Un poste pour les entrees, un pour les plats, un pour le service. Chacun a son role. Si le serveur commence a cuisiner, le chaos arrive. Si api.js manipule le DOM et que afficher.js appelle fetch, pareil. Un role par fichier.

## Pieges a connaitre

Les modules fonctionnent mieux avec un petit serveur local (pas toujours en ouvrant le fichier en file://). Si tu testes avec Live Server, VS Code, ou python -m http.server, tu es bien. Les chemins relatifs comptent : ./api.js veut dire "dans le meme dossier". Oublie le ./ et certains navigateurs se plaignent. N'exporte que ce qui est utile. Tout exporter "au cas ou" reforge le desordre sous une autre forme.

Tu peux aussi faire export default pour une seule export principale, mais named exports (export function ...) sont souvent plus clairs quand tu as plusieurs fonctions.

## Petite histoire

Lea a herite d'un projet client : un seul fichier de 900 lignes. Elle a extrait chargerProduits dans api.js et afficherProduits dans afficher.js en une matinee. Le client n'a rien vu changer cote utilisateur. Mais Lea a retrouve sa sanite mentale. Max, lui, a attendu trop longtemps et a du tout refaire. Morale : decoupe tot, meme pour un exercice.

## Erreur classique

Oublier type="module" dans le script HTML : les import ne marchent pas. Tester en file:// et conclure que "les modules sont casses" alors qu'il faut un serveur local. Mettre fetch et manipulation DOM dans le meme fichier "parce que c'est plus rapide" et regretter deux semaines plus tard.

## En vrai

Sur un vrai projet, tu n'as pas besoin de vingt fichiers le premier jour. Trois fichiers clairs battent un monstre de 800 lignes. Ouvre un vieux script unique. Identifie deux fonctions exportables. Ecris leurs noms d'export. Tu n'as pas besoin de tout migrer maintenant. Juste sentir la decoupe.

## A toi

Prends un vieux script unique (ou celui du mini-projet). Identifie deux fonctions que tu pourrais sortir dans api.js et afficher.js. Ecris mentalement leurs signatures export. Puis fais la migration reelle si tu as le temps. L'atelier modules au chapitre 16 te guidera pas a pas.

## import vs export : le vocabulaire

export function maFonction() {} rend la fonction disponible a l'exterieur du fichier. import { maFonction } from "./fichier.js" la recupere. Les accolades importent un nom precis. Les modules ES6 utilisent des chemins relatifs avec extension .js explicite (bonne pratique navigateur). Si tu vois import truc from "lodash" sans chemin, c'est souvent un bundler (hors scope ici).

## Cycle de vie module

Chaque module n'est evalue qu'une fois par page. Les imports sont "live bindings" pour les variables exportees, mais pour commencer retiens surtout : une fonction exportee est une fonction partagee, pas recopiee. Pratique pour garder une seule fonction chargerListe.

## Zoom DanielCraft

Quand Lea livre un petit site vitrine avec fetch, elle livre souvent index.html, styles.css, main.js, api.js, afficher.js. Le client peut lire la structure. Sam note les eleves sur la clarte des exports. Max n'a pas besoin de tout comprendre, mais il sait ou modifier le texte d'erreur (souvent afficher.js ou main.js). C'est deja une victoire organisationnelle.
