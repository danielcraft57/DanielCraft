# Chapitre 5 - Liens et images

Sans liens, le web serait juste des pages isolees.
Sans images, ce serait un peu triste.

## Les liens

```html
<a href="https://danielcraft.fr">Aller sur DanielCraft</a>
```

`a` comme "ancre" (anchor en anglais).
`href` = ou ca mene.

### Lien vers une autre page de ton site

```html
<a href="contact.html">Contact</a>
```

### Lien qui ouvre un nouvel onglet

```html
<a href="https://exemple.com" target="_blank" rel="noopener">Site externe</a>
```

`target="_blank"` = nouvel onglet.
`rel="noopener"` = petite secu. Prends le reflexe.

### Lien mailto

```html
<a href="mailto:salut@exemple.com">M'ecrire</a>
```

Ca ouvre le mail (si le visiteur a un logiciel mail configure).

## Les images

```html
<img src="chat.jpg" alt="Un chat orange sur un canape">
```

`src` = ou est le fichier image.
`alt` = description. Toujours. Pour ceux qui ne voient pas l'image, et pour le referencement.

### Ou mettre tes images ?

Le plus simple au debut :

```
mon-site/
  index.html
  images/
    chat.jpg
```

Alors :

```html
<img src="images/chat.jpg" alt="Un chat orange">
```

### Largeur (debutant)

```html
<img src="images/chat.jpg" alt="Un chat" width="300">
```

Plus tard, tu gereras ca mieux avec le CSS. Pour l'instant, c'est ok.

## Figure + legende (plus propre)

```html
<figure>
  <img src="images/chat.jpg" alt="Un chat orange">
  <figcaption>Mon chat, Roi du canape.</figcaption>
</figure>
```

## A toi

1. Ajoute un lien vers une page que tu aimes.
2. Ajoute une image (une photo de chez toi, un dessin, peu importe).
3. Ecris un vrai `alt`.

Si le lien marche et l'image s'affiche, nickel.
