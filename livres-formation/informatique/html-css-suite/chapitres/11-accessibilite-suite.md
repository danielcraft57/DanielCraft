# Chapitre 11 - Accessibilite suite : focus, contrastes, labels

Le premier livre a plante le decor : textes lisibles, alt, structure. Ici, on solidifie trois reflexes qui changent vraiment la vie des gens : focus visible, contrastes, labels (et un peu d'ordre au clavier).

Accessibilite, ce n'est pas un badge. C'est "est-ce que quelqu'un d'autre que moi peut utiliser cette page sans souffrir ?". Chez DanielCraft, on le traite comme de la qualite produit, pas comme un bonus cosmetique.

## Focus visible : savoir ou on est

Beaucoup de gens naviguent au clavier (Tab, Shift+Tab, Entree). Si tu enleves les contours de focus parce que "c'est moche", tu les perds dans la page.

```css
:focus-visible {
  outline: 2px solid var(--couleur-principale, #1a5f4a);
  outline-offset: 2px;
}
```

`:focus-visible` cible surtout le focus clavier (selon navigateurs / contexte), ce qui evite parfois un anneau au simple clic souris. Tu peux affiner par composant (boutons, liens, champs).

```css
.bouton:focus-visible {
  outline: 3px solid var(--couleur-principale);
  outline-offset: 3px;
}
```

Test minimal : charge ta page, cache la souris, Tab jusqu'au bout. Tu dois toujours voir clairement l'element actif.

## Contrastes : lisible, pas juste joli

Texte gris pale sur fond beige, ca fait "design soft"... et illegible au soleil ou avec une vue fatiguee. Vise un contraste solide entre texte et fond.

Regles pratiques :

Texte courant sombre sur fond clair, ou texte clair sur fond sombre.

Les liens ne se distinguent pas seulement par la couleur (souligne au hover/focus, ou poids).

Les placeholders tres clairs ne remplacent pas un label.

Tu peux verifier avec un outil de contraste (extensions, sites de check). Si tu hesites entre deux beiges, choisis le plus lisible. La marque survit a un contraste correct.

```css
:root {
  --couleur-texte: #1b1b1b;
  --couleur-fond: #f7f5f0;
  --couleur-muette: #444;
}
```

`--couleur-muette` trop claire (#aaa sur blanc) devient un piege pour les mentions legales.

## Labels : dire le nom des champs

On l'a vu au chapitre formulaires. On insiste parce que c'est le bug n°1 des "jolis" formulaires.

```html
<label for="email">Email</label>
<input id="email" type="email" name="email">
```

Pas ca :

```html
<input type="email" placeholder="Email">
```

Le placeholder peut aider en exemple (`nom@domaine.fr`), pas en remplacement du label.

Pour une case a cocher :

```html
<label>
  <input type="checkbox" name="newsletter">
  J'accepte de recevoir la newsletter
</label>
```

Ou `for`/`id` separes. L'important : le nom est annonce clairement.

## Ordre de tabulation naturel

L'ordre du HTML guide le Tab. Si tu deplaces visuellement des blocs avec Grid/Flex, l'ordre visuel peut diverger de l'ordre clavier. En cas de doute, rearrange le HTML pour coller a l'ordre de lecture logique (entete, contenu, aside...).

Evite `tabindex` positifs inventes (1, 2, 3...) : ca devient un labyrinthe. `tabindex="0"` parfois pour rendre un element focusable ; `tabindex="-1"` pour du focus programme. Au debut, le HTML bien ordonne suffit.

## Images et boutons

Image informative → `alt` utile.

Bouton icone seul → nom accessible (texte visible, ou `aria-label` si vraiment icone seule).

```html
<button type="button" aria-label="Fermer">X</button>
```

Mieux encore : un texte "Fermer" visible si tu as la place.

## Landing : checklist express

Un seul `h1`.

Menu atteignable au clavier.

CTA avec focus visible.

Contraste du texte hero (attention texte blanc sur photo claire : ajoute un voile sombre).

Formulaire avec labels.

```css
.hero {
  background: linear-gradient(rgba(0, 0, 0, 0.45), rgba(0, 0, 0, 0.45)),
    url("hero.jpg") center/cover;
  color: #fff;
}
```

Le degrade aide le contraste du texte sur image.

## Erreur classique

`outline: none` global. Liens oranges sur fond orange. Formulaire "flottant" sans labels. Modale ou menu qui piege le focus (sujet avance : au moins, ne casse pas Tab sur une page simple).

Autre piege : croire que "personne ne navigue au clavier". Faux. Et meme parmi les souris, certains ont besoin de focus clair.

## En vrai

Prends ta page produit ou landing. Fais le parcours Tab complet. Note chaque trou (focus invisible, ordre bizarre). Monte le contraste d'un texte secondaire trop pale. Verifie chaque `input` pour un label.

Si tu peux, active un lecteur d'ecran basique juste cinq minutes (Narrateur sur Windows, VoiceOver sur Mac) et ecoute la page. Tu entendras vite les trous.

## A toi

Ameliore une page existante avec trois commits mentaux : (1) `:focus-visible` global propre, (2) correction de deux contrastes faibles, (3) labels complets sur un formulaire. Ecris en trois lignes ce que tu as change. C'est ton "rapport a11y" personnel.
