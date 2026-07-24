# Chapitre 11 - Lire et ecrire un fichier

Parfois tu veux garder des infos hors du programme.
Sinon tout disparait a la fermeture.

## Ecrire

```python
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Salut\n")
    f.write("Deuxieme ligne\n")
```

`with` ferme le fichier proprement. Prends le reflexe.

## Lire

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    contenu = f.read()
print(contenu)
```

## Lire ligne par ligne

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        print(">", ligne.strip())
```

## Modes utiles

Le mode `"w"` ecrit (et ecrase). `"a"` ajoute a la fin. `"r"` lit seulement.

## JSON (plus avance, tres utile)

```python
import json

data = {"prenom": "Sam", "score": 120}

with open("joueur.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("joueur.json", "r", encoding="utf-8") as f:
    charge = json.load(f)

print(charge["score"])
```

JSON = format texte standard pour echanger des donnees.
Parfait pour sauvegarder un score ou une config.

## pathlib (apercu)

```python
from pathlib import Path

p = Path("notes.txt")
print(p.exists())
print(p.read_text(encoding="utf-8"))
```

Plus moderne que `open` seul pour certains cas.
Les deux cohabitent.

## Erreurs classiques

Un mauvais dossier donne souvent "fichier introuvable". Oublier `encoding="utf-8"` foire les accents. Et le mode `"w"` ecrase sans prevenir.

## A toi

Ecris ton prenom dans `moi.txt`.
Relis le fichier et affiche-le.
Puis sauvegarde un petit dico dans `moi.json`.

## En vrai, sur le terrain

Ajoute 3 lignes dans un journal `journal.txt` en mode `"a"`.
Relance 2 fois. Verifie que ca s'allonge.

## Mini defi

Programme qui demande un score, le sauve en JSON, le recharge, l'affiche.
