# Chapitre 18 - Garder des infos (localStorage)

Jusqu'ici, tout vivait en memoire vive. Tu fermes l'onglet ou tu appuies sur F5 : le compteur repart a zero, la todo s'evapore. Des fois, tu veux que ca reste. **`localStorage`** range des textes dans le navigateur, sur cet appareil, dans ce navigateur precis. Tu recharges la page : les donnees sont encore la. Petit pouvoir, gros effet "waouh" quand tu le montres a quelqu'un. Chez DanielCraft, on l'enseigne apres la todo et le compteur, parce que sans logique metier qui marche, sauvegarder ne sert a rien. Lea sauve des brouillons UI. Max sauve son score de basket salon. Sam montre aussi les limites avant la feerie : ce n'est pas un coffre-fort, ce n'est pas synchronise entre telephones.

Un tiroir dans ce navigateur precis, sur cet ordinateur. Tu y glisses des papiers texte etiquetes ("score", "taches", "prenom"). Tu peux les relire demain, apres un refresh, apres avoir ferme l'onglet. Si tu changes de navigateur, de machine, ou si tu vides les donnees du site, le tiroir est vide. Utile pour des preferences, un brouillon, un score perso. Pas pour des secrets. Lea explique toujours les limites avant la demo. Sam fait perdre les donnees volontairement en cours pour enseigner la fragilite.

```js
localStorage.setItem("prenom", "Nora");
const prenom = localStorage.getItem("prenom");
console.log(prenom);
```

Tu ranges avec **`setItem`**. Tu relis avec **`getItem`**. Tu vis. Et tu te souviens que tout ca reste local a ce navigateur, sur cet appareil. Change de navigateur ou vide le cache : le tiroir est vide. Utile. Local. Fragile. Les deux faces du meme outil.

## Ce que ce n'est pas

Ce n'est pas une base de donnees serveur. Rien n'est envoye sur internet automatiquement. Ce n'est pas synchronise entre appareils : le score sur le PC du bureau ne suit pas sur le telephone. Ce n'est pas safe pour mots de passe, tokens ou donnees sensibles : n'importe qui avec acces au navigateur peut lire localStorage. Ce n'est pas magique : ca stocke des **strings**. Pour nombres et listes, tu passes par conversion ou **JSON**. Et ce n'est pas "indestructible" : l'utilisateur peut vider le cache. Max a crie de joie, puis autrement, le jour du cache vide.

## Nombres et tableaux

```js
const score = 12;
localStorage.setItem("score", String(score));
const lu = Number(localStorage.getItem("score"));

const taches = ["acheter du pain", "reviser JS"];
localStorage.setItem("taches", JSON.stringify(taches));
const retrouvees = JSON.parse(localStorage.getItem("taches") || "[]");
```

Tout est string dans localStorage. Un nombre devient `"12"`. Un tableau devient une longue chaine JSON. **`JSON.stringify`** transforme en texte. **`JSON.parse`** reconstitue. Le `|| "[]"` evite de parser `null` quand rien n'a encore ete sauve : petit garde-fou, gros calme. Lea met ce pattern partout. Max l'a appris apres un crash au chargement.

:::attention
Tout est string dans localStorage. Nombres et tableaux : convertis. Et ne stocke jamais de secrets ici.
:::

## Brancher sur la todo ou le compteur

Pseudo-plan pour la todo : un tableau `taches = []` en memoire ; a chaque ajout ou suppression : modifier le tableau, sauvegarder avec `JSON.stringify`, mettre a jour le rendu ; au demarrage : charger avec `JSON.parse`, puis afficher chaque tache. Pour le score du chapitre 13 : `setItem` a chaque changement de score, `getItem` au chargement avant d'afficher. Ordre important : charger, afficher, puis ecouter les clics. Sinon tu ecoutes avec un score a zero alors que le tiroir en contient un autre.

Au load : `score = Number(localStorage.getItem("score") || "0")` puis `afficher()`. A chaque clic qui change le score : modifier, afficher, `localStorage.setItem("score", String(score))`. Ce pattern tient pour presque tout ce que tu sauveras en debutant.

:::retenir
Charger au demarrage, afficher, puis ecouter. Sauver apres chaque changement. Ordre : geste d'abord, tiroir ensuite.
:::

## Petite histoire

Max a crie quand son score a survecu au F5 pour la premiere fois. Il a montre l'ecran a toute la famille. Puis il a vide le cache du navigateur en voulant "nettoyer" et a crie autrement. Lea explique toujours les limites avant la feerie : pouvoir + prudence. Sam fait perdre les donnees volontairement en fin de seance : "regardez, ce n'est pas magique". Trois scenes, une posture : utiliser l'outil en connaissance de cause.

## Erreur classique

Oublier que tout est string : tu compares `"12" > 10` sans convertir, surprises possibles. Parser sans garde-fou : `JSON.parse(null)` plante. Stocker des secrets : mauvaise idee, point. Croire que ca marche sur un autre telephone automatiquement : non. Sauvegarder sans recharger le rendu au demarrage : les donnees existent dans le tiroir, l'ecran reste vide. Sauvegarder avant que l'ajout marche : ordre geste d'abord, memoire ensuite. Lea insiste sur l'ordre load -> afficher -> ecouter.

## En vrai

Branche localStorage sur ton compteur du chapitre 13. Sauvegarde a chaque changement. Recharge la page : le score revient. Ouvre les outils developpeur (Application / Storage), vide le stockage du site, recharge : le score repart a zero. Tu as vu les deux faces. Puis pense a ta todo : meme logique avec un tableau JSON. Lea explique toujours les limites avant la feerie. Toi aussi, tu les as vues de tes yeux.

## A toi

Branche localStorage sur ta todo : sauvegarde a chaque ajout et suppression, restauration au load. Ecris trois lignes sur ce que tu ne stockeras jamais ainsi (mots de passe, donnees clients, tokens). Posture DanielCraft : pouvoir + prudence. Montre la version qui survit au F5 a quelqu'un. L'effet "waouh" vaut le detour - a condition de connaitre la fragilite du tiroir.
