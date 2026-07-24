# Chapitre 9 - logging basique

`print` est parfait pour apprendre. Pour un script qui vit un peu, `logging` est plus souple : niveaux (info, warning, error), format, et possibilite d'ecrire dans un fichier sans changer toute la logique.

Chez DanielCraft, on garde `print` pour l'affichage utilisateur du CLI, et `logging` pour ce qui se passe "sous le capot".

## Premier logger

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s",
)

logging.info("Demarrage du script")
logging.warning("Fichier presque vide")
logging.error("Echec de l'appel API")
```

Tu verras des lignes avec le niveau. Si tu mets `level=logging.WARNING`, les `info` disparaissent. Pratique : en prod tu baisses le bruit, en debug tu montes le detail.

## Niveaux en une idee

`DEBUG` : detail pour developper. `INFO` : deroulement normal. `WARNING` : bizarre mais on continue. `ERROR` : ca a rate. `CRITICAL` : tres grave.

Pour debuter, `INFO` + `ERROR` suffisent souvent. Ajoute `DEBUG` quand tu chasses un bug.

## Logger nomme

Dans un projet a plusieurs fichiers, on evite le logger racine partout. Pattern courant :

```python
import logging

logger = logging.getLogger(__name__)

def moyenne(valeurs):
    logger.debug("Nb valeurs : %s", len(valeurs))
    if not valeurs:
        logger.error("Liste vide")
        return None
    return sum(valeurs) / len(valeurs)
```

`%s` et les arguments separes : le message n'est formate que si le niveau est actif. Habitude propre.

Configure `basicConfig` une seule fois, cote point d'entree (`main`), pas dans chaque module.

## Ecrire dans un fichier

```python
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",
    encoding="utf-8",
)
```

Utile pour un script lance la nuit, ou pour relire apres coup. Tu peux aussi cumuler console + fichier avec des handlers (un cran plus avance : regarde la doc quand tu en auras besoin).

## Avec requests / CSV

```python
logger.info("Lecture de %s", chemin)
logger.info("Appel API %s", url)
logger.error("HTTP %s sur %s", status, url)
```

Tu retraces l'histoire sans noyer l'utilisateur. Sur le CLI, toi tu affiches : "Impossible de charger la meteo." Dans le log : le status, l'URL, peut-etre l'exception.

## print ou logging ?

Regle simple pour un CLI : ce que l'humain doit lire comme resultat va dans `print` (la moyenne, la temperature). Ce qui explique le deroulement ou l'echec technique va dans `logging`. Tu peux tout mettre en `print` sur un script de 20 lignes. Des que ca grandit, tu seras content d'avoir separe.

## Exception + log

```python
try:
    data = fetch_json(url)
except RuntimeError as e:
    logging.exception("Echec fetch")
    print("Impossible de recuperer les donnees.")
```

`logging.exception` (dans un `except`) ajoute la traceback au log. L'utilisateur voit une phrase calme. Toi, tu as le detail dans `app.log` ou dans la console de debug.

## Erreur classique

Logger des secrets (jetons, mots de passe). Ou laisser des centaines de `DEBUG` bruyants sans pouvoir les couper. Ou melanger `print` debug partout au point de ne plus voir le vrai resultat utilisateur. Ou appeler `basicConfig` dans trois modules differents et ne plus comprendre quel format gagne.

## En vrai

Ajoute trois logs a ton script CSV ou meteo : demarrage, succes, echec. Change le niveau INFO vers WARNING et observe ce qui reste.

## A toi

Separe clairement : un `print` pour le resume final, des `logging.info/error` pour le deroulement. Si tu peux couper le bruit en changeant un seul `level=`, c'est gagne.
