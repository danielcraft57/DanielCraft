# Chapitre 3 - JSON, le format des donnees voyageuses

Quand ta page parle a un serveur, elle n'envoie pas un objet JavaScript magique qui traverse l'internet tel quel. Elle envoie du texte. **JSON**, c'est la facon standard d'ecrire ce texte pour que tout le monde se comprenne : navigateur, serveur, API meteo, boutique en ligne, application mobile. JSON veut dire JavaScript Object Notation. Le nom fait peur. L'idee est simple : des donnees rangees comme des objets et des tableaux, mais ecrites en texte pur, lisible par une machine et par un humain. Une fois ce reflexe acquis, fetch devient beaucoup moins mysterieux.

Chez DanielCraft, on resume souvent ainsi : objet en memoire pour travailler, JSON en texte pour voyager. Lea manipule des fiches produit. Max envoie des demandes de devis. Sam prepare des listes de questions pour ses quiz. Dans tous les cas, le meme reflexe revient : **JSON.stringify** pour produire, **JSON.parse** pour consommer. Tu vas le refaire cent fois dans une vie de front : autant le rendre automatique des maintenant.

Imagine une valise etiquetee. Dedans, ce n'est pas l'objet lui-meme, c'est une fiche qui decrit l'objet : nom, prix, en stock oui ou non. Le transporteur (le reseau) ne transporte que la fiche. A l'arrivee, tu reconstruis l'objet en lisant la fiche. parse lit la fiche. stringify ecrit la fiche. Si la fiche est dechiree ou ecrite dans un autre langage, tu ne reconstruis rien de fiable. D'ou l'importance de verifier avant de parser.

## A quoi ca ressemble

Voici une fiche produit en JSON. Tu peux la lire a voix haute : c'est presque du francais structure.

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

Tu reconnais les objets { }, les tableaux [ ], les chaines entre guillemets doubles, les nombres, true / false, et null. En JSON strict, les cles sont toujours entre guillemets doubles. Pas de fonction. Pas de commentaire. Pas de virgule en trop apres le dernier element (certains parseurs tolerent, d'autres non). Ce formalisme n'est pas du snobisme : c'est ce qui permet a des outils differents de se comprendre sans negociation.

## De texte vers objet : parse

Ta page recoit souvent une chaine de caracteres. Pour travailler avec, tu la transformes en vrai objet JS. Sans cette etape, tu ne peux pas faire data.nom ou data[0] de facon fiable.

```js
const texte = '{"nom":"Casque audio","prix":59.9}';
const produit = JSON.parse(texte);

console.log(produit.nom);   // Casque audio
console.log(produit.prix);  // 59.9
```

JSON.parse lit le texte et construit l'objet. Si le texte est casse (virgule en trop, guillemets manquants, HTML d'erreur a la place du JSON), ca plante. On verra la gestion d'erreurs au chapitre reseau. Pour l'instant, retiens : parse sur du vrai JSON uniquement. Si tu as un doute, ouvre la reponse dans l'onglet Network et regarde si ca commence bien par { ou [.

## D'objet vers texte : stringify

L'inverse : tu as un objet JS en memoire, tu veux l'envoyer ou le stocker. Le serveur ne "voit" pas ton objet vivant dans le navigateur. Il voit un corps de requete texte.

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

Utile pour fetch en POST, pour localStorage, pour ecrire dans un fichier cote serveur. Quand Lea envoie un formulaire contact, stringify transforme l'objet { nom, email, message } en corps de requete que le serveur peut lire. Sans stringify, tu risques d'envoyer la fameuse chaine "[object Object]" - un classique douloureux.

:::attention
Ne confonds pas objet JS et JSON. En JS, les cles peuvent parfois aller sans guillemets. En JSON strict, cles et chaines sont en guillemets doubles. parse sur du HTML d'erreur = explosion garantie.
:::

## Pieges courants

Premier piege : confondre objet JS et JSON. En JS, tu peux ecrire { nom: "Lea" } avec des guillemets simples parfois, et parfois sans guillemets sur les cles. En JSON vrai, les cles et les chaines sont en guillemets doubles. Deuxieme piege : JSON.parse sur quelque chose qui n'est pas du JSON.

```js
JSON.parse("salut"); // erreur
JSON.parse("{nom: Lea}"); // erreur (pas de guillemets sur les cles)
```

Troisieme piege : croire que stringify garde les fonctions. Non. Les fonctions disparaissent. Les dates deviennent des chaines ISO. Les undefined sautent souvent. JSON transporte des **donnees**, pas du comportement. Quatrieme piege : parser deux fois ou stringifier deux fois.

```js
const dejaTexte = '{"a":1}';
const encore = JSON.stringify(dejaTexte);
// resultat : une chaine avec des echappements bizarres
```

Regle simple : parse quand tu recois du texte JSON. Stringify quand tu veux produire du texte JSON. Une fois suffit. Si tu stringifies quelque chose qui est deja une chaine JSON, tu emballes du texte dans du texte : ca devient illisible pour le serveur.

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

Tu peux imaginer la meme chose avec une reponse meteo ou une liste de produits d'une API. Sam stocke ainsi ses listes de mots pour ses exercices. Max pourrait sauvegarder un brouillon de devis dans le navigateur. Le geste reste : objet -> texte pour voyager ou stocker, texte -> objet pour travailler.

## Petite histoire

Lea a recu une reponse API et a essaye JSON.parse dessus. Sauf que le serveur renvoyait une page HTML d'erreur 500, pas du JSON. Le parse a explose. Elle a appris a verifier response.ok avant de parser, et a regarder le Content-Type quand c'est disponible. Ce chapitre pose la base ; le chapitre erreurs reseau complete la protection. Sam montre souvent cette histoire a ses eleves pour qu'ils ne traitent jamais "toute reponse" comme du JSON sacre.

## Erreur classique

Traiter toute reponse HTTP comme du JSON sans verifier. Ou oublier stringify avant un POST et envoyer "[object Object]" au serveur. Ou copier-coller du JSON depuis un generateur en laissant une virgule finale : certains outils tolerent, JSON.parse strict non. Ou stringifier deux fois "pour etre sur" et produire une chaine echappee illisible.

## En vrai

Ouvre la console du navigateur. Colle un petit JSON.parse('{"ville":"Nantes","temp":14}'). Affiche ville et temp. Puis JSON.stringify un objet de ton choix. Regarde le texte produit. C'est tout. Mais ce geste-la, tu vas le refaire cent fois dans ta vie de dev front. Fais-le maintenant pour que ce soit automatique. Si tu as un fichier .json local, ouvre-le aussi dans l'editeur et compare a ce que parse attend.

## A toi

Cree un objet commande avec client (nom), produits (tableau de noms), et total (nombre). Transforme-le en texte JSON avec stringify. Reparse-le avec parse. Affiche une phrase : "Commande de X pour Y euros". Si ca marche sans erreur, JSON n'a plus de mystere pour toi. Passe ensuite au chapitre fetch pour voir ce texte voyager sur le reseau.

:::retenir
JSON = texte de voyage. parse pour lire, stringify pour envoyer - une fois suffit, et seulement sur du vrai JSON.
:::
