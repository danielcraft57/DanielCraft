# Chapitre 3 - Les balises, c'est des etiquettes

Une balise, c'est une etiquette.
Elle dit au navigateur : "ce bout de texte, c'est un titre" ou "c'est un lien".

## Forme generale

```html
<nom>contenu</nom>
```

Exemple :

```html
<strong>Important</strong>
```

Ca met le mot en gras.

## Quelques balises utiles tout de suite

| Balise | Role simple |
|--------|-------------|
| `h1` a `h6` | Titres (h1 le plus grand) |
| `p` | Paragraphe |
| `a` | Lien |
| `img` | Image |
| `ul` / `ol` / `li` | Listes |
| `div` | Boite generique (on range des trucs dedans) |
| `span` | Petit bout de texte dans une phrase |
| `br` | Retour a la ligne (balise seule) |

## Balises seules (pas de fermeture)

Certaines n'ont pas de contenu a enfermer.

```html
<br>
<img src="photo.jpg" alt="Une photo">
```

`br` = aller a la ligne.
`img` = afficher une image.

## Attributs : des infos en plus

Dans une balise, tu peux ajouter des details.

```html
<a href="https://exemple.com">Clique ici</a>
```

`href` = l'adresse du lien.
`src` = le chemin de l'image.
`alt` = texte si l'image ne charge pas (utile aussi pour l'accessibilite).

## HTML, c'est de l'ordre

Le navigateur lit de haut en bas.
Ce que tu mets en premier apparait en premier (sauf si le CSS change l'ordre plus tard).

## Erreur classique

Oublier de fermer une balise.
Ou ecrire `</p>` sans avoir ouvert `<p>`.

Si la page a l'air cassee, regarde d'abord ca.
Respire. Corrige. Rafraichis.

## Mini exo

Ecris une page avec :
- un titre h1
- deux paragraphes
- un mot en gras avec `<strong>`

Si ca s'affiche, tu as compris l'idee des balises.
