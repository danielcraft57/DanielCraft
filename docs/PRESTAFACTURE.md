# Prestafacture — API publique (notes DanielCraft)

Source : doc Prestafacture (2026). Prefixe : `/api/public/…`  
Auth : `Authorization: Bearer fact_…` (jetons dans Parametres → API — Jetons)  
Format : JSON UTF-8. Plan **Pro** (ou superieur) requis.

## Config locale

Variables dans `.env` (non versionne) :

```env
PRESTAFACTURE_API_BASE=https://prestafacture.com/api/public
PRESTAFACTURE_API_TOKEN=fact_…
```

Alternatives encore lues par `api/prestafacture-common.php` : `FACTURIO_API_BASE` / `FACTURIO_API_TOKEN` (legacy).

- Prod : `https://prestafacture.com/api/public`
- Dev : `http://localhost:3000/api/public` (backend) ou proxy Vite `http://localhost:5173/api`
- Rate limit : **60 req / IP / 15 min** sur `/api/public/*`

Test rapide :

```bash
curl -s -H "Authorization: Bearer $PRESTAFACTURE_API_TOKEN" \
  "https://prestafacture.com/api/public"
```

## Usage DanielCraft

| Flux | Endpoints | Scopes |
|------|-----------|--------|
| Devis prestations | `POST /devis`, `POST /devis/:id/send` (+ clients / produits SKU) | `clients.*`, `devis.*`, `produits.*` |
| Facture deja payee (Stripe audit / livres) | `POST /factures` (`paidExternally: true`) puis `POST /factures/:id/send` | `factures.read`, `factures.write`, `factures.send` |

Code PHP : `api/prestafacture-common.php`  
- `prestafacture_issue_audit_invoice` — facture PAID + email PDF  
- `prestafacture_issue_quote_devis` — devis + envoi  
- Avoirs : **pas dans l'API publique** (a creer dans l'UI) — voir section remboursement ci-dessous

## Parcours (ce qu'on peut / ne peut pas faire)

**Prestafacture ne remplace pas Stripe.** Ce n'est pas un PSP (pas de carte bancaire native dans l'API publique documentee). Role : catalogue, clients, **devis**, **factures** + envoi PDF.

| Parcours | Qui encaisse ? | Role Prestafacture | Chez DanielCraft |
|----------|----------------|--------------------|------------------|
| **A — Devis** | Plus tard (virement / Stripe / autre) | Creer + envoyer devis ; client accepte / refuse via page publique (`publicToken`) | Prestations (`prestafacture_issue_quote_devis`) |
| **B — Facture deja payee** | **Externe** (Stripe, Woo, virement…) | `paidExternally: true` → statut PAID → email PDF **sans** lien de paiement | Audit premium apres Stripe ; **livres PDF** apres Stripe |
| **C — Facture a payer** | Selon config Prestafacture (lien eventuel sur page `/public/invoices/:token`) | Creer facture **sans** `paidExternally`, puis `send` — le PDF peut inclure un **lien de paiement** cote app | **Non utilise** aujourd'hui (on force le parcours B apres Stripe) |

### Reponse courte : « on peut payer avec ? »

- **Payer la commande web (livres / audit)** : **oui via Stripe** sur danielcraft.fr, puis Prestafacture **enregistre** la facture payee (parcours B).
- **Payer « dans » Prestafacture** comme checkout e-commerce : **pas via l'API publique** documentee ; au mieux un lien sur une facture non payee (parcours C), a activer dans l'UI Prestafacture — ce n'est pas le flux recommande pour la boutique livres.

### Flux recommande boutique livres

```
Client paie Stripe Checkout
        |
        v
Webhook / retour success
        |
        +--> Prestafacture : POST /factures (paidExternally) + /send  (= justificatif PDF)
        |
        +--> DanielCraft : page `/livres/telechargement/` + code unique `DC-XXXX-XXXX`
```

**Code** : `api/stripe-livre-fulfillment.php`, `api/request-paid-livre.php`, `api/download-livre.php`, `api/livre-download-lookup.php`  
**Page UX** : `/livres/telechargement/` (`src/pages/livres-telechargement.html`)  
**Retour client** : Stripe success → page telechargement (fulfill + affichage code)  
**Webhook** : `api/stripe-webhook.php` (meme evenement `checkout.session.completed`, route livre via `product_type=livre_pdf`)

Variables optionnelles :

```env
LIVRE_PDF_DIR=/chemin/vers/livres-formation/pdf
LIVRE_DOWNLOAD_DIR=/var/lib/danielcraft/livre-tokens
LIVRE_DOWNLOAD_TTL_DAYS=30
LIVRE_DOWNLOAD_MAX_ATTEMPTS=5
LIVRE_DOWNLOAD_LOCK_HOURS=24
```

**Securite page telechargement** (`/livres/telechargement/`) :

