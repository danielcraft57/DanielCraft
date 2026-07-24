# Chapitre 4 - fetch GET : demander des infos

Jusqu'ici, tes donnees vivaient dans ton fichier. Maintenant, ta page peut demander des infos ailleurs : une API meteo, une liste de produits, un fichier JSON sur un serveur.

`fetch` est l'outil moderne du navigateur pour ca. En mode GET (le mode par defaut), tu dis : "donne-moi cette ressource".

## L'idee en une image

Ta page envoie une demande a une adresse (une URL). Le serveur repond. Tu lis la reponse. Souvent, la reponse est du JSON. Tu le parses (souvent avec `.json()`), puis tu affiches.

Chez DanielCraft, on resume comme ca : demander, attendre, lire, montrer.

## Premier appel

Il existe des API publiques pour s'entrainer. L'exemple ci-dessous utilise une URL fictive pour rester clair. Le schema reste le meme partout.

```js
fetch("https://exemple.api/produits")
  .then(function (reponse) {
    return reponse.json();
  })
  .then(function (produits) {
    console.log(produits);
  });
```

Que se passe-t-il ? `fetch` part chercher l'URL. Quand la reponse HTTP arrive, le premier `then` recoit un objet `Response`. `reponse.json()` lit le corps et le transforme en objet/tableau JS (comme un `JSON.parse` intelligent). Le second `then` recoit les donnees pretes.

On detaillera les promesses au chapitre suivant. Pour l'instant, retiens la chaine : fetch -> json -> utiliser.

## Afficher dans la page

Imagine une liste de produits.

```html
<ul id="liste"></ul>
<p id="statut">Chargement...</p>
```

```js
const liste = document.querySelector("#liste");
const statut = document.querySelector("#statut");

fetch("https://exemple.api/produits")
  .then(function (reponse) {
    return reponse.json();
  })
  .then(function (produits) {
    statut.textContent = produits.length + " produits trouves";
    liste.innerHTML = "";

    for (const p of produits) {
      const li = document.createElement("li");
      li.textContent = p.nom + " - " + p.prix + " €";
      liste.appendChild(li);
    }
  });
```

Tu vois le pattern. Pendant le chargement, tu peux montrer un message. Ensuite tu vides la liste et tu ajoutes les elements. C'est le coeur de beaucoup d'apps web simples.

## Meteo : autre exemple mental

Tu appelles une URL avec une ville. Tu recois `{ "ville": "Paris", "temp": 18, "ciel": "nuageux" }`. Tu ecris dans un `p` : "A Paris, il fait 18°C, ciel nuageux." Memes etapes. Seules les proprietes changent.

## Ce que fetch renvoie vraiment

Attention : `fetch` reussit souvent meme si le serveur dit "404 introuvable". Techniquement, la requete reseau a marche. Le code HTTP peut etre une erreur. On traitera `response.ok` au chapitre erreurs. Pour ce chapitre, concentre-toi sur le chemin heureux : URL ok, JSON ok, affichage ok.

## Erreur classique

Oublier `return reponse.json()`. Si tu ecris seulement `reponse.json()` sans `return` dans le `then`, le suivant recoit `undefined`. Autre classique : traiter la reponse comme du JSON alors que c'est du HTML d'erreur. Ou appeler une mauvaise URL et croire que "fetch est casse".

## En vrai

Cherche une API publique simple (JSONPlaceholder, Open-Meteo, etc. selon ce qui est dispo chez toi). Ouvre l'URL dans le navigateur. Regarde le JSON brut. Puis tente un petit `fetch` dans la console sur une page autorisee, ou dans un fichier local servi correctement. Le but : voir des vraies donnees arriver.

## A toi

Ecris une fonction `chargerProduits(url)` qui fait un GET, lit le JSON, et affiche chaque `nom` dans une liste. Meme avec des donnees fictives en local (un fichier `produits.json` a cote), le geste compte. Si tu n'as pas encore de serveur local, ecris le code quand meme : tu le brancheras au prochain chapitre avec async/await.
