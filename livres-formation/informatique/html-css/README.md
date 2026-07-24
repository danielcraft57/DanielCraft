# HTML & CSS - Les bases

Livre de formation. Langage simple. On part de zero.

## Plan du livre

1. Salut, c'est quoi une page web ?
2. Ton premier fichier HTML
3. Les balises, c'est des etiquettes
4. Titres, textes, paragraphes
5. Liens et images
6. Listes et tableaux
7. Les formulaires (demander des infos)
8. CSS : on habille la page
9. Couleurs, polices, tailles
10. Les boites (margin, padding, border)
11. Flexbox : ranger les blocs
12. Un site qui marche sur telephone
13. Mini-projet : ta page perso
14. Ce qu'il faut retenir + suite

## Fichiers

| Fichier | Role |
|---------|------|
| `livre.html` | Livre complet, joli a l'ecran et a l'impression |
| `chapitres/` | Sources texte (14 chapitres) |
| `build_livre.py` | Assemble le HTML + PDF dans `../../pdf/html-css-les-bases.pdf` |

Rebuild :

```powershell
python livres-formation\informatique\html-css\build_livre.py
python livres-formation\informatique\html-css\build_livre.py --eco
```

Le build :
- compresse les images (`images/print/*.jpg`)
- genere le HTML + PDF
- ajoute metadonnees (auteur **DanielCraft**), numeros de page, signets

`--eco` genere aussi `html-css-les-bases-eco.pdf` (plus soft pour l'impression).

Images sources dans `images/`, versions print dans `images/print/`.

## Style

Voir `../../DIRECTIVES.md`. Phrases courtes. Comme entre amis.
