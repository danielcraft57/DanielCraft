# Chapitre 5 - Les conditions (if)

Parfois tu veux : si ca, alors ca. Sinon, autre chose. Les **conditions** sont le volant de ton script. Sans elles, le programme fait toujours la meme chose, bete et droit, quelle que soit la situation. Avec elles, tu decides : majeur ou mineur, mot de passe correct ou refuse, canicule ou froid. C'est la ou JavaScript commence a "penser" - pas comme un humain, mais en suivant des regles que tu ecris. Chez DanielCraft, on insiste sur **`===`** pour comparer, et on reserve **`=`** a l'affectation. Lea a perdu une heure sur un `=` dans un `if`. Max aussi. Sam le piege volontairement en cours - et tout le monde tombe une fois. Puis plus jamais.

Chaque `if` est une question. Chaque reponse ouvre ou ferme une porte. Si tu ecris mal la question (`=` au lieu de `===`), tu ne compares pas : tu forces une reponse. Lea appelle ca "soudoyer le portier sans le vouloir". Max a compris le jour ou son acces chantier s'ouvrait pour tout le monde. Sam fait jouer "portier" a voix haute avant le code : la logique se clarifie avant qu'une ligne soit ecrite.

```js
const age = 15;
if (age >= 18) {
  console.log("Majeur");
} else {
  console.log("Mineur");
}
```

Tu peux enchainer avec `else if`. Tu combines avec `&&` (et) et `||` (ou). Tu gardes les tests lisibles : une idee claire par branche. Si ta foret d'if devient illisible, decoupe - ou passe par une fonction. Le code lisible, c'est du code que tu peux relire dans six mois sans te demander ce que tu voulais dire.

:::retenir
Dans un `if`, `===` compare. `=` assigne. Une lettre, un monde de bugs. Dis la regle a voix haute avant de coder.
:::

## Ce que ce n'est pas

Ce n'est pas un `switch` obligatoire (utile plus tard pour beaucoup de cas identiques). Ce n'est pas `==` "parce que plus court" : **`===`** protege des surprises de types melanges. Ce n'est pas une foret de `if` imbriques sur vingt niveaux - personne ne peut lire ca, toi inclus dans deux jours. Et ce n'est pas "mettre un `=` dans le if pour aller plus vite". Ce geste assigne. Il ne compare pas. Resultat : toujours "vrai", toujours le mauvais chemin.

Lea rappelle : un `if` bien ecrit, c'est une phrase en francais traduite en code. Si tu ne peux pas la dire a voix haute, le code sera flou aussi.

## else if, comparaisons, et / ou

```js
const note = 14;
if (note >= 16) {
  console.log("Excellent");
} else if (note >= 10) {
  console.log("C'est valide");
} else {
  console.log("On revise");
}

const aUnTicket = true;
const estVip = false;
if (aUnTicket || estVip) {
  console.log("Tu peux entrer");
}
```

Comparaisons utiles : `===`, `!==`, `>`, `<`, `>=`, `<=`. Tu les verras partout. Apprends-les comme des outils de poche. Le `&&` veut dire "les deux doivent etre vrais". Le `||` veut dire "au moins un des deux suffit". Simple. Puissant.

:::attention
Dans un `if`, ecris toujours `===` (compare). Jamais un seul `=` (assigne). Une lettre, un monde de bugs.
:::

## Petite histoire

Lea validait un mot de passe avec `if (motDePasse = "secret123")`. Toujours "OK". Effroi. Puis comprehension : elle assignait au lieu de comparer. Max a fait un acces chantier : age + invitation. Il a mis un `=` par reflexe. Sam fait jouer "portier" a voix haute avant le code : "si age >= 18 ou invitation, alors entrer". Quand tu peux expliquer la decision a voix haute, le code suit. Les eleves qui passent par la voix haute font moins d'erreurs. Ce n'est pas magique. C'est de la traduction.

## Erreur classique

```js
if (motDePasse = "secret123") { /* assigne ! */ }
if (motDePasse === "secret123") { /* compare */ }
```

Oublier les accolades sur un `if` d'une ligne puis ajouter une deuxieme ligne "dedans" qui n'y est pas. Lis toujours le bloc. Autre piege : trop de conditions dans une seule ligne - decoupe pour rester lisible. Max a appris a ecrire ses conditions sur plusieurs lignes quand ca depasse deux tests. Lea decoupe en fonctions des qu'elle voit plus de trois `else if`. Avant d'ecrire le `if`, dis la regle a voix haute. Puis code. Moins d'erreurs.

## Exemple complet

```js
const age = 16;
const aInvitation = true;
const estBlackliste = false;

function peutEntrer(age, invitation, blackliste) {
  if (blackliste) return "Acces refuse : compte bloque";
  if (age < 13) return "Acces refuse : trop jeune";
  if (age >= 18 || invitation) return "Bienvenue !";
  return "Acces refuse : invitation requise";
}

console.log(peutEntrer(age, aInvitation, estBlackliste));
```

Lis chaque branche comme une phrase. Blackliste ? Refuse. Trop jeune ? Refuse. Majeur ou invite ? Bienvenue. Sinon ? Invitation requise. C'est lisible. C'est testable. C'est du DanielCraft : clair, pas malin pour rien.

## En vrai

Cree une variable `motDePasse` en dur. Si elle vaut `"secret123"`, affiche "OK", sinon "Refuse". Change la valeur. Observe. Puis casse volontairement avec un seul `=` dans le `if` et vois le piege : tout passe, toujours. Remets `===`. Le contraste enseigne mieux qu'un paragraphe de theorie. Lea fait ce test avec chaque stagiaire. Max s'en souvient encore.

## A toi

Variable `temperature` : >= 35 canicule, >= 25 chaud, >= 15 correct, sinon froid. Change plusieurs fois et observe chaque branche. Ecris en une phrase ta regle d'or sur `===`. Dis-la a voix haute avant le prochain `if` que tu ecriras. Chez DanielCraft, cette regle evite des soirees tristes devant l'ecran.
