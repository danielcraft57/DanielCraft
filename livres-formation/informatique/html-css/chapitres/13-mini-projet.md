# Chapitre 13 - Mini-projet : ta page perso

On assemble tout ce que tu as appris. Une page sur toi - ou un personnage invente si tu preferes rester discret. L'objectif est concret : une page unique avec `index.html` et `style.css`, un en-tete et un menu, une section "A propos", une section "Ce que j'aime" en liste, une image, un formulaire contact, un pied de page. Une seule page, mais complete. Pas un examen piege. Une preuve que les pieces collent entre elles.

Chez DanielCraft, le mini-projet n'est pas la ou tu dois impressionner avec des effets fous. C'est la ou tu livres une version 1 honnete : structure vraie, style separe, telephone inclus, contenu a toi. Lea fait ce genre de page en version client chaque mois. Max a fait la sienne pour son activite d'artisan et l'a montree a sa famille. Sam demande la meme structure a toute la classe pour comparer les gouts. En 2026, quand quelqu'un dit "j'ai fait ma page perso", il parle souvent de ca. Tu livres aujourd'hui. Tu ameliores demain. Tu restes le pilote.

:::retenir
Version 1 livrable bat maquette eternelle. Solide d'abord. Wow ensuite.
:::

## Ce que ce n'est pas

Ce n'est pas un site de vingt pages avec blog, boutique et espace membre. Ce n'est pas du JavaScript pour l'instant. Ce n'est pas "parfait ou rien" : si tu attends la perfection, tu ne publies jamais, meme en local. C'est livrable, lisible, a toi. Une vitrine d'une piece, pas un chateau entier. Lea dit : "version 1 qui existe bat version 12 dans ta tete".

Imagine une vitrine avec une seule piece visible. On entre par le **header**. On lit qui tu es dans "A propos". On decouvre ce que tu aimes. On peut t'ecrire via le formulaire. On sort par le **footer**. Le menu saute aux sections avec des ancres `#apropos`, `#likes`, `#contact`. Le CSS tient sur telephone. Tes couleurs, pas celles du voisin. Max compare a un meuble : "imparfait, mais a moi". Sam vote pour la page la plus claire, pas la plus chargee.

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Ma page perso</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header class="entete">
    <strong>Ton Prenom</strong>
    <nav class="menu">
      <a href="#apropos">A propos</a>
      <a href="#likes">J'aime</a>
      <a href="#contact">Contact</a>
    </nav>
  </header>
  <main class="conteneur">
    <section id="apropos">
      <h1>Salut, moi c'est ...</h1>
      <p>Deux ou trois phrases sur toi.</p>
      <img src="images/moi.jpg" alt="Photo de ...">
    </section>
    <section id="likes">
      <h2>Ce que j'aime</h2>
      <ul>
        <li>...</li>
        <li>...</li>
        <li>...</li>
      </ul>
    </section>
    <section id="contact">
      <h2>Me contacter</h2>
      <form action="#" method="post">
        <label for="nom">Nom</label>
        <input id="nom" name="nom" type="text" required>
        <label for="email">Email</label>
        <input id="email" name="email" type="email" required>
        <label for="msg">Message</label>
        <textarea id="msg" name="msg" rows="4"></textarea>
        <button type="submit">Envoyer</button>
      </form>
    </section>
  </main>
  <footer class="pied">
    <p>Fait avec HTML et CSS. Et un peu de cafe.</p>
  </footer>
</body>
</html>
```

```css
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: Georgia, serif;
  font-size: 18px;
  line-height: 1.6;
  color: #222;
  background: #f4f1ec;
}
.entete {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 1.5rem;
  background: #1f6f5b;
  color: white;
}
.menu { display: flex; gap: 1rem; }
.menu a { color: white; }
.conteneur { width: min(100% - 2rem, 720px); margin: 2rem auto; }
img { max-width: 100%; height: auto; border-radius: 12px; }
form { display: flex; flex-direction: column; gap: 0.5rem; }
input, textarea, button { font: inherit; padding: 0.6rem 0.8rem; }
button {
  background: #1f6f5b; color: white; border: 0;
  border-radius: 8px; cursor: pointer;
}
.pied { text-align: center; padding: 2rem; color: #555; }
@media (max-width: 600px) {
  .entete { flex-direction: column; gap: 0.75rem; }
  .menu { flex-direction: column; align-items: center; }
}
```

Adapte les couleurs. Remplace les textes. Mets ta photo. C'est ton chantier, pas une copie morte du livre.

## Criteres de reussite

Ta page s'ouvre sans erreur visible. Le menu saute aux bonnes sections. C'est lisible sur petite largeur. Tes couleurs sont les tiennes. Les labels du formulaire sont presents. L'image a un vrai **`alt`**. Le **viewport** est dans le head. Le CSS est dans un fichier separe. Chez DanielCraft, ces criteres battent n'importe quel effet wow.

:::astuce
Construis en une soiree. Pas dix. Livre une version 1. Ameliore demain. C'est le rythme DanielCraft : petit, souvent, proprement.
:::

## Petite histoire

Lea demande toujours "montre-moi sur telephone" avant "montre-moi le code". Max a copie le squelette, change les textes, mis sa photo de chantier, et a envoye le dossier a son neveu avec fierte. Sam affiche trois pages perso anonymisees et fait voter pour la plus claire, pas la plus chargee. La clarte gagne presque toujours. Trois scenes, une lecon : livre, montre, ameliore.

## Erreur classique

Tout coller dans un seul fichier HTML avec les styles en ligne. Oublier les `id` des ancres. Image introuvable. Formulaire sans labels. Ne pas tester sous 600px. Viser le wow avant le socle. Autre piege : dix soirees de peaufinage sans jamais dire "c'est une v1". Lea chronometre parfois : "ce soir, tu livres".

## En vrai

Construis la page en une soiree. Pas dix soirees espacees. Livre une version 1 complete. Ameliore demain avec un seul point (contraste, menu mobile, ou `alt` plus precis). Une version honnete bat une maquette eternelle jamais montree. Ouvre-la sur telephone si tu peux. Souris. C'est a toi.

## A toi

Construis ta page perso maintenant. Bonus si tu veux : ajoute un second fichier `projets.html`, relie les deux pages, mets trois projets inventes en liste. Puis ecris trois ameliorations futures. Chez DanielCraft, on aime les versions 1 honnetes plus que les maquettes eternelles. Tu as les outils. Il ne reste que le geste.
