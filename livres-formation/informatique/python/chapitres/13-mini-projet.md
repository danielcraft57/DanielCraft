# Mini-projet : gestionnaire de contacts

## L'objectif

On cree un petit programme en ligne de commande qui permet d'ajouter, lister et chercher des contacts. Ce projet combine variables, listes, dictionnaires, fonctions, boucles, conditions et fichiers.

## Structure du programme

```python
import json
from pathlib import Path

FICHIER = Path("contacts.json")

def charger():
    if FICHIER.exists():
        return json.loads(FICHIER.read_text(encoding="utf-8"))
    return []

def sauvegarder(contacts):
    FICHIER.write_text(
        json.dumps(contacts, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

def ajouter(contacts):
    nom = input("Nom : ")
    tel = input("Telephone : ")
    contacts.append({"nom": nom, "tel": tel})
    sauvegarder(contacts)
    print(f"{nom} ajoute.")

def lister(contacts):
    if not contacts:
        print("Aucun contact.")
        return
    for i, c in enumerate(contacts, 1):
        print(f"  {i}. {c['nom']} - {c['tel']}")

def chercher(contacts):
    terme = input("Recherche : ").lower()
    resultats = [c for c in contacts if terme in c["nom"].lower()]
    if resultats:
        for c in resultats:
            print(f"  {c['nom']} - {c['tel']}")
    else:
        print("Aucun resultat.")

def main():
    contacts = charger()
    while True:
        print("\n1. Ajouter  2. Lister  3. Chercher  4. Quitter")
        choix = input("> ")
        if choix == "1":
            ajouter(contacts)
        elif choix == "2":
            lister(contacts)
        elif choix == "3":
            chercher(contacts)
        elif choix == "4":
            print("A bientot !")
            break

if __name__ == "__main__":
    main()
```

## Ce que tu apprends

- Decouverte de `json` pour sauvegarder des donnees structurees.
- Utilisation de `Path` pour verifier l'existence d'un fichier.
- Boucle principale avec menu textuel.
- Fonctions bien decoupees (une par action).

> **Astuce DanielCraft** - Commence par le squelette (menu + fonctions vides), puis remplis une fonction a la fois.

## Pour aller plus loin

- Ajouter un champ email.
- Permettre la suppression d'un contact.
- Trier les contacts par nom.

## A retenir

- Un projet = assemblage de notions deja vues.
- Decouper en fonctions rend le code lisible.
- `json` permet de sauvegarder des donnees facilement.
