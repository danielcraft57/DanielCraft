# Chapitre 18 - Organiser un petit projet

Un script unique, c'est bien pour apprendre. Des qu'il y a CSV + API + CLI + tests, un peu d'ordre evite le chaos. Pas besoin d'architecture d'entreprise. Juste un dossier clair. Un nouvel arrivant (souvent toi dans trois semaines) doit comprendre en trente secondes ou cliquer.

Trois zones : donnees (`data/`), code (`src/` ou fichiers a plat), tests (`tests/`). A cote : venv (ignore), requirements (partage), secrets (`.env` ignore, `.env.example` partage). Le point d'entree parse les arguments et appelle la logique. La logique ne connait pas argparse. Lea dessine parfois ces zones sur papier avant de deplacer quoi que ce soit. Max aussi, depuis qu'il a perdu un CSV dans un dossier "Nouveau dossier (3)".

Chez DanielCraft, on vise exactement ca. Lea range ses scripts clients dans une arborescence simple. Max a supprime ses `script_final_v2_REEL.py` et un seul dossier propre. Sam partage son projet notes avec un README de quinze lignes que tout le monde comprend. L'ordre n'est pas du perfectionnisme. C'est du temps gagne et de la peur en moins.

## Ce que ce n'est pas

Organiser, ce n'est pas recopier l'arborescence d'un monorepo Google. Ce n'est pas non plus renommer vingt fois pour le plaisir. Ce n'est pas "src obligatoire des la ligne 1". Si deux fichiers suffisent, reste a plat. Et ce n'est surtout pas committer le `.venv` "pour etre sur" : c'est lourd, inutile, parfois fragile.

:::retenir
Ecris la structure sur papier avant de deplacer les fichiers. Dix minutes d'ordre economisent une heure de chasse.
:::

## Arborescence type

```text
mon-outil/
  .venv/
  .gitignore
  .env.example
  requirements.txt
  README.md
  data/
    notes.csv
  src/
    mon_outil/
      __init__.py
      cli.py
      notes.py
      meteo.py
  tests/
    test_notes.py
```

Variante plus simple, tout a plat au debut :

```text
mon-outil/
  .venv/
  requirements.txt
  resume.py
  notes_lib.py
  data/
  tests/
```

L'important : separer donnees, code, tests. Ne pas melanger le CSV de prod et les brouillons sans nom. Sam colle un fichier `notes.exemple.csv` a cote du vrai, pour que les eleves ne cassent pas les donnees reelles.

## requirements.txt

```text
requests==2.32.3
pytest==8.3.0
```

Les versions exactes (pin) rendent les installs reproductibles. Pour un apprentissage, pinner au moins les paquets critiques.

Installation :

```text
python -m venv .venv
# activer le venv
python -m pip install -r requirements.txt
```

## README court

Quatre blocs suffisent : a quoi sert l'outil, comment installer, comment lancer (2 exemples), ou mettre sa cle si besoin (renvoi a `.env.example`). Ecris pour un humain presse, pas pour un roman. Lea lit ses README a voix haute : si elle hesite, elle raccourcit.

## .gitignore utile

```text
.venv/
.env
__pycache__/
*.pyc
.pytest_cache/
app.log
```

Tu ignores le virtuel, les secrets, le cache Python, les logs locaux. Chez DanielCraft, ce fichier est non negociable des qu'il y a un depot.

## Ou mettre le point d'entree ?

`cli.py` ou `resume.py` parse les arguments et appelle des fonctions. `notes.py` / `meteo.py` portent la logique. Les tests importent la logique, pas le parseur complet (sauf tests d'integration plus tard). Max a longtemps tout mis dans un seul fichier. Ca marchait. Puis il a voulu tester. La, ca a cesse de marcher confortablement. Decoupage.

## Variante : tout a plat au debut

Si ton projet tient en deux fichiers, ne force pas une arborescence lourde. Lea commence souvent avec `resume.py` + `notes_lib.py` + `data/` + `tests/`. Quand un troisieme module apparait (meteo, config, export), elle decoupe. La regle : separe des que tu te perds, pas avant. Sam partage ses projets eleves avec cette structure minimale. Max a migre vers `src/` seulement quand il a eu cinq scripts qui se parlaient entre eux.

## Commandes types dans le README

Un bon README inclut les commandes copiables :

```text
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python resume.py --mode notes --fichier data/notes.csv --eleve Alice
python resume.py --mode meteo --lat 48.85 --lon 2.35
pytest
```

Sam colle ce bloc en haut de ses projets eleves. Lea ajoute une ligne "Variables : voir .env.example". Max note quel venv activer selon le dossier. Dix lignes de README, zero reunion pour expliquer comment lancer.

## Petite histoire

Max avait un dossier "Nouveau dossier (3)" avec quatre versions de son script meteo. Lea lui a fait passer une heure a ranger : un dossier, un README, un requirements.txt. Le lendemain, Max a retrouve son outil en dix secondes au lieu de dix minutes. L'ordre, ce n'est pas du perfectionnisme. C'est du temps gagne.

Autre scene : Sam recoit un projet eleve sans README. Il ouvre, ferme, renvoie : "quinze lignes, puis on regarde le code". L'eleve rale. Puis remercie. Chez DanielCraft, on valide ce rituel sans honte.

## Erreur classique

Un dossier `Nouveau dossier (3)` avec `script_final_v2_REEL.py`. Ou installer sans `requirements.txt` et ne plus savoir quoi recreer sur une autre machine. Ou committer `.venv` (lourd, inutile, parfois fragile). Ou melanger donnees reelles et brouillons de test sans distinction. Autre piege : six fichiers `utils.py` qui s'appellent tous pareil dans des sous-dossiers. Nomme clairement.

:::attention
Ne committe jamais `.env` ni `.venv`. Partage `.env.example` et `requirements.txt`. C'est le minimum vital.
:::

## En vrai

Reprends ton mini-projet. Range-le dans une arborescence simple. Ajoute `requirements.txt`, `.env.example`, un README de 15 lignes. Supprime les fichiers morts. Lance depuis le README sans tricher. Si tu bloques, le README est trop flou : corrige-le.

## A toi

Ecris la structure choisie sur papier (ou dans le README) avant de deplacer les fichiers. Dix minutes d'ordre economisent une heure de "ou j'avais mis ca ?". Bonus : demande a quelqu'un de lancer ton outil uniquement avec le README. Note ou il bute. Si la personne bloque, corrige le README avant de "expliquer a l'oral" : l'oral ne voyage pas avec le depot.

:::astuce
Si quelqu'un lance ton outil uniquement avec le README et bute, c'est le README qui est trop flou - pas ton collegue.
:::
