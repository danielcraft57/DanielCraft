# Maquettes UI — DanielCraft

Références visuelles validées (30–31 juil. 2026). Palette site : teal `#0f3550` / `#1a5f85`, accents mint, cartes blanches. Pas de violet, pas de crème terracotta.

## Fichiers

| Zone | Fichier | Inspiration | Cible live |
|------|---------|-------------|------------|
| Livres catalogue | `livres/maquette-livres-catalogue.png` | Fnac / Amazon livres | `/livres/` |
| Livres fiche | `livres/maquette-livres-fiche.png` | Cultura / Amazon produit | `/livres/<slug>/` |
| Livres mobile | `livres/maquette-livres-mobile.png` | Apps retail livres | `/livres/` (mobile) |
| Prestations catalogue | `prestations/maquette-prestations-catalogue.png` | Stripe Pricing, Linear, marketplaces | `/nos-offres` |
| Prestations fiche | `prestations/maquette-prestations-fiche.png` | Webflow / Framer product | `/nos-offres` → fiche |
| Blog liste | `blog/maquette-blog-liste.png` | Medium, Smashing Magazine | `/blog/` |
| Blog article | `blog/maquette-blog-article.png` | Medium, Stripe Blog | `/blog/<slug>/` |

## Patterns à respecter

### Commun
- Hero gradient soft + barre de recherche dominante + chips de filtre
- Cartes blanches, coins ~8–12px, ombre légère
- Prix / méta bien ancrés, CTA clair

### Livres
- Pack de la semaine sous la recherche
- Rayons / filtres (niveau, type, catégorie)
- Couvertures PDF dominantes, prix 0,50 € / packs

### Prestations
- Flux page `/nos-offres` : **recherche** → **offre de la semaine** → **packs** → catalogue + sidebar → landing allégée
- Rotation hebdo : `src/data/prestations-deal-week.json` (ISO week, `force_slug` optionnel)
- Sidebar catégories + compteurs (desktop)
- Grille dense desktop (3–4+ cartes)
- Bandeau confiance (expertise, délai, accompagnement, paiement)
- Fiche produit : visuel gauche, prix + highlights, bénéfices / inclus en 2 colonnes
- Prompts images cartes : `prestations/PROMPTS-IMAGES.md`

### Blog
- Hero éditorial + recherche + chips sujets
- Carte « À la une » large (image + extrait)
- Grille d’articles (catégorie, temps de lecture, Lire →)
