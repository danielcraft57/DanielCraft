# Chapitre 2 - HTML semantique : donner un sens a la page

Tu peux construire toute une page avec des `div`. Ca marche. Le navigateur affiche. Mais pour un humain qui lit le code, pour un lecteur d'ecran, pour un moteur de recherche, une pile de `div` anonymes, c'est un mur sans portes ni pieces nommees. Le HTML **semantique**, c'est nommer les pieces. `header`, `nav`, `main`, `article`, `section`, `footer` (et d'autres). Tu dis ce que c'est, pas seulement "un bloc".

Chez DanielCraft, on traite ca comme le plan d'une boutique : vitrine, rayon, caisse, sortie. Si tout s'appelle "piece", tu te perds. Si chaque zone a un role, la visite devient claire. Lea ouvre un fichier client six mois plus tard et retrouve le menu sans jouer aux detectives. Max comprend mieux sa page quand "entete / contenu / pied" sont des balises, pas des classes mysterieuses. Sam force ses eleves a expliquer la page a voix haute avec les noms de balises : si ca sonne juste, la structure tient.

## Pourquoi ca compte vraiment

Le navigateur n'a pas besoin de `header` pour afficher un bandeau. Une `div` avec une classe ferait l'affaire pour le CSS. Alors pourquoi s'embeter ? Parce que le sens voyage. Un lecteur d'ecran peut proposer "aller au contenu principal" grace a `main`. Les titres dans un `article` ont un contexte. Les moteurs comprennent mieux la structure. Toi, dans six mois, tu rouvres le fichier et tu sais ou est le menu.

Sur une landing, le hero n'est pas "div 1". C'est souvent un `header` ou une `section` claire dans le `main`. Sur un blog, chaque billet est un `article`. Sur une page produit, la fiche peut etre un `article` ou une `section` bien titree. Le CSS viendra poser Grid ou Flex dessus. Le sens est la avant la peinture.

:::astuce
Avant de styler, lis ton HTML a voix haute : "en-tete, menu, contenu principal, article, pied". Si ca sonne comme un sommaire, tu es sur la bonne voie.
:::

## Les balises de structure que tu vas utiliser

`header` : en-tete d'une page ou d'une section (logo, titre, parfois le menu). Commence simple : un en-tete de page. `nav` : menus reels, pas chaque lien isole. `main` : le contenu principal unique - en general un seul par page. `article` : un contenu qui tient tout seul (billet, fiche produit). `section` : regroupement thematique avec souvent un titre (Services, Contact...). `footer` : pied de page ou d'article. `aside` : contenu complementaire a cote. Pas obligatoire partout.

Tu auras encore des `div` pour le layout neutre. Semantique = nommer les zones importantes. Si tout est `section` sans reflechir, tu n'as gagne que du bruit.

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

Le `h1` reste unique et fort. Les `h2` portent les sections. Tu ne sautes pas de `h1` a `h3` sans raison. Lea livre souvent ce squelette avant toute couleur. Max le reconnait : "c'est comme afficher clairement l'entree, le comptoir, la sortie".

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

Le `div.grille` sert au layout CSS. Les `article` portent le sens de chaque produit. `div` = boite neutre. Semantique = boite qui dit son role.

## Ce que ce n'est pas

Ce n'est pas une religion ni "ca fait pro donc j'enveloppe tout le body dans un `section` geant". Un nom sans role clair = bruit.

## Petite histoire

Sam a demande a un eleve de decrire sa page sans regarder l'ecran. L'eleve a dit "plein de divs". Ils ont renomme : `header`, `main`, deux `article`, `footer`. Meme CSS. L'oral est devenu clair en trente secondes. Lea a vecu le meme moment avec un client qui voulait "juste changer le menu" : avec un vrai `nav`, la cible etait evidente. Max a remplace son bandeau `div.haut` par un `header` et a soudain retrouve ou coller le telephone.

:::attention
Trois `main` sur la meme page, ou un `header` qui avale tout le contenu principal : tu gagnes du jargon, tu perds le sens. Un `main`, un `h1` fort, des zones nommees avec intention.
:::

## Erreur classique

Mettre trois `main` sur la meme page. Ou envelopper tout le body dans un seul `section` geant sans titre. Ou utiliser `header` uniquement parce que "ca fait pro", puis y coller le contenu principal entier. Autre piege : confondre `nav` et une liste de liens sociaux dans le pied. Un groupe de liens peut rester une liste dans le `footer` sans `nav`, ou avec un `nav` clairement libelle si c'est vraiment de la navigation.

## En vrai

Prends une de tes pages. Remplace mentalement (puis dans le code) les gros `div` par `header`, `main`, `footer`. Ajoute `nav` autour du vrai menu. Si tu as un billet ou une fiche, tente `article`. Recharge. Visuellement, rien ne change si le CSS ciblait des classes. Structurellement, la page respire mieux.

Ouvre ensuite l'inspecteur : l'arbre DOM se lit comme un sommaire. C'est exactement ce que tu veux pour la suite (Grid, accessibilite, debug).

## A toi

Recree une mini page "Produit" en HTML seul (presque pas de CSS). `header` avec nom de boutique + `nav`, `main` avec un `article` produit (titre, paragraphe, prix), `footer` avec une ligne de contact. Valide que tu as un seul `h1` et un seul `main`.

:::retenir
Semantique = nommer les pieces. Un `main`, un `h1` fort. Les `div` restent pour le neutre. Le sens avant la peinture.
:::
