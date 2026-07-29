# Lire et ecrire des fichiers

## Pourquoi manipuler des fichiers ?

Les programmes ont souvent besoin de sauvegarder des donnees ou d'en lire. Python rend la lecture et l'ecriture de fichiers texte tres simples.

## Ecrire dans un fichier

```python
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Maths : 15\n")
    f.write("Francais : 13\n")
```

`"w"` cree le fichier (ou l'ecrase). `with` ferme le fichier automatiquement.

## Lire un fichier

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    contenu = f.read()
print(contenu)
```

## Lire ligne par ligne

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        print(ligne.strip())
```

> **Astuce DanielCraft** - Precise toujours `encoding="utf-8"` pour eviter les problemes d'accents.

## Ajouter sans ecraser

```python
with open("notes.txt", "a", encoding="utf-8") as f:
    f.write("Histoire : 16\n")
```

`"a"` (append) ajoute a la fin sans supprimer le contenu existant.

## Petite histoire

Nora ecrit un programme qui sauvegarde ses depenses dans un fichier CSV. Chaque jour elle ajoute une ligne. A la fin du mois elle relit le fichier et calcule le total.

## Erreur classique

```python
f = open("data.txt")
contenu = f.read()
# Si une erreur survient ici, le fichier reste ouvert
```

Utilise toujours `with` pour garantir la fermeture.

## A retenir

- `with open(...) as f:` pour ouvrir proprement.
- `"r"` lire, `"w"` ecrire (ecrase), `"a"` ajouter.
- Toujours preciser `encoding="utf-8"`.
