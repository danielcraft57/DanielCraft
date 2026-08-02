# Chapitre 17 - Dark mode avec variables

Tu as deja theme une page via `:root`. Le dark mode, c'est la meme idee, branchee sur la preference systeme (et/ou un choix manuel). Pas besoin de doubler tout ton CSS. Tu redefinis les variables. Le reste suit.

Chez DanielCraft, un mode sombre lisible, c'est un confort nocturne, pas un filtre gris illisible. Contraste d'abord, ambiance ensuite. Lea livre souvent les deux themes d'un coup. Max lit ses devis le soir sur le canape : il veut du lisible, pas du "style OLED". Sam montre en classe le bascule systeme des outils developpeur - les eleves voient la page changer sans toucher aux composants.

## Ce que ce n'est pas

Ce n'est pas dupliquer toutes les classes (`.carte-dark`, `.bouton-dark`...). Ce n'est pas inverser seulement le fond et oublier cartes et champs. Ce n'est pas non plus un noir pur `#000` partout "parce que ca fait tech". Et ce n'est surtout pas activer un dark mode alors que ta page a encore des hex en dur partout. Discipline variables d'abord.

## Preference systeme

Le systeme de l'utilisateur demande parfois un theme sombre. Toi, tu ecoutes cette demande dans un media query, tu reecris les variables du `:root`, et toute la page bascule. Ensuite, si tu veux, tu ajoutes une classe manuelle qui force clair ou sombre - parce que le choix explicite de l'humain gagne souvent sur le reglage systeme. Les composants ne bougent pas. Seule la palette bouge.

```css
:root {
  --fond: #f7f5f0;
  --texte: #1b1b1b;
  --carte: #ffffff;
  --couleur-principale: #1a5f4a;
  --bordure: #ddd;
  color-scheme: light dark;
}

@media (prefers-color-scheme: dark) {
  :root {
    --fond: #121a17;
    --texte: #e8f0eb;
    --carte: #1a2822;
    --couleur-principale: #5dcaa5;
    --bordure: #2c3d34;
  }
}

body {
  background: var(--fond);
  color: var(--texte);
}
```

`color-scheme: light dark` aide le navigateur sur les controles natifs (scrollbars, champs) pour qu'ils ne restent pas "blancs agressifs" en theme sombre. Pas magique partout, mais bon reflexe.

:::retenir
Redefinis les variables, pas les classes. Contraste d'abord, ambiance ensuite. Inputs et ombres doivent suivre le theme aussi.
:::

## Bascule manuelle, ombres, formulaires

```css
html.theme-dark {
  --fond: #121a17;
  --texte: #e8f0eb;
  --carte: #1a2822;
  --couleur-principale: #5dcaa5;
  --bordure: #2c3d34;
  --ombre: 0 4px 18px rgba(0, 0, 0, 0.45);
}
```

Un bouton "Mode sombre" en JavaScript bascule la classe. Ce livre ne force pas le JS : tu peux tester en collant la classe a la main. Si tu ajoutes le JS plus tard, le CSS est deja pret. Decide si la classe manuelle doit gagner sur `prefers-color-scheme`. Souvent oui.

Une ombre douce en clair devient un halo bizarre ou invisible en sombre : passe aussi `--ombre` en variable. Les photos restent des photos. N'assombris pas une image informative jusqu'a la rendre inutile. Pour les champs :

```css
input,
textarea,
select {
  background: var(--carte);
  color: var(--texte);
  border: 1px solid var(--bordure);
}
```

Sans ca, des champs blancs eclatent dans une page sombre.

## Contrastes, pas ambiance

Le dark mode "instagrammable" trompe. Vert menthe pale sur fond tres sombre, magnifique en capture, illisible en paragraphe. Lea l'a appris chez un client. Elle a eclairci `--texte`, teinte le fond, corrige les inputs. Le client a prefere la version lisible. Max teste le soir sur le canape. Sam chronometre : "lis ce paragraphe a voix haute en theme sombre". Si tu butes, le contraste est trop faible.

Verifie aussi les CTA et les liens. Un bouton qui disparait en sombre, c'est pire qu'un fond un peu trop gris. Chez DanielCraft, lisibilite d'abord, ambiance ensuite. Un presque noir teinte (`#121a17`) est souvent plus doux qu'un noir pur sur OLED.

## Petite histoire

Lea avait livre un dark mode "instagrammable" : vert menthe pale sur fond tres sombre. Elle a eclairci `--texte`, fonce legerement le fond teinte, et corrige les inputs. Max a teste le theme sombre de sa page artisan : le bouton devis restait vert clair sur vert clair - oubli de variable sur le bouton. Sam a transforme l'incident en exo de contraste.

:::attention
Contrastes insuffisants "parce que c'est style". Ou CTA qui disparait. Ou champs blancs oublies dans une page sombre. Verifie texte, liens, boutons, labels, inputs.
:::

## Erreur classique

Dupliquer toutes les classes en `.dark`. Activer le mode sombre alors que des hex trainent partout. Hero qui depend du `--fond` sans test des deux themes.

## En vrai

Reprends le mini-projet ou l'atelier variables. Ajoute le media `prefers-color-scheme: dark`. Bascule le theme OS (ou l'emulation dans les outils developpeur). Regarde formulaire, cartes, header. Ajoute ensuite `html.theme-dark` comme override manuel et teste les deux chemins.

## A toi

Active le dark mode par variables sur une page complete (pas un seul bloc). Checklist : body, cartes, bordures, bouton, inputs, ombres. Note une couleur que tu as du corriger pour le contraste. C'est bon signe : tu regardes vraiment. Chez DanielCraft, ce regard-la compte plus qu'un theme "wow" illegible.
