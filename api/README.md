# API formulaire de contact

Le dossier `api/` contient le script PHP d'envoi du formulaire de contact.

- **Endpoint :** `POST /api/send-contact.php`
- **Données :** `name`, `email`, `phone`, `service`, `budget`, `message` (form-data)
- **Réponse :** JSON `{ "success": true }` ou `{ "success": false, "error": "..." }`

Le script envoie un email à `contact@danielcraft.fr` via `mail()`. Sur le serveur, Nginx exécute les `.php` avec PHP 8.2-FPM (voir `scripts/nginx.conf`, socket `php8.2-fpm.sock`).

## Test en local

- **`python -m http.server`** : ne traite pas le PHP ; un `POST` vers `/api/send-contact.php` peut renvoyer **501** ou **405**. Utilisez plutôt le serveur intégré PHP depuis la racine du site :
  - `php -S 127.0.0.1:8000 -t dist`
- Puis ouvrez `http://127.0.0.1:8000/` (ou le dossier `dist/` selon votre flux de build).

## Stripe (paiement fiches vitrine)

Variables dans `.env` (voir `.env.example`) :

- `STRIPE_PUBLISHABLE_KEY` — clé publique (`pk_live_…` ou `pk_test_…`)
- `STRIPE_SECRET_KEY` — clé secrète (`sk_live_…` ou `sk_test_…`)

Endpoints :

- `POST /api/stripe-create-checkout.php` — corps JSON `{ "vitrine_slug": "restauration", "email": "optionnel" }` → `{ "success": true, "url": "https://checkout.stripe.com/…" }`
- `GET /api/stripe-test.php` — test API (optionnel : `?key=` si `STRIPE_TEST_KEY` est défini)

Scripts (depuis la racine du repo) :

```bash
python scripts/merge_stripe_env.py   # après export des clés dans l’environnement
python scripts/stripe_test.py
python scripts/stripe_test.py --checkout
python scripts/stripe_sync_vitrines.py   # crée des Payment Links et met à jour src/data/vitrines.json
```

Le catalogue est copié vers `api/data/vitrines.json` à chaque `python build.py`.

## Devis prestations (Facturio)

- `POST /api/request-prestation-devis.php` — corps `name`, `email`, `phone`, `company`, `message`, `prestation_slug`, `service_slug`, `total_eur`, `addon_id[]` (optionnel)
- Réponse : `{ "success": true, "message": "...", "quote_id": "..." }`
- Flux serveur : `POST https://facturio.danielcraft.fr/api/public/devis` puis `POST …/devis/:id/send`
- Variables `.env` : `FACTURIO_API_BASE`, `FACTURIO_API_TOKEN` (jeton `fact_…`)
- **Scopes jeton** (Facturio → Paramètres → API — Jetons) :
  - Devis catalogue : `clients.read`, `clients.write`, `devis.read`, `devis.write`, `devis.send`, `produits.read`, `produits.write`
  - Facture audit Stripe : `factures.read`, `factures.write`, `factures.send`
- **Flux devis** : recherche/création client (`/clients`) puis `POST /devis` avec `clientId` (pas `clientEmail` seul).
- Les lignes de devis référencent le catalogue Facturio via `productId` (`facturio_product_id` dans `prestations.json`).
- Les prix catalogue sont **HT** ; la TVA 20 % est ajoutée dans Facturio via `taxRate: 0.2`.

Sync catalogue → produits Facturio (écrit `facturio_sku` + `facturio_product_id` dans `src/data/prestations.json`).
Payload complet : `description`, `livrables[]`, `techStack` (`languages`, `ai`), métadonnées visuelles.

```bash
python scripts/facturio_sync_prestations.py --dry-run --slug site-vitrine
python scripts/facturio_sync_prestations.py --full          # PATCH complet (produits existants)
python scripts/facturio_sync_prestations.py --recreate      # DELETE + POST complet (catalogue UI)
python build.py
```

Test rapide (depuis la racine du repo, lit `.env`) :

```bash
python scripts/facturio_test.py
python scripts/facturio_test.py --devis
```

Le catalogue prestations est copié vers `api/data/prestations.json` à chaque `python build.py`.

**Dev local :** `.\scripts\serve_dev.ps1` (build + PHP + `dist/router.php` + watch). Voir `README.md`.
