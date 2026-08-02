# Catalogue - Niveaux, packs et vente site

Organisation validee : **pas de refonte totale**. On garde les livres unitaires, on les classe, on vend aussi en **packs**.

## Vente sur danielcraft.fr

- Catalogue searchable : `/livres` (moteur style nos-offres / blog)
- Fiches produit : `/livres/<slug>/`
- Source de verite : `src/data/livres.json` (categories, niveaux, mots-cles, prix)
- **Prix d'appel** : **0,50 € TTC** / livre
- **Pack de la semaine** : `deal_of_the_week.slug` dans `livres.json` (bandeau sous la recherche)
- Rotation : changer le slug + relancer `python scripts/update_livres_prices_packs.py` puis le build
- Packs dispo : debutant-code, web, python, sql, ia, finance, securite, commerce, ecommerce, git, jvm, backend, mobile, systeme, marketing-com
- PDF locaux : `livres-formation/pdf/` (ignores par git, deploy a part)

## Niveaux

| Niveau | Role | Exemples actuels |
|--------|------|------------------|
| **Base** | Entree, "les bases / essentiel" | HTML/CSS, JS, Python, TS, Git, Marketing, Finance bases, IA essentiel... |
| **Intermediaire** | Suite / pratique | HTML/CSS suite, JS suite, Python pratique, Git equipe, Vente avancee... |
| **Expert** | Perf, archi, cas durs, prod | SQL expert, Securite expert, Deep learning... |
| **Securite** | Transversal | Securite web bases / inter / expert |

Regle : ne pas fusionner base+inter+expert dans un seul PDF monstre. Un PDF = un niveau clair.

## Packs de vente (MVP)

| Pack | Contenu vise |
|------|----------------|
| **Web** | HTML/CSS base+suite, JS base+suite, TypeScript base (+ secu front plus tard) |
| **Python** | Python bases + pratique (+ expert / data plus tard) |
| **Data / SQL** | SQL base → inter → expert (+ lien Python data) |
| **Finance** | Finance bases + actions/obligations + derives + forex + crypto |
| **IA** | IA essentiel + ML + DL |
| **Securite** | Livre(s) securite (add-on ou pack a part) |

Vente unitaire reste possible (entree de gamme).

## Categories dossier (`livres-formation/`)

| Dossier | Theme site |
|---------|------------|
| `informatique/` | Langages, web, SQL, Git, securite |
| `ia/` | IA bases, ML, DL |
| `finance/` | Bases, actions, derives, forex, crypto |
| `commerce/` | Vente, e-commerce, dropshipping |
| `marketing/` | Marketing bases |
| `communication/` | Communication bases |

## Images

Tout texte visible dans une image generee = **francais uniquement**. Relire avant commit.
PDF et PNG livres = hors git (voir `.gitignore`).
