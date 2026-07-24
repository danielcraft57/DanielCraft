# Chapitre 19 - Accessibilite et bonnes manieres

Accessibilite, ca veut dire : le plus de gens possible peuvent utiliser ta page.
Y compris avec un clavier, un lecteur d'ecran, ou un contraste faible.

Pas besoin d'etre expert. Juste quelques reflexes.

## Textes a la place des images

```html
<img src="chat.jpg" alt="Chat orange assis sur un canape">
```

Pas : `alt="image"` (inutile).
Pas : `alt=""` sauf si l'image est purement decorative.

## Contraste

Texte gris clair sur fond blanc = fatigue.
Texte sombre sur fond clair = mieux.
Si tu plisses les yeux pour lire, change.

## Liens clairs

Mauvais : "Clique ici"
Mieux : "Voir les tarifs"

Le texte du lien doit dire ou on va.

## Boutons assez gros

Sur telephone, un tout petit bouton c'est l'enfer.
Laisse de l'air. Vise une zone confortable.

## Titres dans l'ordre

`h1` puis `h2` puis `h3`.
Pas de saut bizarre juste pour la taille.
La taille, c'est le CSS.

## Clavier

Essaye : touche Tab sur ta page.
Tu dois pouvoir atteindre liens et boutons.
Si tu te perds, simplifie.

## Mini checklist

- [ ] `alt` utiles
- [ ] contraste ok
- [ ] liens explicites
- [ ] titres ranges
- [ ] zones cliquables confortables
- [ ] viewport present

## A toi

Reprends ta page perso.
Corrige 3 points d'accessibilite.
C'est deja un vrai plus.
