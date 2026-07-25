# Chapitre 4 - fetch GET : demander des infos

Jusqu'ici, tes donnees vivaient dans ton fichier ou dans le code que tu avais ecrit toi-meme. Maintenant, ta page peut demander des infos ailleurs : une API meteo, une liste de produits, un fichier JSON heberge sur un serveur, une base de donnees exposee via une URL. **fetch** est l'outil moderne du navigateur pour ca. En mode **GET**, le mode par defaut, tu dis simplement : "donne-moi cette ressource a cette adresse." C'est le geste qui transforme une page statique en page vivante.

Chez DanielCraft, on resume le flux en quatre mots : demander, attendre, lire, montrer. Lea charge les produits d'une boutique. Max affiche la meteo de sa ville sur son site. Sam recupere une liste de citations pour un exercice. Le geste est identique ; seules les URLs et les proprietes JSON changent. Une fois ce schema dans les doigts, tu pourras brancher n'importe quelle source compatible.

Ta page envoie une demande a une adresse (une **URL**). Le serveur repond. Tu lis la reponse. Souvent, la reponse est du JSON. Tu le parses, souvent avec **.json()**, puis tu affiches dans le DOM. C'est le coeur de beaucoup d'applications web simples : pages qui affichent des donnees vivantes sans rechargement complet. L'utilisateur clique, attend un instant, voit apparaitre une liste : la magie n'en est pas une, c'est ce flux-la.

## Premier appel

Il existe des API publiques pour s'entrainer (JSONPlaceholder, Open-Meteo, etc.). L'exemple ci-dessous utilise une URL fictive pour rester clair. Le schema reste le meme partout. Ne te crispe pas sur l'adresse exacte : concentre-toi sur la chaine d'appels.

```js
fetch("https://exemple.api/produits")
  .then(function (reponse) {
    return reponse.json();
  })
  .then(function (produits) {
    console.log(produits);
  });
```

Que se passe-t-il ? fetch part chercher l'URL. Quand la reponse HTTP arrive, le premier then recoit un objet **Response**. reponse.json() lit le corps et le transforme en objet ou tableau JS (comme un JSON.parse intelligent). Le second then recoit les donnees pretes a l'emploi. On detaillera les promesses au chapitre suivant. Pour l'instant, retiens la chaine : fetch -> json -> utiliser.

:::astuce
N'oublie jamais return devant reponse.json() dans un then. Sans return, le then suivant recoit undefined et tu cherches le bug pendant une heure.
:::

## Afficher dans la page

Imagine une liste de produits affichee a l'utilisateur. Pendant le chargement, tu montres un message. Ensuite tu vides la liste et tu ajoutes les elements un par un. Ce rythme "avant / pendant / apres" est deja une habitude pro.

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
      li.textContent = p.nom + " - " + p.prix + " EUR";
      liste.appendChild(li);
    }
  });
```

Tu vois le pattern. Pendant le chargement, tu montres un message. Ensuite tu vides la liste et tu ajoutes les elements un par un. Lea utilise exactement ce schema pour les catalogues clients. Simple, lisible, efficace. Plus tard, async/await rendra ce code encore plus lineaire, mais le flux mental reste le meme.

## Meteo : autre exemple mental

Tu appelles une URL avec une ville en parametre. Tu recois { "ville": "Paris", "temp": 18, "ciel": "nuageux" }. Tu ecris dans un paragraphe : "A Paris, il fait 18 degres, ciel nuageux." Memes etapes. Seules les proprietes et le texte affiche changent. Max a monte sa widget meteo locale avec ce principe en une soiree. Sam fait faire la meme chose a ses eleves avec des citations : meme ossature, autre contenu.

## Ce que fetch renvoie vraiment

Attention : fetch reussit souvent meme si le serveur dit "404 introuvable" ou "500 erreur serveur". Techniquement, la requete reseau a abouti. Le code HTTP peut etre une erreur metier. On traitera response.ok au chapitre erreurs. Pour ce chapitre, concentre-toi sur le chemin heureux : URL correcte, JSON valide, affichage propre. Mais garde en tete que "pas d'exception" ne veut pas dire "tout va bien". C'est l'un des pieges les plus importants du livre.

:::attention
fetch qui "marche" (pas d'exception) ne veut pas dire que les donnees sont bonnes. Un 404 peut arriver sans planter. On corrigera ca avec response.ok au chapitre 7.
:::

## Petite histoire

Sam voulait afficher des citations dans son exercice en ligne. Il a ouvert l'URL du fichier JSON dans le navigateur, a vu le texte brut, puis a ecrit dix lignes de fetch. Les eleves ont vu les citations apparaitre sans recharger la page. "C'est magique" ont-ils dit. Non : c'est fetch. La magie, c'est de comprendre le flux. Lea, elle, rappelle toujours d'ouvrir d'abord l'URL dans le navigateur : si le JSON n'est pas la, inutile de blamer le JavaScript.

## Erreur classique

Oublier return reponse.json() dans le then. Si tu ecris seulement reponse.json() sans return, le then suivant recoit undefined. Autre classique : traiter la reponse comme du JSON alors que c'est du HTML d'erreur. Ou appeler une mauvaise URL et croire que "fetch est casse" alors que c'est l'adresse qui est fausse. Ou tester en ouvrant le fichier HTML en file:// alors que fetch exige souvent un serveur local.

## En vrai

Cherche une API publique simple ou prepare un fichier produits.json a cote de ta page. Ouvre l'URL dans le navigateur. Regarde le JSON brut. Puis tente un petit fetch dans la console ou dans un fichier servi par un mini serveur local (Live Server, python -m http.server). Le but : voir des vraies donnees arriver dans ta page. Si ca echoue en file://, ce n'est pas un echec personnel : c'est le navigateur qui protege.

## A toi

Ecris une fonction chargerProduits(url) qui fait un GET, lit le JSON, et affiche chaque nom dans une liste ul. Meme avec des donnees fictives en local (un fichier produits.json a cote), le geste compte. Si tu n'as pas encore de serveur local, ecris le code quand meme : tu le brancheras au chapitre async/await avec une syntaxe encore plus lisible.

:::retenir
GET avec fetch = demander une URL, lire .json(), afficher - et se souvenir que "pas d'exception" n'est pas encore "succes".
:::
