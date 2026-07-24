# Chapitre 15 - Atelier variables : une marque en `:root`

Atelier pratique. Objectif : themater une petite page produit uniquement via des variables CSS. Tu dois pouvoir changer toute l'ambiance en touchant `:root`, sans chasser des couleurs en dur dans cinquante classes.

## Brief

Page "Carte produit" : nom de boutique, une carte (titre produit, court texte, prix, bouton), trois pastilles d'info en dessous (livraison, retour, origine). Tu livres deux palettes : une claire, une "soir" (plus sombre). La bascule peut etre manuelle : tu commentes/decommentes un bloc `:root`, ou tu ajoutes une classe sur `body` (encore mieux).

## Etapes

1. Pose le HTML semantique minimal (`header`, `main`, `article`, `footer`).
2. Cree un `:root` avec au moins : `--couleur-principale`, `--fond`, `--texte`, `--carte`, `--rayon`, `--espace`, `--ombre`.
3. Branche body, carte, liens, bouton, pastilles sur `var(...)`.
4. Zero couleur hex "en dur" hors de `:root` (sauf eventuel blanc/noir de texte sur bouton si tu les declares aussi en variables).
5. Cree une seconde palette.
6. Fais basculer via `body.theme-soir` (recommande) ou en echangeant le bloc `:root`.
7. Verifie les contrastes dans les deux themes.
8. Ajoute une transition legere sur le bouton (toujours via variables pour la couleur).

## Amorce palette + bascule

```css
:root {
  --couleur-principale: #1a5f4a;
  --fond: #f7f5f0;
  --texte: #1b1b1b;
  --carte: #ffffff;
  --rayon: 10px;
  --espace: 1rem;
  --ombre: 0 4px 14px rgba(0, 0, 0, 0.08);
}

body.theme-soir {
  --couleur-principale: #5dcaa5;
  --fond: #14221c;
  --texte: #eef5f1;
  --carte: #1c3229;
  --ombre: 0 4px 14px rgba(0, 0, 0, 0.4);
}

body {
  background: var(--fond);
  color: var(--texte);
}

.carte {
  background: var(--carte);
  border-radius: var(--rayon);
  padding: calc(var(--espace) * 1.25);
  box-shadow: var(--ombre);
}

.bouton {
  background: var(--couleur-principale);
  color: var(--fond);
  border: 0;
  border-radius: var(--rayon);
  padding: 0.7rem 1.1rem;
  transition: filter 200ms ease;
}
```

Pour tester le theme soir : `<body class="theme-soir">`. Tu verras au chapitre dark mode une version plus "systeme". Ici, l'important est la discipline des variables.

## Pastilles

Une petite grille `repeat(3, 1fr)` sur desktop, une colonne sur mobile. Chaque pastille utilise `--carte` et une bordure `color-mix` ou une bordure simple en `var(--couleur-principale)`.

```css
.infos {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: var(--espace);
}
```

## Criteres de reussite

Changer uniquement les variables change fond, texte, carte, bouton.

Les deux themes restent lisibles (contraste).

Pas de chasse au hex dans les classes de composants.

Le HTML reste simple et semantique.

## Piege a eviter

Garder `#1a5f4a` dans `.bouton` "temporairement". Le temporaire reste. Autre piege : theme sombre avec texte `#666` sur fond `#14221c` (illisible). Monte le contraste.

## Bonus

Ajoute `--font-titre` et `--font-corps` en variables (noms de familles). Ou un `--accent` pour le prix uniquement.

## A toi

Livre la page + les deux themes. Fais une capture mentale (ou reelle) des deux versions. Si tu peux basculer en une classe, tu es pret pour le chapitre dark mode.
