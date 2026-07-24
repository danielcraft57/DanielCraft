# Chapitre 15 - Atelier : CLI utile

Objectif : transformer un script "en dur" en outil avec arguments. Tu dois pouvoir changer de fichier et d'eleve sans editer le code.

## Etapes

1. Reprends (ou recree) un script qui calcule la moyenne d'un eleve depuis un CSV.
2. Ajoute `argparse` avec `--fichier` (obligatoire) et `--eleve` (obligatoire).
3. Ajoute `--seuil` optionnel (float). Si present, affiche aussi combien de notes sont >= seuil pour cet eleve.
4. Ajoute `--verbose` (`store_true`). En verbose, logue chaque ligne retenue (via `logging` ou `print` clairement marque).
5. Verifie que `python script.py -h` affiche une aide comprehensible en francais.
6. Teste au moins trois lancements : eleve connu, eleve inconnu, fichier inexistant.

## Criteres de reussite

- L'aide `-h` explique chaque option sans jargon inutile.
- Eleve inconnu -> message du type "Aucune note pour X", code retour non zero possible (`sys.exit(1)`).
- Fichier manquant -> message clair.
- Aucune valeur secrete, aucun chemin absolu grave dans le code (chemins passes en arguments).

## Exemple d'appel

```text
python moyenne_cli.py --fichier data/notes.csv --eleve Alice --seuil 12 --verbose
```

## Bonus

Accepte un argument positionnel `fichier` a la place de `--fichier`, et garde `--eleve`. Habitue-toi aux deux styles.

## Piege

Tout valider "plus loin" dans le code alors qu'argparse peut deja exiger les options. Si `--eleve` manque, mieux vaut le refus immediat d'argparse qu'un `None` mysterieux au milieu du calcul.

## A toi

Montre a quelqu'un (ou a toi-meme demain) uniquement l'aide `-h` et un exemple d'appel. Si on comprend sans lire le source, l'atelier est reussi. C'est l'esprit des petits outils DanielCraft : utilisables, pas seulement "techniquement corrects".
