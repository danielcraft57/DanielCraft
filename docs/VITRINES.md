# Vitrines HTML (catalogue, démos, captures)

## Ancre sur l’accueil

La section catalogue sur la page d’accueil a l’**id `vitrines`** : liens internes du type `/#vitrines` ou `#vitrines` (navigation, hero, pied de page).

Le style utilise toujours la classe **`vitrines-showcase`** ; seul l’identifiant d’ancre a été raccourci.

## Fichiers générés (ne pas éditer à la main)

- **`src/includes/vitrines-catalog-embed.html`** — bloc catalogue sur l’accueil (`build_vitrines_catalog_embed()`).
- **`src/includes/vitrines-page-collection.html`** — même grille pour la page **`/vitrines/`** (généré dans la foulée).
- Données : **`src/data/vitrines.json`**. Toute modification manuelle de ces includes est écrasée au prochain build.

## Sources et build

| Rôle | Emplacement |
|------|-------------|
| Données catalogue (titres, slugs, prix, textes) | `src/data/vitrines.json` |
| Maquettes statiques (HTML/CSS démo) | `assets/vitrines/demos/` |
| Captures Playwright (optionnel en dépôt) | `assets/vitrines/screenshots/<slug>/` |
| Sortie site | `dist/vitrines/` : catalogue **`index.html`**, index technique démos **`hub-bulma.html`**, `/<slug>/demo/`, captures, fiches `/<slug>/index.html` |

Commandes utiles :

```bash
python build.py
python scripts/screenshot_vitrines.py   # ou scripts/screenshot_showcases.ps1
```

Variables d’environnement des captures : voir **`.env.example`** (`WEBSITE_SCREENSHOT_*`).

## Git et images

Les fichiers sous **`assets/vitrines/screenshots/`** sont ignorés par Git (sauf **`.gitkeep`**). Les **WebP** sous **`assets/images/projets/`** et certaines variantes **about-section-hero** le sont aussi : voir **`.gitignore`**.

Après un clone : exécuter **`screenshot_vitrines.py`** (ou récupérer les captures par un autre canal) avant un build destiné à la prod si les vignettes sont nécessaires.

## Déploiement

Le dossier **`dist/vitrines/`** doit être publié avec le reste du site (HTML, `assets/`, `api/`, `blog/`, `projets/`). Le script **`scripts/deploy-content.ps1`** synchronise tout **`dist/`** en mode rsync ; en fallback **scp**, le dossier **`vitrines/`** est copié explicitement. Voir aussi **`docs/DEPLOYMENT.md`** et **`docs/DEPLOYMENT-PS.md`**.

## Versions / tags

Les tags de version (ex. `v1.4.0`) et l’historique détaillé restent dans **`docs/CHANGELOG.md`** ; aligner une release vitrine avec un tag se fait au choix de publication (pas d’automatisation imposée ici).
