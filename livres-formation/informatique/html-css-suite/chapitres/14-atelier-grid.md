# Chapitre 14 - Atelier Grid : blog en zones

Atelier pratique. Objectif : construire le squelette d'un petit blog en Grid avec `grid-template-areas`, puis l'adapter en une colonne sur petit ecran.

Pas de framework. HTML + CSS. Tu peux reutiliser des couleurs via des variables.

## Brief

La page contient un en-tete (titre du blog + menu), un contenu principal avec deux articles, une colonne "A lire aussi" avec trois liens, un pied. Sur grand ecran : contenu et aside cote a cote, entete et pied pleine largeur. Sur petit ecran : tout s'empile dans un ordre lisible (en-tete, contenu, aside, pied).

Theme libre : "Notes de voyage", "Cuisine du dimanche", "Journal d'atelier"...

## Etapes

1. Ecris le HTML semantique : `header`, `nav`, `main` avec deux `article`, `aside`, `footer`.
2. Cree un conteneur `.layout` en `display: grid`.
3. Dessine les areas sur grand ecran (entete pleine largeur, contenu + aside, pied pleine largeur).
4. Relie chaque piece avec `grid-area`.
5. Ajoute `gap` et une largeur max centree (`max-width` + `margin-inline: auto`).
6. Declare un `:root` minimal (couleurs, gap).
7. Sous `max-width: 700px` (ou similaire), repasse en une colonne et redefinis `grid-template-areas` pour empiler.
8. Style leger des articles (fond carte, rayon) sans casser le plan.

## Amorce CSS

```css
:root {
  --couleur-principale: #1a5f4a;
  --fond: #f7f5f0;
  --carte: #fff;
  --gap: 1.5rem;
}

.layout {
  display: grid;
  grid-template-columns: 2fr 1fr;
  grid-template-areas:
    "entete entete"
    "contenu aside"
    "pied pied";
  gap: var(--gap);
  max-width: 1000px;
  margin-inline: auto;
  padding: 1rem;
}

.entete { grid-area: entete; }
.contenu { grid-area: contenu; }
.aside { grid-area: aside; }
.pied { grid-area: pied; }

@media (max-width: 700px) {
  .layout {
    grid-template-columns: 1fr;
    grid-template-areas:
      "entete"
      "contenu"
      "aside"
      "pied";
  }
}
```

Adapte si tu ajoutes une colonne menu. L'important : le dessin reste coherent (meme nombre de cellules par ligne).

## Contenu minimum

Chaque article : un `h2`, un paragraphe, un lien "Lire la suite". L'aside : un titre et une liste de liens. Pas besoin de vrais articles longs. Un `h1` dans l'entete ou au debut du `main` (un seul).

## Criteres de reussite

Les zones sont au bon endroit. Le HTML se lit sans CSS dans la tete (ordre logique). Sur mobile, rien ne debord. Tu n'as pas triche avec des `absolute` pour le plan general. Les variables pilotent au moins fond et gap.

## Piege a eviter

Copier un layout Grid trouve sur le web sans comprendre les noms de zones. Si tu bloques, colorie temporairement chaque area (fond different) pour voir qui est ou.

Autre piege : mettre l'aside avant le `main` dans le HTML pour "aider" le CSS desktop, puis se retrouver avec l'aside avant les articles au Tab sur mobile. Preferer l'ordre de lecture : contenu puis aside, et laisser Grid placer.

## Bonus

Une carte "article epingle" avec `grid-column: 1 / -1` au-dessus des deux articles dans le `main` (petite grille interne). Ou un header en Flex (titre / nav).

## A toi

Livre la page. Change le texte des articles. Si le layout tient en large et en etroit, l'atelier est valide. Montre-la a quelqu'un : demande ou est "le menu" et "l'article" en trois secondes.
