# Chapitre 12 - Mini-projet : liste depuis une API

On assemble tout ce que tu as vu. Objectif : une page qui charge une liste (produits, citations, posts fictifs) depuis une URL JSON, affiche les titres ou noms, et gere le cas d'erreur proprement. Tu peux utiliser une API publique de demo, ou un fichier produits.json servi en local. L'important n'est pas la source exacte. C'est le parcours complet : evenement, fetch, verification, affichage, echec gracieux.

Chez DanielCraft, ce mini-projet est le passage oblige entre "j'ai lu les chapitres" et "je sais livrer une petite feature". Lea le fait systematiquement avec les juniors. Max l'a utilise pour sa liste de prestations. Sam l'adapte en exercice note. Si tu reussis les deux chemins (succes et erreur), tu as le socle. Sans le chemin erreur, tu as seulement une demo qui sourit par beau temps.

## Ce que ce n'est pas

Ce mini-projet, ce n'est pas un framework. Ce n'est pas non plus "tout decouper en micro-modules des la premiere heure". Ce n'est pas une excuse pour afficher une stack trace au visiteur. Et ce n'est surtout pas "ca marche chez moi en file://" : sers le dossier en local, comme en vrai.

Un bouton "Charger". Un clic. Un message "Chargement...". Puis soit une liste remplie, soit "Impossible de charger. Reessaie." Pas de page blanche. Pas de spinner infini. Pas de stack trace affichee au visiteur. C'est ca, une appli minimale mais pro. Lea visualise le parcours comme un entonnoir : clic, attente, succes ou message humain. Max aussi. Sam force les eleves a dessiner les deux sorties avant de coder.

:::retenir
Deux chemins obligatoires : liste OK, et erreur claire. Sans l'erreur, ce n'est pas un outil.
:::

## Parcours en etapes

1. HTML : un titre, un bouton "Charger", une zone #liste, une zone #message.
2. Au clic, tu appelles une fonction async qui fait fetch.
3. Tu verifies reponse.ok.
4. Tu parses le JSON avec await reponse.json().
5. Tu vides #liste, puis tu ajoutes un element par item.
6. Si ca rate, tu ecris un message humain dans #message.

## Squelette de depart

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

Adapte item.nom selon ta source (titre, texte, name). L'ossature reste identique. Lea change souvent la cle. Max aussi. L'important, c'est le schema : ok, json, vider, remplir, catch.

## Variante meteo (idee)

Meme structure : bouton, chargement, affichage temperature ou description, erreur claire. L'API change. Le schema mental reste. Max a fait sa widget meteo locale en une soiree avec ce squelette. Lea ajoute parfois un second bouton "Actualiser" qui rappelle la meme fonction. Sam propose une variante "citations" pour varier les plaisirs sans changer le muscle.

## Qualite minimale attendue

Pas de page blanche silencieuse. Pas d'erreur technique crachee a l'utilisateur (TypeError en gros sur la page). Un etat "Chargement..." visible pendant l'attente. Des noms de variables lisibles (liste, message, reponse, pas x et tmp). Un console.error dans le catch pour toi. Si tu decoupes en modules (api.js + afficher.js), c'est un bonus, pas une obligation pour valider le mini-projet.

Chez DanielCraft, on ajoute souvent un critere invisible : un ami comprend-il la page sans lire le code ? Bouton clair, message clair, liste claire. Si oui, tu as livre une feature, pas un exercice.

## Petite histoire

Sam a fait faire ce mini-projet a ses eleves. La moitie a oublie response.ok et affichait "0 elements" sur une 404. L'autre moitie a casse l'URL volontairement et a vu le message d'erreur. Devine qui a vraiment compris fetch ? Ceux qui ont teste l'echec.

Lea a montre sa page a un client non technicien. Le client a clique, vu "Chargement...", puis la liste. Il a dit "c'est clair". Elle n'a pas parle de async/await. Elle a livre une sensation. Chez DanielCraft, on valide ca.

## Erreur classique

Oublier de servir le dossier avec un serveur local : fetch sur file:// echoue souvent. Ne pas tester l'URL cassee : tu crois que tout va bien alors que tu n'as jamais vu le catch en action. Afficher les donnees sans vider la liste avant : les items s'accumulent a chaque clic. Autre piege : laisser le message "Chargement..." apres succes. Efface ou remplace.

:::attention
Tester seulement le beau chemin, c'est se mentir. Casse l'URL une fois. Regarde le catch. Puis reparer.
:::

## En vrai

Code cette page en local. Casse volontairement l'URL. Verifie que ton message d'erreur apparait. Remets la bonne URL. Verifie la liste. Si ces deux chemins marchent, le mini-projet est reussi. Montre-le a quelqu'un : peut-il comprendre ce qui se passe sans lire le code ?

## A toi

Implemente la page complete. Puis decoupe optionnellement en api.js et afficher.js si tu te sens pret (sinon, l'atelier 16 le fera). Ecris en une phrase ce que tu as appris en forcant une erreur reseau. Garde cette phrase : c'est ta preuve que tu as depasse la lecture passive.
