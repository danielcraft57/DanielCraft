# Chapitre 14 - A retenir

Tu as traverse le socle TypeScript debutant. Ce chapitre ne rajoute presque rien de neuf : il range. Chez DanielCraft, on fait souvent une carte avant les ateliers. Lea coches ce qu'elle reutilise chaque semaine. Max relit cette page avant une session de code. Sam s'en sert comme checklist orale en fin de module.

TypeScript, c'est JavaScript plus des **types** verifies avant l'execution. Tu ecris en `.ts`, tu lances **`tsc`**, tu obtiens du `.js`. Les annotations (`: string`) et les **interfaces** decrivent des contrats. Les **unions** (`|`) et les **optionnels** (`?`) disent la verite sur les cas multiples. Les fonctions et tableaux types rendent les appels plus surs. Le **narrowing** prouve un type dans un `if`. Tu evites **`any`**, tu preferes `unknown` ou un vrai modele. Tu lis les erreurs du compilateur au calme. Tu gardes le DOM avec des `null` checks.

:::retenir
Types, interfaces, unions, narrowing, erreurs lues : voila la carte. Le reste est de la pratique.
:::

## Ce que ce n'est pas

Ce n'est pas la fin de TypeScript. Generics avances, utilitaires `Partial`, monorepos, decorateurs : hors scope ici. Ce n'est pas non plus un examen. Si une case de la carte est floue, tu retournes au chapitre, tu ne fais pas semblant. Lea dit : "mieux vaut trois briques solides que vingt notions citees".

## Carte rapide

- Install / `tsc` / `tsconfig` leger
- string, number, boolean
- annotation `: type` et inference
- interface pour les objets
- `|` et `?`
- fonctions typees (params + retour)
- `Type[]`
- narrowing avec `typeof` / `if`
- `any` rare, `unknown` + preuve
- lire `tsc`, pas l'eteindre
- DOM : query + garde
- mini-projet compteur

Max imprime parfois cette liste. Sam la fait reformuler a voix haute sans jargon. DanielCraft mesure le succes a "je peux expliquer a un ami", pas a "j'ai survole vingt videos".

:::astuce
Pour chaque item de la carte, cite un exemple de ton propre code. Si tu ne peux pas, relis le chapitre correspondant.
:::

## Petite histoire

Apres le mini-projet, Max a dit "en fait c'est surtout de la precision". Lea a sourit : c'etait exactement le message. Sam a ferme le projecteur et demande trois mots. Les eleves ont repondu : contrat, compilateur, preuve. Pas "framework". Pas "magie". Chez DanielCraft, ces trois mots suffisent pour repartir coder.

## Erreur classique

Croire qu'il faut tout memoriser avant d'ouvrir un fichier. Ou au contraire tout sauter pour "faire React demain". Autre piege : garder `any` "en attendant" sans date de retour. La carte sert a prioriser, pas a culpabiliser.

:::attention
Si tu ne retiens qu'une chose : lis l'erreur, corrige le contrat, recompile. Ce cycle bat la theorie isolee.
:::

## En vrai

Sans notes, ecris sur papier les dix idees que tu gardes. Compare a la liste ci-dessus. Entoure les trous. Planifie deux relectures ciblees avant les ateliers.

## Fil rouge DanielCraft

Si tu ne devais garder que cinq phrases : (1) TS verifie avant d'executer. (2) Annoter le coeur. (3) Interface pour les objets. (4) Prouver avec narrowing. (5) Eviter `any`, lire `tsc`, recompiler. Tout le reste du livre illustre ces phrases avec Lea, Max et Sam.

Relie aussi mentalement ce livre au parcours JavaScript bases. Variables, fonctions, tableaux, DOM : tu les as deja. TypeScript ne les remplace pas. Il les etiquette. Quand tu reviendras a un script JS nu, tu sentiras le manque du filet - et tu sauras quoi ajouter.

Prochaine etape pratique : les ateliers. Ils ne rajoutent pas beaucoup de theorie. Ils forcent le geste. Fais-les pour de vrai, meme imparfaits. Un atelier termine vaut trois chapitres relu a vitesse x2.

## Reviser en boucle courte

Prends trois soirs de vingt minutes. Soir 1 : annotations + fonctions. Soir 2 : interfaces + unions + narrowing. Soir 3 : DOM + mini projet + lecture d'erreurs. Tu n'as pas besoin de tout relire. Tu as besoin de refaire. Lea revise comme ca avant de former. Max a prefere binge-watch des videos et a moins retenu. Sam impose la boucle courte en fin de module.

Garde aussi une question talisman : quelle valeur illegale mon type refuse-t-il ? Si tu ne sais pas repondre pour une variable, ton annotation est decorative. Si tu sais, tu pilotes. C'est le test DanielCraft pour savoir si tu as vraiment fini les bases.

## A toi

Choisis un petit script JS personnel. Liste trois endroits ou un type t'aiderait. Annote-les en TS. Compile. Tu viens de transformer la carte en geste. C'est le but DanielCraft.
