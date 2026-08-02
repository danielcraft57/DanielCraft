# Chapitre 13 - Mini-projet : compteur type

Il est temps d'assembler. Tu vas construire un **compteur** type : un etat `number`, des actions claires (`incrementer`, `reset`), un affichage DOM garde. Chez DanielCraft, un mini-projet n'est pas un portfolio. C'est une preuve que les briques tiennent ensemble. Lea livre souvent ce genre de demo en formation. Max a fini le sien un dimanche. Sam chronometre : "deux heures max pour la V1".

L'idee : un score commence a 0. Un bouton ajoute 1. Un autre remet a 0. Le span affiche la valeur. Tout est annote. Pas de `any`. Pas de `as` gratuits. Si `tsc` proteste, tu lis et tu corriges.

:::retenir
Etat type + fonctions typees + DOM garde = un mini-projet TypeScript digne de ce nom.
:::

## Ce que ce n'est pas

Ce n'est pas une app complete. Ce n'est pas Redux. Ce n'est pas "il faut Vite". Un fichier HTML + un fichier `.ts` compile suffisent. Ce n'est pas non plus une todo entiere (tu la feras en atelier). Ici, le compteur force l'essentiel : nombre, void, null check.

## Squelette

```ts
let score: number = 0;

const scoreEl = document.querySelector<HTMLElement>("#score");
const btnPlus = document.querySelector<HTMLButtonElement>("#plus");
const btnReset = document.querySelector<HTMLButtonElement>("#reset");

function afficher(): void {
  if (!scoreEl) return;
  scoreEl.textContent = String(score);
}

function incrementer(): void {
  score = score + 1;
  afficher();
}

function reset(): void {
  score = 0;
  afficher();
}

btnPlus?.addEventListener("click", incrementer);
btnReset?.addEventListener("click", reset);
afficher();
```

HTML minimal : un span, deux boutons, le script compile. Lea separe volontairement `afficher` du reste : une fonction, un role. Max a d'abord tout mis dans le listener ; Sam l'a fait extraire.

:::astuce
Compile souvent. Une erreur apres dix lignes se trouve plus vite qu'apres deux cents.
:::

## Petite histoire

Lea, Max et Sam ont valide le compteur ensemble. Lea a refuse un `score: any`. Max a oublie le garde sur `scoreEl` ; `tsc` l'a rattrape en strict. Sam a demande un `reset` type `void` et un affichage initial. En vingt minutes, le trio avait une demo stable. DanielCraft garde ce rythme : petit, clair, testable. Pas de ceremony.

## Erreur classique

Laisser `score` en string parce que `textContent` est string. Melanger logique et DOM dans une seule fonction geante. Oublier d'appeler `afficher` apres mutation. Autre piege : compiler une fois, puis ne plus relancer `tsc` pendant une heure. Le filet ne sert que si tu le tendes.

:::attention
`textContent` est string. Ton etat peut rester `number` : convertis a l'affichage avec `String(score)`.
:::

## En vrai

Code le compteur. Ajoute un bouton `-1` qui ne descend pas sous 0. Type tout. Si tu bloques sur le DOM, relis le chapitre 12. Si tu bloques sur le type de `score`, relis les annotations.

## Construire sans te perdre

Decoupe le travail en tranches. D'abord l'etat type et `render` avec un score fixe. Ensuite un bouton +. Ensuite moins et reset. Ensuite les gardes null. Enfin une regle metier (plafond, message). Lea travaille exactement dans cet ordre avec les clients presses. Max voulait tout d'un coup et se perdait dans cinq erreurs. Sam impose des commits mentaux : "ca compile ?" entre chaque tranche.

Garde le CSS minimal. Une page laide qui clique bat une page belle qui ne compile pas. Tu pourras habiller apres. Le livre JavaScript bases t'a deja montre le compteur en JS : ici tu ajoutes le filet. Compare les deux versions si tu les as. Tu verras que la logique est la meme, le contrat est plus visible.

Quand tu bloques, relis le chapitre erreur compilateur. Quand le clic ne fait rien, verifie le JS charge et les ids. Quand le type gene, demande si c'est le type ou la valeur qui ment. Chez DanielCraft, ces trois portes resolvent presque tous les blocages debutants.

## Checklist avant de montrer

Coches mentales : score en number, render appele apres chaque changement, boutons trouves (ou message clair si absents), tsc sans erreur, page qui charge le bon js. Lea lit cette liste a voix haute avant un appel client. Max l'a scraptee sur un sticky. Sam met un point si un eleve montre sans avoir recompile.

Si tu choisis la variante todo, ta checklist change un peu : interface presente, tableau type, trim sur la saisie, liste DOM reconstruite proprement. Dans les deux cas, zero any, une extension personnelle, un sourire a la fin. Chez DanielCraft, le sourire compte : il dit que tu as traverse le rouge sans abandonner.

## A toi

Livre ta V1. Puis ecris en trois lignes : (1) ce que `tsc` a refuse, (2) comment tu as corrige, (3) ce que tu ajouterais demain (plafond, pas de score negatif deja fait...). Chez DanielCraft, cette note de fin transforme l'exercice en apprentissage.
