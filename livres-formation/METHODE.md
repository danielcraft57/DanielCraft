# Methode - Creer un livre de formation

Recette issue des livres HTML/CSS, JavaScript, Python, Git et Commerce. A suivre pour les prochains.

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

- Markdown, phrases courtes
- Exemples concrets + section "A toi" / "En vrai"
- H1 : `# Chapitre N - Titre` (ou titre libre pour quiz/bravo)
- H2 pour les sous-parties (ils deviennent cliquables dans le sommaire)

## 4. Images et schemas

### Prompts

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
| JavaScript | `pdf/javascript-les-bases.pdf` | ~51 pages | vert |
| Python | `pdf/python-les-bases.pdf` | ~55 pages | bleu encre + abricot (`theme="python"`) ; exceptions + classes |
| Git / GitHub | `pdf/git-les-bases.pdf` | ~49 pages | graphite + corail (`theme="git"`) ; stash, undo, PR |
| Commerce | `pdf/commerce-les-bases.pdf` | ~38 pages | sarcelle + or sable (`theme="commerce"`) |

## 9. Suites possibles

- Marketing digital debutant  
- Communication  
- Page site pour telecharger les PDF  
