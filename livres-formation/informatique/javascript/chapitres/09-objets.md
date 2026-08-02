# Chapitre 9 - Les objets (des fiches)

Un **objet**, c'est une fiche avec des cases nommees. Prenom, score, actif. Titre, pages, lu. Prix, quantite, client. Au lieu d'une liste anonyme ou tout est "case 0, case 1", tu as des etiquettes claires. Tu lis `joueur.prenom`. Tu changes `joueur.score`. Tu comprends sans deviner. Chez DanielCraft, on dit : tableau pour lister, objet pour decrire une chose. Souvent, tu combines : un **tableau d'objets**. C'est le modele le plus frequent des qu'une page web devient un peu riche.

Lea, freelance web, modele des clients ainsi : nom, email, projet, statut. Max, artisan, represente un devis : client, montant, date, paye. Sam, enseignant, represente un eleve : prenom, moyenne, present. Trois metiers, une meme structure. Une chose = une fiche. Une liste de choses = un tableau de fiches. Une fois que tu sens ca, beaucoup de tutos deviennent lisibles d'un coup.

Pense a une fiche cartonnée : nom, prenom, classe. Chaque case a un nom. Tu ne cherches pas "la case numero 2" : tu cherches "prenom". Un tableau de fiches, c'est le classeur. Max a arrete ses "deux tableaux paralleles" (prenoms d'un cote, scores de l'autre) le jour ou il a vu la fiche unique. Sam montre les deux modeles et demande lequel survit a l'ajout d'une propriete `ville`. L'objet gagne.

```js
const joueur = {
  prenom: "Sam",
  score: 120,
  estActif: true
};
console.log(joueur.prenom);
joueur.score = joueur.score + 10;
```

Tu lis avec `joueur.prenom` ou `joueur["prenom"]`. Si la cle a un espace, les crochets deviennent necessaires. Le point marche pour les noms simples. Les crochets sauvent les cas bizarres. Tu n'as pas a tout memoriser. Tu as a savoir ou regarder quand ca rale.

:::retenir
Tableau = liste. Objet = fiche. Tableau d'objets = classeur. Trois outils, trois jobs.
:::

## Ce que ce n'est pas

Ce n'est pas un tableau (meme si les deux se croisent constamment). Ce n'est pas encore du JSON fichier sur disque (proche, mais on reste en JavaScript vivant). Ce n'est pas "tout mettre dans un seul objet geant du monde" avec cinquante proprietes melees. Des petites fiches claires. Une chose = un objet. Une liste de choses = un tableau. Et ce n'est pas confondre `joueur.score` avec une variable libre `score` flottant quelque part : la propriete vit dans l'objet.

Ce n'est pas non plus "plus complique qu'un tableau". C'est souvent plus clair. Lea dit aux stagiaires : si tu as besoin de nommer les cases, prends un objet. Si tu as besoin d'un ordre et d'une longueur, prends un tableau. Si tu as les deux besoins, combine.

## Tableau d'objets

```js
const equipe = [
  { prenom: "Sam", score: 120 },
  { prenom: "Lea", score: 95 }
];
console.log(equipe[0].prenom);
equipe[1].score = equipe[1].score + 5;
```

Quand utiliser quoi ? Tableau : plusieurs elements du meme genre. Objet : une chose avec plusieurs infos. Combo : liste de choses riches. C'est le modele le plus frequent sur le web debutant. Une liste de produits. Une liste de taches. Une liste de joueurs. Chaque element est une fiche. Tu parcours avec `for...of`. Tu lis `item.nom`. Tu modifies `item.fini`. Ca tient.

Si tu te retrouves avec `prenoms[]` et `scores[]` qui doivent rester aligns : passe a un tableau d'objets. Moins d'index qui derivent, moins de bugs silencieux.

## Petite histoire

Max stockait prenom et score dans deux tableaux paralleles et se trompait d'index des qu'il triait ou supprimait. Lea a dit : un objet par joueur. Fin du chaos. En une apres-midi, sa mini page de scores est devenue lisible. Sam montre les deux modeles et demande lequel survit a l'ajout d'une propriete `ville`. L'objet gagne a chaque fois. Les eleves refactorent. Ils ne veulent plus revenir en arriere.

Lea, elle, livre des listes de temoignages clients en tableau d'objets : texte, auteur, note. Max un devis multi-lignes : designation, quantite, prix. Sam un bulletin : matiere, note, coefficient. Trois scenes, une structure. Chez DanielCraft, on repete : nomme les cases, range les fiches.

## Erreur classique

```js
const user = { "nom complet": "Leo Martin" };
console.log(user["nom complet"]); // ok
// user.nom complet -> erreur de syntaxe
```

Oublier la virgule entre proprietes. Confondre `joueur.score` et `joueur[score]` sans guillemets (JavaScript cherche alors une variable `score`). Autre piege : vouloir un tableau la ou une fiche suffit, ou l'inverse. Ou creer un objet geant "app" avec tout dedans et ne plus oser le toucher. Prefere des petites fiches. Assemble-les dans un tableau si besoin.

:::attention
`joueur["score"]` avec guillemets lit la propriete. `joueur[score]` sans guillemets lit la variable `score` comme cle. Une paire de guillemets, un monde de bugs.
:::

## Exemple complet

```js
const inventaire = [
  { nom: "Zelda", heures: 40, fini: true },
  { nom: "Minecraft", heures: 120, fini: false },
  { nom: "Tetris", heures: 5, fini: true }
];
function afficherJeux(jeux) {
  for (const jeu of jeux) {
    const statut = jeu.fini ? "fini" : "en cours";
    console.log(jeu.nom + " (" + jeu.heures + "h) - " + statut);
  }
}
afficherJeux(inventaire);
```

Tu melanges objet, tableau, boucle et fonction. C'est le combo qui revient partout ensuite. Lis ligne par ligne. Sens le rythme. Puis ajoute un jeu avec `push` et relance. Chez DanielCraft, ce genre de mini inventaire se montre en une minute et convainc mieux qu'un discours.

## En vrai

Cree un objet `livre` : titre, pages, `lu` (boolean). Affiche une phrase complete avec backticks. Change `lu` a `true`. Reaffiche. Puis transforme-le en tableau de deux livres et parcours-les. Tu dois sentir la difference entre "une fiche" et "un classeur". Si tu bloques sur le point ou les crochets, loggue l'objet entier avec `console.log(livre)`.

## A toi

Objet `moi` avec prenom, age, ville, et `hobbies` (un tableau dedans). Affiche "J'aime : ..." en parcourant les hobbies. Puis un tableau de deux amis-objets avec les memes cles. Affiche chaque ami. Tu melanges objet et tableau : c'est le reflexe a garder pour la suite du livre, pour la todo enrichie, et pour les projets DanielCraft.