| Mesure | Detail |
|--------|--------|
| Essais max | 5 codes incorrects / IP → blocage 24 h |
| Lock code | 12 essais sur un meme code → lock 24 h |
| Honeypot | champs `company` / `website` caches |
| Timing | min. 2 s entre chargement page et envoi |
| Rate soft | 30 lookups / 15 min / IP |
| Download | PDF uniquement via `token` (plus via `code=`) |
| Delai | 250–600 ms apres chaque echec |

### Distinction importante

| | Stripe | Prestafacture |
|--|--------|---------------|
| Encaissement CB | Oui | Non (API publique) |
| Facture comptable PDF | Non | Oui |
| Devis accepter/refuser | Non | Oui |
| Metadata commande (`livre_slug`, etc.) | Oui | Lignes descriptives |

## Paiement externe + email (parcours B — type e-commerce)

Cas : commande reglee ailleurs (Stripe, Woo…). Prestafacture enregistre la facture **payee** puis envoie le PDF.

1. `POST /api/public/factures` avec `paidExternally: true`, `clientEmail`, `lines[]`  
   - `taxRate` : `0.2` ou `20` (20 %)  
   - optionnel : `externalPaymentMethod`, `externalPaymentDate`, `clientName`, `currency`
2. Reponse : `id`, `status` PAID, `balance` 0  
3. `POST /api/public/factures/:id/send`  
   `{ "email": "…", "updateClientEmail": true }`  
   - Reponse : `emailSent`, `alreadyPaid: true` (PDF sans lien de paiement)

Exemple corps create :

```json
{
  "clientEmail": "client@boutique.fr",
  "clientName": "Client Boutique",
  "paidExternally": true,
  "externalPaymentMethod": "Stripe",
  "externalPaymentDate": "2026-05-22",
  "currency": "EUR",
  "lines": [
    {
      "description": "Commande #4521",
      "quantity": 1,
      "unitPrice": 149.99,
      "taxRate": 0.2
    }
  ]
}
```

## Clients

- `GET /clients?page=&pageSize=&search=`
- `POST /clients` — `{ name, email, countryCode, isCompany? }` — email existant → client reutilise
- `PATCH` / `DELETE` `/clients/:id`

## Produits

- `GET /produits?search=&kind=`
- `GET /produits/sku/:sku` — SKU exact
- `POST /produits` — `name`, `sku`, `unitPrice`, `kind`, `techStack`, `details` / `livrables`
- Visuel omis → icon-gradient ou `library:…` aleatoire
- Catalogue livrables : `GET /produits/livrables/catalog?q=`

## Devis

`clientId` = **string** (ex. `"kl644kqh8r"`), pas un entier.

Lignes — un seul mode par ligne :

1. Manuelle : `description` + `unitPrice` + `quantity` (+ `taxRate`)
2. Catalogue : `productId` seul (+ `quantity`)
3. Get-or-create SKU : `productSku` + `description`/`productName` + `unitPrice` a la 1re occurrence

Ne pas combiner `productId` et `productSku` sur la meme ligne.

Envoi : `POST /devis/:id/send` — PDF + liens accepter / refuser (`publicToken`).

## Import catalogue

- Preferer session JWT `POST /api/products` pour un import massif (hors rate limit public)
- Via API publique : espacer les `POST /produits`
- Avant creation : `GET /produits?search=MON-SKU`

## Remboursement Stripe + avoir Prestafacture

Deux systemes distincts : Stripe rend l'argent, Prestafacture corrige la compta.

**Stripe** (encaissement) — helper `stripe_refund_payment_intent()` dans `api/stripe-common.php`, script :

```bash
python scripts/stripe_refund.py --session cs_live_xxx --env .env.prod
python scripts/stripe_refund.py --payment-intent pi_xxx --env .env.prod
```

Raisons Stripe : `requested_by_customer` (defaut), `duplicate`, `fraudulent`. Pas d'endpoint HTTP public.

**Prestafacture** (facture PDF) — l'API publique (`GET /api/public`) n'expose que `clients`, `produits`, `factures`, `devis`. **Pas de ressource avoirs** (`POST /avoirs`, `/factures/:id/avoir` → 404). Un `POST /factures` avec `type: AVOIR` cree une **nouvelle facture PAID**, pas un avoir.

Les factures ont un champ `appliedAvoirs` : les avoirs existent dans l'app, pas dans l'API Bearer. Apres un refund Stripe : ouvrir la facture dans Prestafacture → **creer un avoir** a la main, puis l'envoyer au client si besoin.

## Pages publiques (hors jeton API)

`/public/invoices/:token`, etc. — distinctes de l'API Bearer.

## SSE (app web)

`GET /api/realtime/stream` — session JWT, hors jeton API. Un produit cree/modifie via API rafraichit le catalogue cote UI.
