# Chapitre 3 - Ton premier programme

Ouvre `salut.py` et ecris :

```python
print("Salut Python")
```

Lance :

```bash
python salut.py
```

Si tu vois `Salut Python`, bravo. C'est parti.

## print, c'est quoi ?

`print(...)` affiche quelque chose a l'ecran.
Le texte va entre guillemets.

```python
print("Coucou")
print(2 + 2)
print("2 + 2 =", 2 + 2)
```

Tu peux afficher plusieurs choses separees par des virgules.
Python ajoute un espace entre.

## f-strings (pratique)

```python
prenom = "Leo"
age = 12
print(f"Je m'appelle {prenom} et j'ai {age} ans")
```

Le `f` devant la chaine laisse coller des variables avec `{...}`.
Plus lisible que coller avec `+` partout.

## Commentaires

```python
# Ceci est une note pour toi. Python l'ignore.
print("Je compte")  # commentaire en fin de ligne
```

Ecris des commentaires utiles, pas "ici j'affiche".
Plutot : pourquoi tu fais un truc pas evident.

## input : demander quelque chose

```python
prenom = input("Ton prenom ? ")
print("Salut", prenom)
print(f"Enchante, {prenom} !")
```

`input` attend que tu ecrives puis Entree.
Attention : `input` renvoie toujours du **texte** (str).

## Nettoyer une reponse

```python
reponse = input("Ville ? ").strip()
```

`strip()` enleve les espaces avant/apres.
Utile. Les gens tapent souvent un espace sans le voir.

## Erreur classique

Oublier les guillemets :

```python
print(Salut)  # erreur : Salut n'existe pas comme variable
```

Le message d'erreur pointe souvent la ligne. Lis-la.

## Exemple complet

```python
# mini presentation
prenom = input("Prenom ? ").strip()
hobby = input("Hobby ? ").strip()
print(f"Salut {prenom}. Cool pour {hobby}.")
print("Fin du programme.")
```

## A toi

Demande le prenom et l'age (age en texte pour l'instant).
Affiche : `Bonjour, <prenom> ! Tu as <age> ans.`
Avec une f-string.

## En vrai, sur le terrain

Retape l'exemple sans copier-coller.
Change les phrases. Relance. Regarde.

## Mini defi

Ajoute une 3e question (ville ou animal prefere).
Affiche une mini bio en 2 lignes.
