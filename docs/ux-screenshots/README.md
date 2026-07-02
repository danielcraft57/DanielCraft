# Captures UX — audit 2026

Captures de contrôle visuel (non versionnées — régénérer en local si besoin).

## Viewports

| Dossier | Résolution | Préfixe fichiers | Notes |
|---------|------------|------------------|-------|
| `desktop/` | 1280×900 | `d01` … `d08` | Nav complète, CTA header visible |
| `tablet/` | 768×1024 | `t01` … `t08` | Menu burger (< 960 px), grilles 1–2 colonnes |
| `mobile/` | 390×844 | `m01` … `m08` | CTV multi-lignes, wizard pleine largeur |

## Pages (01 → 08)

| # | Slug | URL | Points vérifiés |
|---|------|-----|-----------------|
| 01 | accueil | `/` | CTV hero, 24 h, 3 démos desktop |
| 02 | nos-offres | `/nos-offres` | Comparatif Facebook, pack 1 190 € |
| 03 | contact | `/contact` | Wizard étape 1 |
| 04 | audit | `/audit` | CTA « 3 priorités… » |
| 05 | pro | `/pro` | Persona dev/SaaS |
| 06 | 404 | URL invalide | CTAs devis + audit |
| 07 | blog | `/blog/` | Bannière artisans, chips Metz/GEO |
| 08 | vitrine | `/vitrines/restauration/` | 42 € / 490 €, titre complet |

Exemple de nom : `desktop/d01-accueil.png`, `mobile/m04-audit.png`.

## Cohérence cross-viewport (juillet 2026)

| Critère | Desktop | Tablette | Mobile | Statut |
|---------|---------|----------|--------|--------|
| 24 h ouvrées (contact, audit, footer) | OK | OK | OK | OK |
| CTV longs lisibles (devis, audit) | OK | OK | OK (retour ligne) | OK |
| Menu burger < 960 px | — | OK | OK | OK |
| Comparatif Facebook empilé | 2 col | 1 col | 1 col | OK |
| Titre vitrine non tronqué | OK | OK | OK | OK |
| aria-label sociaux | OK | OK | OK | OK |
| FAQ clavier (↑↓ Esc) | — | — | — | OK JS |

Témoignages exclus du périmètre.

## Lighthouse (accueil, mobile, local)

| Catégorie | Score |
|-----------|-------|
| Performance | 27 |
| Accessibilité | 90 |

Rapport JSON : `docs/lighthouse-mobile-home.json` (gitignoré). Score perf bas en local (pas de cache CDN). À re-mesurer en prod après déploiement.

```powershell
npx lighthouse http://127.0.0.1:8000/ --only-categories=performance,accessibility --form-factor=mobile --screenEmulation.mobile --output=json --output-path=docs/lighthouse-mobile-home.json
```
