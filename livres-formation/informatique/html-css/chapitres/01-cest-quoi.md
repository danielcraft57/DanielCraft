# Chapitre 1 - Salut, c'est quoi une page web ?

Imagine une maison.

Le HTML, c'est les murs, les pieces, les portes. La structure.
Le CSS, c'est la peinture, les rideaux, les couleurs. L'apparence.

Sans HTML, y'a rien a regarder.
Sans CSS, ca marche, mais c'est moche. Genre page blanche avec du texte noir. Pas super sexy.

## Le navigateur

Quand tu ouvres Chrome, Firefox, Edge ou Safari, tu lances un navigateur.
C'est lui qui lit ton code et te montre la page.

Tu ecris du texte special (le code).
Le navigateur le transforme en page.

## HTML et CSS, deux roles

Le HTML dit : "ici un titre", "ici une image", "ici un bouton". Le CSS, lui, dit : "ce titre est grand et bleu", "cette image a des bords ronds".

Les deux marchent ensemble. Toujours.

## Pourquoi commencer par ca ?

Parce que presque tout le web repose la-dessus.
Les sites, les blogs, les boutiques... Au fond, y'a du HTML et du CSS.

Tu apprendras d'autres trucs plus tard (JavaScript, etc.).
Mais d'abord : les bases. Solides.

## Ce que tu vas savoir faire a la fin

A la fin de ce livre, tu sauras creer une vraie page web. Tu pourras y mettre du texte, des images et des liens, puis changer les couleurs et les polices. Tu apprendras aussi a ranger les blocs proprement, et tu construiras une petite page perso a toi.

Pas besoin d'etre un genie.
Juste de la curiosite et un peu de patience.

Allez, on attaque.

## Erreur classique

Penser que le HTML sert a rendre une page jolie. Beaucoup de debutants cherchent comment "mettre du bleu" directement dans le HTML. La couleur, c'est le job du CSS.

Mauvais reflexe : melanger les deux roles des le depart.

Bon reflexe : d'abord une page HTML simple, puis on ajoute le CSS pour la forme.

## Exemple complet

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Structure vs style</title>
  <!-- Le CSS habille la page -->
  <style>
    body {
      font-family: sans-serif;
      background: #f0f0f0;
      margin: 0;
      padding: 20px;
    }
    h1 { color: #1a5f4a; }
    .carte {
      background: white;
      padding: 16px;
      border-radius: 8px;
    }
  </style>
</head>
<body>
  <!-- Le HTML structure le contenu -->
  <div class="carte">
    <h1>Ma page</h1>
    <p>Ici le HTML dit : c'est un titre, c'est un paragraphe.</p>
    <p>Le CSS dit : fond gris clair, titre vert, carte blanche.</p>
  </div>
</body>
</html>
```

## Mini defi

Ouvre un site que tu visites souvent. Fais un clic droit, puis Inspecter (ou appuie sur F12). Clique sur une ligne de HTML dans l'inspecteur, et repere une regle CSS associee dans le panneau de droite. Note une chose structuree en HTML et une chose stylee en CSS. C'est deja de la vraie lecture de code.

## A retenir

HTML, c'est les murs et les pieces : la structure. CSS, c'est la peinture et la deco : l'apparence. Le navigateur transforme ton code en page visible, et les deux travaillent toujours ensemble. Pas besoin d'etre expert pour commencer.


## En vrai, sur le terrain

Prends 10 minutes. Refais l'exemple du chapitre sans regarder.
Si tu bloques, relis juste la partie qui coinçe. Puis repars.

Le but c'est pas de memoriser. C'est de reconnaitre le motif la prochaine fois.

## Mini defi

Ecris 3 lignes de notes a toi-meme :
1. ce que tu as compris
2. ce qui reste flou
3. un truc a retester demain

Garde ces notes. Elles valent plus qu'un long cours jamais relu.
