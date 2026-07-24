# Chapitre 10 - Organiser un petit projet

Un projet web, ce n'est pas seulement "du code qui marche". C'est aussi un rangement que tu comprends dans une semaine, quand tu auras oublie les details.

Voici une structure simple qui marche pour beaucoup de mini-apps :

```
mon-projet/
  index.html
  styles.css
  main.js
  api.js
  afficher.js
  data/   (optionnel)
```

`index.html` : la page. Peu de logique. `styles.css` : l'habillage. `main.js` : le chef d'orchestre (ecoute les clics, lance les chargements). `api.js` : fetch et parsing. `afficher.js` : creer des elements DOM a partir des donnees.

## Responsabilites

Si `api.js` commence a manipuler le DOM, tu melanges les roles. Si `afficher.js` appelle `fetch`, pareil. Garde une regle : chaque fichier a une phrase pour se presenter. "Moi, je charge les donnees." "Moi, je dessine la liste." "Moi, je branche les boutons."

## Noms clairs

`faireTruc.js` n'aide personne. `chargerProduits`, `afficherErreur`, `viderListe` : on comprend. Les noms longs et clairs battent les noms courts et mysterieux.

## Une seule source de verite

Evite d'avoir le meme tableau de produits copie dans trois endroits. Charge une fois, stocke dans une variable (ou un petit etat), puis affiche. Si tu modifies, tu modifies a un seul endroit.

## En vrai

Beaucoup de debutants collent tout dans `index.html` entre deux balises script. Ca marche pour dix lignes. Au-dela, c'est une nasse. Passe tot aux fichiers separes, meme pour un exercice.

## A toi

Dessine sur papier (ou dans un commentaire) les 4 fichiers de ton prochain mini-projet et une phrase de role pour chacun. Si tu ne trouves pas la phrase, le fichier n'est peut-etre pas necessaire.
