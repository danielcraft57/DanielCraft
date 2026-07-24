# Chapitre 18 - Perf CSS legeres : aller vite sans obsession

La performance, ce n'est pas seulement JavaScript et images. Le CSS peut aussi ralentir ou faire "sauter" une page. Bonne nouvelle : pour un site vitrine simple, quelques hygiene habits suffisent. Pas besoin de devenir ingenieur navigateur.

Chez DanielCraft, on vise "snappy et propre" : chargement raisonnable, peu de surprise visuelle, CSS maintenable.

## Moins de CSS inutile

Chaque regle que tu n'utilises plus reste un poids mental (et parfois reseau). Quand tu termines un atelier, supprime les essais commentes sur vingt lignes. Garde un fichier clair.

Evite aussi les selecteurs ultra longs. Ils sont fragiles et le navigateur prefere des classes simples sur les elements concernes.

```css
/* Fragile */
body div.main section.cartes article.carte p.prix span {}

/* Clair */
.carte-prix {}
```

## Images : le vrai levier

Souvent, le CSS n'est pas le coupable n°1 : ce sont les images. Compresse. Redimensionne a la taille utile. `width`/`height` ou `aspect-ratio` pour reserver l'espace (moins de layout shift). `srcset` quand tu as plusieurs fichiers.

Une landing avec un hero 3 Mo restera lente quoi que tu fasses en CSS.

## Eviter les reflows dramatiques

Animer `width`, `height`, `top`, `left` peut couter plus cher qu'animer `transform` et `opacity`. Pour les hovers de cartes, tu le sais deja : `translateY` + ombre.

Ne recalcule pas toute la page avec des mesures exotiques a chaque hover. Reste simple.

## Fonts

Charger cinq familles Google Fonts pour trois titres ralentit. Une ou deux familles suffisent. `font-display: swap` (quand tu charges une webfont) evite le texte invisible trop longtemps.

Sur beaucoup de pages de ce livre, une stack systeme soignee ou une serif locale reste honnete et rapide.

## Critical CSS ? Pas obligatoire ici

Les pros inlinent parfois le CSS critique du dessus de page. Pour ton niveau et un petit site, une feuille externe claire + images legeres + peu de polices, c'est deja excellent. N'optimise pas ce que tu n'as pas mesure.

## Mesurer un peu

Ouvre l'onglet Reseau : poids total, poids images. Lighthouse / insights : regarde surtout les gros ecarts (image enorme, contraste, etc.). Ne cours pas apres 100/100 pour une page d'atelier. Cours apres "rien d'enorme et bete".

## CSS qui aide la stabilite

```css
img,
video {
  max-width: 100%;
  height: auto;
}

.carte img {
  aspect-ratio: 4 / 3;
  object-fit: cover;
}
```

Reserver l'espace limite les sauts quand l'image arrive. Tes visiteurs te remercient inconsciemment.

## Variables et maintenance

Un theme en variables, c'est aussi de la perf humaine : tu modifies moins de lignes, tu introduis moins de bugs, tu livres plus vite. La perf, ce n'est pas que des millisecondes.

## Erreur classique

Ajouter une lib CSS entiere pour deux boutons. Ou dix animations permanentes. Ou des ombres a dix couches sur chaque carte. Ou charger la meme image hero en fond CSS et en balise `img`.

Autre piege : micro-optimiser le CSS pendant que le PNG du logo fait 2 Mo.

## En vrai

Sur ta landing, liste les fichiers (CSS, images, polices). Note le plus lourd. Attaque celui-la. Recompresse l'image. Supprime une font inutile. Relance. Sens la difference.

Regarde aussi le nombre de regles CSS mortes : cherche une classe dans le HTML ; si elle n'existe plus, vire-la du CSS.

## A toi

Fais un "pass perf" de 30 minutes sur une page : (1) image la plus lourde recompressee, (2) CSS nettoye d'essais, (3) verification `max-width` sur media, (4) une seule famille de police principale. Ecris le poids avant/apres de l'image. Objectif : -50 % sur cette image, ou mieux.
