# Chapitre 6 - Listes et tableaux

Des listes partout. Courses, etapes, menus...
Des tableaux quand tu compares des infos.

## Liste a puces

```html
<ul>
  <li>Pain</li>
  <li>Lait</li>
  <li>Beurre</li>
</ul>
```

`ul` = unordered list (liste sans ordre strict).
`li` = list item (un element).

## Liste numerotee

```html
<ol>
  <li>Ouvrir l'editeur</li>
  <li>Ecrire le HTML</li>
  <li>Sauvegarder</li>
  <li>Ouvrir dans le navigateur</li>
</ol>
```

`ol` = ordered list. Utile pour des etapes.

## Liste dans une liste

```html
<ul>
  <li>Fruits
    <ul>
      <li>Pommes</li>
      <li>Bananes</li>
    </ul>
  </li>
  <li>Legumes</li>
</ul>
```

Ca marche. Mais n'en abuse pas, sinon ca devient illisible.

## Les tableaux

```html
<table>
  <thead>
    <tr>
      <th>Langage</th>
      <th>Role</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>HTML</td>
      <td>Structure</td>
    </tr>
    <tr>
      <td>CSS</td>
      <td>Style</td>
    </tr>
  </tbody>
</table>
```

- `table` = le tableau
- `tr` = une ligne
- `th` = cellule d'en-tete
- `td` = cellule normale

## Quand utiliser un tableau ?

Quand les donnees sont vraiment en lignes et colonnes.
Pas pour "faire un layout" de page. Ca, c'est le job du CSS.

## A toi

Fais une liste de 5 choses que tu veux apprendre.
Puis un petit tableau : jour / activite (ex. Lundi / HTML).
