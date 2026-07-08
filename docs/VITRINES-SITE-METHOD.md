# Méthode « vrai site » pour les vitrines multi-pages

Référence de travail vitrine par vitrine. **Modèle pilote : `restauration`** (Brasserie Saint-Jacques).

Objectif : passer d’une démo IA minimaliste (hero + 3 blocs) à un **site sectoriel crédible** (navigation, contenu HTML, photos, formulaire, footer, SEO local).

---

## Vue d’ensemble du pipeline

```
vitrine_scenarios.py          Textes & structure multi-pages (source de vérité narrative)
        ↓
scripts/data/vitrine_photos/<slug>.json   Prompts photo par image + contextes par page
        ↓
gen_vitrine_photo_prompts.py  → scripts/data/vitrine_photo_prompts.json (manifeste global)
        ↓
[Génération IA des PNG]       → install_vitrine_photo.py (redimensionne + installe)
        ↓
vitrine_site_blocks.py        Blocs HTML Bootstrap réutilisables
        ↓
build_vitrine_site.py         Assemble les pages HTML du slug
        ↓
assets/vitrines/demos/<slug>/ styles.css (thème sectoriel)
        ↓
Sync dist/                    Copie vers dist/vitrines/<slug>/demo/ (serveur local)
```

---

## SEO & Schema.org microdata (`scripts/vitrine_seo.py`)

Chaque page générée par `build_vitrine_site.py` inclut automatiquement (via `_wrap_vitrine_page`) :

| Élément | Emplacement |
|---------|-------------|
| **Meta** | `<head>` — `title`, `description`, `robots`, `canonical`, OG, Twitter |
| **WebSite** | `<header>` — marque avec `itemprop="url"` + `itemprop="name"` |
| **WebPage** | `<main itemscope>` — `itemprop="url"`, `inLanguage` |
| **Contenu page** | Premier `<h1>` → `name` ; chapô `.lead` → `description` ; 1ère image hero → `image` |
| **Entité locale / SaaS** | `<footer itemscope>` — type sectoriel (`Restaurant`, `SoftwareApplication`…), adresse, téléphone, geo |
| **BreadcrumbList** | Fil d'Ariane **visible** sous le header (pages internes uniquement) |
| **FAQPage** | Section FAQ — `Question` / `Answer` dans l'accordéon (`vitrine_layouts.py`) |

Pas de JSON-LD, pas de microdata dans le `<head>`, pas de blocs `visually-hidden` pour le schema.

Entités par slug dans `ENTITIES`. URLs : `https://danielcraft.fr/vitrines/<slug>/demo/<page>.html`

Rebuild complet : `python scripts/build_vitrine_site.py --all`

---

## Étape 1 — Scénario et contenu (`vitrine_scenarios.py`)

Chaque vitrine a un bloc `SCENARIOS` avec :

- `slug`, `brand`, `category`, `layout`, `nav`, `pages[]`
- Par page : `hero`, `story`, `chapters`, `cards`, `gallery`, `timeline`, `cta`

La fonction `_collect_images()` **fusionne tous les contextes** de toutes les pages pour chaque fichier image (alt, titres, paragraphes). Utile pour tracer les prompts photo.

**Ne pas régénérer aveuglément** avec `vitrine_gen_multipage.py` après un site « complet » : ça écrase le HTML enrichi. Utiliser `build_vitrine_site.py` pour ce slug.

---

## Étape 2 — Prompts photo par vitrine

### Fichier dédié

Copier le modèle :

```bash
cp scripts/data/vitrine_photos/_template.json scripts/data/vitrine_photos/<slug>.json
```

Remplir pour **chaque image** (`hero.png`, `scene-1..3`, `card-1..3`, `gallery-1..2`) :

| Champ | Rôle |
|-------|------|
| `subject` | Description visuelle détaillée pour la génération IA |
| `style_suffix` | Suffixe commun au slug (ex. ambiance Metz, secteur HCR…) |
| `contexts[]` | `{ page, section, text }` — lien avec le HTML |
| `alt` | Accessibilité |
| `width` / `height` | hero 1200×520, autres 800×520 |

### Manifeste global

```bash
python scripts/gen_vitrine_photo_prompts.py
```

Les entrées avec `photo_manifest` dans le JSON global proviennent du fichier par slug.

### Génération et installation

1. Générer les PNG (IA ou autre outil) à partir du champ `prompt` du manifeste.
2. Installer :

```bash
python scripts/install_vitrine_photo.py <chemin-source.png> <slug> <filename>
# ex. python scripts/install_vitrine_photo.py gen-hero.png beaute hero.png
```

3. Nettoyer les fichiers temporaires (`gen-*.png` dans le cache Cursor, etc.).

---

## Étape 3 — Site HTML (Bootstrap 5)

### Fichiers clés

