# Chapitre 8 - Les tableaux (des listes)

Un **tableau**, c'est une file d'elements ranges dans un ordre. Tu y mets des courses, des jeux, des taches, des scores, des noms de clients. Tu ajoutes, tu retires, tu parcours. L'**index** commence a 0. Oui, a 0. C'est bizarre au debut, puis ca devient un reflexe. Sans tableaux, tu te retrouves avec dix variables `fruit1`, `fruit2`, `fruit3` et tu pleures des qu'il faut en ajouter un quatrieme. Avec un tableau, tu as une seule boite qui grandit.

Chez DanielCraft, le tableau est la structure "liste" par defaut avant les objets. Lea, freelance web, les utilise pour menus de navigation et listes de tags sur les pages clients. Max, artisan plombier, range ses fournitures du mois dans un tableau pour les afficher proprement. Sam, enseignant, fait compter a partir de zero jusqu'a ce que ca rentre dans la tete des eleves. Trois metiers, une meme idee : une liste ordonnee, un index qui part de zero, une longueur qui dit combien il y a d'elements.

Pense a des casiers numerotes 0, 1, 2. Le casier 0 tient le premier element. Si tu demandes le casier 3 alors qu'il n'y en a que trois (0, 1, 2), tu obtiens `undefined`. Quand tu fais `push`, tu ouvres un nouveau casier a la fin. Quand tu fais `pop`, tu retires ce qui est dans le dernier. La longueur change. L'ordre compte.

```js
const courses = ["pain", "lait", "oeufs"];
console.log(courses[0]); // pain
courses[1] = "lait d'avoine";
console.log(courses.length); // 3
```

`push` ajoute a la fin. `pop` retire le dernier. `includes` verifie la presence. Tu parcours avec `for` ou `for...of`. Une liste qui vit : c'est ca, le tableau. Tu n'as pas besoin de tout savoir d'un coup. Tu as besoin de sentir que la liste grandit et retrecit sous tes doigts.

:::retenir
Tableau = liste ordonnee. Index 0 pour le premier. Dernier index = `length - 1`. Jamais `length` comme index.
:::

## Ce que ce n'est pas

Ce n'est pas un objet (fiches nommees : chapitre suivant). Ce n'est pas "l'index 1 est le premier" - le premier est 0. Ce n'est pas `length` egal au dernier index : le dernier index est `length - 1`. Si tu ecris `courses[courses.length]`, tu obtiens `undefined`. Et ce n'est pas encore les methodes avancees `map` / `filter`. On reste sur le solide : creer, lire, ajouter, retirer, parcourir.

Ce n'est pas non plus "tout mettre dans un tableau geant sans reflechir". Une liste de fruits, oui. Melanger scores, images et mots de passe dans le meme tableau sans structure, non. Lea dit : une liste, un genre d'elements. Sam ajoute : si tu ne peux pas expliquer ce que contient la liste en une phrase, elle est trop floue.

## Ajouter, retirer, parcourir

```js
courses.push("beurre");
const dernier = courses.pop();

for (let i = 0; i < courses.length; i = i + 1) {
  console.log(courses[i]);
}
for (const item of courses) {
  console.log(item);
}
if (courses.includes("pain")) {
  console.log("On a du pain");
}
```

Le `for` classique te donne l'index : utile si tu as besoin du numero. Le `for...of` te donne directement l'element : plus lisible quand tu n'as pas besoin de l'index. `includes` repond vrai ou faux. Trois outils, trois situations. Lea prefere `for...of` pour afficher. Max utilise souvent l'index quand il numerote une facture. Sam montre les deux et laisse choisir.

:::astuce
Pour le premier element : `[0]`. Pour le dernier : `[tableau.length - 1]`. Jamais `[tableau.length]` - ca donne `undefined`.
:::

## Petite histoire

Max cherchait le "dernier" avec `courses[courses.length]` et voyait `undefined` sur sa page de fournitures. Il a rage cinq minutes. Lea a dit `length - 1`. Il a note sur un post-it. Depuis, il ne se trompe plus. Sam fait une course en classe : "qui donne l'index de banane dans `['pomme', 'banane', 'kiwi']` ?" La moitie leve la main pour "2". Puis on verifie. Puis on refait. Compter a partir de zero devient un reflexe, pas une blague de developpeur.

Lea, elle, utilise les tableaux pour generer des menus : dix liens, une boucle, pas dix lignes copiees. Max numerote ses etapes de devis. Sam fait afficher une liste de prenoms avec "Salut, ..." en boucle. Quand la liste grandit d'un `push` et que l'affichage suit, le tableau devient concret.

## Erreur classique

Confondre index et longueur. Modifier une liste en bouclant d'une facon qui saute des elements (plus tard, quand tu filtreras en place). Croire que `push` renvoie le tableau (il renvoie la nouvelle longueur). Pour debuter, affiche le tableau apres chaque action avec `console.log`. Tu verras evoluer la liste. Ca rassure. Autre piege : commencer a compter a 1 "parce que c'est plus naturel" et tout decaler d'une case. Lea dit : accepte le zero. C'est le dialecte du langage. `["a", "b"]` : index de `"a"` = 0, `length` = 2, dernier index = 1. Trois nombres, trois pieges classiques.

## Exemple complet

```js
const courses = ["pain", "lait", "oeufs"];
courses.push("fromage");
for (let i = 0; i < courses.length; i = i + 1) {
  console.log(i + 1 + ". " + courses[i]);
}
if (courses.includes("lait")) {
  console.log("lait est dans la liste");
}
const retire = courses.pop();
console.log("Retire : " + retire);
console.log("Reste :", courses);
```

Lis ligne par ligne. Tu ajoutes, tu numerotes a l'affichage (1, 2, 3... pour les humains), tu verifies une presence, tu retires. C'est le rythme d'une todo, d'un panier, d'un inventaire. Chez DanielCraft, on aime ce genre d'exemple parce qu'il se montre en trente secondes.

## En vrai

Cree une liste de quatre jeux. Fais un `push` d'un cinquieme. Affiche tous avec une boucle. Observe `length` avant et apres. Puis retire le dernier avec `pop` et reaffiche. Tu dois sentir la liste respirer. Si `undefined` apparait, regarde ton index. Corrige. Relance. Cinq minutes actives valent mieux qu'une page de theorie.

## A toi

Cinq films. Affiche le premier et le dernier. Fais un `push`, un `pop`, un parcours `for...of` avec `.toUpperCase()` sur chaque titre. Observe la liste evoluer dans la console. Note en une phrase ta regle anti-`undefined` sur le dernier element. Tu prepares la todo de l'atelier : sans tableau solide, la liste de taches ne tiendra pas.
