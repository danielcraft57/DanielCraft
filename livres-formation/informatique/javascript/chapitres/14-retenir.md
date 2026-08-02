# Chapitre 14 - Ce qu'il faut retenir

Presque fini. Encore l'atelier todo, localStorage, la lecture des erreurs, le quiz, le bravo. Ce chapitre ne recrache pas tout le livre mot pour mot. Il range la boite a outils dans ta tete pour que tu saches quoi rouvrir quand tu bloques demain matin sur un selecteur faux ou un listener silencieux. Retenir, chez DanielCraft, ce n'est pas decorer sa memoire. C'est savoir ou est le bon outil et comment l'utiliser sans panique.

**JavaScript** rend la page interactive. Tu ranges des infos avec **`const`** et **`let`**. Tu manipules texte, nombres, booleens. Tu decides avec `if`, tu repetes avec des boucles, tu reutilises avec des **fonctions**. Les tableaux sont des listes ordonnees. Les objets sont des fiches avec des proprietes nommees. Avec le **DOM**, tu trouves et tu modifies des elements. Avec les **evenements**, tu reagis - surtout au `click` pour commencer. Lea revoit encore ces bases avant des demos clients. Max est fier de son compteur et sait qu'il grandira. Sam dit a ses eleves : retenir, c'est refaire. Une checklist ne remplace pas le geste des doigts sur le clavier.

Imagine une ceinture a outils accrochee au mur. Dessus : fichier `.js`, variables, types, `if`, boucles, fonctions, tableaux, objets, `querySelector`, `textContent` / `classList`, `addEventListener`. Chaque outil a sa place. Les ateliers qui viennent (todo, localStorage) vont te forcer a t'en servir sous pression douce. Le quiz va secouer ce que tu crois savoir. Tu n'as pas besoin de tout tenir en memoire en meme temps. Tu as besoin de savoir ou chercher et comment tester.

## Ce que ce n'est pas

Ce n'est pas "tu maitrises tout JavaScript". Loin de la. Ce n'est pas les frameworks React ou Vue - pas encore, pas ici. Ce n'est pas la fin du chemin : c'est un socle solide sur lequel tu peux construire. Lea revoit encore des bases avant des demos importantes. Max est fier de son compteur et sait qu'il y ajoutera localStorage puis autre chose. Sam dit : retenir, c'est refaire. Une checklist ne remplace pas le geste. Ne confonds pas "j'ai lu" et "je sais faire".

## Habitudes solides

Script avant `</body>` pour que le HTML existe quand le JS tourne. Noms clairs : `scoreEl` plutot que `s`. **`console.log`** pour verifier avant de deviner. Petites fonctions courtes : `afficher()`, pas un bloc de cent lignes. **`===`** pour comparer, pas `==`. Tester apres chaque petit changement, pas apres avoir ecrit cinquante lignes. Lire les erreurs en console au lieu de tout reecrire d'un coup. Une hypothese, un test, une correction. Chez DanielCraft, c'est la methode anti-drama. Lea la suit. Max l'a apprise a la dure. Sam l'enseigne des le premier cours.

:::retenir
Declarer clair. Comparer avec `===`. Trouver avant de modifier. Ecouter avant d'agir. Lire la console.
:::

## Erreurs classiques a connaitre par coeur

Selecteur DOM faux : tu obtiens `null`, puis "Cannot read properties of null". Fonction ecrite mais jamais appelee : le code existe, rien ne se passe. Boucle `while` sans fin : la page freeze, tu fermes l'onglet. Script trop haut dans le HTML : les elements n'existent pas encore. `"5" + 2` donne `"52"`, pas `7` : types melanges. `=` dans un `if` au lieu de `===` : bug sournois. Oubli de `return` dans une fonction qui doit renvoyer quelque chose. Index de tableau : le premier element est `0`, pas `1`. Tu les croiseras. Tu les reconnaitras. Chaque reconnaissance te fait gagner dix minutes de frustration.

## Petite histoire

Lea garde une checklist JS a cote de sa checklist HTML/CSS sur un post-it rose. Max a la version post-it jaune sur son ecran d'atelier. Sam fait recopier la checklist en fin de sequence : six lignes max, sans regarder le cours. Ceux qui oublient "script avant body" ou "=== pas ==" la recopient deux fois. Tu peux ecrire la tienne maintenant : six lignes max. Pas un roman. Un filet de securite pour les jours ou le cerveau est fatigue. Ce qui manque quand tu ecris sans regarder = ce qu'il faut revoir avant l'atelier todo.

## Suite possible

Atelier todo : input, clic, creation d'elements. localStorage : se souvenir apres refresh. Mieux lire les erreurs : methode en cinq etapes. Puis formulaires plus riches, `fetch`, outils modernes. Mais la : bases d'abord. Elles portent tout le reste. Lea le repete aux clients impatients de "passer a React". Max comprend maintenant. Sam le dessine au tableau : socle, puis etages.

:::attention
Un framework sur un sol mou, ca penche. Les bases de ce livre portent tout le reste. Ne saute pas a React avant de savoir selectionner un bouton.
:::

## En vrai

Rouvre ton compteur du chapitre 13. Ajoute un seul bonus sans relire le chapitre entier : un message si score >= 10, ou un bouton +5. Si tu y arrives en moins de quinze minutes, c'est entre. Sinon, relis juste la piece qui manque - pas tout le livre. Cible. Teste. Corrige. C'est la methode DanielCraft : petit, clair, actionnable.

## A toi

Ecris trois forces ("je sais brancher un clic"), deux faiblesses ("je confonds parfois const et let"), une prochaine etape (todo, localStorage, ou quiz). Date le papier si possible. Plan post-parcours. Style DanielCraft : petit, clair, honnete, actionnable. Tu sauras ou reprendre sans te noyer.
