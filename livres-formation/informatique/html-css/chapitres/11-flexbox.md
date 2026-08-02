# Chapitre 11 - Flexbox : ranger les blocs

**Flexbox**, c'est l'outil qui range les blocs sur une page. Menu en ligne, colonnes qui s'alignent, logo a gauche et liens a droite, centrage vertical sans pleurer : ca sauve des soirees entieres. Avant Flexbox, les developpeurs bricolaient avec des floats, des clearfix et des coleres silencieuses. Aujourd'hui, tu dis a un parent : "range tes enfants en flex". Ils obeissent. Chez DanielCraft, on l'apprend des qu'on a compris les boites, parce que le web moderne aligne beaucoup de choses cote a cote ou les unes sous les autres.

Tu as deux roles a retenir. Le **conteneur flex** (le parent) recoit `display: flex`. Les **items flex** (les enfants) se placent selon les regles que tu choisis. Tu peux les mettre en ligne, en colonne, les centrer, les repartir, leur donner de l'espace. La propriete **`gap`** ajoute de l'air entre eux proprement, sans empiler des margins hasardeuses. Flexbox ne remplace pas le HTML semantique : il range ce qui existe deja.

Lea, freelance web, utilise Flexbox sur presque chaque livraison client. Max, artisan, l'a decouvert quand il voulait aligner son logo et son numero sur la meme barre. Sam, enseignant, fait un atelier ou les eleves doivent reproduire une barre de navigation : ils finissent toujours par tomber sur flex. Trois metiers, un meme outil. En 2026, quand quelqu'un dit "j'aligne avec flex", il parle souvent de ca. Derriere, il y a Grid. Pour toi, le geste reste : parent flex, enfants ranges. Tu restes le pilote.

:::retenir
Flexbox = le parent range les enfants. `display: flex` sur le conteneur, pas sur chaque enfant.
:::

## Ce que ce n'est pas

Ce n'est pas **CSS Grid**, l'autre grand outil de mise en page (on le verra plus tard dans ta formation). Ce n'est pas obligatoire sur chaque `<div>` de la page : si un bloc est seul, inutile de le flexer. Ce n'est pas magique sans reflechir a l'axe : tu dois savoir si tu ranges en ligne (`row`) ou en colonne (`column`). Et ce n'est surtout pas une excuse pour oublier la structure HTML : Flexbox aligne, il ne remplace pas `<header>`, `<nav>`, `<main>` et le sens du contenu.

Ce n'est pas non plus "je mets flex partout et ca marche". Sans `gap`, sans axe clair, tu recrees le bordel d'avant avec un autre outil. Lea dit : "flex avec intention, pas flex par panique".

Imagine une etagere. Le meuble est le conteneur flex. Les boites posees dessus sont les items. Tu decides si elles se mettent cote a cote ou empilees. Tu decides si elles collent a gauche, se centrent, ou se repartissent. **`justify-content`** travaille sur l'axe principal. **`align-items`** travaille sur l'axe croise. Tu experimentes, tu changes une valeur, tu regardes. C'est normal de confondre les deux au debut. Max les confond encore parfois. Sam fait changer une valeur a la fois en classe. Lea chronometre : "cinq minutes pour une barre propre".

```html
<div class="rangee">
  <div>A</div>
  <div>B</div>
  <div>C</div>
</div>
```

```css
.rangee {
  display: flex;
  gap: 16px;
}
```

Trois blocs cote a cote, espaces proprement. Simple. Efficace. Chez DanielCraft, ce mini exemple se montre en trente secondes.

## Direction et alignement

La direction par defaut est `row` : les enfants se placent en ligne. Passe en `column` et ils s'empilent. Pour une barre de navigation classique :

```css
.rangee {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

.colonne {
  display: flex;
  flex-direction: column;
}
```

`space-between` pousse le premier element a gauche et le dernier a droite. `align-items: center` aligne verticalement au milieu. Pour centrer un bloc au coeur d'une zone :

```css
.centre {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 200px;
}
```

Les enfants peuvent aussi partager l'espace avec `flex: 1`. Pratique pour trois cartes de meme largeur :

```css
.rangee > div {
  flex: 1;
}
```

:::astuce
Logo a gauche, liens a droite : flex + `justify-content: space-between` + `align-items: center`. Cinq lignes de CSS, barre propre. Lea livre ca en dix minutes.
:::

## Petite histoire

Lea devait aligner un logo a gauche et deux liens a droite pour un fleuriste. Avant Flexbox, elle bricolait des floats et des largeurs fixes qui cassaient au premier redimensionnement. Maintenant : un conteneur flex, `space-between`, `align-items: center`, `gap` si besoin. Cinq lignes. Livraison propre. Max voulait empiler ses boutons d'appel sur telephone : meme conteneur, mais `flex-direction: column` dans une media query. Sam fait ses eleves chercher seuls : quand ils trouvent flex, ils comprennent pourquoi le web moderne ne souffre plus autant qu'avant. Trois scenes, un outil.

## Erreur classique

Mettre `display: flex` sur l'enfant au lieu du parent. C'est l'erreur numero un. Si rien ne range, verifie ou tu as ecrit flex. Confondre `justify-content` et `align-items` pendant trois jours, c'est normal aussi : change une valeur, regarde, recommence. Oublier `gap` et compenser avec des margins inegales sur chaque enfant, ca desaligne vite. Forcer des largeurs fixes partout et perdre la souplesse de flex, c'est retomber dans les vieilles habitudes.

:::attention
`display: flex` se met sur le parent, pas sur chaque enfant. Si ca ne range pas, c'est souvent la premiere chose a verifier.
:::

## En vrai

Ouvre ta page perso ou une page vierge. Cree une barre avec un "logo" (un mot en gras) a gauche et deux liens a droite. Indice : flex + `space-between` + `align-items: center`. Puis passe la barre en colonne avec `flex-direction: column`. Observe la difference. Cinq minutes actives valent mieux qu'une lecture passive. Si ca ne range pas, regarde le parent. Toujours le parent.

## A toi

Cree trois cartes cote a cote avec `display: flex` et `gap`, chacune avec un titre et un paragraphe. Ajoute `flex: 1` sur les enfants pour qu'elles partagent l'espace. Reduis la fenetre du navigateur : si ca se serre bizarrement, note-le pour le chapitre responsive. Tu prepares le terrain pour la suite. Style DanielCraft : petit layout clair, testable, montrable.
