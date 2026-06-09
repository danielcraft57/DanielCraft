#!/usr/bin/env python3
"""
Synchronise prestations.json vers Facturio /produits (payload catalogue complet).

Champs synchronises : name, sku, unitPrice, category, purpose, visualType, iconName,
description, **livrables[]** (`livrable`, `montant`, `heures`), **techStack** (`languages`, `ai`).

Usage:
  python scripts/facturio_sync_prestations.py
  python scripts/facturio_sync_prestations.py --full          # PATCH complet (sans supprimer)
  python scripts/facturio_sync_prestations.py --recreate    # DELETE + POST complet
  python scripts/facturio_sync_prestations.py --slug site-vitrine --recreate
  python scripts/facturio_sync_prestations.py --dry-run --recreate
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

from facturio_product_payload import build_rich_product_body, livrables_summary

ROOT = Path(__file__).resolve().parents[1]
PRESTATIONS_JSON = ROOT / "src" / "data" / "prestations.json"

SERVICE_SLUG_TO_SKU: dict[str, str] = {
    "pack_vitrine": "SITE-VITRINE",
    "pack_identite": "IDENTITE-MULTI",
    "pack_seo_complet": "PACK-SEO-GOOGLE-CHATGPT",
    "seo_basique_290": "SEO-BASIQUE",
    "seo_chatgpt_490": "SEO-CHATGPT",
    "ia_faq_site": "IA-FAQ-SITE",
    "ia_support_client": "IA-SUPPORT-EMAIL",
    "maint_site_mensuel": "MAINT-MENSUEL",
    "ia_contenu_web": "IA-CONTENUS-WEB",
    "ia_redaction_pro": "IA-REDACTION-COMMERCIALE",
    "ia_analyse_donnees": "IA-ANALYSE-DONNEES",
    "ia_chatbot_ecom": "IA-CHATBOT-ECOMMERCE",
    "ia_automatisation": "IA-AUTOMATISATION-TACHES",
    "ia_abo_mensuel": "IA-MAINTENANCE-MENSUEL",
    "ia_evolution": "IA-EVOLUTION-FEATURE",
    "ia_audit": "IA-AUDIT-USAGE",
    "tech_conseil_archi": "CONSEIL-ARCHI",
    "tech_integration_crm": "INTEG-CRM",
    "tech_migration_donnees": "MIGRATION-DONNEES",
    "tech_api_webhook": "INTEG-API",
    "tech_perf_rapport": "RAPPORT-PERF",
    "site_page_supp": "PAGE-SUPP",
    "site_form_avance": "FORM-AVANCE",
    "site_refonte_visuelle": "REFONTE-LEGERE",
    "site_maj_contenu_5h": "MAJ-CONTENU-5H",
    "maint_hebergement": "HEBERG-DOMAIN",
    "maint_backup": "BACKUP-SECU",
    "maint_ssl": "SSL-CONFIG",
    "maint_support_abo": "SUPPORT-ABO",
    "maint_depannage_2h": "DEPANNAGE-2H",
    "maint_accompagnement_h": "ACCOMP-H",
    "maint_support_prio_h": "SUPPORT-H",
}

ADDON_ID_TO_SKU: dict[str, str] = {
    "page_extra": "PAGE-SUPP",
    "form_advanced": "FORM-AVANCE",
    "maint_ia": "IA-MAINTENANCE-MENSUEL",
}


def load_env() -> None:
    import os

    env_path = ROOT / ".env"
    if not env_path.is_file():
        return
    for raw in env_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, val = line.split("=", 1)
        val = val.strip().strip('"').strip("'")
        os.environ.setdefault(key.strip(), val)


def api_request(method: str, path: str, body: dict | None = None) -> tuple[int, dict | str]:
    import os
    import urllib.error
    import urllib.request

    base = os.environ.get("FACTURIO_API_BASE", "").rstrip("/")
    token = os.environ.get("FACTURIO_API_TOKEN", "").strip()
    if not base or not token:
        print("FACTURIO_API_BASE ou FACTURIO_API_TOKEN manquant dans .env", file=sys.stderr)
        sys.exit(1)
    url = base + ("/" + path.lstrip("/") if path else "")
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json; charset=utf-8",
    }
    data = None
    if body is not None:
        headers["Content-Type"] = "application/json; charset=utf-8"
        data = json.dumps(body, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method=method.upper())

    last_status = 0
    last_data: dict | str = ""
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=25) as resp:
                raw = resp.read().decode("utf-8", errors="replace")
                try:
                    return resp.status, json.loads(raw)
                except json.JSONDecodeError:
                    return resp.status, raw
        except urllib.error.HTTPError as e:
            raw = e.read().decode("utf-8", errors="replace")
            try:
                last_status, last_data = e.code, json.loads(raw)
            except json.JSONDecodeError:
                last_status, last_data = e.code, raw
            if e.code == 429 and attempt < 3:
                wait = 5 * (2 ** attempt)
                print(f"    [429] pause {wait}s...", file=sys.stderr)
                time.sleep(wait)
                continue
            return last_status, last_data
        except OSError as e:
            if attempt < 3:
                wait = 2 ** attempt
                print(f"    [reseau] {e} — pause {wait}s...", file=sys.stderr)
                time.sleep(wait)
                continue
            raise
    return last_status, last_data


class ProductCatalog:
    def __init__(self) -> None:
        self.by_sku: dict[str, dict] = {}

    def load(self) -> None:
        page = 1
        while True:
            status, data = api_request("GET", f"/produits?page={page}&pageSize=100")
            if status == 401:
                raise RuntimeError(
                    "Jeton Facturio invalide (401). Regenerez fact_… dans Parametres → API."
                )
            if status == 429:
                raise RuntimeError("Rate limit Facturio (429). Attendez 1-2 minutes.")
            if status != 200 or not isinstance(data, dict):
                msg = data.get("message", data) if isinstance(data, dict) else data
                raise RuntimeError(f"GET /produits page {page}: HTTP {status} — {msg}")
            items = data.get("items") or []
            if not isinstance(items, list):
                break
            for item in items:
                if not isinstance(item, dict):
                    continue
                sku = (item.get("sku") or "").strip().upper()
                if sku:
                    self.by_sku[sku] = item
            if len(items) < 100:
                break
            page += 1
            time.sleep(0.5)

    def get(self, sku: str) -> dict | None:
        return self.by_sku.get(sku.upper())


def recreate_delete_all(catalog: ProductCatalog, skus: set[str], dry_run: bool) -> int:
    ok = 0
    for sku in sorted(skus):
        existing = catalog.get(sku)
        if not existing:
            continue
        pid = int(existing["id"])
        if dry_run:
            print(f"  [dry-run] DELETE {sku} id={pid}")
            ok += 1
            continue
        status, data = api_request("DELETE", f"/produits/{pid}")
        if status >= 300:
            msg = data.get("message", data) if isinstance(data, dict) else data
            print(f"  [ERREUR] DELETE {sku} id={pid}: HTTP {status} - {msg}", file=sys.stderr)
            continue
        print(f"  supprime {sku} id={pid}")
        catalog.by_sku.pop(sku.upper(), None)
        ok += 1
        time.sleep(1.0)
    return ok


def upsert_product(
    catalog: ProductCatalog,
    sku: str,
    body: dict,
    dry_run: bool,
    mode: str,
) -> tuple[int | None, str]:
    if mode == "recreate":
        existing = catalog.get(sku)
        if existing:
            return int(existing["id"]), "recree"

    existing = catalog.get(sku)
    if existing and mode in ("skip", "patch", "patch_price"):
        pid = int(existing["id"])
        if mode == "skip":
            return pid, "existant"
        if dry_run:
            return pid, "patch (dry-run)"
        patch_body = body if mode == "patch" else {
            "unitPrice": body["unitPrice"],
            "name": body["name"],
        }
        status, patched = api_request("PATCH", f"/produits/{pid}", patch_body)
        if status >= 300:
            msg = patched.get("message", patched) if isinstance(patched, dict) else patched
            print(f"    [ERREUR] PATCH {sku}: HTTP {status} - {msg}", file=sys.stderr)
            return None, "echec patch"
        catalog.by_sku[sku.upper()] = {**existing, **patch_body}
        return pid, "mis a jour"

    if dry_run:
        return None, "creer (dry-run)"

    status, created = api_request("POST", "/produits", body)
    if status not in (200, 201) or not isinstance(created, dict) or "id" not in created:
        msg = created.get("message", created) if isinstance(created, dict) else created
        print(f"    [ERREUR] POST /produits {sku}: HTTP {status} - {msg}", file=sys.stderr)
        return None, "echec"
    catalog.by_sku[sku.upper()] = created
    time.sleep(1.0)
    return int(created["id"]), "recree" if mode == "recreate" else "cree"


def resolve_sku(entry: dict, *, is_addon: bool) -> str:
    explicit = (entry.get("facturio_sku") or "").strip()
    if explicit:
        return explicit.upper()
    if is_addon:
        aid = (entry.get("id") or "").strip()
        return ADDON_ID_TO_SKU.get(aid, "")
    service = (entry.get("service_slug") or "").strip()
    return SERVICE_SLUG_TO_SKU.get(service, "")


def sync_entry(
    catalog: ProductCatalog,
    label: str,
    entry: dict,
    sku: str,
    parent: dict | None,
    slug: str,
    dry_run: bool,
    update_prices: bool,
    full_update: bool,
    recreate: bool,
) -> bool:
    if not sku:
        print(f"  - {label}: pas de SKU mappe")
        return False

    title = (entry.get("title") or label).strip()
    try:
        price = int(entry.get("price_eur") or 0)
    except (TypeError, ValueError):
        price = 0

    body = build_rich_product_body(entry, sku, title, price, parent, slug=slug)
    livrables = body.get("livrables") or []
    tech = body.get("techStack") or {}
    langs = ", ".join(tech.get("languages") or [])
    ai = ", ".join(tech.get("ai") or [])

    print(f"  - {label} -> {sku} ({price} EUR HT)")
    print(f"    {livrables_summary(livrables)}")
    if langs:
        print(f"    techStack.languages: {langs}")
    if ai:
        print(f"    techStack.ai: {ai}")

    if recreate:
        mode = "recreate"
    elif full_update:
        mode = "patch"
    elif update_prices:
        mode = "patch_price"
    elif dry_run:
        mode = "recreate"  # simule creation
    else:
        mode = "skip"

    pid, action = upsert_product(catalog, sku, body, dry_run, mode)
    entry["facturio_sku"] = sku
    if pid is not None:
        entry["facturio_product_id"] = pid
        print(f"    id={pid} ({action})")
        return True
    if dry_run:
        entry.pop("facturio_product_id", None)
        print(f"    ({action})")
    return dry_run


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync prestations.json -> Facturio produits (complet)")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--slug", help="Une seule prestation (slug)")
    parser.add_argument("--update-prices", action="store_true", help="PATCH prix + nom uniquement")
    parser.add_argument(
        "--full",
        action="store_true",
        help="PATCH tous les champs catalogue sur produits existants",
    )
    parser.add_argument(
        "--recreate",
        action="store_true",
        help="DELETE chaque SKU puis POST payload complet",
    )
    args = parser.parse_args()

    if not PRESTATIONS_JSON.is_file():
        print(f"[ERREUR] {PRESTATIONS_JSON} introuvable", file=sys.stderr)
        return 1

    load_env()
    catalog = ProductCatalog()
    if not args.dry_run:
        print("Chargement catalogue Facturio (/produits)...")
        try:
            catalog.load()
        except RuntimeError as e:
            print(f"[ERREUR] {e}", file=sys.stderr)
            return 1
        print(f"  {len(catalog.by_sku)} produit(s) indexes\n")
    else:
        print("[dry-run] Pas d'appel API (apercu payload uniquement)\n")

    data = json.loads(PRESTATIONS_JSON.read_text(encoding="utf-8"))
    touched = 0
    failures = 0
    work: list[tuple[str, dict, str, dict | None, str]] = []

    for item in data.get("items") or []:
        if not isinstance(item, dict):
            continue
        slug = (item.get("slug") or "").strip()
        if args.slug and slug != args.slug:
            continue
        sku = resolve_sku(item, is_addon=False)
        if sku:
            work.append((slug or item.get("title", "?"), item, sku, None, slug))
        addons = item.get("addons") or []
        if isinstance(addons, list):
            for addon in addons:
                if not isinstance(addon, dict):
                    continue
                aid = (addon.get("id") or "").strip()
                addon_label = f"{slug}/{aid}" if slug else aid
                addon_sku = resolve_sku(addon, is_addon=True)
                if addon_sku:
                    work.append((addon_label, addon, addon_sku, item, slug))

    if args.recreate and work:
        unique_skus = {sku for _, _, sku, _, _ in work}
        print(f"Suppression de {len(unique_skus)} SKU(s) DanielCraft...")
        recreate_delete_all(catalog, unique_skus, args.dry_run)
        print()

    for label, entry, sku, parent, slug in work:
        try:
            if sync_entry(
                catalog, label, entry, sku, parent, slug,
                args.dry_run, args.update_prices, args.full, args.recreate,
            ):
                touched += 1
            else:
                failures += 1
        except OSError as e:
            print(f"  [ERREUR] {label}: {e}", file=sys.stderr)
            failures += 1

    if args.dry_run:
        print(f"\n[dry-run] {touched} entree(s)")
        if work:
            label, entry, sku, parent, slug = work[0]
            title = (entry.get("title") or label).strip()
            price = int(entry.get("price_eur") or 0)
            sample = build_rich_product_body(entry, sku, title, price, parent, slug=slug)
            print("\nExemple payload JSON :")
            print(json.dumps(sample, ensure_ascii=False, indent=2))
        return 0

    if touched == 0 and failures:
        return 1

    PRESTATIONS_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    api_copy = ROOT / "api" / "data" / "prestations.json"
    if api_copy.parent.is_dir():
        api_copy.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"\n[OK] {touched} entree(s) — prestations.json (+ api/data/)")
    if failures:
        print(f"[WARN] {failures} entree(s) en echec")
    if args.recreate or args.full:
        print("Rafraichissez le catalogue Facturio (F5).")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
