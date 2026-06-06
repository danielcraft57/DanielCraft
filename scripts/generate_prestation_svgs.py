#!/usr/bin/env python3
"""Génère les illustrations SVG manquantes pour le catalogue prestations."""
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "assets" / "images" / "prestations"

THEMES = {
    "identite": ("Image harmonisée", "#7b68c8"),
    "visibilite": ("Visibilité Google & IA", "#4da9d6"),
    "google": ("Référencement Google", "#2f9e6a"),
    "ia-visibilite": ("Assistants intelligents", "#5c7cfa"),
    "assistant-site": ("Répondeur sur le site", "#4da9d6"),
    "emails": ("Aide e-mails clients", "#e07a5f"),
    "maintenance": ("Entretien mensuel", "#0f3550"),
    "contenus": ("Textes & articles", "#4da9d6"),
    "redaction": ("Rédaction commerciale", "#c9a227"),
    "analyse": ("Comprendre vos chiffres", "#2f9e6a"),
    "boutique": ("Conseiller boutique", "#e07a5f"),
    "automatisation": ("Tâches automatisées", "#5c7cfa"),
    "conseil": ("Conseil projet", "#0f3550"),
    "connexion": ("Outils connectés", "#4da9d6"),
    "transfert": ("Transfert de données", "#7b68c8"),
    "vitesse": ("Site rapide", "#2f9e6a"),
    "page": ("Page en plus", "#4da9d6"),
    "formulaire": ("Formulaire sur mesure", "#e07a5f"),
    "look": ("Nouveau look", "#c9a227"),
    "hebergement": ("Hébergement & domaine", "#0f3550"),
    "securite": ("Sauvegardes & sécurité", "#2f9e6a"),
    "support": ("Support & accompagnement", "#4da9d6"),
    "depannage": ("Dépannage express", "#e07a5f"),
}


def svg(name: str, label: str, accent: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" role="img" aria-hidden="true">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e8f6fc"/><stop offset="100%" stop-color="#fff"/></linearGradient>
    <linearGradient id="acc" x1="0" y1="1" x2="1" y2="0"><stop offset="0%" stop-color="{accent}"/><stop offset="100%" stop-color="#0f3550"/></linearGradient>
  </defs>
  <rect width="800" height="420" rx="24" fill="url(#sky)"/>
  <circle cx="400" cy="180" r="72" fill="#fff" stroke="{accent}" stroke-width="3" opacity="0.95"/>
  <path d="M360 180 L388 208 L448 148" fill="none" stroke="url(#acc)" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
  <rect x="140" y="280" width="520" height="12" rx="6" fill="#e8f4fa"/>
  <rect x="220" y="305" width="360" height="10" rx="5" fill="#e8f4fa"/>
  <text x="400" y="370" text-anchor="middle" font-family="system-ui,sans-serif" font-size="15" font-weight="700" fill="#0f3550">{label}</text>
</svg>
'''


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for stem, (label, accent) in THEMES.items():
        path = OUT / f"{stem}.svg"
        if path.name == "site-vitrine.svg" and path.exists():
            continue
        path.write_text(svg(stem, label, accent), encoding="utf-8")
        print(f"[OK] {path.name}")


if __name__ == "__main__":
    main()
