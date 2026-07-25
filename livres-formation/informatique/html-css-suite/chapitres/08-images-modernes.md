# Chapitre 8 - Images modernes : taille, cadrage, srcset

Une belle image mal geree casse une page. Elle debord. Elle ecrase le texte. Elle pese 4 Mo et fait attendre le telephone en 4G. Les bases, tu les as (`img`, `alt`). Ici, on range le comportement CSS et on touche a l'idee de `srcset`.

Chez DanielCraft, une image de produit nette et legere, c'est du respect pour le visiteur. Pas besoin d'etre ingenieur perf : quelques reflexes suffisent. Lea verifie le poids avant chaque livraison. Max a appris apres qu'un client a attendu sur 4G. Sam projette l'onglet Reseau : silence, puis "ah".

## Ne jamais deborder : max-width

```css
img {
  max-width: 100%;
  height: auto;
}
```

Regle d'or. L'image peut retrecir dans son conteneur. Elle garde ses proportions grace a `height: auto`. Sans ca, une grande photo dans une colonne etroite fait scroller horizontalement. Moche. Sur une carte blog, le conteneur a une largeur ; l'image suit.

## Object-fit : cadrer sans deformer

Parfois tu fixes une hauteur de cadre (hero, vignette carree). L'image source n'a pas le meme ratio. `object-fit` decide comment remplir.

```css
.carte img {
  width: 100%;
  height: 180px;
  object-fit: cover;
  display: block;
}
```

`cover` : remplit le cadre, recadre ce qui depasse. Ideal pour des vignettes produit uniformes. `contain` : image entiere visible, eventuelles bandes. Utile pour un logo ou un schema qu'on ne doit pas couper. `fill` : etire (souvent moche). Evite sauf cas special.

```css
.hero-media img {
  width: 100%;
  height: 320px;
  object-fit: cover;
  object-position: center top;
}
```

`object-position` dit ou ancrer le cadrage (visage en haut, produit centre...).

:::retenir
`max-width: 100%` + `height: auto` partout. Cadre fixe + `object-fit: cover` pour des vignettes alignees. Le poids, c'est le fichier, pas le CSS.
:::

## Le HTML reste responsable du fond

```html
<img
  src="cafe.jpg"
  alt="Sac de cafe grains, torrefaction maison"
  width="800"
  height="500"
>
```

`width` et `height` (attributs) aident le navigateur a reserver l'espace et limitent le saut de layout pendant le chargement. Le CSS peut ensuite redimensionner. `alt` vide (`alt=""`) seulement si l'image est purement decorative. Sinon, decris ce que l'image apporte, pas "image1".

## Idee srcset, en simple

Souvent tu as une grande photo. Sur telephone, telecharger le monstre 2000px est du gaspillage. `srcset` propose plusieurs fichiers ; le navigateur choisit.

```html
<img
  src="produit-800.jpg"
  srcset="produit-400.jpg 400w, produit-800.jpg 800w, produit-1200.jpg 1200w"
  sizes="(max-width: 600px) 100vw, 400px"
  alt="Mug ceramique blanc"
>
```

`srcset` liste les fichiers avec leur largeur reelle (`400w` = largeur 400px du fichier). `sizes` dit approximativement quelle largeur l'image occupera a l'ecran. Ici : plein ecran sous 600px, sinon environ 400px (carte dans une grille). `src` reste un fallback.

Tu n'as pas besoin de maitriser tous les cas. Comprends l'idee : plusieurs poids, le navigateur choisit. Pour un projet perso, commencer par compresser une seule image correctement reste deja un gros gain. `srcset` vient apres.

## Formats et poids

JPEG/WebP pour photos. PNG pour schemas a aplats / transparence. Evite d'envoyer un PNG enorme pour une photo. Compresse avant upload (outils en ligne, Squoosh...). Une carte produit a 200 Ko au lieu de 3 Mo, ca se sent. Le CSS ne compresse pas le fichier. Il controle l'affichage. Le poids, c'est le fichier source.

## Image dans une grille

```css
.grille {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem;
}

.carte img {
  width: 100%;
  aspect-ratio: 4 / 3;
  object-fit: cover;
}
```

`aspect-ratio` aide a garder des cartes alignees meme avant chargement complet. Combo sympathique avec `object-fit: cover`.

## Ce que ce n'est pas

Ce n'est pas un carrousel de cinq images hero des le premier projet. Une bonne image bien cadre et legere bat un slider bancal. Ce n'est pas non plus `background-image` pour une image informative : moins accessible, plus penible a gerer pour le contenu.

:::attention
Une image de 4 Mo sur une vignette, c'est du mepris pour la 4G. Pese avant de publier. Et n'oublie jamais un `alt` utile sur une image qui informe.
:::

## Petite histoire

Lea a livre une galerie avec cinq photos Instagram a pleine resolution. La page a rame sur telephone. Elle a recompresse, unifie les cadres avec `object-fit: cover`, et garde une seule image hero nette. Max a vu la difference sur sa page artisan. Sam projette le panneau Reseau : les eleves comprennent sans discours.

## Erreur classique

Mettre une largeur fixe en pixels enorme sur mobile. Oublier `alt`. Forcer `height` sans `object-fit` et ecraser le sujet. Cinq images hero en slider des le premier projet.

## En vrai

Prends une page produit. Applique `max-width: 100%` globalement sur `img`. Uniformise les vignettes avec hauteur fixe + `object-fit: cover`. Pese ton fichier image. S'il depasse 500 Ko pour une vignette, recompresse.

Si tu as deux tailles de fichier, tente un petit `srcset` sur une seule image et regarde dans l'onglet Reseau quelle variante part selon la largeur de fenetre.

## A toi

Page "Galerie atelier" : grille de quatre images (meme fausses URLs ou placeholders). Toutes en `object-fit: cover` dans un cadre `aspect-ratio: 1 / 1`. Un `alt` utile chacune. Bonus : une des images en `srcset` simple a deux largeurs.
