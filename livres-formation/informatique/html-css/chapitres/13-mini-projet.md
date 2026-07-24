# Chapitre 13 - Mini-projet : ta page perso

On assemble tout. Une page sur toi (ou un perso invente, libre a toi).

## Objectif

Une page unique `index.html` + `style.css`. Tu y mets un en-tete avec ton nom et un petit menu, une section "A propos", une section "Ce que j'aime" (en liste), une image, un petit formulaire de contact, et un pied de page. Une seule page, mais complete.

## Structure HTML proposee

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

## CSS de demarrage (a personnaliser)

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

.menu {
  display: flex;
  gap: 1rem;
}

.menu a { color: white; }

.conteneur {
  width: min(100% - 2rem, 720px);
  margin: 2rem auto;
}

img {
  max-width: 100%;
  height: auto;
  border-radius: 12px;
}

form {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

input, textarea, button {
  font: inherit;
  padding: 0.6rem 0.8rem;
}

button {
  background: #1f6f5b;
  color: white;
  border: 0;
  border-radius: 8px;
  cursor: pointer;
}

.pied {
  text-align: center;
  padding: 2rem;
  color: #555;
}

@media (max-width: 600px) {
  .entete { flex-direction: column; gap: 0.75rem; }
  .menu { flex-direction: column; align-items: center; }
}
```

## Criteres de reussite

La page s'ouvre sans erreur visible. Le menu saute bien aux sections (`#apropos` et les autres). C'est lisible sur petite largeur. Et surtout : tes couleurs a toi. Change le vert si tu veux, c'est ton terrain.

## Bonus

Ajoute une deuxieme page `projets.html`, relie les deux avec des liens, et mets trois "projets" inventes dans une liste. Quand c'est fait, tu as une vraie mini vitrine.
Pas parfaite. Mais a toi. C'est le plus important.


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
