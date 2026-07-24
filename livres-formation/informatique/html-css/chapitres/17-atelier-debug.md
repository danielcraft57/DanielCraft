# Chapitre 17 - Atelier debug : la page est cassee

Ca arrive. Souvent. Et c'est normal.
La, on apprend a chercher sans paniquer.

## Methode en 5 etapes

1. Relis la derniere chose que tu as changee
2. Regarde la console (F12) s'il y a du JS plus tard ; pour HTML/CSS, regarde surtout le resultat
3. Verifie les balises ouvertes / fermees
4. Verifie les chemins (`href`, `src`, `link`)
5. Simplifie : commente un gros bloc, reteste

## Checklist HTML

Verifie que `<!DOCTYPE html>` est present, que tu as bien `lang="fr"`, et que `charset` + `viewport` sont la. Chaque balise ouverte doit etre fermee. Et garde un seul `h1` principal.

## Checklist CSS

Le `<link rel="stylesheet" href="style.css">` doit etre bien la, avec le nom de fichier exact (casse comprise). La classe HTML doit matcher la classe CSS (`.carte` vs `carte`). Et sois propre sur les `;` a la fin des proprietes : CSS tolere parfois, mais autant rester propre.

## Exemple de piege classique

```html
<link rel="stylesheet" href="Style.css">
```

Alors que le fichier s'appelle `style.css`.
Sur certains systemes, ca casse. Garde les noms simples, en minuscules.

## Exercice

Casse volontairement ta page (enlève une balise fermante).
Puis repare-la.
Tu apprendras plus en 10 minutes comme ca qu'en regardant 1h de video.

## Ce qu'il faut retenir

Le debug, c'est pas "etre nul".
C'est le vrai boulot. Les gens qui avancent, c'est ceux qui supportent de chercher.
