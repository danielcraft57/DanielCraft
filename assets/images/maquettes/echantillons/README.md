# Maquettes `/echantillons` - catalogue themes

References design (pas servies en live). Cible : page catalogue alignee sur `/bouquins` et `/nos-offres`.

## Role

Remplacer le hero + piliers actuels de `/echantillons` par le meme ADN catalogue :

1. **Search hero** (fond SVG orbes / vagues, titre, recherche, chips secteurs)
2. **Template de la semaine** (bandeau type deal-week bouquins / offres)
3. **Grille catalogue** (cartes echantillon, ordre melange chaque jour, lazy-load images)
4. **CTA + liens** bas de page

## Comportements a coder ensuite

| Fonction | Detail |
|----------|--------|
| Ordre journalier | Melange deterministe des cartes selon la date du jour (meme ordre pour tous les visiteurs d'un meme jour) |
| Template de la semaine | 1 echantillon mis en avant (rotation hebdo), ruban « Template de la semaine » |
| Lazy-load | Images cartes en `data-src` + `dc-lazy-img` (comme le catalogue actuel / livres) |

## Composition desktop XL

1. Header site DanielCraft
2. Hero recherche : titre, lead court, champ recherche, chips (Tous, Restau, Commerce, Beaute, Sante, Auto…)
3. Bandeau **Template de la semaine** : apercu fenetre site + copy + CTAs (fiche / demo live)
4. Grille 3 colonnes de cartes echantillon (media scrollable, badge secteur, titre, extrait, 2 boutons)
5. CTA « Parler d'un projet » + nav secondaire

## Responsive

- **Mobile** : hero stack, deal-week empile, grille 1 colonne, chips horizontales scrollables
- **Tablette** : grille 2 colonnes, deal-week 2 colonnes

## Fichiers maquettes

| Fichier | Role |
|---------|------|
| `echantillons-xl-catalogue.png` | Page complete XL (hero + semaine + grille) |
| `echantillons-xl-template-semaine.png` | Zoom bandeau Template de la semaine |
| `echantillons-mobile-catalogue.png` | Variante mobile stack |

Prompts : [`PROMPTS.md`](PROMPTS.md).

## Style

Aligne `/bouquins` + `/nos-offres` : fond clair technique `#f5f7fb` → `#e9eef6`, encre `#0f172a`, bleu UI `#2563eb` / cyan `#7bcde3`, vert doux `#91b98a`. Accent CTA / rubans en **ambre** `#d97706` / `#f59e0b` (complementaire du bleu, pas de rouge site). Pas de cartoon. Textes francais. Marque DanielCraft discrete.
