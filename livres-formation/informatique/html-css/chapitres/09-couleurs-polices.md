# Chapitre 9 - Couleurs, polices, tailles

Maintenant on rend ca vivant. Couleurs, polices, tailles : c'est souvent ce que les gens appellent "le design". En vrai, c'est surtout de la **lisibilite**. Un beau site illisible n'est pas beau longtemps. Chez DanielCraft, on commence doux : fond clair, texte sombre, titre qui ressort, paragraphes qui respirent. Lea garde une petite palette de trois couleurs max. Max a choisi un vert chantier et s'y tient. Sam interdit le jaune fluo sur blanc.

Tu peux ecrire une couleur par nom (`teal`, `navy`), en **hex** (`#ff6600`), ou en rgb. Hex est le plus courant sur le web. `#000000` est noir. `#ffffff` est blanc. Tu n'as pas a retenir les codes par coeur : un color picker suffit. En 2026, quand quelqu'un dit "j'ai choisi ma charte", il parle souvent de ca. Derriere, il y a des design systems. Pour toi, le geste reste : contraste, hierarchie, respiration. Tu restes le pilote. L'oeil suit.

:::retenir
Fond clair, texte sombre, titre qui ressort, line-height qui respire. Lisibilite avant spectacle.
:::

## Ce que ce n'est pas

Ce n'est pas quinze polices differentes. Ce n'est pas du texte gris clair sur blanc. Ce n'est pas "plus gros = mieux" sans hierarchie. Ce n'est pas non plus obligatoire d'importer Google Fonts le premier jour : des polices systeme bien choisies suffisent largement pour apprendre.

Ce n'est pas non plus "design = decoration". Tu choisis des couleurs pour guider l'oeil, pas pour impressionner ton neveu. Un accent sur le bouton contact. Un titre qui ressort. Le reste calme. Lea dit : "moins de couleurs, plus de clarte". Sam raye les palettes arc-en-ciel sur les copies.

Pense a une vitrine. La couleur du mur (fond), la couleur des etiquettes (texte), la taille des pancartes (titres vs paragraphes), l'espace entre les lignes (**line-height**). Si tout crie, personne n'entre. Si tout chuchote pareil, personne ne sait ou regarder. Tu crees un contraste utile, pas un spectacle. Max dit : "ma vitrine artisan, c'est fond clair, texte fonce, vert sur le bouton - point". Lea projette deux versions chez le client : contraste faible vs contraste. Le vote est rare.

```css
body {
  color: #222222;
  background: #f7f3ee;
}
h1 {
  color: teal;
}
```

## Polices

```css
body {
  font-family: Georgia, "Times New Roman", serif;
  font-size: 18px;
  line-height: 1.6;
}
```

`font-family` propose une police, puis des secours. `line-height: 1.6` fait respirer. Pour un look moderne sans empattement : `Arial, sans-serif`. Pour un ton un peu plus litteraire : `Georgia, serif`. Deux familles, ca suffit au debut. Lea n'importe des polices exotiques que quand le client insiste - et elle teste toujours la vitesse de chargement. Chez DanielCraft, une police lisible bat une police "originale" illisible.

## Graisse, style, taille, alignement

```css
h1 { font-weight: 700; font-size: 2.5rem; text-align: center; }
p  { font-size: 1rem; }
em { font-style: italic; }
```

`px` est simple. `rem` est relatif a la taille de base, plus souple pour l'accessibilite. Au debut, `px` est ok. Tu passeras a `rem` quand tu seras a l'aise. `text-align` accepte `left`, `right`, `center`, `justify`. Centrer tout un long article fatigue : reserve le center aux titres courts ou aux citations. Sam interdit le justify sur mobile en debut d'apprentissage : trop de trous bizarre.

## Petite histoire

Lea a livre une page "elegante" en gris `#bbbbbb` sur blanc. Sur le telephone du client en exterieur, illisible. Elle a fonce le texte, augmente le line-height, et la page est devenue "moins design" selon le client - puis il a recu plus de messages. Max a mis un titre a 60px sur mobile : ca cassait tout. Il a appris a tester petit ecran. Sam fait comparer deux versions en classe : contraste faible vs contraste. Vote unanime pour le texte fonce. Trois scenes, une lecon : lisibilite d'abord.

:::attention
Texte gris clair sur blanc = piege classique. Fonce. Augmente le line-height. Relis dehors si tu peux.
:::

## Erreur classique

Trop de couleurs. Police minuscule "parce que ca fait pro". Centrer tout le texte d'un long article. Oublier le line-height. Changer dix proprietes d'un coup et ne plus savoir ce qui a aide. Une modification, un regard. Autre piege : copier une palette trendy sans tester sur ton contenu reel. Ce qui marche sur un site de mode peut tuer une page artisan sobre. Lea teste toujours sur le vrai texte client, pas sur du "Lorem ipsum".

## En vrai

Choisis un fond doux, un texte sombre, un titre colore, des paragraphes a 16-18px minimum. Lis trois phrases a l'ecran. Si tu plisses les yeux, corrige. Puis change seulement la couleur d'accent et observe : parfois un seul changement suffit a rendre la page plus "toi". Reduis la fenetre. Relis. Le telephone revele beaucoup.

## A toi

Cree une mini palette ecrite : fond, texte, accent. Applique-la. Puis change seulement l'accent. Note quelle version tu garderais pour ta page perso. Le gout se travaille comme le code - progressivement. DanielCraft conseille de garder cette palette sur un post-it jusqu'au mini-projet : coherence avant fantaisie. Tu sauras ou tu vas.
