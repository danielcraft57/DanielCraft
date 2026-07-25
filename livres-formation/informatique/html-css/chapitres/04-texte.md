# Chapitre 4 - Titres, textes, paragraphes

Le texte, c'est le coeur de presque toutes les pages. Boutique, blog, page artisan, fiche de cours : on lit. Si le texte est un mur, on fuit. Si les titres sont dans le desordre, on se perd. Chez DanielCraft, on traite le texte HTML comme un plan de redaction : un sujet clair, des parties, des sous-parties, des phrases qui respirent. Lea coupe les murs chez ses clients. Max a appris a faire trois petits blocs au lieu d'un roman. Sam interdit les sauts de niveaux "parce que c'est joli".

Les titres vont de **`h1`** a **`h6`**. Regle simple : un seul `h1` par page (le sujet principal). Ensuite des `h2` pour les parties, des `h3` pour les sous-parties. C'est comme un sommaire. Ca aide le lecteur. Ca aide aussi Google. Mais surtout, ca aide toi a penser clair avant de styler. En 2026, quand quelqu'un dit "ma page est bien structuree", il parle souvent de ce plan. Derriere, il y a du SEO et de l'accessibilite. Pour toi, le geste reste humain : ecrire pour qu'on comprenne. Tu restes le pilote. Le plan guide.

:::retenir
Un seul `h1` par page. Ensuite `h2`, puis `h3`. Le plan avant la taille.
:::

## Ce que ce n'est pas

Ce n'est pas "choisir h1 parce que c'est plus gros". La taille, c'est le job du CSS. Ce n'est pas non plus un seul paragraphe geant de quarante lignes. Ce n'est pas du gras partout : si tout est important, plus rien ne l'est. Ce n'est pas non plus du texte copie-colle depuis Word avec des styles caches : tu repars propre en HTML, phrase par phrase.

Ce n'est pas "personne ne voit la structure". Les lecteurs d'ecran la lisent. Google la lit. Toi dans six mois, tu la liras aussi quand tu devras corriger une page client. Lea dit : "le plan HTML, c'est ta table des matieres invisible".

Imagine un livre. Le titre du livre, c'est le `h1`. Les chapitres, ce sont les `h2`. Les sous-parties, les `h3`. Les paragraphes portent les idees. Le gras et l'italique soulignent, ils ne remplacent pas le plan. Si tu sautes des niveaux juste pour la taille, tu ecris un livre dont la table des matieres ment. Le lecteur humain peut s'en sortir. La machine, elle, perd le fil. Sam dessine un sommaire au tableau avant chaque exo de texte. Max a arrete les `<br><br><br>` le jour ou sa page mobile est devenue un desert blanc.

## Les titres en pratique

```html
<h1>Le plus grand</h1>
<h2>Un cran en dessous</h2>
<h3>Encore un peu plus petit</h3>
```

Un `h1` = le sujet de la page. Des `h2` = les grandes sections. Des `h3` = les details sous une section. Tu peux descendre jusqu'a `h6`, mais rarement besoin au debut. Si tu hesites entre `h2` et `h3`, demande-toi : est-ce une partie ou un detail de la partie ? Lea pose cette question a voix haute avant de coder. Sam l'exige en copie.

## Les paragraphes

```html
<p>Une idee par paragraphe, c'est souvent plus clair.</p>
<p>Tu peux en mettre plusieurs a la suite.</p>
```

Coupe. Respire. Lis a voix haute si besoin. Une page web n'est pas un SMS interminable. Elle n'est pas non plus un memoire universitaire. Elle est un chemin pour un humain presse. Trois phrases par paragraphe, souvent, c'est deja bien. Max a divise sa page "services" en six petits blocs : les clients ont enfin lu jusqu'au bout. Chez DanielCraft, on aime les pages qui respirent.

## Gras, italique, et cie

```html
<p>Voici un mot <strong>important</strong>.</p>
<p>Voici un mot <em>en emphase</em> (souvent en italique).</p>
<p>Un <mark>surlignage</mark> pour attirer l'oeil.</p>
```

`strong` = vraiment important. `em` = on insiste un peu. Utilise-les avec parcimonie. Lea dit a ses clients : "trois mots en strong max par paragraphe, sinon on crie partout". Le CSS pourra grossir un titre ; le HTML dit pourquoi il est un titre. Sam raye le gras excessif au stylo rouge sur les copies papier.

## Citations et code

```html
<blockquote>
  Une citation un peu longue.
</blockquote>
<p>En ligne, on peut citer <code>du code</code>.</p>
```

`code` est pratique quand tu expliques une balise dans une phrase. `blockquote` dit : ceci est cite, pas ton propos principal. Sam les utilise pour des definitions courtes en cours. Lea pour un avis client. Max pour une phrase du fabricant sur ses materiaux. Trois usages, une meme idee : marquer la difference entre ta voix et une autre voix.

## Commentaires (pour toi, pas pour le visiteur)

```html
<!-- Ceci ne s'affiche pas sur la page -->
```

Utile pour te laisser des notes, ou desactiver un bout sans l'effacer. Max commente les sections "a revoir" avant d'envoyer a un neveu qui l'aide. Sam demande aux eleves de commenter leur intention : `<!-- section horaires -->`. Lea commente les zones fragiles avant une livraison. Le commentaire est un post-it invisible. Utilise-le.

## Petite histoire

Lea a repris une page "services" ou chaque sous-titre etait un `h1` parce que le client voulait "que ca claque". Resultat : bruyant pour les lecteurs d'ecran, confus pour le SEO, et moche a corriger. Elle a remis un `h1`, des `h2`, et grossi en CSS. Meme look voulu. Meilleure structure. Le client n'a rien perdu. La page a gagne.

Max avait empile des `<br><br><br>` pour "faire des paragraphes". Sur mobile, c'etait un desert blanc. Sam lui a montre les vrais `<p>`. Meme contenu, meilleure respiration. Lea dit souvent : "si tu mets trois br de suite, tu cherches probablement un paragraphe". Trois scenes, une hygiene.

:::attention
Ne saute pas de `h1` a `h4` "parce que c'est plus petit". Utilise le bon niveau, puis stylise en CSS.
:::

## Erreur classique

Sauter de `h1` a `h4` sans raison. Tout mettre en `strong`. Utiliser `<br><br><br>` pour "faire des paragraphes" au lieu de vrais `<p>`. Ou croire que le plan HTML, "personne ne le voit". Si, beaucoup le voient autrement : clavier, lecteur d'ecran, moteur de recherche, toi dans six mois. Autre piege : un mur de texte sans titres. Coupe. Titre. Respire.

## En vrai

Ouvre ta page. Ecris "Ma journee" avec un `h1`, trois `h2` (matin, apres-midi, soir), un petit paragraphe sous chaque. Relis. Si tu peines a respirer, coupe encore. Puis ajoute un `blockquote` avec une phrase que quelqu'un t'a dit aujourd'hui. Tu vois la difference entre ton texte et une citation. Sauvegarde. F5. Montre a quelqu'un si tu peux.

## A toi

Ajoute sous chaque partie un mot en `strong` et une phrase avec `em`. Puis enleve le gras partout sauf un seul mot par section. Observe comme la page devient plus calme. Note ce que tu preferes. C'est ton gout qui se forme - DanielCraft adore ca. Garde cette page : tu la styliseras bientot, et tu seras content d'avoir un plan propre a habiller.
