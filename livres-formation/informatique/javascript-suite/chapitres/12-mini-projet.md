# Chapitre 12 - Mini-projet : liste depuis une API

On assemble. Objectif : une page qui charge une liste (produits, citations, ou posts fictifs) depuis une URL JSON, affiche les titres, et gere le cas d'erreur proprement.

Tu peux utiliser une API publique de demo, ou un fichier `produits.json` servi en local. L'important n'est pas la source exacte. C'est le parcours.

## Parcours

1. HTML : un titre, un bouton "Charger", une zone `#liste`, une zone `#message`.
2. Au clic, tu appelles une fonction `async` qui fait `fetch`.
3. Tu verifies `reponse.ok`.
4. Tu parses le JSON.
5. Tu vides `#liste`, puis tu ajoutes un element par item.
6. Si ca rate, tu ecris un message humain dans `#message` ("Impossible de charger. Reessaie.").

## Squelette

```js
async function charger() {
  const message = document.querySelector("#message");
  const liste = document.querySelector("#liste");
  message.textContent = "Chargement...";
  try {
    const reponse = await fetch("./produits.json");
    if (!reponse.ok) throw new Error("HTTP " + reponse.status);
    const data = await reponse.json();
    liste.innerHTML = "";
    for (const item of data) {
      const li = document.createElement("li");
      li.textContent = item.nom;
      liste.appendChild(li);
    }
    message.textContent = data.length + " elements";
  } catch (e) {
    message.textContent = "Impossible de charger. Reessaie.";
    console.error(e);
  }
}
```

## Variante meteo (idee)

Meme structure : bouton, chargement, affichage temperature ou description, erreur claire. L'API change. Le schema mental reste.

## Qualite minimale

Pas de page blanche silencieuse. Pas d'erreur technique crachee a l'utilisateur. Un etat "chargement" visible. Des noms de variables lisibles.

## A toi

Code cette page en local. Casse volontairement l'URL. Verifie que ton message d'erreur apparait. Remets l'URL. Verifie la liste. Si ces deux chemins marchent, le mini-projet est reussi.
