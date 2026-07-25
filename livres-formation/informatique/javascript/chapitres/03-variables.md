# Chapitre 3 - Les variables (des boites a infos)

Une **variable**, c'est une boite avec une etiquette. Tu ranges une valeur dedans. Tu la reutilises plus tard sans recopier partout. Sans variables, tu recopies des nombres et des textes a chaque endroit, et tu te perds des qu'une valeur change. Avec variables, tu changes une fois, tout suit. C'est la base de toute programmation, pas seulement JavaScript. Le jour ou Lea a du changer le nom d'un client dans huit endroits differents parce qu'elle n'avait pas de variable, elle a compris pourquoi ce chapitre existe.

Chez DanielCraft, on enseigne **`const`** par defaut et **`let`** seulement si la valeur doit changer. Lea nomme ses variables comme elle nommerait des dossiers clients : `prenomClient`, `nombreDevis`, pas `x` ou `tmp`. Max a arrete les noms flous apres s'etre embrouille sur un compteur un dimanche soir devant sa famille. Sam refuse les noms incomprehensibles dans les copies : "si tu ne peux pas l'expliquer a voix haute, renomme". Trois metiers, une meme hygiene.

L'etiquette dit `score`, le contenu dit `0`. Tu peux remplacer le contenu d'une boite `let`. Une boite `const` refuse qu'on change le contenu (pour les valeurs simples : tu ne reassigne pas). Si tu ecris sur le mur sans boite (`score = 10` sans `let`/`const`), le chantier devient sale : d'autres scripts peuvent ecraser ta valeur sans que tu le voies. Max appelle ca "le graffiti du code".

```js
let age = 12;
const prenom = "Leo";
```

Avec **let**, tu pourras changer la valeur plus tard. Avec **const**, tu ne reassigne pas : protection volontaire contre les erreurs. Astuce debutant : `const` d'abord. Si tu dois vraiment changer (compteur, score, etat qui evolue), tu passes a `let`. Ce n'est pas une religion. C'est une hygiene qui evite des bugs silencieux quand le projet grandit.

:::retenir
Variable = boite etiquetee. `const` par defaut, `let` si ca bouge. Nomme clair, declare toujours.
:::

## Ce que ce n'est pas

Ce n'est pas **`var`** (ancien, comportement bizarre, on s'en fiche pour l'instant - si tu le vois dans un vieux tuto, ignore-le). Ce n'est pas une variable sans declaration (`score = 10` tout seul) qui pollue l'espace global et cree des conflits entre scripts. Ce n'est pas "tout en `let` parce que plus flexible" : trop de flexibilite, trop de bugs quand le projet grandit. Et ce n'est pas un objet magique : une variable tient une valeur, point. Tu la nommes. Tu la lis. Tu la changes (si `let`). C'est tout.

Ce n'est pas non plus confondre **`=`** avec "egal" en maths. En JS, `=` range une valeur dans la boite. On compare plus tard avec `===`. Lea a perdu une heure la-dessus avant de comprendre que le signe unique ne pose pas la meme question que deux signes egal. Tu peux eviter sa douleur en gardant cette distinction en tete des maintenant.

## Changer et nommer

```js
let score = 0;
score = 10;
score = score + 1; // 11

let nombreDeClics = 0;
const messageBienvenue = "Salut";
```

Oui aux noms clairs : `nombreDeClics`, `messageBienvenue`, `prixTotal`. Non a `x` et `a1` sauf calcul ultra local dans une boucle. Attention : `const ville = "Lyon"; ville = "Paris";` provoque une erreur. C'est voulu. Le navigateur te protege. Tu le remercieras quand tu auras cent lignes de code et que tu ne sauras plus ou tu as touche quoi.

:::astuce
Par defaut, ecris `const`. Passe a `let` seulement quand tu dois vraiment reassigner (compteur, score, etat qui bouge).
:::

## Petite histoire

Lea debugait un compteur qui "sautait" de facon aleatoire sur une demo client. Deux scripts utilisaient `score` sans `let` / `const` et se marchaient dessus dans l'espace global. Elle a declare proprement avec `let score = 0` dans un seul endroit. Calme retrouve. Le client n'a jamais su qu'il y avait eu un mini drame technique derriere son bouton qui comptait enfin correctement.

Max a voulu changer son `const prenom` apres une faute de frappe et a rage contre le navigateur pendant cinq minutes. Sam a dit : "il te protege, pas il te punie". Max a sourit le lendemain quand il a compris. Il garde maintenant un post-it : "const sauf compteur". Lea dit : "nomme comme si quelqu'un d'autre devait lire demain matin a 8h sans t'appeler". C'est la regle DanielCraft pour les variables : clarte d'abord, elegance ensuite.

## Erreur classique

Oublier `let` ou `const` et ecrire `score = 10` tout seul. Reassigner une `const` et croire que le navigateur est "bete". Reutiliser un nom sans le declarer dans un nouveau fichier. Croire que l'erreur "Assignment to constant variable" est une punition : c'est un garde-fou. Autre piege : noms trop courts (`a`, `tmp2`, `data`) qui ne disent rien quand tu reviens dans deux jours. Lea garde une regle : si tu hesites sur le nom, c'est que tu n'as pas compris ce que la variable represente.

:::attention
`=` range une valeur dans la variable. Ce n'est pas une comparaison. On compare plus tard avec `===`. Une lettre de difference, un monde de bugs.
:::

## Exemple complet

```js
const pseudo = "PixelFox";
let niveau = 1;
let xp = 0;

xp = xp + 50;
console.log(pseudo + " a " + xp + " xp");

if (xp >= 50) {
  niveau = niveau + 1;
  xp = xp - 50;
  console.log("Niveau up ! Tu es niveau " + niveau);
}

console.log("Etat final : niveau " + niveau + ", xp " + xp);
```

Lis le code ligne par ligne. `pseudo` ne change jamais : `const`. `niveau` et `xp` evoluent : `let`. La logique du `if` viendra au chapitre 5. Pour l'instant, sens le rythme : declarer, modifier, afficher. C'est le coeur de tout script JavaScript.

## En vrai

Cree `const prenom`, `let points = 0`, ajoute 5 aux points, affiche les deux avec `console.log`. Change seulement les `let`. Laisse les `const` tranquilles. Si la console rale quand tu touches une `const`, tu as compris la protection. Puis essaie de renommer une variable avec une faute de frappe dans un `console.log` : lis l'erreur "is not defined". C'est le navigateur qui te dit : "je ne connais pas cette boite". Lea adore ce moment. Toi aussi, tu peux le provoquer volontairement.

## A toi

Trois `const` (prenom, ville, animal) et deux `let` (compteurVisites, derniereNote). Affiche une phrase qui melange tout avec des `+`. Note ta regle perso : "const sauf si...". Chez DanielCraft, cette regle evite des soirees tristes devant l'ecran. Garde-la sur un post-it jusqu'au mini-projet.
