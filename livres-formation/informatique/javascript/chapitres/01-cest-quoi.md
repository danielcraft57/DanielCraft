# Chapitre 1 - Salut, c'est quoi JavaScript ?

Tu as deja HTML (la structure) et CSS (le look).
JavaScript, c'est le mouvement. La reaction. La vie.

Sans JS, une page regarde.
Avec JS, elle repond.

## Image mentale

Pense a une personne. Le HTML, c'est le corps : la forme, les pieces, ce qui existe. Le CSS, ce sont les vetements : couleurs, style, presentation. JavaScript, c'est le cerveau, et un peu les muscles. C'est lui qui decide, qui reagit, qui fait bouger.

Tu cliques un bouton ? JS peut compter.
Tu ecris ton prenom ? JS peut te dire "Salut, toi".
Tu rates un champ ? JS peut te prevenir.

## Ou ca tourne ?

Dans le navigateur. Directement.
Pas besoin d'installer un truc complique pour commencer.

## Ce que tu vas savoir faire

A la fin de ce parcours, tu sauras ecrire tes premiers scripts et ranger des infos dans des variables. Tu apprendras a prendre des decisions avec `if`, a repeter des actions avec des boucles, et a creer des fonctions reutilisables. Tu verras aussi comment modifier la page (le DOM) et comment reagir aux clics. Bref : rendre une page vivante, pas juste jolie.

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

Ouvre un site que tu aimes (YouTube, un jeu en ligne, peu importe). Note trois actions interactives : un clic, un scroll, un formulaire... Pour chacune, demande-toi : c'est plutot HTML, CSS ou JS ? Ensuite, si tu peux, desactive JavaScript dans les options developpeur du navigateur et regarde ce qui casse. Tu verras tout de suite a quoi sert le "cerveau" de la page.

## A retenir

JavaScript, c'est le cerveau interactif de la page. Il tourne dans le navigateur, sans installation compliquee pour commencer. HTML structure, CSS habille, JS fait bouger et reagir. Ici, on apprend les bases, pas un framework.


## En vrai, sur le terrain

Ouvre la console. Retape l'exemple a la main.
Change une valeur. Regarde ce qui bouge. C'est comme ca que ca rentre.

## Mini defi

Inventes un tout petit cas perso (ton prenom, ton score, ton jeu prefere).
Repars de l'exemple avec TES donnees. Si ca marche, c'est bon signe.
