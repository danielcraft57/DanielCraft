# Chapitre 17 - Dark mode avec variables

Tu as deja theme une page via `:root`. Le dark mode, c'est la meme idee, branchee sur la preference systeme (et/ou un choix manuel). Pas besoin de doubler tout ton CSS. Tu redefinis les variables.

Chez DanielCraft, un mode sombre lisible, c'est un confort nocturne, pas un filtre gris illisible. Contraste d'abord.

## Prefers-color-scheme

Le systeme de l'utilisateur peut demander un theme sombre.

```css
:root {
  --fond: #f7f5f0;
  --texte: #1b1b1b;
  --carte: #ffffff;
  --couleur-principale: #1a5f4a;
  --bordure: #ddd;
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

Tout ce qui consomme les variables bascule. Les classes de composants ne bougent pas. C'est exactement pour ca qu'on a discipline le theme a l'atelier variables.

## Color-scheme (detail utile)

```css
:root {
  color-scheme: light dark;
}
```

Ca aide le navigateur sur les controles natifs (scrollbars, champs) pour qu'ils ne restent pas "blancs agressifs" en theme sombre. Pas magique partout, mais bon reflexe.

## Bascule manuelle (classe)

Le systeme ne suffit pas toujours : certains veulent forcer clair/sombre. Une classe sur `html` ou `body` :

```css
html.theme-dark {
  --fond: #121a17;
  --texte: #e8f0eb;
  --carte: #1a2822;
  --couleur-principale: #5dcaa5;
  --bordure: #2c3d34;
}
```

Un bouton "Mode sombre" en JavaScript bascule la classe. Ce livre ne force pas le JS : tu peux tester en collant la classe a la main. Si tu ajoutes le JS plus tard, le CSS est deja pret.

Attention a la priorite : decide si la classe manuelle doit gagner sur `prefers-color-scheme`. Souvent oui (choix utilisateur explicite).

## Images et ombres

Une ombre douce en clair devient un halo bizarre ou invisible en sombre. Variables :

```css
:root {
  --ombre: 0 4px 14px rgba(0, 0, 0, 0.08);
}

html.theme-dark {
  --ombre: 0 4px 18px rgba(0, 0, 0, 0.45);
}
```

Les images photos restent des photos. Parfois tu baisses legerement l'opacite d'une image decorative en sombre, mais n'assombris pas une image informative jusqu'a la rendre inutile.

## Formulaires en sombre

```css
input,
textarea,
select {
  background: var(--carte);
  color: var(--texte);
  border: 1px solid var(--bordure);
}
```

Sans ca, des champs blancs eclatent dans une page sombre. Inclue-les dans le systeme de variables.

## Contrastes : double check

Un vert menthe sur fond sombre peut etre magnifique et illegible en petit texte. Verifie :

Texte courant.

Liens.

Boutons (texte sur fond principal).

Labels et mentions.

Si besoin, eclaircis `--texte` ou fonce `--fond`. Le "vrai noir" `#000` pur sur OLED est discutable ; un presque noir teinte (`#121a17`) est souvent plus doux.

## Landing : hero en sombre

Si le hero a deja un voile sombre pour du texte blanc, il peut rester valable dans les deux themes. Si le hero depend du `--fond`, test les deux. Un CTA doit rester evidemment cliquable.

## Erreur classique

Dupliquer toutes les classes (`.carte-dark`, `.bouton-dark`...) au lieu des variables. Ou inverser seulement le fond et oublier les cartes/champs. Ou contrastes insuffisants "parce que c'est style".

Autre piege : dark mode active alors que ta page a encore des hex en dur partout. Corrige d'abord la discipline variables.

## En vrai

Reprends le mini-projet ou l'atelier variables. Ajoute le media `prefers-color-scheme: dark` qui redefinit les variables. Bascule le theme OS (ou l'emulation dans les outils developpeur : prefers-color-scheme). Regarde formulaire, cartes, header.

Ajoute ensuite `html.theme-dark` comme override manuel et teste les deux.

## A toi

Active le dark mode par variables sur une page complete (pas un seul bloc). Checklist : body, cartes, bordures, bouton, inputs, ombres. Note une couleur que tu as du corriger pour le contraste. C'est bon signe : tu regardes vraiment.
