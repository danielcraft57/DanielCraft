# Chapitre 11 - Lire une erreur du compilateur

Une erreur **`tsc`**, ce n'est pas une insulte. C'est un rapport : fichier, ligne, message. Chez DanielCraft, on apprend a lire avant de googler au hasard. Lea ouvre toujours le premier diagnostic, pas le vingtieme. Max respirait mal devant le rouge ; maintenant il cherche le type attendu vs le type fourni. Sam enseigne une grille : ou ? quoi ? pourquoi probable ? correction minimale ?

Le message typique ressemble a : `Type 'string' is not assignable to type 'number'.` Traduction : tu ranges du texte dans une boite nombre. Autre classique : `Property 'email' does not exist on type 'Contact'.` Traduction : soit faute de frappe, soit champ absent de l'interface, soit narrowing manquant. Encore : `Object is possibly 'undefined'.` Traduction : optionnel ou tableau vide, ajoute un garde. Une fois que tu traduis, la peur baisse.

:::retenir
Lis l'erreur comme une phrase : type fourni vs type attendu, propriete manquante, valeur peut-etre vide. Puis corrige une chose.
:::

## Ce que ce n'est pas

Ce n'est pas "TypeScript est casse". Ce n'est pas une raison d'ajouter `as any`. Ce n'est pas ignorer la ligne indiquee pour reecrire tout le fichier. Et ce n'est pas honteux d'avoir des erreurs : c'est le mode normal d'apprentissage. Lea en produit encore. La difference, c'est la vitesse de lecture. Max notait autrefois "ca marche pas" ; maintenant il note le message exact.

## Methode calme

1. Ouvre le fichier et la ligne cites.
2. Lis le message jusqu'au bout (souvent la fin dit l'attendu).
3. Identifie si c'est assignation, appel de fonction, acces propriete, ou absence de return.
4. Corrige le minimum : type, valeur, `if`, ou signature.
5. Relance `tsc`. Une erreur de moins = progres.

```ts
let total: number = 0;
// total = "120";
// error: Type 'string' is not assignable to type 'number'.
total = 120;
```

Parfois l'editeur souligne en rouge avant meme `tsc`. C'est le meme moteur. Lea regarde le survol (hover) : TypeScript explique souvent l'attendu. Sam demande aux eleves de lire a voix haute : la salle rit, puis comprend.

:::astuce
Corrige la premiere erreur d'abord. Les suivantes sont parfois des cascades.
:::

## Petite histoire

Max a passe une soiree a "desactiver strict" parce qu'une propriete optionnelle le genait. Sam lui a montre le `if (user.age !== undefined)`. Dix minutes. Lea, en revue, refuse les PR qui ajoutent `// @ts-ignore` sans justification. Elle demande le message original dans le commentaire de revue. DanielCraft : le rouge est un professeur severe mais coherent. Le jour ou Max a corrige trois erreurs sans chat, il a sourit tout seul.

## Erreur classique

Lire seulement "error" et paniquer. Coller le message dans un chat sans le fichier. Ajouter `!` (non-null assertion) partout pour silence. Autre piege : corriger le type pour qu'il accepte n'importe quoi (`string | number | boolean | null`) au lieu de corriger la donnee. Prefere la donnee honnete.

:::attention
`// @ts-ignore` et `as any` font taire le professeur. Ils n'enlevent pas le bug. Utilise-les seulement en dernier recours documente.
:::

## En vrai

Introduis volontairement trois erreurs : mauvaise assignation, propriete inconnue, return manquant. Lis chaque message a voix haute. Corrige. Tu entraines le muscle. Chronometre-toi : le but n'est pas la vitesse olympique, c'est la lecture complete.

## Traduire le rouge en action

Fabrique-toi un mini dictionnaire perso. "not assignable" = mauvaise valeur pour ce type. "does not exist" = champ inconnu ou narrowing manque. "possibly undefined / null" = garde manquant. "Expected N arguments" = appel de fonction incomplet. Lea colle ce dictionnaire dans le README stagiaires. Max l'a dans sa tete maintenant. Sam interroge : "traduis cette erreur en une phrase francaise" avant d'autoriser la correction.

Ne corrige pas au hasard. Change une chose, recompile, observe. Si l'erreur se deplace, tu progresses. Si elle mute en autre chose, lis la nouvelle. Les cascades existent : une mauvaise interface produit dix diagnostics. Repare la source.

Evite aussi le piege du message en anglais "je ne comprends rien". Tu n'as pas besoin de tout comprendre : tu as besoin des mots types et des noms de variables cites. Relie-les a ton code. C'est un jeu de pistes, pas une dissertation.

## A toi

Prends un petit fichier type. Casse-le. Note pour chaque erreur : (1) ligne, (2) en francais ce que TS reproche, (3) ta correction. Chez DanielCraft, cette fiche d'erreurs vaut un chapitre de theorie supplementaire. Garde-la a cote du mini-projet.
