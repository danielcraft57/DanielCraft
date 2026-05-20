#!/usr/bin/env python3
"""Met à jour les excerpts SEO du catalogue vitrines."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "src" / "data" / "vitrines.json"

EXCERPTS = {
    "technologie": "Site SaaS ou ESN crédible : hero, preuves, FAQ et formulaire démo — maquette tech pour Metz et le Grand Est.",
    "restauration": "Site restaurant qui donne faim : carte, photos et réservation — modèle HCR pour Metz, Nancy et Thionville.",
    "beaute": "Institut beauté et spa : soins, rendez-vous et engagements — page claire pour fidéliser votre clientèle locale.",
    "odontologie": "Cabinet dentaire rassurant : tarifs, prévention et rappel téléphonique — site patient pour Moselle et Metz.",
    "industrie": "Site usinage et industrie : machines, devis express et FAQ qualité — convertissez les appels d'offres.",
    "association": "Association et ESS : dons, bénévolat et projets — vitrine mobilisatrice pour le Grand Est.",
    "commerce": "Commerce de proximité et drive : rayons, click & collect et fidélité — maquette retail prête à l'emploi.",
    "comptable": "Cabinet comptable : forfaits, bilan flash et contact dirigeant — crédibilité pro en un clic.",
    "education": "Centre de formation : parcours, inscriptions et alternance — rassurez apprenants et entreprises.",
    "services": "Facility et conciergerie : offres illustrées, devis et FAQ — pour immeubles tertiaires en Lorraine.",
    "banque": "Banque régionale : comptes, crédits et agences de proximité — modèle qui inspire confiance.",
    "etablissement": "Hôtel 4 étoiles : chambres, spa et séminaires — réservation visible, design hôtellerie premium.",
    "automobile": "Garage auto : entretien, pneus, carrosserie et RDV — site atelier qui rassure avant le devis.",
    "chocolatier": "Chocolatier artisan : boutique, coffrets et atelier — galerie gourmande pour booster les ventes.",
    "immobilier": "Agence immobilière : biens, estimation gratuite et gestion — captez vendeurs et acquéreurs locaux.",
    "juridique": "Avocats affaires et social : expertises, forfaits et contact — cabinet crédible pour PME à Metz.",
    "architecture": "Agence d'architecture : projets, méthode et brief — portfolio pro pour gagner vos consultations.",
    "fitness": "Salle de sport : cours, tarifs et essai gratuit — site énergique qui remplit les créneaux.",
    "photographie": "Photographe mariage et corporate : portfolio, prestations et devis — studio qui inspire confiance.",
}

data = json.loads(path.read_text(encoding="utf-8"))
for it in data["items"]:
    slug = it["slug"]
    if slug in EXCERPTS:
        it["excerpt"] = EXCERPTS[slug]
path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("OK excerpts", len(EXCERPTS))
