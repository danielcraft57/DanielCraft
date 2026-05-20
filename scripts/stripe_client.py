#!/usr/bin/env python3
"""Client Stripe minimal (urllib) pour scripts de sync / test."""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def load_dotenv() -> None:
    env_path = ROOT / '.env'
    if not env_path.is_file():
        return
    for raw in env_path.read_text(encoding='utf-8').splitlines():
        line = raw.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        key, val = line.split('=', 1)
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if key and os.environ.get(key) in (None, ''):
            os.environ[key] = val


def secret_key() -> str:
    load_dotenv()
    return (os.environ.get('STRIPE_SECRET_KEY') or '').strip()


def publishable_key() -> str:
    load_dotenv()
    return (os.environ.get('STRIPE_PUBLISHABLE_KEY') or '').strip()


def site_base() -> str:
    load_dotenv()
    return (os.environ.get('SITE_BASE') or 'https://danielcraft.fr').rstrip('/')


def stripe_request(method: str, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
    sk = secret_key()
    if not sk.startswith('sk_'):
        raise RuntimeError('STRIPE_SECRET_KEY manquante ou invalide dans .env')

    url = 'https://api.stripe.com/v1' + path
    method_u = method.upper()
    if method_u == 'GET' and params:
        url += '?' + urllib.parse.urlencode(params, doseq=True)
        req = urllib.request.Request(url, method='GET')
    elif method_u == 'POST':
        data = urllib.parse.urlencode(params or {}, doseq=True).encode('utf-8')
        req = urllib.request.Request(url, data=data, method='POST')
    else:
        req = urllib.request.Request(url, method=method_u)
    auth = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    auth.add_password(None, 'api.stripe.com', sk, '')
    handler = urllib.request.HTTPBasicAuthHandler(auth)
    opener = urllib.request.build_opener(handler)
    try:
        with opener.open(req, timeout=45) as resp:
            body = resp.read().decode('utf-8')
            return json.loads(body)
    except urllib.error.HTTPError as e:
        err_body = e.read().decode('utf-8', errors='replace')
        try:
            payload = json.loads(err_body)
            msg = payload.get('error', {}).get('message', err_body)
        except json.JSONDecodeError:
            msg = err_body
        raise RuntimeError(f'Stripe HTTP {e.code}: {msg}') from e
