# Prompts — illustration « À propos » (`about-section-hero`)

L’image à droite du bloc **« Passionné par l’excellence technique »** doit refléter : **Full-Stack (JS/TS, Python, PHP, React, Node)**, **apps performantes**, **automatisation**, **IA**, **7+ ans**, **qualité & tests (SOLID, Jest, TDD)**, **agile / CI/CD**, **collaboration** — sans visage photo, sans logos de marques (pas de logo React officiel, etc.).

> **Note** : le rendu généré par `scripts/rasterize_about_hero.py` (à partir du SVG) reste **fonctionnel mais volontairement simple**. Pour un visuel **plus soigné et mémorable**, exporte depuis une IA avec l’un des prompts ci-dessous, puis remplace `about-section-hero.png` / `.webp` (mêmes noms de fichiers).

**Régénération technique (placeholder)** :

```bash
python scripts/rasterize_about_hero.py
python scripts/rasterize_about_hero.py --size 1600
```

**Source vectorielle** : `assets/images/about-section-hero.svg` (composition de base ; à mettre à jour si tu changes fortement le design).

---

## Charte commune (tous prompts)

- **Palette** : bleus DanielCraft — dégradé `#7bcde3` → `#4da9d6` → `#2f78a6`, touches `#0f3550` pour le contraste ; fond global très clair `#f3f4f6` ou `#f9fafb`.
- **Format** : carré **1:1** (ex. **1200×1200** ou **1600×1600**), carte centrale aux coins arrondis, ombre douce.
- **Style** : illustration **vectorielle / flat premium**, lignes nettes, peu d’éléments, pas de bruit ni de texture « photo ».
- **Interdits** : visages réalistes, texte lisible, watermarks, logos trademarkés, esthétique « clipart années 2000 », 3D cheap, dominante rouge/orange.

**Negative prompt (à coller en complément si l’outil le permet)** :

```text
photorealistic face, human eyes, readable text, logos, WordPress icon, stock photo, messy UI screenshot, neon cyberpunk overload, low resolution, jpeg artifacts, red dominant, cluttered dashboard
```

---

## A — « Excellence technique » + architecture / modularité

**Alignement texte** : *excellence technique*, *architecture modulaire*, *bonnes pratiques*.

```text
Square 1:1 editorial illustration for a senior full-stack developer "About" section. One large rounded card with a refined blue gradient (#7bcde3 to #2f78a6). Inside: abstract layered panels or stacked translucent rectangles suggesting modular architecture — clean geometry, generous whitespace, subtle depth via soft shadows only. A few thin orthogonal lines hinting at structure, no readable code. Premium flat vector, calm and confident, not cute. Light gray #f3f4f6 canvas around the card. No people, no logos.
```

---

## B — « Code de qualité » + tests (Jest, TDD) sans texte

**Alignement texte** : *SOLID*, *tests automatisés*, *Jest*, *TDD*.

```text
1:1 minimal illustration: rounded blue gradient card on pale gray background. Visual metaphor for automated testing: a small abstract "module" cube or chip connected by a thin line to a grid of tiny dots or a faint check-rhythm pattern (like test cases), all monochrome white and pale cyan on the blue card. Suggest precision and rigor, not a literal checklist with letters. Flat vector, high-end SaaS marketing aesthetic. No faces, no brand icons, no readable words.
```

---

## C — « Apps performantes » + automatisation + IA (abstrait)

**Alignement texte** : *applications performantes*, *outils d’automatisation*, *solutions basées sur l’IA*.

```text
Square illustration for a developer portfolio About column. Central rounded card, blue-teal gradient. Abstract motif combining: (1) three or four softly glowing nodes linked by fine curves suggesting a light neural / data graph, very subtle; (2) a horizontal "pipeline" of small circles implying automation flow — ultra light, low contrast white lines. Convey speed and intelligence without robots or brains. Modern flat vector, Apple-like restraint. Background #f3f4f6. No text, no logos, no photorealism.
```

---

## D — « Livraison rapide » + agile / CI/CD (métaphore douce)

**Alignement texte** : *Scrum*, *cycles courts*, *déploiements continus*, *CI/CD*.

```text
1:1 abstract illustration, professional tech portfolio. Large rounded rectangle with blue gradient. Inside, suggest continuous delivery with minimal shapes: a gentle loop or two curved arrows forming an almost-complete cycle (very abstract, not a literal Agile diagram), plus 2–3 small horizontal "stage" bars like a simplified pipeline. All elements flat, white or ice-blue on the gradient. Feeling: rhythm, iteration, reliability — not chaos, not comic. No characters, no icons of specific CI tools, no text.
```

---

## E — « Collaboration » + besoins métier (sans personnages réalistes)

**Alignement texte** : *communication claire*, *travail en équipe*, *adaptation aux besoins métier*.

```text
Square 1:1 illustration for B2B freelance developer About section. Rounded blue gradient card on light gray. Abstract collaboration metaphor: two soft rounded speech-bubble shapes or overlapping translucent panels converging toward a central point — geometric, friendly but serious. Optional single thin link line between shapes. Palette strictly cool blues and white. Flat vector, plenty of breathing room. No realistic people, no handshake photos, no logos, no text.
```

---

## F — « Full-Stack » (couches front / API / données) — géométrie seule

**Alignement texte** : *JavaScript/TypeScript, Python, PHP*, *React*, *Node* — **en abstraction** (pas d’icônes de frameworks).

```text
1:1 premium flat illustration. A tall-ish rounded card (still fits square canvas) with blue gradient. Three horizontal "bands" or floating layers (top lighter, bottom slightly darker navy accent) connected by two or three vertical hairline connectors suggesting full-stack stack: presentation, logic, data — purely abstract rectangles and lines. Subtle dot grid in the background of the card at 5% opacity. Crisp edges, vector-like. No logos, no readable code, no faces. Background #f3f4f6.
```

---

## Variante courte (modèles qui préfèrent peu de tokens)

```text
Minimal square About illustration, blue gradient rounded card, abstract developer excellence: modular shapes + subtle pipeline or nodes, white/cyan accents, light gray background, flat vector, no text, no faces, no logos, high-end SaaS style.
```

---

## Essais déjà générés (Cursor / même charte)

Fichiers dans `assets/images/` (recadrage carré 1200×1200 pour le hero actif) :

| Fichier | Prompt doc | Idée |
|--------|----------------|------|
| `about-section-hero-trial-a.png` | **A** — Excellence / architecture | Grille type « bento », calme, très pro |
| `about-section-hero-trial-c.png` | **C** — Perf / auto / IA | Nœuds reliés + pipeline discret |
| `about-section-hero-trial-f.png` | **F** — Full-stack couches | Trois plans reliés (UI / logique / data), style glass léger |

Par défaut le site utilise **`about-section-hero.png` / `.webp`** générés par **`scripts/rasterize_about_hero.py`** à partir de **`about-section-hero.svg`** (silhouette professionnel + écran simplifié, charte bleu DanielCraft). Les fichiers `about-section-hero-trial-*.png` restent des essais IA optionnels (gitignorés).

---

## Après génération

1. Recadrer si besoin en **carré strict**, vérifier la netteté sur fond blanc de la page.
2. Exporter **`about-section-hero.webp`** (qualité ~85–90) + **`about-section-hero.png`** dans `assets/images/`.
3. Optionnel : mettre à jour `about-section-hero.svg` à la main ou ignorer le SVG si tu ne relies plus le script Pillow à cette composition.
4. `python build.py` (ou ton déploiement) puis contrôle visuel section « À propos ».
