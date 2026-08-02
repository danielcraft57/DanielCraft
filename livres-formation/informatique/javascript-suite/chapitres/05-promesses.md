# Chapitre 5 - Les promesses, sans jargon opaque

Quand tu appelles fetch, le resultat n'arrive pas tout de suite. Le reseau prend du temps. Le serveur peut etre loin, surcharge, ou simplement occupe a preparer la reponse. JavaScript dans le navigateur ne peut pas rester bloque a attendre comme un ascenseur en panne : la page doit rester utilisable. L'utilisateur doit pouvoir scroller, cliquer, taper pendant que ta requete voyage. C'est pour ca que le web moderne parle en "plus tard" plutot qu'en "attends ici jusqu'a la fin".

Une **promesse**, c'est un objet qui dit : "je te donnerai une valeur plus tard, ou une erreur." Tu branches ensuite ce qui se passe en cas de succes (**then**) ou d'echec (**catch**). C'est le langage du "plus tard" sur le web moderne. Tu n'as pas besoin de tout le jargon interne pour commencer. Tu as besoin de brancher correctement succes et echec.

Tu commandes une pizza. Le restaurant te donne un ticket. Ce ticket n'est pas la pizza. C'est la promesse de la pizza. Plus tard, soit tu recois la pizza (then), soit on t'annonce un probleme (catch). fetch te rend ce ticket tout de suite. Les donnees arrivent apres. Lea compare ca a un numero de suivi colis : tu as une reference immediate, le contenu arrive plus tard. Si tu ouvres le carton trop tot (code juste apres fetch sans then), tu trouves du vide.

Chez DanielCraft, on insiste : les promesses ne sont pas un exercice theorique de cours. Fetch, lecture de fichiers, timers avances, plein d'APIs modernes parlent en promesses. Une fois l'idee du ticket pizza digeree, async/await au chapitre suivant devient presque confortable. Tu ne changes pas de concept : tu changes de facon d'ecrire.

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

Chaque then peut renvoyer une nouvelle valeur. Le then suivant la recoit. C'est pour ca qu'on ecrit return reponse.json() : **json()** renvoie aussi une promesse, parce que lire le corps de la reponse prend un peu de temps. Si tu oublies le return, la chaine se casse silencieusement. Ce "silence" est souvent plus dangereux qu'une erreur rouge : tu crois que tout va bien, et data est undefined.

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

Si le reseau tombe, ou si json() explose sur un texte invalide, tu tombes dans catch. Un seul catch a la fin peut couvrir toute la chaine. Pratique. Max a ajoute un catch sur sa meteo : quand le wifi de chantier est faible, la page affiche "Meteo indisponible" au lieu de rester vide. Sam insiste : un ecran qui explique vaut mieux qu'une console rouge invisible pour l'eleve.

:::astuce
Ajoute toujours un catch (ou un try/catch plus tard) des le premier fetch "serieux". Tester le chemin rate une fois te sauve des demos humiliantes.
:::

## Pourquoi pas juste "attendre" ?

Parce que JS dans le navigateur est **evenementiel**. Pendant que la requete voyage, l'utilisateur peut encore interagir. Les promesses permettent de dire "continue ta vie, et rappelle-moi quand c'est pret." Tu n'as pas besoin de connaitre tous les etats internes (pending, fulfilled, rejected) pour commencer. Retiens : une promesse aboutit ou echoue ; tu branches then et catch. Le reste du vocabulaire viendra si tu en as besoin.

## Chainer sans se noyer

Evite les pyramides de then imbriques. Preferes une ligne claire. Une fonction qui retourne la chaine reste lisible et reutilisable.

```js
function afficherMeteo(ville) {
  return fetch("https://exemple.api/meteo?ville=" + encodeURIComponent(ville))
    .then(function (reponse) {
      return reponse.json();
    })
    .then(function (data) {
      document.querySelector("#meteo").textContent =
        "A " + data.ville + ", " + data.temp + " degres";
    })
    .catch(function () {
      document.querySelector("#meteo").textContent =
        "Impossible de charger la meteo.";
    });
}

afficherMeteo("Lyon");
```

**encodeURIComponent** protege les accents et espaces dans l'URL. Petit detail utile quand Lea passe "Saint-Etienne" ou "Aix-en-Provence" en parametre. Sans ca, certaines villes cassent silencieusement la requete.

:::attention
Le code juste apres fetch(...) s'execute tout de suite. Les donnees n'arrivent que dans then. Ecrire console.log juste apres fetch en croyant voir les donnees, c'est le piege numero un.
:::

## Petite histoire

Sam a ecrit un fetch sans catch. Un jour de cours, le fichier JSON etait mal nomme. La console est devenue rouge, les eleves ont panique, Sam aussi. En ajoutant un catch qui ecrit un message dans la page, le probleme est devenu visible et expliquable. "La liste est indisponible" vaut mieux qu'un ecran fige et une console effrayante. Lea raconte la meme chose aux juniors : un catch n'est pas du pessimisme, c'est du professionnalisme.

## Erreur classique

Oublier le catch, puis ne rien voir quand ca rate. Ou mettre du code juste apres fetch(...) en croyant que les donnees sont deja la.

```js
// FAUX reflexe
fetch(url);
console.log("deja arrive ?"); // non, trop tot
```

Le code apres fetch s'execute tout de suite. Les donnees arrivent dans then, plus tard. Autre piege : enchainer trop de then sans return intermediaire. La chaine devient une cascade de undefined. Tu cherches alors un bug "dans les donnees" alors que le probleme est dans le branchement.

## En vrai

Prends un fetch qui marche chez toi. Ajoute un catch qui ecrit un message dans la page. Coupe le wifi une seconde, ou mets une URL inventee, et regarde le catch se declencher. Tu dois sentir la difference entre succes et echec. C'est un reflexe pro. Si tu n'oses pas couper le wifi, une URL inventee suffit largement.

## A toi

Ecris chargerTodos(url) avec then et catch. En succes, affiche le nombre de todos dans un paragraphe. En echec, affiche "Liste indisponible". Pas besoin que l'API soit parfaite : le branchement compte. Au chapitre suivant, tu reecriras la meme fonction en async/await pour comparer.

:::retenir
Promesse = ticket "plus tard" : then pour le succes, catch pour l'echec, return dans la chaine - le code apres fetch n'a pas encore les donnees.
:::
