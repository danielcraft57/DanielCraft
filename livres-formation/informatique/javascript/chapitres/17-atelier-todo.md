# Chapitre 17 - Atelier : une todo liste mini

On passe a la pratique guidee. Tu vas construire une liste de taches : ecrire une tache, cliquer pour l'ajouter, la voir apparaitre dans une liste. En bonus, la supprimer d'un clic ou valider avec la touche Entree. L'objectif n'est pas une app parfaite. C'est sentir le combo **input** + **clic** + creation d'elements **DOM** - le trio que tu retrouveras partout. Duree prevue : 30 a 45 minutes si tu avances pas a pas. Chez DanielCraft, la todo est l'atelier qui fait "waouh" parce que tu construis une mini appli visible, utilisable, montrable.

Lea en a livre des versions polish pour des clients qui voulaient "quelque chose d'interactif sans refaire tout le site". Max s'en sert pour ses courses du samedi - oui, vraiment, une todo perso. Sam chronometre le premier `li` qui apparait en classe : quand il tombe, il y a souvent des sourires. Trois metiers, meme logique : d'abord ca marche en memoire vive (DOM), ensuite ca se souvient (localStorage au chapitre suivant). Lea dit toujours : "geste d'abord, tiroir ensuite".

Tu ecris dans le champ. Tu cliques Ajouter. Un item nait dans la liste. Tu cliques dessus plus tard pour le retirer (bonus). La memoire vive, c'est le DOM. Le tiroir sur le disque du navigateur, ca viendra. La, on valide le geste de base. Sans geste solide, sauvegarder ne sert a rien.

## Ce que ce n'est pas

Ce n'est pas encore localStorage - chapitre 18 juste apres. Ce n'est pas une app collaborative multi-utilisateurs. Ce n'est pas cent options (priorites, tags, dates). Ajouter proprement suffit pour valider l'atelier. Et ce n'est pas accepter le vide : une tache pleine d'espaces avec `trim()` oublie, ce n'est pas une tache. Sam refuse ca des la premiere version. Max a eu des "fantomes" dans sa liste avant d'apprendre.

## HTML

```html
<h1>Mes taches</h1>
<input id="champ" type="text" placeholder="Nouvelle tache">
<button id="ajouter">Ajouter</button>
<ul id="liste"></ul>
<script src="script.js"></script>
```

Quatre elements cles : le champ, le bouton, la liste vide qui va se remplir, le script en bas. Les ids doivent matcher ton JS. Une faute, silence total.

## JS de base

```js
const champ = document.querySelector("#champ");
const bouton = document.querySelector("#ajouter");
const liste = document.querySelector("#liste");

bouton.addEventListener("click", function () {
  const texte = champ.value.trim();
  if (texte === "") {
    return;
  }
  const li = document.createElement("li");
  li.textContent = texte;
  liste.appendChild(li);
  champ.value = "";
  champ.focus();
});
```

Pourquoi **`trim()`** ? Pour enlever les espaces avant et apres le texte saisi. Sinon tu ajoutes une tache "vide" pleine d'espaces invisibles. Moche. Frustrant. Sam refuse ca des la premiere version. Le **`return`** sur texte vide sort de la fonction sans rien creer : pas de fantome. Vider le champ et **`focus()`** remet le curseur pret pour la tache suivante. Petit detail, gros confort. Lea l'ajoute systematiquement.

:::astuce
Apres ajout : vide le champ et `focus()`. Le clavier reste pret. Tu enchaines les taches sans recliquer dans le champ.
:::

## Bonus (quand la base marche)

Valider aussi avec Entree :

```js
champ.addEventListener("keydown", function (event) {
  if (event.key === "Enter") {
    bouton.click();
  }
});
```

Supprimer au clic sur l'item :

```js
li.addEventListener("click", function () {
  li.remove();
});
```

Dis-toi que cliquer sur une tache = "c'est fait, je retire". Simple. Clair. Suffisant pour l'atelier. Tu peux livrer sans les bonus. Avec, tu gagnes en fierte et en confort d'usage.

## Petite histoire

Lea ajoute toujours `focus()` apres clear : ses clients enchainent les saisies sans friction. Max oubliait `trim` et avait des lignes vides fantomes dans sa liste de courses - sa femme a ri, puis a insiste pour le fix. Sam refuse les todos qui acceptent le vide : "si tu valides rien, rien ne doit naitre". Trois details, une appli plus humaine. Tu peux livrer la version de base. Avec les bonus, tu montres que tu penses utilisateur, pas seulement code.

## Erreur a eviter

Creer le `li` hors du listener : tu n'ajoutes qu'une fois au chargement. Oublier **`appendChild`** : element fantome invisible. Ne pas gerer le vide : liste pleine de fantomes. Tout coller sans tester item par item : tu ne sais pas ou ca casse. Vouloir localStorage avant que l'ajout marche : ordre DanielCraft, geste d'abord, memoire ensuite. Lea a vu des juniors bloquer une semaine sur la sauvegarde d'une todo qui n'ajoutait rien.

:::attention
Si rien n'apparait : loggue `texte` apres `trim`. Verifie `appendChild`. Verifie que tu ecoutes bien le bon bouton et le bon id.
:::

## Livrable

Une todo qui ajoute au minimum, avec `trim`, champ vide, et cinq lignes de lecons apprises (sur un post-it ou en commentaire). Bonus Enter + delete au clic. Montre-la a quelqu'un. Meme trente secondes. Le geste compte.

## En vrai

Ajoute trois taches reelles de ta semaine. Utilise-la une journee entiere si tu peux. Note ce qui manque (sauvegarde apres refresh ? tri ?). Tu prepares localStorage consciemment. DanielCraft aime les outils qu'on ose utiliser soi-meme - pas les demos jamais rouvertes. Si ta todo disparait au F5, c'est normal pour l'instant : le chapitre 18 est la pour ca.

## A toi

Construis la version de base. Teste avec trois taches reelles. Ajoute au moins un bonus (Enter ou delete). Ecris cinq lignes "ce que j'ai appris". Puis passe au chapitre 18 si tu veux que ta liste survive au F5. Montre-la a quelqu'un. Meme trente secondes. Le geste compte autant que le code.
