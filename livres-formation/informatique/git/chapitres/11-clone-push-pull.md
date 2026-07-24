# Chapitre 11 - clone, push, pull

Le dialogue avec le serveur.

## clone

Recuperer un depot existant :

```bash
git clone https://github.com/TON_COMPTE/mon-carnet.git
cd mon-carnet
```

`clone` = copie + lien `origin` deja configure.

## push

Envoyer tes commits locaux vers le remote :

```bash
git push
```

La premiere fois (si pas de `-u`) :

```bash
git push -u origin main
```

## pull

Recuperer les commits distants et les fusionner chez toi :

```bash
git pull
```

Reflexe avant de recommencer a coder le matin : `git pull`.

## fetch (apercu)

```bash
git fetch
```

`fetch` telecharge les infos sans fusionner tout de suite.
`pull` ≈ `fetch` + merge (en simplifiant).

## Schema

```text
toi (local) --push--> GitHub
toi (local) <--pull-- GitHub
```

## Erreurs frequentes

- `rejected` : le remote a des commits que tu n'as pas -> `pull` d'abord
- auth ratee : mauvais token / session
- mauvaise branche : tu pushes `main` alors que tu es ailleurs

## A toi

1. Modifie un fichier
2. commit
3. push
4. Change quelque chose sur GitHub via l'interface (petit edit)
5. `git pull` en local

## En vrai, sur le terrain

Sur un projet a deux : toujours `pull` avant de pousser.
Ca diminue les conflits.

## Mini defi

Clone un petit depot public open source (lecture seule).
Explore `log --oneline`. Ne push rien.
