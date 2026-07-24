# Methode - Creer un livre de formation

Recette issue du premier livre (HTML/CSS). A suivre pour JS, commerce, marketing, etc.

## 0. Regles de fond (toujours)

Voir `DIRECTIVES.md` :
- Ton naturel, simple, comme entre amis
- Un enfant doit pouvoir comprendre
- Apostrophes droites `'`
- Tirets simples `-` seulement (pas de tirets cadratins)
- Auteur PDF / metadonnees : **DanielCraft**

## 1. Creer le dossier du livre

Exemple pour un livre "javascript" :

```
livres-formation/informatique/javascript/
  chapitres/          # 01-xxx.md ... 16-bravo.md
  images/             # sources PNG + schemas SVG
  images/print/       # JPG compresses (genere)
  build_livre.py      # assemble HTML + PDF
  livre.html          # genere
  README.md
```

PDF final : `livres-formation/pdf/<slug>-les-bases.pdf`

## 2. Plan des chapitres (modele HTML/CSS)

1. C'est quoi / pourquoi
2. Premier fichier / setup
3-7. Concepts de base (petits, avec "A toi")
8-12. Concepts un cran au-dessus
13. Mini-projet concret
14. Recap
15. Quiz QCM + corriges
16. Bravo + image felicitation

Vise plusieurs dizaines de pages une fois mis en page.

## 3. Ecrire les chapitres

- Fichiers markdown courts, phrases courtes
- Exemples de code simples
- Eviter le jargon ; si un mot technique est obligatoire, l'expliquer tout de suite
- Titre H1 du type : `# Chapitre N - Titre clair`

## 4. Images et schemas

### Prompts

Range dans :
- `livres-formation/prompts/images/`
- `livres-formation/prompts/schemas/`

Toujours preciser :
> Tout texte visible dans l'image doit etre en FRANCAIS. Aucun mot anglais.

### Schemas critiques (box model, flexbox, etc.)

Preferer des **SVG faits main** (texte FR garanti), puis les rasteriser en PNG via Playwright.

Les illustrations "ambiance" (couverture, page perso, bravo) peuvent etre generees en image, puis copiees dans `images/`.

### Compression

Le `build_livre.py` cree `images/print/*.jpg` (largeur max ~1400, qualite ~75).

## 5. Build HTML + PDF

Script type `build_livre.py` (copier/adapter celui de `html-css/`) :

1. Compresse les images
2. Assemble `livre.html` (CSS print soigne)
3. Genere le PDF avec **Playwright** (`page.pdf`, fond + pieds de page)
4. Enrichit avec PyPDF2 : metadonnees + signets

```powershell
python livres-formation\informatique\<livre>\build_livre.py
python livres-formation\informatique\<livre>\build_livre.py --eco
```

### Pieges deja vus (a ne pas refaire)

- `break-inside: avoid` sur de gros chapitres -> pages blanches / trous
- Images en `width:100%` sans `max-height` -> image pleine page
- `merge_page` + `compress_content_streams` sur PDF Chrome -> pages blanches
- Texte anglais dans les images IA -> passer par SVG pour les schemas
- Chrome CLI `--print-to-pdf` coupe parfois la fin -> preferer Playwright

### CSS print utile

- Images : `max-height` ~55mm, centrees
- Titres : `break-after: avoid`
- Chapitres : `break-inside: auto`
- Couverture : pas de `min-height: 100vh`
- Orphelins / veuves : `orphans/widows: 3`

## 6. Checklist avant de dire "livre pret"

- [ ] 14+ chapitres + quiz + bravo
- [ ] Langage simple, directive style OK
- [ ] Images/schemas en francais
- [ ] PDF genere, pages avec du vrai contenu (pas blanches)
- [ ] Metadonnees : Author=DanielCraft, Title, Subject
- [ ] Signets (couverture, sommaire, chapitres)
- [ ] Numeros de page en pied
- [ ] README du livre a jour

## 7. Structure globale du depot

```
livres-formation/
  DIRECTIVES.md
  METHODE.md          # ce fichier
  README.md
  prompts/images/
  prompts/schemas/
  pdf/                # PDF telechargeables
  informatique/
    html-css/
    javascript/       # suivant
  commerce/
  marketing/
  communication/
```

## 8. Ordre de travail recommande

1. Plan + dossiers
2. Chapitres markdown
3. Prompts + images/SVG
4. Adapter `build_livre.py`
5. Build + relecture visuelle PDF
6. Quiz + bravo
7. Commit sur la branche livres-formation
