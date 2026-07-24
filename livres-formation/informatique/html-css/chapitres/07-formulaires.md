# Chapitre 7 - Les formulaires

Un formulaire, c'est quand tu demandes des infos a quelqu'un.
Nom, email, message... Tu vois le genre.

## La base

```html
<form action="#" method="post">
  <label for="prenom">Prenom</label>
  <input id="prenom" name="prenom" type="text">

  <button type="submit">Envoyer</button>
</form>
```

`form` enveloppe tout.
`label` = le texte a cote du champ (important pour la clarte).
`input` = le champ.
`button` = le bouton.

`for` du label doit matcher `id` de l'input. Comme ca, cliquer sur le texte focus le champ. Pratique.

## Types d'input utiles

```html
<input type="text" placeholder="Ton prenom">
<input type="email" placeholder="toi@exemple.com">
<input type="password">
<input type="number" min="1" max="120">
<input type="checkbox"> J'accepte
<input type="radio" name="choix" value="a"> Option A
<input type="radio" name="choix" value="b"> Option B
```

`placeholder` = texte fantome dans le champ. Disparait quand tu ecris.

## Zone de texte longue

```html
<label for="msg">Message</label>
<textarea id="msg" name="msg" rows="5"></textarea>
```

## Liste deroulante

```html
<label for="ville">Ville</label>
<select id="ville" name="ville">
  <option value="paris">Paris</option>
  <option value="lyon">Lyon</option>
  <option value="marseille">Marseille</option>
</select>
```

## Requis

```html
<input type="email" required>
```

Le navigateur refuse d'envoyer si c'est vide. Utile, mais ce n'est pas une vraie securite cote serveur. Pour plus tard.

## Petit rappel

Pour l'instant, `action="#"` veut dire "on n'envoie nulle part de special".
Plus tard tu brancheras ca a un vrai traitement (PHP, API...).
La on apprend juste a construire le formulaire.

## A toi

Fais un formulaire "Contact" avec :
- nom
- email
- message
- bouton Envoyer


## En vrai, sur le terrain

Prends 10 minutes. Refais l'exemple du chapitre sans regarder.
Si tu bloques, relis juste la partie qui coinçe. Puis repars.

Le but c'est pas de memoriser. C'est de reconnaitre le motif la prochaine fois.

## Mini defi

Ecris 3 lignes de notes a toi-meme :
1. ce que tu as compris
2. ce qui reste flou
3. un truc a retester demain

Garde ces notes. Elles valent plus qu'un long cours jamais relu.
