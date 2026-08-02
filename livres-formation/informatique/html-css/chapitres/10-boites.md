# Chapitre 10 - Les boites (margin, padding, border)

En CSS, presque tout est une **boite**. Un paragraphe est une boite. Une image est une boite. Un bouton est une boite. Comprendre le modele en boite, c'est arreter de se battre contre "l'espace bizarre". Chez DanielCraft, c'est souvent le chapitre ou les debutants passent de "je bricole" a "je controle". Lea change padding quand le texte colle au bord. Max change margin quand deux blocs se touchent trop. Sam fait dessiner le modele sur papier avant le CSS.

De l'exterieur vers l'interieur : **margin** (espace autour, hors de la boite), **border** (la bordure), **padding** (air dans la boite, entre bord et contenu), puis le contenu. Tu te tromperas entre margin et padding. Tout le monde se trompe. Tu corrigeras. En 2026, quand quelqu'un dit "je maitrise un peu le CSS", il parle souvent de ca. Derriere, il y a Grid et des layouts complexes. Pour toi, le geste reste : padding dedans, margin dehors, inspecter. Tu restes le pilote. La boite obeit.

:::retenir
Padding = air dedans. Margin = air dehors. `border-box` des le depart. Inspecte avec F12.
:::

## Ce que ce n'est pas

Ce n'est pas "mettre des `<br>` pour faire de l'air". Ce n'est pas non plus ignorer `box-sizing` et subir des largeurs mysterieuses. Ce n'est pas croire que margin et padding sont synonymes. Et ce n'est pas encore Flexbox : la on parle d'une boite seule et de son enveloppe.

Ce n'est pas non plus "je mets de la margin partout jusqu'a ce que ca marche". C'est tentant. Ca devient vite un puzzle. Une propriete, un test, un regard. Lea dit : "si tu ajoutes la cinquieme margin sans comprendre, arrete-toi et inspecte". Sam chronometre le debug boite : sous cinq minutes avec F12.

Une photo encadree. Le padding, c'est le passe-partout blanc entre photo et cadre. La border, c'est le cadre. La margin, c'est l'espace jusqu'a la photo voisine sur le mur. Si tu elargis le passe-partout, la photo respire dans son cadre. Si tu elargis l'espace mur, tu eloignes les cadres entre eux. Max retient : "padding dedans, margin dehors". Simple. Durable. Lea projette le schema colore des outils developpeur : margin orange, border jaune, padding vert. Les clients comprennent d'un coup.

```css
.carte {
  background: white;
  border: 2px solid #333;
  padding: 20px;
  margin: 16px;
  border-radius: 12px;
}
```

:::astuce
Texte colle au bord -> augmente le padding. Deux cartes trop proches -> augmente la margin (ou utilise `gap` en Flexbox).
:::

## Largeur, hauteur, box-sizing

```css
.boite {
  width: 300px;
  max-width: 100%;
  height: auto;
}

* {
  box-sizing: border-box;
}
```

`max-width: 100%` evite les debordements telephone. Sans `border-box`, padding + border peuvent agrandir la boite de facon contre-intuitive. Avec **`border-box`**, `width` inclut padding et border. Plus clair. Mets ca presque toujours en haut de ton CSS. Lea le met en ligne 1. Max a arrete les scrolls horizontaux honteux le jour ou il l'a compris. Chez DanielCraft, c'est un reflexe moderne, pas une option.

:::astuce
Ajoute `* { box-sizing: border-box; }` en haut de ton CSS. Reflexe moderne, moins de surprises.
:::

## Display : block ou inline

`block` prend toute la largeur (`p`, `div`, `h1`). `inline` reste dans le flux du texte (`span`, `a` sans style). `inline-block` mixe : dans la ligne, mais padding propre possible.

```css
span.badge {
  display: inline-block;
  padding: 4px 8px;
  background: #eee;
}
```

Utile pour des etiquettes, des badges, des petits boutons texte. Sam les utilise pour marquer "nouveau" ou "gratuit" dans les exercices. Lea pour des tags clients. Max pour "urgence" sur un devis en ligne. Trois usages, une meme boite inline-block.

## Petite histoire

Lea avait une "carte produit" ou le texte collait a la bordure. Elle ajoutait des margins partout. Pire. Un collegue a dit : padding. Une ligne. Sourire. Max mettait `width: 400px` sans `max-width`, et sur telephone ca debordait avec un scroll horizontal honteux. `max-width: 100%` l'a sauve. Sam fait colorier le modele en boite dans les outils developpeur : margin orange, border jaune, padding vert. Les eleves voient enfin. Trois scenes, un cran : tu controles l'espace au lieu de le subir.

## Erreur classique

Utiliser margin quand tu veux padding (ou l'inverse) dix fois de suite sans tester. Oublier `box-sizing`. Mettre des largeurs fixes partout. Empiler des margins qui "collapsent" de facon surprenante entre deux blocs. Quand c'est flou : inspecte (F12) et regarde la boite coloree. Ne devine pas : regarde. Autre piege : des `<br>` pour "faire de l'air". Prefere padding et margin. Lea raye les br de decoration sur les audits.

## En vrai

Cree une classe `.carte` avec fond, padding, bordure, coins ronds. Applique-la a une `div` avec titre + paragraphe. Enleve le padding. Remets. Remplace par de la margin. Sens la difference. Reduis la fenetre du navigateur : si rien ne debord, tu progresses. Ouvre F12 et regarde la boite coloree. Tu vois enfin ce que tu manipules.

## A toi

Ajoute `* { box-sizing: border-box; }`, une carte a `width: 300px; max-width: 100%;`, et un badge `inline-block`. Reduis la fenetre. Si rien ne debord, tu as gagne un reflexe web moderne. Note-le pour le mini-projet DanielCraft : boites maitrisees, page credible sur telephone. Tu prepares Flexbox avec un sol solide.
