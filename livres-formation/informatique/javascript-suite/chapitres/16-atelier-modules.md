# Chapitre 16 - Atelier : decouper en modules

Objectif : reprendre l'atelier fetch et le decouper en trois fichiers.

## Fichiers

- `api.js` : `export async function chargerCitations()`
- `afficher.js` : `export function afficherCitations(liste, data)`
- `main.js` : branche le bouton, appelle api + afficher, gere le message d'erreur

HTML :

```html
<script type="module" src="main.js"></script>
```

## Etapes

1. Deplace le `fetch` dans `api.js`.
2. Deplace la boucle DOM dans `afficher.js`.
3. Dans `main.js`, importe les deux fonctions.
4. Garde le `try/catch` dans `main.js` (orchestration).

## Criteres de reussite

- Ca marche comme avant.
- Aucun fichier ne depasse ~40 lignes (ordre de grandeur).
- Tu peux expliquer a voix haute le role de chaque fichier en une phrase.

## Bonus

Ajoute `export function afficherErreur(zone, texte)` dans `afficher.js`. `main.js` ne touche plus au DOM des messages directement.
