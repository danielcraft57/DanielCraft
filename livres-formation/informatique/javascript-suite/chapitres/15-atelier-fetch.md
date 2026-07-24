# Chapitre 15 - Atelier : fetch et afficher

Objectif : charger un JSON et remplir une liste HTML.

## Preparation

Cree un fichier `citations.json` a cote de ta page :

```json
[
  { "texte": "Petit a petit, l'oiseau fait son nid.", "auteur": "Proverbe" },
  { "texte": "On apprend en faisant.", "auteur": "DanielCraft" },
  { "texte": "Le code clair se lit comme une histoire.", "auteur": "Atelier" }
]
```

Sers le dossier avec un petit serveur local.

## Etapes

1. Bouton "Charger les citations".
2. `fetch("./citations.json")`.
3. Verifie `ok`, puis `json()`.
4. Pour chaque item, cree un `<li>` avec le texte et l'auteur.
5. Affiche "Chargement..." pendant l'attente.
6. En cas d'erreur, message humain + `console.error`.

## Criteres de reussite

- Trois citations visibles.
- URL cassee volontairement -> message d'erreur.
- Pas d'exception non geree dans la console (sauf ton log volontaire).

## Bonus

Ajoute un champ recherche qui filtre la liste deja chargee (sans refaire fetch a chaque lettre pour l'instant). Le debounce viendra plus tard.
