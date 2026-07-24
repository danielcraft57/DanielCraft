# Chapitre 8 - CSS : on habille la page

La le HTML est nu. On va lui mettre des habits.

## Trois facons d'ajouter du CSS

### 1. Dans le fichier HTML (balise style)

```html
<head>
  <style>
    p {
      color: blue;
    }
  </style>
</head>
```

Pratique pour tester. Moins propre sur un gros site.

### 2. Fichier CSS separe (le mieux)

`style.css` :

```css
p {
  color: blue;
}
```

Dans le HTML :

```html
<link rel="stylesheet" href="style.css">
```

Mets le `<link>` dans le `<head>`.

### 3. En ligne (a eviter souvent)

```html
<p style="color: blue;">Coucou</p>
```

Ca marche. Mais ca devient vite le bordel. Garde ca pour des cas rares.

## Anatomie d'une regle CSS

```css
selecteur {
  propriete: valeur;
}
```

Exemple :

```css
h1 {
  color: tomato;
  font-size: 40px;
}
```

Le selecteur dit "qui".
Les proprietes disent "quoi changer".

## Commentaire CSS

```css
/* Ceci est une note pour toi */
```

## Premier test

1. Cree `style.css` a cote de `index.html`
2. Relie-les avec `<link>`
3. Mets tous les `p` en bleu
4. Rafraichis

Si c'est bleu, CSS est branche. Nice.
