# Maquettes UI — Livres, Prestations, Blog

Références de design validées (30/07/2026). Les PNG sont dans `assets/images/maquettes/`.

## Palette commune DanielCraft

| Token | Usage |
|-------|--------|
| `#0f3550` | Encre / titres / CTA foncé |
| `#1a5f85` | Accent principal (teal) |
| `#2f9e6a` | Accent positif / packs |
| `#e8f6fc` → `#eef8f1` | Fonds hero (dégradé doux) |
| Blanc + gris bleu `#f3f7f9` | Cartes / rayons |

Éviter : violet, cream/terracotta, layout « journal ».

---

## Livres (`/livres/`)

**Inspiration :** Fnac / Amazon livres  
**Fichiers :** `assets/images/maquettes/livres/`

| Fichier | Écran |
|---------|--------|
| `maquette-livres-catalogue.png` | Catalogue + recherche + deal + grille |
| `maquette-livres-fiche.png` | Fiche produit PDF |
| `maquette-livres-mobile.png` | Mobile catalogue |

**À développer :**
1. Hero recherche + chips (déjà branché)
2. Pack de la semaine (déjà branché)
3. Barre rayons / filtres niveaux
4. Cartes couverture + prix + CTA Acheter
5. Fiche : couverture dominante, prix, trust, Stripe

---

## Prestations (`/nos-offres`)

**Inspiration :** Stripe Pricing, Linear, marketplaces templates  
**Fichiers :** `assets/images/maquettes/prestations/`

| Fichier | Écran |
|---------|--------|
| `maquette-prestations-catalogue.png` | Catalogue services + recherche + vedettes |
| `maquette-prestations-fiche.png` | Fiche offre + devis |

**À développer :**
1. Hero recherche + chips (existant — peaufiner)
2. Bandeau « Services en vedette »
3. Cartes plus SaaS (icône, prix « À partir de », CTA Voir)
4. Trust strip bas de page
5. Fiche : visuel + prix + devis

---

## Blog (`/blog/`)

**Inspiration :** Medium, Smashing Magazine, Stripe Blog  
**Fichiers :** `assets/images/maquettes/blog/`

| Fichier | Écran |
|---------|--------|
| `maquette-blog-liste.png` | Index : hero split + à la une + grille |
| `maquette-blog-article.png` | Article éditorial

**À développer :**
1. Hero split (titre + recherche/chips)
2. Carte « À la une » horizontale
3. Grille articles (vignette, catégorie, extrait, temps de lecture)
4. Article : colonne lisible, meta, articles liés

---

## Ordre d’implémentation

1. Livres (catalogue + fiche) — base e-commerce déjà en place  
2. Prestations (catalogue + trust + peaufinage cartes)  
3. Blog (index éditorial + article)

Garder le moteur de recherche client existant (`*-search.js`) et la charte site (nav/footer inchangés hors pages concernées).
