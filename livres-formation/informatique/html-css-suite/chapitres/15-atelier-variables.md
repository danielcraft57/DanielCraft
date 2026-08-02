# Chapitre 15 - Atelier variables : une marque en `:root`

Atelier pratique. Objectif : themater une petite page produit uniquement via des variables CSS. Tu dois pouvoir changer toute l'ambiance en touchant `:root`, sans chasser des couleurs en dur dans cinquante classes. Chez DanielCraft, c'est le geste qui separe "page bricolee" et "page de marque".

Lea refuse desormais de livrer une carte produit sans variables : un client qui change d'avis sur le vert ne doit pas couter une soiree de chercher-remplacer. Max comprend l'idee quand on lui dit "une peinture pour tout l'atelier, pas un pot par mur". Sam fait basculer le theme en cours devant la classe : les eleves voient le pouvoir du `:root` en une seconde.

## Ce que ce n'est pas

Ce n'est pas encore le dark mode systeme du chapitre 17 (meme si tu t'en approches). Ce n'est pas non plus "mettre deux variables et garder le reste en hex". Et ce n'est pas un concours de gradients. Une palette simple, lisible, coherente. Si tu triches avec un `#1a5f4a` "temporaire" dans `.bouton`, le temporaire reste - et l'atelier rate son but.

## Brief

Page "Carte produit" : nom de boutique, une carte (titre produit, court texte, prix, bouton), trois pastilles d'info en dessous (livraison, retour, origine). Tu livres deux palettes : une claire, une "soir" (plus sombre). La bascule peut etre manuelle : tu commentes / decommentes un bloc `:root`, ou - mieux - tu ajoutes une classe sur `body`. Quand tu bascules, tout suit. Si quelque chose reste fige, c'est qu'un hex trainee encore dans une classe.

## Etapes

1. Pose le HTML semantique minimal (`header`, `main`, `article`, `footer`).
2. Cree un `:root` avec au moins : `--couleur-principale`, `--fond`, `--texte`, `--carte`, `--rayon`, `--espace`, `--ombre`.
3. Branche body, carte, liens, bouton, pastilles sur `var(...)`.
4. Zero couleur hex "en dur" hors de `:root` (sauf eventuel blanc/noir declares aussi en variables).
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

Pour tester le theme soir : `<body class="theme-soir">`. Au chapitre dark mode, tu brancheras une version plus "systeme". Ici, l'important est la discipline des variables.

:::retenir
Tout le theme passe par des variables. Changer `:root` (ou une classe sur `body`) change fond, texte, carte, bouton. Zero hex fugitif dans les classes.
:::

## Pastilles et criteres

Une petite grille `repeat(3, 1fr)` sur desktop, une colonne sur mobile. Chaque pastille utilise `--carte` et une bordure simple en `var(--couleur-principale)`.

```css
.infos {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: var(--espace);
}
```

Criteres de reussite : changer uniquement les variables change fond, texte, carte, bouton ; les deux themes restent lisibles (contraste) ; pas de chasse au hex dans les classes de composants ; le HTML reste simple et semantique.

## Petite histoire

Lea a livre une page avec theme clair uniquement. Le client a demande "version nuit pour Instagram Stories". Elle a ajoute `body.theme-soir` en vingt minutes parce que tout etait deja en variables. La fois d'avant, sans variables, ca avait pris trois heures et casse deux contrastes. Max a vu la demo et a demande la meme chose pour sa page devis - "le soir, mes clients lisent sur le canape". Sam a note le cas pour le cours suivant.

:::attention
Theme sombre avec texte `#666` sur fond `#14221c` : illisible. Monte le contraste. Un theme "joli" mais illisible n'est pas un theme : c'est une deco dangereuse. Et le `#1a5f4a` "temporaire" dans `.bouton` reste presque toujours.
:::

## Erreur classique

Garder des hex en dur hors de `:root`. Contrastes insuffisants en theme soir. Croire que deux variables suffisent pendant que le reste du CSS reste en dur.

## En vrai

Fais la chasse aux hex : cherche `#` dans ton CSS. Tout ce qui n'est pas dans `:root` ou `body.theme-soir` est suspect. Corrige. Bascule dix fois de suite. Si un element clignote encore dans l'ancienne couleur, tu as trouve le fugitif.

## Bonus

Ajoute `--font-titre` et `--font-corps` en variables (noms de familles). Ou un `--accent` pour le prix uniquement. Utile, pas obligatoire.

## A toi

Livre la page + les deux themes. Fais une capture mentale (ou reelle) des deux versions. Si tu peux basculer en une classe, tu es pret pour le chapitre dark mode. Ecris en une phrase la couleur que tu as du eclaircir ou foncer pour le contraste - ce geste-la, c'est le metier.
