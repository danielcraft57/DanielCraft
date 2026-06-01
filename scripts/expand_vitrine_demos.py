#!/usr/bin/env python3
"""Expand vitrine demos with extra sections (target ~220+ lines)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "assets" / "vitrines" / "demos"

EXTRA = {
    "education": """
  <section class="edu-detail vt-reveal" style="padding:2rem 1.5rem;max-width:900px;margin:0 auto">
    <h2>Campus Saint-Nicolas</h2>
    <p>Salles équipées, fab lab et partenariats avec les CCI Moselle et Meurthe-et-Moselle. Alternance en entreprise dès la 2<sup>e</sup> année.</p>
    <ul><li>1200 apprenants / an</li><li>35 parcours certifiants</li><li>92 % insertion à 6 mois</li></ul>
    <h3>Témoignages</h3>
    <blockquote>« J'ai trouvé mon alternance à Metz grâce au réseau Mercure. » — Léa, développeuse web</blockquote>
    <blockquote>« Formateurs accessibles, matériel récent. » — Karim, reconversion industrielle</blockquote>
    <h3>Prochaines sessions</h3>
    <table style="width:100%;border-collapse:collapse;margin-top:1rem">
      <thead><tr><th>Parcours</th><th>Début</th><th>Lieu</th></tr></thead>
      <tbody>
        <tr><td>Tech &amp; data</td><td>Sept. 2026</td><td>Nancy</td></tr>
        <tr><td>Management</td><td>Oct. 2026</td><td>Metz</td></tr>
        <tr><td>Langues pro</td><td>Nov. 2026</td><td>Nancy</td></tr>
      </tbody>
    </table>
    <h3>Accessibilité</h3>
    <p>Locaux PMR, boucles magnétiques en amphithéâtre. Contact : formation@institut-mercure.fr (démo).</p>
  </section>
""",
    "services": """
  <section class="vt-reveal" style="padding:2rem 1.5rem;background:#f1f5f9">
    <h2>Nos engagements QHSE</h2>
    <p>Audits trimestriels, charte éthique et reporting RSE pour sites tertiaires du Grand Est.</p>
    <ol><li>Diagnostic gratuit sous 72 h</li><li>Plan d'action chiffré</li><li>Équipes formées SST</li><li>Interlocuteur unique Moselle</li></ol>
    <h3>Références</h3>
    <p>Technopoles de Metz, cliniques privées, immeubles tertiaires Thionville-Yutz.</p>
    <form style="max-width:28rem;margin-top:1.5rem" action="#" method="get">
      <label>Société <input type="text" style="width:100%;padding:.5rem"></label>
      <label>Surface (m²) <input type="number" style="width:100%;padding:.5rem"></label>
      <button type="submit" style="margin-top:.5rem;padding:.5rem 1rem">Demander un audit (démo)</button>
    </form>
  </section>
""",
    "banque": """
  <section class="vt-reveal" style="padding:2rem 1.5rem">
    <h2>Agences de proximité</h2>
    <p>Thionville centre, Yutz, Metz Sablon, Forbach — conseillers qui connaissent le tissu local.</p>
    <h3>FAQ</h3>
    <details><summary>Ouverture le samedi ?</summary><p>Oui, 9 h–12 h en agence Thionville.</p></details>
    <details><summary>Prêt jeune actif ?</summary><p>Taux préférentiel Moselle-Est sous conditions.</p></details>
    <details><summary>Virement instantané ?</summary><p>Gratuit sur l'application Verlaine.</p></details>
  </section>
""",
    "etablissement": """
  <section class="vt-reveal" style="padding:2rem 1.5rem;background:#2a221c;color:#f5efe6">
    <h2>Séminaires &amp; événements</h2>
    <p>Salles modulables 10–120 personnes, pause café terroir et partenariat traiteurs nancéiens.</p>
    <ul><li>Wi-Fi fibre</li><li>Parking 80 places</li><li>Navette gare TGV 8 min</li></ul>
    <form style="display:grid;gap:.5rem;max-width:24rem" action="#" method="get">
      <label>Dates <input type="text"></label><label>Participants <input type="number"></label>
      <button type="submit">Demander un devis (démo)</button>
    </form>
  </section>
""",
    "automobile": """
  <section class="vt-reveal" style="padding:2rem 1.5rem">
    <h2>Prestations atelier</h2>
    <ul><li>Entretien constructeur préservé</li><li>Climatisation &amp; diagnostic électronique</li><li>Pneus toutes saisons — stock Moselle</li><li>Véhicule de courtoisie</li></ul>
    <h3>Horaires</h3>
    <p>Lun–ven 7 h30–19 h · sam 8 h–12 h · Plappeville</p>
  </section>
""",
    "chocolatier": """
  <section class="vt-reveal" style="padding:2rem 1.5rem">
    <h2>Coffrets &amp; entreprises</h2>
    <p>Personnalisation logo, livraison Grand Est 72 h. Ateliers team-building le vendredi.</p>
    <h3>Allergènes</h3>
    <p>Traces possibles : lait, fruits à coque. Fiches détaillées en boutique Nancy.</p>
  </section>
