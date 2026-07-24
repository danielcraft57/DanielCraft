# Methode - Creer un livre de formation

Recette issue des livres HTML/CSS, JavaScript, Python, Git, Commerce, E-commerce, Marketing et Communication. A suivre pour les prochains.

## 0. Regles de fond (toujours)

Voir `DIRECTIVES.md` :
- Ton naturel, simple, comme entre amis
- Un enfant doit pouvoir comprendre
- Apostrophes droites `'`
- Tirets simples `-` seulement (pas de tirets cadratins)
- Auteur PDF / metadonnees : **DanielCraft**

## 1. Structure des dossiers

```
livres-formation/
  DIRECTIVES.md
  METHODE.md              # ce fichier
  _book_lib.py            # moteur partage (markdown, CSS, PDF navigable)
  prompts/images/
  prompts/schemas/
  pdf/                    # PDF finaux telechargeables
  informatique/
    html-css/
    javascript/
    <nouveau-livre>/
  commerce/
  marketing/
  communication/
```

Un livre :

```
informatique/<slug>/
  chapitres/           # 01-...md ... quiz ... bravo
  images/              # PNG + SVG sources
  images/print/        # JPG compresses (genere)
  build_livre.py       # wrapper autour de _book_lib
  livre.html           # genere
  README.md
```

PDF : `livres-formation/pdf/<slug>-les-bases.pdf`

## 2. Plan type (19 parties)

1-14. Cours + mini projet + recap  
15-17. Ateliers / approfondissements  
18. Quiz + corriges  
19. Bravo + image felicitation  

Chaque chapitre commence sur une **nouvelle page**.

## 3. Ecriture

- Markdown, phrases courtes, **prose d'abord** (peu de puces : voir DIRECTIVES.md)
- Exemples concrets + section "A toi" / "En vrai" / "Mini defi"
- H1 : `# Chapitre N - Titre` (ou titre libre pour quiz/bravo)
- H2 pour les sous-parties (ils deviennent cliquables dans le sommaire)
- QCM : options A/B/C en puces OK

## 4. Images et schemas

**Chaque livre** : couverture + felicitation + plusieurs schemas cles (SVG FR -> PNG).
Ne pas livrer un PDF "que du texte".

Dans `prompts/images/` et `prompts/schemas/`. Toujours :

> Tout texte visible dans l'image doit etre en FRANCAIS. Aucun mot anglais.

### Schemas critiques

**SVG faits main** (texte FR garanti) -> raster PNG via Playwright.  
Illustrations ambiance (couverture, bravo) : generation image OK, puis copie dans `images/`.

### Compression

`build_livre.py` cree `images/print/*.jpg`.

## 5. Build HTML + PDF

1. Compresse images  
2. Assemble `livre.html` via `_book_lib.md_to_html`  
   - ids sur H1/H2  
   - sommaire chapitres + sous-chapitres  
   - CSS print : pas de gros trous, code court garde ensemble  
3. PDF avec **Playwright** (fond + pieds de page)  
4. **`finalize_pdf` (PyMuPDF)** :  
   - metadonnees (auteur DanielCraft)  
   - **liens cliquables du sommaire** (GOTO pages)  
   - signets lateraux (chapitres + sous-chapitres)  

```powershell
python livres-formation\informatique\<livre>\build_livre.py
```

### Pieges deja vus

| Probleme | Cause | Fix |
|----------|--------|-----|
| Pages blanches | `break-inside:avoid` + merge/compress PDF | CSS print + Playwright + pas de compress agressif |
| Images pleine page | `width:100%` sans max-height | `max-height` ~55mm |
| Texte anglais sur schemas | IA | SVG manuel FR |
| Sommaire non cliquable | Chromium PDF sans vrais liens | `finalize_pdf` PyMuPDF injecte les liens |
| Fin du PDF coupee | Chrome CLI | Playwright |

## 6. Checklist "livre pret"

- [ ] 15+ chapitres + ateliers + quiz + bravo  
- [ ] Directive style OK  
- [ ] Images/schemas en francais  
- [ ] Chaque chapitre = nouvelle page  
- [ ] Sommaire : liens cliquables verifies dans un lecteur PDF  
- [ ] Signets lateraux OK  
- [ ] Metadonnees Author=DanielCraft  
- [ ] Dizaines de pages (viser 40+)  

## 7. Ordre de travail

1. Plan + dossier  
2. Chapitres markdown  
3. Prompts + images/SVG  
4. Adapter `build_livre.py` (copier un existant, changer titres/images/fichiers)  
5. Build + test clics sommaire  
6. Commit sur `feature/livres-formation`  

## 8. Deja livre

| Livre | PDF | Notes |
|-------|-----|--------|
| HTML/CSS | `pdf/html-css-les-bases.pdf` | ~51 pages | vert |
| HTML/CSS - La suite | `pdf/html-css-la-suite.pdf` | ~40+ pages | bleu-vert + cyan (`theme="htmlcss2"`) ; Grid, variables, a11y |
| JavaScript | `pdf/javascript-les-bases.pdf` | ~51 pages | vert |
| JavaScript - La suite | `pdf/javascript-la-suite.pdf` | ~40+ pages | indigo + lime (`theme="javascript2"`) ; fetch, async, modules |
| Python | `pdf/python-les-bases.pdf` | ~55 pages | bleu encre + abricot (`theme="python"`) ; exceptions + classes |
| Python - Pratique | `pdf/python-pratique.pdf` | ~40+ pages | charcoal + menthe (`theme="python2"`) ; CSV, CLI, API, venv |
| Git / GitHub | `pdf/git-les-bases.pdf` | ~49 pages | graphite + corail (`theme="git"`) ; stash, undo, PR |
| Git - En equipe | `pdf/git-en-equipe.pdf` | ~40+ pages | midnight + ambre (`theme="git2"`) ; flux, revue, CI, rebase |
| Commerce | `pdf/commerce-les-bases.pdf` | ~32-38 pages | sarcelle + or ; prose |
| Commerce - Vente avancee | `pdf/vente-avancee.pdf` | ~40+ pages | teal + or sable (`theme="commerce2"`) ; pipeline, closing |
| E-commerce | `pdf/ecommerce-les-bases.pdf` | ~35+ pages | ocean + orange ; clients, dropshipping, tendances 2026 |
| Marketing digital | `pdf/marketing-les-bases.pdf` | ~35+ pages | prune + peche (`theme="marketing"`) ; cible, contenu, canaux, mesure |
| Communication | `pdf/communication-les-bases.pdf` | ~46 pages | bordeaux + miel (`theme="communication"`) ; message, ecoute, pitch, crise |

## 9. Suites possibles

- Marketing / communication avances
- Page site pour telecharger les PDF  

