# Chapitre 11 - Lire et ecrire un fichier

Parfois tu veux garder des infos hors du programme. Sinon tout disparait a la fermeture. Un score, un journal, une config, une liste de taches : le fichier est la memoire durable du debutant. Sans fichiers, tu rejoues tout a chaque lancement. Avec fichiers, ton script commence a ressembler a un petit outil. En 2026, meme un outil perso "pour moi seul" gagne a laisser une trace claire sur le disque.

Chez DanielCraft, on insiste sur `with open(...)` des le premier exemple. `with` ferme le fichier proprement, meme si une erreur survient au milieu. Lea a deja laisse des fichiers verrouilles en oubliant de fermer. Max a ecrase un journal avec le mode `"w"` par accident. Sam fait ecrire puis relire systematiquement : la boucle "ecris / lis / verifie" forme mieux qu'un discours. Tu n'as pas besoin d'une base de donnees pour commencer. Tu as besoin d'un fichier que tu comprends.

## Ce que ce n'est pas

Ecrire un fichier, ce n'est pas "hacker le systeme". Ce n'est pas non plus une base de donnees complete. Ce n'est pas automatique : tu choisis le nom, le mode, l'encodage. Et ce n'est surtout pas anodin d'ouvrir en `"w"` : ce mode ecrase sans ceremonie. Si tu voulais ajouter, c'est `"a"`. Si tu voulais lire, c'est `"r"`. Trois lettres, trois intentions. Melange-les, et tu pleures.

Ce n'est pas non plus "seulement du texte brut". JSON te permettra de sauver des structures (dicos, listes) de facon standard. Le texte brut reste parfait pour un journal ou un export simple.

Tu ouvres un carnet (`open`). Tu ecris des lignes (`write`). Tu refermes (`with` s'en charge). Plus tard, tu rouvres et tu lis (`read` ou ligne par ligne). JSON, c'est le meme carnet, mais structure comme un dictionnaire : pratique pour un score ou une config. `pathlib` est une facon plus moderne de parler des chemins. Les deux styles cohabitent. Ici, tu apprends d'abord `open` + `json`. Chez DanielCraft, on pose le geste simple avant l'outil elegant.

Lea voit un journal client. Max voit un score de jeu. Sam voit une liste de notes. Trois carnets, meme geste : ouvrir, ecrire, relire, verifier.

## Ecrire, lire, modes

```python
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Salut\n")
    f.write("Deuxieme ligne\n")
```

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    contenu = f.read()
print(contenu)
```

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        print(">", ligne.strip())
```

Modes utiles : `"w"` ecrit (et ecrase). `"a"` ajoute a la fin. `"r"` lit seulement. Toujours `encoding="utf-8"` si tu touches aux accents. Lea l'ecrit par reflexe. Max l'a appris apres un "Leo" transforme en bizarre. Sam le met dans la checklist du tableau.

## JSON (tres utile)

```python
import json

data = {"prenom": "Sam", "score": 120}

with open("joueur.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("joueur.json", "r", encoding="utf-8") as f:
    charge = json.load(f)

print(charge["score"])
```

JSON = format texte standard pour echanger des donnees. Parfait pour sauvegarder un score ou une config. `ensure_ascii=False` garde les accents lisibles. `indent=2` rend le fichier humainement relisible. Chez DanielCraft, on aime les fichiers que tu peux ouvrir et comprendre sans outil special. Si tu ne peux pas lire ton JSON a l'oeil, tu auras du mal a deboguer.

## pathlib (apercu)

```python
from pathlib import Path

p = Path("notes.txt")
print(p.exists())
print(p.read_text(encoding="utf-8"))
```

Plus moderne que `open` seul pour certains cas. Les deux cohabitent. Tu n'as pas a tout migrer aujourd'hui. Tu dois reconnaitre le mot. Le livre Python pratique approfondira `pathlib`. Ici, l'apercu suffit pour ne pas etre surpris.

## Petite histoire

Lea a cree `journal.txt` en mode `"a"`. Chaque lancement ajoute une ligne datee (plus tard avec `datetime`). Elle relance deux fois, ouvre le fichier, voit s'allonger. Sensation concrete : le programme laisse une trace. Max a sauve son score en JSON, ferme le terminal, relance, recharge, sourit. Sam demande ce mini defi a toute la classe avant le chapitre modules. Ceux qui ecrasent avec `"w"` apprennent vite la difference. Une erreur, une histoire, une habitude.

## Erreur classique

Mauvais dossier : "fichier introuvable". Oublier `encoding="utf-8"` et foire les accents. Mode `"w"` qui ecrase sans prevenir. Chemin absolu casse quand tu changes de machine. Autre piege : croire que `json.dump` "ecrit tout seul" sans `open` - non, tu fournis le fichier ouvert. Lis l'exemple encore une fois si besoin. Lea a aussi confondu `json.dump` (vers un fichier) et `json.dumps` (vers une chaine). Une lettre de difference, deux usages.

## En vrai

Ajoute 3 lignes dans un journal `journal.txt` en mode `"a"`. Relance 2 fois. Verifie que ca s'allonge. Puis programme qui demande un score, le sauve en JSON, le recharge, l'affiche. Fais les deux dans le meme dossier. Note le chemin exact du terminal. Le "fichier introuvable" est souvent un probleme de dossier courant, pas de Python.

## A toi

Ecris ton prenom dans `moi.txt`. Relis le fichier et affiche-le. Puis sauvegarde un petit dico dans `moi.json` et recharge-le. Bonus : si le JSON existe deja, affiche l'ancien score avant d'en ecrire un nouveau. Garde ces fichiers. Ils serviront d'exemples dans les ateliers.

## Zoom : w, a, r en une phrase

`"r"` lit sans toucher. `"a"` ajoute a la fin. `"w"` ecrase et recommence. Si tu hesites, demande-toi : "est-ce que je peux me permettre de perdre le contenu actuel ?" Si non, ce n'est probablement pas `"w"`. Chez DanielCraft, cette question avant chaque `open` evite des drames du dimanche soir.
