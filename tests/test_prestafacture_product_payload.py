"""Tests payload Prestafacture (descriptions courtes, heures réalistes)."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from prestafacture_product_payload import (  # noqa: E402
    DESCRIPTION_MAX_LEN,
    build_livrables,
    build_rich_product_body,
    product_description,
)


class PrestafactureProductPayloadTests(unittest.TestCase):
    def test_product_description_is_short(self) -> None:
        entry = {
            "short_description": "Un site simple à parcourir sur mobile.",
            "tagline": "Votre vitrine en ligne",
            "description": "Je crée un site vitrine sur mesure : pages essentielles, textes lisibles, "
            "formulaire de contact et mise en ligne. Vous gardez la main sur vos contenus.",
            "promo": "Premier pas en ligne sans engagement lourd.",
            "price_label": "Forfait",
        }
        desc = product_description(entry, "Site vitrine professionnel", 590)
        self.assertLessEqual(len(desc), DESCRIPTION_MAX_LEN)
        self.assertNotIn("Vous gardez la main", desc)
        self.assertIn("590", desc)

    def test_livrables_limited_and_hours_realistic(self) -> None:
        entry = {
            "category": "identite",
            "includes": [
                "Jusqu'à 5 pages",
                "Design adapté",
                "Formulaire contact",
                "Mise en ligne",
                "Extra ligne ignorée",
            ],
        }
        livrables = build_livrables(entry, "SITE-VITRINE", "Site vitrine", 590)
        self.assertEqual(len(livrables), 2)
        total_h = sum(float(x["heures"]) for x in livrables)
        self.assertEqual(total_h, 26.0)
        self.assertEqual(sum(int(x["montant"]) for x in livrables), 590)

    def test_eco_audit_payload(self) -> None:
        entry = {
            "category": "eco",
            "short_description": "Mesure du poids de vos pages.",
            "price_label": "Forfait",
        }
        body = build_rich_product_body(entry, "ECO-AUDIT-SITE", "Audit éco", 149, slug="audit-eco-numerique")
        self.assertLessEqual(len(body["description"]), DESCRIPTION_MAX_LEN)
        self.assertEqual(body["estimatedHours"], 5)
        self.assertEqual(len(body["livrables"]), 2)


if __name__ == "__main__":
    unittest.main()
