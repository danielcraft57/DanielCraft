# Chapitre 9 - Styler un formulaire proprement

Tu sais faire un formulaire HTML (champs, labels, bouton submit). La, on le rend agreable et clair. Pas un theme de science-fiction. Un formulaire ou on a envie de taper son email.

Sur une landing, le formulaire d'inscription est souvent le moment de verite. Sur un blog, le contact aussi. Chez DanielCraft, un champ lisible + un bouton evident, ca convertit mieux qu'une animation tape-a-l'oeil.

## HTML d'abord, toujours

```html
<form class="form" action="#" method="post">
  <p>
    <label for="nom">Nom</label>
    <input id="nom" name="nom" type="text" autocomplete="name" required>
  </p>
  <p>
    <label for="email">Email</label>
    <input id="email" name="email" type="email" autocomplete="email" required>
  </p>
  <p>
    <label for="message">Message</label>
    <textarea id="message" name="message" rows="4"></textarea>
  </p>
  <p>
    <button type="submit">Envoyer</button>
  </p>
</form>
```

Label visible, relie avec `for` / `id`. Pas seulement un placeholder. Le placeholder disparait a la saisie ; le label reste. `autocomplete` aide les navigateurs et les gestionnaires de mots de passe.

## Une colonne claire

```css
.form {
  display: grid;
  gap: 1rem;
  max-width: 28rem;
}

.form label {
  display: block;
  margin-bottom: 0.35rem;
  font-weight: 600;
}

.form input,
.form textarea {
  width: 100%;
  padding: 0.65rem 0.75rem;
  border: 1px solid var(--champ-bordure, #ccc);
  border-radius: var(--rayon, 8px);
  font: inherit;
  background: #fff;
  color: inherit;
}
```

`font: inherit` evite les champs avec une police systeme bizarre differente du reste. `width: 100%` dans un conteneur borne, c'est confortable sur mobile.

## Focus visible

Quand on tabule jusqu'au champ, il faut voir ou on est.

```css
.form input:focus,
.form textarea:focus {
  border-color: var(--couleur-principale, #1a5f4a);
  outline: 2px solid var(--couleur-principale, #1a5f4a);
  outline-offset: 2px;
}
```

Ne supprime pas `outline` sans remplacement. C'est un classique d'accessibilite (on y revient au chapitre 11).

## Bouton coherent

```css
.form button {
  border: 0;
  border-radius: var(--rayon, 8px);
  padding: 0.75rem 1.25rem;
  background: var(--couleur-principale, #1a5f4a);
  color: #fff;
  font: inherit;
  cursor: pointer;
}

.form button:hover {
  filter: brightness(1.05);
}

.form button:focus-visible {
  outline: 2px solid var(--couleur-principale, #1a5f4a);
  outline-offset: 3px;
}
```

Le bouton ressemble au reste du site grace aux variables. Pas un gris systeme perdu dans le coin.

## Deux champs cote a cote (desktop)

```css
.form-rangee {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

@media (max-width: 600px) {
  .form-rangee {
    grid-template-columns: 1fr;
  }
}
```

Prenom / nom sur desktop, empiles sur mobile. Grid rend ca limpide.

## Etats d'erreur (leger)

Sans JavaScript pousse, tu peux deja styler `:invalid` avec prudence (certains navigateurs le montrent tot) :

```css
.form input:user-invalid {
  border-color: #a12;
}
```

Si `:user-invalid` n'est pas dispo partout chez toi, garde un style d'erreur via une classe `.champ-erreur` ajoutee plus tard. L'important : le message d'erreur en texte, pas seulement la couleur.

## Case a cocher et radio

Laisse assez d'espace cliquable. Associe toujours label et input. Evite de reduire la case a 8px invisibles.

```css
.form-check {
  display: flex;
  align-items: flex-start;
  gap: 0.5rem;
}
```

Flex pour aligner case + texte. Simple.

## Erreur classique

Placeholder comme seul label. Champs trop etroits au centre avec du blanc partout sur mobile. Bouton submit sans type clair. Couleur de bordure trop pale sur fond pale (contraste). `outline: none` global sur tous les inputs.

Autre piege : styler uniquement l'etat "beau au repos" et oublier hover / focus / disabled.

## En vrai

Reprends le formulaire contact d'une landing. Passe-le en grille verticale, labels au-dessus, variables de marque, focus visible. Navigue au clavier uniquement. Demande a quelqu'un de le remplir sans explication : s'il hesite, clarifie les labels.

Compare un champ natif non style et le tien : le tien doit rester evidemment un champ, pas un mystere design.

## A toi

Formulaire "Inscription atelier" : nom, email, choix de creneau (`select`), message, bouton. Style coherent avec un `:root` de variables. Rangee prenom/nom en deux colonnes desktop. Test Tab complet. Aucun `outline: none` sans alternative.
