# Chapitre 18 - Erreurs classiques TypeScript

Tu vas croiser les memes pieges souvent. Ce chapitre les nomme pour que tu les reconnaisses vite. Chez DanielCraft, on prefere une liste courte et vicieuse a un catalogue encyclopedique. Lea les voit en revue de code. Max les a toutes faites. Sam les affiche en debut de seance "erreurs du mois".

Le point commun : vouloir le silence du compilateur au lieu du contrat clair. `any`, ignore, mauvais cast, union fourre-tout, optionnel jamais verifie. Si tu sens l'envie de "juste compiler", pause. Relis le message.

:::retenir
Les classiques : `any` partout, `@ts-ignore`, `as` sans preuve, unions trop larges, optionnels sans garde.
:::

## Ce que ce n'est pas

Ce n'est pas une honte d'avoir fait ces erreurs. Ce n'est pas non plus une interdiction absolue de chaque outil (un `as` rare peut exister). C'est un radar. Lea autorise un escape hatch documente. Max documentait trop tard. Sam exige la raison dans un commentaire d'une ligne.

## Les pieges a coller au mur

**1. `any` de confort.** Ca compile. Les bugs aussi. Remplace par interface ou union.

**2. `as Type` magique.** Tu forces. Prefere narrowing.

**3. `// @ts-ignore` / `@ts-expect-error` sans suite.** Le professeur est baillonne.

**4. `string | number | boolean | null | undefined`.** Union poubelle. Modele mieux.

**5. Optionnel puis `.methode()` direct.** Crash. Garde d'abord.

**6. `!` non-null partout.** Tu affirmes sans preuve.

**7. JSON.parse puis `as MonType`.** Aucune validation.

```ts
// fragile
const data = JSON.parse(raw) as TodoItem;

// plus honnete (debut)
const data: unknown = JSON.parse(raw);
// puis narrowing / validation des champs
```

:::attention
Faire taire `tsc` n'est pas corriger. C'est reporter la facture au runtime.
:::

## Petite histoire

Un PR de Max ajoutait trois `as any` "temporaires". Lea a demande les messages originaux. En vingt minutes, deux etaient des narrowing simples, un etait une vraie interface manquante. Sam a garde l'histoire pour la promo suivante. DanielCraft : le temporaires sans date devient permanent.

## Erreur classique (meta)

Lire ce chapitre, hocher la tete, puis remettre `any` le soir meme sous pression. Antidote : une regle d'equipe "pas de `any` sans TODO date". Autre piege : elargir le type jusqu'a ce que tout passe. Prefere corriger la donnee.

:::astuce
Quand tu tapes `any` ou `as`, ecris une phrase : "je fuis quelle erreur exacte ?" Si tu ne sais pas, relis le diagnostic.
:::

## En vrai

Ouvre un vieux fichier. Cherche `any`, `as `, `@ts-ignore`. Pour chacun, tente une vraie correction. Chronometre. Souvent moins long que tu ne le crains.

## Comment utiliser cette liste

N'essaie pas de tout memoriser d'un coup. Imprime ou copie les titres. Chaque fois que tu bloques dix minutes, scanne la liste. Souvent le piege est deja nomme. Lea le fait en mentoring : "c'est le numero 3, recompile". Max a affiche la liste a cote du moniteur une semaine. Sam en tire des QCM rapides en debut de seance.

Ajoute tes propres erreurs quand tu en decouvres. Le chapitre devient vivant. TypeScript n'invente pas de nouveaux peches chaque mois au niveau debutant : ce sont souvent les memes dix. Les maitriser te rend etonnamment rapide.

## A toi

Liste tes trois pieges personnels (ceux que tu referais demain). A cote, la correction preferee. Colle la liste pres de l'ecran. Chez DanielCraft, cette feuille bat un chapitre relu passivement.
