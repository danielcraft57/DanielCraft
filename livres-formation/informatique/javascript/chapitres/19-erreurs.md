# Chapitre 19 - Erreurs JS frequentes (et comment les lire)

Le navigateur parle. Apprends a l'ecouter au lieu de paniquer. La **console** (F12, onglet Console) affiche du rouge quand quelque chose bloque. Souvent avec un numero de ligne et un fichier. Lire ca, ce n'est pas etre nul. C'est avancer. Chez DanielCraft, on dit que debugger, c'est un metier - pas une punition. Lea lit les stacks tous les jours sur des projets clients. Max a gagne en calme le jour ou il a suivi la ligne indiquee au lieu de tout effacer. Sam transforme chaque message d'erreur en enigme devant ses eleves : "qu'est-ce que le navigateur essaie de te dire ?"

Le navigateur est un collegue sec mais honnete. Il ne te jugera pas. Il te dit ou ca fait mal : fichier, ligne, type d'erreur. Toi, tu vas a la ligne indiquee, tu poses un **`console.log`** juste avant pour voir ce qui se passe, tu corriges le plus petit truc possible, tu retestes. Max prefere ca aux soirees entieres a tout recommencer. Sam affiche les messages au video-projecteur comme des indices de jeu d'enquete. L'erreur devient un puzzle, pas une humiliation.

Tu vas croiser "X is not defined" : variable absente, faute de frappe, mauvaise portee. "Cannot read properties of null" : `querySelector` a renvoye vide, script trop haut, id faux. "Unexpected token" : syntaxe cassee - parenthese, crochet, guillemet oublie. Boucle infinie : page freeze, fan du PC qui tourne, `while` sans fin. Chaque message a une cause typique. Tu apprends le dialecte. Ensuite, tu paniques moins. Tu corriges plus vite. Lea raconte qu'un junior a reecrit 80 lignes pour une typo sur la ligne 12. Elle lui a appris a lire la ligne 12.

## Ce que ce n'est pas

Ce n'est pas paniquer et tout effacer pour recommencer de zero. Ce n'est pas ignorer le numero de ligne parce que "c'est du charabia". Ce n'est pas "ca marche sur mon PC" sans lire le message. Une methode anti-stress bat dix reecritures aveugles. Et ce n'est pas une honte : Lea, Max et Sam cassent encore regulierement. La difference, c'est la methode. Lea appelle ca "chirurgie", pas "demolition".

## Methode en 5 etapes

1. Lis le message (meme si tu ne comprends pas tout).
2. Va a la ligne indiquee dans ton fichier.
3. `console.log` juste avant pour voir l'etat des variables.
4. Corrige le plus petit truc possible (une typo, un id, une parenthese).
5. Reteste. Recommence si une nouvelle erreur apparait.

:::retenir
Lis. Va a la ligne. Log. Corrige petit. Reteste. Cinq gestes, moins de drama.
:::

## Erreurs frequentes detaillees

"X is not defined" : faute de frappe (`scoree` vs `score`), variable declaree dans un bloc mais utilisee ailleurs, script charge avant la definition. "Cannot read properties of null" : selecteur faux, `#id` qui n'existe pas, script place trop haut dans le HTML avant que l'element existe. "Unexpected token" : relis les guillemets, les accolades, les parentheses autour de la ligne indiquee - souvent une virgule ou un `)` manquant. Boucle infinie : la page freeze, coupe l'onglet, ajoute l'increment manquant dans ton `while`, reprends calmement. `"5" + 2` donne `"52"` : types melanges, pas une erreur rouge mais un bug logique. `=` dans un `if` au lieu de `===` : le code tourne, le resultat est faux.

## Petite histoire

Lea raconte un junior qui a reecrit 80 lignes pour une typo sur un nom de variable. Elle lui a appris a lire "line 12" et a corriger deux caracteres. Vingt secondes. Max a freeze son navigateur avec un `while` sans increment, a eu peur, puis a ri en voyant que c'etait juste une ligne oubliee. Sam affiche des messages d'erreur au video-projecteur : "Cannot read properties of null - qui veut deviner ?" Les eleves cherchent. L'erreur devient un jeu. Toi aussi, tu peux jouer.

:::astuce
Casse volontairement un truc qui marche. Renomme un id. Oublie une parenthese. Lis l'erreur. Repare. Tu entraines le reflexe sans la pression d'un vrai bug en production.
:::

## Exercice atelier

Casse volontairement ton compteur : renomme un id dans le HTML sans toucher au JS. Lis l'erreur. Repare. Casse une `const` en tentant de la reassigner. Lis. Repare. Casse une parenthese dans une fonction. Lis. Repare. Trois casses, trois lectures, trois victoires. Le calme s'installe avec la repetition. Pas magie. Habitude.

## En vrai

Ouvre la console sur une page qui marche (ton compteur ou ta todo). Provocation volontaire : une typo dans un selecteur. Observe le message rouge. Va a la ligne. Corrige. Observe la disparition du rouge. Le reflexe s'installe. Prochaine panique reelle, tu commences par F12 au lieu de tout effacer. Lea appelle ca "chirurgie". Max prefere ca aux soirees a tout recommencer. Toi aussi, tu peux.

## A toi

Cree une mini fiche "mes 4 erreurs" avec pour chacune : le message, la cause typique, le fix en une ligne. Colle-la pres de ton ecran. Prochaine panique, tu commences par la fiche, pas par le bouton "tout supprimer". Reflexe DanielCraft : methode avant drama. Dans une semaine, ajoute une cinquieme erreur que tu auras croisee. La fiche grandit avec toi.
