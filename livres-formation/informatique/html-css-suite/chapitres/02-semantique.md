# Chapitre 2 - HTML semantique : donner un sens a la page

Tu peux construire toute une page avec des `div`. Ca marche. Le navigateur affiche. Mais pour un humain qui lit le code, pour un lecteur d'ecran, pour un moteur de recherche, une pile de `div` anonymes, c'est un mur sans portes ni pieces nommees.

Le HTML semantique, c'est nommer les pieces. `header`, `nav`, `main`, `article`, `section`, `footer` (et d'autres). Tu dis ce que c'est, pas seulement "un bloc".

Chez DanielCraft, on traite ca comme le plan d'une boutique : vitrine, rayon, caisse, sortie. Si tout s'appelle "piece", tu te perds. Si chaque zone a un role, la visite devient claire.

## Pourquoi ca compte vraiment

Le navigateur n'a pas besoin de `header` pour afficher un bandeau. Une `div` avec une classe ferait l'affaire pour le CSS. Alors pourquoi s'embeter ?

Parce que le sens voyage. Un lecteur d'ecran peut proposer "aller au contenu principal" grace a `main`. Les titres dans un `article` ont un contexte. Les moteurs comprennent mieux la structure. Toi, dans six mois, tu rouvres le fichier et tu sais ou est le menu sans jouer aux detectives.

Sur une landing, le hero n'est pas "div 1". C'est souvent un `header` ou une `section` claire dans le `main`. Sur un blog, chaque billet est un `article`. Sur une page produit, la fiche peut etre un `article` ou une `section` bien titre.

## Les balises de structure que tu vas utiliser

`header` : en-tete d'une page ou d'une section. Logo, titre du site, parfois le menu. Une page peut avoir plusieurs `header` (un pour la page, un dans un article), mais commence simple : un en-tete de page.

`nav` : navigation principale (ou secondaire). Liens pour se deplacer dans le site. Pas besoin d'envelopper chaque lien isole dans un `nav`. Reserve-le aux menus reels.

`main` : le contenu principal unique de la page. En general, un seul `main` par page. C'est "le coeur" : pas le menu global, pas le pied, pas la pub laterale.

`article` : un contenu qui tient tout seul (billet de blog, carte produit riche, commentaire autonome). Si tu peux l'imaginer extrait et encore comprehensible, `article` colle souvent.

`section` : un regroupement thematique avec souvent un titre. Sur une landing : section "Services", section "Temoignages", section "Contact". Ce n'est pas un `div` deplus : c'est un chapitre dans la page.

`footer` : pied de page ou pied d'un article. Mentions, liens secondaires, copyright. Comme `header`, il peut vivre a plusieurs niveaux, mais un pied de site suffit au debut.

`aside` : contenu a cote, complementaire (encart "A lire aussi", infos secondaires). Pas obligatoire partout. Utile des que tu as une vraie colonne laterale.

## Une page blog, version semantique

```html
<body>
  <header>
    <p class="logo">Mon Blog</p>
    <nav aria-label="Principale">
      <a href="/">Accueil</a>
      <a href="/articles">Articles</a>
    </nav>
  </header>

  <main>
    <article>
      <h1>Titre du billet</h1>
      <p>Intro du texte...</p>
    </article>
  </main>

  <aside>
    <h2>A lire aussi</h2>
    <ul>
      <li><a href="#">Autre billet</a></li>
    </ul>
  </aside>

  <footer>
    <p>Contact - Mentions</p>
  </footer>
</body>
```

Tu vois deja le plan. Le CSS viendra poser Grid ou Flex dessus. Le sens est la avant la peinture.

## Landing simple

Sur une landing atelier, tu peux faire :

```html
<header>
  <p class="marque">Atelier Ceramique</p>
  <nav>...</nav>
</header>
<main>
  <section class="hero">
    <h1>Apprends la terre en un week-end</h1>
    <p>Petit groupe, vrai four, vrai fun.</p>
    <a class="bouton" href="#inscription">Je m'inscris</a>
  </section>
  <section id="programme">
    <h2>Programme</h2>
    ...
  </section>
</main>
<footer>...</footer>
```

Le `h1` reste unique et fort. Les `h2` portent les sections. Tu ne sautes pas de `h1` a `h3` sans raison.

## Carte produit

Une grille de cartes peut etre une liste d'`article` :

```html
<main>
  <h1>Nos cafes</h1>
  <div class="grille">
    <article class="carte">
      <h2>Blend maison</h2>
      <p>Notes de cacao.</p>
      <p class="prix">9,90 €</p>
    </article>
  </div>
</main>
```

Le `div.grille` sert au layout CSS. Les `article` portent le sens de chaque produit.

## Ce que ce n'est pas

Ce n'est pas une religion. Tu auras encore des `div` et des `span` pour le style ou les petits morceaux. L'idee : les zones importantes de la page ont un nom utile. Si tout est `section` ou tout est `article` sans reflechir, tu n'as gagne que du bruit.

`div` = boite neutre. Semantique = boite qui dit son role.

## Erreur classique

Mettre trois `main` sur la meme page. Ou envelopper tout le body dans un seul `section` geant sans titre. Ou utiliser `header` uniquement parce que "ca fait pro", puis y coller le contenu principal entier.

Autre piege : confondre `nav` et une liste de liens sociaux dans le pied. Un groupe de liens peut rester une liste dans le `footer` sans `nav`, ou avec un `nav` clairement libelle si c'est vraiment de la navigation.

## En vrai

Prends une de tes pages. Remplace mentalement (puis dans le code) les gros `div` par `header`, `main`, `footer`. Ajoute `nav` autour du vrai menu. Si tu as un billet ou une fiche, tente `article`. Recharge. Visuellement, rien ne change si le CSS ciblait des classes. Structurellement, la page respire mieux.

Ouvre ensuite l'inspecteur : l'arbre DOM se lit comme un sommaire.

## A toi

Recree une mini page "Produit" en HTML seul (presque pas de CSS). `header` avec nom de boutique + `nav`, `main` avec un `article` produit (titre, paragraphe, prix), `footer` avec une ligne de contact. Valide que tu as un seul `h1` et un seul `main`.
