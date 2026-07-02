# Parcours client — devis → appel → livraison

Document de référence (backlog P3) pour l’alignement UX, emails et support.

## Vue d’ensemble

```mermaid
flowchart LR
  A[Visite site] --> B{Besoin clair ?}
  B -->|Oui| C[Devis PDF / contact]
  B -->|Non| D[Wizard 5 étapes]
  C --> E[Email confirmation]
  D --> E
  E --> F[Appel sous 24 h ouvrées]
  F --> G[Validation devis]
  G --> H[Livraison 5-8 j]
  H --> I[Support 14 j]
  I --> J[Suivi mensuel valeur]
```

## Les 5 étapes (côté client)

| Étape | Moment | Ce que voit le client | Canal |
|-------|--------|-------------------------|-------|
| 1. Découverte | J0 | Hero CTV, `/nos-offres`, fiche vitrine 42 € / 490 € | Site |
| 2. Demande | J0 | Wizard contact ou modale devis PDF (< 2 min) | Site + email auto |
| 3. Échange | J0–J1 | Rappel téléphone / visio, devis affiné | Téléphone, email |
| 4. Livraison | J+5 à J+8 | Mise en ligne, handover, support 14 j | Email + accès site |
| 5. Fidélisation | M+1… | Email valeur prouvée (stats, conseils) | Email mensuel |

## Points de contact automatisés

| Déclencheur | Fichier / zone | Message clé |
|-------------|----------------|-------------|
| Devis PDF demandé | `api/devis-notification.php` | PDF + « Voici les 24 h suivantes » |
| Audit gratuit | `api/request-free-audit.php` | 3 priorités sous 48 h ouvrées |
| Erreur formulaire | Overlay contact / modale devis | CTA téléphone + `/contact` |
| Post-livraison (M+1) | `api/post-livraison-email.php` | Rappel support + valeur mesurable |

## SLA affichés sur le site

- **Réponse humaine** : 24 h ouvrées (contact, devis, rappel)
- **Audit gratuit** : rapport sous 48 h ouvrées
- **Vitrine standard** : 5–8 jours ouvrés après validation
- **Support** : 14 jours inclus post-livraison

## Pages du parcours

1. `/` — orientation (hero + 3 offres)
2. `/nos-offres` — comparatif et pack recommandé
3. `/contact` — wizard situation → offre → coordonnées
4. `/prestations/{slug}/` — détail + modale devis
5. `/vitrines/{metier}/` — achat modèle ou sur mesure
6. `/audit` — entrée diagnostic gratuit
