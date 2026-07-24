# Chapitre 3 - JSON, le format des donnees voyageuses

Quand ta page parle a un serveur, elle n'envoie pas un objet JavaScript magique. Elle envoie du texte. JSON, c'est une facon d'ecrire ce texte pour que tout le monde se comprenne : navigateur, serveur, API meteo, boutique en ligne...

JSON veut dire "JavaScript Object Notation". Le nom fait peur. L'idee est simple : des donnees rangees comme des objets et des tableaux, mais en texte.

## A quoi ca ressemble

Voici une fiche produit en JSON :

```json
{
  "nom": "Casque audio",
  "prix": 59.9,
  "enStock": true,
  "tags": ["son", "promo"]
}
```

Et une liste :

```json
[
  { "ville": "Paris", "temp": 18 },
  { "ville": "Lyon", "temp": 16 }
]
```

Tu reconnais les objets `{ }`, les tableaux `[ ]`, les chaines entre guillemets doubles, les nombres, `true` / `false`, et `null`. En JSON "strict", les cles sont toujours entre guillemets doubles. Pas de fonction. Pas de commentaire.

## De texte vers objet : parse

Ta page recoit souvent une chaine. Pour travailler avec, tu la transformes en vrai objet JS.

```js
const texte = '{"nom":"Casque audio","prix":59.9}';
const produit = JSON.parse(texte);

console.log(produit.nom);   // Casque audio
console.log(produit.prix);  // 59.9
```

`JSON.parse` lit le texte et construit l'objet. Si le texte est casse, ca plante. On verra les erreurs plus loin.

## D'objet vers texte : stringify

L'inverse : tu as un objet JS, tu veux l'envoyer ou le stocker.

```js
const contact = {
  nom: "Lea",
  email: "lea@exemple.fr",
  message: "Bonjour, je veux un devis."
};

const texte = JSON.stringify(contact);
console.log(texte);
// {"nom":"Lea","email":"lea@exemple.fr","message":"Bonjour, je veux un devis."}
```

Utile pour `fetch` en POST, pour `localStorage`, pour un fichier... DanielCraft utilise souvent ce reflexe : objet en memoire pour travailler, JSON en texte pour voyager.

## Pieges courants

Premier piege : confondre objet JS et JSON. En JS, tu peux ecrire `{ nom: "Lea" }` avec des guillemets simples autour des valeurs, et parfois sans guillemets sur les cles. En JSON "vrai", les cles et les chaines sont en guillemets doubles.

Deuxieme piege : `JSON.parse` sur quelque chose qui n'est pas du JSON.

```js
JSON.parse("salut"); // erreur
JSON.parse("{nom: Lea}"); // erreur (pas de guillemets)
```

Troisieme piege : croire que `stringify` garde les fonctions. Non. Les fonctions disparaissent. Les dates deviennent des chaines. Les `undefined` sautent souvent. JSON transporte des donnees, pas du comportement.

Quatrieme piege : parser deux fois, ou stringifier deux fois, et se retrouver avec une chaine bizarre.

```js
const dejaTexte = '{"a":1}';
const encore = JSON.stringify(dejaTexte);
// result: "\"{\\\"a\\\":1}\""  -> un vrai bordel
```

Regle simple : parse quand tu recois du texte JSON. Stringify quand tu veux produire du texte JSON. Une fois suffit.

## Exemple concret : todo en texte

```js
const taches = [
  { id: 1, titre: "Acheter du pain", faite: false },
  { id: 2, titre: "Appeler Lea", faite: true }
];

const pourStockage = JSON.stringify(taches);
// plus tard...
const relues = JSON.parse(pourStockage);
console.log(relues[0].titre); // Acheter du pain
```

Tu peux imaginer la meme chose avec une reponse meteo ou une liste de produits d'une API.

## En vrai

Ouvre la console du navigateur. Colle un petit `JSON.parse('{"ville":"Nantes","temp":14}')`. Affiche `ville` et `temp`. Puis `JSON.stringify` un objet de ton choix. Regarde le texte produit. C'est tout. Mais ce geste-la, tu vas le refaire cent fois.

## A toi

Cree un objet `commande` avec client, produits (tableau de noms), et total. Transforme-le en texte JSON. Reparse-le. Affiche une phrase : "Commande de X pour Y euros". Si ca marche, JSON n'a plus de mystere.
