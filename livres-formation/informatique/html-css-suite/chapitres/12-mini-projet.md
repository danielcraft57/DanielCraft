# Chapitre 12 - Mini-projet : page d'accueil responsive (Grid + variables)

On assemble. Tu vas construire une petite page d'accueil : marque, menu, hero, grille de cartes, bandeau d'appel, formulaire court, pied. Responsive. Theme via variables. Layout via Grid. Pas de framework.

L'objectif n'est pas la perfection pixel. C'est une page coherente, lisible, utilisable au clavier, qui tient sur telephone et desktop. Le genre de base qu'on aimerait livrer pour un atelier, une boutique naive, ou une vitrine DanielCraft miniature.

## Brief

Sujet libre, mais concret. Exemples : "Atelier ceramique", "Cafe de quartier", "Coach sportif", "Librairie".

La page contient :

Un header avec nom + navigation (2-4 liens).

Un hero avec `h1`, une phrase, un bouton.

Une section "Nos pepites" (ou equivalent) : grille de 3 ou 4 cartes (titre, texte, lien).

Une section contact : petit formulaire (nom, email, message).

Un footer simple.

Sur grand ecran : hero confortable, grille multi-colonnes. Sur petit ecran : tout s'empile, boutons aisees a taper.

## Etape 1 - HTML semantique

Pose le squelette sans te battre avec le style.

```html
<body>
  <header class="site-header">...</header>
  <main>
    <section class="hero">...</section>
    <section class="section" id="cartes">...</section>
    <section class="section" id="contact">...</section>
  </main>
  <footer class="site-footer">...</footer>
</body>
```

Un `h1` dans le hero. Des `h2` de section. Cartes en `article`. Formulaire avec labels. Liens du menu qui pointent vers `#cartes` et `#contact` si tu veux du one-page.

## Etape 2 - Variables

```css
:root {
  --couleur-principale: #1a5f4a;
  --couleur-fond: #f7f5f0;
  --couleur-texte: #1b1b1b;
  --couleur-carte: #fff;
  --rayon: 10px;
  --espace: 1rem;
  --gap: 1.25rem;
  --largeur-max: 1100px;
  --ombre: 0 4px 14px rgba(0, 0, 0, 0.08);
}
```

Branche `body`, liens, boutons, cartes sur ces variables. Aucune couleur magique eparpillee si tu peux l'eviter.

## Etape 3 - Coquille et header

```css
body {
  margin: 0;
  font-family: Georgia, "Times New Roman", serif;
  background: var(--couleur-fond);
  color: var(--couleur-texte);
  line-height: 1.5;
}

.wrap {
  max-width: var(--largeur-max);
  margin-inline: auto;
  padding: var(--espace);
}

.site-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: var(--espace);
  flex-wrap: wrap;
}
```

Flex pour le header. Serif volontaire pour sortir des stacks par defaut, tout en restant simple. Tu peux choisir une autre police web si tu veux, tant que c'est lisible.

## Etape 4 - Hero

```css
.hero {
  display: grid;
  gap: var(--espace);
  padding: calc(var(--espace) * 2) 0;
}

.hero h1 {
  font-size: clamp(1.8rem, 4vw, 3rem);
  line-height: 1.15;
  margin: 0;
}
```

`clamp` donne une taille fluide entre min et max. Pas obligatoire, mais agreable. Un seul CTA principal dans le hero.

## Etape 5 - Grille de cartes

```css
.grille {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: var(--gap);
}

.carte {
  background: var(--couleur-carte);
  border-radius: var(--rayon);
  padding: var(--espace);
  box-shadow: var(--ombre);
}
```

Images optionnelles : si tu en mets, `max-width: 100%` + `object-fit: cover` + `aspect-ratio`.

## Etape 6 - Formulaire et footer

Reprend les patterns du chapitre 9. Formulaire en grid verticale, max-width raisonnable. Footer discret avec contraste correct.

## Etape 7 - Transitions legeres

Boutons et cartes : 200ms. `prefers-reduced-motion` en bas de fichier.

## Etape 8 - Accessibilite express

Tab complet. Focus visible. Labels. Contraste hero. `alt` si images.

## Criteres de reussite

La page se lit sans CSS (ordre logique).

Changer 2 variables change le theme de facon visible.

La grille passe d'une a plusieurs colonnes sans casser.

Pas de scroll horizontal sur mobile.

Focus visible sur liens, boutons, champs.

## Erreur classique

Tout faire en `position: absolute`. Copier un theme enormement complexe. Oublier le formulaire labels. Mettre cinq CTA aussi forts les uns que les autres dans le hero. Grille fixe `1fr 1fr 1fr` sans media query qui ecrase le telephone.

## En vrai

Chronometre-toi 90 minutes. Livrable imparfait > concept parfait non code. Ensuite tu peaufines 30 minutes : contrastes, gaps, textes.

Montre la page a quelqu'un. Demande : "C'est pour quoi, en cinq secondes ?" Si la reponse matche ton intention, le hero fait son job.

## A toi

Livre `index.html` + `styles.css`. Nom du projet dans le header. Trois cartes minimum. Un formulaire. Un theme 100 % variables. Bonus : une variante en commentant une autre palette dans `:root` (tu basculeras vraiment au chapitre dark mode).
