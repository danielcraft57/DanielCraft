# Chapitre 7 - Erreurs reseau et reponses foireuses

Le reseau n'est pas gentil. Wifi coupe. Serveur en maintenance. URL tapee de travers. JSON invalide renvoye par erreur. Et le piege le plus vicieux pour les debutants : une reponse HTTP 404 ou 500 que fetch considere quand meme comme "arrivee". Techniquement, la requete a abouti. Metier, c'est un echec. Ce chapitre te donne un reflexe solide : verifier, attraper, expliquer a l'utilisateur. Chez DanielCraft, on considere qu'une appli sans gestion d'erreur n'est pas livrable, meme pour un exercice.

Lea a deja vu un client dire "ca marche chez moi" alors que la moitie des utilisateurs avait un ecran blanc en 4G faible. Max a appris a afficher "Envoi impossible" au lieu de faire semblant. Sam montre a ses eleves que gerer l'echec fait partie du metier, pas un bonus optionnel.

## response.ok

Quand fetch se termine sans planter, tu as un objet Response. Regarde reponse.ok : c'est true pour les codes 200-299. Sinon, quelque chose cloche cote serveur ou URL.

```js
async function chargerProduits(url) {
  const reponse = await fetch(url);

  if (!reponse.ok) {
    throw new Error("HTTP " + reponse.status);
  }

  return reponse.json();
}
```

Tu transformes un "mauvais statut" en vraie erreur. Ensuite try/catch peut la recuperer. C'est le pattern que DanielCraft recommande presque toujours avec fetch. Sans ce if, tu risques d'afficher "Succes" avec des donnees vides ou du HTML d'erreur parse en JSON.

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

Tu vois les couches. Message pendant le chargement. Verification HTTP. Verification du format (tableau attendu). Affichage. Et si ca casse, un message humain a l'ecran plus le detail technique dans la console pour toi, le dev.

## Differents types d'echecs

Coupure reseau : fetch rejette, tu tombes dans catch. 404 ou 500 : fetch resout, mais ok est false. D'ou le if (!reponse.ok). JSON casse : reponse.json() rejette. Encore le catch. Bug dans ton affichage : aussi le catch, si tu as enveloppe assez large. Parfois trop large : apprends a lire console.error pour voir la vraie cause sans deviner.

## Ne mens pas a l'utilisateur

"Erreur 500 Internal Server Error" ne parle qu'aux devs. Preferes "Le service produits est indisponible. Reessaie dans cinq minutes." Tu peux garder le detail pour la console ou un mode debug. Pour un formulaire de contact, "Envoi impossible (reseau)" vaut mieux qu'un ecran blanc ou un spinner infini. Ton appli a deux publics : l'utilisateur (message simple) et toi (console avec details). L'utilisateur veut savoir quoi faire. Toi, tu veux savoir pourquoi. Ne confonds pas les deux. Max affiche "Service indisponible" au client et garde le stack trace pour lui.

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
  zone.textContent = data.temp + " degres - " + data.ciel;
}
```

Renvoyer null puis tester, c'est une autre facon de gerer. L'important : ne jamais faire comme si les donnees etaient la quand elles ne le sont pas.

## Erreur classique

Afficher "Succes !" alors que ok est false, parce que tu n'as regarde que "pas d'exception". Ou avaler l'erreur avec un catch vide. Un catch vide, c'est cacher la poussiere sous le tapis. Ou afficher le message technique brut a l'utilisateur final : effrayant et inutile.

## En vrai

Force une erreur volontairement. URL inventee. Puis une URL qui existe mais renvoie 404. Observe la difference entre rejet reseau et ok === false. Ecris les deux cas dans un petit commentaire pour toi. Ce sera ta fiche perso.

## A toi

Prends ton chargeur de liste (chapitre 4 ou 6). Ajoute response.ok, un vrai message utilisateur, et un console.error. Teste le chemin heureux et le chemin rate. Les deux doivent "marcher" : l'un affiche des donnees, l'autre explique le probleme sans planter la page.
