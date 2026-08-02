# Chapitre 7 - Les formulaires

Un **formulaire**, c'est quand tu demandes des infos a quelqu'un : nom, email, message, choix. Tu vois le genre partout - contact, inscription, devis, quiz. En HTML, tu construis les champs. Tu n'as pas encore le serveur qui recoit. Et c'est ok. Chez DanielCraft, on separe : d'abord une forme claire et etiquetee, ensuite le branchement technique. Lea refuse de livrer un contact sans labels. Max a ajoute les siens apres qu'un client age ait bloque. Sam note "placeholder seul" comme erreur grave.

La base enveloppe tout dans `<form>`. Chaque champ a un **`<label>`** clair. Un `<input>` ou un `<textarea>` recoit la saisie. Un `<button type="submit">` envoie. Le `for` du label doit matcher l'`id` de l'input : cliquer le texte focus le champ. Pratique. Accessible. Professionnel. En 2026, quand quelqu'un dit "j'ai un formulaire contact", il parle souvent de ca. Derriere, il y a des backends et des validations avancees. Pour toi, le geste reste : labels, types, clarte. Tu restes le pilote. Le visiteur comprend.

:::retenir
Label + id/for + type correct. Structure claire d'abord ; envoi reel, plus tard.
:::

## Ce que ce n'est pas

Ce n'est pas encore une vraie collecte securisee. `action="#"` veut dire "on n'envoie nulle part de special" pour l'apprentissage. Ce n'est pas non plus `required` = securite totale : le navigateur aide, un serveur devra verifier plus tard. Ce n'est pas un formulaire sans labels "parce que le placeholder suffit" : le placeholder disparait, le label reste.

Ce n'est pas non plus "joli = utilisable". Un formulaire peut etre esthetique et illisible. Les pros commencent par la clarte. Le CSS viendra habiller des champs deja comprehensibles. Lea dit : "d'abord on comprend, ensuite on habille".

Pense a un guichet. Le label est la pancarte au-dessus du guichet. Le champ est la fenetre ou tu glisses le papier. Le bouton est "valider". Si la pancarte manque, les gens (et les lecteurs d'ecran) devinent. Max compare souvent : "sans label, c'est comme un guichet sans numero - tu fais la queue au hasard". Sam fait remplir un mauvais formulaire en classe pour sentir la douleur, puis le corriger. Lea projette les deux versions cote a cote chez le client. Le vote est unanime.

```html
<form action="#" method="post">
  <label for="prenom">Prenom</label>
  <input id="prenom" name="prenom" type="text">
  <button type="submit">Envoyer</button>
</form>
```

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

`placeholder` = texte fantome. Utile en complement, pas en remplacement du label. Les radios partagent le meme `name` pour ne choisir qu'une option. Deux radios avec des `name` differents, et tu peux tout cocher : piege classique. Sam le piege volontairement. Max est tombe une fois. Lea le verifie sur chaque livraison.

:::astuce
Le `for` du label = l'`id` du champ. Clique le texte : le champ se focus. Teste toujours ce geste.
:::

## Zone de texte et liste deroulante

```html
<label for="msg">Message</label>
<textarea id="msg" name="msg" rows="5"></textarea>

<label for="ville">Ville</label>
<select id="ville" name="ville">
  <option value="paris">Paris</option>
  <option value="lyon">Lyon</option>
</select>
```

`textarea` pour les longs messages. `select` + `option` pour une liste fermee. Choisis selon la liberte que tu veux laisser. Lea met un `select` pour le sujet (Devis, Support, Autre) : moins de messages hors sujet. Max ajoute une checkbox "rappel le matin" : simple, humain. Chez DanielCraft, un champ de moins bien place bat trois champs flous.

## Requis

```html
<input type="email" required>
```

Le navigateur refuse d'envoyer si c'est vide. Utile pour debuter. Rappel : ce n'est pas une vraie securite cote serveur. Pour plus tard. Mais ca t'entraine a penser "quels champs sont obligatoires ?" avant de styler. Lea coche `required` sur email et message. Max sur telephone. Sam exige au moins un champ requis par formulaire d'exercice.

## Petite histoire

Lea a herite d'un formulaire "joli" sans labels, avec des placeholders gris. Sur telephone, un client a tape, a perdu le contexte, a envoye n'importe quoi. Elle a remis labels + `required` + types corrects (`email`). Les messages sont devenus lisibles. Max a fait un devis contact avec checkbox "j'accepte d'etre rappele" : simple, clair, humain. Sam fait comparer deux versions : placeholder seul vs labels visibles. Vote unanime pour les labels. Trois scenes, une hygiene.

:::attention
Le placeholder ne remplace pas le label. Quand on tape, le placeholder disparait. Le label reste.
:::

## Erreur classique

Oublier le lien `for` / `id`. Mettre deux radios avec des `name` differents (du coup on peut tout cocher). Croire que le formulaire "envoie un mail tout seul" sans backend. Styler avant d'avoir des labels. Structure d'abord. Autre piege : oublier `name` sur les champs - sans `name`, rien n'est identifie cote serveur plus tard. Lea le rappelle aux stagiaires avant chaque livraison.

## En vrai

Fais un formulaire Contact : nom, email, message, bouton Envoyer. Clique le label : le champ doit se focus. Laisse l'email vide avec `required` et tente d'envoyer : le navigateur doit raler. Puis remplis avec un faux email : le type `email` doit aussi raler. Tu vois que le HTML aide deja un peu. Note ce qui manque encore (le serveur). Tu restes lucide.

## A toi

Ajoute une case a cocher "Je prefere etre contacte le matin" et une liste deroulante de sujet (Devis, Question, Autre). Ecris en deux phrases ce que tu feras plus tard cote serveur, meme si tu ne sais pas encore comment. Le but : savoir ce qui manque - posture de pilote DanielCraft. Garde ce formulaire : tu le styliseras au chapitre CSS, et tu le reprendras au mini-projet.
