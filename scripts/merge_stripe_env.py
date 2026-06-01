#!/usr/bin/env python3
"""Fusionne STRIPE_* dans .env (ne jamais committer .env)."""
from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = ROOT / '.env'

KEYS = ('STRIPE_PUBLISHABLE_KEY', 'STRIPE_SECRET_KEY', 'STRIPE_TEST_KEY', 'STRIPE_WEBHOOK_SECRET')


def main() -> int:
    updates = {k: os.environ.get(k, '').strip() for k in KEYS}
    pk = updates['STRIPE_PUBLISHABLE_KEY']
    sk = updates['STRIPE_SECRET_KEY']
    if not pk or not sk:
        print('Définissez STRIPE_PUBLISHABLE_KEY et STRIPE_SECRET_KEY puis relancez.', file=sys.stderr)
        print('Ex. PowerShell :', file=sys.stderr)
        print('  $env:STRIPE_PUBLISHABLE_KEY="pk_live_..."', file=sys.stderr)
        print('  $env:STRIPE_SECRET_KEY="sk_live_..."', file=sys.stderr)
        print('  python scripts/merge_stripe_env.py', file=sys.stderr)
        return 1

    lines: list[str] = []
    if ENV_PATH.is_file():
        lines = ENV_PATH.read_text(encoding='utf-8').splitlines()

    out: list[str] = []
    seen: set[str] = set()
    for line in lines:
        key_part = line.split('=', 1)[0].strip() if '=' in line else ''
        if key_part in KEYS and updates.get(key_part):
            out.append(f'{key_part}={updates[key_part]}')
            seen.add(key_part)
        else:
            out.append(line)

    block = ['', '# Stripe (DanielCraft catalogue vitrines)']
    for key in KEYS:
        val = updates.get(key) or ''
        if val and key not in seen:
            block.append(f'{key}={val}')
            seen.add(key)

    if block:
        if out and out[-1].strip() != '':
            out.append('')
        out.extend(block)

    ENV_PATH.write_text('\n'.join(out).rstrip() + '\n', encoding='utf-8')
    print(f'[OK] {ENV_PATH} mis à jour (STRIPE_PUBLISHABLE_KEY + STRIPE_SECRET_KEY).')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
