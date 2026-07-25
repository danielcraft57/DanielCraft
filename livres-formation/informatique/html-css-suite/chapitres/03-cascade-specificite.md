# Chapitre 3 - Cascade et specificite : qui gagne ?

Tu ecris une regle. Tu en ecris une autre. La couleur ne change pas. Ou elle change, mais pas celle que tu voulais. Bienvenue dans la **cascade**. Ce n'est pas un monstre. C'est l'ordre dans lequel le navigateur decide quelle regle CSS l'emporte. La **specificite**, c'est le "poids" d'un selecteur. Ensemble, elles expliquent presque tous les "pourquoi ca marche pas".

Chez DanielCraft, on compare ca a des couches de peinture : la derniere couche visible gagne, sauf si une couche precedente etait beaucoup plus "forte" (vernis special). Tu n'as pas besoin de jargon opaque. Tu as besoin d'instinct. Lea ouvre l'inspecteur avant de crier au bug. Max appelle ca "trouver qui commande le bouton". Sam note au tableau : ordre, poids, inline, `!important` - dans cet ordre de suspicion.

## L'ordre compte

A poids egal, la regle la plus basse dans le fichier (la derniere lue) gagne en general.

```css
.titre {
  color: blue;
}

.titre {
  color: green;
}
```

Le titre sera vert. Deuxieme declaration, meme selecteur : elle ecrase la premiere. Si tu charges deux feuilles CSS, l'ordre des `<link>` compte aussi. La feuille liee en dernier peut ecraser la precedente, a specificite egale.

## Qu'est-ce qui pese plus ?

Sans rentrer dans une formule magique a retenir par coeur, retiens cette echelle simple, du plus faible au plus fort. Un selecteur de type (`p`, `h1`) pese peu. Une **classe** (`.carte`, `.bouton`) pese plus. Un identifiant (`#menu`) pese encore plus. Les styles inline dans le HTML (`style="..."`) pesent tres fort (a eviter pour le travail serieux). `!important` force encore plus fort (a utiliser presque jamais).

```css
p {
  color: black;
}

.intro {
  color: #1a5f4a;
}

#accroche {
  color: red;
}
```

Sur `<p id="accroche" class="intro">`, le rouge de `#accroche` gagne. Pas parce qu'il est "mieux", parce qu'il pese plus.

## Classes plutot que ID pour le style

Les ID sont utiles en HTML (cibles de liens, labels `for`). Pour le CSS du quotidien, prefere les classes. Pourquoi ? Parce qu'un ID trop present dans le CSS rend les overrides douloureux. Tu te retrouves a monter en `!important` ou a empiler des selecteurs monstrueux.

Sur une landing, `.hero-titre` se reutilise et se surcharge proprement. `#hero-titre` devient un piege des que tu veux une variante. Lea a appris ca en livrant une variante "promo" : avec des classes, dix minutes ; avec des ID, une soiree de bagarre.

:::astuce
Quand une couleur "refuse" de changer, F12 > Styles. Cherche la propriete barree. Tu vois le gagnant. Ensuite tu corriges avec intention : ordre, poids, ou selecteur plus clair - pas au hasard.
:::

## Selecteurs composes

`.carte .prix` est plus specifique qu'un simple `.prix`. Normal : tu as cible plus precisement.

```css
.prix {
  color: #333;
}

.carte .prix {
  color: #1a5f4a;
}
```

Dans une carte produit, le prix prend le vert. Ailleurs, un `.prix` seul reste gris fonce. Attention a ne pas ecrire des selecteurs kilometriques du type `body div main section article div p span`. Plus c'est long, plus c'est fragile.

## Heritage (rapide)

Certaines proprietes se transmettent aux enfants (couleur de texte, police...). D'autres non (margin, padding, border en general). Si un paragraphe "prend" la couleur du `body`, ce n'est pas toujours la cascade qui ecrase : c'est l'**heritage**. Quand tu debogues : demande-toi "est-ce une regle qui s'applique a cet element, ou une valeur heritee du parent ?"

## Conflit classique sur une carte

```css
a {
  color: blue;
}

.carte a {
  color: inherit;
}

.bouton {
  color: white;
  background: #1a5f4a;
}
```

Si ton bouton est un lien `<a class="bouton">`, tu peux avoir une bataille entre `a`, `.carte a` et `.bouton`. Regarde dans l'inspecteur quelle regle est barree. C'est la meilleure lecon. Sam fait exactement cet exo en classe : les eleves voient le gagnant avant de "deviner".

## !important, le extincteur

`!important` eteint l'incendie... et detruit souvent la maison ensuite. Une fois que tu en mets partout, plus rien n'est previsible. Garde-le pour des cas rares (utile temporairement pour debug, ou contrainte tres particuliere). Le vrai fix, c'est : selecteur un peu plus clair, ordre du fichier, moins d'ID.

## Ce que ce n'est pas

Ce n'est pas une formule a recracher par coeur le jour du quiz. Ce n'est pas non plus "mettre un ID partout pour etre sur de gagner". Tu gagnes aujourd'hui, tu perds demain. Et ce n'est surtout pas modifier le HTML en inline `style=""` parce que "ca marche tout de suite". Ca marche, et ca pollue.

:::attention
`!important` et les styles inline calment la panique une minute, puis rendent la cascade illegible. Prefere classes claires, ordre du fichier, inspecteur.
:::

## Petite histoire

Lea avait un bouton CTA qui restait bleu "lien" malgre sa classe `.bouton`. L'inspecteur montrait `.carte a` plus fort. Elle a clarifie le selecteur du bouton, retire un `!important` temporaire, et respire. Max avait colle `style="color:red"` sur un titre "pour voir". Son neveu a refuse de toucher le fichier tant que l'inline etait la. Sam appelle ca "la regle du vernis : si tout est vernis, plus rien ne se voit".

## Erreur classique

Penser "je vais mettre un ID, comme ca je suis sur que ca gagne". Ou empiler trois classes inventees (`.bloc.special.urgent`) au lieu de clarifier la structure. Autre piege : modifier le HTML en inline parce que ca marche tout de suite. Autre encore : paniquer et tout mettre en `!important`.

## En vrai

Ouvre une page ou un style "refuse" de s'appliquer. F12, inspecte l'element, onglet Styles. Cherche la propriete barree. Remonte au selecteur gagnant. Demande-toi : ordre ? poids ? inline ? Une fois que tu vois le gagnant, tu corriges avec intention.

Fais le meme exercice sur une landing avec menu + bouton. Regarde quelle regle colore les liens du menu vs le bouton CTA.

## A toi

Cree une mini page avec un paragraphe `.intro` et un titre `#titre` (oui, un ID, pour l'exercice). Ecris volontairement des regles conflictuelles (type, classe, ID) sur la couleur. Note sur papier qui gagne avant d'ouvrir l'inspecteur. Verifie. Ensuite, retire l'ID du CSS et refais le style uniquement avec des classes. Garde la lecon.

:::retenir
A poids egal, la derniere regle gagne. Classes > types. Evite ID et `!important` pour le style quotidien. L'inspecteur montre qui gagne.
:::