| Fichier | Rôle |
|---------|------|
| `scripts/vitrine_site_blocks.py` | Blocs : topbar, navbar, hero, stats, menu HTML, formulaire, footer, microdata inline… |
| `scripts/build_vitrine_site.py` | Builder par slug (dict `BUILDERS`) |
| `assets/vitrines/demos/<slug>/styles.css` | Thème Bootstrap (variables `--vt-*`, surcharge `--bs-*`) |

### Ajouter une nouvelle vitrine au builder

1. Dupliquer la section `restauration` dans `build_vitrine_site.py` → nouveau slug.
2. Adapter : `NAV`, contenu métier (menu, services, FAQ…), blocs utilisés.
3. Créer / adapter `styles.css` (palette sectorielle).
4. Optionnel : blocs spécifiques dans `vitrine_site_blocks.py` si le secteur l’exige (ex. prise de RDV spa, fiche bien immobilier).

```bash
python scripts/build_vitrine_site.py <slug>
```

### Bonnes pratiques (restaurant → généralisable)

- **Menu / offres en HTML**, pas en PDF ni image seule.
- **CTA visible** : navbar + hero + barre mobile + bandeau bas de page.
- **Infos pratiques** en haut : horaires, adresse, téléphone cliquable.
- **Footer 3 colonnes** : marque, liens, contact.
- **Schema.org** adapté au secteur (`Restaurant`, `LocalBusiness`, `MedicalBusiness`…).
- **Éviter les galeries pleine largeur redondantes** en bas de page si les mêmes visuels apparaissent déjà dans les chapitres / cartes.

### Variantes de layout (agencements différents)

| Slug | Layout | Blocs clés |
|------|--------|------------|
| `restauration` | Hero **centré** + bande stats | `block_hero_rich`, `block_stats`, chapitres alternés |
| `beaute` | Hero **centré** spa doux | `wrap_page_spa`, Cormorant Garamond |
| `odontologie` | Hero **split** 40/60 + entonnoir | `vitrine_layouts.py` : `block_hero_split`, `block_trust_strip`, `block_funnel_steps`, `block_bento_cards`, `block_compact_features` |
| `automobile` | Hero **overlay** + tuiles services + split **inversé** | `block_hero_overlay`, `block_service_tiles`, `block_hero_split_reverse`, `block_timeline` |
| `commerce` | Hero **éditorial** + bandeau **promos** + entonnoir drive | `block_hero_editorial`, `block_promo_cards`, `block_funnel_steps`, `block_bento_cards` |
| `comptable` | Hero **preuve sociale** + **tableau avant/après** + FAQ | `block_hero_proof_split`, `block_credentials_strip`, `block_comparison_table`, `block_stat_narrative_rows`, `block_faq_accordion` |
| `industrie` | Hero **technique** + grille specs + certs + flux horizontal | `block_hero_technical`, `block_spec_grid`, `block_cert_strip`, `block_process_flow`, `block_specs_table`, `block_sector_strip`, `wrap_page_industrial` |
| `immobilier` | Hero **recherche** + grille annonces + secteurs | `block_hero_property_search`, `block_listing_grid`, `block_neighborhood_strip`, `block_property_estimation_form`, `wrap_page_property` |
| `juridique` | Hero **overlay** navy/or + tuiles expertises + FAQ | `block_hero_overlay`, `block_service_tiles`, `block_credentials_strip`, `block_faq_accordion`, `block_legal_consultation_form`, `wrap_page_legal` |
| `architecture` | Hero **éditorial** + bento magazine + grille projets | `block_hero_editorial`, `block_bento_cards`, `block_project_grid`, `block_compact_features`, `block_architecture_brief_form`, `wrap_page_architecture` |

Inspirations web (CPA / consulting 2026) : témoignage + stats en hero, bandeau agréments E-E-A-T, tableau situation→résultat, panneaux chiffre+narratif alternés, FAQ avec schema `FAQPage`, JSON-LD `AccountingService`.

Inspirations web (B2B manufacturing) : grille capacités machine, bandeau certifications ISO/IATF, flux RFQ horizontal, formulaire devis technique, JSON-LD `ProfessionalService`.

Inspirations web (immobilier premium) : barre recherche achat/louer/vendre, grille annonces avec prix, bandeau secteurs, formulaire estimation, JSON-LD `RealEstateAgent`.

Inspirations UX (transcripts TikTok) : test des 5 premières secondes (quoi faire / pourquoi / bénéfice), une action évidente, entonnoir hero → preuves → CTA, réduction de l'effort cognitif.

Fichier layouts alternatifs : `scripts/vitrine_layouts.py`.

### Images WebP

- **`vt_picture()`** dans `vitrine_site_blocks.py` : `<picture><source webp><img png>` pour tous les blocs BS5.
- **`install_vitrine_photo.py`** : génère `.webp` en plus du `.png` à l'installation.
- **Conversion batch** : `python scripts/vitrine_webp.py [slug]` (tous les slugs si slug omis).

---

