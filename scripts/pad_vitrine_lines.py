#!/usr/bin/env python3
"""Pad vitrine HTML toward ~220 lines with FAQ + galerie complète."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "assets" / "vitrines" / "demos"

PAD = {
    "commerce": ("com-pad", "Thionville", [
        ("commerce-artisan.png", "Primeur"), ("commerce-rayon.png", "Rayon"), ("commerce-drive.png", "Drive"),
        ("hero.svg", "Halles"), ("card-1.svg", "Traiteur"), ("card-2.svg", "Rayon"), ("card-3.svg", "Épicerie"),
    ]),
    "comptable": ("cpa-pad", "Metz", [
        ("hero.png", "Bureau"), ("reunion.png", "Réunion"), ("conseil-client.png", "Conseil"),
        ("compta-bureau-plat.png", "Documents"), ("compta-croquis-engrenage.png", "Processus"),
        ("card-1.svg", "Expert"), ("card-2.svg", "Paie"), ("card-3.svg", "Juriste"),
    ]),
    "architecture": ("arch-pad", "Metz & Grand Est", [
        ("hero.svg", "Façade atelier"), ("projet-metz.svg", "Metz"), ("projet-lux.svg", "Luxembourg"),
        ("projet-verdun.svg", "Verdun"),
    ]),
    "association": ("ass-pad", "Metz solidarité", [
        ("hero.png", "Quartier"), ("mission-benevoles.png", "Bénévoles"), ("cuisine.png", "Cuisine"),
        ("assoc-fete-quartier.png", "Fête"), ("assoc-gen-quartier.png", "Vie locale"),
        ("assoc-gen-mains.png", "Mains"), ("assoc-gen-volontaires.png", "Volontaires"),
        ("assoc-poster-illu.png", "Affiche"), ("card-1.svg", "Maraude"), ("card-2.svg", "Cuisine"),
        ("card-3.svg", "Fête"),
    ]),
    "automobile": ("auto-pad", "Plappeville", [
        ("auto-mecanique.png", "Atelier"), ("auto-pont.png", "Pont"), ("auto-pneus.png", "Pneus"),
        ("hero.svg", "Garage"), ("card-1.svg", "Entretien"), ("card-2.svg", "Carrosserie"), ("card-3.svg", "Contrôle"),
    ]),
    "banque": ("bnq-pad", "Moselle", [
        ("hero.png", "Agence"), ("conseil.png", "Conseil"), ("agences.png", "Réseau"),
        ("banque-poignee-main.png", "Accueil"), ("banque-infographic.png", "Infographie"),
        ("card-1.svg", "Crédit"), ("card-2.svg", "Épargne"), ("card-3.svg", "Pro"),
    ]),
    "beaute": ("bea-pad", "Nancy", [
        ("beaute-soin.png", "Soin"), ("beaute-spa.png", "Spa"), ("beaute-produits.png", "Produits"),
        ("hero.svg", "Institut"), ("card-1.svg", "Massage"), ("card-2.svg", "Mains"), ("card-3.svg", "Parfums"),
    ]),
    "chocolatier": ("ch-pad", "Nancy", [
        ("hero.png", "Vitrine"), ("atelier.png", "Atelier"), ("cacao-origines.png", "Cacao"),
        ("choco-degustation-plateau.png", "Dégustation"), ("choco-aquarelle-coffrets.png", "Coffrets"),
        ("produit-1.png", "Tablette"), ("produit-2.png", "Lait"), ("produit-3.png", "Pralinés"),
        ("card-1.svg", "Ganaches"), ("card-2.svg", "Origines"), ("card-3.svg", "Coffrets"),
    ]),
    "education": ("edu-pad", "Nancy", [
        ("edu-gen-parcours.png", "Parcours"), ("edu-gen-modules.png", "Modules"),
        ("edu-gen-mosaic.png", "Campus"), ("edu-groupe.png", "Groupe"), ("edu-salle.png", "Salle"),
        ("edu-formateur.png", "Formateur"), ("card-1.svg", "Digital"), ("card-2.svg", "Alternance"),
        ("card-3.svg", "VAE"),
    ]),
    "etablissement": ("etab-pad", "Nancy", [
        ("etab-chambre.png", "Chambre"), ("etab-lobby.png", "Lobby"), ("etab-seminaire.png", "Séminaire"),
        ("hero.svg", "Hôtel"), ("card-1.svg", "Chambre"), ("card-2.svg", "Spa"), ("card-3.svg", "Resto"),
    ]),
    "fitness": ("fit-pad", "Thionville", [
        ("hero.svg", "Salle"), ("cours-hiit.svg", "HIIT"), ("cours-yoga.svg", "Yoga"), ("cours-cycling.svg", "Cycling"),
    ]),
    "immobilier": ("imm-pad", "Thionville", [
        ("bien-thionville.svg", "Thionville"), ("bien-yutz.svg", "Yutz"), ("bien-sablon.svg", "Sablon"),
        ("hero.svg", "Agence"), ("equipe-agence.svg", "Équipe"),
    ]),
    "industrie": ("ind-pad", "Yutz", [
        ("hero.png", "Usine"), ("ligne-production.png", "Ligne"), ("controle.png", "Qualité"),
        ("industrie-soudure.png", "Soudure"), ("industrie-plan-usine.png", "Plan"),
        ("card-1.svg", "CNC"), ("card-2.svg", "Logistique"), ("card-3.svg", "Maintenance"),
    ]),
    "juridique": ("jur-pad", "Metz", [
        ("hero.svg", "Cabinet"), ("expertise-contentieux.svg", "Contentieux"),
        ("expertise-societes.svg", "Sociétés"), ("expertise-social.svg", "Social"),
    ]),
    "odontologie": ("odo-pad", "Thionville", [
        ("hero.png", "Cabinet"), ("salle.png", "Salle"), ("equipe-soins.png", "Équipe"),
        ("odo-salle-soins-vide.png", "Équipement"), ("odo-illus-brossage.png", "Prévention"),
        ("card-1.svg", "Soins"), ("card-2.svg", "Prévention"), ("card-3.svg", "Implants"),
    ]),
    "photographie": ("pho-pad", "Metz", [
        ("hero.svg", "Studio"), ("portfolio-mariage.svg", "Mariage"), ("portfolio-portrait.svg", "Portrait"),
        ("portfolio-corporate.svg", "Corporate"), ("portfolio-reportage.svg", "Reportage"),
        ("portfolio-architecture.svg", "Architecture"), ("portfolio-mode.svg", "Mode"),
    ]),
    "restauration": ("resto-pad", "Thionville", [
        ("resto-salle.png", "Salle"), ("resto-chef.png", "Chef"), ("resto-assiette.png", "Assiette"),
        ("hero.svg", "Brasserie"), ("card-1.svg", "Carte"), ("card-2.svg", "Terrasse"), ("card-3.svg", "Cave"),
    ]),
    "services": ("svc-pad", "Metz", [
        ("services-accueil.png", "Accueil"), ("services-nettoyage.png", "Nettoyage"),
        ("services-facility.png", "Facility"), ("card-1.svg", "Accueil"), ("card-2.svg", "Sécurité"),
        ("card-3.svg", "Maintenance"),
    ]),
    "technologie": ("tech-pad", "Thionville", [
        ("tech-datacenter.png", "Datacenter"), ("tech-equipe.png", "Équipe"), ("tech-reseau.png", "Réseau"),
        ("hero.svg", "Cloud"), ("card-1.svg", "API"), ("card-2.svg", "Data"), ("card-3.svg", "Sécurité"),
    ]),
}

FAQ = [
    "Quels sont vos horaires ?",
    "Comment prendre rendez-vous ?",
    "Intervenez-vous en Moselle et Meurthe-et-Moselle ?",
    "Proposez-vous un devis gratuit ?",
    "Quels délais de réponse ?",
    "Acceptez-vous les entreprises locales ?",
    "Y a-t-il un parking ?",
    "Comment préparer ma première visite ?",
    "Quels moyens de paiement ?",
    "Puis-je annuler ou reporter ?",
]


def gallery(slug: str, gid: str, images: list) -> str:
    items = "\n".join(
        f'    <figure class="vitrine-figure"><a href="images/{s}" class="glightbox" data-gallery="{gid}" '
        f'data-glightbox="title: {a}"><img src="images/{s}" alt="{a}" loading="lazy" decoding="async" '
        f'style="width:100%;height:200px;object-fit:cover"></a></figure>'
        for s, a in images
    )
    return f"""
  <section class="{slug}-galerie vt-reveal" aria-label="Galerie photos">
    <h2>Galerie — {slug}</h2>
    <p class="pad-lead">Cliquez pour agrandir (GLightbox). Tous les visuels du dossier démo.</p>
    <div class="pad-grid">
{items}
    </div>
  </section>
  <section class="pad-faq vt-reveal">
    <h2>Questions fréquentes</h2>
    <dl>
{chr(10).join(f"      <dt>{q}</dt><dd>Réponse indicative — démonstration portfolio DanielCraft, secteur {slug} en Lorraine.</dd>" for q in FAQ)}
    </dl>
  </section>
  <section class="pad-contact vt-reveal">
    <h2>Contact</h2>
    <form class="pad-form" action="#" method="get">
      <label>Prénom <input type="text" name="prenom"></label>
      <label>Nom <input type="text" name="nom"></label>
      <label>E-mail <input type="email" name="email"></label>
      <label>Téléphone <input type="tel" name="tel"></label>
      <label>Message <textarea name="msg" rows="4"></textarea></label>
      <label><input type="checkbox" name="rgpd"> J'accepte la politique de confidentialité (démo)</label>
      <button type="submit">Envoyer</button>
    </form>
    <p class="pad-note">Formulaire statique — aucune donnée transmise.</p>
  </section>
