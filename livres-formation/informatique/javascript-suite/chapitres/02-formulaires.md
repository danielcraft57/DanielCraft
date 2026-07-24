# Chapitre 2 - Formulaires qui tiennent la route

Un formulaire, c'est une conversation. La personne ecrit. Ta page ecoute. Si quelque chose cloche, tu le dis clairement. Si tout va bien, tu continues.

Beaucoup de debutants font deux erreurs. Soit ils laissent le navigateur tout gerer sans rien expliquer. Soit ils envoient le formulaire sans verifier, et la page se recharge en silence. Ici, on prend le controle.

## Lire les champs

Imagine un petit contact : nom, email, message.

```html
<form id="contact">
  <label for="nom">Nom</label>
  <input id="nom" name="nom" type="text">

  <label for="email">Email</label>
  <input id="email" name="email" type="email">

  <label for="message">Message</label>
  <textarea id="message" name="message"></textarea>

  <p id="erreur" hidden></p>
  <button type="submit">Envoyer</button>
</form>
```

En JS, tu selectionnes le formulaire et tu ecoutes `submit`.

```js
const form = document.querySelector("#contact");
const zoneErreur = document.querySelector("#erreur");

form.addEventListener("submit", function (event) {
  event.preventDefault();

  const nom = form.nom.value.trim();
  const email = form.email.value.trim();
  const message = form.message.value.trim();

  // on validera juste apres
});
```

`preventDefault()` dit au navigateur : "ne recharge pas, je gere". Sans ca, ta page clignote et ton message disparait. C'est le geste numero un des formulaires en JS.

## Valider sans etre mechant

La validation, ce n'est pas punir. C'est aider. Un message utile dit quoi corriger. Un message inutile dit juste "erreur".

Exemple simple :

```js
function afficherErreur(texte) {
  zoneErreur.hidden = false;
  zoneErreur.textContent = texte;
}

function cacherErreur() {
  zoneErreur.hidden = true;
  zoneErreur.textContent = "";
}

form.addEventListener("submit", function (event) {
  event.preventDefault();
  cacherErreur();

  const nom = form.nom.value.trim();
  const email = form.email.value.trim();
  const message = form.message.value.trim();

  if (nom === "") {
    afficherErreur("Dis-nous ton nom, meme un prenom suffit.");
    form.nom.focus();
    return;
  }

  if (email === "" || !email.includes("@")) {
    afficherErreur("L'email semble incomplet. Verifie le @.");
    form.email.focus();
    return;
  }

  if (message.length < 10) {
    afficherErreur("Ton message est un peu court. Ajoute quelques mots.");
    form.message.focus();
    return;
  }

  // Ici, tout est ok : on pourrait envoyer plus tard avec fetch
  zoneErreur.hidden = false;
  zoneErreur.textContent = "Merci " + nom + " ! Message pret a partir.";
});
```

Tu vois l'idee. On arrete des la premiere erreur. On remet le focus sur le champ. On explique en francais simple. Chez DanielCraft, on prefere un message humain a un code d'erreur mysterieux.

## HTML5 aide, JS decide

Les attributs `required`, `type="email"`, `minlength` aident. Mais ne compte pas seulement dessus. Les navigateur ne montrent pas tous les memes bulles. Et parfois tu as des regles metier ("le message doit parler d'un produit", "le stock doit etre un nombre positif"). JS reste le chef d'orchestre.

Tu peux combiner : laisser HTML pour le minimum, puis affiner en JS.

## Cas concret : todo avec garde-fou

Sur une todo, le piege classique c'est d'ajouter une tache vide.

```js
const champ = document.querySelector("#tache");
const liste = document.querySelector("#liste");
const formTodo = document.querySelector("#form-todo");

formTodo.addEventListener("submit", function (event) {
  event.preventDefault();
  const texte = champ.value.trim();

  if (texte === "") {
    afficherErreur("Ecris une tache avant d'ajouter.");
    return;
  }

  const li = document.createElement("li");
  li.textContent = texte;
  liste.appendChild(li);
  champ.value = "";
  champ.focus();
  cacherErreur();
});
```

Meme logique partout : lire, nettoyer (`trim`), verifier, agir.

## Erreur classique

Afficher l'erreur une seule fois, puis ne jamais la cacher. La personne corrige, renvoie, et l'ancien message reste. Moche. Efface l'erreur au debut de chaque tentative, ou des que la personne retape dans le champ.

Autre piege : valider seulement au clic du bouton, jamais au `submit`. Si quelqu'un appuie sur Entree, ton code ne part pas. Ecoute `submit` sur le formulaire. C'est plus solide.

## En vrai

Ouvre un formulaire de site (inscription, contact...). Essaie d'envoyer vide. Regarde le message. Est-il clair ? Est-ce qu'il pointe le champ ? Note ce que tu aimes. Tu peux voler les bonnes idees pour ton propre code.

## A toi

Fais un formulaire "avis produit" : note de 1 a 5, commentaire. Refuse une note hors plage. Refuse un commentaire de moins de 5 caracteres. Affiche un message de succes quand tout est bon. Pas besoin d'envoyer au serveur pour l'instant.