## Étape 4 — Preview locale

Après modification :

```powershell
# Regénérer le site du slug
python scripts/build_vitrine_site.py <slug>

# Copier vers dist (si serveur sur :8000)
Copy-Item -Path "assets\vitrines\demos\<slug>\*" -Destination "dist\vitrines\<slug>\demo\" -Recurse -Force
```

URL : `http://127.0.0.1:8000/vitrines/<slug>/demo/index.html` — rechargement **Ctrl+F5**.

Build complet site : `python build.py` (republie toutes les vitrines).

---

## Checklist par vitrine

Cocher au fur et à mesure :

| Slug | Photos JSON | Images IA | Site BS | Statut |
|------|-------------|-----------|---------|--------|
| **restauration** | ✅ | ✅ | ✅ | **Pilote terminé** — hero centré + stats |
| **beaute** | ✅ | ✅ | ✅ | **Terminé** — hero centré spa |
| **odontologie** | ✅ | ✅ | ✅ | **Terminé** — hero split + bento + entonnoir |
| **automobile** | ✅ | ✅ | ✅ | **Terminé** — hero overlay + tuiles + split inversé |
| **commerce** | ✅ | ✅ | ✅ | **Terminé** — hero éditorial + promos + entonnoir drive |
| **comptable** | ✅ | ✅ | ✅ | **Terminé** — preuve sociale + tableau + FAQ |
| **industrie** | ✅ | ✅ | ✅ | **Terminé** — hero technique + specs + certs + flux RFQ |
| **immobilier** | ✅ | ✅ | ✅ | **Terminé** — hero recherche + grille annonces + estimation |
| **juridique** | ✅ | ✅ | ✅ | **Terminé** — hero overlay + tuiles expertises + FAQ |
| **architecture** | ✅ | ✅ | ✅ | **Terminé** — hero éditorial + bento + grille projets |
| **fitness** | ✅ | ✅ | ✅ | **Terminé** — hero overlay sombre + planning + tarifs |
| **photographie** | ✅ | ✅ | ✅ | **Terminé** — hero éditorial + galerie masonry + preuves |
| **association** | ✅ | ✅ | ✅ | **Terminé** — hero vert + jauge impact + mobilisation |
| **education** | ✅ | ✅ | ✅ | **Terminé** — hero technique + Qualiopi + parcours admission |
| **services** | ✅ | ✅ | ✅ | **Terminé** — hero overlay teal + bento FM + offres promo |
| **etablissement** | ✅ | ✅ | ✅ | **Terminé** — hero luxe + snap chapters + marquee |
| **technologie** | ✅ | ✅ | ✅ | **Terminé** — hero scan + tabs animés + marquee clients |
| **saas-landing** | ✅ | ✅ | ✅ | **Terminé** — orbes + mockup flottant + tabs + pricing tilt |
| saas-onboarding | ✅ | ✅ | ✅ | **Terminé** — wizard progression + snap chapters |
| saas-dashboard | ✅ | ✅ | ✅ | **Terminé** — KPI pulse + compteurs live |
| saas-empty | ✅ | ✅ | ✅ | **Terminé** — morph avant/après + tabs |
| saas-notifications | ✅ | ✅ | ✅ | **Terminé** — feed notifications cascade |

---

## Ordre de travail recommandé (une par une)

1. Lire les 4 pages HTML actuelles + paragraphes dans `vitrine_scenarios.py`.
2. Rédiger `scripts/data/vitrine_photos/<slug>.json` (tous les `contexts` par page).
3. `python scripts/gen_vitrine_photo_prompts.py`
4. Générer et installer les 9 images.
5. Implémenter le builder dans `build_vitrine_site.py` + `styles.css`.
6. `python scripts/build_vitrine_site.py <slug>` → preview → ajustements.
7. Captures optionnelles : `python scripts/screenshot_vitrines.py --slugs restauration,beaute,… --install-dist` (génère dans `assets/vitrines/screenshots/` et copie vers `dist/vitrines/<slug>/screenshots/` + `demo/`)

---

## Fichiers restauration (référence)

```
scripts/data/vitrine_photos/restauration.json
scripts/build_vitrine_site.py          # BUILDERS["restauration"]
scripts/vitrine_site_blocks.py
assets/vitrines/demos/restauration/
  index.html | carte.html | histoire.html | contact.html
  styles.css
  images/hero.png, scene-*.png, card-*.png, gallery-*.png
```

---

## Rappels

- **`vitrine_gen_multipage.py`** : génération IA basique — ne pas l’utiliser sur un slug déjà passé en « vrai site ».
- **`gen_vitrine_assets.py`** : placeholders PIL — remplacer par photos IA via la méthode ci-dessus.
- Les includes catalogue (`src/includes/vitrines-*.html`) restent gérés par `build.py`, indépendamment des démos.

Voir aussi : [VITRINES.md](./VITRINES.md) (catalogue, deploy, captures).
