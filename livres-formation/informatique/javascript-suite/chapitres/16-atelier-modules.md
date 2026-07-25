# Chapitre 16 - Atelier : decouper en modules

Objectif : reprendre l'atelier fetch (ou le mini-projet) et le decouper en trois fichiers avec import/export. Duree : 30 a 45 minutes. Materiel : atelier-fetch fonctionnel, serveur local.

Lea dit : "Si tu ne peux pas expliquer le role de chaque fichier en une phrase, tu as decoupe trop tot ou pas assez." Cet atelier force la clarte. Max a gagne en lisibilite. Sam note la capacite a expliquer a voix haute. Chez DanielCraft, decouper n'est pas "faire joli". C'est pouvoir toucher le reseau sans casser l'affichage, et toucher l'affichage sans casser le reseau.

Tu pars d'un fichier unique qui marche. Tu le coupes. Tu verifies que ca marche encore - succes et erreur. Si ca casse, tu as decoupe trop vite ou oublie type="module". Le refactor qui "semble propre" mais ne tourne plus n'est pas un refactor. C'est une illusion.

## Les fichiers cibles

api.js porte le reseau : tu y exportes une fonction async chargerCitations qui fait le fetch, verifie ok, et renvoie le JSON. afficher.js porte le DOM : tu y exportes afficherCitations(listeEl, data) qui boucle et cree les li. main.js orchestre : il importe les deux, branche le bouton, gere try/catch et les messages. Dans le HTML, un seul script : type="module" vers main.js.

```html
<script type="module" src="main.js"></script>
```

Trois roles, trois phrases. Si une phrase est floue, renomme ou recoupe.

## Exercice 1 - Extraire api.js (10 min)

Deplace tout le fetch dans api.js. Exporte chargerCitations sans parametre si l'URL est fixe (./citations.json), ou avec url en parametre si tu preferes reutiliser. Garde if (!reponse.ok) throw ... dedans. Lea insiste : le throw reste dans api, pas dans main. Ainsi main ne connait que "ca a marche" ou "ca a plante".

## Exercice 2 - Extraire afficher.js (10 min)

Deplace la boucle qui cree les li. Exporte afficherCitations(liste, data). Option : export function afficherMessage(zone, texte) pour centraliser les textes statut. Max aime cette option : main devient encore plus mince.

## Exercice 3 - main.js orchestrateur (15 min)

Importe chargerCitations et afficherCitations. Sur clic bouton : message Chargement, try { const data = await chargerCitations(); afficherCitations(liste, data); message succes } catch { message erreur; console.error }. main.js ne doit pas contenir de fetch ni de createElement pour les li (sauf si tu as choisi de garder les messages dans main via afficherMessage). Sam fait expliquer a voix haute avant de noter.

## Exercice 4 - Verifier les tailles (5 min)

Aucun fichier ne devrait depasser environ 40 lignes pour cet exercice. Si un fichier est enorme, tu n'as pas assez decoupe ou tu as laisse du code mort. Supprime les doublons "temporaires".

## Livrable

Meme dossier qu'avant, restructure. README ou commentaire en tete de main.js : une phrase par fichier. Les deux chemins (succes, URL cassee) doivent encore marcher.

## Criteres de reussite

Ca marche comme avant (succes et erreur). Tu peux expliquer a voix haute le role de chaque fichier en une phrase. type="module" present. Serveur local utilise. Pas de fetch dans main.

## Bonus

Ajoute export function afficherErreur(zone, texte) dans afficher.js. main.js ne touche plus au textContent des messages directement. Encore plus propre.

## Petite histoire

Lea a decoupe trop tot un projet junior : six fichiers pour trente lignes, personne ne savait ou regarder. Max a laisse un monolithe de 400 lignes : impossible de tester le fetch seul. Sam a trouve le juste milieu avec cet atelier : trois fichiers, trois roles, deux chemins verifies. Chez DanielCraft, on dit : decoupe pour comprendre, pas pour impressionner.

## Erreur classique

Oublier type="module". Chemins import sans ./ (./api.js). Laisser un doublon de fetch dans main.js "temporairement". Tester en file://. Croire que "ca compile" (il n'y a pas de compile) alors que la console crie Mixed content ou Failed to resolve module.

:::attention
Sans type="module", import/export ne demarre meme pas. Verifie le HTML avant de reecrire tout le JS.
:::

## En vrai

Apres decoupage, casse encore l'URL. Verifie le message. Remets. Puis explique a quelqu'un (ou a un canard en plastique) le role de chaque fichier en une phrase. Si tu hesites, renomme. La clarte orale predit la clarte du code. Lea le fait a voix haute. Max aussi. Sam l'exige en binome.

## Note de rythme

DanielCraft forme des gens qui livrent. Un decoupage propre vaut le temps passe. Ne survole pas : fais tourner les deux chemins erreur et succes apres refactor.

## A toi

Livre la version modulaire. Ecris les trois phrases de role (api, afficher, main). Si une phrase est floue, renomme ou recoupe encore. Bonus : demande a un ami de lire seulement ces trois phrases et de predire ou vit le fetch.
