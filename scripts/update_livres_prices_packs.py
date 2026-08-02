#!/usr/bin/env python3
"""Prix unitaires bas + packs projetes (remise volume) + deal de la semaine."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "src" / "data" / "livres.json"

UNIT_EUR = 0.5

PACK_DISCOUNT_BY_N = {
    2: 0.22,
    3: 0.34,
    4: 0.38,
    5: 0.42,
    6: 0.45,
}

# Pack mis en avant sous la recherche (rotation manuelle)
DEAL_OF_THE_WEEK_SLUG = "pack-web"


def pack_price_eur(n_books: int, unit: float = UNIT_EUR) -> float:
    if n_books < 1:
        return unit
    sum_unit = round(n_books * unit, 2)
    discount = PACK_DISCOUNT_BY_N.get(n_books)
    if discount is None:
        discount = min(0.50, 0.18 + 0.04 * (n_books - 1))
    raw = sum_unit * (1.0 - discount)
    cents = int(round(raw * 100))
    endings = (49, 79, 99)
    base = (cents // 100) * 100
    candidates = [base + e for e in endings] + [
        base - 100 + e for e in endings if base >= 100
    ]
    candidates = [c for c in candidates if 50 <= c < int(sum_unit * 100)]
    if not candidates:
        psycho = max(50, int(sum_unit * 100) - 21)
    else:
        psycho = min(candidates, key=lambda c: abs(c - cents))
    price = round(psycho / 100, 2)
    if price >= sum_unit:
        price = max(0.5, round(sum_unit - 0.21, 2))
    return price


def eur_fr(value: float) -> str:
    return f"{value:.2f}".replace(".", ",")


PACKS = [
    {
        "slug": "pack-debutant-code",
        "title": "Pack Debutant code",
        "tagline": "HTML, JS, Python et Git — le kit demarrage",
        "short_description": (
            "4 PDF pour poser des bases solides : HTML/CSS, JavaScript, Python et Git."
        ),
        "keywords": ["pack", "debutant", "html", "javascript", "python", "git"],
        "icon": "fa-rocket",
        "book_slugs": [
            "html-css-les-bases",
            "javascript-les-bases",
            "python-les-bases",
            "git-les-bases",
        ],
    },
    {
        "slug": "pack-web",
        "title": "Pack Web",
        "tagline": "HTML/CSS, JavaScript et TypeScript",
        "short_description": (
            "5 PDF pour demarrer et monter en web front : "
            "HTML/CSS base+suite, JS base+suite, TypeScript."
        ),
        "keywords": ["pack", "web", "html", "css", "javascript", "typescript"],
        "icon": "fa-globe",
        "book_slugs": [
            "html-css-les-bases",
            "html-css-la-suite",
            "javascript-les-bases",
            "javascript-la-suite",
            "typescript-les-bases",
        ],
    },
    {
        "slug": "pack-python",
        "title": "Pack Python",
        "tagline": "Bases + pratique",
        "short_description": "2 PDF Python : les bases puis la pratique avec mini-projets.",
        "keywords": ["pack", "python", "script"],
        "icon": "fa-python",
        "book_slugs": ["python-les-bases", "python-pratique"],
    },
    {
        "slug": "pack-sql",
        "title": "Pack Data / SQL",
        "tagline": "Base, intermediaire et expert",
        "short_description": "3 PDF SQL du debutant a l'expert : requetes, sous-requetes, perf.",
        "keywords": ["pack", "sql", "data", "base de donnees"],
        "icon": "fa-database",
        "book_slugs": ["sql-les-bases", "sql-intermediaire", "sql-expert"],
    },
    {
        "slug": "pack-ia",
        "title": "Pack IA",
        "tagline": "Essentiel, ML et deep learning",
        "short_description": "3 PDF IA : bases, machine learning, deep learning.",
        "keywords": ["pack", "ia", "ml", "deep learning"],
        "icon": "fa-robot",
        "book_slugs": ["ia-les-bases", "ia-machine-learning", "ia-deep-learning"],
    },
    {
        "slug": "pack-finance",
        "title": "Pack Finance",
        "tagline": "Marches, produits et crypto",
        "short_description": (
            "5 PDF finance : bases, actions/obligations, derives, forex, crypto."
        ),
        "keywords": ["pack", "finance", "bourse", "crypto"],
        "icon": "fa-chart-line",
        "book_slugs": [
            "finance-les-bases",
            "finance-actions-obligations",
            "finance-produits-derives",
            "finance-forex-matieres",
            "finance-crypto",
        ],
    },
    {
        "slug": "pack-securite",
        "title": "Pack Securite web",
        "tagline": "Base, intermediaire et expert",
        "short_description": (
            "3 PDF securite web : gestes essentiels, attaques courantes, hardening."
        ),
        "keywords": ["pack", "securite", "https", "owasp"],
        "icon": "fa-shield-alt",
        "book_slugs": [
            "securite-web-les-bases",
            "securite-web-intermediaire",
            "securite-web-expert",
        ],
    },
    {
        "slug": "pack-commerce",
        "title": "Pack Commerce & vente",
        "tagline": "Offre, closing et clients",
        "short_description": (
            "4 PDF : commerce bases, vente avancee, trouver des clients, fideliser."
        ),
        "keywords": ["pack", "commerce", "vente", "clients"],
        "icon": "fa-store",
        "book_slugs": [
            "commerce-les-bases",
            "vente-avancee",
            "ecommerce-trouver-clients",
            "ecommerce-clients",
        ],
    },
    {
        "slug": "pack-ecommerce",
        "title": "Pack E-commerce",
        "tagline": "Boutique, dropshipping et acquisition",
        "short_description": (
            "4 PDF e-commerce : dropshipping, lancement, acquisition et clients."
        ),
        "keywords": ["pack", "ecommerce", "dropshipping", "boutique"],
        "icon": "fa-shopping-cart",
        "book_slugs": [
            "dropshipping",
            "ecommerce-dropshipping",
            "ecommerce-trouver-clients",
            "ecommerce-clients",
        ],
    },
    {
        "slug": "pack-git",
        "title": "Pack Git",
        "tagline": "Solo puis en equipe",
        "short_description": "2 PDF Git : les bases puis le travail en equipe (PR, CI).",
        "keywords": ["pack", "git", "github", "equipe"],
        "icon": "fa-code-branch",
        "book_slugs": ["git-les-bases", "git-en-equipe"],
    },
    {
        "slug": "pack-jvm",
        "title": "Pack Java & Kotlin",
        "tagline": "JVM : bases et intermediaire",
        "short_description": "4 PDF : Java et Kotlin, niveau bases puis intermediaire.",
        "keywords": ["pack", "java", "kotlin", "jvm"],
        "icon": "fa-mug-hot",
        "book_slugs": [
            "java-les-bases",
            "java-intermediaire",
            "kotlin-les-bases",
            "kotlin-intermediaire",
        ],
    },
    {
        "slug": "pack-backend",
        "title": "Pack Backend",
        "tagline": "PHP, Go, C# et Python",
        "short_description": "4 PDF cote serveur : PHP, Go, C# et Python bases.",
        "keywords": ["pack", "backend", "php", "go", "csharp", "python"],
        "icon": "fa-server",
        "book_slugs": [
            "php-les-bases",
            "go-les-bases",
            "csharp-les-bases",
            "python-les-bases",
        ],
    },
    {
        "slug": "pack-mobile",
        "title": "Pack Mobile",
        "tagline": "Swift et Kotlin",
        "short_description": "3 PDF mobile : Swift bases + Kotlin bases et intermediaire.",
        "keywords": ["pack", "mobile", "swift", "kotlin", "ios", "android"],
        "icon": "fa-mobile-alt",
        "book_slugs": ["swift-les-bases", "kotlin-les-bases", "kotlin-intermediaire"],
    },
    {
        "slug": "pack-systeme",
        "title": "Pack Systeme",
        "tagline": "C/C++, Rust et Go",
        "short_description": "3 PDF proches machine : C/C++, Rust et Go.",
        "keywords": ["pack", "systeme", "c", "rust", "go"],
        "icon": "fa-microchip",
        "book_slugs": ["c-cpp-les-bases", "rust-les-bases", "go-les-bases"],
    },
    {
        "slug": "pack-marketing-com",
        "title": "Pack Marketing & com",
        "tagline": "Message, canaux et clarte",
        "short_description": (
            "3 PDF : marketing, communication et commerce — pour parler net et vendre mieux."
        ),
        "keywords": ["pack", "marketing", "communication", "commerce"],
        "icon": "fa-bullhorn",
        "book_slugs": [
            "marketing-les-bases",
            "communication-les-bases",
            "commerce-les-bases",
        ],
    },
    {
        "slug": "pack-frontend-avance",
        "title": "Pack Front avance",
        "tagline": "Suite HTML/CSS, JS et TypeScript",
        "short_description": (
            "3 PDF pour monter d'un cran cote front : HTML/CSS suite, JavaScript suite, TypeScript."
        ),
        "keywords": ["pack", "frontend", "typescript", "javascript", "css"],
        "icon": "fa-laptop-code",
        "book_slugs": [
            "html-css-la-suite",
            "javascript-la-suite",
            "typescript-les-bases",
        ],
    },
    {
        "slug": "pack-data-ia",
        "title": "Pack Data & IA",
        "tagline": "SQL + machine learning",
        "short_description": (
            "4 PDF : SQL bases et intermediaire, IA bases et machine learning."
        ),
        "keywords": ["pack", "data", "sql", "ia", "ml"],
        "icon": "fa-brain",
        "book_slugs": [
            "sql-les-bases",
            "sql-intermediaire",
            "ia-les-bases",
            "ia-machine-learning",
        ],
    },
    {
        "slug": "pack-investisseur",
        "title": "Pack Investisseur",
        "tagline": "Bases, actions et crypto",
        "short_description": (
            "3 PDF finance pour demarrer sans se perdre : bases, actions/obligations, crypto."
        ),
        "keywords": ["pack", "investissement", "actions", "crypto", "finance"],
        "icon": "fa-coins",
        "book_slugs": [
            "finance-les-bases",
            "finance-actions-obligations",
            "finance-crypto",
        ],
    },
]


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    data["default_price_eur"] = UNIT_EUR
    data["pricing_note"] = (
        f"Unitaire {eur_fr(UNIT_EUR)} EUR TTC. "
        "Pack = somme unitaire moins remise volume (prix .49/.79/.99)."
    )
    data["intro_note"] = (
        f"Livres a {eur_fr(UNIT_EUR)} EUR TTC — packs en remise volume."
    )
    data["stripe_note"] = "Checkout via api/stripe-create-livre-checkout.php (livre ou pack)."
    data["deal_of_the_week"] = {
        "slug": DEAL_OF_THE_WEEK_SLUG,
        "badge": "Pack de la semaine",
        "urgency": "Offre limitee — mise en avant cette semaine",
        "cta_label": "Profiter de l'offre",
    }
    data.pop("pack_price_eur", None)

    cats = data.get("categories") or []
    if not any(c.get("id") == "packs" for c in cats):
        cats.insert(
            0,
            {
                "id": "packs",
                "title": "Packs",
                "nav_label": "Packs",
                "icon": "fa-box-open",
                "description": (
                    "Plusieurs PDF moins cher qu'a l'unite — remise volume sur le prix d'appel."
                ),
            },
        )
    data["categories"] = cats

    levels = data.get("levels") or []
    if not any(lv.get("id") == "pack" for lv in levels):
        levels.append({"id": "pack", "label": "Pack", "icon": "fa-box-open"})
    data["levels"] = levels

    items = []
    for it in data.get("items", []):
        if it.get("kind") == "pack" or str(it.get("slug", "")).startswith("pack-"):
            continue
        it["price_eur"] = UNIT_EUR
        it["price_label"] = "Prix d'appel"
        it["price_note"] = "TTC — PDF envoye par e-mail apres paiement"
        it["kind"] = "livre"
        items.append(it)

    slug_to_title = {it["slug"]: it.get("title", it["slug"]) for it in items}

    pack_items = []
    print("Packs calcules :")
    for pk in PACKS:
        n = len(pk["book_slugs"])
        missing = [s for s in pk["book_slugs"] if s not in slug_to_title]
        if missing:
            raise SystemExit(f"Slugs manquants pour {pk['slug']}: {missing}")
        sum_unit = round(n * UNIT_EUR, 2)
        price = pack_price_eur(n)
        titles = [slug_to_title[s] for s in pk["book_slugs"]]
        save = round(sum_unit - price, 2)
        print(
            f"  {pk['slug']}: {n} PDF | unite {eur_fr(sum_unit)} -> pack {eur_fr(price)} "
            f"(eco {eur_fr(save)})"
        )
        pack_items.append(
            {
                "slug": pk["slug"],
                "kind": "pack",
                "category": "packs",
                "level": "pack",
                "title": pk["title"],
                "tagline": pk["tagline"],
                "short_description": pk["short_description"],
                "description": (
                    f"{pk['short_description']} {n} livres PDF pour {eur_fr(price)} EUR TTC "
                    f"(au lieu de {eur_fr(sum_unit)} a l'unite). Chez DanielCraft."
                ),
                "keywords": pk["keywords"],
                "source_dir": "",
                "pdf": "",
                "book_slugs": pk["book_slugs"],
                "icon": pk["icon"],
                "price_eur": price,
                "compare_at_eur": sum_unit,
                "price_label": "Pack",
                "price_note": (
                    f"TTC — {n} PDF (valeur {eur_fr(sum_unit)} a l'unite) "
                    "envoyes par e-mail apres paiement"
                ),
                "currency": "EUR",
                "featured": True,
                "has_page": True,
                "stripe_payment_link_url": "",
                "benefits": [
                    f"{n} livres PDF inclus",
                    f"Economie d'environ {eur_fr(save)} EUR vs a l'unite",
                    "Meme pedagogie claire (Lea, Max, Sam)",
                    "Envoi par e-mail apres paiement",
                ],
                "includes": [f"PDF : {t}" for t in titles],
            }
        )

    data["items"] = pack_items + items
    data["featured_order"] = [DEAL_OF_THE_WEEK_SLUG] + [
        p["slug"] for p in PACKS if p["slug"] != DEAL_OF_THE_WEEK_SLUG
    ][:7] + [
        "javascript-les-bases",
        "python-les-bases",
        "html-css-les-bases",
        "ia-les-bases",
    ]

    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"[OK] livres={len(items)} @{eur_fr(UNIT_EUR)} | packs={len(pack_items)} | "
        f"deal={DEAL_OF_THE_WEEK_SLUG}"
    )


if __name__ == "__main__":
    main()
