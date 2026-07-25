# Chapitre 14 - Atelier Grid : blog en zones

Atelier pratique. Objectif : construire le squelette d'un petit blog en Grid avec `grid-template-areas`, puis l'adapter en une colonne sur petit ecran. Pas de framework. HTML + CSS. Tu peux reutiliser des couleurs via des variables. Chez DanielCraft, on aime les ateliers qui laissent une page sous la main, pas seulement une theorie correctement recopiee.

Lea fait ce genre de squelette avant chaque refonte blog client : zones d'abord, deco ensuite. Max n'a pas de blog, mais il comprend l'idee quand on lui montre "entete / contenu / aside / pied" comme les pieces d'un atelier. Sam donne exactement ce brief a ses eleves : un plan lisible avant le pixel perfect.

## Ce que ce n'est pas

Ce n'est pas un concours de CSS creatif. Ce n'est pas non plus "copier un layout GitHub sans comprendre les noms de zones". Et ce n'est pas l'endroit pour `position: absolute` sur le plan general. Si tu triches avec du positionnement absolu pour "faire tenir" le blog, tu rates l'atelier meme si ca a l'air joli une minute.

## Brief

La page contient un en-tete (titre du blog + menu), un contenu principal avec deux articles, une colonne "A lire aussi" avec trois liens, un pied. Sur grand ecran : contenu et aside cote a cote, entete et pied pleine largeur. Sur petit ecran : tout s'empile dans un ordre lisible - en-tete, contenu, aside, pied. Theme libre : "Notes de voyage", "Cuisine du dimanche", "Journal d'atelier"...

Tu dessines d'abord le plan sur papier en deux cases (large / etroit). Ensuite seulement tu codes. Le papier evite la panique devant `grid-template-areas`.

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

Adapte si tu ajoutes une colonne menu. L'important : le dessin reste coherent (meme nombre de cellules par ligne). Une faute de typo dans un nom de zone et toute la grille "glisse" : l'outline temporaire (chapitre debug) t'aidera.

:::astuce
Colorie temporairement chaque area (fond different) pour voir qui est ou. Enleve apres. C'est le meilleur projecteur quand tu bloques.
:::

## Contenu minimum et criteres

Chaque article : un `h2`, un paragraphe, un lien "Lire la suite". L'aside : un titre et une liste de liens. Pas besoin de vrais articles longs. Un `h1` dans l'entete ou au debut du `main` (un seul).

Criteres de reussite : les zones sont au bon endroit ; le HTML se lit sans CSS dans la tete (ordre logique) ; sur mobile, rien ne debord ; tu n'as pas triche avec des `absolute` pour le plan general ; les variables pilotent au moins fond et gap.

## Petite histoire

Sam a vu un eleve mettre l'aside avant le `main` dans le HTML "pour aider le CSS desktop". Sur mobile, au Tab, l'aside arrivait avant les articles. Le correctif : ordre de lecture contenu puis aside, et laisser Grid placer. Lea a eu le meme reflexe sur un projet client. Max, en voyant la demo, a dit : "c'est comme ranger l'atelier pour que le client trouve le devis avant les factures fournisseurs". Exactement.

:::attention
Oublier de redefinir `grid-template-areas` dans le media query te laisse avec deux colonnes ecrasees sur telephone. Chaque breakpoint a son dessin.
:::

## Erreur classique

Copier un layout Grid trouve sur le web sans comprendre les noms de zones. Typo dans un nom de zone. Ordre HTML qui place l'aside avant le contenu "pour aider le CSS".

## En vrai

Chronometre 90 minutes. Premiere heure : HTML + grille qui tient. Demi-heure : style leger et test mobile. Si au bout d'une heure le plan tient sans deco, tu as deja gagne l'essentiel. La deco vient apres, jamais avant le plan.

## Bonus

Une carte "article epingle" avec `grid-column: 1 / -1` au-dessus des deux articles dans le `main` (petite grille interne). Ou un header en Flex (titre / nav). Optionnel. Ne saute pas dessus tant que le squelette n'est pas valide.

## A toi

Livre la page. Change le texte des articles. Si le layout tient en large et en etroit, l'atelier est valide. Montre-la a quelqu'un : demande ou est "le menu" et "l'article" en trois secondes. Note la reponse. Si la personne hesite, ton plan n'est pas encore assez clair - et c'est utile a savoir.

:::retenir
`grid-template-areas` = plan en mots. Meme nombre de cellules par ligne. Contenu avant aside dans le HTML. Une colonne sur mobile.
:::
