# Chapitre 7 - Erreurs reseau et reponses foireuses

Le reseau n'est pas gentil. Wifi coupe. Serveur en vacances. URL tapee de travers. JSON invalide. Et le piege le plus vicieux : une reponse HTTP 404 ou 500 que `fetch` considere quand meme comme "arrivee".

Ce chapitre te donne un reflexe solide : verifier, attraper, expliquer a l'utilisateur.

## response.ok

Quand `fetch` se termine sans planter, tu as un objet `Response`. Regarde `reponse.ok` : c'est `true` pour les codes 200-299. Sinon, quelque chose cloche cote serveur ou URL.

```js
async function chargerProduits(url) {
  const reponse = await fetch(url);

  if (!reponse.ok) {
    throw new Error("HTTP " + reponse.status);
  }

  return reponse.json();
}
```

Tu transformes un "mauvais statut" en vraie erreur. Ensuite `try/catch` peut la recuperer. C'est le pattern que DanielCraft recommande presque toujours avec fetch.

## try/catch async, version complete

```js
const statut = document.querySelector("#statut");
const liste = document.querySelector("#liste");

async function afficherProduits() {
  statut.textContent = "Chargement...";
  liste.innerHTML = "";

  try {
    const reponse = await fetch("https://exemple.api/produits");

    if (!reponse.ok) {
      throw new Error("Le serveur a repondu " + reponse.status);
    }

    const produits = await reponse.json();

    if (!Array.isArray(produits)) {
      throw new Error("Format inattendu");
    }

    statut.textContent = produits.length + " produits";
    for (const p of produits) {
      const li = document.createElement("li");
      li.textContent = p.nom;
      liste.appendChild(li);
    }
  } catch (erreur) {
    statut.textContent = "Impossible de charger la liste. Reessaie plus tard.";
    console.error(erreur);
  }
}

afficherProduits();
```

Tu vois les couches. Message pendant le chargement. Verification HTTP. Verification du format. Affichage. Et si ca casse, un message humain + le detail technique dans la console pour toi.

## Differents types d'echecs

Coupure reseau : `fetch` rejette, tu tombes dans `catch`.

404 / 500 : `fetch` resout, mais `ok` est false. D'ou le `if (!reponse.ok)`.

JSON casse : `reponse.json()` rejette. Encore le `catch`.

Bug dans ton affichage : aussi le `catch`, si tu as enveloppe assez large. Parfois trop large. Apprends a lire `console.error` pour voir la vraie cause.

## Ne mens pas a l'utilisateur

"Erreur 500 Internal Server Error" ne parle qu'aux devs. Preferes "Le service produits est indisponible. Reessaie dans cinq minutes." Tu peux garder le detail pour la console ou un mode debug.

Pour un formulaire de contact, "Envoi impossible (reseau)" vaut mieux qu'un ecran blanc.

## Cas meteo

```js
async function meteo(ville) {
  try {
    const reponse = await fetch(
      "https://exemple.api/meteo?ville=" + encodeURIComponent(ville)
    );
    if (!reponse.ok) {
      throw new Error("ville ou service introuvable");
    }
    const data = await reponse.json();
    return data;
  } catch (e) {
    return null;
  }
}

async function ui() {
  const data = await meteo("Toulouse");
  const zone = document.querySelector("#meteo");
  if (!data) {
    zone.textContent = "Pas de meteo pour cette ville.";
    return;
  }
  zone.textContent = data.temp + "°C - " + data.ciel;
}
```

Renvoyer `null` puis tester, c'est une autre facon de gerer. L'important : ne jamais faire comme si les donnees etaient la.

## Erreur classique

Afficher "Succes !" alors que `ok` est false, parce que tu n'as regarde que "pas d'exception". Ou avaler l'erreur avec un `catch` vide. Un `catch` vide, c'est cacher la poussiere sous le tapis.

## En vrai

Force une erreur. URL inventee. Puis une URL qui existe mais renvoie 404. Observe la difference entre rejet reseau et `ok === false`. Ecris les deux cas dans un petit commentaire pour toi.

## A toi

Prends ton chargeur de liste. Ajoute `response.ok`, un vrai message utilisateur, et un `console.error`. Teste le chemin heureux et le chemin rate. Les deux doivent "marcher" : l'un affiche des donnees, l'autre explique le probleme.
