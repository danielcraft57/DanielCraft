# Scripts — traitement des images (portfolio, hero)

Prérequis :

```bash
pip install -r requirements-scripts.txt
```

## Rôle de chaque script

| Script | Rôle |
|--------|------|
| `recolor_red_dominant_images.py` | Cible **uniquement** les images à fort rouge/orange → bleu métal. |
| `recolor_project_hero_to_blue.py` | Recolorise **tout** le dossier projets + hero (rouges → bleu). À utiliser avec parcimonie : peut uniformiser en bleu. |
| `soften_white_backgrounds.py` | Fonds blancs → pastel `#e8f2fc`. **Par défaut** `--max-side 1920` (rapide) ; `--max-side 0` = pleine résolution (lent sur hero). `--skip-hero` pour ignorer `assets/images/hero/`. |
| **`reduce_blue_cast.py`** | Réduit une **dominante bleue** trop forte (pixels B dominants) : réchauffe légèrement, baisse le bleu. |
| **`apply_complementary_grades.py`** | **6 variantes** + `--blend dark\|wide\|midtone\|full` (défaut **dark** pour UI sombres) + `--punch` pour amplifier les teintes. |
| **`portfolio_image_pipeline.py`** | Enchaîne : soften → reduce_blue → grades (sous-processus). |
| **`og_image_pipeline.py`** | Images **Open Graph** (`assets/images/og/`) : bleu métal → reduce_blue → grades complémentaires → optionnel 1200×630 + WebP (`optimize_images`). |
| **`generate_site_og_images.py`** | Génère les cartes OG **1200×630** du site (pages statiques, prestations, vitrines, projets — hors blog). |
| `generate_favicon_pngs.py` | Pack favicons depuis le SVG. |
| **`rasterize_about_hero.py`** | PNG + WebP 1200×1200 (ou `--size`) pour `about-section-hero`, même composition que le SVG (Pillow, sans Cairo). |
| **`generate_home_images.py`** | Illustrations accueil (`assets/images/home/`) : hero + 4 cartes offres, charte bleu DanielCraft (PNG + WebP). |

## Module partagé

- `_image_tools.py` : `ROOT`, `EXTS`, `save_image()`, `iter_image_files()`, dossiers par défaut projets + hero.

## Pipeline conseillé (après un gros recolor bleu)

1. `python scripts/reduce_blue_cast.py --strength 0.45`
2. `python scripts/apply_complementary_grades.py --strength 0.30`
3. (Optionnel) `python scripts/soften_white_backgrounds.py` si les fonds blancs ressortent encore.

Ou tout d’un coup :

```bash
# Teintes complémentaires visibles sur captures sombres :
python scripts/portfolio_image_pipeline.py --reduce-strength 0.45 --grade-strength 0.55 --grade-blend dark --grade-punch 1.2

# Encore plus fort (toute l’image teintée) :
python scripts/apply_complementary_grades.py --blend full --strength 0.4 --punch 1.3
```

Pour **simuler** les deux dernières étapes :

```bash
python scripts/portfolio_image_pipeline.py --skip-soften --dry-run
```

## Paramètres utiles

- `reduce_blue_cast.py --strength 0..1` — intensité de la correction anti-bleu.
- `apply_complementary_grades.py --strength 0..1` — intensité sur les **midtones** (ombres / hautes lumières préservées).
- `apply_complementary_grades.py --include-hero` — inclut `assets/images/hero/`.

Ensuite : `python build.py` (ou `--watch`) pour copier vers `dist/`.
