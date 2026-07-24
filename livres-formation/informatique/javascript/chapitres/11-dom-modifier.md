# Chapitre 11 - Le DOM : changer la page

Une fois l'element trouve, tu peux le modifier.

## Changer le texte

```js
const titre = document.querySelector("#titre");
titre.textContent = "Nouveau titre";
```

## Changer le HTML interne (avec prudence)

```js
titre.innerHTML = "Salut <strong>toi</strong>";
```

`textContent` = texte simple (plus sur pour debuter).
`innerHTML` = peut interpreter des balises.

## Classes CSS

```js
const carte = document.querySelector(".carte");
carte.classList.add("active");
carte.classList.remove("active");
carte.classList.toggle("active");
```

Super couple avec ton CSS.

## Style direct (ok pour tester)

```js
titre.style.color = "teal";
titre.style.fontSize = "28px";
```

Sur un vrai projet, prefere souvent les classes.

## Creer un element

```js
const p = document.createElement("p");
p.textContent = "Je viens d'apparaitre";
document.body.appendChild(p);
```

## A toi

Change le texte d'un paragraphe au chargement de la page.
Ajoute aussi une classe CSS `highlight` a un titre.


## En vrai, sur le terrain

Ouvre la console. Retape l'exemple a la main.
Change une valeur. Regarde ce qui bouge. C'est comme ca que ca rentre.

## Mini defi

Inventes un tout petit cas perso (ton prenom, ton score, ton jeu prefere).
Repars de l'exemple avec TES donnees. Si ca marche, c'est bon signe.
