# Chapitre 10 - datetime pratique

Les dates sont partout : horodatage d'un log, "derniere mise a jour", filtrer des lignes apres une certaine date, afficher un jour lisible. Le module **datetime** de la bibliotheque standard couvre l'essentiel. Tu n'as pas besoin d'une these sur les fuseaux pour etre utile demain matin. Tu as besoin de trois gestes : maintenant, formater, parser.

Une date, c'est un objet Python que tu peux comparer, additionner (avec **timedelta**), formater en texte (`strftime`), ou parser depuis un texte (`strptime`). Ne compare jamais des dates en string : `"9/7/2026"` et `"10/7/2026"` mentent en ordre alphabetique. Parse d'abord, compare ensuite. Lea visualise un calendrier pose sur le bureau : les objets date, c'est ca. Les chaines, c'est l'etiquette colle dessus pour l'humain.

On reste pratique. Pas de theorie profonde sur les fuseaux horaires (c'est un monde a part). Juste de quoi etre a l'aise au quotidien. Sam filtre les evenements du mois dans un CSV. Max horodate ses exports factures. Lea affiche "mis a jour le ..." dans ses rapports clients. Trois usages, une meme boite a outils. Chez DanielCraft, on insiste : ne compare jamais des dates en string. Cette regle seule evite des bugs absurdes qui font perdre une apres-midi.

## Ce que ce n'est pas

`datetime`, ce n'est pas "gestion complete du temps mondial". Ce n'est pas non plus une raison de paniquer devant `%Y-%m-%d`. Ce n'est pas obligatoire d'apprendre tous les motifs d'un coup. Et ce n'est surtout pas interchangeable avec un tri alphabetique de chaines "qui a l'air de marcher". Ca ment souvent.

:::attention
Comparer des dates en chaines, c'est un piege classique. `"9/7"` passe apres `"10/7"` en alphabetique. Parse en `date`, puis compare.
:::

## Maintenant

```python
from datetime import datetime, date, timedelta

maintenant = datetime.now()
aujourd_hui = date.today()
print(maintenant)
print(aujourd_hui)
```

`date` = jour sans heure. `datetime` = jour + heure. Souvent tu as besoin de l'un ou de l'autre, pas des deux en meme temps. Max utilise `date` pour ses factures. Lea utilise `datetime` pour ses logs. Sam montre les deux le meme cours pour eviter la confusion.

## Formater pour afficher

```python
maintenant = datetime.now()
print(maintenant.strftime("%Y-%m-%d %H:%M"))
print(maintenant.strftime("%d/%m/%Y"))
```

`strftime` transforme une date en texte selon un motif. `%Y` annee sur 4 chiffres, `%m` mois, `%d` jour, `%H` heure 24h, `%M` minutes. Tu retiendras les motifs en les reutilisant. Pas besoin de les apprendre comme une poesie.

Pour un CSV ou un nom de fichier, le format ISO `2026-07-24` trie bien dans l'ordre alphabetique. Pratique. Chez DanielCraft, on le recommande des qu'on controle le format.

## Parser une chaine

Tu lis `"24/07/2026"` dans un fichier. Tu veux un vrai objet date :

```python
texte = "24/07/2026"
jour = datetime.strptime(texte, "%d/%m/%Y").date()
print(jour)
```

`strptime` = parse. `strftime` = format. Les deux utilisent le meme langage de motifs. Si le texte ne correspond pas, tu attrapes une `ValueError`. Sam fait planter volontairement avec un mauvais motif. Les eleves retiennent.

## Ajouter / retirer des jours

```python
aujourd_hui = date.today()
dans_une_semaine = aujourd_hui + timedelta(days=7)
hier = aujourd_hui - timedelta(days=1)
print(dans_une_semaine, hier)
```

`timedelta` sait aussi `hours=`, `minutes=`. Ideal pour "expire dans 48h" ou "fichier plus vieux que 30 jours". Max calcule "dans dix jours" pour ses relances devis. Lea calcule "il y a trente jours" pour purger des logs.

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

Ou laisse le format `asctime` du logging faire le travail (chapitre precedent). Sans horodatage, un log est une rumeur.

:::astuce
Pour un CSV ou un nom de fichier, prefere `YYYY-MM-DD`. Ca trie bien, ca se parse avec `fromisoformat`, ca voyage bien.
:::

## Petite histoire

Sam avait un CSV d'absences avec des dates en `JJ/MM/AAAA`. Il filtrait "a la main" en triant alphabetiquement. Resultat : septembre avant janvier, chaos total. Avec `strptime` puis comparaison de vrais objets `date`, le filtre du trimestre marche du premier coup. Lea fait pareil pour ses rapports mensuels clients.

Max horodate ses exports factures avec `strftime("%Y-%m-%d")` dans le nom de fichier. Il retrouve "le fichier de mardi" en une seconde. Petit geste, gros confort. Chez DanielCraft, on collectionne ces petits conforts : ils restent quand les tutos s'oublient.

## Erreur classique

Comparer des chaines `"9/7/2026"` et `"10/7/2026"` en ordre alphabetique... ca ment. Parse en `date`, puis compare. Autre classique : oublier que `strftime` et `strptime` ont besoin du meme motif exact. Autre piege : melanger `date` et `datetime` dans une comparaison sans conversion. Et encore : croire que "maintenant" suffit toujours - parfois tu as besoin d'une date fixe pour un rapport reproductible.

## En vrai

Affiche la date du jour en `JJ/MM/AAAA`. Calcule la date dans 10 jours. Parse une chaine de ton choix. Trois gestes, beaucoup d'usages. Puis compare deux dates parsees : sens la difference avec un tri de chaines.

## A toi

Ecris `jours_depuis(texte)` qui prend `"2026-01-15"` et retourne le nombre de jours jusqu'a aujourd'hui. Utile pour "ca fait combien de temps ?". Bonus : gere une `ValueError` si le texte est mal forme, avec un message clair. Sam utilise ce genre de fonction pour "combien de jours depuis la derniere absence". Max pour "combien de jours avant la relance devis".

:::retenir
Parse, compare, formate. Des objets date, jamais des chaines pour l'ordre.
:::
