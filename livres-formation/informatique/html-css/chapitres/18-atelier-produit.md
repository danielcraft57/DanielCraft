# Chapitre 18 - Atelier : une mini page produit

On fait une page "produit" simple. Comme une fiche boutique en ligne, sans la boutique entiere derriere. Objectif concret : nom du produit, prix visible, courte description, liste d'avantages, bouton "Ajouter au panier" (meme s'il ne fait rien encore sans JavaScript), CSS mobile-friendly. Une fiche claire, pas une usine a gaz. Chez DanielCraft, cet atelier entraine la **hierarchie visuelle** et la retenue : savoir ce qui compte en premier pour le lecteur presse.

Lea livre des fiches produit pour des artisans et des petites marques. Elle sait qu'un prix cache en petit gris, personne ne le voit. Max a fait la sienne pour un kit d'entretien : nom, prix, trois avantages, bouton d'appel. Sam utilise l'exercice pour parler clarte, pas "design circus". En 2026, quand quelqu'un dit "j'ai une fiche produit", il parle souvent de cette hierarchie. Tu restes le pilote. L'oeil suit ton ordre.

:::retenir
Le regard tombe sur le nom, puis le prix, puis pourquoi c'est bien, puis l'action. Respecte cet ordre.
:::

## Ce que ce n'est pas

Ce n'est pas une vraie boutique avec panier, paiement et stock. Ce n'est pas quinze polices et six popups qui crient "PROMO". Ce n'est pas une image de stock illegible sans **`alt`**. Un seul objectif : que quelqu'un comprenne le produit en quelques secondes, sans zoomer, sans deviner. Lea dit : "si tu dois expliquer ou est le prix, tu as rate".

Une etiquette de magasin bien faite. Le regard tombe d'abord sur le nom, puis sur le **prix**, puis sur pourquoi c'est bien, puis sur l'action. Si tu inverses (blabla d'abord, prix perdu en bas), tu perds le lecteur presse. La hierarchie visuelle, c'est guider l'oeil, pas le noyer. Max compare a son etal de marche : "le prix se voit avant le roman". Sam chronometre : "trois secondes pour comprendre ?"

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

```css
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: Georgia, serif;
  background: #f6f3ee;
  color: #222;
}
.fiche {
  width: min(100% - 2rem, 420px);
  margin: 2rem auto;
  padding: 1.5rem;
  background: white;
  border-radius: 12px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.08);
}
.tag { color: #1f6f5b; font-weight: 700; margin: 0; }
.prix { font-size: 2rem; font-weight: 700; margin: 0.5rem 0; }
.btn {
  display: inline-block;
  margin-top: 1rem;
  padding: 0.8rem 1.2rem;
  background: #1f6f5b;
  color: white;
  text-decoration: none;
  border-radius: 8px;
}
@media (max-width: 480px) {
  .prix { font-size: 1.6rem; }
}
```

Adapte le produit. Change les couleurs. Mets une vraie image avec `alt` si tu veux. Garde la hierarchie.

## Criteres de reussite

Le nom et le prix se voient tout de suite. Les avantages sont en liste. Le bouton est assez grand sur telephone. La fiche tient a 360px sans scroll horizontal. Le viewport est present. Chez DanielCraft, ces criteres battent dix badges "promo".

## Petite histoire

Lea a herite d'une fiche ou le prix etait en bas, en gris, apres trois paragraphes marketing. Elle l'a remonte sous le titre. Les clics ont monte. Max a fait sa fiche kit d'entretien pour le marche : trois avantages, gros prix, bouton "Appeler". Les gens ont compris sans lui demander. Sam fait comparer deux versions en classe : prix visible vs prix cache. Vote unanime. Trois scenes, une lecon.

## Erreur classique

Prix trop petit. Bouton trop petit. Trop de texte avant l'essentiel. Image sans `alt`. Oublier le mobile. Autre piege : cinq polices et six couleurs "parce que ca fait boutique". Prefere une fiche calme et nette. Lea raye le bruit visuel sur les audits.

:::attention
Si le prix n'est pas lisible en trois secondes, remonte-le et grossis-le. Le reste peut attendre.
:::

## En vrai

Construis la fiche avec ton produit (reel ou invente). Montre-la a quelqu'un pendant cinq secondes. Demande : "c'est quoi, ca coute combien ?" Si la reponse est juste, tu as gagne. Sinon, corrige la hierarchie. Reteste. Cinq minutes actives valent mieux qu'une heure de peaufinage flou.

## A toi

Fais ta fiche produit maintenant. Bonus : ajoute une image avec `figure`/`figcaption`, et un second bouton "En savoir plus" vers une ancre. Ecris trois lignes sur ce que tu as choisi de mettre en premier et pourquoi. Posture DanielCraft : hierarchie consciente, pas deco au hasard.
