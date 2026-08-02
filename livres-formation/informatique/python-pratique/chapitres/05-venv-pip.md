# Chapitre 5 - venv et pip : isoler les paquets

Python de base sait beaucoup de choses. Mais pour parler HTTP facilement, on utilisera `requests` (chapitre suivant). `requests` n'est pas dans la bibliotheque standard : tu l'installes avec **pip**.

Si tu installes tout "dans le Python global" de ta machine, les projets se marchent dessus. Une version de bibliotheque pour le projet A casse le projet B. La solution : un environnement virtuel (**venv**) par projet. Un venv, c'est une boite a outils privee pour un projet. Dedans : un Python isole et un pip isole. Quand tu actives la boite, tes commandes `python` et `pip` pointent vers elle. Quand tu desactives, tu reviens au Python systeme. Rien ne se melange. Tu changes de dossier, tu changes de boite.

Chez DanielCraft, regle simple : un projet, un venv. Lea a deux clients avec deux versions de `requests` differentes. Max a un script meteo isole de son outil CSV. Sam recree son venv proprement chaque annee scolaire.

:::retenir
Un projet, un venv. On partage `requirements.txt`, pas le dossier `.venv`.
:::

## Creer un venv

Dans le dossier de ton projet :

```text
python -m venv .venv
```

Ca cree un dossier `.venv` (le nom est une convention courante). Dedans : un Python isole et un `pip` isole.

## L'activer

Sous Windows (PowerShell) :

```text
.\.venv\Scripts\Activate.ps1
```

Sous Windows (cmd) :

```text
.\.venv\Scripts\activate.bat
```

Sous macOS / Linux :

```text
source .venv/bin/activate
```

Quand c'est actif, ton invite de commande montre souvent `(.venv)`. Les commandes `python` et `pip` pointent alors vers le venv. Pour desactiver : `deactivate`.

Si PowerShell refuse l'execution de scripts, c'est une politique Windows. Tu peux chercher la doc officielle sur l'execution de scripts, ou utiliser `cmd` pour activer. L'idee reste la meme.

## Installer un paquet

Avec le venv actif :

```text
pip install requests
```

Tu peux figer les versions dans un fichier **requirements.txt** :

```text
requests==2.32.3
```

Puis installer d'un coup :

```text
pip install -r requirements.txt
```

On approfondira l'organisation du projet plus loin. Pour l'instant, retiens : `pip install` dans le venv, pas "au feeling" dans le Python systeme.

## Verifier

```text
python -c "import requests; print(requests.__version__)"
```

Si ca affiche une version, `requests` est bien la. Si tu desactives le venv et que tu relances sans le paquet global, ca peut echouer - et c'est normal.

## .gitignore

Le dossier `.venv` ne se partage pas sur Git. Il est lourd et propre a chaque machine. On partage `requirements.txt`, et chacun recree son venv. Si tu utilises Git, ajoute `.venv/` au `.gitignore`.

## Mettre a jour pip (souvent utile)

Dans le venv fraichement cree, pip peut etre vieux. Un classique :

```text
python -m pip install --upgrade pip
```

Puis installe tes paquets. Moins de messages bizarres, moins de surprises.

## Plusieurs projets, plusieurs venv

Projet notes d'un cote, projet meteo de l'autre : deux dossiers, deux `.venv`. Tu actives celui du projet sur lequel tu travailles. Si tu changes de dossier dans le terminal, pense a reactiver (ou a ouvrir un terminal "dans" le bon projet via ton editeur).

:::astuce
Toujours `python -m pip install ...` avec le meme interpreteur. Comme ca, pip et python sont maries. Fini le "j'ai installe mais ModuleNotFoundError".
:::

## Petite histoire

Lea avait installe `requests` "quelque part" sur sa machine. Son script marchait chez elle, pas chez le client. Le diagnostic : elle avait un `pip` et un `python` qui ne parlaient pas au meme endroit. La regle `python -m pip install requests` a tout regle en une commande. Depuis, chaque projet a son venv et son `requirements.txt`. Zero surprise entre machines.

Max a perdu une soiree a chercher pourquoi "ca marchait hier". Sam lui a demande : "venv active ?" Non. Relance, ca marche. Le rituel compte autant que la commande.

## Erreur classique

Installer avec un `pip` et lancer avec un autre `python`. Symptome : "j'ai installe requests mais Python dit ModuleNotFoundError". Contre-mesure : toujours `python -m pip install ...` avec le meme interpreteur.

```text
python -m pip install requests
```

Comme ca, pip et python sont maries. Autre classique : oublier d'activer le venv et croire que "pip est casse". Ou supprimer le dossier `.venv` a la main puis s'etonner que plus rien ne s'importe : il suffit de recreer le venv et de reinstaller depuis `requirements.txt`.

:::attention
Ne committe jamais `.venv`. Il est lourd, propre a chaque machine, et inutile sur Git. Committe `requirements.txt`.
:::

## En vrai

Cree un dossier `demo-venv`. Fais `python -m venv .venv`. Active. Installe `requests`. Verifie l'import. Desactive. C'est un rituel a connaitre par coeur.

## A toi

Ecris un `requirements.txt` minimal avec `requests`. Documente en trois lignes (dans un `README` perso ou un commentaire) : creer le venv, activer, installer. Ton futur toi aime les rituels ecrits. Bonus : recree le venv depuis zero sur une machine (ou un dossier) propre en suivant uniquement ton README. Si tu bloques, le rituel est trop flou : corrige-le avant d'ajouter un paquet.
