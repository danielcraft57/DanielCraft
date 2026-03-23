# Scripts V6

## clone-loupix57-repos.ps1

Telecharge (clone) tous les depots GitHub du compte **loupix57** dans le dossier `repos-loupix57` a la racine du projet (DanielCraft).

**Prerequis :** Git installe et accessible en ligne de commande.

**Execution :**

```powershell
cd <chemin-vers-projet>\V6
.\scripts\clone-loupix57-repos.ps1
```

Ou depuis la racine DanielCraft :

```powershell
.\V6\scripts\clone-loupix57-repos.ps1
```

Les depots sont clones en `DanielCraft/repos-loupix57/` (un sous-dossier par repo). Les depots deja presents sont ignores (SKIP). Pour tout recloner, supprime le dossier `repos-loupix57` puis relance le script.

**But :** etudier le code source de chaque projet loupix57 et les integrer au site V6 (donnees deja integrees dans `assets/js/github-projects.js` et une selection dans `assets/js/portfolio.js`).

## Favicons (palette bleue DanielCraft)

- **Source** : `assets/icons/favicon.svg` (dégradé aligné sur la navbar).
- **Pack PNG / ICO / manifest** : régénérer après modification du SVG :

```powershell
pip install -r requirements-scripts.txt
python scripts/generate_favicon_pngs.py
```

Les fichiers sont écrits dans `assets/icons/favicons/`. Le build copie tout le dossier `assets/` vers `dist/`.

## Images portfolio / hero (recolor, fonds, complémentaires)

Voir **[README_IMAGES.md](README_IMAGES.md)** : `reduce_blue_cast.py`, `apply_complementary_grades.py`, `portfolio_image_pipeline.py`, et lien avec `soften_white_backgrounds.py` / `recolor_project_hero_to_blue.py`.
