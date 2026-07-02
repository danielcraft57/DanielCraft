# Captures UX — backlog audit 2026

Branche `feature/ux-backlog-audit-2026` · juillet 2026.

## Viewports

| Dossier | Résolution | Notes |
|---------|------------|-------|
| `desktop/` | 1280×900 | Nav complète, CTA header visible |
| `tablet/` | 768×1024 | Menu burger (< 960 px), grilles 1–2 colonnes |
| `mobile/` | 390×844 | CTV multi-lignes, wizard pleine largeur |

## Fichiers (01 → 08)

| # | Fichier | URL | Points vérifiés |
|---|---------|-----|-----------------|
| 01 | accueil | `/` | CTV hero, 24 h, 3 démos desktop |
| 02 | nos-offres | `/nos-offres` | Comparatif Facebook, pack 1 190 € |
| 03 | contact | `/contact` | Wizard étape 1 |
| 04 | audit | `/audit` | CTA « 3 priorités… » |
| 05 | pro | `/pro` | Persona dev/SaaS |
| 06 | 404 | URL invalide | CTAs devis + audit |
| 07 | blog | `/blog/` | Bannière artisans, chips Metz/GEO |
| 08 | vitrine | `/vitrines/restauration/` | 42 € / 490 €, titre complet |

## Cohérence cross-viewport (juillet 2026)

| Critère | Desktop | Tablette | Mobile | Statut |
|---------|---------|----------|--------|--------|
| 24 h ouvrées (contact, audit, footer) | OK | OK | OK | OK |
| CTV longs lisibles (devis, audit) | OK | OK | OK (retour ligne) | OK |
| Menu burger < 960 px | — | OK | OK | OK |
| Comparatif Facebook empilé | 2 col | 1 col | 1 col | OK |
| Titre vitrine non tronqué | OK | OK | OK | OK corrigé build |
| aria-label sociaux | OK | OK | OK | OK corrigé |
| FAQ clavier (↑↓ Esc) | — | — | — | OK JS |

Témoignages exclus du périmètre.

## Lighthouse (accueil, mobile)

| Catégorie | Score | Fichier |
|-----------|-------|---------|
| Performance | 27 | `docs/lighthouse-mobile-home.json` |
| Accessibilité | 90 | idem |

Score perf bas en local (pas de cache CDN, images non optimisées au build dev). À re-mesurer en prod après déploiement.
