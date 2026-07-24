# Chapitre 2 - Ton premier fichier HTML

On va creer un fichier. Rien de complique.

## De quoi tu as besoin

1. Un editeur de texte. Bloc-notes marche. VS Code c'est mieux (gratuit).
2. Un navigateur (celui que tu utilises deja).

C'est tout. Pas de compte. Pas de carte bleue.

## Cree le fichier

1. Ouvre ton editeur.
2. Copie le code ci-dessous.
3. Enregistre le fichier en `index.html` (attention a l'extension `.html`).
4. Double-clique dessus. Ca s'ouvre dans le navigateur.

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Ma premiere page</title>
</head>
<body>
  <h1>Salut !</h1>
  <p>Ca y est. J'ai fait une page web.</p>
</body>
</html>
```

Si tu vois "Salut !" en gros, bravo. C'est bon.

## On explique ligne par ligne (sans stress)

`<!DOCTYPE html>`
Ca dit au navigateur : "hey, c'est du HTML moderne". Toujours en haut.

`<html lang="fr">`
La page commence. `lang="fr"` = contenu en francais.

`<head> ... </head>`
La tete de la page. Infos pour le navigateur, pas vraiment ce que tu vois au milieu de l'ecran.
Exemple : le titre de l'onglet (`<title>`).

`<meta charset="UTF-8">`
Pour que les accents marchent. Crucial en francais. Sans ca, tu peux avoir des caracteres bizarres.

`<body> ... </body>`
Le corps. Tout ce que tu vois sur la page va ici.

`<h1>` = un gros titre.
`<p>` = un paragraphe.

## Les balises ouvrantes et fermantes

Regarde : `<p>` ouvre. `</p>` ferme.
Le slash `/` veut dire "c'est fini pour ce truc".

Comme des parentheses. Tu ouvres, tu fermes.

## A toi

Change le texte. Mets ton prenom dans le titre.
Rafraichis la page (F5).
Tu viens de modifier un site. Serieux.
