# Chapitre 18 - Atelier : une mini page produit

On fait une page "produit" simple.
Comme une fiche boutique, sans boutique.

## Objectif

Une page avec le nom du produit, le prix, une courte description, une liste d'avantages, et un bouton "Ajouter" (meme s'il ne fait rien encore). Le tout avec un joli CSS mobile-friendly. Une fiche claire, pas une usine a gaz.

## HTML de base

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Casque SoftBeat</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <main class="fiche">
    <p class="tag">Nouveau</p>
    <h1>Casque SoftBeat</h1>
    <p class="prix">79 €</p>
    <p>Un casque confortable pour la maison, les cours, et les trains un peu longs.</p>
    <h2>Pourquoi il est cool</h2>
    <ul>
      <li>Leger</li>
      <li>Bonne autonomie</li>
      <li>Son clair</li>
    </ul>
    <a class="btn" href="#">Ajouter au panier</a>
  </main>
</body>
</html>
```

## CSS de base

```css
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: Georgia, serif;
  background: #f3f6f4;
  color: #14221c;
}
.fiche {
  width: min(100% - 2rem, 560px);
  margin: 2rem auto;
  background: white;
  padding: 1.5rem;
  border-radius: 14px;
  border: 1px solid #c5d4cc;
}
.tag {
  display: inline-block;
  background: #fff4d6;
  padding: 0.2rem 0.55rem;
  border-radius: 999px;
  font-size: 0.85rem;
}
.prix {
  font-size: 1.8rem;
  color: #1a4d3e;
  font-weight: bold;
}
.btn {
  display: inline-block;
  margin-top: 1rem;
  background: #1a4d3e;
  color: white;
  text-decoration: none;
  padding: 0.7rem 1rem;
  border-radius: 10px;
}
@media (max-width: 600px) {
  .fiche { margin: 1rem; }
}
```

## Variantes a tester

1. Change le produit (livre, plante, jeu)
2. Ajoute une image
3. Passe le bouton en pleine largeur sur mobile
4. Ajoute une section "Avis"

## Criteres de qualite

La page doit etre lisible sans zoomer sur telephone. La hierarchie reste claire : titre, puis prix, puis texte. Pas quinze polices differentes. Et un seul objectif : comprendre le produit.

## Bonus

Ajoute un faux tableau de tailles / couleurs.
Garde-le simple. Une page propre bat une page surchargee.
