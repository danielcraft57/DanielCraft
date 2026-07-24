# Chapitre 17 - Atelier : une todo liste mini

On fait une liste de taches.
Ajouter. Afficher. (Supprimer en bonus.)

## HTML

```html
<h1>Mes taches</h1>
<input id="champ" type="text" placeholder="Nouvelle tache">
<button id="ajouter">Ajouter</button>
<ul id="liste"></ul>
<script src="script.js"></script>
```

## JS

```js
const champ = document.querySelector("#champ");
const bouton = document.querySelector("#ajouter");
const liste = document.querySelector("#liste");

bouton.addEventListener("click", function () {
  const texte = champ.value.trim();
  if (texte === "") {
    return;
  }

  const li = document.createElement("li");
  li.textContent = texte;
  liste.appendChild(li);
  champ.value = "";
  champ.focus();
});
```

## Pourquoi `trim()` ?

Pour enlever les espaces avant/apres.
Sinon tu peux ajouter une tache "vide" pleine d'espaces. Moche.

## Bonus 1 : Enter aussi

```js
champ.addEventListener("keydown", function (event) {
  if (event.key === "Enter") {
    bouton.click();
  }
});
```

## Bonus 2 : supprimer une tache

```js
li.addEventListener("click", function () {
  li.remove();
});
```

Dis-toi que cliquer = "c'est fait, je retire".

## Criteres

- Ajout marche
- Champ se vide apres ajout
- Pas d'ajout vide
- Code lisible

## Ce que tu pratiques ici

- DOM
- Evenements
- Conditions
- Creation d'elements

C'est pile le coeur du JS front debutant.
