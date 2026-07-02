# Charte visuelle BD cartoon — DanielCraft

Document de référence pour images Open Graph, vidéos, réseaux sociaux et illustrations marketing.

## Résumé

Style **bande dessinée européenne (ligne claire)** : scènes plein cadre, personnages expressifs en interaction, bulles en français, ambiance chaleureuse et professionnelle pour artisans et commerces de Metz & Lorraine.

## Couleurs

- Fonds clairs : `#e8f6fc`, `#f3f4f6`
- Bleus marque : `#7bcde3`, `#4da9d6`, `#2f78a6`
- Encre / contours : `#0f3550`
- Accent CTA : `#dc2626`

## Images Open Graph (1200×630)

- Scène illustrative occupant tout le cadre
- Bandeau bas avec titre + sous-titre en blanc sur dégradé navy
- Badge rouge pour l’offre (« Audit gratuit », etc.)
- Lisible en miniature (test ~400 px de large)

## Vidéo

Réutiliser le même univers visuel :

- Personnages récurrents (consultant DanielCraft, artisan/client local)
- Décors : boutique, atelier, bureau avec écran montrant un site
- Transitions douces entre scènes type « avant / après visibilité Google »
- Sous-titres et titres en français, ton TPE (pas de jargon technique)

## Exemple de prompt (IA)

```
Open Graph banner 1200x630 pixels, landscape. European ligne claire comic illustration,
full-bleed immersive scene. Two expressive cartoon characters interacting [SCÈNE].
French speech bubble: "[PHRASE]". DanielCraft palette: sky blue #e8f6fc, primary #4da9d6,
navy ink #0f3550, red accent #dc2626. Bottom gradient scrim with bold white title
"[TITRE]" and subtitle "[SOUS-TITRE]". Warm Metz Lorraine small business context.
Not photorealistic, not flat corporate icons.
```

## Fichiers

| Type | Chemin |
|------|--------|
| Pages statiques | `assets/images/og/{slug}-1200x630.jpg` |
| Prestations | `assets/images/og/prestations/{slug}-1200x630.jpg` |
| Vitrines | `assets/images/og/vitrines/{slug}-1200x630.jpg` |
| Projets | `assets/images/og/projets/{slug}-1200x630.jpg` |
| Blog | `assets/images/og/blog-1200x630.jpg` + `assets/images/og/{article-slug}-1200x630.jpg` |

Après génération : `python build.py`.
