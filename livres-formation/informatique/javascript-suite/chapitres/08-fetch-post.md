# Chapitre 8 - fetch POST : envoyer un peu de JSON

GET, c'est "donne-moi". POST, c'est "voici quelque chose". Formulaire de contact, creation d'une todo, envoi d'un avis produit, enregistrement d'une commande : souvent, tu POSTES un corps JSON au serveur. On reste leger dans ce chapitre. Pas besoin d'authentification complexe ni de tokens OAuth. Juste : methode, headers, body. Le trio qui fait voyager tes donnees du navigateur vers le serveur.

Chez DanielCraft, le flux contact est un classique : valider cote client (chapitre 2), montrer "Envoi en cours", POST le JSON, gerer succes et echec. Lea l'implemente sur presque chaque site vitrine. Max l'utilise pour son formulaire de devis. Sam simule l'envoi en exercice avant de brancher un vrai backend.

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

  return reponse.json();
}
```

Trois ingredients essentiels. method: "POST" pour dire que tu envoies des donnees. Content-Type: application/json pour prevenir que le corps est du JSON. body avec le texte produit par JSON.stringify. Sans le header, certains serveurs ne comprennent pas. Sans stringify, tu envoies "[object Object]" et ca finit tres mal.

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

Tu valides d'abord (chapitre 2). Tu montres un etat intermediaire. Tu postes. Tu geres succes et echec. C'est un flux realiste de page contact. Note le async sur le handler submit : indispensable pour utiliser await dedans.

## GET vs POST en une phrase

GET pour lire sans modifier (liste, meteo, detail produit). POST pour creer ou envoyer (message, nouvelle tache, commande). Il existe aussi PUT, PATCH, DELETE pour mettre a jour ou supprimer. Plus tard. Pour ce livre, GET plus POST suffisent largement pour des mini-apps utiles.

## Ce que le serveur renvoie

Parfois rien d'utile (code 204). Parfois un objet { "id": 42, "status": "recu" }. Parfois une erreur JSON { "erreur": "email invalide" }. Lis la doc de l'API quand tu en as une. En exercice, tu peux simuler avec un service de test ou un petit backend maison. L'important cote front : savoir envoyer proprement et lire la reponse.

## Petite histoire

Lea a oublie JSON.stringify une fois. Le serveur recevait "[object Object]". Le client jurait que "le formulaire est casse". En regardant l'onglet Network du navigateur, elle a vu le corps de la requete. Deux minutes pour corriger, des heures de debug evitees ensuite. Verifie toujours ce qui part vraiment sur le fil.

## Erreur classique

Ecrire body: contact au lieu de body: JSON.stringify(contact). Ou oublier async sur le handler submit et mettre await dedans. Ou poster sans preventDefault et perdre l'etat au rechargement. Ou croire que POST "marche" parce que le reseau n'a pas plante, sans lire reponse.ok. Meme regle qu'au chapitre 7.

## En vrai

Si tu as un endpoint de test (style JSONPlaceholder posts), envoie un petit objet { titre, corps }. Affiche l'id renvoye. Sinon, ecris la fonction et un console.log(JSON.stringify(contact)) pour verifier le corps avant meme d'appeler le reseau. Voir le JSON avant l'envoi, c'est une habitude pro.

## Zoom : ce que tu envoies vraiment

Ouvre Network avant de cliquer. Regarde Headers (Content-Type) et Payload (le body). Si tu vois [object Object], stringify a rate. Si tu vois du JSON clair, tu es bon. Lea fait ce geste a chaque nouveau formulaire. Max aussi, depuis qu'il a envoye un devis "casse" sans le savoir. Sam le montre en projeteur : silence, puis "ah". Chez DanielCraft, voir le fil avant de deboguer le serveur, c'est un reflexe.

## A toi

Ajoute un bouton "Envoyer l'avis" avec note et commentaire. Valide les champs. POST en JSON vers une URL de test ou simule avec console.log. Affiche "Avis enregistre" ou un message d'erreur. Garde le code court. La clarte bat la longueur. Bonus : desactive le bouton pendant l'envoi pour eviter le double POST.
