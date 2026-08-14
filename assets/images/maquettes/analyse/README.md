# Maquettes `/analyse` - produit d'appel

References design (pas servies en live). Cible : page **rapport** ouverte via lien email ProspectLab, pas un outil libre mis en nav.

## Role

Lien type :

`https://danielcraft.fr/analyse?website=https://site-du-prospect.fr&full=1`

(+ `email` / `name` optionnels pour prefill du formulaire lead)

Le prospect voit ses scores, puis convertit (clics) via :

1. **Recevoir l'audit** - formulaire pre-rempli (lead)
2. **Audit premium** - CTA fort, **sans prix** sur cette page
3. **Bandeau offres** - 2 a 4 prestations cliquables
4. **Offre speciale** - 1 tuile mise en avant selon le pire score

## Persistance des donnees (etat actuel)

Pas de session navigateur / PHP dediee sur `/analyse`.

| Couche | Existe | N'existe pas |
|--------|--------|--------------|
| ProspectLab | Rapport stocke cote API, relu via `website` | - |
| Proxy `api/website-analysis.php` | GET + rate-limit IP | Session user, ecriture lead |
| Front `analyse-report.js` | URL partageable `?website=&full=` | `sessionStorage` / `localStorage` du rapport |
| Clics offres | - | Tracking clic / session parcours |

Vague code suivante : poster le lead (ex. `request-free-audit.php`), UTM / event sur clics fiches. Les donnees d'analyse restent la source de verite ProspectLab.

## Regle prix

**Aucun prix visible** sur `/analyse` ni sur ces maquettes (ni premium, ni prestations). CTAs : « Recevoir l'audit », « Demander l'audit premium », « Voir l'offre ». Tarifs sur `/audit` et fiches `/prestations/...`.

## Composition desktop XL (~1440-1600 px)

1. Header leger DanielCraft + « Rapport d'analyse »
2. Identite prospect (nom / URL / date)
3. 4 scores anneaux : Performance, SEO, Securite, Risque (langage client)
4. Capture site + 3-4 points cles (bon / moyen / faible)
5. **Bandeau conversion** (2 colonnes) :
   - A : Recevoir l'audit (email, nom, site pre-remplis) + CTA
   - B : Audit premium (perks courts) + CTA sans prix
6. **Bandeau offres** (grille 3-4 tuiles) :
   - Titre « Pour aller plus loin » / « Offres adaptees a votre site »
   - Tuile speciale avec ribbon « Offre speciale pour vous »

### Mapping score -> offre speciale (indicatif)

| Score faible | Offre mise en avant |
|--------------|---------------------|
| Performance | Site trop lent / alléger le site |
| SEO | Etre trouve / visibilite locale |
| Securite / Risque | Securiser le site |
| Message / conversion | Vitrine claire / contact |

## Responsive

- **Mobile** : scores 2x2, capture pleine largeur, form puis premium en stack, offres en liste / carrousel
- **Tablette** : scores + capture cote a cote, conversion empilee, offres 2x2

## Fichiers maquettes

| Fichier | Role |
|---------|------|
| `analyse-xl-rapport-cta.png` (+ `.webp`) | Page complete XL (rapport + conversion + bandeau offres + speciale) |
| `analyse-xl-conversion-band.png` (+ `.webp`) | Zoom form Recevoir l'audit + Audit premium |
| `analyse-mobile-rapport.png` (+ `.webp`) | Variante mobile stack |

Prompts : [`PROMPTS.md`](PROMPTS.md).

## Style

Aligné pages recentes (`/audit`) + rule visuelle technique premium : fond `#f5f7fb` → `#e9eef6`, encre `#0f172a`, accent CTA `#dc2626`, anneaux de scores, pas de cartoon.
