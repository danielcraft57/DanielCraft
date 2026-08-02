# Chapitre 18 - Perf CSS legeres : aller vite sans obsession

La performance, ce n'est pas seulement JavaScript et images. Le CSS peut aussi ralentir ou faire "sauter" une page. Bonne nouvelle : pour un site vitrine simple, quelques hygiene habits suffisent. Pas besoin de devenir ingenieur navigateur.

Chez DanielCraft, on vise "snappy et propre" : chargement raisonnable, peu de surprise visuelle, CSS maintenable. Lea coupe une image hero avant d'optimiser une media query. Max se fiche des scores Lighthouse : il veut que sa page devis s'ouvre vite sur 4G. Sam apprend a ses eleves a mesurer avant de micro-optimiser. Trois postures, meme ordre : d'abord le gros, ensuite le detail.

## Ce que ce n'est pas

Ce n'est pas courir apres 100/100 sur une page d'atelier. Ce n'est pas inliner du "critical CSS" obligatoire a ton niveau. Ce n'est pas non plus ajouter une lib CSS entiere pour deux boutons. Et ce n'est surtout pas micro-optimiser le CSS pendant qu'un PNG de logo fait 2 Mo. La perf honnete commence par le poids evident.

## Ordre d'attaque

Tu ouvres l'onglet Reseau. Tu vois le poids total et le poids images. Tu listes CSS, images, polices. Tu attaques le plus lourd. Souvent, ce n'est pas ta feuille de style : c'est le hero. Ensuite tu nettoies les regles mortes, tu limites les fonts, tu reserves l'espace des media pour eviter les sauts. La page respire. Tes visiteurs ne savent pas pourquoi - ils restent.

Chez DanielCraft, on attaque dans cet ordre : images, polices, CSS mort, animations permanentes, micro-selecteurs. Pas l'inverse. Si tu n'as que trente minutes, fais uniquement l'image la plus lourde. Un gros gain visible bat dix micro-optimisations invisibles.

:::retenir
Mesure avant de micro-optimiser. Images d'abord, puis polices, puis CSS mort. Un gros gain visible bat dix tweaks invisibles.
:::

## Hygiene CSS et selecteurs

Chaque regle que tu n'utilises plus reste un poids mental (et parfois reseau). Quand tu termines un atelier, supprime les essais commentes sur vingt lignes. Evite les selecteurs ultra longs : fragiles, et le navigateur prefere des classes simples sur les elements concernes.

```css
/* Fragile */
body div.main section.cartes article.carte p.prix span {}

/* Clair */
.carte-prix {}
```

Animer `width`, `height`, `top`, `left` peut couter plus cher qu'animer `transform` et `opacity`. Pour les hovers de cartes, tu le sais : `translateY` + ombre. Ne recalcule pas toute la page a chaque hover.

## Images, fonts, stabilite

Compresse. Redimensionne a la taille utile. `width`/`height` ou `aspect-ratio` pour reserver l'espace (moins de layout shift). `srcset` quand tu as plusieurs fichiers. Une landing avec un hero 3 Mo restera lente quoi que tu fasses en CSS.

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

Charger cinq familles Google Fonts pour trois titres ralentit. Une ou deux familles suffisent. `font-display: swap` (quand tu charges une webfont) evite le texte invisible trop longtemps. Sur beaucoup de pages de ce livre, une stack systeme soignee reste honnete et rapide.

## Petite histoire

Lea a passe une apres-midi a "optimiser" des transitions pendant qu'une image Instagram exportee a pleine resolution plombait la home. Elle a recompresse : -70 % sur le fichier, page transformee. Max a demande a son neveu pourquoi le site "saccadait" : une image sans hauteur reservee faisait sauter le bouton devis. Sam a affiche le panneau Reseau en projecteur : silence dans la classe, puis "ah".

:::attention
Dix animations permanentes, ombres a dix couches, meme image hero en fond CSS et en balise `img` : tu alourdis sans gagner. Et non, les variables CSS ne "ralentissent" pas le site.
:::

## Erreur classique

Micro-optimiser le CSS pendant qu'un PNG de 3 Mo plombe la home. Croire que les variables ralentissent. Charger cinq fonts pour trois titres. Ou dix animations permanentes "pour faire vivant" : souvent elles coutent plus qu'elles n'apportent.

## En vrai

Sur ta landing, liste les fichiers. Note le plus lourd. Attaque celui-la. Recompresse l'image. Supprime une font inutile. Relance. Sens la difference. Cherche ensuite une classe CSS orpheline : si elle n'existe plus dans le HTML, vire-la. Si tu as trente minutes seulement, ignore le CSS mort et fais uniquement l'image. Lea a perdu une apres-midi sur des transitions pendant qu'un hero Instagram plombait tout. Max a gagne dix secondes de perception en compressant juste le hero. Sam affiche le waterfall Reseau : les eleves voient le "gros" avant le "fin".

## A toi

Fais un "pass perf" de 30 minutes sur une page : (1) image la plus lourde recompressee, (2) CSS nettoye d'essais, (3) verification `max-width` sur media, (4) une seule famille de police principale. Ecris le poids avant/apres de l'image. Objectif : -50 % sur cette image, ou mieux. Garde le chiffre. C'est ta preuve, pas un sentiment.
