#!/usr/bin/env python3
"""Rembourse un paiement Stripe (PaymentIntent, charge ou session Checkout).

Usage (depuis la racine du repo) :

    python scripts/stripe_refund.py --payment-intent pi_xxx
    python scripts/stripe_refund.py --session cs_live_xxx --env .env.prod
    python scripts/stripe_refund.py --charge ch_xxx --reason requested_by_customer

Ne pas exposer ca en endpoint public. Prestafacture : l'avoir se fait a la main
(API publique sans ressource avoirs — voir docs/PRESTAFACTURE.md).
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

from stripe_client import stripe_request  # noqa: E402


def load_env_file(path: Path) -> None:
    if not path.is_file():
        raise SystemExit(f'[ERREUR] Fichier env introuvable : {path}')
    for raw in path.read_text(encoding='utf-8').splitlines():
        line = raw.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        key, val = line.split('=', 1)
        os.environ[key.strip()] = val.strip().strip('"').strip("'")


def resolve_payment_intent(session_id: str = '', charge_id: str = '', payment_intent: str = '') -> str:
    if payment_intent:
        if not payment_intent.startswith('pi_'):
            raise SystemExit('[ERREUR] --payment-intent doit commencer par pi_')
        return payment_intent
    if session_id:
        if not session_id.startswith('cs_'):
            raise SystemExit('[ERREUR] --session doit commencer par cs_')
        sess = stripe_request('GET', f'/checkout/sessions/{session_id}')
        pi = sess.get('payment_intent') or ''
        if not pi:
            raise SystemExit('[ERREUR] Session sans PaymentIntent (paiement pas encore capture ?)')
        return str(pi)
    if charge_id:
        if not charge_id.startswith('ch_'):
            raise SystemExit('[ERREUR] --charge doit commencer par ch_')
        charge = stripe_request('GET', f'/charges/{charge_id}')
        pi = charge.get('payment_intent') or ''
        if not pi:
            raise SystemExit('[ERREUR] Charge sans PaymentIntent.')
        return str(pi)
    raise SystemExit('[ERREUR] Passez --payment-intent, --session ou --charge.')


def main() -> int:
    parser = argparse.ArgumentParser(description='Rembourse un paiement Stripe DanielCraft')
    parser.add_argument('--env', default='.env', help='Fichier env (defaut .env ; live : .env.prod)')
    parser.add_argument('--payment-intent', default='', help='pi_…')
    parser.add_argument('--session', default='', help='cs_… (Checkout)')
    parser.add_argument('--charge', default='', help='ch_…')
    parser.add_argument(
        '--reason',
        default='requested_by_customer',
        choices=['requested_by_customer', 'duplicate', 'fraudulent'],
    )
    args = parser.parse_args()

    load_env_file(ROOT / args.env)
    pi = resolve_payment_intent(args.session, args.charge, args.payment_intent)
    refund = stripe_request(
        'POST',
        '/refunds',
        {
            'payment_intent': pi,
            'reason': args.reason,
        },
    )
    rid = refund.get('id', '')
    status = refund.get('status', '')
    amount = refund.get('amount', 0)
    print(f'[OK] Remboursement {rid} — {status} — {amount} centimes — PI {pi}')
    print('     Avoir Prestafacture : a creer a la main (API publique sans /avoirs).')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
