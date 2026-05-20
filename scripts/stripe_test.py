#!/usr/bin/env python3
"""Teste les clés Stripe (.env) : balance + session Checkout factice."""
from __future__ import annotations

import argparse
import sys

from stripe_client import publishable_key, secret_key, site_base, stripe_request


def main() -> int:
    parser = argparse.ArgumentParser(description='Test connexion Stripe DanielCraft')
    parser.add_argument('--slug', default='restauration', help='Slug vitrine pour test Checkout')
    parser.add_argument('--checkout', action='store_true', help='Créer une session Checkout (sans ouvrir le navigateur)')
    args = parser.parse_args()

    pk = publishable_key()
    sk = secret_key()
    if not sk:
        print('[ERREUR] STRIPE_SECRET_KEY absente — lancez scripts/merge_stripe_env.py', file=sys.stderr)
        return 1

    print(f'[OK] Clé secrète : {sk[:12]}… (mode {"live" if sk.startswith("sk_live") else "test"})')
    print(f'[OK] Clé publique : {(pk[:12] + "…") if pk else "(non définie)"}')
    print(f'[OK] SITE_BASE : {site_base()}')

    balance = stripe_request('GET', '/balance')
    livemode = balance.get('livemode')
    print(f'[OK] API Stripe — livemode={livemode}')

    if args.checkout:
        base = site_base()
        slug = args.slug
        params = {
            'mode': 'payment',
            'success_url': f'{base}/vitrines/{slug}/?stripe=success',
            'cancel_url': f'{base}/vitrines/{slug}/?stripe=cancel',
            'line_items[0][quantity]': 1,
            'line_items[0][price_data][currency]': 'eur',
            'line_items[0][price_data][unit_amount]': 4200,
            'line_items[0][price_data][product_data][name]': f'Test Checkout — {slug}',
            'metadata[vitrine_slug]': slug,
        }
        session = stripe_request('POST', '/checkout/sessions', params)
        url = session.get('url', '')
        print(f'[OK] Session Checkout : {session.get("id")}')
        if url:
            print(f'     URL (ouvrir pour tester) : {url}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
