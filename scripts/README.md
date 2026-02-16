# Scripts V6

## clone-loupix57-repos.ps1

Telecharge (clone) tous les depots GitHub du compte **loupix57** dans le dossier `repos-loupix57` a la racine du projet (DanielCraft).

**Prerequis :** Git installe et accessible en ligne de commande.

**Execution :**

```powershell
cd c:\Users\loicDaniel\Documents\DanielCraft\V6
.\scripts\clone-loupix57-repos.ps1
```

Ou depuis la racine DanielCraft :

```powershell
.\V6\scripts\clone-loupix57-repos.ps1
```

Les depots sont clones en `DanielCraft/repos-loupix57/` (un sous-dossier par repo). Les depots deja presents sont ignores (SKIP). Pour tout recloner, supprime le dossier `repos-loupix57` puis relance le script.

**But :** etudier le code source de chaque projet loupix57 et les integrer au site V6 (donnees deja integrees dans `assets/js/github-projects.js` et une selection dans `assets/js/portfolio.js`).
