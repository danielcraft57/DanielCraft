# Chapitre 8 - CSS : on habille la page

La, le HTML est nu. On va lui mettre des habits. Le **CSS** ne cree pas le contenu : il decide comment le contenu apparait - couleurs, tailles, espacements, alignements. Chez DanielCraft, on branche le CSS le plus tot possible dans un fichier separe, parce que melanger tout dans le HTML devient vite le bordel. Lea travaille presque toujours en fichier separe. Max a commence en `<style>`, puis a migre. Sam interdit le style en ligne des la deuxieme seance.

Il y a trois facons d'ajouter du CSS. Dans une balise `<style>` dans le `head` : pratique pour tester. Dans un fichier **`style.css`** relie par `<link>` : le mieux pour un vrai projet. En ligne avec `style="..."` sur une balise : a eviter souvent. En 2026, quand quelqu'un dit "j'ai du CSS", il parle souvent du fichier separe. Derriere, il y a des preprocesseurs et des frameworks. Pour toi, le geste reste : selecteur, propriete, valeur, fichier branche. Tu restes le pilote. La page s'habille.

:::retenir
Fichier `style.css` + `<link>` dans le head. Selecteur + propriete + valeur. Verifie le branchement avant de paniquer.
:::

## Ce que ce n'est pas

Ce n'est pas un remplacement du HTML. Sans structure, le plus beau CSS habille du vide. Ce n'est pas non plus "une seule facon absolue" : les trois methodes existent, mais la discipline compte. Ce n'est pas magique : une typo dans un **selecteur** et "rien ne change". Tu verifieras. Ce n'est pas non plus JavaScript : le CSS ne calcule pas, ne verifie pas, ne charge pas des donnees.

Ce n'est pas "joli = bon". Un CSS peut rendre une page illisible. La lisibilite reste la base. On habille, on n'etouffe pas. Lea dit : "si tu ne lis plus ton texte, ce n'est pas du design, c'est du bruit".

Le HTML pose les meubles. Le CSS choisit peinture, luminaires, distances. Le selecteur CSS dit "qui" (tous les `p`, le `h1`, la classe `.carte`). Les **proprietes** disent "quoi" (`color`, `font-size`...). Tu parles a des etiquettes. Si l'etiquette HTML n'existe pas, le CSS parle dans le vide. Lea dit : "selecteur = adresse ; propriete = instruction". Max retient : "si rien ne change, je regarde le link d'abord". Sam dessine la chaine au tableau : HTML, link, CSS, navigateur.

## Fichier CSS separe (le mieux)

`style.css` :

```css
p {
  color: blue;
}
```

Dans le HTML, dans le `<head>` :

```html
<link rel="stylesheet" href="style.css">
```

Cree le fichier a cote de `index.html`. Relie. Rafraichis. Si les paragraphes deviennent bleus, c'est branche. Si rien ne bouge, ne reecris pas dix regles : verifie le chemin du `<link>` en premier. Une lettre suffit a tout casser (`styles.css` vs `style.css`). Lea a perdu une heure la-dessus. Max aussi. Sam le piege volontairement.

:::astuce
Prefere un fichier `style.css` des le debut. Tu gagnes en clarte, en reutilisation, en calme.
:::

## Anatomie d'une regle

```css
selecteur {
  propriete: valeur;
}

h1 {
  color: tomato;
  font-size: 40px;
}
```

Commentaire CSS : `/* note pour toi */`. Utile comme les commentaires HTML, dans un autre dialecte. Chaque ligne se termine par un point-virgule `;`. Les deux-points `:` separent propriete et valeur. Une faute la, et toute la regle peut etre ignoree. Chez DanielCraft, on lit la syntaxe avant de blamer le navigateur.

## Petite histoire

Lea a passe une heure a "deboguer le bleu" : le `<link>` pointait vers `styles.css` alors que le fichier s'appelait `style.css`. Une lettre. Max avait mis le link apres `</html>` : ignore. Sam projette volontairement un mauvais chemin et fait chercher la classe. Le geste devient un reflexe : verifier le branchement avant de reecrire dix regles.

Max avait aussi ecrit `color blue` sans deux-points. Rien ne marchait. Il a cru que "CSS etait casse". Une correction de syntaxe, tout est parti. Lea garde cette phrase sur un post-it : "d'abord le link, ensuite la syntaxe, ensuite le selecteur". Trois scenes, une methode.

:::attention
Si "rien ne change" : verifie le `<link>`, le nom du fichier, puis la syntaxe (`:` et `;`). Dans cet ordre.
:::

## Erreur classique

Oublier le `<link>`. Se tromper de nom de fichier (casse comprise). Ecrire `color blue;` sans deux-points. Oublier le point-virgule et croire que "CSS est casse" alors qu'une seule ligne derape. Mettre du style en ligne partout puis ne plus oser toucher. Prefere un fichier. Autre piege : modifier le CSS sans rafraichir le navigateur - meme reflexe que pour le HTML : F5. Lea chronometre parfois le debug "rien ne change" : sous deux minutes si on suit l'ordre.

## En vrai

Cree `style.css` a cote de `index.html`. Relie-les avec `<link>`. Mets tous les `p` en bleu. Rafraichis. Puis change `h1 { color: teal; }`. Si ca bouge, tu pilotes. Deplace une regle dans un `<style>` temporaire pour tester, puis remets-la dans le fichier : tu sens pourquoi DanielCraft pousse le fichier separe. Casse volontairement le chemin. Lis. Repare. Le contraste enseigne.

## A toi

Ecris trois regles : couleur de fond du `body`, couleur du `h1`, taille des `p`. Ensuite deplace une regle du fichier vers un `<style>` temporaire, teste, remets dans le fichier. Tu dois sentir pourquoi le fichier separe gagne : clarte, reutilisation, moins de panique. Note le chemin exact de ton `style.css` - tu en auras besoin jusqu'au mini-projet.
