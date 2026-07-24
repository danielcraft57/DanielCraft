# Chapitre 1 - Salut, c'est quoi JavaScript ?

Tu as deja HTML (la structure) et CSS (le look).
JavaScript, c'est le mouvement. La reaction. La vie.

Sans JS, une page regarde.
Avec JS, elle repond.

## Image mentale

- HTML = le corps
- CSS = les vetements
- JS = le cerveau (et un peu les muscles)

Tu cliques un bouton ? JS peut compter.
Tu ecris ton prenom ? JS peut te dire "Salut, toi".
Tu rates un champ ? JS peut te prevenir.

## Ou ca tourne ?

Dans le navigateur. Directement.
Pas besoin d'installer un truc complique pour commencer.

## Ce que tu vas savoir faire

- Ecrire tes premiers scripts
- Garder des infos dans des variables
- Prendre des decisions (if)
- Repeter des actions (boucles)
- Creer des fonctions
- Modifier la page (le DOM)
- Reagir aux clics

## Important

On reste sur les bases.
Pas de framework. Pas de magie obscure.
Juste du JS clair, pour comprendre.

Allez. On branche le cerveau de la page.

## Erreur classique

Beaucoup de debutants confondent JavaScript et Java. Ce sont deux langages differents. JavaScript vit dans le navigateur pour rendre les pages vivantes. Java sert surtout a d'autres types de programmes.

Autre piege : croire que JS remplace HTML ou CSS. Non. Les trois travaillent ensemble.

## Exemple complet

Imagine une page avec un bouton. Sans JS, le bouton ne fait rien d'utile. Avec JS, il peut reagir :

```js
// On attend que la page soit chargee
const bouton = document.querySelector("#direBonjour");

// Quand on clique, on affiche un message
bouton.addEventListener("click", function () {
  alert("Salut ! La page t'a entendu.");
});
```

Tu n'as pas besoin de tout comprendre maintenant. L'idee : JS ecoute et repond.

## Mini defi

- Ouvre un site que tu aimes (YouTube, un jeu en ligne, etc.)
- Note 3 actions interactives (clic, scroll, formulaire...)
- Pour chacune, devine : HTML, CSS ou JS ?
- Verifie en desactivant JS dans le navigateur (option developpeur). Que se passe-t-il ?

## A retenir

- JavaScript = le cerveau interactif de la page
- Il tourne dans le navigateur, sans installation compliquee
- HTML structure, CSS habille, JS fait bouger et reagir
- Tu vas apprendre les bases, pas un framework


## En vrai, sur le terrain

Ouvre la console. Retape l'exemple a la main.
Change une valeur. Regarde ce qui bouge. C'est comme ca que ca rentre.

## Mini defi

Inventes un tout petit cas perso (ton prenom, ton score, ton jeu prefere).
Repars de l'exemple avec TES donnees. Si ca marche, c'est bon signe.
