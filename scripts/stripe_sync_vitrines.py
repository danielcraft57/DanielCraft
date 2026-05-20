#!/usr/bin/env python3
"""
Crée / met à jour des Payment Links Stripe pour chaque vitrine et écrit stripe_payment_link_url dans src/data/vitrines.json.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from stripe_client import site_base, stripe_request

ROOT = Path(__file__).resolve().parents[1]
VITRINES_JSON = ROOT / 'src' / 'data' / 'vitrines.json'


def find_product_by_slug(slug: str) -> str | None:
    products = stripe_request('GET', '/products', {'limit': 100, 'active': 'true'})
    for p in products.get('data', []):
        meta = p.get('metadata') or {}
        if meta.get('vitrine_slug') == slug:
            return p.get('id')
    return None


def ensure_product(slug: str, title: str, dry_run: bool) -> str:
    existing = find_product_by_slug(slug)
    if existing:
        return existing
    if dry_run:
        return f'prod_DRY_{slug}'
    created = stripe_request('POST', '/products', {
        'name': f'{title} — maquette DanielCraft',
        'metadata[vitrine_slug]': slug,
    })
    return created['id']


def ensure_price(product_id: str, amount_cents: int, dry_run: bool) -> str:
    if dry_run:
        return f'price_DRY_{product_id}'
    price = stripe_request('POST', '/prices', {
        'product': product_id,
        'unit_amount': amount_cents,
        'currency': 'eur',
    })
    return price['id']


def ensure_payment_link(price_id: str, slug: str, dry_run: bool) -> str:
    if dry_run:
        return f'https://checkout.stripe.com/dry-run/{slug}'
    base = site_base()
    link = stripe_request('POST', '/payment_links', {
        'line_items[0][price]': price_id,
        'line_items[0][quantity]': 1,
        'metadata[vitrine_slug]': slug,
        'after_completion[type]': 'redirect',
        'after_completion[redirect][url]': f'{base}/vitrines/{slug}/?stripe=success',
    })
    return link.get('url') or ''


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true', help='Simule sans appeler Stripe')
    parser.add_argument('--slug', help='Un seul slug (sinon tout le catalogue)')
    args = parser.parse_args()

    if not VITRINES_JSON.is_file():
        print(f'[ERREUR] {VITRINES_JSON} introuvable', file=sys.stderr)
        return 1

    data = json.loads(VITRINES_JSON.read_text(encoding='utf-8'))
    default_price = int(data.get('default_price_eur') or 42)
    items = data.get('items') or []
    updated = 0

    for item in items:
        slug = (item.get('slug') or '').strip()
        if not slug:
            continue
        if args.slug and slug != args.slug:
            continue
        title = (item.get('title') or slug).strip()
        try:
            price_eur = int(item.get('price_eur', default_price))
        except (TypeError, ValueError):
            price_eur = default_price

        print(f'— {slug} ({price_eur} € HT)')
        product_id = ensure_product(slug, title, args.dry_run)
        price_id = ensure_price(product_id, price_eur * 100, args.dry_run)
        url = ensure_payment_link(price_id, slug, args.dry_run)
        if url:
            item['stripe_payment_link_url'] = url
            updated += 1
            print(f'  → {url}')

    if args.dry_run:
        print(f'[DRY-RUN] {updated} lien(s) simulés (fichier non modifié).')
        return 0

    VITRINES_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'[OK] {updated} payment link(s) enregistrés dans {VITRINES_JSON}')
    print('Relancez python build.py pour publier les fiches.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
