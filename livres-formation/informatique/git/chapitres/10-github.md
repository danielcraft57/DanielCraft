# Chapitre 10 - GitHub, c'est quoi ?

GitHub heberge tes depots Git sur internet.
Sauvegarde distante + collaboration + issues + pull requests.

## Compte

1. Cree un compte sur github.com
2. Confirme l'email
3. Optionnel mais recommande : active la double authentification

## Nouveau depot en ligne

Sur GitHub : **New repository**
- Nom : `mon-carnet`
- Public ou prive
- Tu peux ne **pas** cocher "Add a README" si tu as deja un depot local

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

- HTTPS : simple au debut (parfois un token)
- SSH : cles, tres confortable au quotidien

Les deux marchent. Choisis-en un et avance.

## README.md

Sur GitHub, `README.md` s'affiche en vitrine.
Ecris 5 lignes : but du projet + comment lancer.

## A toi

1. Cree un depot GitHub de test (prive OK)
2. Branche `origin`
3. `push` ta branche `main`

## En vrai, sur le terrain

Apres le push, rafraichis la page GitHub.
Tu dois voir tes fichiers. Soulagement.

## Mini defi

Ajoute un vrai `README.md` clair. Commit. Push. Verifie le rendu.
