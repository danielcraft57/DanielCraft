# Chapitre 4 - Variables CSS : une couleur, un endroit

Tu as deja change une couleur primaire dans dix classes differentes. Tu as oublie la onzieme. La page a l'air batarde. Ca arrive a tout le monde.

Les variables CSS (custom properties) resolvent ca. Tu declares une valeur une fois, souvent dans `:root`, puis tu la reutilises partout avec `var(...)`.

`:root`, c'est la racine du document. En pratique : "mes reglages globaux pour toute la page".

Chez DanielCraft, une palette claire, c'est une marque qui tient. Variables = palette centralisee.

## Declarer et utiliser

```css
:root {
  --couleur-principale: #1a5f4a;
  --couleur-fond: #f7f5f0;
  --couleur-texte: #222;
  --espace: 1rem;
}

body {
  background: var(--couleur-fond);
  color: var(--couleur-texte);
}

a {
  color: var(--couleur-principale);
}

.bouton {
  background: var(--couleur-principale);
  color: #fff;
  padding: var(--espace) calc(var(--espace) * 1.5);
}
```

Le double tiret `--` marque le nom de la variable. Tu choisis des noms clairs : `--couleur-principale` plutot que `--c1`.

## Pourquoi c'est genial sur une landing

Imagine une landing avec bouton, liens, bordures d'accent, titre surligne. Si demain tu passes du vert au bleu marine, tu changes une ligne dans `:root`. Toute la page suit. C'est ca, une vraie palette.

Tu peux aussi stocker des tailles, des rayons, des ombres legeres :

```css
:root {
  --rayon: 8px;
  --ombre: 0 4px 12px rgba(0, 0, 0, 0.08);
  --largeur-max: 1100px;
}

.carte {
  border-radius: var(--rayon);
  box-shadow: var(--ombre);
}

.wrap {
  max-width: var(--largeur-max);
  margin-inline: auto;
}
```

Sur un blog, le meme `--espace` rythme le padding des articles et le gap de la grille. Moins de magie, plus de coherence.

## Valeur de secours

`var(--couleur-principale, #1a5f4a)` utilise la variable si elle existe, sinon le second argument. Utile quand tu experimentes ou quand une variable pourrait manquer.

```css
.badge {
  background: var(--couleur-accent, #c45c26);
}
```

## Changer localement

Une variable n'est pas obligatoirement globale. Tu peux la redefinir dans un bloc :

```css
.carte-promo {
  --couleur-principale: #8b1e3f;
}

.carte-promo .bouton {
  background: var(--couleur-principale);
}
```

La carte promo a son accent. Le reste du site garde le vert. Les enfants de `.carte-promo` voient la nouvelle valeur. C'est puissant pour des themes de section sans dupliquer tout le CSS.

## Noms qui aident

Mieux vaut `--couleur-principale` et `--couleur-fond` que `--vert` et `--beige` si tu comptes changer de teinte. Les noms de role (principale, fond, texte, bordure) survivent aux restyles. Les noms de teinte se periment.

Pour une boutique : `--prix`, `--dispo`, `--rupture` peuvent aussi etre des variables de couleur semantiques.

## Variables et formulaires

```css
:root {
  --champ-bordure: #ccc;
  --champ-focus: #1a5f4a;
}

input {
  border: 1px solid var(--champ-bordure);
}

input:focus {
  border-color: var(--champ-focus);
  outline-color: var(--champ-focus);
}
```

Tu prepares deja le terrain pour le chapitre formulaires et pour le dark mode plus tard.

## Erreur classique

Declarer vingt variables "au cas ou" sans les utiliser. Ou copier la meme valeur en dur dans une classe "parce que c'est plus rapide" - tu reviens au probleme initial.

Autre piege : oublier que le nom est sensible a la casse et aux tirets. `--Couleur` n'est pas `--couleur`.

## En vrai

Ouvre une page existante. Liste les couleurs qui reviennent (boutons, liens, titres). Cree un `:root` avec trois a six variables. Remplace les valeurs en dur. Change une variable. Souris si toute la page suit.

Fais la meme chose pour `--espace` sur une grille de cartes produit : padding de carte et `gap` du parent.

## A toi

Cree une mini landing : titre, paragraphe, bouton, une carte. Tout le theme passe par `:root` (`--couleur-principale`, `--fond`, `--texte`, `--rayon`, `--espace`). Change uniquement `:root` pour obtenir une variante "soir" (fond plus sombre, texte clair). Ne touche pas aux classes. Si ca marche, tu as compris les variables.
