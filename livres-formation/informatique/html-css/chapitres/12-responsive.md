# Chapitre 12 - Un site qui marche sur telephone

La plupart des gens regardent le web sur mobile.
Si ta page est illisible sur telephone, c'est rate.

## La balise magique (viewport)

Dans le `<head>` :

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

Sans ca, le telephone croit que ta page fait la largeur d'un grand ecran et zoom de facon horrible.
Mets-la. Toujours.

## Largeurs souples

```css
img {
  max-width: 100%;
  height: auto;
}

.conteneur {
  width: min(100% - 2rem, 700px);
  margin-inline: auto;
}
```

Traduction : la boite ne depasse pas 700px, et sur petit ecran elle prend la place dispo avec un peu d'air.

## Media queries

```css
.menu {
  display: flex;
  gap: 1rem;
}

@media (max-width: 600px) {
  .menu {
    flex-direction: column;
  }
}
```

En dessous de 600px de large, le menu passe en colonne.
Tu adaptes. Tu ne fais pas "un autre site". Tu ajustes.

## Tailles de doigt

Sur mobile, les boutons trop petits c'est l'enfer.
Vise une zone cliquable confortable (genre 40px+ de haut).

## Teste vraiment

- Reduis la fenetre de ton navigateur
- Ou ouvre les outils developpeur (F12) et le mode telephone
- Ou regarde sur ton vrai telephone (en local c'est plus technique, on verra plus tard)

## Checklist mobile

- [ ] meta viewport presente
- [ ] images qui ne debordent pas
- [ ] texte lisible sans zoomer
- [ ] boutons assez grands
- [ ] pas de scroll horizontal bizarre

## A toi

Prends ta page et ajoute le viewport.
Passe le menu en colonne sous 600px.
Verifie en redimensionnant la fenetre.
