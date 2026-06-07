"""Tests unitaires des helpers Python du build."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import build  # noqa: E402


class FormatAuditPriceTests(unittest.TestCase):
    def test_integer_ttc(self) -> None:
        self.assertEqual(build.format_audit_price_eur_display(199), '199')

    def test_decimal_fr_comma(self) -> None:
        self.assertEqual(build.format_audit_price_eur_display(19.99), '19,99')

    def test_invalid_or_zero_defaults_to_launch_price(self) -> None:
        self.assertEqual(build.format_audit_price_eur_display(None), '199')
        self.assertEqual(build.format_audit_price_eur_display('bad'), '199')
        self.assertEqual(build.format_audit_price_eur_display(0), '199')


class AuditConfigTests(unittest.TestCase):
    def test_paid_audit_catalog(self) -> None:
        cfg = build.load_audits_config()
        paid = cfg.get('paid_audit')
        self.assertIsInstance(paid, dict)
        self.assertEqual(paid.get('slug'), 'audit-complet-ia')
        self.assertEqual(paid.get('price_eur'), 199)
        self.assertEqual(paid.get('price_cents'), 19900)


class PrestationPriceTests(unittest.TestCase):
    def test_forfait_display(self) -> None:
        label = build._prestation_price_display({'price_eur': 490, 'price_label': 'Forfait'})
        self.assertEqual(label, 'Forfait · 490 €')

    def test_zero_price_returns_label_only(self) -> None:
        label = build._prestation_price_display({'price_eur': 0, 'price_label': 'Sur devis'})
        self.assertEqual(label, 'Sur devis')


class TruncateMetaTests(unittest.TestCase):
    def test_truncates_long_text(self) -> None:
        long_text = 'a' * 200
        out = build._truncate_meta_text(long_text, 120)
        self.assertLessEqual(len(out), 120)
        self.assertTrue(out.endswith('…'))


if __name__ == '__main__':
    unittest.main()
