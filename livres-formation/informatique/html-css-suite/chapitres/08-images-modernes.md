# Chapitre 8 - Images modernes : taille, cadrage, srcset

Une belle image mal geree casse une page. Elle debord. Elle ecrase le texte. Elle pese 4 Mo et fait attendre le telephone en 4G. Les bases, tu les as (`img`, `alt`). Ici, on range le comportement CSS et on touche a l'idee de `srcset`.

Chez DanielCraft, une image de produit nette et legere, c'est du respect pour le visiteur. Pas besoin d'etre ingenieur perf : quelques reflexes suffisent.

## Ne jamais deborder : max-width

```css
img {
  max-width: 100%;
  height: auto;
}
```

Regle d'or. L'image peut retrecir dans son conteneur. Elle garde ses proportions grace a `height: auto`. Sans ca, une grande photo dans une colonne etroite fait scroller horizontalement. Moche.

Sur une carte blog, le conteneur a une largeur ; l'image suit.

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

`cover` : remplit le cadre, recadre ce qui depasse. Ideal pour des vignettes produit uniformes.

`contain` : image entiere visible, eventuelles bandes. Utile pour un logo ou un schema qu'on ne doit pas couper.

`fill` : etire (souvent moche). Evite sauf cas special.

```css
.hero-media img {
  width: 100%;
  height: 320px;
  object-fit: cover;
  object-position: center top;
}
```

`object-position` dit ou ancrer le cadrage (visage en haut, produit centre...).

## Le HTML reste responsable du fond

```html
<img
  src="cafe.jpg"
  alt="Sac de cafe grains, torrefaction maison"
  width="800"
  height="500"
>
```

`width` et `height` (attributs) aident le navigateur a reserve l'espace et limitent le saut de layout pendant le chargement. Le CSS peut ensuite redimensionner.

`alt` vide (`alt=""`) seulement si l'image est purement decorative. Sinon, decris ce que l'image apporte, pas "image1".

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

Lecture douce :

`srcset` liste les fichiers avec leur largeur reelle (`400w` = largeur 400px du fichier).

`sizes` dit approximativement quelle largeur l'image occupera a l'ecran. Ici : plein ecran sous 600px, sinon environ 400px (carte dans une grille).

`src` reste un fallback.

Tu n'as pas besoin de maitriser tous les cas. Comprends l'idee : plusieurs poids, le navigateur choisit. Pour un projet perso, commencer par compresser une seule image correctement reste deja un huge win. `srcset` vient apres.

## Formats et poids (sans dogmatisme)

JPEG/WebP pour photos. PNG pour schemas a aplats / transparence. Evite d'envoyer un PNG enorme pour une photo. Compresse avant upload (outils en ligne, Squoosh, script...). Une carte produit a 200 Ko au lieu de 3 Mo, ca se sent.

Le CSS ne compresse pas le fichier. Il controle l'affichage. Le poids, c'est le fichier source.

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

## Erreur classique

Mettre une largeur fixe en pixels enorme sur mobile. Oublier `alt`. Utiliser `background-image` pour une image informative (moins accessible, plus penible a gerer pour le contenu). Forcer `height` sans `object-fit` et ecraser le sujet.

Autre piege : cinq images hero en slider des le premier projet. Une bonne image bien cadre bat un carrousel bancal.

## En vrai

Prends une page produit. Applique `max-width: 100%` globalement sur `img`. Uniformise les vignettes avec hauteur fixe + `object-fit: cover`. Pese ton fichier image (proprietes du fichier). S'il depasse 500 Ko pour une vignette, recompresse.

Si tu as deux tailles de fichier, tente un petit `srcset` sur une seule image et regarde dans l'onglet Reseau du navigateur quelle variante part selon la largeur de fenetre.

## A toi

Page "Galerie atelier" : grille de quatre images (meme fausses URLs ou placeholders). Toutes en `object-fit: cover` dans un cadre `aspect-ratio: 1 / 1`. Un `alt` utile chacune. Bonus : une des images en `srcset` simple a deux largeurs.
