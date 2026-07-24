# Chapitre 10 - datetime pratique

Les dates sont partout : horodatage d'un log, "derniere mise a jour", filtrer des lignes apres une certaine date, afficher un jour lisible en francais. Le module `datetime` de la bibliotheque standard couvre l'essentiel.

On reste pratique. Pas de theorie profonde sur les fuseaux horaires (c'est un monde a part). Juste de quoi etre a l'aise au quotidien.

## Maintenant

```python
from datetime import datetime, date, timedelta

maintenant = datetime.now()
aujourd_hui = date.today()
print(maintenant)
print(aujourd_hui)
```

`date` = jour sans heure. `datetime` = jour + heure. Souvent tu as besoin de l'un ou de l'autre, pas des deux en meme temps.

## Formater pour afficher

```python
maintenant = datetime.now()
print(maintenant.strftime("%Y-%m-%d %H:%M"))
print(maintenant.strftime("%d/%m/%Y"))
```

`strftime` transforme une date en texte selon un motif. `%Y` annee sur 4 chiffres, `%m` mois, `%d` jour, `%H` heure 24h, `%M` minutes. Tu retiendras les motifs en les reutilisant.

Pour un CSV ou un nom de fichier, le format ISO `2026-07-24` trie bien dans l'ordre alphabetique. Pratique.

## Parser une chaine

Tu lis `"24/07/2026"` dans un fichier. Tu veux un vrai objet date :

```python
texte = "24/07/2026"
jour = datetime.strptime(texte, "%d/%m/%Y").date()
print(jour)
```

`strptime` = parse. `strftime` = format. Les deux utilisent le meme langage de motifs. Si le texte ne correspond pas, tu attrapes une `ValueError`.

## Ajouter / retirer des jours

```python
aujourd_hui = date.today()
dans_une_semaine = aujourd_hui + timedelta(days=7)
hier = aujourd_hui - timedelta(days=1)
print(dans_une_semaine, hier)
```

`timedelta` sait aussi `hours=`, `minutes=`. Ideal pour "expire dans 48h" ou "fichier plus vieux que 30 jours".

## Filtrer des lignes "du mois"

Imagine un CSV avec une colonne `jour` au format `2026-07-24` :

```python
from datetime import date
import csv
from pathlib import Path

debut = date(2026, 7, 1)
fin = date(2026, 7, 31)

with Path("data/events.csv").open(encoding="utf-8", newline="") as f:
    for ligne in csv.DictReader(f):
        j = date.fromisoformat(ligne["jour"])
        if debut <= j <= fin:
            print(ligne)
```

`fromisoformat` lit directement `YYYY-MM-DD`. Si tu controles le format de ton CSV, c'est le plus simple.

## Timestamp de log

```python
import logging
from datetime import datetime

logging.info("Evenement a %s", datetime.now().isoformat(timespec="seconds"))
```

Ou laisse le format `asctime` du logging faire le travail (chapitre precedent). L'idee : une date lisible aide a enqueter.

## Erreur classique

Comparer des chaines `"9/7/2026"` et `"10/7/2026"` en ordre alphabetique... ca ment. Parse en `date`, puis compare. Autre classique : oublier que `strftime` et `strptime` ont besoin du meme motif exact.

## En vrai

Affiche la date du jour en `JJ/MM/AAAA`. Calcule la date dans 10 jours. Parse une chaine de ton choix. Trois gestes, beaucoup d'usages.

## A toi

Ecris `jours_depuis(texte)` qui prend `"2026-01-15"` et retourne le nombre de jours jusqu'a aujourd'hui. Utile pour "ca fait combien de temps ?".
