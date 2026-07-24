# Chapitre 13 - Ce qu'il faut retenir

Tu as grimpe d'un cran. Voici la carte en version poche.

## En une minute

Les formulaires : valider, `preventDefault`, messages utiles. JSON : `parse` et `stringify` pour echanger des donnees. `fetch` : demander au serveur. Promesses puis `async/await` : attendre sans embrouiller le fil. Erreurs : `response.ok` + `try/catch`. POST : envoyer un body JSON quand il faut. Modules : decouper. Organisation : un role par fichier. Debug : lire la ligne, tester une hypothese.

## Habitudes solides

1. Toujours gerer l'echec reseau
2. Montrer un etat de chargement
3. Messages humains a l'ecran, details techniques en console
4. Fichiers courts
5. Noms clairs
6. Un changement a la fois quand tu debogues

## Erreurs classiques

Oublier `await`. Oublier de verifier `ok`. Parser du HTML en croyant que c'est du JSON. Melanger DOM et fetch dans le meme monstre de fichier. Tester en `file://` avec des modules et ne pas comprendre pourquoi ca bloque.

## Suite dans ce livre

Ateliers pratiques, puis CORS, debounce, perf legere, quiz, bravo. Tu n'as pas besoin d'etre parfait. Tu as besoin d'etre capable de charger, afficher, et expliquer ce qui casse.

## Mini defi

Sans regarder tes notes, ecris de memoire le squelette `async` + `fetch` + `ok` + `json` + `catch`. Compare ensuite. Les trous montrent ce qu'il faut relire.
