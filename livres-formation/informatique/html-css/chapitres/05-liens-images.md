# Chapitre 5 - Liens et images

Sans liens, le web serait des pages isolees. Sans images, ce serait souvent triste - ou du moins plus abstrait. Les liens connectent. Les images montrent. Ensemble, ils font passer une page de "texte sur fond" a "petit monde navigable". Chez DanielCraft, on apprend les deux avec la meme exigence : un lien clair, une image decrite, des chemins qui existent vraiment. Lea verifie chaque lien avant de livrer. Max a appris les `alt` utiles apres un retour client. Sam note des points si l'`alt` dit juste "image".

Un lien, c'est la balise **`a`** (anchor, ancre). L'attribut **`href`** dit ou ca mene. Une image, c'est **`img`**, avec `src` pour le fichier et **`alt`** pour la description. En 2026, quand quelqu'un dit "ma page a des liens et des photos", il parle souvent de ca. Derriere, il y a des galeries et des menus complexes. Pour toi, le geste reste simple : promesse claire, chemin reel, description utile. Tu restes le pilote. Le visiteur suit.

:::retenir
Lien = `a` + `href` + texte clair. Image = `src` + `alt` utile. Chemins reels, noms coherents.
:::

## Ce que ce n'est pas

Ce n'est pas "clique ici" partout. Le texte du lien doit dire la destination. Ce n'est pas une image sans `alt` "parce que c'est evident". Ce n'est pas non plus coller vingt photos enormes sans dossier `images/`. Et ce n'est pas encore du CSS : on peut mettre une largeur debutant, mais le vrai controle viendra plus tard.

Ce n'est pas non plus une image "dans" le HTML. Le HTML pointe vers un fichier a cote. Si le fichier manque, tu vois une icone cassee. C'est normal. Ca veut dire : verifie le chemin, pas panique sur le code. Lea dit : "le HTML montre le chemin ; le fichier doit exister au bout".

Pense a un plan de ville. Les liens sont les routes entre les lieux. Les images sont les photos sur le plan. Si une route mene nulle part (`href` casse), le visiteur se perd. Si une photo n'a pas de legende (`alt` vide inutile), une partie des gens ne comprend pas. Tu construis des chemins et des preuves visuelles. Lea dit : "un lien, c'est une promesse ; une image, c'est une preuve". Max compare a un devis : "si le chemin photo est faux, le client croit que je n'ai pas de realisations". Sam dessine des fleches au tableau entre pages.

## Les liens

```html
<a href="https://danielcraft.fr">Aller sur DanielCraft</a>
```

Vers une autre page de ton site : `<a href="contact.html">Contact</a>`. Vers un nouvel onglet : ajoute `target="_blank"` et `rel="noopener"` (petite secu, prends le reflexe). Pour ouvrir le mail : `<a href="mailto:salut@exemple.com">M'ecrire</a>` - ca marche si le visiteur a un client mail configure. Pour appeler : `<a href="tel:0612345678">Appeler</a>`. Max utilise les deux sur sa page artisan. Lea refuse les "clique ici". Sam raye ce texte sur les copies.

:::astuce
Texte du lien = destination claire. "Contact" bat "clique ici". Toujours.
:::

## Les images

```html
<img src="chat.jpg" alt="Un chat orange sur un canape">
```

`src` = ou est le fichier. `alt` = description. Toujours. Pour ceux qui ne voient pas l'image, pour le referencement, pour toi quand le chemin est faux. Organise ton projet simplement :

```
mon-site/
  index.html
  images/
    chat.jpg
```

Alors : `<img src="images/chat.jpg" alt="Un chat orange">`. Largeur debutant possible avec `width="300"` ; plus tard, le CSS fera mieux. Attention a la **casse** : `Photo.JPG` et `photo.jpg` ne sont pas pareils sur tous les serveurs. Max a appris ca sur le telephone de son neveu. Lea normalise tout en minuscules des le premier jour.

## Figure + legende

```html
<figure>
  <img src="images/chat.jpg" alt="Un chat orange">
  <figcaption>Mon chat, Roi du canape.</figcaption>
</figure>
```

Plus propre quand tu veux une legende visible, pas seulement un `alt`. Le `alt` decrit pour l'accessibilite ; le `figcaption` commente pour tout le monde. Lea utilise `figure` sur les portfolios. Sam le demande des qu'une image porte un message pedagogique. Max l'utilise pour une photo de chantier avec une legende honnete.

## Petite histoire

Lea livrait une page portfolio. Deux liens menaient a d'anciennes URL. Le client a clique devant elle. Silence. Elle a rougi, corrige en cinq minutes, et ajoute une checklist "cliquer chaque lien". Max avait mis `src="Photo.JPG"` alors que le fichier etait `photo.jpg`. Sur son PC Windows, parfois ca passait. Sur le telephone du neveu, non. Il a normalise les noms en minuscules. Sam fait casser les liens volontairement en cours pour forcer le debug calme. Trois scenes, une hygiene : teste avant de montrer.

:::attention
`alt="image"` ne sert a rien. Decris ce qu'on voit : sujet, contexte, utile.
:::

## Erreur classique

Oublier le dossier `images/`. Ecrire `alt="image"`. Utiliser "clique ici". Ouvrir un nouvel onglet sans `rel="noopener"`. Croire que l'image "est dans le HTML" alors qu'elle est un fichier a cote. HTML pointe. Il n'embarque pas magiquement la photo. Autre piege : lien vers `http://` sur un site en `https://` - parfois ca bloque. Garde les chemins simples et coherents. Chez DanielCraft, un chemin clair bat une galerie fancy cassee.

## En vrai

Ajoute un lien vers une page que tu aimes. Ajoute une image (photo, dessin, peu importe). Ecris un vrai `alt`. Clique le lien. Si l'image ne s'affiche pas, lis le `src` a voix haute et verifie le dossier. Ouvre les outils developpeur : parfois le navigateur te dit exactement quel fichier il cherche. Corrige. Relance. Le geste compte plus que la theorie.

## A toi

Fais une mini page "Mes trois liens utiles" avec trois ancres explicites, une image avec `figure`/`figcaption`, et un `mailto` vers une adresse fictive. Note le chemin exact de ton image. Ce papier te servira au debug. Puis clique chaque lien : tu entraines le reflexe pro que DanielCraft attend avant livraison. Garde cette page pour le mini-projet.