"""


def pad(slug: str) -> None:
    if slug not in PAD:
        return
    cls, region, imgs = PAD[slug]
    p = ROOT / slug / "index.html"
    html = p.read_text(encoding="utf-8")
    if "pad-faq" in html:
        return
    block = gallery(slug, f"{slug}-gal", imgs)
    for anchor in ("<footer", '<p class="hub-back"', "← Hub vitrines", "</main>"):
        if anchor in html:
            html = html.replace(anchor, block + "\n  " + anchor, 1)
            break
    p.write_text(html, encoding="utf-8")
    css_p = ROOT / slug / "styles.css"
    extra = """
.pad-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:.75rem;padding:1.5rem}
.pad-faq{padding:2rem 1.5rem;max-width:48rem;margin:0 auto}
.pad-faq dt{font-weight:700;margin-top:1rem}
.pad-faq dd{margin:.25rem 0 0;color:#555}
.pad-contact{padding:2rem 1.5rem;background:#f5f5f5}
.pad-form{display:grid;gap:.75rem;max-width:28rem}
.pad-form label{display:grid;gap:.25rem}
.pad-form input,.pad-form textarea{padding:.5rem;border:1px solid #ccc;border-radius:6px}
.pad-lead{opacity:.85;padding:0 1.5rem}
"""
    c = css_p.read_text(encoding="utf-8")
    if "pad-grid" not in c:
        css_p.write_text(c.strip() + extra + "\n", encoding="utf-8")
    print("padded", slug)


if __name__ == "__main__":
    for s in PAD:
        pad(s)
