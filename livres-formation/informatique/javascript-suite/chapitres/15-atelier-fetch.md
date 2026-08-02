# Chapitre 15 - Atelier : fetch et afficher

Objectif : charger un fichier JSON local et remplir une liste HTML avec gestion complete du chargement et des erreurs. Duree : 30 a 45 minutes. Materiel : editeur, serveur local (Live Server ou python -m http.server).

Sam utilise cet atelier avant le chapitre modules : d'abord tout dans un fichier, puis decoupe. Lea verifie que response.ok et le message d'erreur sont presents. Max l'a fait avec des citations au lieu de produits. L'important : le parcours fetch complet. Chez DanielCraft, on ne valide pas "ca affiche quelque chose". On valide les deux chemins : succes et echec.

Tu vas sentir pourquoi file:// te ment souvent. fetch aime un vrai serveur local, meme minuscule. Si tu ouvres le HTML en double-clic et que "ca marche pas", ce n'est pas forcement ton code - c'est le protocole. Note ca. Tu gagneras une heure la prochaine fois.

## Preparation

Cree un fichier citations.json a cote de ta page :

```json
[
  { "texte": "Petit a petit, l'oiseau fait son nid.", "auteur": "Proverbe" },
  { "texte": "On apprend en faisant.", "auteur": "DanielCraft" },
  { "texte": "Le code clair se lit comme une histoire.", "auteur": "Atelier" }
]
```

Sers le dossier avec un petit serveur local. Ouvrir index.html en file:// fera souvent echouer fetch : c'est normal, pas un bug de ton code.

## Exercice 1 - HTML et bouton (5 min)

Page avec titre, bouton "Charger les citations", ul#liste, p#message. Style minimal optionnel. Lea ajoute parfois un petit CSS pour que ca ressemble a une vraie mini-app - pas obligatoire pour valider.

## Exercice 2 - fetch async (15 min)

Au clic, message.textContent = "Chargement...". fetch("./citations.json"). Verifie reponse.ok. await reponse.json(). Vide la liste. Pour chaque item, cree un li avec texte et auteur (ex. "texte - auteur"). message = N citations chargees. Si tu oublies de vider innerHTML, un second clic double la liste : piege classique.

## Exercice 3 - Erreurs (10 min)

try/catch autour du tout. URL cassee volontairement (citations.json -> citatons.json) : message humain "Impossible de charger. Reessaie." plus console.error(e). Remets la bonne URL et verifie les trois citations visibles. Sam note surtout cet exercice : sans lui, tu n'as qu'une demi-competence.

## Exercice 4 - Bonus recherche locale (15 min optionnel)

Ajoute un input#filtre. A chaque frappe, filtre la liste deja chargee en memoire (pas de nouveau fetch a chaque lettre). Stocke les citations dans une variable let cache = null apres le premier chargement. Le chapitre debounce affinera ce comportement. Max adore ce bonus : ca donne tout de suite l'impression d'un outil.

## Livrable

Dossier atelier-fetch/ avec index.html, app.js, citations.json. Deux tests notes : succes (3 items) et echec (URL cassee). Sans les deux, l'atelier n'est pas fini.

## Criteres de reussite

Trois citations visibles en cas de succes. URL cassee -> message d'erreur, pas de page blanche. Pas d'exception non geree dans la console (sauf ton log volontaire dans catch). Etat "Chargement..." visible pendant l'attente.

## Petite histoire

Sam a fait faire cet atelier a une classe. La moitie a oublie response.ok et affichait "0 citations" sur une 404. L'autre moitie a casse l'URL et a vu le message. Devine qui a vraiment compris fetch ? Ceux qui ont teste l'echec. Lea raconte la meme scene en stage. Chez DanielCraft, c'est devenu un rituel : casse avant de dire "c'est bon".

## Erreur classique

Oublier return ou await sur reponse.json(). Oublier de vider innerHTML avant de remplir (double clic = double liste). Tester sans serveur local et conclure que fetch "ne marche pas". Afficher le stack trace a l'utilisateur au lieu d'un message humain.

:::attention
file:// n'est pas ton ami pour fetch. Sers le dossier. Sinon tu debogues un fantome.
:::

## En vrai

Lance le chemin heureux. Puis renomme le JSON une seconde. Clique. Lis le message. Remets le nom. Clique. Si les deux chemins sont nets, tu as le muscle. Chronometre : en moins de deux minutes, tu dois pouvoir basculer entre succes et echec sans toucher au JS (juste le nom de fichier). Lea chronometre ses juniors. Max aussi, pour lui-meme.

## Note de rythme

Prends le temps. Un atelier fait a fond vaut mieux que trois ateliers survoles. DanielCraft forme des gens qui livrent, meme petit. Ecris le livrable, meme minimal.

## A toi

Livre l'atelier. Puis reecris la fonction charger en async/await si tu l'avais faite en then. Compare. Garde la version la plus lisible pour l'atelier modules suivant. Bonus : note en une phrase ce que tu as appris en forcant l'erreur.
