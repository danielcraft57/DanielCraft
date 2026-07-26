# Chapitre 15 - Atelier : CLI utile

Objectif : transformer un script "en dur" en outil avec **arguments**. Tu dois pouvoir changer de fichier et d'eleve sans editer le code. Duree : 30 a 45 minutes. Materiel : ton script CSV ou equivalent, Python 3, terminal.

Max avait un script qui marchait... chez lui, avec son fichier, pour Alice. Lea lui a dit : "Ajoute **argparse**, et montre-moi `-h`." C'est cet atelier. Sam en profite pour rendre son outil de notes utilisable par un collegue sans formation Python. Chez DanielCraft, un script sans `-h` lisible, c'est un brouillon, pas un outil. Tu vas sentir la difference entre "ca marche si je connais le code" et "ca marche si je lis l'aide".

Avant : ouvrir l'editeur, changer `"Alice"` en `"Bob"`, sauver, lancer. Apres : `python moyenne_cli.py --fichier data/notes.csv --eleve Bob`. Meme calcul. Autre posture. Les options obligatoires refusent tot. Les options optionnelles enrichissent. Les echecs (fichier absent, eleve inconnu) parlent francais. C'est le passage "script perso" vers "outil partageable".

:::astuce
Montre `-h` a quelqu'un (ou a toi demain). Si on comprend sans lire le source, l'atelier est deja a moitie gagne.
:::

## Exercice 1 - Arguments de base (10 min)

Reprends (ou recree) un script qui calcule la moyenne d'un eleve depuis un CSV. Ajoute `argparse` avec `--fichier` (obligatoire) et `--eleve` (obligatoire). Verifie que `python script.py -h` affiche une aide comprehensible en francais. Si l'aide est en jargon, reecris les `help=`.

## Exercice 2 - Options avancees (10 min)

Ajoute `--seuil` optionnel (float). Si present, affiche aussi combien de notes sont >= seuil pour cet eleve. Ajoute `--verbose` (`store_true`). En verbose, logue chaque ligne retenue (via `logging` ou `print` clairement marque). Lea adore `--verbose` quand un client dit "c'est faux" : elle voit quelles lignes ont ete prises.

## Exercice 3 - Cas d'echec (10 min)

Teste au moins trois lancements : eleve connu, eleve inconnu, fichier inexistant. Eleve inconnu -> message du type "Aucune note pour X", code retour non zero possible (`sys.exit(1)`). Fichier manquant -> message clair. Aucune valeur secrete, aucun chemin absolu grave dans le code. Si argparse refuse une option manquante, c'est une victoire, pas un echec.

## Exercice 4 - Montrer a quelqu'un (5 min)

Montre a quelqu'un (ou a toi-meme demain) uniquement l'aide `-h` et un exemple d'appel. Si on comprend sans lire le source, l'atelier est reussi. Sam fait souvent cet exercice avec un collegue non tech : "lance ca pour Alice".

## Exemple d'appel

```text
python moyenne_cli.py --fichier data/notes.csv --eleve Alice --seuil 12 --verbose
```

## Petite histoire

Max a montre son `-h` a Lea. Lea a dit : "Je comprends." Max a sourit. Deux jours plus tard, il a change de CSV fournisseur sans toucher une ligne de code. Sam a ajoute `--seuil` pour reperer les eleves sous la moyenne. Chez DanielCraft, on mesure le succes d'un CLI a une question : demain matin, fatigue, est-ce que tu retrouves comment l'appeler sans rouvrir le source ?

## Livrable

Un script `moyenne_cli.py` (ou nom equivalent) avec argparse complet, trois tests manuels documentes (eleve connu, inconnu, fichier absent), et une capture ou note de l'aide `-h`.

## Criteres de reussite

L'aide `-h` explique chaque option sans jargon inutile. Eleve inconnu et fichier manquant produisent des messages clairs. Aucun secret, aucun chemin absolu en dur. Si tu coches ces trois points, tu as un outil partageable, pas seulement un script perso.

## Bonus

Accepte un argument positionnel `fichier` a la place de `--fichier`, et garde `--eleve`. Habitue-toi aux deux styles. Ou ajoute `--sortie` pour ecrire aussi un mini CSV resume. Lea ajoute souvent `--sortie` sur ses exports clients. Max prefere rester simple : terminal seulement. Sam demande les deux styles pour que les eleves voient la difference.

## Erreur classique

Tout valider "plus loin" dans le code alors qu'argparse peut deja exiger les options. Si `--eleve` manque, mieux vaut le refus immediat d'argparse qu'un `None` mysterieux au milieu du calcul. Autre piege : laisser un chemin `C:\Users\...` en dur "juste pour tester" et l'oublier. Autre piege : une aide `-h` en anglais cryptique alors que ton public lit le francais.

:::attention
`required=True` des le debut bat un `None` mysterieux au milieu du calcul. Laisse argparse refuser tot.
:::

## En vrai

Lance ton script avec `-h`. Copie l'aide dans un fichier `AIDE.txt` ou en commentaire en haut du script. Relance demain sans ouvrir l'editeur : est-ce que tu retrouves les options ?

## A toi

Documente en haut du fichier deux exemples d'appel commentes. Ton futur toi fatigue te remerciera. C'est l'esprit des petits outils DanielCraft : utilisables, pas seulement "techniquement corrects".

Quand tu bloques sur une option, relis l'aide `-h` a voix haute. Si tu hesites, un collegue hesite aussi. Lea passe souvent cinq minutes a reecrire les `help=` avant de livrer. Max a appris a forcer trois lancements (ok, inconnu, fichier absent) avant de dire "c'est fini". Sam note ces trois lancements dans un commentaire en haut du fichier. Chez DanielCraft, ce rituel suffit a transformer un script perso en outil partageable.

:::retenir
Un CLI utile : options claires, `-h` lisible, echecs propres, zero chemin en dur.
:::
