"""Validation des catalogues JSON source (audits, prestations, vitrines)."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'src' / 'data'


class AuditsCatalogTests(unittest.TestCase):
    def test_audits_json_paid_offer(self) -> None:
        raw = json.loads((DATA / 'audits.json').read_text(encoding='utf-8'))
        paid = raw['paid_audit']
        self.assertEqual(raw.get('currency'), 'EUR')
        self.assertGreaterEqual(float(paid['price_eur']), 50)
        self.assertEqual(int(paid['price_cents']), int(round(float(paid['price_eur']) * 100)))
        self.assertIn('checkout_product_name', paid)


class PrestationsCatalogTests(unittest.TestCase):
    def test_prestations_has_categories_and_items(self) -> None:
        raw = json.loads((DATA / 'prestations.json').read_text(encoding='utf-8'))
        self.assertGreaterEqual(len(raw.get('categories', [])), 3)
        self.assertGreaterEqual(len(raw.get('items', [])), 20)

    def test_each_item_has_slug_and_title(self) -> None:
        raw = json.loads((DATA / 'prestations.json').read_text(encoding='utf-8'))
        for item in raw.get('items', []):
            self.assertTrue(item.get('slug'), msg=f"item sans slug: {item}")
            self.assertTrue(item.get('title'), msg=f"item sans titre: {item.get('slug')}")


class VitrinesCatalogTests(unittest.TestCase):
    def test_vitrines_has_entries(self) -> None:
        raw = json.loads((DATA / 'vitrines.json').read_text(encoding='utf-8'))
        items = raw.get('items', [])
        self.assertGreaterEqual(len(items), 5)
        for item in items:
            self.assertRegex(item.get('slug', ''), r'^[a-z0-9-]+$')


if __name__ == '__main__':
    unittest.main()
