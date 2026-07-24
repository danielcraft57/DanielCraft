# Chapitre 10 - GitHub, c'est quoi ?

GitHub heberge tes depots Git sur internet.
Sauvegarde distante + collaboration + issues + pull requests.

## Compte

Cree un compte sur github.com. Confirme l'email. Optionnel mais recommande : active la double authentification.

## Nouveau depot en ligne

Sur GitHub : **New repository**. Choisis un nom, par exemple `mon-carnet`. Public ou prive. Tu peux ne **pas** cocher "Add a README" si tu as deja un depot local.

## Lier ton depot local

Sur la page du depot vide, GitHub montre des commandes.
En general :

```bash
git remote add origin https://github.com/TON_COMPTE/mon-carnet.git
git branch -M main
git push -u origin main
```

`origin` = surnom classique de ton remote principal.

## Voir les remotes

```bash
git remote -v
```

## SSH ou HTTPS ?

HTTPS est simple au debut (parfois un token). SSH utilise des cles et devient tres confortable au quotidien. Les deux marchent. Choisis-en un et avance.

## README.md

Sur GitHub, `README.md` s'affiche en vitrine.
Ecris 5 lignes : but du projet + comment lancer.

## A toi

Cree un depot GitHub de test (prive OK). Branche `origin`. Fais `push` de ta branche `main`.

## En vrai, sur le terrain

Apres le push, rafraichis la page GitHub.
Tu dois voir tes fichiers. Soulagement.

## Mini defi

Ajoute un vrai `README.md` clair. Commit. Push. Verifie le rendu.
