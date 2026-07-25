# Chapitre 2 - Formulaires qui tiennent la route

Un formulaire, c'est une conversation entre ta page et la personne qui la visite. Elle ecrit. Ta page ecoute. Si quelque chose cloche, tu le dis clairement, sans agresser. Si tout va bien, tu continues vers l'envoi ou l'affichage d'un succes. Beaucoup de debutants font deux erreurs opposees : soit ils laissent le navigateur tout gerer sans rien expliquer, soit ils envoient le formulaire sans verifier et la page se recharge en silence, effacant tout ce que la personne avait tape. Ici, on prend le controle avec JavaScript. Ce n'est pas "plus complique pour le plaisir" : c'est plus clair pour l'humain qui remplit.

Chez DanielCraft, on considere qu'un formulaire reussi, c'est un formulaire ou l'utilisateur sait toujours ou il en est. Champ manquant ? Message clair. Email bizarre ? Explication simple. Envoi en cours ? Indication visible. Succes ? Confirmation nette. Lea utilise ce reflexe sur chaque site client. Max l'applique a son formulaire de devis. Sam le montre a ses eleves comme base de toute appli web serieuse. Tu vas retrouver ce meme standard jusqu'au chapitre POST.

Imagine un guichet. La personne remplit une fiche. Avant de la glisser dans la boite, un assistant verifie : nom present ? email avec un @ ? message assez long ? Si non, il renvoie la fiche avec un stylo sur la ligne a corriger. **preventDefault()**, c'est dire au navigateur : "Ne recharge pas la page, je gere la verification moi-meme." Sans ca, ta page clignote et le message disparait. C'est le geste numero un des formulaires en JS. Sans ce geste, le reste de ta logique n'a souvent meme pas le temps de parler.

## Lire les champs

Imagine un petit contact : nom, email, message. Rien d'exotique. Trois champs, une zone d'erreur, un bouton. C'est deja assez pour apprendre le pattern qui servira partout.

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

En JS, tu selectionnes le formulaire et tu ecoutes **submit**. Pas seulement le clic du bouton : Entree dans un champ compte aussi. C'est plus solide et plus accessible.

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

La methode **trim()** enleve les espaces au debut et a la fin. Un champ rempli uniquement d'espaces, ce n'est pas un vrai contenu. Ce detail evite des bugs betes en production. Max a perdu des heures avec des "noms" faits d'espaces avant de comprendre ce reflexe.

:::astuce
Lis toujours les champs avec .value.trim() des le debut. Tu te proteges des faux remplissages et tu simplifies toutes les verifications suivantes.
:::

## Valider sans etre mechant

La **validation**, ce n'est pas punir. C'est aider. Un message utile dit quoi corriger et ou. Un message inutile dit juste "erreur" et laisse la personne deviner. Preferes une phrase humaine a un code mysterieux. Preferes pointer le champ concerne plutot que d'afficher un mur de texte en haut de page sans lien avec l'action.

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

  zoneErreur.hidden = false;
  zoneErreur.textContent = "Merci " + nom + " ! Message pret a partir.";
});
```

Tu vois l'idee. On arrete des la premiere erreur. On remet le **focus** sur le champ concerne. On explique en francais simple. Chez DanielCraft, on prefere un message humain a un code d'erreur mysterieux copie depuis une doc API. Plus tard, tu pourras afficher plusieurs erreurs d'un coup (atelier 14) ; le principe reste le meme : aider, pas intimider.

## HTML5 aide, JS decide

Les attributs required, type="email", minlength aident. Mais ne compte pas seulement dessus. Les navigateurs ne montrent pas tous les memes bulles d'erreur. Et parfois tu as des regles metier : le message doit mentionner un produit, la note doit etre entre 1 et 5, le stock doit etre un nombre positif. JS reste le chef d'orchestre. Tu peux combiner : HTML pour le minimum, JS pour affiner. Lea valide cote client pour le confort, et rappelle toujours qu'un vrai serveur devra revalider : le front aide, le back protege.

## Petite histoire

Max avait mis un formulaire contact sur son site de plomberie. Les clients envoyaient des messages vides ou avec "@" oublie. Il recevait des mails inutilisables et perdait du temps a rappeler. En ajoutant trim(), preventDefault() et trois verifications simples, il a divise par deux les echanges inutiles. Lea, elle, valide cote client ET cote serveur : le front aide l'utilisateur, le back securise vraiment. Sam montre les deux niveaux a ses eleves pour qu'ils comprennent la difference. Trois facons de vivre le meme probleme, une meme lecon : ne jamais faire confiance au "champ rempli" sans regarder.

## Cas concret : todo avec garde-fou

Sur une todo, le piege classique c'est d'ajouter une tache vide. Le pattern est exactement le meme que pour le contact : lire, nettoyer, verifier, agir.

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

Meme logique partout : lire, nettoyer avec trim, verifier, agir. Ce pattern reviendra au chapitre POST quand tu enverras le formulaire au serveur. Une fois que tu le sens dans les doigts, le reste du livre devient beaucoup plus fluide.

## Erreur classique

Afficher l'erreur une seule fois, puis ne jamais la cacher. La personne corrige, renvoie, et l'ancien message reste affiche. Moche et confus. Efface l'erreur au debut de chaque tentative, ou des que la personne retape dans le champ concerne.

Autre piege : valider seulement au clic du bouton, jamais au submit. Si quelqu'un appuie sur Entree dans un champ, ton code ne part pas. Ecoute submit sur le formulaire entier. C'est plus solide et plus accessible.

## En vrai

Ouvre un formulaire de site connu (inscription, contact, avis produit). Essaie d'envoyer vide. Regarde le message. Est-il clair ? Pointe-t-il le champ ? Note ce que tu aimes et ce qui t'agace. Tu peux voler les bonnes idees pour ton propre code. Compare aussi ce que fait le navigateur seul (required) et ce que fait le JS en plus. Tu verras vite pourquoi JS reste utile meme avec HTML5.

## A toi

Fais un formulaire "avis produit" : note de 1 a 5, commentaire. Refuse une note hors plage. Refuse un commentaire de moins de 5 caracteres. Affiche un message de succes quand tout est bon. Pas besoin d'envoyer au serveur pour l'instant : concentre-toi sur la validation et les messages. Si ca marche, tu as la base solide pour le chapitre POST.

:::retenir
Formulaire solide = preventDefault + trim + messages humains + focus sur le champ - ecoute submit, pas seulement le clic.
:::
