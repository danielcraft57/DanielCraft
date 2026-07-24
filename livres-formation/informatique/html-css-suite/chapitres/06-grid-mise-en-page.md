# Chapitre 6 - Mise en page avec Grid : header, contenu, aside

Les bases de Grid, tu les as. Maintenant on pose une vraie page : en-tete, contenu, colonne laterale, pied. C'est le squelette d'un blog, d'une doc simple, d'une page "ressources" avec menu.

L'outil star ici : `grid-template-areas`. Tu dessines la page avec des mots. Ensuite chaque zone recoit son nom. C'est lisible. C'est modifiable. C'est parfait pour un PDF de formation comme chez DanielCraft : tu vois le plan avant le detail.

## Le dessin de zones

```css
.layout {
  display: grid;
  grid-template-columns: 2fr 1fr;
  grid-template-areas:
    "entete entete"
    "contenu aside"
    "pied pied";
  gap: 1.5rem;
  max-width: 1100px;
  margin-inline: auto;
  padding: 1rem;
}
```

Chaque ligne du dessin a le meme nombre de cellules. Ici : deux colonnes. L'entete prend les deux. Le contenu et l'aside se partagent la rangee du milieu. Le pied prend les deux.

## Brancher le HTML

```html
<div class="layout">
  <header class="entete">...</header>
  <main class="contenu">...</main>
  <aside class="aside">...</aside>
  <footer class="pied">...</footer>
</div>
```

```css
.entete { grid-area: entete; }
.contenu { grid-area: contenu; }
.aside { grid-area: aside; }
.pied { grid-area: pied; }
```

Le nom dans `grid-area` doit matcher le mot du dessin. Si tu ecris `grid-area: header` mais que le dessin dit `entete`, ca ne se place pas.

## Variante avec menu lateral

Sur grand ecran, un blog peut aussi avoir :

```css
.layout {
  grid-template-columns: 180px 1fr 240px;
  grid-template-areas:
    "entete entete entete"
    "nav contenu aside"
    "pied pied pied";
}
```

Trois colonnes. Le `nav` a gauche, le contenu au centre, l'aside a droite. Sur une landing marketing, tu n'as peut-etre pas besoin d'aside : simplifie.

## Empiler sur petit ecran

```css
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

Une colonne. Ordre lisible : en-tete, contenu d'abord (priorite), puis aside, puis pied. Si tu as un `nav` separe, decide s'il passe juste sous l'entete ou apres le contenu. Pour un blog, menu haut puis articles reste naturel.

## Contenu dans les zones

Dans `main.contenu`, tu peux encore avoir une grille interne pour les articles :

```css
.liste-articles {
  display: grid;
  gap: 1rem;
}
```

Ou deux colonnes d'articles sur tablette. Grid imbriquee : normale et saine. La page a un Grid de structure ; une section a un Grid de cartes.

Dans l'aside : titre + liste de liens. Pas besoin d'en faire une usine.

## Header interne en Flex

Souvent, le `header` en zone Grid utilise Flexbox a l'interieur : logo a gauche, liens a droite.

```css
.entete {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}
```

Tu vois la complementarite : Grid pose les pieces de la page, Flex range le contenu d'une piece.

## Zones nommees et debug

Si tu te perds, colore temporairement :

```css
.entete { background: #e8f5ef; }
.contenu { background: #fff8e8; }
.aside { background: #eef0ff; }
.pied { background: #f3f3f3; }
```

Tu vois immediatement qui est ou. Enleve les fonds apres.

## Erreur classique

Des lignes du dessin avec un nombre de cellules different (`"entete entete"` puis `"contenu"` seul alors que tu as deux colonnes). Le navigateur rale ou se comporte bizarrement. Compte les mots.

Autre piege : oublier `grid-area` sur un enfant. Il se place quand meme "dans le flux" de la grille et peut casser le dessin prevu.

Oublier le responsive : un aside etroit en pixels fixes a cote d'un contenu sur telephone, ca etouffe. Repasse en une colonne.

## En vrai

Construis le squelette d'un blog : deux articles dans le `main`, trois liens dans l'`aside`, un vrai `header`/`footer`. Areas sur desktop, pile sur mobile. Redimensionne lentement. Note a quelle largeur ca devient serre - c'est ton breakpoint.

Compare avec une ancienne page ou tu avais tout fait en Flex + largeurs en %. Le dessin areas se lit souvent plus clairement.

## A toi

Livre une page "Blog atelier" complete (HTML + CSS). Layout areas comme ci-dessus. Variables pour gap et couleurs. Sur `max-width: 700px`, une colonne. Critere : sans CSS, le HTML reste dans un ordre logique (entete, articles, aside, pied).
