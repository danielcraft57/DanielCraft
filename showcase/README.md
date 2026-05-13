# Vitrines fictives (portfolio)

Sites statiques **100 % fictifs** pour captures d’écran (desktop, tablette, mobile). Aucune marque réelle.

## Images

Les fichiers `showcase/*/images/*.png` sont des **visuels générés** (ambiance photographique) pour la démo ; **aucune** entreprise réelle n’est représentée.

Pour régénérer les **mosaïques PNG** (éducation + association) sans IA externe, à la racine du dépôt : `python scripts/generate_showcase_vitrine_visuals.py` (Pillow). Les SVG de référence optionnels sont dans `showcase/shared/generated/`.

## Design (références)

- **Material Design 3** : surfaces tonales, formes (coins), élévation, typo **Roboto**, courbes de mouvement — [m3.material.io/styles](https://m3.material.io/styles).
- **UX « sites primés »** : hiérarchie typographique claire, cartes avec élévation et survol discret, en-têtes sticky où pertinent, `prefers-reduced-motion`, focus visible.

## Animations (certaines vitrines)

Sur **technologie**, **chocolatier**, **beaute**, **banque**, **automobile** : [AOS](https://michalsnik.github.io/aos/) (apparition au scroll), [anime.js](https://animejs.com/) (entrée du hero), CSS partagé `shared/vitrine-animations.css` (reflet léger sur bandeaux CTA, état pré-JS du hero). Choix alignés avec la veille [librairies JS utiles au front](https://www.codeur.com/blog/meilleures-librairies-javascript/) (AOS, anime.js). Les scripts CDN sont chargés dans chaque page concernée ; `prefers-reduced-motion: reduce` désactive AOS et l’animation hero.

En complément (sélection inspirée de [27 librairies d’animation web CSS et JS — Blog du Webdesign](https://www.blogduwebdesign.com/blog/webdesign/librairies-d-animation-web-css-javascript.html)) : **Hover.css** (survol « léger » sur cartes ou boutons), **Animate.css** (entrées hero sur **odontologie**, **education**), **Micron.js** (micro-interactions au clic sur **technologie** et **banque**). Fichier `shared/vitrine-lib-compat.css` atténue Hover / Animate lorsque l’utilisateur demande moins de mouvement.

Effets **maison** (sans dépendance npm) dans `shared/vitrine-creative.css` + `shared/vitrine-creative.js` : barre de progression de lecture en haut de page, halo souris sur hero (**industrie**, **services**), cartes « usine » en perspective (**industrie**), titre métal animé + boutons magnétiques (**services**), aurora conique sur CTA (**association**), lignes de tableau en cascade (**comptable**), constellation CSS sur hero hôtel (**etablissement**). Le script désactive halo et magnétisme si `prefers-reduced-motion: reduce` ; la barre de progression reste utilisable.

**Images** : [GLightbox](https://github.com/biati-digital/glightbox) (galerie plein écran, zoom, navigation clavier/tactile) et [Swiper](https://swiperjs.com/) (carrousel **coverflow** + autopause au survol) via `shared/vitrine-images.css` et `shared/vitrine-images.js`. Swiper sur **restauration**, **automobile**, **education** (visuels Pillow) et **association** ; GLightbox sur ces pages plus **beaute**, **commerce**, **services**, **etablissement**, **chocolatier**, **technologie** (galerie + effet **Ken Burns** CSS sur le visuel réseau). Transitions **`.vitrine-img-reveal`** (IntersectionObserver) et **`.vitrine-figure--motion`** (survol) + traits SVG **`.vitrine-sketch-stroke`**. `prefers-reduced-motion` raccourcit ou coupe autoplay Swiper, effets d’ouverture GLightbox, traits animés et reveals.

Fichiers partagés : `shared/reset.css`, `shared/tokens.css`, `shared/media.css`, **`shared/layout-desktop.css`** (grilles XL, colonnes, sous-nav ancrage, blocs « densité » typographique). Hub : `hub.css`.

## Desktop & ergonomie

- **Chocolatier** : en-tête regroupé (`site-head`) sticky sur grand écran, **sous-navigation** « Sur cette page » (masquée en dessous de 1024px de large), section journal en **2 colonnes** + encadré KPI sticky, grille produits jusqu’à **4 colonnes** (≥ 1400px).
- **Autres vitrines** : `layout-desktop.css` pour textes **pleine largeur** (lead, colonnes type journal ≥ 1320px), bannières image 21:9, grilles denses.
- Le dossier `showcase/screenshots/` (généré par le script ci-dessous) est **ignoré par Git** — régénérez-le après changements CSS.

## Captures multi-viewports (Playwright)

Installez une fois :

```bash
pip install -r showcase/requirements-screenshots.txt
playwright install chromium
```

Puis à la racine du dépôt :

```bash
python showcase/screenshot_showcases.py
```

Sortie : `showcase/screenshots/<hub|chocolatier|…>/<desktop|tablet|mobile>_<WxH>.jpg` (ou `.webp` si `WEBSITE_SCREENSHOT_CAPTURE_FORMAT=webp`). Les tailles de viewport, délais, `wait_until`, qualités JPEG/WebP, `device_scale_factor`, blocage trackers, `reduced_motion` et désactivation des animations suivent les variables d’environnement **`WEBSITE_SCREENSHOT_*`** (mêmes noms que la config Celery du site). Capture PNG pleine page côté Playwright, puis **redimensionnement** selon `WEBSITE_SCREENSHOT_MAX_WIDTH_*` et export via **Pillow** (inclus dans `requirements-screenshots.txt`).

PowerShell :

```powershell
.\scripts\screenshot_showcases.ps1
```

Utilisez ces images pour ajuster marges, tailles de police et points de rupture responsive.

## Prévisualisation locale (recommandé)

À la **racine du dépôt** — sert le dossier `showcase/` et **ouvre le navigateur** sur le hub :

```bash
python showcase/serve_showcase.py
```

Options :

```bash
python showcase/serve_showcase.py --port 9000 --no-browser
python showcase/serve_showcase.py --host 0.0.0.0
```

Sous **Windows** (PowerShell), depuis la racine :

```powershell
.\scripts\serve_showcase.ps1
.\scripts\serve_showcase.ps1 -Port 9000 -NoBrowser
```

Alternative sans script : `cd showcase` puis `python -m http.server 8765`, puis ouvrir `http://127.0.0.1:8765/` (aucune ouverture auto du navigateur).

## Déploiement (nginx)

Copier le dossier `showcase/` sur le serveur (ex. `/var/www/showcase-demos/`) et exposer ce répertoire comme racine ou sous-chemin (`location /showcase/ { alias ...; }`). Les liens du hub utilisent des chemins relatifs par dossier.

## Structure

| Dossier        | Secteur     |
|----------------|-------------|
| `chocolatier/` | Artisanat   |
| `odontologie/` | Santé bucco |
| `banque/`      | Finance     |
| `industrie/`   | B2B / usine |
| `comptable/`   | Expertise   |
| `association/` | ESS         |
