# Chapitre 8 - Variables d'environnement

Une cle API, un mot de passe, un jeton : ca ne doit pas vivre en clair dans ton code source. Surtout si tu partages le projet, ou si tu le pousses sur Git. La bonne habitude : lire les **secrets** depuis l'environnement.

`os.environ` donne acces aux variables d'environnement du systeme (ou de ton terminal). Le code dit : "j'ai besoin d'une variable nommee API_CLE". La valeur vient de l'exterieur : le terminal, un fichier **`.env`**, ou le systeme. Si la variable manque, le script s'arrete avec un message clair. Personne ne voit le secret dans le source partage. Tu peux montrer ton code. Tu ne montres pas ta cle.

Chez DanielCraft, on dit : le code connait le nom de la variable, pas la valeur secrete. Lea stocke sa cle API meteo dans `API_CLE`, jamais dans le fichier. Max a un fichier `.env` local ignore par Git. Sam montre a ses eleves la difference entre config publique et secret.

:::attention
Une cle poussee sur GitHub est brulee. Revoque-la. Puis `.env` + `.gitignore` + `.env.example`. Pas de "juste cette fois".
:::

## Lire une variable

```python
import os

cle = os.environ.get("API_CLE")
if not cle:
    raise RuntimeError("Variable API_CLE manquante")
```

`.get` retourne `None` si absente. Tu peux aussi ecrire `os.environ["API_CLE"]`, qui leve une `KeyError` si elle n'y est pas. Pour un script clair, verifier et afficher un message explicite est souvent mieux.

## Definir la variable avant de lancer

Sous Windows PowerShell :

```text
$env:API_CLE = "valeur-secrete"
python mon_script.py
```

Sous cmd :

```text
set API_CLE=valeur-secrete
python mon_script.py
```

Sous macOS / Linux :

```text
export API_CLE=valeur-secrete
python mon_script.py
```

La variable existe pour cette session de terminal. Ce n'est pas magique dans le fichier `.py`.

## Le fichier .env

Beaucoup de projets utilisent un fichier `.env` a la racine :

```text
API_CLE=valeur-secrete
VILLE_DEFAUT=Paris
```

Ce fichier n'est pas du Python. Des outils (comme la bibliotheque `python-dotenv`) peuvent le charger dans `os.environ` au demarrage. L'idee importante, meme sans installer quoi que ce soit pour l'instant :

Tu ne commits pas `.env` (secrets). Tu commits un **`.env.example`** avec les noms de variables et des fausses valeurs.

```text
API_CLE=remplace-moi
VILLE_DEFAUT=Paris
```

Comme ca, un collegue sait quoi configurer sans voir tes vrais secrets.

## Charger .env a la main (mini version)

Pour comprendre le principe, sans dependance :

```python
from pathlib import Path
import os

def charger_env(chemin=".env"):
    p = Path(chemin)
    if not p.exists():
        return
    for ligne in p.read_text(encoding="utf-8").splitlines():
        ligne = ligne.strip()
        if not ligne or ligne.startswith("#") or "=" not in ligne:
            continue
        nom, valeur = ligne.split("=", 1)
        os.environ.setdefault(nom.strip(), valeur.strip())
```

`setdefault` ne recouvre pas une variable deja definie dans le systeme. Utile.

En pratique, pour un vrai projet, `python-dotenv` fait ca plus completement. L'essentiel est le reflexe : secrets dehors du code.

## Config non secrete

Tout n'est pas secret. Une ville par defaut, un seuil, un mode debug : variables d'environnement ou arguments CLI, selon ce qui est le plus pratique. Les secrets, eux, passent presque toujours par l'environnement (ou un gestionnaire de secrets plus avance, hors sujet ici).

## Ce que ce n'est pas

Les variables d'environnement, ce n'est pas "cacher le code". Ce n'est pas non plus une raison de mettre toute la config dans `.env` sans reflechir. Ce n'est pas magique : si la variable n'est pas definie dans la session qui lance le script, Python ne la invente pas. Et ce n'est surtout pas une excuse pour logger la valeur "juste pour verifier".

:::astuce
Meme si ton API demo n'a pas de cle, prends le reflexe `.env.example` maintenant. Le muscle se construit avant l'urgence.
:::

## Petite histoire

Lea a pousse un script sur GitHub avec `API_CLE = "sk-xxxxx"` en haut du fichier. Quelqu'un a scanne le depot en dix minutes. La cle etait brulee. Revocation, nouvelle cle, `.env.example`, `.gitignore` mis a jour. Depuis, c'est un reflexe chez DanielCraft : jamais de secret dans le code, jamais dans un screenshot, jamais dans un log.

Max a failli logger sa cle "pour debug". Sam l'a arrete. Une ligne de log, une cle exposee. Pas ce soir.

## Erreur classique

Ecrire `API_CLE = "sk-xxxxx"` en haut du fichier et pousser sur GitHub. Une fois public, considere la cle brulee : revoque-la. Autre classique : logger la cle "pour debug". Ne jamais imprimer un secret. Autre piege : committer le fichier `.env` par erreur parce qu'il n'est pas dans `.gitignore`.

## En vrai

Cree une variable `MON_NOM` dans ton terminal. Lis-la dans un script et affiche "Bonjour, ...". Puis simule l'absence de variable et affiche une erreur claire.

## A toi

Prepare un `.env.example` pour un futur script meteo ou API (noms de variables seulement). Ajoute `.env` a ton `.gitignore` mental (et reel si tu utilises Git). Le muscle "pas de secret dans le code" se construit maintenant.

:::retenir
Le code connait le nom de la variable. La valeur secrete reste dehors : environnement, `.env` ignore, `.env.example` partageable.
:::
