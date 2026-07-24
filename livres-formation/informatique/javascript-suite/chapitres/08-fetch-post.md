# Chapitre 8 - fetch POST : envoyer un peu de JSON

GET, c'est "donne-moi". POST, c'est "voici quelque chose". Formulaire de contact, creation d'une todo, envoi d'un avis produit : souvent, tu POSTES un corps JSON.

On reste leger. Pas besoin d'auth compliquee. Juste : methode, headers, body.

## Anatomie d'un POST

```js
async function envoyerContact(contact) {
  const reponse = await fetch("https://exemple.api/contact", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(contact)
  });

  if (!reponse.ok) {
    throw new Error("Envoi refuse (" + reponse.status + ")");
  }

  return reponse.json(); // parfois le serveur renvoie { ok: true, id: 12 }
}
```

Trois ingredients. `method: "POST"` pour dire que tu envoies. `Content-Type: application/json` pour prevenir que le corps est du JSON. `body` avec le texte produit par `JSON.stringify`.

Sans le header, certains serveurs ne comprennent pas. Sans `stringify`, tu envoies "[object Object]" et ca finit mal.

## Brancher sur un formulaire

```js
const form = document.querySelector("#contact");
const statut = document.querySelector("#statut");

form.addEventListener("submit", async function (event) {
  event.preventDefault();

  const contact = {
    nom: form.nom.value.trim(),
    email: form.email.value.trim(),
    message: form.message.value.trim()
  };

  if (contact.nom === "" || contact.message.length < 10) {
    statut.textContent = "Complete le formulaire avant d'envoyer.";
    return;
  }

  statut.textContent = "Envoi en cours...";

  try {
    const resultat = await envoyerContact(contact);
    statut.textContent = "Message envoye. Merci !";
    form.reset();
    console.log(resultat);
  } catch (e) {
    statut.textContent = "Envoi impossible. Verifie ta connexion.";
    console.error(e);
  }
});
```

Tu valides d'abord (chapitre 2). Tu montres un etat intermediaire. Tu postes. Tu geres succes et echec. C'est un flux realiste de page contact chez DanielCraft et partout ailleurs.

## GET vs POST en une phrase

GET pour lire sans modifier (liste, meteo, detail produit). POST pour creer ou envoyer (message, nouvelle tache, commande). Il existe aussi PUT, PATCH, DELETE. Plus tard. Pour ce livre, GET + POST suffisent largement.

## Ce que le serveur renvoie

Parfois rien d'utile (204). Parfois un objet `{ "id": 42, "status": "recu" }`. Parfois une erreur JSON `{ "erreur": "email invalide" }`. Lis la doc de l'API quand tu en as une. En exercice, tu peux simuler avec un service de test ou un petit backend. L'important cote front : savoir envoyer proprement.

## Erreur classique

Ecrire `body: contact` au lieu de `body: JSON.stringify(contact)`. Ou oublier `async` sur le handler `submit` et mettre `await` dedans. Ou poster sans `preventDefault` et perdre l'etat au rechargement.

Autre piege : croire que POST "marche" parce que le reseau n'a pas plante, sans lire `reponse.ok`. Meme regle qu'au chapitre 7.

## En vrai

Si tu as un endpoint de test (ou JSONPlaceholder style posts), envoie un petit objet `{ titre, corps }`. Affiche l'id renvoye. Sinon, ecris la fonction et un `console.log(JSON.stringify(contact))` pour verifier le corps avant meme d'appeler le reseau.

## A toi

Ajoute un bouton "Envoyer l'avis" avec note + commentaire. Valide. POST en JSON. Affiche "Avis enregistre" ou un message d'erreur. Garde le code court. La clarte bat la longueur.
