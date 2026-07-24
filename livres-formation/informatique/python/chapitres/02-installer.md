# Chapitre 2 - Installer et ecrire Python

Avant de coder, il faut un Python qui marche.
Sur Windows, le plus simple :

1. Va sur le site officiel python.org
2. Telecharge la version recente
3. Installe (coche "Add Python to PATH" si tu vois l'option)
4. Ouvre un terminal et tape : `python --version`

Si tu vois un numero de version, c'est bon.

Parfois c'est `py --version` qui marche mieux sur Windows.
Les deux existent. Garde celui qui repond.

## Ou ecrire le code ?

Deux options debutant :

1. **VS Code** (gratuit) + extension Python
2. **IDLE** (fourni avec Python) - plus basique, mais ok

Plus tard tu peux aimer PyCharm ou autre.
Pour ce livre, VS Code ou IDLE suffisent largement.

## Fichier `.py`

Cree un dossier `mes-tests-python`.
Dedans, cree un fichier `salut.py`.
C'est ton programme.

Astuce : un dossier par projet.
Evite de tout mettre sur le Bureau en vrac.

## Lancer

Dans le dossier du fichier :

```bash
python salut.py
```

Ou :

```bash
py salut.py
```

Si le terminal dit "introuvable", c'est souvent :
- mauvais dossier (tu n'es pas au bon endroit)
- PATH pas coche a l'install

## La console interactive

```bash
python
```

Tu peux tester des lignes une par une.
Utile pour un calcul vite fait.

```python
>>> 2 + 2
4
>>> exit()
```

`exit()` pour quitter.
Ou Ctrl+Z puis Entree sur Windows.

## Virtualenv ? (apercu)

Plus tard, les projets serieux utilisent un "environnement virtuel".
Idee : isoler les bibliotheques d'un projet.

```bash
python -m venv .venv
```

Puis on active, puis `pip install ...`.
Pour l'instant, tu n'en as pas besoin.
Mais le mot existe. Tu le reverras.

## A toi

1. Verifie `python --version` (ou `py --version`)
2. Cree le dossier + `salut.py`
3. On ecrira dedans au chapitre suivant

## Erreur classique

Tu lances `python salut.py` depuis le mauvais dossier.
Le terminal dit qu'il ne trouve pas le fichier.
Solution : `cd` vers le bon dossier, puis relance.

## En vrai, sur le terrain

Ouvre le terminal. Tape la commande de version.
Note le resultat. Si ca marche, tu es pret.

## Mini defi

Cree aussi `notes.md` dans ton dossier.
Ecris-y : version Python + outil choisi (VS Code / IDLE).
