# Chapitre 1 - Salut, c'est quoi JavaScript ?

Tu as deja **HTML** (la structure) et **CSS** (le look). JavaScript, c'est le mouvement. La reaction. La vie. Sans JS, une page regarde. Avec JS, elle repond. Tu cliques, elle compte. Tu ecris ton prenom, elle te salue. Tu rates un champ, elle te previent avant l'envoi. Ce n'est pas magie. Ce sont des instructions que le navigateur execute, une apres l'autre, quand quelque chose se passe - ou des le chargement.

Chez DanielCraft, on presente JS comme le cerveau de la page - pas comme un monstre a frameworks, pas comme un club reserve aux "vrais" developpeurs. Le HTML pose le corps : ce qui existe. Le CSS habille : couleurs, style, presentation. **JavaScript** decide, reagit, fait bouger. Lea branche des boutons sur des pages clients. Max a ajoute un compteur de devis sur sa page artisan. Sam montre a ses eleves qu'une page "morte" et une page "vivante", c'est souvent dix lignes de JS clair. Trois metiers, meme logique : petit script, gros effet ressenti.

En 2026, quand quelqu'un dit "j'ai du JavaScript sur mon site", il parle le plus souvent d'interactions simples : menu qui s'ouvre, formulaire qui verifie, compteur qui monte. Derriere, il y a parfois des outils plus gros (React, Vue...). Pour toi, le geste reste le meme : ecrire des instructions claires, tester, corriger. Tu restes le pilote. Le navigateur accelere.

:::retenir
JavaScript = le cerveau de la page. Tu restes le pilote. Lui, il reagit quand tu lui donnes des instructions claires.
:::

## Ce que ce n'est pas

Ce n'est pas **Java**. Deux langages differents, malgre le nom proche. Ce n'est pas un remplacement de HTML ou CSS : les trois travaillent ensemble, comme trois metiers sur un chantier. Ce n'est pas un framework (React et cie) des le jour un. Ce n'est pas "installer un truc complique" pour commencer : ca tourne dans le navigateur, souvent avec un simple fichier `.js`. Et ce n'est pas magie : si tu ecris flou, tu obtiens flou.

Ce n'est pas non plus "tout automatiser d'un coup". Commence par un clic qui affiche un message. Monte ensuite vers variables, conditions, DOM. Tu seras pret. Lea rappelle souvent : une premiere victoire vaut mieux qu'un plan de trente pages jamais code.

## Ce que tu vas savoir faire

A la fin de ce livre, tu sauras ecrire tes premiers scripts, ranger des infos dans des **variables**, decider avec `if`, repeter avec des boucles, creer des fonctions, manipuler tableaux et objets, trouver et modifier des elements (**DOM**), reagir aux clics, faire un mini compteur, une todo, un peu de localStorage, et lire les erreurs dans la console. Niveau debutant solide. Pas de framework. Juste du JS clair pour comprendre ce que tu touches quand tu ouvres un site.

Niveau debutant solide. Pas besoin d'avoir deja code en Python ou autre. Besoin de curiosite et de tester : JS aide ; il ne remplace pas ta verification ligne par ligne.

## Comment lire ce livre

Lis dans l'ordre au debut. Les premiers chapitres posent le sol : ou ecrire, variables, types. Les chapitres du milieu construisent la logique. Les ateliers font faire. Le quiz verifie. Tu peux revenir ensuite a un chapitre precis (DOM, evenements, erreurs) comme a une fiche. A chaque fin, il y a un "A toi". Fais-le. Cinq minutes actives valent mieux qu'une lecture passive de quarante pages.

Chez DanielCraft, on forme des gens qui livrent petit, souvent, proprement - pas des collectionneurs de tutos oublies dans dix onglets. Tu modifies. Tu sauvegardes. Tu rafraichis. Tu regardes la console. Ce rythme bat une soiree de videos sans jamais ouvrir un fichier.

## Petite histoire

Lea devait rendre un bouton "demander un devis" utile pour un client fleuriste. Sans JS, il menait nulle part - clic, silence. Avec JS, il affiche un message de confirmation, compte les clics de test, et prepare le terrain pour un vrai formulaire plus tard. Quarante minutes, demo nette. Le client comprend. Lea assume le code, pas l'IA.

Max, lui, voulait juste "que ca bouge un peu" sur sa page plomberie. Il a commence par un `alert` basique. Puis un compteur. Puis sa famille a clique en souriant pendant le repas du dimanche. Sam desactive JS dans le navigateur en cours : les eleves voient un site perdre ses superpouvoirs en direct. L'idee rentre sans jargon. Personne ne dit "c'est complique". Ils disent "ah, c'est ca le cerveau".

## Erreur classique

Confondre JavaScript et Java. Croire que JS remplace HTML/CSS. Vouloir un framework avant de savoir selectionner un bouton avec `querySelector`. Ou penser "ca ne marche pas" sans ouvrir la **console** (F12). La console est ton ami. On y revient souvent dans ce livre. Autre piege : tout vouloir le premier soir. Un bouton qui repond suffit comme premiere victoire. DanielCraft insiste : petit, clair, testable.

:::attention
Sans console ouverte, tu codes a l'aveugle. F12 des le premier test : tu verras ce que le navigateur te dit vraiment.
:::

## En vrai

Ouvre un site que tu visites souvent. Note trois interactions : un menu, un formulaire, un bouton qui change quelque chose. Si tu peux, desactive JavaScript dans les options developpeur de ton navigateur et regarde ce qui casse. Tu verras le "cerveau" disparaitre. Puis reactive. Le contraste vaut une heure de theorie. Ensuite, ouvre la console sur n'importe quelle page et tape `console.log("test")`. Si tu vois "test", tu as deja parle a JavaScript. Note en une phrase ce qui "meurt" sans JS : tu poseras mieux tes priorites pour la suite du livre.

## A toi

Ecris en trois phrases : (1) une interaction que tu voudrais sur ta page, (2) ce que tu acceptes d'apprendre d'abord (variables, clics...), (3) ce que tu ne feras pas encore (API, framework). Garde ce papier pour le mini-projet du chapitre 13. Chez DanielCraft, ce petit brief vaut plus qu'une heure de tutorials flous : tu sais ou tu vas, et ce que tu refuses pour l'instant.

## Exemple pour sentir

```js
const bouton = document.querySelector("#direBonjour");
bouton.addEventListener("click", function () {
  alert("Salut ! La page t'a entendu.");
});
```

Tu n'as pas besoin de tout comprendre maintenant. L'idee : JS ecoute et repond. Dans ce livre, on demonte ca piece par piece, avec Lea, Max et Sam comme compagnons de route - et DanielCraft comme fil : petit, clair, testable. Chaque chapitre ajoute une brique. A la fin, la page obeit.
