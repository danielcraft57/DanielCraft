# Chapitre 4 - Les types simples

Les valeurs n'ont pas toutes la meme forme en JavaScript. Du texte n'est pas un nombre. Un vrai/faux n'est pas une phrase. Si tu melanges sans faire attention, JavaScript peut coller au lieu de calculer - et tu obtiens des resultats absurdes sans comprendre pourquoi. C'est le piege numero un des debutants. Chez DanielCraft, on apprend les **types** tot pour eviter le classique `"19" + 3` qui donne `"193"` au lieu de `22`. Une fois que tu vois ca une fois, tu ne l'oublies plus.

Lea le croise dans les formulaires web : tout ce qui sort d'un champ est du texte, meme si l'utilisateur tape des chiffres. Max l'a vu sur un "total devis" qui affichait "150030" au lieu de 1530 parce qu'il additionnait deux strings. Sam le fait tester en classe jusqu'au "ah !" collectif quand `"5" + 2` s'affiche a cote de `5 + 2`. Trois metiers, une meme lecon : regarde la forme de la valeur avant de calculer.

Une **string**, c'est du texte entre guillemets. Un **number**, c'est un nombre (entier ou decimal). Un **boolean**, c'est `true` ou `false`. `undefined` veut dire "pas encore defini". `null` veut dire "volontairement vide". Tu n'as pas a en faire des tartines maintenant : sache que ca existe, et regarde les guillemets avant de blamer les maths. `"5"` est une brique texte. `5` est une brique nombre. Les coller avec `+` ne donne pas le meme resultat.

```js
const phrase = "Bonjour";
const prix = 19.99;
const quantite = 3;
const total = prix * quantite;
const estConnecte = true;
```

## Ce que ce n'est pas

Ce n'est pas encore les objets et tableaux (chapitres 8 et 9). Ce n'est pas "les guillemets sont optionnels pour le texte" : sans guillemets, JavaScript cherche une variable qui s'appelle comme ton mot. Ce n'est pas croire que `==` arrangera tout : on preferera **`===`** pour comparer sans surprise de type. Et ce n'est pas paniquer sur **`typeof`** : c'est un outil pour verifier, pas un examen. Tu l'utilises pour debug, pas pour impressionner.

Ce n'est pas non plus penser que le navigateur "devine" ce que tu veux. Il suit des regles. `"5" + 2` colle du texte. `5 + 2` calcule. Point. Lea dit : "le navigateur n'est pas bete. Il fait ce que tu lui demandes. Parfois tu lui demandes n'importe quoi."

:::retenir
String = texte. Number = nombre. Boolean = vrai/faux. Guillemets = texte. Pas de guillemets sur un nombre = calcul.
:::

## Assembler du texte

```js
const prenom = "Maya";
console.log("Salut " + prenom);
console.log(`Salut ${prenom}`);
```

Les **backticks** (accent grave, touche a cote du 1) permettent d'inserer `${...}` directement dans la phrase. Plus moderne, tres pratique pour les messages longs. Une fois que tu y goutes, tu y reviens souvent. Lea prefere les backticks pour les mails clients. Max les utilise pour ses recus de devis. Sam montre les deux syntaxes puis laisse les eleves choisir leur preferee.

Quand tu tapes dans un formulaire, le navigateur te donne des briques texte. Toi, tu decides si tu calcules (convertir en number avec `Number(...)`) ou si tu affiches tel quel (string). `"19" + 3` donne `"193"` (collage). `19 + 3` donne `22` (calcul). Si la valeur vient d'un champ, convertis avant les maths.

## Petite histoire

Max additionnait un prix tape dans un champ (texte `"150"`) avec une quantite (nombre `3`). Resultat : `"1503"` affiche fierement sur sa page plomberie. Lea lui a montre `Number(prixChamp)` avant le calcul. Facture correcte : 450. Max a note "Number avant calcul" sur son carnet. Sam projette `"5" + 2` et `5 + 2` cote a cote : les eleves votent a main levee, puis verifient dans la console. Le type devient concret. Plus personne ne dit "le navigateur est bete". On dit "j'ai colle du texte".

## Erreur classique

```js
const total = "19" + 3; // "193" - collage
const totalOk = 19 + 3; // 22 - calcul
```

Ou convertir avec `Number("19")` si ca vient d'un champ. Autre piege : melanger simples et doubles guillemets sans coherence dans un fichier (pas grave, mais choisis un style). Et oublier que `typeof null` dit `"object"` - bizarre, historique, on le note sans en faire un drame. Ce n'est pas toi qui as mal code. C'est JS qui traine une vieille bizarrerie.

:::attention
Tout ce qui sort d'un champ de formulaire est du texte (string), meme si ca "ressemble" a un nombre. Convertis avant de calculer.
:::

## Exemple complet

```js
const client = "Maya";
const article = "Casque";
const prixUnitaire = 29.99;
const quantite = 2;
const tauxTva = 0.2;

const sousTotal = prixUnitaire * quantite;
const montantTva = sousTotal * tauxTva;
const totalTTC = sousTotal + montantTva;

const recu = `
Facture pour ${client}
- ${quantite} x ${article} : ${sousTotal.toFixed(2)} EUR
- TVA : ${montantTva.toFixed(2)} EUR
= Total : ${totalTTC.toFixed(2)} EUR
`;
console.log(recu);
```

`.toFixed(2)` arrondit a deux decimales pour l'affichage. Pratique pour les prix. Lea l'utilise sur tous ses devis demo. Max aussi sur sa page artisan. Tu verras ce genre de detail partout ou l'argent apparait dans le code.

## En vrai

Fais un mini ticket de caisse : prix, quantite, total, message avec backticks. Affiche `typeof` sur chaque variable dans la console. Observe les etiquettes : `"string"`, `"number"`, `"boolean"`. Tu verras les formes des briques. Puis teste `"5" + 2` et `5 + 2` cote a cote. Note la difference en une phrase. Ce geste vaut une demi-heure de cours. Max l'a note sur un post-it. Toi aussi, tu peux.

## A toi

Teste `"5" + 2` et `5 + 2`. Note la difference en une phrase claire. Cree une string, un number, un boolean. Assemble un message avec backticks et `${}`. Tu poses une brique solide pour les conditions du chapitre suivant. Chez DanielCraft, ce chapitre evite des heures de debug absurde sur des totaux qui collent au lieu de calculer.
