# Prompt pour l'image de la section "À propos"

Ce prompt sert à générer l'illustration principale de la section "À propos" (`about-section-hero.webp/.png`), celle qui s'affiche dans le bloc visuel à droite du texte (grand carré rouge avec une icône/profil stylisé).

Réutilise la même charte que pour les autres visuels du site (voir `prompts_images_projets.md`), en particulier :

- Couleur principale : rouge vif `#dc2626` (et variantes `#b91c1c`, `#ef4444`)
- Fonds de page : blanc / gris très clair
- Style : moderne, épuré, pro, sans fouillis
- Pas de visages réels (uniquement avatar / silhouette abstraite)

## Prompt pour Midjourney / DALL-E / Stable Diffusion

```text
Create a modern, minimalistic "About" section illustration for a freelance web developer portfolio, matching the DanielCraft visual identity.

Visual layout:
- Main element: a large rounded rectangle card (almost square) with a smooth red gradient background (from #dc2626 to a slightly darker red like #b91c1c).
- Center of the card: a simple, abstract avatar icon representing a developer (circle for the head, rounded shoulders), flat design, light pink / very light skin tone or neutral beige, no facial details.
- Around or behind the avatar: a few very subtle tech shapes (small dots, lines, or circuit / data-inspired curves) in slightly lighter or darker red tones, staying minimal.

Global style:
- Background of the whole image: white or very light gray (#f9fafb / #f3f4f6), so the red card stands out clearly.
- Card with soft shadow, rounded corners (8 to 16px feeling), clean and centered composition.
- No text on the card, no logos, no additional typography.
- Flat / semi-flat illustration style, very clean and professional, no 3D kitsch.

Mood and tone:
- Professional but friendly.
- Feels like a modern portfolio section for a serious but approachable developer.
- High contrast and good readability when the card is displayed as a medium-size block on a white page.

Technical details:
- Aspect ratio: 4:3 or close to a square (e.g. 1200x900).
- High resolution PNG or WebP, ready to be used as "about-section-hero" illustration on a website.

Avoid:
- Realistic human faces or photos.
- Too many details or clutter around the avatar.
- Text, UI screenshots, or logos inside the card.
```

## Variante "profil développeur + IA / data"

Si tu veux une version qui insiste plus sur l'aspect IA / data / automatisation (pour coller au texte de la section), utilise plutôt :

```text
Create a modern, minimalistic "About" section illustration for a freelance full‑stack developer specialized in web apps, data and AI.

Visual layout:
- Main element: a large rounded corner red gradient card (from #dc2626 to #b91c1c), almost square.
- Center: abstract avatar icon of a developer (flat, no real face), with a neutral head-and-shoulders silhouette.
- Around the avatar inside the card: 2 or 3 subtle pictograms in outline style:
  - a small code window icon,
  - a simple data chart (line chart or bar chart),
  - a tiny neural network / brain outline for AI.
- All pictograms in light tones (white / very light pink) with low visual weight.

Global style:
- Background of the global image: white or very light gray, with maybe a very soft shadow under the red card.
- Clean composition: one main card, no extra panels or text.
- Flat / vector style, smooth shapes, no noise.

Technical details:
- Aspect ratio: 4:3 (e.g. 1600x1200) or square 1:1, to be cropped inside a right‑side column.
- Output as PNG or WebP, high resolution, ready to be named "about-section-hero".

Avoid:
- Overly busy dashboards or interfaces.
- Realistic people or faces.
- Strong secondary colors that break the red identity (stay mainly in reds + white / light gray).
```

## Intégration sur le site

1. Génère l'image dans ton outil (Midjourney, DALL‑E, etc.) avec un fond transparent ou plein, mais en gardant bien le grand bloc rouge comme élément principal.
2. Exporte en **WebP** et en **PNG** (pour compatibilité maximale).
3. Place les fichiers dans `assets/images/about-section-hero.webp` et `assets/images/about-section-hero.png`.
4. Vérifie le rendu sur la page d'accueil, section "À propos" (`index.html`), dans la colonne de droite.

