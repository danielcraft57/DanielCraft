#!/usr/bin/env python3
"""Test API Prestafacture (lecture .env local). Usage: python scripts/prestafacture_test.py [--devis]"""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_env() -> None:
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
    base = os.environ.get("PRESTAFACTURE_API_BASE", "").rstrip("/")
    token = os.environ.get("PRESTAFACTURE_API_TOKEN", "").strip()
    if not base or not token:
        print("PRESTAFACTURE_API_BASE ou PRESTAFACTURE_API_TOKEN manquant dans .env")
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
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
            try:
                return resp.status, json.loads(raw)
            except json.JSONDecodeError:
                return resp.status, raw
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8", errors="replace")
        try:
            return e.code, json.loads(raw)
        except json.JSONDecodeError:
            return e.code, raw


def catalog_product_id(slug: str = "site-vitrine") -> int | None:
    """Lit prestafacture_product_id depuis src/data/prestations.json (sync locale ou prod)."""
    path = ROOT / "src" / "data" / "prestations.json"
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    for item in data.get("items") or []:
        if isinstance(item, dict) and item.get("slug") == slug:
            pid = item.get("prestafacture_product_id")
            if isinstance(pid, int) and pid > 0:
                return pid
            if isinstance(pid, str) and pid.isdigit():
                return int(pid)
    return None


def main() -> None:
    load_env()
    status, data = api_request("GET", "")
    print(f"GET /public -> {status}")
    print(json.dumps(data, ensure_ascii=False, indent=2) if isinstance(data, dict) else data)

    if "--devis" not in sys.argv:
        sys.exit(0 if 200 <= status < 300 else 1)

    import urllib.parse
    from datetime import datetime, timezone

    test_email = f"test-devis-script-{datetime.now(timezone.utc).strftime('%H%M%S')}@mailinator.com"
    client_body = {
        "name": "Test DanielCraft",
        "email": test_email,
        "isCompany": False,
        "countryCode": "FR",
    }
    status, client_data = api_request("POST", "/clients", client_body)
    print(f"\nPOST /clients -> {status}")
    if not isinstance(client_data, dict) or "id" not in client_data:
        print(json.dumps(client_data, ensure_ascii=False, indent=2) if isinstance(client_data, dict) else client_data)
        sys.exit(1)

    line: dict = {
        "description": "Site vitrine professionnel (test)",
        "quantity": 1,
        "unitPrice": 490,
        "taxRate": 0.2,
    }
    product_id = catalog_product_id()
    if product_id:
        line["productId"] = product_id
        print(f"productId catalogue (site-vitrine): {product_id}")
    else:
        print("productId absent — ligne libre (lancez prestafacture_sync_prestations.py)")

    devis_body = {
        "clientId": client_data["id"],
        "expiryDate": "2026-09-01",
        "notes": "Test script prestafacture_test.py — à archiver",
        "lines": [line],
    }
    status, data = api_request("POST", "/devis", devis_body)
    print(f"POST /devis -> {status}")
    print(json.dumps(data, ensure_ascii=False, indent=2) if isinstance(data, dict) else data)

    if isinstance(data, dict) and data.get("id"):
        send_status, send_data = api_request(
            "POST",
            f"/devis/{data['id']}/send",
            {"email": test_email, "updateClientEmail": True},
        )
        print(f"POST /devis/{{id}}/send -> {send_status}")
        print(json.dumps(send_data, ensure_ascii=False, indent=2) if isinstance(send_data, dict) else send_data)

    sys.exit(0 if 200 <= status < 300 else 1)


if __name__ == "__main__":
    main()
