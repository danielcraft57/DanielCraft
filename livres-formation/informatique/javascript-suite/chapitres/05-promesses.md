# Chapitre 5 - Les promesses, sans jargon opaque

Quand tu appelles `fetch`, le resultat n'arrive pas tout de suite. Le reseau prend du temps. JavaScript ne peut pas rester bloque a attendre comme un ascenseur en panne : la page doit rester utilisable.

Une promesse, c'est un objet qui dit : "je te donnerai une valeur plus tard, ou une erreur". Tu branches ensuite ce qui se passe en cas de succes (`then`) ou d'echec (`catch`).

## Image mentale

Tu commandes une pizza. Le restaurant te donne un ticket. Ce ticket n'est pas la pizza. C'est la promesse de la pizza. Plus tard, soit tu recois la pizza (`then`), soit on t'annonce un probleme (`catch`).

`fetch` te rend ce ticket tout de suite. Les donnees viennent apres.

## then : quand ca marche

```js
fetch("https://exemple.api/meteo?ville=Paris")
  .then(function (reponse) {
    return reponse.json();
  })
  .then(function (data) {
    console.log("Temperature :", data.temp);
  });
```

Chaque `then` peut renvoyer une nouvelle valeur. Le `then` suivant la recoit. C'est pour ca qu'on ecrit `return reponse.json()` : `json()` renvoie aussi une promesse (parce que lire le corps prend un peu de temps).

## catch : quand ca casse

```js
fetch("https://exemple.api/meteo?ville=Paris")
  .then(function (reponse) {
    return reponse.json();
  })
  .then(function (data) {
    console.log(data.temp);
  })
  .catch(function (erreur) {
    console.log("Probleme :", erreur.message);
  });
```

Si le reseau tombe, ou si `json()` explose sur un texte invalide, tu tombes dans `catch`. Un seul `catch` a la fin peut couvrir la chaine. Pratique.

## Pourquoi pas juste "attendre" ?

Parce que JS dans le navigateur est evenementiel. Pendant que la requete voyage, l'utilisateur peut encore cliquer, scroller, ecrire. Les promesses permettent de dire "continue, et rappelle-moi quand c'est pret".

Tu n'as pas besoin de connaitre tous les etats internes (`pending`, `fulfilled`, `rejected`) pour commencer. Retiens : une promesse aboutit ou echoue ; tu branches `then` et `catch`.

## Chainer sans se noyer

Evite les pyramides. Preferes une ligne claire :

```js
function afficherMeteo(ville) {
  return fetch("https://exemple.api/meteo?ville=" + encodeURIComponent(ville))
    .then(function (reponse) {
      return reponse.json();
    })
    .then(function (data) {
      document.querySelector("#meteo").textContent =
        "A " + data.ville + ", " + data.temp + "°C";
    })
    .catch(function () {
      document.querySelector("#meteo").textContent =
        "Impossible de charger la meteo.";
    });
}

afficherMeteo("Lyon");
```

`encodeURIComponent` protege les accents et espaces dans l'URL. Petit detail utile.

## Ce que DanielCraft veut que tu sentes

Les promesses ne sont pas un exercice theorique. C'est le langage du "plus tard" sur le web. Fetch, fichiers, timers avances, plein d'APIs modernes parlent en promesses. Une fois l'idee du ticket pizza digeree, `async/await` (chapitre suivant) devient presque confortable.

## Erreur classique

Oublier le `catch`, puis ne rien voir quand ca rate. Ou mettre du code juste apres `fetch(...)` en croyant que les donnees sont deja la.

```js
// FAUX reflexe
fetch(url);
console.log("deja arrive ?"); // non, trop tot
```

Le code apres `fetch` s'execute tout de suite. Les donnees, elles, arrivent dans `then`.

## En vrai

Prends un `fetch` qui marche. Ajoute un `catch` qui ecrit un message dans la page. Coupe le wifi une seconde (ou mets une URL inventee) et regarde le `catch` se declencher. Tu dois sentir la difference entre "succes" et "echec".

## A toi

Ecris `chargerTodos(url)` avec `then` / `catch`. En succes, affiche le nombre de todos. En echec, affiche "Liste indisponible". Pas besoin que l'API soit parfaite : le branchement compte.
