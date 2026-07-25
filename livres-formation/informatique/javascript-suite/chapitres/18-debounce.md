# Chapitre 18 - Debounce : ne pas frapper trop vite

Imagine une barre de recherche sur un site e-commerce. A chaque lettre tapee, tu lances un fetch vers le serveur. L'utilisateur ecrit "casque" : cinq requetes partent (c, ca, cas, casq, casque). Le serveur souffle. L'affichage clignote entre des resultats partiels. La facture API grimpe. L'experience utilisateur devient nauseeuse. Mauvaise idee partout.

Le debounce, c'est attendre un petit silence avant d'agir. Tu tapes, tu tapes, tu pauses 300 ms : la seulement, tu lances la recherche ou le filtre. Une requete utile au lieu de dix inutiles. Lea l'ajoute sur presque toute recherche live. Max l'a decouvert en filtrant sa liste de prestations. Sam le montre apres l'atelier fetch bonus.

Comme un ascenseur avec porte retardee : les gens entrent encore, la porte attend. Personne n'entre plus depuis un moment, la porte se ferme et on part. Chaque nouvelle frappe "reinitialise" le timer. Le voyage n'a lieu qu'apres la pause.

## Idee en code

```js
function debounce(fn, delai) {
  let timer;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delai);
  };
}

const rechercher = debounce((texte) => {
  console.log("Je cherche :", texte);
  // ici : fetch ou filtre local sur cache
}, 300);

input.addEventListener("input", (e) => rechercher(e.target.value));
```

debounce prend une fonction et un delai en ms. Elle renvoie une nouvelle fonction. A chaque appel, le timer precedent est annule et un nouveau demarre. Quand l'utilisateur s'arrete assez longtemps, fn s'execute une fois avec la derniere valeur.

## Filtre local vs fetch

Si tu as deja charge toutes les citations en memoire (atelier 15), debounce plus filtre local suffit souvent : pas de reseau, instantane apres la pause. Si tu cherches dans une grosse base distante, debounce plus fetch evite le spam. Ne confonds pas : debounce ne remplace pas le cache ni le debounce cote serveur pour des apps enormes, mais pour ce livre c'est largement suffisant.

## Quand l'utiliser

Recherche pendant la frappe. Redimensionnement de fenetre (recalcul layout). Sauvegarde auto d'un brouillon. Partout ou un evenement se repete trop vite et ou tu veux une action "finale" apres stabilisation.

## Quand ne pas l'utiliser

Un clic sur "Envoyer" : pas besoin, un clic = une action. Un compteur de jeu a chaque frame : ce n'est pas le meme outil (throttle serait plus adapte, hors scope ici). Une validation de formulaire au submit : non plus.

## Petite histoire

Lea a deploye une recherche sans debounce. L'API a rate-limite le client en heure de pointe. En ajoutant 300 ms de debounce et un filtre local sur les resultats deja charges, le probleme a disparu. Quinze lignes de code, grosse difference.

## Erreur classique

Mettre un delai ridiculement court (10 ms) : tu as encore trop de requetes. Trop long (2000 ms) : l'interface semble molle. 250-400 ms est un bon depart pour une recherche texte. Oublier clearTimeout : timers multiples s'empilent. Copier debounce sans comprendre : difficile a debugger.

## En vrai

Ajoute un debounce sur un champ input qui console.log la valeur. Tape vite "bonjour". Verifie qu'un seul log apparait apres ta pause, pas sept. Ajuste delai au feeling. Si tu vois encore sept logs, ton clearTimeout ne tourne pas : relis la fonction.

## A toi

Reprends l'atelier fetch avec filtre bonus. Enveloppe la fonction de filtre dans debounce(..., 300). Teste en tapant vite. Note combien de filtrages reels se declenchent. Si c'est un par "rafale de frappe", c'est gagne. Bonus : passe a 400 ms et sens la difference de "molle".

## Debounce vs throttle (apercu)

Debounce : agir apres la pause (recherche). Throttle : agir au plus une fois par intervalle fixe (scroll, resize intense). Ce livre reste sur debounce car c'est le cas le plus frequent pour les recherche live. Si un jour tu scroll une carte qui doit se mettre a jour en continu, tu chercheras throttle. Ne melange pas les deux sans raison.

## Variante avec fonction nommee

```js
function filtrerListe(texte) {
  // filtre sur cache local
}
const filtrerDebounced = debounce(filtrerListe, 300);
input.addEventListener("input", (e) => filtrerDebounced(e.target.value));
```

Separer filtrerListe et debounce rend le test plus facile : tu peux appeler filtrerListe directement en console sans attendre le delai. Lea garde cette structure pour deboguer plus vite. Max aussi, depuis qu'il a du "sentir" le timer a l'aveugle.

## En resume

Debounce protege le reseau, le serveur, et les yeux de l'utilisateur. Ce n'est pas du luxe sur une recherche live. C'est hygiene. Combine au cache local (liste deja chargee), tu obtiens une UX fluide sans infrastructure complexe. DanielCraft recommande ce duo sur tout champ de filtre branche a fetch ou a une grosse liste DOM. Une pause de 300 ms, c'est souvent invisible pour l'humain et precieux pour le serveur.