""",
    "immobilier": """
  <section class="vt-reveal" style="padding:2rem 1.5rem">
    <h2>Services vendeur / acquéreur</h2>
    <p>Estimation gratuite, home staging, gestion locative et syndic de copropriété.</p>
    <h3>Estimation en ligne</h3>
    <form action="#" method="get" style="display:grid;gap:.5rem;max-width:20rem">
      <label>Adresse <input type="text"></label><label>Surface <input type="number"></label>
      <button type="submit">Estimer (démo)</button>
    </form>
  </section>
""",
    "juridique": """
  <section class="jur-extra vt-reveal" style="padding:2rem 1.5rem;border-top:2px solid #c9a227;max-width:900px;margin:0 auto">
    <h2>Honoraires transparents</h2>
    <p>Forfait création SASU dès 890 € HT. Abonnement PME : conseil illimité par e-mail.</p>
    <h3>Barreau &amp; déontologie</h3>
    <p>Avocats inscrits au barreau de Metz. Secret professionnel strict.</p>
  </section>
""",
    "architecture": """
  <section class="vt-reveal" style="padding:2rem 1.5rem;border-top:3px solid #0a0a0a">
    <h2>Approche</h2>
    <p>Matériaux biosourcés, performance énergétique et dialogue avec les ABF sur le patrimoine messin.</p>
    <p>MOE, concours, OPC — équipe 12 personnes à Metz.</p>
  </section>
""",
    "fitness": """
  <section class="vt-reveal" style="padding:2rem 1.5rem">
    <h2>Tarifs</h2>
    <table class="table"><tr><td>Mensuel</td><td>39 €</td></tr><tr><td>Annuel</td><td>399 €</td></tr><tr><td>Pass 10 séances</td><td>89 €</td></tr></table>
    <p>Essai gratuit 7 jours — sans engagement.</p>
  </section>
""",
    "photographie": """
  <section class="vt-reveal" style="padding:2rem 1.5rem;text-align:center">
    <h2>Prestations</h2>
    <p>Mariages, corporate, reportage industriel Moselle. Déplacements Grand Est.</p>
    <p>Livraison galerie privée sous 15 jours.</p>
  </section>
""",
    "technologie": """
  <section class="vt-reveal" style="padding:2rem 1.5rem">
    <h2>Certifications</h2>
    <p>ISO 27001, hébergement souverain, support 24/7 francophone.</p>
    <h2>Clients</h2>
    <p>Industrie, santé, collectivités lorraines.</p>
  </section>
""",
    "restauration": """
  <section class="vt-reveal" style="padding:2rem 1.5rem;text-align:center">
    <h2>Réservation</h2>
    <p>Groups 8+ : menu dégustation 48 €. Terrasse ombragée mai–septembre.</p>
    <p>Cave 120 références — vins de Moselle.</p>
  </section>
""",
    "beaute": """
  <section class="vt-reveal" style="padding:2rem 1.5rem">
    <h2>Forfaits</h2>
    <ul><li>Éclat 1 h — 75 €</li><li>Rituel spa 2 h — 140 €</li><li>Journée bien-être — 220 €</li></ul>
    <p>Carte cadeau disponible en boutique Nancy.</p>
  </section>
""",
    "odontologie": """
  <section class="vt-reveal" style="padding:2rem 1.5rem">
    <h2>Urgences</h2>
    <p>Créneaux réservés chaque jour 11 h–12 h et 17 h–18 h.</p>
    <p>3D intra-oral, scanners sans empreinte classique.</p>
    <form action="#" method="get" style="display:grid;gap:.5rem;max-width:20rem">
      <label>Nom <input type="text"></label><label>Téléphone <input type="tel"></label>
      <button type="submit">Rappel (démo)</button>
    </form>
  </section>
""",
    "industrie": """
  <section class="vt-reveal" style="padding:2rem 1.5rem">
    <h2>Capacités</h2>
    <p>Usinage 3 et 5 axes, séries 50–50 000 pièces. Matières : acier, inox, aluminium.</p>
    <p>Certification ISO 9001 — délais moyens 3 semaines.</p>
  </section>
""",
    "association": """
  <section class="vt-reveal" style="padding:2rem 1.5rem;background:#fff">
    <h2>Comment aider</h2>
    <p>Bénévolat cuisine, maraude hiver, don en ligne. Reçu fiscal pour les dons.</p>
    <form action="#" method="get" style="display:grid;gap:.5rem;max-width:18rem">
      <label>Montant <input type="number" min="5" value="20"></label>
      <button type="submit">Faire un don (démo)</button>
    </form>
  </section>
""",
}


def expand(slug: str) -> None:
    p = ROOT / slug / "index.html"
    if not p.exists() or slug not in EXTRA:
        return
    html = p.read_text(encoding="utf-8")
    block = EXTRA[slug]
    if block.strip()[:30] in html:
        return
    for anchor in ("<footer", "</main>", '<p class="hub-back"'):
        if anchor in html:
            html = html.replace(anchor, block + "\n  " + anchor, 1)
            break
    p.write_text(html, encoding="utf-8")
    print("expanded", slug)


if __name__ == "__main__":
    for s in EXTRA:
        expand(s)
    print("done")
