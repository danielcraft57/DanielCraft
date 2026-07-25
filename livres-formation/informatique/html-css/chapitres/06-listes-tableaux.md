# Chapitre 6 - Listes et tableaux

Des listes partout : courses, etapes, menus, avantages produit. Des tableaux quand tu compares vraiment des infos en lignes et colonnes. Les deux structurent. Ils ne "decorent" pas. Chez DanielCraft, on les enseigne tot parce qu'ils sauvent des pages confuses : au lieu d'un paragraphe qui enumere vingt choses, tu ranges. Lea utilise des listes pour les livrables client. Max met ses horaires en tableau simple. Sam force les eleves a choisir liste ou tableau avant d'ecrire.

Une liste a puces (**`ul`** + **`li`**) dit : voici des elements sans ordre strict. Une liste numerotee (**`ol`** + `li`) dit : l'ordre compte - des etapes. Un **tableau** (`table`, `tr`, `th`, `td`) dit : ces donnees se croisent. En 2026, quand quelqu'un dit "j'ai structure mon contenu", il parle souvent de ca. Derriere, il y a des composants complexes. Pour toi, la bonne question reste : "quelle forme a l'info ?" Tu restes le pilote. La forme suit le fond.

:::retenir
Ordre libre -> `ul`. Etapes -> `ol`. Donnees croisees -> `table`. Pas de tableau pour la mise en page.
:::

## Ce que ce n'est pas

Ce n'est pas un outil de mise en page generale. Ancienne mauvaise habitude : faire tout le layout avec des tableaux. Aujourd'hui, non - c'est le job du CSS (Flexbox plus loin). Ce n'est pas non plus des listes imbriquees a cinq niveaux "parce que ca a l'air pro". Illisible. Et ce n'est pas un tableau pour trois mots : une liste suffit souvent.

Ce n'est pas non plus des tirets dans un paragraphe a la place d'une vraie liste. Visuellement, ca peut ressembler. Structurellement, le navigateur ne voit pas une liste. Et les lecteurs d'ecran non plus. Lea dit : "si c'est une liste, ecris une liste".

La liste, c'est un carnet a puces. Le tableau, c'est une grille d'emplois du temps. Si tu mets l'emploi du temps en puces, tu perds les croisements. Si tu mets la liste de courses en tableau a dix colonnes, tu te fatigues pour rien. Choisis l'outil selon la forme de l'info. Max dit : "ma liste de materiel, c'est des puces ; mes creneaux dispo, c'est un tableau". Sam dessine les deux formes au tableau avant chaque exo. Les eleves votent. Puis ils codent.

## Liste a puces

```html
<ul>
  <li>Pain</li>
  <li>Lait</li>
  <li>Beurre</li>
</ul>
```

`ul` = unordered list. `li` = list item. Simple, clair, reutilisable. Parfait pour des avantages, des ingredients, des outils sans ordre impose. Lea les utilise pour les "inclus dans le devis". Max pour son materiel de base. Sam pour les objectifs de seance.

## Liste numerotee

```html
<ol>
  <li>Ouvrir l'editeur</li>
  <li>Ecrire le HTML</li>
  <li>Sauvegarder</li>
  <li>Ouvrir dans le navigateur</li>
</ol>
```

Parfait pour des procedures. Lea numerote ses checklists de mise en ligne. Max numerote "devis, chantier, facture". Sam numerote les etapes d'un exercice : l'ordre compte, le `ol` le dit clairement. Si tu peux changer l'ordre sans perdre le sens, c'etait probablement un `ul`.

:::astuce
Avant d'ecrire : "l'ordre compte-t-il ?" Oui -> `ol`. Non -> `ul`. Donnees croisees -> `table`.
:::

## Liste dans une liste

Ca marche. Tu peux imbriquer. Mais n'en abuse pas : au-dela de deux niveaux, le lecteur se noie. Prefere plusieurs listes courtes avec des titres `h2`/`h3`. Lea decoupe les gros projets client en sections avec listes courtes plutot qu'une tour de Pise a puces. Chez DanielCraft, lisible bat impressionnant.

## Les tableaux

```html
<table>
  <thead>
    <tr>
      <th>Langage</th>
      <th>Role</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>HTML</td>
      <td>Structure</td>
    </tr>
    <tr>
      <td>CSS</td>
      <td>Style</td>
    </tr>
  </tbody>
</table>
```

`table` enveloppe. `tr` est une ligne. `th` une cellule d'en-tete. `td` une cellule normale. Tu empiles comme des briques. `thead` / `tbody` clarifient pour toi et pour l'accessibilite. Les `th` disent "c'est un titre de colonne", pas juste du texte en gras par defaut. Max met ses horaires ainsi. Lea ses specs produit. Sam ses notes d'eleves en demo.

## Petite histoire

Max voulait "un joli menu" avec un tableau a une cellule. Ca tenait a peu pres. Puis sur telephone, c'etait l'enfer. Lea lui a dit : liste ou Flexbox, pas tableau. Il a refait. Sam, en classe, montre un tableau HTML vs un layout CSS : meme look possible, intentions differentes. Les eleves retiennent surtout : tableau = donnees, pas deco.

Lea a herite d'un site e-commerce ou les specs produit etaient des paragraphes avec des virgules. Elle a mis un vrai tableau : poids, dimensions, garantie. Les clients ont arrete de poser les memes questions. Structure claire, moins de mails. Trois scenes, une lecon.

:::attention
Ne construis pas ta mise en page avec des tableaux. Tableau = donnees. Layout = CSS.
:::

## Erreur classique

Utiliser un tableau pour centrer un logo. Oublier les `th` et tout mettre en `td` : on perd le sens des en-tetes. Mettre une liste sans `ul`/`ol`, juste des tirets dans un `p` : le navigateur ne voit pas une liste. Ecrire la structure. Croire qu'un tableau "c'est plus pro" pour trois mots : une `ul` suffit. Autre piege : imbriquer cinq niveaux de listes. Coupe. Titre. Respire.

## En vrai

Fais une liste de cinq choses que tu veux apprendre. Puis un petit tableau jour / activite (Lundi / HTML, etc.). Ouvre la page. Si le tableau parait trop large, c'est normal : on stylera plus tard. La, valide la structure. Relis a voix haute : est-ce que l'ordre de ta liste numerotee a du sens ? Si non, passe en `ul`.

## A toi

Cree une page "Ma semaine" avec un `h1`, une liste d'objectifs, et un tableau de trois jours. Ajoute une phrase sous le tableau qui explique pourquoi tu as choisi tableau et pas liste. Cette phrase force le jugement - competence DanielCraft. Garde-la : tu la reliras au mini-projet quand tu choisiras quoi mettre ou.
