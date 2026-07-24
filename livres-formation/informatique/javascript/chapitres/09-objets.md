# Chapitre 9 - Les objets (des fiches)

Un objet, c'est une fiche avec des cases nommees.

## Exemple

```js
const joueur = {
  prenom: "Sam",
  score: 120,
  estActif: true
};

console.log(joueur.prenom);
joueur.score = joueur.score + 10;
```

## Objet dans un tableau

```js
const equipe = [
  { prenom: "Sam", score: 120 },
  { prenom: "Lea", score: 95 }
];

console.log(equipe[0].prenom);
```

## Quand utiliser quoi ?

Un tableau, c'est une liste d'elements du meme genre : plusieurs jeux, plusieurs prenoms, plusieurs prix. Un objet, c'est une seule chose avec plusieurs infos : un joueur, un livre, un produit. Souvent, tu combines les deux : un tableau d'objets.

## A toi

Cree un objet `livre` avec un titre, un nombre de pages, et une propriete `lu` en true ou false. Affiche ensuite une phrase du genre "Le livre X a Y pages". Tu dois voir le titre et le nombre sortir ensemble.

## Erreur classique

Tu melanges point et crochets. Les deux marchent, mais sois coherent.

Ca marche :

```js
joueur.prenom
joueur["prenom"]
```

Piege : si la cle a un espace ou un tiret, utilise les crochets :

```js
const user = { "nom complet": "Leo Martin" };
console.log(user["nom complet"]); // ok
console.log(user.nom complet);    // erreur
```

## Exemple complet

```js
// Inventaire de jeux
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

function totalHeures(jeux) {
  let total = 0;
  for (const jeu of jeux) {
    total = total + jeu.heures;
  }
  return total;
}

afficherJeux(inventaire);
console.log("Total heures : " + totalHeures(inventaire));
```

Objets dans un tableau : combo tres courant en JS.

## Mini defi

Cree un objet `moi` avec prenom, age et ville. Ajoute aussi une propriete `hobbies` (un tableau de textes). Affiche "J'aime : ..." en joignant les hobbies. Puis cree un tableau de deux amis (des objets) et affiche leurs prenoms. Tu melanges objet et tableau : c'est exactement le reflexe a prendre.

## A retenir

Un objet, c'est une fiche avec des proprietes nommees. Tu lis avec `objet.cle` ou `objet["cle"]`. Un tableau d'objets, c'est une liste de fiches. En resume : tableau pour lister, objet pour decrire une chose.


## En vrai, sur le terrain

Ouvre la console. Retape l'exemple a la main.
Change une valeur. Regarde ce qui bouge. C'est comme ca que ca rentre.

## Mini defi

Inventes un tout petit cas perso (ton prenom, ton score, ton jeu prefere).
Repars de l'exemple avec TES donnees. Si ca marche, c'est bon signe.
